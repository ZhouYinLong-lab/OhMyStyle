#!/usr/bin/env python3
"""Shared discovery and deterministic registry generation for core resources."""

from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import yaml

from safe_yaml import safe_load


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return safe_load(handle)


def discover_packages(style_root: Path) -> list[Path]:
    root = style_root.resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Style package root does not exist: {style_root}")
    packages = sorted(path.parent for path in root.rglob("package.yaml"))
    if not packages:
        raise FileNotFoundError(f"No package.yaml found under: {style_root}")
    return packages


def _asset_count(directory: Path) -> int:
    if not directory.is_dir():
        return 0
    ignored = {".md", ".yaml", ".yml", ".json", ".csv", ".txt"}
    return sum(1 for path in directory.iterdir() if path.is_file() and path.suffix.lower() not in ignored)


def _reference_count(package: Path) -> int:
    manifest = package / "references" / "manifest.csv"
    if not manifest.is_file():
        return 0
    with manifest.open(encoding="utf-8", newline="") as handle:
        return sum(1 for _ in csv.DictReader(handle))


def build_registry(style_root: Path) -> dict[str, Any]:
    root = style_root.resolve()
    repository_root = root.parent
    entries: list[dict[str, Any]] = []
    for package in discover_packages(root):
        package_data = load_yaml(package / "package.yaml")
        resource_data = load_yaml(package / "resource.yaml")
        entries.append(
            {
                "resource_id": resource_data["resource_id"],
                "name": package_data["name"],
                "kind": package_data["kind"],
                "domain": package_data["domain"],
                "package_path": package.relative_to(repository_root).as_posix(),
                "maturity": resource_data["maturity"],
                "focus_dimensions": resource_data["focus_dimensions"],
                "reference_count": _reference_count(package),
                "accepted_example_count": _asset_count(package / "examples" / "accepted"),
                "rejected_example_count": _asset_count(package / "examples" / "rejected"),
                "benchmark": (package / "benchmark" / "benchmark.yaml").is_file(),
            }
        )
    return {"schema_version": "1.0.0", "generated_by": "tools/build-registry.py", "packages": entries}


def write_registry(style_root: Path, output: Path) -> None:
    registry = build_registry(style_root)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(yaml.safe_dump(registry, sort_keys=False, allow_unicode=True), encoding="utf-8")
