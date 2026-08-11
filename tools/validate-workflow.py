#!/usr/bin/env python3
"""Validate source-transform workflows and external integration boundaries."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from safe_yaml import safe_load


ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path: Path) -> Any:
    with path.open(encoding="utf-8") as handle:
        return safe_load(handle)


def discover_manifests(root: Path, filename: str) -> list[Path]:
    root = root.resolve()
    if not root.exists():
        raise FileNotFoundError(f"Path does not exist: {root}")
    if root.is_file():
        return [root] if root.name == filename else []
    return sorted(root.rglob(filename))


def validate_workflow_manifest(path: Path, schema: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    try:
        data = load_yaml(path)
    except Exception as exc:
        return [f"{path}: invalid YAML: {exc}"]
    for problem in Draft202012Validator(schema).iter_errors(data):
        location = ".".join(str(part) for part in problem.path) or "<root>"
        errors.append(f"{path}:{location}: {problem.message}")
    if not isinstance(data, dict):
        return errors + [f"{path}: manifest must be a YAML object"]
    if path.parent.name != "" and data.get("id") != path.parent.name:
        errors.append(f"{path}: id must match folder name {path.parent.name}")
    variants = data.get("variants", [])
    variant_ids = [item.get("id") for item in variants if isinstance(item, dict)]
    if len(variant_ids) != len(set(variant_ids)):
        errors.append(f"{path}: variant ids must be unique")
    protected = data.get("style_projection", {}).get("protected_axes", [])
    required_protection = {"source_subject_identity", "user_subject_constraints"}
    if not required_protection.issubset(set(protected)):
        errors.append(f"{path}: protected_axes must include {sorted(required_protection)}")
    if data.get("subject_policy", {}).get("default_subjects") != []:
        errors.append(f"{path}: default_subjects must be empty")
    if data.get("source", {}).get("rights_required") is not True:
        errors.append(f"{path}: source.rights_required must be true")
    return errors


def validate_integration_manifest(path: Path, workflow_root: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = load_yaml(path)
    except Exception as exc:
        return [f"{path}: invalid YAML: {exc}"]
    if not isinstance(data, dict):
        return [f"{path}: manifest must be a YAML object"]
    required = {"id", "kind", "external_only", "copy_upstream_materials", "upstream_url", "workflow_ref", "license", "installation"}
    missing = sorted(required - set(data))
    errors.extend(f"{path}: missing required key {key}" for key in missing)
    if data.get("kind") != "external_workflow":
        errors.append(f"{path}: kind must be external_workflow")
    if data.get("external_only") is not True:
        errors.append(f"{path}: external_only must be true")
    if data.get("copy_upstream_materials") is not False:
        errors.append(f"{path}: copy_upstream_materials must be false")
    if not isinstance(data.get("upstream_url"), str) or not data["upstream_url"].startswith("https://github.com/"):
        errors.append(f"{path}: upstream_url must point to a GitHub HTTPS URL")
    license_data = data.get("license")
    if not isinstance(license_data, dict) or not license_data.get("url"):
        errors.append(f"{path}: license.url is required")
    workflow_ref = data.get("workflow_ref")
    if isinstance(workflow_ref, str):
        target = (ROOT / workflow_ref).resolve()
        try:
            target.relative_to(workflow_root.resolve())
        except ValueError:
            errors.append(f"{path}: workflow_ref must stay inside {workflow_root}")
        if not target.is_file():
            errors.append(f"{path}: workflow_ref does not exist: {workflow_ref}")
    return errors


def validate_all(workflows: Path, integrations: Path) -> list[str]:
    schema = json.loads((ROOT / "schema/workflow.schema.json").read_text(encoding="utf-8"))
    errors: list[str] = []
    workflow_files = discover_manifests(workflows, "workflow.yaml")
    integration_files = sorted(integrations.resolve().rglob("*.yaml")) if integrations.resolve().is_dir() else discover_manifests(integrations, "yaml")
    workflow_ids: set[str] = set()
    for path in workflow_files:
        errors.extend(validate_workflow_manifest(path, schema))
        try:
            data = load_yaml(path)
            if isinstance(data, dict):
                workflow_id = data.get("id")
                if workflow_id in workflow_ids:
                    errors.append(f"{path}: duplicate workflow id {workflow_id}")
                workflow_ids.add(workflow_id)
        except Exception:
            pass
    for path in integration_files:
        errors.extend(validate_integration_manifest(path, workflows))
    if not workflow_files:
        errors.append(f"{workflows}: no workflow.yaml found")
    if not integration_files:
        errors.append(f"{integrations}: no integration manifests found")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workflows", type=Path, default=Path("workflows"))
    parser.add_argument("--integrations", type=Path, default=Path("integrations"))
    args = parser.parse_args()
    try:
        errors = validate_all(args.workflows, args.integrations)
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    workflows = len(discover_manifests(args.workflows, "workflow.yaml"))
    integrations = len(sorted(args.integrations.resolve().rglob("*.yaml"))) if args.integrations.resolve().is_dir() else len(discover_manifests(args.integrations, "yaml"))
    print(f"PASS: {workflows} workflow(s) and {integrations} integration manifest(s) validated")


if __name__ == "__main__":
    main()
