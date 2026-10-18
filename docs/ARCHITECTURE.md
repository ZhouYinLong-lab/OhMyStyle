# OhMyStyle 美术风格包架构

[English](ARCHITECTURE.en.md) · [返回 README](../README.md)

本文说明美术风格包如何组织，以及当前代码实际执行到哪一步。深入的研究依据见 [美术架构提案](ART-STYLE-PACK-ARCHITECTURE.md)，可运行示例见 [v2 试点说明](../experiments/style-v2/README.md)。

## 1. 一个包描述什么

一个美术风格包描述一组可以用于不同主体的视觉决定：如何构成形体、组织明暗和颜色、处理边缘与材质，以及用什么制作过程实现。用户另行提供主体、数量、地点、构图和用途。

例如，日光油画方向可以规定“反射色参与暗面塑形、笔触沿表面转折”，而海滩或船只是具体题材。把它用于院子里的木椅时，仍应能识别这组视觉决定。

同一艺术家可以有多个时期、媒介或实践方向；学院也可以有多个课程方法。来源名称帮助定位研究对象，包的范围应进一步说明实际选择了什么。

| 来源类别 | 应明确的范围 | 应观察的区别 |
| --- | --- | --- |
| 艺术家 | 时期、媒介、选定实践 | 形体、光色、笔触、边缘之间的关系 |
| 摄影师 | 摄影实践、场景条件、成像方式 | 视点、取景时机、距离、光线与影调 |
| 艺术流派 | 历史范围、选定分支 | 共通形式原则，以及与相邻流派的差别 |
| 艺术学院 | 具体课程、工作坊或教学方法 | 材料操作、结构探索与设计过程 |
| 工艺与媒介 | 材料、工具和制作限制 | 由制作过程产生的痕迹与形态 |
| 游戏美术 | 表现方式及技术约束 | 像素、字符、剪影、空间与交互对象的可读性 |
| 原创预设 | 原创目标与作者选择 | 可重复的视觉关系和明确排除项 |

这些是内容编写要求，并不表示现有全部包都已完成逐项审查。

## 2. 五层美术内容

**范围与意图 → 视觉规则 → 参考与反例 → 制作与执行 → 跨题材评审。**

| 层 | 回答的问题 | 需要保存的内容 |
| --- | --- | --- |
| 范围与意图 | 这个包选择了哪种实践，适用于什么条件？ | 媒介、时期或方法、核心意图、适用与冲突条件 |
| 视觉规则 | 创作时具体作出哪些决定？ | 指令、可观察结果、失败条件、重要程度、规则 ID |
| 参考与反例 | 为什么这样定义，区别在哪里？ | 来源记录、分析依据、原作与生成样例的区分、权利信息 |
| 制作与执行 | 用什么过程实现，哪些限制必须严格满足？ | 构建顺序、Prompt、模型能力或确定性渲染参数 |
| 跨题材评审 | 换主体后是否仍成立，是否与近邻方向可区分？ | 完整生成记录、逐规则评审、失败样例与适用例外 |

单条规则应同时包含创作指令和检查办法。例如：

~~~yaml
id: sorolla-light-structure
axis: lighting
importance: core
applies_when: 本方向选择日光任务，画面中存在可见的受光面与阴影面。
instruction: 以主要日光方向塑造体块，让环境反射影响暗面和过渡面。
observable: 同一对象的受光、暗面与反射色关系共同帮助读出结构。
reject_when: 只有整体偏暖或均匀发光，形体明暗和反射关系没有变化。
evidence:
  source_ids:
    - sorolla-national-gallery-technique
    - sorolla-prado-boys-on-the-beach
  basis: curatorial_inference
  visual_review: pending
~~~

这是 [索罗亚试点](../style-packages/artists/joaquin-sorolla/art-direction.yaml) 中的一条规则，不能单独替代完整方向文件。`basis` 区分机构描述、直接视觉观察、研究推断与原创意图；有来源链接不等于规则已经通过视觉评审。

规则还需要联动。例如，反射色、明暗组和笔触应共同说明同一体块。v2 用 `joint_checks` 连接多条规则，避免每条局部成立而整体画面失去一致性。

## 3. 仓库中的内容如何分工

| 位置 | 职责 |
| --- | --- |
| `catalog/` | 人物、机构等来源实体资料 |
| `style-packages/<category>/<id>/` | 当前正式、独立的美术风格包 |
| `style-packages/composites/` | 多个包按职责组合的配方 |
| `styles/` | 继承的 110 个轻量预设，保留原有格式 |
| `experiments/style-v2/` | 三个人工整理的新架构方向，独立于正式包目录 |
| `tasks/` | 一次生成的主体、构图、画幅与任务约束 |
| `workflows/` | 输入素材的观察、提炼和编排过程 |
| `skill/`、根目录 `SKILL.md` | Agent、多轮会话与接口使用协议 |
| `schema/`、`tools/` | 格式契约、读取、编译、渲染及评估工具 |
| `reports/` | 已记录的盘点与实施结果 |
| `runs/` | 本地任务和候选结果，默认忽略于 Git |

组合配方把包分配给媒介、色彩、光线、前景或背景等职责，支持 `stack`、`blend`、`contrast`。它们单独登记；详见 [组合说明](../style-packages/composites/README.md)。

## 4. 当前正式包：多文件契约

~~~text
style-packages/<category>/<id>/
├── README.md / README.en.md
├── package.yaml
├── resource.yaml
├── identity.yaml
├── visual-signature.yaml
├── reproduction.yaml
├── relations.yaml
├── palette/palette.json
├── prompts/base.txt / negative.txt / variations.txt
├── references/manifest.csv
├── provenance.yaml
├── evaluation.yaml
├── gallery-16x9.jpg
└── examples/accepted / generated / rejected
~~~

| 文件 | 保存什么 |
| --- | --- |
| `package.yaml` | 包 ID、版本、分类，以及各文件入口 |
| `resource.yaml` | 资源类型、成熟度、能力维度和证据声明 |
| `identity.yaml` | 来源解释、范围、主体开放策略与排除项 |
| `visual-signature.yaml` | 构图、光色、笔触、材质等视觉特征 |
| `reproduction.yaml` | 制作顺序与技术约束 |
| `relations.yaml` | 相近方向及区分说明 |
| `palette/palette.json` | 色彩角色、色值，或可选调色对 |
| `prompts/` | 当前可直接编译的基础与负面提示等文本 |
| `references/manifest.csv`、`provenance.yaml` | 来源、用途与权利边界 |
| `evaluation.yaml`、`examples/` | 检查标准、候选与已接受或拒绝的样例 |

`package.yaml` 可选声明 `files.art_direction`，将新版规则文件登记为包的一部分。登记本身不改变旧版编译行为；调用者需要显式传入 `--direction package`。没有这个字段的旧包无需转换，仍沿用旧路径。这样可逐包保留旧文件供兼容和检索，同时明确决定何时使用新版规则。

详细格式见 [正式包规范](STYLE-PACKAGE-SPEC.md)，资源与成熟度契约见 [资源架构](RESOURCE-ARCHITECTURE.md)。

### 文件存在与实际执行的区别

当前旧版编译器会加载视觉签名等结构文件，但最终正负 Prompt 主要来自 `prompts/base.txt`、`prompts/negative.txt` 和选定调色对，**不会自动把 `visual-signature.yaml` 的全部规则展开为指令**。`prompts/variations.txt` 也不是该编译路径的自动输入。

检索会读取并展开视觉签名；Agent 直接阅读文件时也可能使用更多规则。因此，“检索到了某个词”“Agent 读到了规则”和“编译任务实际包含规则”是三种不同情况。最终应保存实际交给模型的 Prompt 与输入素材，而不能仅凭 YAML 已修改就判定执行发生了变化。

<a id="v2-direction"></a>

## 5. v2 试点：显式选择的方向文件

v2 暂时保留正式包，用单独的 `direction.yaml` 描述选定方向。不会自动转换整个旧库，也不自动进入正式包检索或画廊。

| 字段 | 职责 |
| --- | --- |
| `base_package` | 明确复用哪个正式包的身份和来源记录 |
| `scope`、`pillars` | 媒介、再现方式、适用边界与编辑意图 |
| `rules` | 带 ID 的指令、观察标准、失败条件与来源依据 |
| `active_rule_ids` | 人工选定本方向采用的规则，必须包含全部核心规则 |
| `joint_checks` | 多条启用规则共同组织画面的要求 |
| `sources` | 正式包来源 ID、机构链接、本地原始文件或原创要求 |
| `execution` | 执行路线、必须满足的要求与避免项 |

契约见 [art-direction.schema.json](../schema/art-direction.schema.json)，编译实现见 [art_direction_runtime.py](../tools/art_direction_runtime.py)。

### 编译与评审信息分开保存

- **正面 Prompt**：用户主体及细节、媒介、再现方式、启用规则的 `instruction`、联动 `instruction` 与制作要求。
- **负面 Prompt**：显式编写的规则 `avoid` 和执行 `avoid`。
- **评审信息**：范围、规则原文、`observable`、`reject_when` 与来源保存在任务的 `review` 中，不直接作为生成指令拼接。
- **追踪信息**：方向文件路径、SHA-256、启用规则 ID 与声明的上下文。

`applies_when` 是供编辑判断的自然语言说明。当前程序检查人工声明的上下文是否缺失或冲突，不会理解主体文本并自动选择规则。研究来源也不会自动变成参考图片输入。

目前只支持 `profile=generic`、`references=none`，不与旧版调色对混用。HTTP/MCP 多轮会话和组合包仍走旧版编译路径；v2 通过命令行的 `--direction` 或 Python 的 `direction_path` 显式启用。方向可以单独存放在实验目录，也可以通过 `package.yaml` 的 `files.art_direction` 登记后用 `--direction package` 选择。

同一包可以分别编译旧版和新版任务，方便检查 Prompt 与规则差异。两路都关闭参考图时：

~~~powershell
python tools/compile-style.py style-packages/artists/joaquin-sorolla --subject "午后日光下无装饰庭院中的木椅，无人物、无水面、无海岸" --references none --output runs/compare/sorolla-legacy.json
python tools/compile-style.py style-packages/artists/joaquin-sorolla --direction package --context daylight --subject "午后日光下无装饰庭院中的木椅，无人物、无水面、无海岸" --output runs/compare/sorolla-direction.json
~~~

逐条对照 `prompt`、`negative_prompt` 和 `review.rules`。这能检查编译路径和输入差异，不代替同模型生图对比；两种格式的完整 Prompt 并不要求字面相同。

### 三个不同的制作方向

| 方向 | 核心视觉关系 | 执行路线 |
| --- | --- | --- |
| [索罗亚日光油画](../style-packages/artists/joaquin-sorolla/art-direction.yaml) | 日光、反射色、明暗组和随形笔触 | `text_only`，声明 `daylight` |
| [包豪斯纸材方法](../style-packages/schools/bauhaus/art-direction.yaml) | 切、撕、折与支撑、开口和投影 | `text_only`，声明 `paper-study` |
| [严格 ASCII 网格](../style-packages/game-art/ascii-character-game-art/art-direction.yaml) | 真实字符、统一单元格、密度与留白 | `deterministic_grid` |
| [梵高方向性笔触](../style-packages/artists/vincent-van-gogh/art-direction.yaml) | 随形笔触、局部冷暖关系、可见厚涂 | `text_only` |
| [莫兰迪静谧色阶](../style-packages/artists/giorgio-morandi/art-direction.yaml) | 近似明度、克制间距、浅空间与选择性软边 | `text_only` |
| [霍普建筑光影](../style-packages/artists/edward-hopper/art-direction.yaml) | 日常建筑平面、方向投影与空间距离 | `text_only` |
| [艾格尼丝·马丁手绘网格](../style-packages/artists/agnes-martin/art-direction.yaml) | 非具象细线网格、低对比色域与手工微差 | `text_only`，声明 `abstract-field` |
| [卡拉瓦乔明暗对照](../style-packages/artists/caravaggio/art-direction.yaml) | 近景动作、单光源明暗与物质感 | `text_only` |
| [广重气象版画](../style-packages/artists/utagawa-hiroshige/art-direction.yaml) | 天气层次、裁切前景、旅途尺度与木版渐变 | `text_only`，声明 `landscape-view` |
| [北斋轮廓色面](../style-packages/artists/katsushika-hokusai/art-direction.yaml) | 剪影层级、套色色面、明确裁切与纸面负形 | `text_only` |
| [弗里德里希人的尺度](../style-packages/artists/caspar-david-friedrich/art-direction.yaml) | 开阔空间、有限人类尺度、远景选择性显现 | `text_only`，声明 `landscape-view` |
| [欧姬芙近距离观察](../style-packages/artists/georgia-okeeffe/art-direction.yaml) | 用户指定形体的放大、色形简化、随形负空间 | `text_only`，声明 `close-observation` |
| [莱利光学节奏](../style-packages/artists/bridget-riley/art-direction.yaml) | 几何单元渐变序列、相邻对比、平面视觉振动 | `text_only`，声明 `abstract-field` |
| [丢勒刻线明暗](../style-packages/artists/albrecht-durer/art-direction.yaml) | 轮廓先行、顺形排线、纸白高光、材质线组 | `text_only` |
| [穆夏装饰海报](../style-packages/artists/alphonse-mucha/art-direction.yaml) | 主体与边框层级、随形曲线、石版平涂、用户控制文字 | `text_only`，声明 `ornamental-poster` |
| [安娜·安彻居室窗光](../style-packages/artists/anna-ancher/art-direction.yaml) | 单一窗光路径、跨墙地家具的反射色、日常室内尺度 | `text_only`，声明 `window-lit-interior` |
| [阿尔泰米西娅身体动作构图](../style-packages/artists/artemisia-gentileschi/art-direction.yaml) | 相抵对角线、贴近动作的裁切、暗部保留局部色彩 | `text_only`，声明 `figure-action` |
| [比亚兹莱墨块与留白](../style-packages/artists/aubrey-beardsley/art-direction.yaml) | 黑白正负形、书写性轮廓、焦点细节与大面积纸白 | `text_only`，声明 `black-and-white-ink-illustration` |
| [莫里索手势笔触与开放边缘](../style-packages/artists/berthe-morisot/art-direction.yaml) | 动势笔触、选择性软边、可见底色与疏密差 | `text_only`，声明 `open-brush-figure-painting` |
| [里维拉公共叙事壁画层次](../style-packages/artists/diego-rivera/art-direction.yaml) | 相连叙事层次、人物与环境共尺度、远距可读的大色面 | `text_only`，声明 `public-narrative-mural` |

## 6. 从主体请求到结果

~~~mermaid
flowchart TD
    A[用户主体与细节] --> B[正式包旧版编译]
    P[正式风格包] --> B
    A --> C[显式选择 v2 方向]
    P --> C
    D[direction.yaml] --> C
    B --> E[图像任务与实际 Prompt]
    C --> F{制作路线}
    F -->|text_only| E
    E --> G[外部图像模型]
    F -->|deterministic_grid| H[人工或文本模型创作字符源]
    H --> I[固定网格与等宽字体逐格渲染]
    G --> J[主体、媒介与逐规则评审]
    I --> J
~~~

`text_only` 表示本阶段不输入参考图片；编译器输出任务，实际模型由使用者选择和配置。

ASCII 路线要求先有字面字符源，再用指定等宽字体逐格绘制。渲染器仅绘制统一背景和字形，拒绝非 ASCII 字符、错行、超宽、全空场景和不合适的字体尺寸。输出无损 PNG、规范化源网格和包含源文件、字体、环境及像素哈希的记录。新主体不会自动改写已有字符源；图像模型生成的近似字符画不算这条路线的结果。

操作命令见 [v2 试点说明](../experiments/style-v2/README.md)，多轮确认与模型接口见 [Skill 使用说明](../skill/README.md)。

## 7. 怎样评审质量与区分度

1. 检查用户要求的主体、数量、构图与排除项。
2. 检查媒介和制作硬约束；ASCII 必须能回溯到字符源，纸材生成图只可作为视觉研究。
3. 按适用的核心规则、支持规则和联动要求分别记录结果。
4. 用多个题材与重复输出检查稳定性，保留失败结果。
5. 与相近艺术家、流派或学院方法比较具体视觉关系，避免只比较风格名称或文本相似度。

比较时固定主体、模型版本、画幅和生成设置；分别保留名称基线、旧包和新规则的实际输入。第一阶段不混入研究图像参考，完整计划见 [比较方案](design/art-style-pack-v2/comparison-plan.yaml)。

现行成熟度为 L0 名称描述、L1 结构化描述、L2 有参考的可执行包、L3 增加已接受生成与评审证据、L4 增加跨模型或适配器验证。旧包的成熟度不会自动继承成 v2 规则的通过结论。

最初三个试点均为 `experimental`，评审均为 `pending`；后续登记的方向也维持实验状态。已完成任务编译和严格 ASCII 源渲染，生成的示意图不作为 provider-backed 对照评审，也没有据此提升成熟度。初始阶段记录见 [实施报告](../reports/style-v2-implementation.json)。

## 8. 版本与后续推进

旧版固定在 `codex/style-v1-preserved` 分支和 `style-v1-snapshot-2026-10-18` 标签，提交为 `59d9aa10ee9eeaedf3b815688d00f3e553ef31ea`。新实现最初在 `codex/style-pack-v2` 开发，现已进入 `main`；后续开发以 `main` 为准。旧版基线继续保留，正式包没有全库批量迁移。

建议按“人工整理方向 → 保存实际编译结果 → 对照生成 → 逐规则评审 → 决定是否扩大”推进。脚本负责结构、引用和记录；视觉规则的补写、来源解释及风格差异由研究和评审决定。成本与风险见 [迁移评估](ART-STYLE-MIGRATION-ASSESSMENT.md)，独立旧版工作区命令见 [回退说明](../experiments/style-v2/README.md#版本保留与回退)。
