#!/usr/bin/env python3
"""Validate OhMyStyle Style Packages without touching legacy style.json folders."""

from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover - exercised in clean environments
    print(
        "Missing validation dependency. Install PyYAML and jsonschema before running this tool.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


REQUIRED_FILES = {
    "README.md",
    "style.yaml",
    "palette/palette.json",
    "composition/composition.md",
    "composition/diagrams/README.md",
    "technique/materials.md",
    "technique/process.md",
    "technique/parameters.yaml",
    "prompts/base.txt",
    "prompts/variations.txt",
    "prompts/negative.txt",
    "examples/successful/README.md",
    "examples/rejected/README.md",
    "metadata/sources.csv",
    "metadata/license.md",
    "provenance.yaml",
    "version.md",
}

REQUIRED_SOURCE_COLUMNS = {
    "path",
    "kind",
    "title",
    "creator",
    "source_url",
    "license",
    "attribution",
    "notes",
}

IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".tif", ".tiff"}


class Errors:
    def __init__(self) -> None:
        self.items: list[str] = []

    def add(self, message: str) -> None:
        self.items.append(message)


def load_yaml(path: Path, errors: Errors) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return yaml.safe_load(handle)
    except (OSError, yaml.YAMLError) as exc:
        errors.add(f"{path}: invalid YAML or unreadable file: {exc}")
        return None


def load_json(path: Path, errors: Errors) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        errors.add(f"{path}: invalid JSON or unreadable file: {exc}")
        return None


def discover_packages(path: Path) -> list[Path]:
    path = path.resolve()
    if (path / "style.yaml").is_file():
        return [path]
    if (path / "styles").is_dir():
        path = path / "styles"
    if path.is_dir():
        return sorted(child for child in path.iterdir() if (child / "style.yaml").is_file())
    raise SystemExit(f"No Style Packages found at {path}")


def validate_sources(package: Path, errors: Errors) -> None:
    sources_path = package / "metadata/sources.csv"
    try:
        with sources_path.open("r", encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            columns = set(reader.fieldnames or [])
            missing = sorted(REQUIRED_SOURCE_COLUMNS - columns)
            if missing:
                errors.add(f"{sources_path}: missing columns: {', '.join(missing)}")
            for number, row in enumerate(reader, start=2):
                if not row.get("path", "").strip():
                    errors.add(f"{sources_path}:{number}: path is required")
                    continue
                asset = package / row["path"]
                if not asset.exists():
                    errors.add(f"{sources_path}:{number}: listed path does not exist: {row['path']}")
                for field in ("creator", "license", "attribution"):
                    if not row.get(field, "").strip():
                        errors.add(f"{sources_path}:{number}: {field} is required")
    except OSError as exc:
        errors.add(f"{sources_path}: cannot read sources CSV: {exc}")


def validate_provenance(package: Path, style: dict[str, Any], errors: Errors) -> None:
    provenance_path = package / "provenance.yaml"
    provenance = load_yaml(provenance_path, errors)
    if not isinstance(provenance, dict):
        errors.add(f"{provenance_path}: top-level value must be an object")
        return

    if provenance.get("package_id") != style.get("id"):
        errors.add(f"{provenance_path}: package_id must match style.yaml id")
    if provenance.get("package_version") != style.get("version"):
        errors.add(f"{provenance_path}: package_version must match style.yaml version")
    if not isinstance(provenance.get("curation_status"), str) or not provenance["curation_status"].strip():
        errors.add(f"{provenance_path}: curation_status is required")

    assets = provenance.get("assets")
    if not isinstance(assets, list) or not assets:
        errors.add(f"{provenance_path}: assets must be a non-empty list")
        return
    for index, asset in enumerate(assets):
        if not isinstance(asset, dict):
            errors.add(f"{provenance_path}: assets[{index}] must be an object")
            continue
        for field in ("path", "role", "source", "license", "attribution"):
            if not isinstance(asset.get(field), str) or not asset[field].strip():
                errors.add(f"{provenance_path}: assets[{index}].{field} is required")


def validate_package(package: Path, schema: dict[str, Any], errors: Errors) -> None:
    for relative in sorted(REQUIRED_FILES):
        if not (package / relative).is_file():
            errors.add(f"{package}: missing required file {relative}")

    style_path = package / "style.yaml"
    style = load_yaml(style_path, errors)
    if not isinstance(style, dict):
        errors.add(f"{style_path}: top-level value must be an object")
        return

    validator = Draft202012Validator(schema)
    for problem in sorted(validator.iter_errors(style), key=lambda item: list(item.path)):
        location = ".".join(str(part) for part in problem.path) or "<root>"
        errors.add(f"{style_path}:{location}: {problem.message}")

    package_id = style.get("id")
    if isinstance(package_id, str) and package_id != package.name:
        errors.add(f"{style_path}: id must match folder name ({package.name})")

    files = style.get("files", {})
    if isinstance(files, dict):
        for key, relative in files.items():
            if isinstance(relative, str) and not (package / relative).exists():
                errors.add(f"{style_path}: files.{key} points to missing path {relative}")

    palette_path = package / "palette/palette.json"
    palette = load_json(palette_path, errors)
    if not isinstance(palette, dict):
        errors.add(f"{palette_path}: top-level value must be an object")
    else:
        colors = palette.get("colors")
        if not isinstance(colors, list) or len(colors) < 3:
            errors.add(f"{palette_path}: colors must contain at least 3 entries")
        else:
            for index, color in enumerate(colors):
                if not isinstance(color, dict):
                    errors.add(f"{palette_path}: colors[{index}] must be an object")
                    continue
                hex_value = color.get("hex")
                if not isinstance(hex_value, str) or len(hex_value) != 7 or not hex_value.startswith("#"):
                    errors.add(f"{palette_path}: colors[{index}].hex must be a #RRGGBB value")

    validate_sources(package, errors)
    validate_provenance(package, style, errors)

    # Only reference images need external source/license rows. Generated
    # examples are package outputs and carry generation metadata sidecars.
    image_files = [
        path
        for root in (package / "references",)
        if root.exists()
        for path in root.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    ]
    if image_files:
        try:
            source_rows = list(csv.DictReader((package / "metadata/sources.csv").open(encoding="utf-8", newline="")))
        except OSError:
            source_rows = []
        listed = {row.get("path", "") for row in source_rows}
        for image in image_files:
            relative = image.relative_to(package).as_posix()
            if relative not in listed:
                errors.add(f"{image}: image must be listed in metadata/sources.csv")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate OhMyStyle Style Packages.")
    parser.add_argument("path", nargs="?", type=Path, default=Path("styles"))
    parser.add_argument(
        "--schema",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "schema/style.schema.json",
    )
    args = parser.parse_args()

    schema = load_json(args.schema.resolve(), Errors())
    if not isinstance(schema, dict):
        raise SystemExit("Schema could not be loaded")

    errors = Errors()
    packages = discover_packages(args.path)
    for package in packages:
        validate_package(package, schema, errors)

    if errors.items:
        for item in errors.items:
            print(f"FAIL: {item}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(packages)} Style Package(s) validated")


if __name__ == "__main__":
    main()
