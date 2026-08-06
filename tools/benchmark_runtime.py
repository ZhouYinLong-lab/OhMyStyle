#!/usr/bin/env python3
"""Shared loading, validation, and provider-neutral compilation for benchmarks."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from safe_yaml import safe_load
from style_runtime import compile_job, load_yaml, resolve_package


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK_SCHEMA = json.loads((ROOT / "schema/benchmark.schema.json").read_text(encoding="utf-8"))
RUN_SCHEMA = json.loads((ROOT / "schema/benchmark-run.schema.json").read_text(encoding="utf-8"))
TASK_SCHEMA = json.loads((ROOT / "schema/render-task.schema.json").read_text(encoding="utf-8"))
TASK_IDS = {"portrait", "still-life", "architecture-environment", "minimal-composition", "fuzzy-brief"}


def resolve_benchmark(path: Path) -> Path:
    path = path.resolve()
    if path.is_file() and path.name == "benchmark.yaml":
        return path.parent
    if (path / "benchmark.yaml").is_file():
        return path
    raise FileNotFoundError(f"No benchmark.yaml found at {path}")


def safe_benchmark_path(root: Path, relative: str, *, label: str) -> Path:
    if not isinstance(relative, str) or not relative.strip() or Path(relative).is_absolute():
        raise ValueError(f"{label} must be a relative path: {relative!r}")
    base = root.resolve()
    candidate = (base / relative).resolve()
    try:
        candidate.relative_to(base)
    except ValueError:
        # Benchmark tasks are intentionally allowed to reference the repository's
        # shared task suite, but never an arbitrary path outside the repository.
        candidate.relative_to(ROOT.resolve())
    if not candidate.exists():
        raise FileNotFoundError(f"{label} does not exist: {candidate}")
    return candidate


def _schema_errors(data: Any, schema: dict[str, Any]) -> list[str]:
    return [problem.message for problem in Draft202012Validator(schema).iter_errors(data)]


def load_benchmark(path: Path) -> dict[str, Any]:
    root = resolve_benchmark(path)
    data = load_yaml(root / "benchmark.yaml")
    errors = _schema_errors(data, BENCHMARK_SCHEMA)
    if errors:
        raise ValueError(f"{root / 'benchmark.yaml'}: " + "; ".join(errors))
    package_root = root.parent
    package = load_yaml(package_root / "package.yaml")
    if data["package_version"] != package.get("version"):
        raise ValueError(f"{root / 'benchmark.yaml'}: package_version does not match package.yaml")
    task_ids = [entry["id"] for entry in data["tasks"]]
    if set(task_ids) != TASK_IDS or len(task_ids) != len(set(task_ids)):
        raise ValueError(f"{root / 'benchmark.yaml'}: tasks must contain exactly {sorted(TASK_IDS)}")
    tasks: list[dict[str, Any]] = []
    for entry in data["tasks"]:
        task_path = safe_benchmark_path(root, entry["task"], label=f"task {entry['id']}")
        task = safe_load(task_path.read_text(encoding="utf-8"))
        task_errors = _schema_errors(task, TASK_SCHEMA)
        if task_errors:
            raise ValueError(f"{task_path}: " + "; ".join(task_errors))
        if task["id"] != f"benchmark-{entry['id']}":
            raise ValueError(f"{task_path}: task id does not match benchmark task {entry['id']}")
        tasks.append({"entry": entry, "path": task_path, "task": task})
    rubric_path = safe_benchmark_path(root, data["rubric"], label="rubric")
    rubric = safe_load(rubric_path.read_text(encoding="utf-8"))
    _validate_rubric(rubric, rubric_path)
    return {"root": root, "package_root": package_root, "package": package, "benchmark": data, "tasks": tasks, "rubric": rubric, "rubric_path": rubric_path}


def _validate_rubric(rubric: Any, path: Path) -> None:
    if not isinstance(rubric, dict):
        raise ValueError(f"{path}: rubric must be a YAML object")
    metrics = rubric.get("task_metrics")
    required = {str(metric.get("id")) for metric in metrics or [] if isinstance(metric, dict)}
    expected = {"style_recognition", "object_completion", "prompt_adherence", "color_fidelity", "material_correctness", "composition_stability", "ai_trace_control"}
    if required != expected:
        raise ValueError(f"{path}: task_metrics must contain exactly {sorted(expected)}")
    weights = [float(metric["weight"]) for metric in metrics]
    if abs(sum(weights) - 1.0) > 1e-6:
        raise ValueError(f"{path}: task metric weights must sum to 1.0")


def compile_benchmark(path: Path, model: str, profile: str = "weak", run_id: str | None = None) -> dict[str, Any]:
    runtime = load_benchmark(path)
    package = runtime["package"]
    slug = re.sub(r"[^a-z0-9]+", "-", f"{package['id']}-{model}".lower()).strip("-")
    run_id = run_id or f"{slug}-visual-style-core-v1"
    compiled_tasks: list[dict[str, Any]] = []
    for item in runtime["tasks"]:
        task = item["task"]
        job = compile_job(runtime["package_root"], task["subject"], profile=profile, model=model, reference_set="all")
        if task.get("brief"):
            job["prompt"] += f"\n\nTASK BRIEF:\n{task['brief']}"
        job["benchmark_task"] = {"id": item["entry"]["id"], "kind": item["entry"]["kind"], "task_path": str(item["path"])}
        compiled_tasks.append({"task_id": item["entry"]["id"], "kind": item["entry"]["kind"], "task_path": str(item["path"]), "image": None, "job": job})
    result = {
        "schema_version": "1.0.0",
        "run_id": run_id,
        "benchmark_id": runtime["benchmark"]["benchmark_id"],
        "package": {"id": package["id"], "version": package["version"]},
        "model": {"name": model, "profile": profile},
        "status": "awaiting_render",
        "tasks": compiled_tasks,
    }
    errors = _schema_errors(result, RUN_SCHEMA)
    if errors:
        raise ValueError("Compiled benchmark run is invalid: " + "; ".join(errors))
    return result
