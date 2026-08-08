#!/usr/bin/env python3
"""Validate that style packages separate visual rules from requested subjects."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from safe_yaml import safe_load


CONTRACT_MARKER = "SUBJECT INDEPENDENCE CONTRACT"


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


def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        value = safe_load(handle)
    if not isinstance(value, dict):
        raise ValueError("top-level value must be an object")
    return value


def validate(package: Path, errors: list[str]) -> None:
    identity_path = package / "identity.yaml"
    prompt_path = package / "prompts" / "base.txt"
    try:
        identity = load_yaml(identity_path)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        errors.append(f"{identity_path}: invalid YAML: {exc}")
        return

    scope = identity.get("scope")
    if not isinstance(scope, dict):
        errors.append(f"{identity_path}: scope must declare subject_policy: open")
    elif scope.get("subject_policy") != "open":
        errors.append(f"{identity_path}: scope.subject_policy must be 'open'")

    try:
        prompt = prompt_path.read_text(encoding="utf-8")
    except OSError as exc:
        errors.append(f"{prompt_path}: unreadable: {exc}")
        return
    if CONTRACT_MARKER not in prompt:
        errors.append(f"{prompt_path}: missing {CONTRACT_MARKER}")
    if "{SUBJECT}" not in prompt and "[SUBJECT]" not in prompt:
        errors.append(f"{prompt_path}: must expose a SUBJECT placeholder")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    args = parser.parse_args()
    errors: list[str] = []
    packages = discover(args.path)
    for package in packages:
        validate(package, errors)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(packages)} package(s) satisfy subject-independence contract")


if __name__ == "__main__":
    main()
