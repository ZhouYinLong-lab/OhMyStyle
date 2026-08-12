from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))


def load_module(name: str, filename: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools" / filename)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


core = load_module("ohmystyle_core", "ohmystyle_core.py")


class OhMyStyleSkillTests(unittest.TestCase):
    def complete_session(self) -> dict:
        session = core.new_session("安静的临海建筑杂志封面")
        session = core.advance(session, {"content": {"subject": "一座临海建筑", "purpose": "杂志封面"}, "confirmed": True})
        session = core.advance(session, {"details": {"aspect_ratio": "16:9", "lighting": "阴天自然光"}, "confirmed": True})
        self.assertEqual(session["phase"], "style_matching")
        session = core.advance(session, {})
        self.assertEqual(session["phase"], "style_confirmation")
        session = core.advance(session, {"style_selection": {"package": "style-packages/artists/jmw-turner"}, "confirmed": True})
        return session

    def test_session_requires_each_confirmation_gate(self) -> None:
        session = core.new_session("测试")
        with self.assertRaises(ValueError):
            core.compile_session(session)
        session = core.advance(session, {"content": {"subject": "一把椅子"}, "confirmed": True})
        with self.assertRaises(ValueError):
            core.compile_session(session)

    def test_confirmed_session_compiles_with_existing_runtime(self) -> None:
        session = self.complete_session()
        job = core.compile_session(session)
        self.assertEqual(session["phase"], "compiled")
        self.assertEqual(job["job_type"], "style_render")
        self.assertEqual(job["subject"], "一座临海建筑")
        self.assertEqual(job["session_id"], session["session_id"])

    def test_provider_neutral_generation_is_explicitly_not_completed(self) -> None:
        session = self.complete_session()
        core.compile_session(session)
        result = core.generate_session(session)
        self.assertEqual(result["status"], "awaiting_provider")
        self.assertEqual(session["phase"], "compiled")

    def test_style_reference_cannot_escape_style_root(self) -> None:
        with self.assertRaises(FileNotFoundError):
            core.resolve_style_reference("../README.md")

    def test_style_reference_accepts_package_id(self) -> None:
        self.assertTrue(core.resolve_style_reference("jmw-turner").is_dir())

    def test_composite_reference_compiles(self) -> None:
        session = core.new_session("像素前景和绘画背景")
        session = core.advance(session, {"content": {"subject": "一片山谷", "purpose": "概念图"}, "confirmed": True})
        session = core.advance(session, {"details": {"aspect_ratio": "16:9"}, "confirmed": True})
        session = core.advance(session, {})
        session = core.advance(session, {"style_selection": {"package": "style-packages/composites/rpg-maker-x-gauguin"}, "confirmed": True})
        job = core.compile_session(session)
        self.assertEqual(job["job_type"], "composite_style_render")

    def test_command_provider_receives_job_file(self) -> None:
        session = self.complete_session()
        core.compile_session(session)
        with tempfile.TemporaryDirectory() as directory:
            script = Path(directory) / "provider.py"
            output = Path(directory) / "received.json"
            script.write_text(
                "import json, pathlib, sys\n"
                f"pathlib.Path({str(output)!r}).write_text(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'), encoding='utf-8')\n",
                encoding="utf-8",
            )
            result = core.generate_session(session, {"type": "command", "command": [sys.executable, str(script)], "output_dir": directory})
            self.assertEqual(result["status"], "completed")
            self.assertEqual(json.loads(output.read_text(encoding="utf-8"))["session_id"], session["session_id"])

    def test_http_json_provider_sends_compiled_job(self) -> None:
        session = self.complete_session()
        core.compile_session(session)
        import http.server
        import threading

        received: list[dict] = []

        class Provider(http.server.BaseHTTPRequestHandler):
            def do_POST(self):  # noqa: N802
                length = int(self.headers["Content-Length"])
                received.append(json.loads(self.rfile.read(length).decode("utf-8")))
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(b'{"image_url":"http://example.test/image.png"}')

            def log_message(self, format, *args):
                return

        server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Provider)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            result = core.generate_session(session, {"type": "http_json", "url": f"http://127.0.0.1:{server.server_port}/generate"})
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=2)
        self.assertEqual(result["status"], "completed")
        self.assertEqual(received[0]["session_id"], session["session_id"])


if __name__ == "__main__":
    unittest.main()
