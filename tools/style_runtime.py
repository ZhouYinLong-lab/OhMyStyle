#!/usr/bin/env python3
"""Shared loader and compiler primitives for executable Style Packages."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from safe_yaml import safe_load


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected a YAML object: {path}")
    return data


def safe_package_file(root: Path, relative: str, *, label: str = "package file") -> Path:
    """Resolve a package-relative file without allowing traversal or symlinks out."""
    if not isinstance(relative, str) or not relative.strip():
        raise ValueError(f"{label} must be a non-empty relative path")
    if Path(relative).is_absolute():
        raise ValueError(f"{label} must be relative: {relative!r}")
    package_root = root.resolve()
    candidate = (package_root / relative).resolve()
    try:
        candidate.relative_to(package_root)
    except ValueError as exc:
        raise ValueError(f"{label} escapes package root: {relative!r}") from exc
    if not candidate.is_file():
        raise FileNotFoundError(f"{label} does not exist: {candidate}")
    return candidate


def resolve_package(path: Path) -> Path:
    path = path.resolve()
    if path.is_file() and path.name == "package.yaml":
        return path.parent
    if (path / "package.yaml").is_file():
        return path
    raise FileNotFoundError(f"No package.yaml found at {path}")


def load_package(path: Path) -> dict[str, Any]:
    root = resolve_package(path)
    package = load_yaml(safe_package_file(root, "package.yaml", label="package manifest"))
    files = package.get("files", {})
    if not isinstance(files, dict):
        raise ValueError("package.files must be an object")

    def file_from(key: str, fallback: str) -> Path:
        relative = str(files.get(key, fallback))
        return safe_package_file(root, relative, label=f"package files.{key}")

    palette_path = file_from("palette", "palette/palette.json")
    with palette_path.open(encoding="utf-8") as handle:
        palette = json.load(handle)
    return {
        "root": root,
        "package": package,
        "identity": load_yaml(file_from("identity", "identity.yaml")),
        "visual_signature": load_yaml(file_from("visual_signature", "visual-signature.yaml")),
        "reproduction": load_yaml(file_from("reproduction", "reproduction.yaml")),
        "relations": load_yaml(file_from("relations", "relations.yaml")),
        "evaluation": load_yaml(file_from("evaluation", "evaluation.yaml")),
        "provenance": load_yaml(file_from("provenance", "provenance.yaml")),
        "palette": palette,
        "base_prompt": safe_package_file(root, "prompts/base.txt", label="base prompt").read_text(encoding="utf-8").strip(),
        "negative_prompt": safe_package_file(root, "prompts/negative.txt", label="negative prompt").read_text(encoding="utf-8").strip(),
    }


def manifest_records(runtime: dict[str, Any]) -> list[dict[str, str]]:
    import csv

    manifest = safe_package_file(runtime["root"], "references/manifest.csv", label="reference manifest")
    with manifest.open(encoding="utf-8", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]
    seen: set[str] = set()
    for row in rows:
        asset_id = row.get("asset_id", "").strip()
        if not asset_id:
            raise ValueError("Reference manifest contains a row without asset_id")
        if asset_id in seen:
            raise ValueError(f"Reference manifest contains duplicate asset_id: {asset_id}")
        seen.add(asset_id)
    return rows


def choose_pair(runtime: dict[str, Any], pair_id: str | None = None) -> dict[str, Any] | None:
    pairs = runtime["palette"].get("pairs", [])
    if not pairs:
        if pair_id is not None:
            raise ValueError("This Style Package does not define palette pairs; omit --pair")
        return None
    if pair_id is None:
        return pairs[0]
    for pair in pairs:
        if pair.get("id") == pair_id:
            return pair
    available = ", ".join(str(pair.get("id")) for pair in pairs)
    raise ValueError(f"Unknown palette pair {pair_id!r}; available: {available}")


def select_references(
    runtime: dict[str, Any], pair: dict[str, Any] | None, reference_set: str = "palette"
) -> list[dict[str, str]]:
    rows = {row.get("asset_id", ""): row for row in manifest_records(runtime)}
    selected: list[dict[str, str]] = []
    raw_selected_ids = (pair or {}).get("reference_asset_ids", [])
    if not isinstance(raw_selected_ids, list):
        raise ValueError("reference_asset_ids must be a list")
    selected_ids = set(str(item) for item in raw_selected_ids)
    unknown_ids = sorted(selected_ids - set(rows))
    if unknown_ids:
        raise ValueError("Palette pair references unknown asset_id(s): " + ", ".join(unknown_ids))

    if reference_set in {"palette", "all"}:
        if selected_ids:
            selected.extend(rows[asset_id] for asset_id in selected_ids if asset_id in rows)
        else:
            selected.extend(row for row in rows.values() if row.get("role") == "details")
    if reference_set in {"primary", "all"}:
        selected.extend(row for row in rows.values() if row.get("role") == "primary")
    if reference_set == "details":
        selected.extend(row for row in rows.values() if row.get("role") == "details")

    result: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in selected:
        relative = row.get("local_path", "").strip()
        if not relative or relative in seen:
            continue
        asset = safe_package_file(runtime["root"], relative, label=f"manifest asset {row.get('asset_id', '')}")
        seen.add(relative)
        result.append(
            {
                "asset_id": row.get("asset_id", ""),
                "path": Path(relative).as_posix(),
                "absolute_path": str(asset.resolve()),
                "title": row.get("title", ""),
                "role": row.get("role", ""),
                "source_url": row.get("source_url", ""),
                "usage": "palette_only" if row.get("role") == "details" else "visual_reference",
            }
        )
    return result


def pair_line(pair: dict[str, Any]) -> str:
    dominant, counter = pair["dominant"], pair["counter"]
    return (
        f"Dominant color: {dominant['name']} {dominant['hex']} RGB {dominant['rgb']}; "
        f"counter color: {counter['name']} {counter['hex']} RGB {counter['rgb']}; "
        f"recommended area ratio: {pair.get('recommended_ratio', 'not specified')}."
    )


def compile_prompt(
    runtime: dict[str, Any],
    subject: str,
    pair: dict[str, Any] | None,
    profile: str = "generic",
    variables: dict[str, str] | None = None,
) -> tuple[str, str]:
    template_values = {"SUBJECT": subject, **(variables or {})}
    base = runtime["base_prompt"]
    for key, value in template_values.items():
        base = base.replace(f"[{key}]", value).replace(f"{{{key}}}", value)
    negative = runtime["negative_prompt"]
    exact = pair_line(pair) if pair else "Follow the package-defined visual signature, process, materials, and constraints exactly."
    if profile == "weak":
        prompt = "\n".join(
            [
                f"SUBJECT: {subject}",
                "PACKAGE BASE PROMPT:",
                base,
                "STYLE TASK: Follow the declared package specification exactly; do not substitute an unrequested subject, medium, process, or visual motif.",
                exact,
                "MUST: preserve all declared visual relationships, hierarchy, materials, lighting, perspective, and background behavior.",
                "MUST: keep the requested material, lighting, perspective, and object count; no extra decorative objects.",
                "MUST: use natural material detail without a global color filter.",
            ]
        )
    else:
        prompt = f"{base}\n\nExact package assignment:\n{exact}\nUse any supplied reference images for palette relationship only, not for subject identity or copied composition."
    return prompt, negative


def compile_job(
    package_path: Path,
    subject: str,
    pair_id: str | None = None,
    profile: str = "generic",
    reference_set: str = "palette",
    model: str = "provider-neutral",
    variables: dict[str, str] | None = None,
) -> dict[str, Any]:
    runtime = load_package(package_path)
    package = runtime["package"]
    pair = choose_pair(runtime, pair_id)
    references = select_references(runtime, pair, reference_set)
    prompt, negative = compile_prompt(runtime, subject, pair, profile, variables=variables)
    unresolved = sorted(set(re.findall(r"(?:\[[A-Z][A-Z0-9_]*\]|\{[A-Z][A-Z0-9_]*\})", prompt)))
    return {
        "schema_version": "0.1.0",
        "job_type": "style_render",
        "package": {
            "id": package.get("id"),
            "name": package.get("name"),
            "version": package.get("version"),
            "root": str(runtime["root"]),
        },
        "model": {"name": model, "profile": profile, "adapter": "provider-neutral"},
        "subject": subject,
        "palette_pair": pair,
        "reference_set": reference_set,
        "reference_images": references,
        "prompt": prompt,
        "negative_prompt": negative,
        "template_variables": {"SUBJECT": subject, **(variables or {})},
        "unresolved_placeholders": unresolved,
        "constraints": {
            "area_ratio": runtime["reproduction"].get("area_ratio", {}),
            "profiles": runtime["evaluation"].get("profiles", {}),
        },
        "provenance": {
            "source_policy": runtime["provenance"].get("source_policy", ""),
            "reference_usage": "Reference images are inputs to the render job; they are not silently inferred.",
        },
    }
