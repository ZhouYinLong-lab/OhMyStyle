#!/usr/bin/env python3
"""Preflight a render task before any stochastic image generation."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

from render_metrics import _lstar, hex_to_rgb
from safe_yaml import safe_load


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schema/render-task.schema.json"


def load_task(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        task = safe_load(handle)
    if not isinstance(task, dict):
        raise ValueError(f"Task must be a YAML object: {path}")
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(task), key=lambda item: list(item.path))
    if errors:
        location = ".".join(str(part) for part in errors[0].path) or "<root>"
        raise ValueError(f"{path}:{location}: {errors[0].message}")
    return task


def _color_constraints(task: dict[str, Any]) -> dict[str, Any]:
    colors = task.get("constraints", {}).get("colors", {})
    parsed: dict[str, Any] = {}
    for name, value in colors.items():
        if not isinstance(value, str):
            continue
        rgb = hex_to_rgb(value)
        parsed[name] = {"hex": f"#{value.lstrip('#').upper()}", "rgb": list(rgb), "lstar": round(_lstar(rgb), 4)}
    return parsed


def build_plan(task: dict[str, Any]) -> dict[str, Any]:
    constraints = task.get("constraints", {})
    colors = _color_constraints(task)
    luminance = constraints.get("luminance", {})
    max_delta = luminance.get("max_delta")
    exact_colors = bool(colors)
    uniform_background = bool(constraints.get("background", {}).get("uniform"))
    hard_luminance = max_delta is not None
    crop_targets = task.get("output", {}).get("target_aspects", [])
    crop_safe = bool(task.get("output", {}).get("safe_zone")) or len(crop_targets) > 1
    masking = constraints.get("masking", {})
    masking_targets = masking.get("targets", []) if isinstance(masking, dict) else []

    warnings: list[str] = []
    color_values = list(colors.values())
    if luminance.get("target_lstar") is not None and color_values:
        target = float(luminance["target_lstar"])
        for name, color in colors.items():
            if abs(color["lstar"] - target) > 1.0:
                warnings.append(f"{name} computes to L*={color['lstar']}, not target L*={target}")
    if max_delta is not None and len(color_values) >= 2:
        actual_delta = abs(color_values[0]["lstar"] - color_values[1]["lstar"])
        if actual_delta > float(max_delta):
            warnings.append(f"declared colors differ by L*={actual_delta:.3f}, above max_delta={max_delta}")
    if masking.get("required"):
        for target in masking_targets:
            profile = target.get("safety_profile")
            protected = target.get("protected_classes", [])
            if profile == "person" and not protected:
                warnings.append(f"mask target {target.get('id', '<unnamed>')} uses person safety_profile without protected_classes")
            if profile == "reflective" and target.get("exclude_specular") is not True:
                warnings.append(f"mask target {target.get('id', '<unnamed>')} must set exclude_specular=true for reflective materials")

    requires_masking = bool(masking.get("required"))
    needs_deterministic = exact_colors or uniform_background or hard_luminance or requires_masking
    if needs_deterministic:
        strategy = "hybrid_model_plus_deterministic_postprocess"
        model_only_allowed = False
        postprocess = [
            "run the declared model adapter to export same-image semantic masks",
            "run tools/mask-from-color.py with the target Lab color and protected classes",
            "apply_exact_background_fill where uniformity is required",
            "run tools/recolor-lab.py on each constrained region with an explicit mask",
            "run evaluate-render.py before human review",
        ]
    else:
        strategy = "model_first_with_layout_guard"
        model_only_allowed = True
        postprocess = ["run evaluate-render.py", "run crop preview checks"] if crop_safe else ["run evaluate-render.py"]

    hard_requirements = []
    if exact_colors:
        hard_requirements.append("Do not delegate exact HEX output to visual judgment; use a deterministic color stage.")
    if hard_luminance:
        hard_requirements.append("Measure CIELAB L* on the declared regions; reject above the declared delta.")
    if uniform_background:
        hard_requirements.append("Measure border-to-center background variance; reject gradients and vignettes.")
    if crop_safe:
        hard_requirements.append("Keep all critical objects inside the declared safe zone for every target aspect.")
    if masking.get("required"):
        hard_requirements.append("Do not recolor until the model-mask manifest hash matches the render and all protected classes are present.")
        if masking.get("fail_closed", True):
            hard_requirements.append("Reject masks with protected-region overlap, unsafe reflection loss, or insufficient active coverage.")

    return {
        "schema_version": "0.1.0",
        "task": {"id": task["id"], "subject": task["subject"], "brief": task.get("brief", "")},
        "output": task["output"],
        "colors": colors,
        "luminance": luminance,
        "strategy": strategy,
        "model_only_allowed": model_only_allowed,
        "hard_requirements": hard_requirements,
        "postprocess": postprocess,
        "masking": {
            "required": bool(masking.get("required", needs_deterministic)),
            "strategy": masking.get("strategy", "color_threshold_plus_protected_classes" if needs_deterministic else "color_threshold"),
            "adapter": masking.get("adapter", "file-segmentation-manifest"),
            "fail_closed": bool(masking.get("fail_closed", True)),
            "targets": masking_targets,
            "protected_classes": sorted({name for target in masking_targets for name in target.get("protected_classes", [])}),
            "status": "adapter_manifest_required" if masking_targets else ("required_for_deterministic_postprocess" if needs_deterministic else "optional"),
        },
        "warnings": warnings,
        "status": "blocked_until_resolved" if warnings else "ready_for_generation",
        "references": task.get("references", {"mode": "none"}),
        "review": {
            "generation_must_not_start_if": warnings,
            "retries_are_not_the_default": True,
            "human_review_after_measurement": True,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    plan = build_plan(load_task(args.task))
    rendered = json.dumps(plan, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"WROTE: {args.output} ({plan['status']})")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
