# 萨尔瓦多·达利

[English](README.en.md)

![萨尔瓦多·达利代表图](gallery-16x9.jpg)

> **分类：** 艺术家  
> **媒介领域：** 绘画  
> **目录：** `style-packages/artists/salvador-dali`

## 简介

萨尔瓦多·达利的画面常把近乎精密的现实表面，放进不太服从现实逻辑的关系里。异常感可能来自尺度、影子、连接或时间感，而不一定来自一堆奇怪物件。本包提取这种清醒而陌生的组织方式，不把融化时钟、荒漠、动物或肖像写成固定内容。

## 策展短评

我喜欢它“看得很清楚，却无法完全解释”的感觉。画面越安静，局部的不合理越有力量。使用时最好只改变一两个关系，让普通主体保持完整；如果每个角落都在变形，梦境就会变成装饰。

## 主体独立性

本包只决定视觉处理，不规定人物、物体、地点、建筑或故事。代表图的石庭和变形物只是测试主体，新的生成应以用户需求为准。

## 来源与版权

研究入口为[现代艺术博物馆的艺术家档案](https://www.moma.org/artists/1364-salvador-dali)。仓库不打包外部作品；代表图是新的匿名场景，不是具体原作，也不表示合作、授权或背书关系。

## 只使用此包

### 方式一：交给有生图能力的 Agent

把本目录交给 Agent，让它先读取 `identity.yaml`、`visual-signature.yaml`、`reproduction.yaml`、`prompts/`、`palette/palette.json` 和 `evaluation.yaml`，再编译你的主体、场景、画幅和用途。生成后检查异常关系是否有限且服务于主体。

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，替换 `{{SUBJECT}}`、`{{ASPECT_RATIO}}` 和 `{{USE_CASE}}`；把 `prompts/negative.txt` 一并提交给支持负面 Prompt 的平台。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，提交基础 Prompt、负面约束和调色板。本仓库不托管密钥或在线生图服务。

### 方式四：本地模型 + ComfyUI

将 Prompt、调色板和复现说明接入本地模型或 ComfyUI，生成后用 `evaluation.yaml` 检查写实表面、异常关系、主体保留和 AI 痕迹。
