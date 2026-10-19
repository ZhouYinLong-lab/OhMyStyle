"""Validate and explicitly compile experimental art directions without rewriting v1."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from safe_yaml import safe_load


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schema/art-direction.schema.json"


def validate_grid(grid: dict[str, Any]) -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    grid_schema = {"$ref": "#/$defs/grid", "$defs": schema["$defs"]}
    problems = list(Draft202012Validator(grid_schema).iter_errors(grid))
    if problems:
        raise ValueError(f"Invalid ASCII grid configuration: {problems[0].message}")
    if grid["margin"] * 2 >= min(grid["width"], grid["height"]):
        raise ValueError("ASCII grid margin leaves no drawable area")
    if grid["foreground"].lower() == grid["background"].lower():
        raise ValueError("ASCII foreground and background must differ")


def load_direction(path: Path, runtime: dict[str, Any]) -> dict[str, Any]:
    """A direction's file and its declared base must both be selected explicitly."""
    from style_runtime import manifest_records, safe_package_file

    path = path.resolve()
    if path.is_dir():
        path = path / "direction.yaml"
    with path.open(encoding="utf-8") as handle:
        data = safe_load(handle)
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    problems = list(Draft202012Validator(schema).iter_errors(data))
    if problems:
        location = ".".join(map(str, problems[0].path)) or "<root>"
        raise ValueError(f"{path}:{location}: {problems[0].message}")
    base_root = runtime["root"].resolve()
    style_root = base_root.parent.parent
    declared = (style_root / data["base_package"]).resolve()
    if declared != base_root or not declared.is_relative_to(style_root):
        raise ValueError("Art direction base_package does not match the selected package")

    def unique_ids(items: list[dict[str, Any]], label: str) -> set[str]:
        ids = [item["id"] for item in items]
        if len(ids) != len(set(ids)):
            raise ValueError(f"Duplicate {label} ID")
        return set(ids)

    rule_ids = unique_ids(data["rules"], "rule")
    source_ids = unique_ids(data["sources"], "source")
    joint_ids = unique_ids(data["joint_checks"], "joint check")
    context_catalog = data.get("contexts")
    if context_catalog is not None:
        context_ids = unique_ids(context_catalog, "context")
        scope_contexts = set(data["scope"]["required_contexts"]) | set(data["scope"]["incompatible_contexts"])
        if not scope_contexts <= context_ids:
            raise ValueError("Scope contexts must be declared in the context catalog")
        for rule in data["rules"]:
            required_contexts = set(rule.get("when_contexts", []))
            excluded_contexts = set(rule.get("unless_contexts", []))
            selected_contexts = required_contexts | excluded_contexts
            if not selected_contexts <= context_ids:
                raise ValueError(f"Rule {rule['id']} references an unknown context")
            if required_contexts & excluded_contexts:
                raise ValueError(f"Rule {rule['id']} both requires and excludes the same context")
    elif any(rule.get("when_contexts") or rule.get("unless_contexts") for rule in data["rules"]):
        raise ValueError("Rule context selectors require a top-level contexts catalog")
    if joint_ids & rule_ids:
        raise ValueError("Rule and joint check IDs must be distinct")
    active = set(data["active_rule_ids"])
    if not active or not active <= rule_ids:
        raise ValueError("active_rule_ids must select known rules")
    core = {rule["id"] for rule in data["rules"] if rule["importance"] == "core"}
    if not core or not core <= active:
        raise ValueError("Every core rule must be active in the authored direction")
    for rule in data["rules"]:
        evidence = set(rule["evidence"]["source_ids"])
        if not evidence or not evidence <= source_ids:
            raise ValueError(f"Rule {rule['id']} references missing evidence")
    for joint in data["joint_checks"]:
        if not joint["rule_ids"] or not set(joint["rule_ids"]) <= active:
            raise ValueError(f"Joint check {joint['id']} must reference active rules")
    scope = data["scope"]
    if set(scope["required_contexts"]) & set(scope["incompatible_contexts"]):
        raise ValueError("A context cannot be both required and incompatible")
    base_sources = {row["asset_id"] for row in manifest_records(runtime)}
    for source in data["sources"]:
        if "base_asset_id" in source and source["base_asset_id"] not in base_sources:
            raise ValueError(f"Unknown base reference: {source['base_asset_id']}")
        if "local_path" in source:
            safe_package_file(base_root, source["local_path"], label="direction source")
    if data["execution"]["route"] == "deterministic_grid":
        validate_grid(data["execution"]["grid"])
    return {"data": data, "path": path, "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}


def compile_direction_job(
    runtime: dict[str, Any],
    path: Path,
    subject: str,
    *,
    contexts: list[str] | None = None,
    reference_set: str = "none",
    pair_id: str | None = None,
    model: str = "provider-neutral",
    profile: str = "generic",
    variables: dict[str, str] | None = None,
) -> dict[str, Any]:
    """Compile curated active instructions, not observations or evidence prose."""
    if reference_set != "none" or pair_id is not None:
        raise ValueError("Experimental directions require references='none' and no legacy palette pair")
    if profile != "generic":
        raise ValueError("Experimental directions currently support profile='generic' only")
    if not isinstance(subject, str) or not subject.strip():
        raise ValueError("A non-empty user subject is required")
    loaded = load_direction(path, runtime)
    data = loaded["data"]
    declared_contexts = set(contexts or [])
    required = set(data["scope"]["required_contexts"])
    if required - declared_contexts:
        raise ValueError("Explicit direction contexts required: " + ", ".join(sorted(required - declared_contexts)))
    conflicts = declared_contexts & set(data["scope"]["incompatible_contexts"])
    if conflicts:
        raise ValueError("Incompatible direction contexts: " + ", ".join(sorted(conflicts)))
    if data.get("contexts") is not None:
        known_contexts = {item["id"] for item in data["contexts"]}
        unknown = declared_contexts - known_contexts
        if unknown:
            raise ValueError("Unknown direction contexts: " + ", ".join(sorted(unknown)))
    variables = variables or {}
    if "SUBJECT" in variables:
        raise ValueError("Direction variables cannot override the user subject")
    active = set(data["active_rule_ids"])

    def applies(rule: dict[str, Any]) -> bool:
        required_contexts = set(rule.get("when_contexts", []))
        excluded_contexts = set(rule.get("unless_contexts", []))
        return (not required_contexts or bool(required_contexts & declared_contexts)) and not (excluded_contexts & declared_contexts)

    rules = [rule for rule in data["rules"] if rule["id"] in active and applies(rule)]
    applicable_ids = {rule["id"] for rule in rules}
    applicable_core = [rule for rule in rules if rule["importance"] == "core"]
    if not applicable_core:
        raise ValueError("No core visual rules apply to the declared direction contexts")
    joint_checks = [
        joint for joint in data["joint_checks"]
        if set(joint["rule_ids"]) <= applicable_ids
    ]
    execution = data["execution"]
    parts = [
        "USER SUBJECT: " + subject.strip(),
        "Preserve the user's requested identities, counts, setting, and layout. Add no default motifs.",
        "VISUAL MEDIUM: " + data["scope"]["medium"],
        "REPRESENTATION: " + data["scope"]["representation"],
    ]
    parts.extend(f"USER DETAIL {key}: {value}" for key, value in sorted(variables.items()))
    parts.append("APPLY THESE AUTHORED VISUAL RULES:")
    parts.extend(f"- [{rule['id']}] {rule['instruction']}" for rule in rules)
    parts.extend(f"- [{joint['id']}] {joint['instruction']}" for joint in joint_checks)
    parts.extend(f"REQUIREMENT: {item}" for item in execution["must"])
    if execution["route"] == "deterministic_grid":
        grid = execution["grid"]
        parts.append(
            f"Return a literal printable-ASCII grid with {grid['rows']} rows and at most "
            f"{grid['columns']} columns per row. Pad missing right-hand cells with spaces. "
            "Every scene shape must be a glyph; rasterize the grid without image-model repainting."
        )
    prompt = "\n".join(parts)
    negative = "\n".join(dict.fromkeys(
        [rule["avoid"] for rule in rules if rule.get("avoid")] + execution["avoid"]
    ))
    package = runtime["package"]
    compiler_files = [ROOT / "tools/style_runtime.py", Path(__file__).resolve()]
    return {
        "schema_version": "0.2.0",
        "job_type": "ascii_grid_construction" if execution["route"] == "deterministic_grid" else "style_render",
        "package": {"id": package["id"], "name": package["name"], "version": package["version"], "root": str(runtime["root"])},
        "model": {"name": model, "profile": profile, "adapter": "provider-neutral"},
        "subject": subject,
        "prompt": prompt,
        "negative_prompt": negative,
        "reference_set": "none",
        "reference_images": [],
        "art_direction": {
            "id": data["id"], "name": data["name"], "schema_version": data["schema_version"],
            "status": "experimental",
            "path": str(loaded["path"]), "sha256": loaded["sha256"],
            "active_rule_ids": data["active_rule_ids"],
            "applicable_rule_ids": [rule["id"] for rule in rules],
            "omitted_context_rule_ids": sorted(active - applicable_ids),
            "contexts": sorted(declared_contexts),
            "applicability": "structured context selectors are enforced; natural-language applies_when conditions are not inferred",
        },
        "execution": execution,
        "review": {
            "status": "pending", "scope": data["scope"], "pillars": data["pillars"], "rules": rules,
            "joint_checks": joint_checks, "sources": data["sources"],
            "note": "Successful compilation is not image-quality validation or a maturity upgrade.",
        },
        "provenance": {
            "direction_sha256": loaded["sha256"],
            "direction_schema_sha256": hashlib.sha256(SCHEMA.read_bytes()).hexdigest(),
            "compiler_sha256": {
                path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
                for path in compiler_files
            },
            "reference_usage": "Research records are not generation inputs.",
        },
    }
