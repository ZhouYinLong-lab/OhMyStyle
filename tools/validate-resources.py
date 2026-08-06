#!/usr/bin/env python3
"""Validate core resource manifests and the generated registry."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from resource_registry import build_registry, discover_packages, load_yaml


def safe_path(package: Path, relative: str) -> Path:
    if not isinstance(relative, str) or not relative.strip() or Path(relative).is_absolute():
        raise ValueError(f"artifact path must be relative: {relative!r}")
    root = package.resolve()
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"artifact path escapes package: {relative!r}") from exc
    return candidate


def validate(style_root: Path) -> list[str]:
    repository_root = style_root.resolve().parent
    resource_schema = json.loads((repository_root / "schema/resource.schema.json").read_text(encoding="utf-8"))
    registry_schema = json.loads((repository_root / "schema/registry.schema.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    packages = discover_packages(style_root)
    for package in packages:
        resource_path = package / "resource.yaml"
        if not resource_path.is_file():
            errors.append(f"{package}: missing resource.yaml")
            continue
        try:
            data = load_yaml(resource_path)
        except (OSError, ValueError, yaml.YAMLError) as exc:
            errors.append(f"{resource_path}: invalid YAML: {exc}")
            continue
        for problem in Draft202012Validator(resource_schema).iter_errors(data):
            location = ".".join(str(part) for part in problem.path) or "<root>"
            errors.append(f"{resource_path}:{location}: {problem.message}")
        if not isinstance(data, dict):
            continue
        package_data = load_yaml(package / "package.yaml")
        if data.get("resource_id") != package_data.get("id") or data.get("resource_id") != package.name:
            errors.append(f"{resource_path}: resource_id must match package.yaml id and folder")
        if data.get("maturity") == "L3" and not data.get("evidence", {}).get("accepted_example"):
            errors.append(f"{resource_path}: L3 requires an accepted example")
        for artifact_name, relative in data.get("artifacts", {}).items():
            try:
                artifact = safe_path(package, relative)
            except ValueError as exc:
                errors.append(f"{resource_path}: artifacts.{artifact_name}: {exc}")
                continue
            if not artifact.exists():
                errors.append(f"{resource_path}: missing artifact {relative}")

    registry_path = repository_root / "registry/index.yaml"
    if not registry_path.is_file():
        errors.append(f"{registry_path}: missing generated registry")
        return errors
    try:
        registry = load_yaml(registry_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        return errors + [f"{registry_path}: invalid YAML: {exc}"]
    for problem in Draft202012Validator(registry_schema).iter_errors(registry):
        location = ".".join(str(part) for part in problem.path) or "<root>"
        errors.append(f"{registry_path}:{location}: {problem.message}")
    expected = build_registry(style_root)
    if registry != expected:
        errors.append(f"{registry_path}: out of date; run python tools/build-registry.py")
    ids = [entry.get("resource_id") for entry in registry.get("packages", [])] if isinstance(registry, dict) else []
    if len(ids) != len(set(ids)):
        errors.append(f"{registry_path}: duplicate resource_id")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    args = parser.parse_args()
    errors = validate(args.path)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(discover_packages(args.path))} core resource manifest(s) validated")


if __name__ == "__main__":
    main()
