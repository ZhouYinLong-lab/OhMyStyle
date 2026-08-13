#!/usr/bin/env python3
"""Local CLI and file interface for the OhMyStyle Skill."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from ohmystyle_core import advance, compile_session, generate_session, match_styles, new_session, session_view


def read_json(value: str | None, path: Path | None) -> dict:
    if path:
        return json.loads(path.read_text(encoding="utf-8"))
    if value:
        return json.loads(value)
    return {}


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    init = sub.add_parser("init", help="Create a multi-turn session file")
    init.add_argument("--brief", default="")
    init.add_argument("--session-id")
    init.add_argument("--repository", type=Path, help="JSON remote repository config")
    init.add_argument("--repo-url", help="HTTPS GitHub repository URL")
    init.add_argument("--ref", default="main", help="GitHub branch, tag, or commit")
    init.add_argument("--sha256", help="Expected SHA-256 of the downloaded archive")
    init.add_argument("--output", type=Path, required=True)
    for name in ("turn", "view", "match", "compile", "generate"):
        command = sub.add_parser(name)
        command.add_argument("--session", type=Path, required=True)
        if name == "turn":
            command.add_argument("--json")
            command.add_argument("--input", type=Path)
        if name == "match":
            command.add_argument("--limit", type=int, default=5)
        if name == "compile":
            command.add_argument("--model", default="provider-neutral")
            command.add_argument("--output", type=Path)
        if name == "generate":
            command.add_argument("--provider", type=Path, help="JSON provider config")
    args = parser.parse_args()
    if args.command == "init":
        repository = read_json(None, args.repository) if args.repository else None
        if args.repo_url:
            if repository:
                parser.error("use either --repository or --repo-url, not both")
            repository = {"url": args.repo_url, "ref": args.ref}
            if args.sha256:
                repository["sha256"] = args.sha256
        data = new_session(args.brief, args.session_id, repository)
        write_json(args.output, data)
        print(json.dumps(session_view(data), ensure_ascii=False, indent=2))
        return
    session = json.loads(args.session.read_text(encoding="utf-8"))
    if args.command == "turn":
        data = advance(session, read_json(args.json, args.input))
        write_json(args.session, data)
        print(json.dumps(session_view(data), ensure_ascii=False, indent=2))
    elif args.command == "view":
        print(json.dumps(session_view(session), ensure_ascii=False, indent=2))
    elif args.command == "match":
        data = match_styles(
            session.get("brief", ""),
            {**session.get("content", {}), **session.get("details", {})},
            args.limit,
            session.get("repository"),
        )
        session["style_candidates"] = data
        session["phase"] = "style_confirmation"
        write_json(args.session, session)
        print(json.dumps(data, ensure_ascii=False, indent=2))
    elif args.command == "compile":
        job = compile_session(session, args.model)
        write_json(args.session, session)
        if args.output:
            write_json(args.output, job)
            print(f"WROTE: {args.output}")
        else:
            print(json.dumps(job, ensure_ascii=False, indent=2))
    elif args.command == "generate":
        provider = read_json(None, args.provider) if args.provider else None
        result = generate_session(session, provider)
        write_json(args.session, session)
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
