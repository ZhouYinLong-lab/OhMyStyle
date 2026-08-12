#!/usr/bin/env python3
"""Validate the public OhMyStyle Skill interface contract."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

from safe_yaml import safe_load


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    root = args.root.resolve()
    errors: list[str] = []
    manifest_path = root / "skill/manifest.yaml"
    skill_path = root / "SKILL.md"
    schema_path = root / "schema/skill-session.schema.json"
    for path in (manifest_path, skill_path, schema_path):
        if not path.is_file():
            errors.append(f"missing required Skill file: {path}")
    if skill_path.is_file() and "风格确认" not in skill_path.read_text(encoding="utf-8"):
        errors.append("SKILL.md must document the style confirmation gate")
    if manifest_path.is_file():
        with manifest_path.open(encoding="utf-8") as handle:
            manifest = safe_load(handle)
        for key in ("id", "entrypoints", "conversation", "style_policy", "provider_policy"):
            if not isinstance(manifest, dict) or key not in manifest:
                errors.append(f"skill/manifest.yaml missing key: {key}")
        if isinstance(manifest, dict) and manifest.get("conversation", {}).get("generation_requires_confirmed_style") is not True:
            errors.append("Skill generation must require confirmed style")
        if isinstance(manifest, dict):
            phases = manifest.get("conversation", {}).get("phases", [])
            required_phases = {"content_confirmation", "detail_confirmation", "style_matching", "style_confirmation", "ready", "compiled", "generated"}
            if not required_phases.issubset(set(phases)):
                errors.append("Skill manifest is missing one or more required conversation phases")
            for entrypoint, relative in manifest.get("entrypoints", {}).items():
                if entrypoint == "file" and not (root / relative).is_file():
                    errors.append(f"Skill file entrypoint does not exist: {relative}")
                if entrypoint in {"cli", "http", "mcp"} and not (root / relative).is_file():
                    errors.append(f"Skill {entrypoint} entrypoint does not exist: {relative}")
    if schema_path.is_file():
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        if not isinstance(schema, dict):
            errors.append("skill session schema must be a JSON object")
        else:
            try:
                Draft202012Validator.check_schema(schema)
            except Exception as exc:
                errors.append(f"skill session schema is invalid: {exc}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print("PASS: OhMyStyle Skill interface contract validated")


if __name__ == "__main__":
    main()
