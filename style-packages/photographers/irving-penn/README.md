# 欧文·佩恩

[English](README.en.md)

![欧文·佩恩代表图](gallery-16x9.jpg)

> **分类：** 摄影师  
> **媒介领域：** 摄影  
> **目录：** `style-packages/photographers/irving-penn`

## 简介

欧文·佩恩的摄影常把人物、服装或普通器物放进高度克制的摄影棚环境里。背景很少抢戏，形体、材料、阴影和留白承担主要叙述。本包提取这种精确而安静的控制感，不把纸张、陶瓷、肖像或时装写成固定内容。

## 策展短评

这类照片让我想到“把多余的声音关掉”之后，材料自己开始说话。它适合那些需要高级感、秩序感，却不想依靠金色滤镜和昂贵道具的画面。生成时要留意阴影边界与物体间距，它们比装饰更能决定气质。

## 主体独立性

本包只决定摄影方式，不规定人物、物体、地点、服装或故事。代表图的纸张和器物只是测试主体，新的生成应以用户需求为准。

## 来源与版权

研究入口为[现代艺术博物馆的艺术家档案](https://www.moma.org/artists/4548-irving-penn)。仓库不打包外部作品；代表图是新的匿名场景，不是具体原作，也不表示合作、授权或背书关系。

## 只使用此包

### 方式一：交给有生图能力的 Agent

把本目录交给 Agent，让它先读取 `identity.yaml`、`visual-signature.yaml`、`reproduction.yaml`、`prompts/`、`palette/palette.json` 和 `evaluation.yaml`，再编译你的主体、画幅和用途。生成后按评价文件检查主体独立性、材料和 AI 痕迹。

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，替换 `{{SUBJECT}}`、`{{ASPECT_RATIO}}` 和 `{{USE_CASE}}`；把 `prompts/negative.txt` 一并提交给支持负面 Prompt 的平台。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，提交基础 Prompt、负面约束和调色板。本仓库不托管密钥或在线生图服务。

### 方式四：本地模型 + ComfyUI

将 Prompt、调色板和复现说明接入本地模型或 ComfyUI，生成后用 `evaluation.yaml` 复核，不要把代表图的道具当成默认主体。
