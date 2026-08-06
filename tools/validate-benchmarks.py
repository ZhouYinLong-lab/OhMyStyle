#!/usr/bin/env python3
"""Validate fixed visual-style benchmark manifests and shared tasks."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from benchmark_runtime import load_benchmark


def discover(root: Path) -> list[Path]:
    if not root.exists():
        raise SystemExit(f"Path does not exist: {root}")
    return sorted(path.parent for path in root.resolve().rglob("benchmark.yaml"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path, default=Path("style-packages"))
    args = parser.parse_args()
    errors: list[str] = []
    manifests = discover(args.path)
    for manifest in manifests:
        try:
            load_benchmark(manifest)
        except (OSError, ValueError, KeyError) as exc:
            errors.append(f"{manifest}: {exc}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
    print(f"PASS: {len(manifests)} benchmark manifest(s) validated")


if __name__ == "__main__":
    main()
