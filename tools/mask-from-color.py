#!/usr/bin/env python3
"""Generate a safe, auditable mask from target color plus model semantic masks."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from mask_adapters import FileSegmentationAdapter, MaskAdapterError, MaskRequest, segment_by_color


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path, help="Grayscale active-material mask")
    parser.add_argument("--target-hex", required=True)
    parser.add_argument("--report", type=Path)
    parser.add_argument("--reflection-mask", type=Path)
    parser.add_argument("--manifest", type=Path, help="Provider-neutral semantic mask manifest")
    parser.add_argument("--role", choices=["subject", "background", "product"], default="subject")
    parser.add_argument("--safety-profile", choices=["generic", "person", "reflective"], default="generic")
    parser.add_argument("--protected-class", action="append", default=[])
    parser.add_argument("--lab-radius", type=float, default=24.0)
    parser.add_argument("--lstar-tolerance", type=float)
    parser.add_argument("--min-component-area", type=int, default=64)
    parser.add_argument("--allow-review", action="store_true", help="Write a review-required mask but return success")
    args = parser.parse_args()

    protected_classes = tuple(args.protected_class)
    if args.safety_profile == "person" and not protected_classes:
        protected_classes = ("skin", "face", "hair", "eyes", "lips", "hands", "jewelry", "glasses")
    provider_masks = None
    adapter_name = None
    try:
        if args.manifest:
            adapter = FileSegmentationAdapter(args.manifest, args.input)
            provider_masks = adapter.require(protected_classes) if protected_classes else {name: adapter.get(name) for name in adapter.classes}
            adapter_name = adapter.name
    except (MaskAdapterError, OSError, ValueError) as error:
        report = {"status": "rejected", "confidence": 0.0, "metrics": {}, "reasons": [str(error)], "provenance": {"model_adapter": adapter_name}}
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        sys.exit(2)

    request = MaskRequest(
        image_path=args.input,
        target_hex=args.target_hex,
        role=args.role,
        safety_profile=args.safety_profile,
        lab_radius=args.lab_radius,
        lstar_tolerance=args.lstar_tolerance,
        min_component_area=args.min_component_area,
        protected_classes=protected_classes,
        fail_closed=not args.allow_review,
    )
    result = segment_by_color(request, provider_masks)
    report = {
        "status": result.status,
        "confidence": result.confidence,
        "metrics": result.metrics,
        "reasons": result.reasons,
        "provenance": {**result.provenance, "model_adapter": adapter_name},
    }
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.mask.save(args.output)
    if args.reflection_mask:
        args.reflection_mask.parent.mkdir(parents=True, exist_ok=True)
        result.reflection_mask.save(args.reflection_mask)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    if result.status != "ready" and not args.allow_review:
        sys.exit(2)


if __name__ == "__main__":
    main()
