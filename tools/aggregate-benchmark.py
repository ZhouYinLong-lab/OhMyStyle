#!/usr/bin/env python3
"""Aggregate score reports across models and expose cross-model stability."""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from pathlib import Path
from typing import Any


def load(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"Report must be an object: {path}")
    return data


def mean(values: list[float]) -> float:
    return sum(values) / len(values) if values else 0.0


def stdev(values: list[float]) -> float:
    if len(values) < 2:
        return 0.0
    average = mean(values)
    return math.sqrt(sum((value - average) ** 2 for value in values) / len(values))


def aggregate(paths: list[Path]) -> dict[str, Any]:
    reports = [load(path) for path in paths]
    package_ids = {report.get("package") for report in reports}
    benchmark_ids = {report.get("benchmark_id") for report in reports}
    if len(package_ids) != 1 or len(benchmark_ids) != 1:
        raise ValueError("All score reports must belong to one package and benchmark")
    models = sorted({str(report.get("model")) for report in reports})
    task_values: dict[str, dict[str, list[float]]] = defaultdict(lambda: defaultdict(list))
    overall_values: list[float] = []
    for report in reports:
        overall_values.append(float(report["overall_score"]))
        for task in report["tasks"]:
            for metric, value in task["scores"].items():
                task_values[task["task_id"]][metric].append(float(value))
    task_summary: dict[str, Any] = {}
    for task_id, metrics in sorted(task_values.items()):
        task_summary[task_id] = {metric: {"mean": round(mean(values), 4), "stddev": round(stdev(values), 4), "n": len(values)} for metric, values in sorted(metrics.items())}
    overall_stddev = stdev(overall_values)
    stability_proxy = max(0.0, min(5.0, 5.0 - (2.0 * overall_stddev)))
    thresholds = reports[0].get("thresholds", {})
    complete = len(models) >= 2 and all(report.get("status") == "pass" for report in reports)
    return {
        "schema_version": "1.0.0",
        "benchmark_id": next(iter(benchmark_ids)),
        "package": next(iter(package_ids)),
        "models": models,
        "report_count": len(reports),
        "status": "ready_for_L4_review" if complete and stability_proxy >= 3.5 else "needs_more_evidence",
        "overall": {"mean": round(mean(overall_values), 4), "stddev": round(overall_stddev, 4), "n": len(overall_values)},
        "cross_model_stability": {"proxy_score": round(stability_proxy, 4), "method": "max(0, 5 - 2 * overall_score_stddev); human review remains authoritative"},
        "task_metrics": task_summary,
        "thresholds": thresholds,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reports", nargs="+", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = aggregate(args.reports)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE: {args.output} ({report['status']})")


if __name__ == "__main__":
    main()
