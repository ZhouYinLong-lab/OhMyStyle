from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tools" / "new-style-package.py"


class StylePackageScaffoldTests(unittest.TestCase):
    def run_scaffold(self, root: Path, *extra: str) -> subprocess.CompletedProcess[str]:
        command = [
            sys.executable, str(SCRIPT), "--kind", "artist", "--id", "scaffold-test",
            "--name", "脚手架测试风格", "--domain", "painting",
            "--summary", "这是一个用于测试风格包创建、文件结构、来源边界和贡献流程的独立示例包。",
            "--root", str(root), *extra,
        ]
        return subprocess.run(command, cwd=ROOT, text=True, capture_output=True, check=False)

    def test_scaffold_creates_complete_l1_package(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = self.run_scaffold(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            package = root / "artists" / "scaffold-test"
            required = {
                "package.yaml", "identity.yaml", "visual-signature.yaml", "reproduction.yaml",
                "relations.yaml", "evaluation.yaml", "provenance.yaml", "resource.yaml",
                "README.md", "README.en.md", "version.md", "gallery-16x9.svg", "palette/palette.json",
                "prompts/base.txt", "prompts/negative.txt", "references/manifest.csv",
                "references/primary/README.md", "references/secondary/README.md",
                "references/details/README.md", "examples/generated/README.md",
                "examples/generated/sample.yaml", "examples/accepted/README.md",
                "examples/rejected/README.md",
            }
            actual = {path.relative_to(package).as_posix() for path in package.rglob("*") if path.is_file()}
            self.assertEqual(actual, required)
            resource_data = yaml.safe_load((package / "resource.yaml").read_text(encoding="utf-8"))
            self.assertEqual(resource_data["maturity"], "L1")
            self.assertFalse(resource_data["evidence"]["reference_backed"])
            text_files = [path for path in package.rglob("*") if path.is_file() and path.suffix != ".svg"]
            self.assertFalse(any("{{" in path.read_text(encoding="utf-8") for path in text_files))

    def test_source_metadata_creates_l2_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = self.run_scaffold(
                root, "--source-url", "https://example.org/source", "--source-title", "Example source",
                "--source-creator", "Example institution", "--source-attribution", "Example institution",
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            package = root / "artists" / "scaffold-test"
            resource = yaml.safe_load((package / "resource.yaml").read_text(encoding="utf-8"))
            self.assertEqual(resource["maturity"], "L2")
            self.assertTrue(resource["evidence"]["reference_backed"])
            manifest = (package / "references" / "manifest.csv").read_text(encoding="utf-8")
            self.assertIn("https://example.org/source", manifest)
            self.assertIn("Example institution", manifest)

    def test_generated_package_yaml_matches_schema(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            result = self.run_scaffold(root)
            self.assertEqual(result.returncode, 0, result.stderr)
            package = root / "artists" / "scaffold-test"
            schema = json.loads((ROOT / "schema/package.schema.json").read_text(encoding="utf-8"))
            data = yaml.safe_load((package / "package.yaml").read_text(encoding="utf-8"))
            self.assertEqual(list(Draft202012Validator(schema).iter_errors(data)), [])
            resource_schema = json.loads((ROOT / "schema/resource.schema.json").read_text(encoding="utf-8"))
            resource = yaml.safe_load((package / "resource.yaml").read_text(encoding="utf-8"))
            self.assertEqual(list(Draft202012Validator(resource_schema).iter_errors(resource)), [])

    def test_existing_target_is_never_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            first = self.run_scaffold(root)
            self.assertEqual(first.returncode, 0, first.stderr)
            second = self.run_scaffold(root)
            self.assertNotEqual(second.returncode, 0)
            self.assertIn("already exists", second.stderr)


if __name__ == "__main__":
    unittest.main()
