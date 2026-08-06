#!/usr/bin/env python3
"""Validate the independent artist, photographer, movement, school, technique, and preset demos."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from safe_yaml import safe_load


REQUIRED_FILES = {
    "package.yaml",
    "README.md",
    "identity.yaml",
    "visual-signature.yaml",
    "reproduction.yaml",
    "relations.yaml",
    "palette/palette.json",
    "prompts/base.txt",
    "prompts/negative.txt",
    "evaluation.yaml",
    "references/manifest.csv",
    "references/primary/README.md",
    "references/secondary/README.md",
    "references/details/README.md",
    "examples/accepted/README.md",
    "examples/rejected/README.md",
    "provenance.yaml",
    "resource.yaml",
    "version.md",
}

SOURCE_COLUMNS = {"asset_id", "local_path", "title", "creator", "year", "source_url", "license", "attribution", "role", "notes"}


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return safe_load(handle)


def safe_package_file(package: Path, relative: str) -> Path:
    if Path(relative).is_absolute():
        raise ValueError(f"path must be relative: {relative!r}")
    root = package.resolve()
    candidate = (root / relative).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValueError(f"path escapes package root: {relative!r}") from exc
    return candidate


def discover(root: Path) -> list[Path]:
    if not root.exists():
        raise SystemExit(f"Path does not exist: {root}")
    root = root.resolve()
    if (root / "package.yaml").is_file():
        return [root]
    if (root / "style-packages").is_dir():
        root = root / "style-packages"
    packages = sorted(path.parent for path in root.rglob("package.yaml"))
    if not packages:
        raise SystemExit(f"No package.yaml found under: {root}")
    return packages


def validate_package(package: Path, schema: dict[str, Any], errors: list[str]) -> None:
    for relative in REQUIRED_FILES:
        try:
            exists = safe_package_file(package, relative).is_file()
        except ValueError as exc:
            errors.append(f"{package}: {relative}: {exc}")
            continue
        if not exists:
            errors.append(f"{package}: missing {relative}")

    try:
        data = load_yaml(safe_package_file(package, "package.yaml"))
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f"{package / 'package.yaml'}: invalid YAML: {exc}")
        return
    if not isinstance(data, dict):
        errors.append(f"{package / 'package.yaml'}: top-level value must be an object")
        return

    for problem in Draft202012Validator(schema).iter_errors(data):
        location = ".".join(str(part) for part in problem.path) or "<root>"
        errors.append(f"{package / 'package.yaml'}:{location}: {problem.message}")
    if data.get("id") != package.name:
        errors.append(f"{package / 'package.yaml'}: id must match folder name {package.name}")

    try:
        manifest_path = safe_package_file(package, "references/manifest.csv")
        with manifest_path.open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            columns = set(reader.fieldnames or [])
            for missing in sorted(SOURCE_COLUMNS - columns):
                errors.append(f"{manifest_path}: missing column {missing}")
            seen_asset_ids: set[str] = set()
            for row_number, row in enumerate(reader, start=2):
                for field in ("asset_id", "title", "creator", "source_url", "license", "attribution", "role"):
                    if not row.get(field, "").strip():
                        errors.append(f"{manifest_path}:{row_number}: {field} is required")
                asset_id = row.get("asset_id", "").strip()
                if asset_id in seen_asset_ids:
                    errors.append(f"{manifest_path}:{row_number}: duplicate asset_id {asset_id}")
                seen_asset_ids.add(asset_id)
                local_path = row.get("local_path", "").strip()
                if local_path:
                    try:
                        asset_path = safe_package_file(package, local_path)
                    except ValueError as exc:
                        errors.append(f"{manifest_path}:{row_number}: {exc}")
                    else:
                        if not asset_path.is_file():
                            errors.append(f"{manifest_path}:{row_number}: missing local asset {local_path}")
    except (OSError, ValueError) as exc:
        errors.append(f"{package / 'references/manifest.csv'}: unreadable: {exc}")

    try:
        base_prompt = safe_package_file(package, "prompts/base.txt").read_text(encoding="utf-8").lower()
    except (OSError, ValueError) as exc:
        errors.append(f"{package / 'prompts/base.txt'}: unreadable: {exc}")
        base_prompt = ""
    canonical_name = str(data.get("name", "")).lower()
    if canonical_name and canonical_name in base_prompt:
        errors.append(f"{package / 'prompts/base.txt'}: anonymous prompt must not contain package name")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate OhMyStyle demo packages.")
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    args = parser.parse_args()
    schema_path = Path(__file__).resolve().parents[1] / "schema/package.schema.json"
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    packages = discover(args.path)
    errors: list[str] = []
    for package in packages:
        validate_package(package, schema, errors)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(packages)} demo package(s) validated")


if __name__ == "__main__":
    main()
