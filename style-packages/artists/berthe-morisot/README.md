# 贝尔特·莫里索

[English](README.en.md)

![贝尔特·莫里索代表图](gallery-16x9.jpg)

> **分类：** 艺术家<br>
> **媒介领域：** 绘画<br>
> **目录：** `style-packages/artists/berthe-morisot`

## 简介

以高明度色调、迅疾松动的笔触、开放的边缘和流动日光组织画面，让人物与环境在轻盈的色块中相互渗透。此包只控制视觉呈现，主体、地点、数量和用途由你的需求决定。

## 策展短评

莫里索的画面常像光线还在移动：轮廓不急着封闭，几笔颜色就让形体浮现。用这套规则时，可以让关键结构清楚，同时把部分边缘交给环境和空气。

## 文件导览

- `identity.yaml`：范围、主体策略与排除项
- `visual-signature.yaml`：跨主题稳定的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础 Prompt 与负面约束
- `palette/palette.json`：色彩角色和值
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源与权利边界

## 来源与权利

参考清单链接至大都会艺术博物馆和美国国家美术馆的馆藏资料，仅供风格研究。仓库不包含莫里索原作或馆藏照片。风格规则提炼自公开可观察的笔触、色调和边缘处理，不复刻特定作品、人物或构图。代表图和样例是新生成的场景，不是历史作品。

## 使用此包

把整个目录交给有生图能力的 Agent，或读取 `prompts/base.txt` 并替换 `{SUBJECT}` 与 `{LOCATION}`。将 `prompts/negative.txt` 一并提交；生成后按照 `evaluation.yaml` 检查主体可读性、笔触、光线和色彩。也可以在自己的 API 或本地模型工作流中使用这些规则；本仓库不托管生图服务或 API Key。

代表图及样例当前标为待人工审核。不要把它们称作莫里索的作品，也不要用它们重建参考清单中的具体画作。

## 新架构：手势笔触与开放边缘（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，让笔触跟随人物转身、衣料走势和邻近形体；在面部、手部等关键锚点保持可读的同时，选择性放开边缘。只有调用者声明 `light-ground-open-margin-allowed` 时，才要求保留画布底色与稀疏边缘。它针对的是笔触如何表现动作、边缘如何停笔和画布如何留气口；莫奈方向更侧重某一时刻的天气、光色条件和不同表面的笔触组织，莫里索方向不默认天气效果或风景系列。

```powershell
python tools/compile-style.py style-packages/artists/berthe-morisot --direction package --context open-brush-figure-painting --context light-ground-open-margin-allowed --subject "A person turning while holding a loose white scarf beside an open window" --output runs/style-v2/berthe-morisot-job.json
```

此方向仍为实验规则；同题生图对照与跨主体稳定性待人工评审。

## 新旧架构视觉对照

查看[同题样图、编译任务和复核限制](comparisons/README.md)。该对照是单题材初步检查，方向仍处于实验状态。
