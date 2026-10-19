"""Shared validation for provider-neutral compiled style jobs."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


SCHEMA = Path(__file__).resolve().parents[1] / "schema/compiled-style-job.schema.json"


def validate_compiled_job(job: dict[str, Any]) -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(job), key=lambda item: list(item.path))
    if errors:
        problem = errors[0]
        location = ".".join(map(str, problem.path)) or "<root>"
        raise ValueError(f"Compiled style job violates its schema at {location}: {problem.message}")
