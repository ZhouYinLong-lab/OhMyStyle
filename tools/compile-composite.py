#!/usr/bin/env python3
"""Compile a multi-style composite recipe into a provider-neutral job."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from composite_runtime import compile_composite


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("composite", type=Path)
    parser.add_argument("--subject", required=True)
    parser.add_argument("--mode", choices=("auto", "stack", "blend", "contrast"), default=None)
    parser.add_argument("--profile", choices=("generic", "weak"), default="generic")
    parser.add_argument("--var", action="append", default=[], metavar="KEY=VALUE")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    variables: dict[str, str] = {}
    for assignment in args.var:
        if "=" not in assignment:
            parser.error(f"--var must use KEY=VALUE: {assignment}")
        key, value = assignment.split("=", 1)
        variables[key.strip()] = value
    job = compile_composite(args.composite, args.subject, mode=args.mode, profile=args.profile, variables=variables)
    rendered = json.dumps(job, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"WROTE: {args.output}")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
