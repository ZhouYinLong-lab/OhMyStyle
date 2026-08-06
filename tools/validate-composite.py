#!/usr/bin/env python3
"""Validate composite style recipes and their referenced base packages."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from composite_runtime import load_yaml, resolve_composite, resolve_base_package, validate_composite_definition


def discover(root: Path) -> list[Path]:
    if not root.exists():
        raise SystemExit(f"Path does not exist: {root}")
    root = root.resolve()
    if (root / "composite.yaml").is_file():
        return [root]
    return sorted(path.parent for path in root.rglob("composite.yaml"))


def validate(root: Path, schema: dict) -> list[str]:
    errors: list[str] = []
    recipe_root = resolve_composite(root)
    try:
        data = load_yaml(recipe_root / "composite.yaml")
    except Exception as exc:  # pragma: no cover - surfaced as a validation error
        return [f"{recipe_root / 'composite.yaml'}: invalid YAML: {exc}"]
    for problem in Draft202012Validator(schema).iter_errors(data):
        location = ".".join(str(part) for part in problem.path) or "<root>"
        errors.append(f"{recipe_root / 'composite.yaml'}:{location}: {problem.message}")
    if not isinstance(data, dict):
        return errors + [f"{recipe_root / 'composite.yaml'}: manifest must be a YAML object"]
    if data.get("id") != recipe_root.name:
        errors.append(f"{recipe_root / 'composite.yaml'}: id must match folder name {recipe_root.name}")
    try:
        validate_composite_definition(data, explicit_mode=data.get("mode"))
        for base in data["bases"]:
            resolve_base_package(recipe_root, str(base["package"]))
    except (ValueError, FileNotFoundError, KeyError) as exc:
        errors.append(f"{recipe_root / 'composite.yaml'}: {exc}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages/composites"))
    args = parser.parse_args()
    schema_path = Path(__file__).resolve().parents[1] / "schema/composite.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    recipes = discover(args.path)
    errors = [error for recipe in recipes for error in validate(recipe, schema)]
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(recipes)} composite recipe(s) validated")


if __name__ == "__main__":
    main()
