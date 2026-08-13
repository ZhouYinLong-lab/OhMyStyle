# OhMyStyle Skill interfaces

The OhMyStyle Skill is a multi-turn style orchestration interface. It does not turn one sentence directly into a generation Prompt. It first confirms the content and details, matches candidates from `style-packages/`, waits for the user's selection, and then calls the existing style runtime to compile a job.

## Three entrypoints

| Entry point | Start with | Session storage | Best for |
| --- | --- | --- | --- |
| Agent file interface | Read the root `SKILL.md` and read/write JSON sessions | A user-selected JSON file | ChatGPT, Claude Code, other Agents |
| Local CLI | `python tools/ohmystyle.py ...` | Local session JSON | Scripts, batch jobs, local models |
| HTTP / MCP | `python tools/ohmystyle_http.py` / `python tools/ohmystyle_mcp.py` | In-process HTTP memory / MCP client session | Tool calls and local applications |

All three entrypoints use `tools/ohmystyle_core.py`, so the confirmation order and safety gates stay identical.

## Remote repository mode

You can provide the GitHub repository URL without manually cloning it. Use an HTTPS URL with a fixed `ref` or commit:

```json
{
  "url": "https://github.com/ZhouYinLong-lab/OhMyStyle",
  "ref": "main"
}
```

The CLI downloads and caches the source archive, then uses the same style-package loader as a local checkout. For production, pin an immutable commit and provide the archive `sha256`. The remote repository supplies project code and style data; it is never executed as a Provider command.

HTTP and MCP servers load repository and Provider configuration at startup. Clients cannot submit a repository, shell command, or API key through a request. MCP clients cannot submit a Provider.

## Session phases

```text
content_confirmation
  → detail_confirmation
  → style_matching
  → style_confirmation
  → ready
  → compiled
  → generated / review
```

No generation is allowed before `ready`, and an unconfirmed style cannot enter the job. The default provider is `provider-neutral`, which returns a job JSON only. A user-managed provider is required for actual generation.

## CLI, HTTP, and MCP usage

See the Chinese README in this directory and the root `SKILL.md` for command examples, HTTP routes, MCP tools, and provider boundaries. The interfaces do not store model accounts or API keys in the repository.

The HTTP service must load a provider configuration at startup; clients cannot submit arbitrary commands. Keep the service on localhost unless authentication, rate limiting, persistence, and HTTPS are added.
