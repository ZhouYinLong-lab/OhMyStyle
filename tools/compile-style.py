#!/usr/bin/env python3
"""Compile a Style Package into a provider-neutral generation job."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from style_runtime import compile_job


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("--subject", required=True, help="Subject or scene to render")
    parser.add_argument("--pair", dest="pair_id", help="Palette pair id")
    parser.add_argument("--profile", choices=("generic", "weak"), default="generic")
    parser.add_argument("--model", default="provider-neutral")
    parser.add_argument("--var", action="append", default=[], metavar="KEY=VALUE", help="Fill a package prompt variable; repeatable")
    parser.add_argument(
        "--references",
        choices=("palette", "details", "primary", "all"),
        default="palette",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    variables = {}
    for assignment in args.var:
        if "=" not in assignment:
            parser.error(f"--var must use KEY=VALUE: {assignment}")
        key, value = assignment.split("=", 1)
        variables[key.strip()] = value
    job = compile_job(
        args.package,
        args.subject,
        pair_id=args.pair_id,
        profile=args.profile,
        reference_set=args.references,
        model=args.model,
        variables=variables,
    )
    rendered = json.dumps(job, ensure_ascii=False, indent=2) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
        print(f"WROTE: {args.output}")
    else:
        print(rendered, end="")


if __name__ == "__main__":
    main()
