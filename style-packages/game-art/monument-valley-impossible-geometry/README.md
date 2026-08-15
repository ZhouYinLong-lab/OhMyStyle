# 纪念碑谷不可能几何游戏美术

[English](README.en.md)

![纪念碑谷不可能几何游戏美术 代表图](gallery-16x9.jpg)

> **分类：** game_art
> **媒介领域：** game_art
> **目录：** style-packages/game-art/monument-valley-impossible-geometry

## 简介

以简洁色块、建筑错视、可旋转的几何路径和宁静留白组织游戏空间，强调视觉谜题而非固定故事。

这是一个可独立使用的风格包。它提取可观察的视觉语言，用来处理用户指定的新主题，不会把代表图中的物体、地点、人物或故事写入默认生成结果。

## 策展短评

我喜欢它把“谜题”藏进建筑秩序里：没有复杂材质，视线却会因为一条不可能的连接停下来。它适合处理空间、物件和环境，不需要每次都变成熟悉的游戏场景。

## 主体独立性

本包只决定“怎么生成”，不决定“生成什么”。人物、物体、地点、建筑、植物、车辆和叙事由你的 Prompt 决定；代表图只用于展示视觉处理，不是固定题材模板。

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、流派、技法或游戏的原作，也不代表合作、授权或背书关系。

详细来源见 provenance.yaml 和 references/manifest.csv。

## 只使用此包

### 方式一：交给有生图能力的 Agent

把本目录交给 Agent，并要求它先读取 identity.yaml、visual-signature.yaml、reproduction.yaml、prompts/base.txt、prompts/negative.txt、palette/palette.json 和 evaluation.yaml，再把你的主体、地点、画幅和用途编译进完整 Prompt。生成后按 evaluation.yaml 检查，不要复制参考作品。

### 方式二：直接复制 Prompt

打开 prompts/base.txt，替换主体、地点和画幅要求；把 prompts/negative.txt 一起交给支持负面 Prompt 的生图平台。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，将基础 Prompt、负面约束、调色板和参考清单一起提交。密钥与生成图片由你自己管理，本仓库不托管在线生图服务。

### 方式四：本地模型与 ComfyUI

将基础 Prompt 和负面约束接入本地模型或 ComfyUI 工作流，按 visual-signature.yaml、reproduction.yaml 和 palette/palette.json 设置视觉参数，生成后用 evaluation.yaml 复核。
