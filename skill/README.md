# OhMyStyle Skill 接口

OhMyStyle Skill 是一个多轮确认式的风格编排接口。它不把用户的一句话直接变成生图 Prompt，而是先确认内容和细节，再从 `style-packages/` 匹配候选，等待用户选择，最后调用现有风格运行时编译任务。

## 三种入口

| 入口 | 启动方式 | 会话存储 | 适合场景 |
| --- | --- | --- | --- |
| Agent 文件接口 | 阅读根目录 `SKILL.md`，读写 JSON 会话 | 用户指定的 JSON 文件 | ChatGPT、Claude Code、其他 Agent |
| 本地 CLI | `python tools/ohmystyle.py ...` | 本地会话 JSON | 脚本、批处理、本地模型 |
| HTTP / MCP | `python tools/ohmystyle_http.py` / `python tools/ohmystyle_mcp.py` | HTTP 进程内存 / MCP 客户端会话 | Agent 工具调用和本地应用 |

三种入口都使用 `tools/ohmystyle_core.py`，所以确认顺序和安全门一致。

## 远程仓库模式

可以直接提供 GitHub 仓库地址，不必手动 Clone。使用 HTTPS 地址和固定的 `ref` 或 commit：

```json
{
  "url": "https://github.com/ZhouYinLong-lab/OhMyStyle",
  "ref": "main"
}
```

CLI 会下载并缓存源码压缩包，再使用与本地仓库相同的风格包加载器。生产环境建议固定不可变 commit，并填写压缩包 `sha256`。远程仓库只提供项目代码与风格资料，不会被当作 Provider 命令执行。

HTTP 和 MCP 服务从启动参数读取仓库与 Provider 配置；客户端不能通过请求提交仓库、Shell 命令或 API Key。

## 会话阶段

```text
content_confirmation
  → detail_confirmation
  → style_matching
  → style_confirmation
  → ready
  → compiled
  → generated / review
```

`ready` 之前不会生成；没有用户确认的风格不会进入任务。默认生成 Provider 是 `provider-neutral`，只返回任务 JSON。要真正生成，用户必须自行配置 Provider。

## CLI 示例

```powershell
python tools/ohmystyle.py init --brief "做一张安静的临海建筑图" --output session.json
python tools/ohmystyle.py turn --session session.json --json '{"content":{"subject":"一座临海建筑","purpose":"杂志封面"},"confirmed":true}'
python tools/ohmystyle.py turn --session session.json --json '{"details":{"aspect_ratio":"16:9","lighting":"阴天自然光"},"confirmed":true}'
python tools/ohmystyle.py match --session session.json --limit 5
python tools/ohmystyle.py turn --session session.json --json '{"style_selection":{"package":"style-packages/artists/jmw-turner"},"confirmed":true}'
python tools/ohmystyle.py compile --session session.json --output job.json
python tools/ohmystyle.py generate --session session.json
```

## HTTP 接口

HTTP 服务默认只监听 `127.0.0.1`，不要直接暴露到公网；生产部署需要自行增加认证、限流、持久化和 HTTPS。真正的 Provider 应通过服务启动参数配置，HTTP 请求不能提交任意命令。

```powershell
python tools/ohmystyle_http.py --host 127.0.0.1 --port 8765 --provider-config skill/provider.example.json
```

核心路由：

```text
POST /sessions                       创建会话
GET  /sessions/{id}                  查看阶段和待确认问题
POST /sessions/{id}/turn             提交一轮确认
POST /sessions/{id}/match            生成风格候选
POST /sessions/{id}/compile          编译 provider-neutral 任务
POST /sessions/{id}/generate         调用用户提供的 Provider
```

HTTP 请求示例：

```powershell
$session = Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8765/sessions -ContentType application/json -Body '{"brief":"做一张安静的建筑图"}'
$id = $session.session.session_id
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8765/sessions/$id/turn" -ContentType application/json -Body '{"content":{"subject":"一座建筑","purpose":"杂志封面"},"confirmed":true}'
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8765/sessions/$id/turn" -ContentType application/json -Body '{"details":{"aspect_ratio":"16:9"},"confirmed":true}'
Invoke-RestMethod -Method Post -Uri "http://127.0.0.1:8765/sessions/$id/match" -ContentType application/json -Body '{}'
```

## MCP 接口

```powershell
python tools/ohmystyle_mcp.py
```

这是一个 JSON-RPC stdio 服务，提供：

- `ohmystyle_start_session`
- `ohmystyle_turn`
- `ohmystyle_match_styles`
- `ohmystyle_compile`
- `ohmystyle_generate`

它不在仓库内保存模型账号或 API Key。MCP 服务端应通过启动参数加载 Provider；客户端不能提交 Provider。
