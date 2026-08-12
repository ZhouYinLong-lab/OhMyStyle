from __future__ import annotations

import json
import threading
import unittest
from http.client import HTTPConnection


import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from ohmystyle_http import Handler, STORE  # noqa: E402
from http.server import ThreadingHTTPServer


class OhMyStyleHTTPTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def request(self, method: str, path: str, body: dict | None = None) -> tuple[int, dict]:
        connection = HTTPConnection("127.0.0.1", self.server.server_port)
        payload = json.dumps(body or {}).encode("utf-8")
        connection.request(method, path, payload, {"Content-Type": "application/json"})
        response = connection.getresponse()
        data = json.loads(response.read().decode("utf-8"))
        connection.close()
        return response.status, data

    def test_session_lifecycle_stops_before_generation_until_confirmed(self) -> None:
        status, created = self.request("POST", "/sessions", {"brief": "测试风格匹配"})
        self.assertEqual(status, 201)
        session_id = created["session"]["session_id"]
        status, blocked = self.request("POST", f"/sessions/{session_id}/compile")
        self.assertEqual(status, 400)
        self.assertIn("not ready", blocked["error"])

    def test_health_route(self) -> None:
        status, data = self.request("GET", "/")
        self.assertEqual(status, 200)
        self.assertEqual(data["status"], "ok")

    def test_http_rejects_client_command_provider(self) -> None:
        status, created = self.request("POST", "/sessions", {"brief": "测试"})
        session_id = created["session"]["session_id"]
        status, data = self.request("POST", f"/sessions/{session_id}/generate", {"provider": {"type": "command", "command": ["powershell", "-Command", "whoami"]}})
        self.assertEqual(status, 400)
        self.assertIn("cannot submit providers", data["error"])


if __name__ == "__main__":
    unittest.main()
