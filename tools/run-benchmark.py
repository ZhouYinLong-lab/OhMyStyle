#!/usr/bin/env python3
"""Compile a five-task benchmark into provider-neutral render jobs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from benchmark_runtime import compile_benchmark


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("benchmark", type=Path)
    parser.add_argument("--model", required=True)
    parser.add_argument("--profile", choices=("generic", "weak"), default="weak")
    parser.add_argument("--run-id")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = compile_benchmark(args.benchmark, args.model, args.profile, args.run_id)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {args.output} ({len(result['tasks'])} tasks)")


if __name__ == "__main__":
    main()
