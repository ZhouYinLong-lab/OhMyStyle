from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
SPEC = importlib.util.spec_from_file_location("ohmystyle_mcp", ROOT / "tools" / "ohmystyle_mcp.py")
assert SPEC and SPEC.loader
MCP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MCP)


class OhMyStyleMCPTests(unittest.TestCase):
    def test_lists_tools(self) -> None:
        response = MCP.handle({"jsonrpc": "2.0", "id": 1, "method": "tools/list"})
        self.assertEqual(response["result"]["content"][0]["type"], "text")
        payload = json.loads(response["result"]["content"][0]["text"])
        self.assertIn("ohmystyle_start_session", {item["name"] for item in payload["tools"]})

    def test_starts_session(self) -> None:
        response = MCP.handle({"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "ohmystyle_start_session", "arguments": {"brief": "测试"}}})
        payload = json.loads(response["result"]["content"][0]["text"])
        self.assertEqual(payload["session"]["phase"], "content_confirmation")


if __name__ == "__main__":
    unittest.main()
