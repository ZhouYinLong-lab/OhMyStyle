# 美术风格包 v2：独立试点

状态：可运行的实验入口，尚未完成跨题材生图对照。三个方向都是人工整理的试点，正式风格包未批量迁移。

## 版本保留与回退

| 版本 | Git 引用 | 用途 |
| --- | --- | --- |
| 旧版快照 | `style-v1-snapshot-2026-10-18` | 固定在 `59d9aa10ee9eeaedf3b815688d00f3e553ef31ea`，已推送远端 |
| 旧版保留分支 | `codex/style-v1-preserved` | 固定在旧版基线，用于查看与对照 |
| 当前主分支 | `main` | 包含架构设计、试点、编译入口与字符渲染器；后续开发继续在此推进 |
| 初始实施分支 | `codex/style-pack-v2` | 保留最初实施历史，改动已进入 `main` |

快照保存 Git 跟踪的内容；被忽略的本地候选图片和运行结果不在 Git 快照内。实施分支另行提交了快照时的架构设计文档，并修复 American Luminism 来源标题缺少引号的问题。

在仓库根目录执行以下命令，可在相邻目录打开独立旧版工作区。目录应尚不存在：

~~~powershell
git worktree add --detach ../OhMyStyle-v1 style-v1-snapshot-2026-10-18
~~~

旧版快照保留原有 American Luminism YAML 解析问题，便于准确还原当时状态。无需重置或删除当前工作区。若当前工作区干净，也可以用 `git switch codex/style-v1-preserved` 查看旧版，用 `git switch main` 返回当前开发版本。旧版分支和标签保留为对照基线，后续开发以 `main` 为准。

## 实际落地的结构

~~~text
experiments/style-v2/<direction>/direction.yaml
  base_package       指定复用哪个正式包
  scope              媒介、再现方式、适用边界与明确声明的上下文
  pillars            编辑意图，保留供人工阅读
  rules              指令、观察标准、失败条件、来源及证据性质
  active_rule_ids    人工选定本方向采用的规则
  joint_checks       多条规则如何共同组织同一画面
  sources            机构资料、正式包来源记录或项目原始文件
  execution          文本生图或严格字符网格路线，以及制作约束
~~~

- 正式契约：[art-direction.schema.json](../../schema/art-direction.schema.json)。字段错误、未知规则、缺失来源、核心规则未启用、联动引用错误和包路径不匹配会拒绝编译。
- 编译只将启用规则的 `instruction`、联动 `instruction`、媒介与执行约束写入 Prompt。`observable`、`reject_when` 和来源留在 `review` 中；显式 `avoid` 写入负面 Prompt。
- `applies_when` 是编辑说明，不会被程序理解为条件表达式。当前用人工整理的规则集合和调用者声明的上下文控制适用范围；不会自动识别主体语句里的夜景等冲突。
- 研究来源不自动作为图片输入。第一阶段仅支持 `references=none`、`profile=generic`，不使用旧版调色对；不支持的组合会明确拒绝。
- 新入口必须显式传入 `--direction`。省略时沿用旧版编译路径及默认参考选择。实验目录不参与正式包检索，也不自动进入画廊。
- 本阶段接入命令行与 Python 编译接口，HTTP、MCP 会话和组合包仍使用旧版路径。任务文件不是自动调用生图服务的承诺。

相对于 [总体设计草案](../../docs/ART-STYLE-PACK-ARCHITECTURE.md)，这份文件是最小实施契约。设计样稿与运行文件分开，避免把尚未支持的字段当作已执行能力。

## 三个试点

| 方向 | 选定范围 | 制作路线 | 必须声明的上下文 |
| --- | --- | --- | --- |
| [索罗亚日光油画](sorolla-sunlit-oil/direction.yaml) | 光线、反射色、笔触与体块的联动 | text_only | daylight |
| [包豪斯纸材研究](bauhaus-paper-study/direction.yaml) | 具体纸材课程方法的当代转译 | text_only | paper-study |
| [严格 ASCII 网格](literal-ascii-grid/direction.yaml) | 全部场景形状由真实字符构成 | deterministic_grid | 无 |

命令在仓库根目录运行，依赖沿用 `requirements-dev.txt`（PyYAML、jsonschema、Pillow）。需要时先执行 `python -m pip install -r requirements-dev.txt`。

### 索罗亚：先编译规则任务

~~~powershell
python tools/compile-style.py style-packages/artists/joaquin-sorolla --direction experiments/style-v2/sorolla-sunlit-oil --context daylight --subject "Two folded blue cloths and a white bowl on an outdoor table in daylight" --output runs/style-v2/sorolla-job.json
~~~

输出任务的 `prompt` 和 `negative_prompt` 可交给你选定的图像模型。此处不下载或上传研究来源图片。`review` 保存规则检查项与来源 ID，方便对照结果时逐项记录。

### 包豪斯：明确是纸材方法

~~~powershell
python tools/compile-style.py style-packages/schools/bauhaus --direction experiments/style-v2/bauhaus-paper-study --context paper-study --subject "A small paper pavilion made from one sheet using cuts and folds, with an opening and visible supports" --output runs/style-v2/paper-job.json
~~~

生成图只用于研究结构的视觉表达，不能据此确认真实折叠或承重可行。该方向不是对整个包豪斯学院的统一画风定义。

### ASCII：字符源 → 等宽字形 → 无损图片

~~~powershell
python tools/compile-style.py style-packages/game-art/ascii-character-game-art --direction experiments/style-v2/literal-ascii-grid --subject "One explorer holding a torch inside a cavern" --output runs/style-v2/ascii-job.json
python tools/render-ascii-grid.py runs/style-v2/ascii-job.json --source style-packages/game-art/ascii-character-game-art/examples/ascii-cave-grid.txt --font C:/Windows/Fonts/consola.ttf --output runs/style-v2/ascii-cave-render
~~~

第二条命令复用旧包的洞穴字符源，演示渲染链路；不会按新主体自动改写字符源。新题材需要先人工创作字符源，或把任务 Prompt 交给文本模型，再保存纯字符结果。不要把这个任务交给普通图像模型重绘。

字符源必须恰有 36 行，每行至多 100 列；支持 LF/CRLF 和一个可选末尾换行；右侧缺列补空格。仅接受 ASCII 可打印字符，拒绝中文、块字符、emoji、Tab、控制字符、超宽行和全空场景。必须显式选择等宽字体；字符不能超出单元格。若改行列数或字号，应先修改方向文件再重新编译。

渲染器只铺统一背景并逐格绘制字形，没有独立场景形状、渐变或模型重绘。输出：

- `master.png`：无损主图。
- `source_grid.txt`：规范化后的逐行字符源。
- `render_record.json`：源文件、规范化源、字体、渲染器、PNG 和 RGB 像素哈希，以及网格、环境版本和方向信息。

输出目录必须不存在，避免覆盖旧结果。复现需使用相同字符源、字体文件、网格设置、渲染器和 Pillow/字体渲染环境；不承诺跨平台像素一致。字形构成的真实性由制作链路保证，主体可读性仍需人工评审。

## 怎样判断值得继续迁移

按 [比较计划](../../docs/design/art-style-pack-v2/comparison-plan.yaml) 保持模型、主体、构图、尺寸及可用随机种子一致，分别比较“名称基线 / 旧包 / 新规则”。第一阶段只比较文本条件；研究图像不作为变量混入。

两个图像方向各包含 3 个题材、每组 2 次重复，即各 18 张、共 36 张；另有 3 个 ASCII 字符源与渲染任务。先检查主体保留、媒介和制作约束，再逐条检查规则及联动。用跨题材结果判断有没有继承相同视觉决定，以及两个方向是否足够可区分。不要用文件校验通过或形容词差异代替图片效果判断。

当前全部试点评审状态均为 `pending`，尚未运行上述生图对照，也未增加正式包数量或提升包成熟度。

本次已实际编译三个试点任务，并使用已有洞穴字符源完成一次无损渲染；操作记录和哈希见 [style-v2-implementation.json](../../reports/style-v2-implementation.json)。本阶段未运行自动化测试套件，单次渲染也不能作为重复渲染一致性的验证结果。
