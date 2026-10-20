# 阿尔丰斯·穆夏

[English](README.en.md)

![阿尔丰斯·穆夏代表图](gallery-16x9.jpg)

> **分类：** 艺术家
> **媒介领域：** 设计
> **目录：** `style-packages/artists/alphonse-mucha`

## 简介

以流动曲线、植物纹样、人物与边框的连续节奏、温暖纸色和装饰性平面组织画面；本包提取穆夏式视觉语法，不固定女性肖像、花卉、广告或文字。

这是一个可独立使用的风格包。它把可观察的媒介、构图、光线、色彩、表面、纹理和复现步骤整理成可执行规则，用于生成新的主题，不用于复制某一件具体作品。

## 策展短评

穆夏式画面迷人的地方，不只是“有花和长发”，而是线条、边框、人物轮廓和植物纹样彼此咬合，像同一条旋律反复变奏。代表图把这种连续的装饰节奏放在普通器物和人物旁边，提醒使用者：换成别的主体后，真正需要保留的是构图语法，而不是固定题材。

## 主体独立性

本包只决定“怎么生成”，不决定“生成什么”。人物、物体、地点、建筑、植物、车辆和叙事由你的 Prompt 决定；本包中的具体场景只属于示例或测试，不会作为默认主体加入生成结果。

## 使用前先看

- `identity.yaml`：范围、对象和排除项
- `visual-signature.yaml`：跨主题仍应保持的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础 Prompt 与负面约束
- `palette/palette.json`：色彩角色与色值
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源和权利边界

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、流派、学校或游戏的原作，也不代表合作、授权或背书关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 以及仓库根目录的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

四种方式可以按手边工具任选其一，不需要同时使用。

### 方式一：交给有生图能力的 Agent

把整个风格包目录上传给 Agent，或把本地目录路径交给它，并附上：

```text
请使用这个风格包帮助我生成图片。

请先读取本目录中的 identity.yaml、visual-signature.yaml、reproduction.yaml、
prompts/base.txt、prompts/negative.txt、palette/palette.json 和 evaluation.yaml。
请把文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。

我的生成需求是：
<填写人物、物体、场景、画幅和用途>

请先编译完整 Prompt，再调用你的生图能力。生成后按照 evaluation.yaml 检查风格特征、
构图、颜色、材质、AI 痕迹和需求遵循度，并说明仍然存在的风险。
```

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，替换主题、人物、物体、场景和画幅；将 `prompts/negative.txt` 作为负面 Prompt 一并提交到支持文本生图的平台。需要更稳定时，同时参考视觉签名和调色板。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，将基础 Prompt、负面约束、调色板和必要的参考清单一起提交。API Key 只保存在你的环境中；本仓库不代管密钥、不托管在线生图服务，也不承诺某个平台的免费额度或接口兼容性。

### 方式四：本地模型 + ComfyUI

将基础 Prompt 和负面约束接入本地模型或 ComfyUI 工作流；按调色板、复现说明和参考清单设置颜色、构图、材质与光线。生成后用 `evaluation.yaml` 做人工或自动复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。

## 新架构：装饰海报层级（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，仅在声明 `ornamental-poster` 时启用：先保证用户指定主体清楚，再让边框曲线和装饰纹样沿主体轮廓展开。调用者可用 `poster-benefits-from-decorative-movement` 启用装饰曲线；`user-supplied-exact-wording-or-blank-title-area` 只在用户提供准确文案或要求留白标题区时启用排字规则。植物纹样和文字都不是默认项。与丢勒以排线塑造明暗的方向不同，穆夏方向以平面色块、流动曲线和主体—边框版式为核心。

```powershell
python tools/compile-style.py style-packages/artists/alphonse-mucha --direction package --context ornamental-poster --subject "A blue glass perfume bottle in a decorative poster, no lettering" --output runs/style-v2/mucha-job.json
```

方向仍处于实验状态。大都会艺术博物馆与美国国家美术馆关于装饰画、彩色石版海报和版式的资料支持这些观察；无人物、无文字主体上的装饰迁移效果仍待评审。

## 新旧架构视觉对照

查看[同题样图、编译任务和复核限制](comparisons/README.md)。该对照是单题材初步检查，方向仍处于实验状态。
