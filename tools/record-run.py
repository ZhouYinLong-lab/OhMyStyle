#!/usr/bin/env python3
"""Record a local render attempt without committing the generated image."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

from render_metrics import evaluate_image, hex_to_rgb


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    parser.add_argument("image", type=Path)
    parser.add_argument("--pair", dest="pair_id")
    parser.add_argument("--profile", default="default")
    parser.add_argument("--dominant-hex")
    parser.add_argument("--counter-hex")
    parser.add_argument("--max-lstar-delta", type=float)
    parser.add_argument("--status", choices=("pending", "accepted", "rejected"), default="pending")
    parser.add_argument("--notes", default="")
    parser.add_argument("--copy-image", action="store_true")
    parser.add_argument("--output-root", type=Path, default=Path("runs"))
    args = parser.parse_args()

    image = args.image.resolve()
    evaluation = evaluate_image(
        args.package,
        image,
        args.pair_id,
        args.profile,
        dominant_rgb=hex_to_rgb(args.dominant_hex) if args.dominant_hex else None,
        counter_rgb=hex_to_rgb(args.counter_hex) if args.counter_hex else None,
        max_lstar_delta=args.max_lstar_delta,
    )
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    run_id = f"{timestamp}-{sha256(image)[:10]}"
    output = args.output_root / run_id
    output.mkdir(parents=True, exist_ok=False)
    record = {
        "run_id": run_id,
        "created_at": datetime.now(UTC).isoformat(),
        "package": str(args.package.resolve()),
        "image": str(image),
        "image_sha256": sha256(image),
        "human_review": {"status": args.status, "notes": args.notes},
        "evaluation": evaluation,
    }
    if args.copy_image:
        target = output / image.name
        shutil.copy2(image, target)
        record["local_copy"] = str(target.resolve())
    (output / "run.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {output / 'run.json'} ({evaluation['status']})")


if __name__ == "__main__":
    main()
