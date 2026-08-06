#!/usr/bin/env python3
"""Evaluate a render against deterministic package-level color constraints."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from render_metrics import evaluate_image, hex_to_rgb


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("image", type=Path)
    parser.add_argument("--pair", dest="pair_id")
    parser.add_argument("--profile", default="default")
    parser.add_argument("--color-threshold", type=float, default=0.28)
    parser.add_argument("--dominant-hex", help="Override package dominant color, e.g. 0070FC")
    parser.add_argument("--counter-hex", help="Override package counter color, e.g. C85400")
    parser.add_argument("--max-lstar-delta", type=float, help="Override the maximum CIELAB L* difference")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate_image(
        args.package,
        args.image,
        pair_id=args.pair_id,
        profile=args.profile,
        color_threshold=args.color_threshold,
        dominant_rgb=hex_to_rgb(args.dominant_hex) if args.dominant_hex else None,
        counter_rgb=hex_to_rgb(args.counter_hex) if args.counter_hex else None,
        max_lstar_delta=args.max_lstar_delta,
    )
    rendered = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"WROTE: {args.output} ({result['status']})")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
