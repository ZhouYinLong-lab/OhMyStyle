from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from benchmark_runtime import compile_benchmark, load_benchmark


def load_tool(filename: str, module_name: str):
    spec = importlib.util.spec_from_file_location(module_name, ROOT / "tools" / filename)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


score_tool = load_tool("score-benchmark.py", "score_benchmark")
aggregate_tool = load_tool("aggregate-benchmark.py", "aggregate_benchmark")


class BenchmarkRuntimeTests(unittest.TestCase):
    def test_pilot_manifests_have_the_fixed_five_task_suite(self):
        paths = [
            ROOT / "style-packages/artists/jmw-turner/benchmark",
            ROOT / "style-packages/artists/johannes-vermeer/benchmark",
            ROOT / "style-packages/game-art/rpg-maker-pixel-art/benchmark",
        ]
        for path in paths:
            benchmark = load_benchmark(path)
            self.assertEqual({task["entry"]["id"] for task in benchmark["tasks"]}, {"portrait", "still-life", "architecture-environment", "minimal-composition", "fuzzy-brief"})

    def test_runner_compiles_five_provider_neutral_jobs(self):
        run = compile_benchmark(ROOT / "style-packages/artists/jmw-turner/benchmark", "test-model", run_id="turner-test")
        self.assertEqual(run["status"], "awaiting_render")
        self.assertEqual(len(run["tasks"]), 5)
        self.assertTrue(all(task["job"]["prompt"] for task in run["tasks"]))

    def test_score_and_cross_model_aggregate(self):
        score_values = {
            "style_recognition": 4,
            "object_completion": 4,
            "prompt_adherence": 4,
            "color_fidelity": 4,
            "material_correctness": 4,
            "composition_stability": 4,
            "ai_trace_control": 4,
        }
        with tempfile.TemporaryDirectory() as temp:
            temp_root = Path(temp)
            reports = []
            for index, model in enumerate(("model-a", "model-b")):
                run = compile_benchmark(ROOT / "style-packages/artists/jmw-turner/benchmark", model, run_id=f"turner-test-{index}")
                run_path = temp_root / f"run-{index}.json"
                score_path = temp_root / f"scores-{index}.json"
                report_path = temp_root / f"report-{index}.json"
                run_path.write_text(json.dumps(run), encoding="utf-8")
                score_path.write_text(json.dumps({"run_id": run["run_id"], "reviewer": "synthetic-fixture", "tasks": {task["task_id"]: {"scores": score_values, "artifact_findings": {}} for task in run["tasks"]}}), encoding="utf-8")
                report = score_tool.score_run(run_path, score_path)
                report_path.write_text(json.dumps(report), encoding="utf-8")
                reports.append(report_path)
                self.assertEqual(report["status"], "pass")
            aggregate = aggregate_tool.aggregate(reports)
            self.assertEqual(aggregate["status"], "ready_for_L4_review")
            self.assertEqual(aggregate["cross_model_stability"]["proxy_score"], 5.0)


if __name__ == "__main__":
    unittest.main()
