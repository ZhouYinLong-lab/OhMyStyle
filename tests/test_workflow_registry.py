from __future__ import annotations

import sys
import tempfile
import unittest
import importlib.util
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

_SPEC = importlib.util.spec_from_file_location("validate_workflow", ROOT / "tools" / "validate-workflow.py")
assert _SPEC and _SPEC.loader
_MODULE = importlib.util.module_from_spec(_SPEC)
_SPEC.loader.exec_module(_MODULE)
load_yaml = _MODULE.load_yaml
validate_all = _MODULE.validate_all
validate_integration_manifest = _MODULE.validate_integration_manifest


class WorkflowRegistryTests(unittest.TestCase):
    def test_bundled_workflows_validate(self) -> None:
        self.assertEqual(validate_all(ROOT / "workflows", ROOT / "integrations"), [])

    def test_workflows_keep_subjects_open(self) -> None:
        for path in sorted((ROOT / "workflows").glob("*/workflow.yaml")):
            data = load_yaml(path)
            self.assertEqual(data["subject_policy"]["default_subjects"], [])
            self.assertIn("source_subject_identity", data["style_projection"]["protected_axes"])
            self.assertIn("user_subject_constraints", data["style_projection"]["protected_axes"])

    def test_external_manifests_do_not_bundle_upstream_material(self) -> None:
        for path in sorted((ROOT / "integrations").glob("*.yaml")):
            data = load_yaml(path)
            self.assertTrue(data["external_only"])
            self.assertFalse(data["copy_upstream_materials"])

    def test_integration_cannot_reference_outside_workflow_root(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.yaml"
            path.write_text(
                """id: bad\nkind: external_workflow\nexternal_only: true\ncopy_upstream_materials: false\nupstream_url: https://github.com/example/project\nworkflow_ref: ../README.md\nlicense:\n  url: https://example.com/license\ninstallation: user_managed_external\n""",
                encoding="utf-8",
            )
            errors = validate_integration_manifest(path, ROOT / "workflows")
            self.assertTrue(any("workflow_ref" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
