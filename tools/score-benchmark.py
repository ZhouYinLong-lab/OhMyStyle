#!/usr/bin/env python3
"""Score a rendered benchmark run from a structured human/vision review file."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from benchmark_runtime import load_benchmark
from safe_yaml import safe_load


TASK_METRICS = [
    "style_recognition",
    "object_completion",
    "prompt_adherence",
    "color_fidelity",
    "material_correctness",
    "composition_stability",
    "ai_trace_control",
]


def load_data(path: Path) -> Any:
    if path.suffix.lower() == ".json":
        return json.loads(path.read_text(encoding="utf-8"))
    return safe_load(path.read_text(encoding="utf-8"))


def score_run(run_path: Path, scores_path: Path) -> dict[str, Any]:
    run = load_data(run_path)
    scores = load_data(scores_path)
    if not isinstance(run, dict) or not isinstance(scores, dict):
        raise ValueError("Run and score files must be objects")
    if run.get("run_id") != scores.get("run_id"):
        raise ValueError("Score run_id must match benchmark run run_id")
    benchmark = load_benchmark(Path(run["tasks"][0]["job"]["package"]["root"]) / "benchmark")
    score_tasks = scores.get("tasks")
    if not isinstance(score_tasks, dict):
        raise ValueError("scores.tasks must map task_id to a review object")
    results: list[dict[str, Any]] = []
    weights = {metric["id"]: float(metric["weight"]) for metric in benchmark["rubric"]["task_metrics"]}
    for task in run["tasks"]:
        task_id = task["task_id"]
        review = score_tasks.get(task_id)
        if not isinstance(review, dict):
            raise ValueError(f"Missing score entry for task {task_id}")
        values = review.get("scores")
        if not isinstance(values, dict) or set(values) != set(TASK_METRICS):
            raise ValueError(f"Task {task_id} must score exactly {TASK_METRICS}")
        for metric in TASK_METRICS:
            value = values[metric]
            if not isinstance(value, (int, float)) or isinstance(value, bool) or not 0 <= float(value) <= 5:
                raise ValueError(f"Task {task_id} metric {metric} must be between 0 and 5")
        task_score = sum(float(values[metric]) * weights[metric] for metric in TASK_METRICS)
        results.append({"task_id": task_id, "score": round(task_score, 4), "scores": values, "artifact_findings": review.get("artifact_findings", {})})
    overall = sum(item["score"] for item in results) / len(results)
    minimum_overall = float(benchmark["benchmark"].get("minimum_overall_score", 3.5))
    minimum_task = float(benchmark["benchmark"].get("minimum_task_score", 3.0))
    status = "pass" if overall >= minimum_overall and min(item["score"] for item in results) >= minimum_task else "fail"
    return {
        "schema_version": "1.0.0",
        "run_id": run["run_id"],
        "benchmark_id": run["benchmark_id"],
        "package": run["package"]["id"],
        "model": run["model"]["name"],
        "status": status,
        "tasks": results,
        "overall_score": round(overall, 4),
        "thresholds": {"minimum_overall_score": minimum_overall, "minimum_task_score": minimum_task},
        "reviewer": scores.get("reviewer", "unspecified"),
        "notes": scores.get("notes", "Scores are evidence-backed observations, not an objective artist-authorship detector."),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run", type=Path)
    parser.add_argument("scores", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = score_run(args.run, args.scores)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {args.output} ({report['status']}, overall={report['overall_score']})")


if __name__ == "__main__":
    main()
