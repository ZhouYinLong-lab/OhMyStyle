from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class RemoteCliTests(unittest.TestCase):
    def test_init_accepts_direct_repository_url_without_downloading(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "session.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(ROOT / "tools/ohmystyle.py"),
                    "init",
                    "--repo-url",
                    "https://github.com/example/OhMyStyle",
                    "--ref",
                    "main",
                    "--brief",
                    "测试",
                    "--output",
                    str(output),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stderr)
            session = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(session["repository"]["url"], "https://github.com/example/OhMyStyle")
            self.assertEqual(session["repository"]["ref"], "main")


if __name__ == "__main__":
    unittest.main()
