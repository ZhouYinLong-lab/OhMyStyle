#!/usr/bin/env python3
"""Build the deterministic core resource registry."""

from __future__ import annotations

import argparse
from pathlib import Path

from resource_registry import write_registry


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    parser.add_argument("--output", type=Path, default=Path("registry/index.yaml"))
    args = parser.parse_args()
    write_registry(args.path, args.output)
    print(f"WROTE: {args.output}")


if __name__ == "__main__":
    main()
