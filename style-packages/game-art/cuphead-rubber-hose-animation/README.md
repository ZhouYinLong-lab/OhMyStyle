# 三十年代橡皮管动画游戏美术

[English](README.en.md)

![三十年代橡皮管动画游戏美术代表图](gallery-16x9.jpg)

> **分类：** 游戏美术  
> **媒介领域：** 游戏美术  
> **目录：** `style-packages/game-art/cuphead-rubber-hose-animation`

## 简介

这个包把三十年代手绘动画中的橡皮管动作、变化明显的墨线、赛璐珞式色块、水彩或水粉背景和纸面印刷痕迹转译为游戏环境美术。它不是像素包，也不是三维卡通渲染包。

## 策展短评

这种美术语言最有趣的地方在于“线条会动”：轮廓不追求工程图般的稳定，而是用弯曲、拉伸和夸张的节奏让静态画面带出动作。代表图选择了海边工业环境，是为了让前中后景和可游玩路径一眼可读；换成别的主体后，应该保留的是墨线、绘制层次和有限色彩，而不是风车、码头或某个角色。

## 主体独立性

本包只决定手绘动画媒介、轮廓、层次、色彩和表面，不规定角色、敌人、风车、海边村落、码头或故事。代表图中的环境只是示例；使用者提供的主体、玩法和构图优先。

## 使用前先看

- `identity.yaml`：范围与排除项
- `visual-signature.yaml`：换主体后仍应保留的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础约束
- `palette/palette.json`：色彩角色
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源与权利边界

## 来源与版权

本包参考[《茶杯头艺术设定集》的资料页](https://digital.darkhorse.com/books/ef9898a203a8440dbc5d9dc84e30e19a/art-of-cuphead)，借鉴其中所述的三十年代动画视觉语境，只提取可观察的媒介与技术特征。代表图是新的原创环境，不复制具体游戏画面、角色或标志，也不表示与相关游戏、工作室或出版方存在合作、授权或背书关系。详细边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库根目录的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

四种方式任选其一：

1. **交给有生图能力的 Agent**：把本目录交给 Agent，要求先读取身份、视觉签名、复现说明、Prompt、调色板和评估文件，再把你的游戏主体编译成完整 Prompt；生成后按 `evaluation.yaml` 复核，不要只输入游戏风格名称。
2. **直接复制 Prompt**：打开 `prompts/base.txt`，替换 `{SUBJECT}` 与 `{LOCATION}`；将 `prompts/negative.txt` 一并提交。
3. **配置 API Key 后提交生成**：在你自己的平台或编译工具中配置 API Key，提交基础 Prompt、负面约束、调色板和必要参考清单。本仓库不托管密钥或在线生图服务。
4. **本地模型 + ComfyUI**：把基础 Prompt 和负面约束接入工作流，按复现说明设置墨线、层次、有限色彩和纸面质感；生成后用 `evaluation.yaml` 复核。

模型权重、密钥和生成图片由使用者自行管理。参考资料用于理解特征，不用于复制原作。
