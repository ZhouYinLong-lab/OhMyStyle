#!/usr/bin/env python3
"""Shared loader and compiler primitives for executable Style Packages."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"Expected a YAML object: {path}")
    return data


def resolve_package(path: Path) -> Path:
    path = path.resolve()
    if path.is_file() and path.name == "package.yaml":
        return path.parent
    if (path / "package.yaml").is_file():
        return path
    raise FileNotFoundError(f"No package.yaml found at {path}")


def load_package(path: Path) -> dict[str, Any]:
    root = resolve_package(path)
    package = load_yaml(root / "package.yaml")
    files = package.get("files", {})

    def file_from(key: str, fallback: str) -> Path:
        relative = str(files.get(key, fallback))
        return root / relative

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
        "base_prompt": (root / "prompts/base.txt").read_text(encoding="utf-8").strip(),
        "negative_prompt": (root / "prompts/negative.txt").read_text(encoding="utf-8").strip(),
    }


def manifest_records(runtime: dict[str, Any]) -> list[dict[str, str]]:
    import csv

    manifest = runtime["root"] / "references/manifest.csv"
    with manifest.open(encoding="utf-8", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def choose_pair(runtime: dict[str, Any], pair_id: str | None = None) -> dict[str, Any]:
    pairs = runtime["palette"].get("pairs", [])
    if not pairs:
        raise ValueError("Palette has no pairs")
    if pair_id is None:
        return pairs[0]
    for pair in pairs:
        if pair.get("id") == pair_id:
            return pair
    available = ", ".join(str(pair.get("id")) for pair in pairs)
    raise ValueError(f"Unknown palette pair {pair_id!r}; available: {available}")


def select_references(
    runtime: dict[str, Any], pair: dict[str, Any], reference_set: str = "palette"
) -> list[dict[str, str]]:
    rows = {row.get("asset_id", ""): row for row in manifest_records(runtime)}
    selected: list[dict[str, str]] = []
    selected_ids = set(str(item) for item in pair.get("reference_asset_ids", []))

    if reference_set in {"palette", "all"}:
        selected.extend(rows[asset_id] for asset_id in selected_ids if asset_id in rows)
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
        asset = runtime["root"] / relative
        if not asset.is_file():
            raise FileNotFoundError(f"Manifest asset does not exist: {asset}")
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
    pair: dict[str, Any],
    profile: str = "generic",
) -> tuple[str, str]:
    base = runtime["base_prompt"].replace("[SUBJECT]", subject)
    negative = runtime["negative_prompt"]
    exact = pair_line(pair)
    if profile == "weak":
        prompt = "\n".join(
            [
                f"SUBJECT: {subject}",
                "STYLE TASK: Follow the color assignment exactly; do not reinterpret the subject as a flower arrangement.",
                exact,
                "MUST: keep the dominant and counter colors separate; preserve the specified background; use only restrained neutral support colors.",
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
) -> dict[str, Any]:
    runtime = load_package(package_path)
    package = runtime["package"]
    pair = choose_pair(runtime, pair_id)
    references = select_references(runtime, pair, reference_set)
    prompt, negative = compile_prompt(runtime, subject, pair, profile)
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
        "constraints": {
            "area_ratio": runtime["reproduction"].get("area_ratio", {}),
            "profiles": runtime["evaluation"].get("profiles", {}),
        },
        "provenance": {
            "source_policy": runtime["provenance"].get("source_policy", ""),
            "reference_usage": "Reference images are inputs to the render job; they are not silently inferred.",
        },
    }
