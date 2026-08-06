#!/usr/bin/env python3
"""Load, resolve, validate, and compile multi-style composite recipes."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from style_runtime import compile_prompt, load_package, load_yaml, resolve_package


MODES = {"stack", "blend", "contrast"}
ROLES = {"medium", "composition", "lighting", "palette", "surface", "texture", "subject", "layout"}


def safe_composite_file(root: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative.strip() or Path(relative).is_absolute():
        raise ValueError(f"Composite path must be relative: {relative!r}")
    package_root = root.resolve()
    candidate = (package_root / relative).resolve()
    try:
        candidate.relative_to(package_root)
    except ValueError as exc:
        raise ValueError(f"Composite path escapes recipe root: {relative!r}") from exc
    if not candidate.is_file():
        raise FileNotFoundError(f"Composite file does not exist: {candidate}")
    return candidate


def resolve_composite(path: Path) -> Path:
    path = path.resolve()
    if path.is_file() and path.name == "composite.yaml":
        return path.parent
    if (path / "composite.yaml").is_file():
        return path
    raise FileNotFoundError(f"No composite.yaml found at {path}")


def load_composite(path: Path) -> dict[str, Any]:
    root = resolve_composite(path)
    data = load_yaml(safe_composite_file(root, "composite.yaml"))
    if not isinstance(data, dict):
        raise ValueError("Composite manifest must be a YAML object")
    validate_composite_definition(data, explicit_mode=data.get("mode"))
    return {"root": root, "composite": data}


def _bases(data: dict[str, Any]) -> list[dict[str, Any]]:
    bases = data.get("bases")
    if not isinstance(bases, list) or len(bases) < 2:
        raise ValueError("Composite must declare at least two bases")
    return bases


def validate_composite_definition(data: dict[str, Any], explicit_mode: str | None = None) -> None:
    bases = _bases(data)
    packages: set[str] = set()
    for index, base in enumerate(bases):
        if not isinstance(base, dict):
            raise ValueError(f"bases[{index}] must be an object")
        package = base.get("package")
        role = base.get("role")
        if not isinstance(package, str) or not package.strip():
            raise ValueError(f"bases[{index}].package must be a non-empty path")
        if package in packages:
            raise ValueError(f"Composite repeats base package: {package}")
        packages.add(package)
        if role not in ROLES:
            raise ValueError(f"bases[{index}].role must be one of {sorted(ROLES)}")
        weight = base.get("weight")
        if weight is not None and (not isinstance(weight, (int, float)) or weight <= 0):
            raise ValueError(f"bases[{index}].weight must be positive")

    mode = explicit_mode or "auto"
    if mode not in MODES and mode != "auto":
        raise ValueError(f"Unknown composite mode: {mode}")
    roles = [str(base["role"]) for base in bases]
    if mode == "stack" and len(roles) != len(set(roles)):
        raise ValueError("stack mode requires distinct base roles")
    if mode == "blend":
        total = sum(float(base.get("weight", 1.0)) for base in bases)
        if total <= 0:
            raise ValueError("blend mode requires positive total weight")
    if mode == "contrast":
        zones = [base.get("zone") for base in bases]
        if any(not isinstance(zone, str) or not zone.strip() for zone in zones):
            raise ValueError("contrast mode requires a zone for every base")
        if len(set(zones)) < 2:
            raise ValueError("contrast mode requires at least two zones")


def infer_mode(data: dict[str, Any], subject: str = "") -> str:
    declared = data.get("mode")
    if declared in MODES:
        return str(declared)
    auto = data.get("auto") or {}
    if isinstance(auto, dict) and auto.get("enabled") is False:
        return auto.get("default_mode") if auto.get("default_mode") in MODES else "stack"
    hints = {str(item).lower() for item in auto.get("hints", [])} if isinstance(auto, dict) else set()
    bases = _bases(data)
    zones = [base.get("zone") for base in bases]
    if "contrast" in hints or (all(isinstance(zone, str) and zone.strip() for zone in zones) and len(set(zones)) > 1):
        return "contrast"
    roles = [base.get("role") for base in bases]
    if "blend" in hints or len(roles) != len(set(roles)):
        return "blend"
    lower_subject = subject.lower()
    if any(word in lower_subject for word in ("foreground", "background", "split", "zone", "区域", "前景", "背景")):
        return "contrast"
    if any(word in lower_subject for word in ("blend", "mix", "融合", "混合")):
        return "blend"
    default_mode = auto.get("default_mode") if isinstance(auto, dict) else None
    return default_mode if default_mode in MODES else "stack"


def _style_packages_root(composite_root: Path) -> Path:
    root = composite_root.resolve().parents[1]
    if root.name != "style-packages":
        raise ValueError("Composite must live under style-packages/composites")
    return root


def resolve_base_package(composite_root: Path, package_ref: str) -> Path:
    if not isinstance(package_ref, str) or not package_ref.strip() or Path(package_ref).is_absolute():
        raise ValueError(f"Base package must be a relative style-packages path: {package_ref!r}")
    style_root = _style_packages_root(composite_root)
    candidate = (style_root / package_ref).resolve()
    try:
        candidate.relative_to(style_root)
    except ValueError as exc:
        raise ValueError(f"Base package escapes style-packages: {package_ref!r}") from exc
    return resolve_package(candidate)


def _component_label(base: dict[str, Any], index: int) -> str:
    role = base["role"]
    zone = f" zone={base['zone']}" if base.get("zone") else ""
    weight = f" weight={base['weight']}" if base.get("weight") is not None else ""
    return f"COMPONENT {index + 1}: role={role}{zone}{weight}"


def _declared_conflicts(bases: list[dict[str, Any]]) -> list[str]:
    conflicts: list[str] = []
    for index, base in enumerate(bases):
        incompatible = set(str(item) for item in base.get("incompatibilities", []))
        for other_index, other in enumerate(bases):
            if index == other_index:
                continue
            capabilities = set(str(item) for item in other.get("capabilities", []))
            overlap = sorted(incompatible & capabilities)
            conflicts.extend(f"base {index + 1} conflicts with base {other_index + 1}: {item}" for item in overlap)
    return sorted(set(conflicts))


def compile_composite(
    composite_path: Path,
    subject: str,
    mode: str | None = None,
    profile: str = "generic",
    variables: dict[str, str] | None = None,
) -> dict[str, Any]:
    runtime = load_composite(composite_path)
    root = runtime["root"]
    data = runtime["composite"]
    selected_mode = mode if mode in MODES else infer_mode(data, subject)
    validate_composite_definition(data, explicit_mode=selected_mode)
    bases = _bases(data)
    declared_conflicts = _declared_conflicts(bases)
    conflict_config = data.get("conflicts") or {}
    policy = conflict_config.get("policy", "fail")
    if policy not in {"fail", "warn", "resolve"}:
        raise ValueError(f"Unknown conflict policy: {policy}")
    if declared_conflicts and policy == "fail":
        raise ValueError("Composite conflicts require resolution: " + "; ".join(declared_conflicts))

    components: list[dict[str, Any]] = []
    negative_prompts: list[str] = []
    for index, base in enumerate(bases):
        base_path = resolve_base_package(root, str(base["package"]))
        base_runtime = load_package(base_path)
        prompt, negative = compile_prompt(base_runtime, subject, None, profile, variables=variables)
        components.append(
            {
                "label": _component_label(base, index),
                "package": base["package"],
                "role": base["role"],
                "zone": base.get("zone"),
                "weight": base.get("weight", 1.0),
                "prompt": prompt,
                "capabilities": base.get("capabilities", []),
            }
        )
        if negative:
            negative_prompts.append(negative)

    if selected_mode == "stack":
        instructions = "Use each component only for its declared role. Do not let a component overwrite another component's role."
    elif selected_mode == "blend":
        total = sum(float(component["weight"]) for component in components)
        weights = "; ".join(f"{component['role']}={float(component['weight']) / total:.3f}" for component in components)
        instructions = f"Blend components within their shared dimensions using normalized weights: {weights}. Preserve the subject and resolve conflicts toward the higher weight."
    else:
        zones = "; ".join(f"{component['zone']} uses {component['role']}" for component in components)
        instructions = f"Keep style boundaries explicit by region. Zone assignments: {zones}. Do not smear one zone's medium or surface rules into another zone."

    prompt_parts = [
        f"COMPOSITE STYLE MODE: {selected_mode}",
        instructions,
        "COMPOSITE OVERRIDES:",
        str(data.get("overrides", {})),
        "COMPONENT PROMPTS:",
    ]
    prompt_parts.extend(f"{component['label']}\n{component['prompt']}" for component in components)
    constraints = data.get("constraints") or {}
    if constraints.get("must"):
        prompt_parts.append("COMPOSITE MUST:\n- " + "\n- ".join(str(item) for item in constraints["must"]))
    if constraints.get("avoid"):
        prompt_parts.append("COMPOSITE AVOID:\n- " + "\n- ".join(str(item) for item in constraints["avoid"]))

    negative = "\n".join(dict.fromkeys(negative_prompts))
    unresolved = sorted(set(re.findall(r"(?:\[[A-Z][A-Z0-9_]*\]|\{[A-Z][A-Z0-9_]*\})", "\n".join(prompt_parts))))
    return {
        "schema_version": "0.1.0",
        "job_type": "composite_style_render",
        "composite": {"id": data.get("id"), "name": data.get("name"), "version": data.get("version"), "mode": selected_mode, "root": str(root)},
        "subject": subject,
        "components": components,
        "prompt": "\n\n".join(prompt_parts),
        "negative_prompt": negative,
        "constraints": constraints,
        "conflicts": {
            "policy": policy,
            "detected": declared_conflicts,
            "resolutions": conflict_config.get("resolutions", []),
        },
        "template_variables": {"SUBJECT": subject, **(variables or {})},
        "unresolved_placeholders": unresolved,
        "provenance": data.get("provenance", {}),
    }
