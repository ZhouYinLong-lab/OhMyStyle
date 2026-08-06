# 自然窗光

[English](README.en.md)

![自然窗光代表图](gallery-16x9.jpg)

> **分类：** 原创预设
> **类型：** 原创预设
> **目录：** `style-packages/presets/natural-window-light`

## 简介

这是一个面向「自然窗光」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 风格重点

大窗软光、自然阴影、低饱和材质与真实镜头表现。Prompt 会优先表达这些可观察特征，同时保留新主题、新构图和新的对象关系。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 参考来源

- [Anonymous photographic study / 摄影预设](https://www.loc.gov/photos/)

## 来源与版权

参考链接只用于研究和视觉分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有；本包不重新分发受版权保护的原作。代表图是新的匿名生成场景，不是相关艺术家、摄影师、设计师或游戏的原作，也不代表合作或授权关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

1. 下载本目录，阅读 `identity.yaml`、`visual-signature.yaml` 和 `reproduction.yaml`。
2. 打开 `prompts/base.txt`，把主题替换为自己的内容；负面约束见 `prompts/negative.txt`。
3. 选择一种执行方式：直接复制 Prompt 到生图平台；配置自己的 API Key 后提交编译任务；或将 Prompt、参考清单和调色板导入本地模型与 ComfyUI。
4. 参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。

模型权重、API Key 和生成图片由使用者自行管理；本仓库不托管在线生图服务。
