#!/usr/bin/env python3
"""Render a compiled ASCII job from a literal source grid and explicit font."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ascii_grid_runtime import render_grid_job


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("job", type=Path)
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--font", required=True, type=Path, help="Monospace TrueType/OpenType font file")
    parser.add_argument("--output", required=True, type=Path, help="New render directory")
    args = parser.parse_args()
    job = json.loads(args.job.read_text(encoding="utf-8"))
    try:
        record = render_grid_job(job, args.source, args.font, args.output)
    except (ValueError, OSError) as error:
        parser.error(str(error))
    print(f"WROTE: {args.output / 'master.png'}")
    print(f"RGB SHA256: {record['output']['rgb_pixels_sha256']}")


if __name__ == "__main__":
    main()
