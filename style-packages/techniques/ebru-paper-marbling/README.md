# 水面浮彩纸张纹样

[English](README.en.md)

![水面浮彩纸张纹样代表图](gallery-16x9.jpg)

> **分类：** 工艺与媒介　**媒介：** 水面浮彩与纸张转印　**目录：** `style-packages/techniques/ebru-paper-marbling`

## 简介

这个包把颜料漂浮在黏稠水面、再转印到纸张的过程整理成可迁移的视觉规则。滴落、扩散、牵引、梳理和纸面吸收共同形成云纹、石纹与流动色带。随机性来自材料过程，而不是数字噪声。

## 策展短评

我喜欢它既可控又不完全听话。先给液面一个方向，再允许颜料在边缘发生偏移，最后让纸张把水面留下来；这样的不确定性有手感，也比简单添加“渐变”和“梦幻”更有辨识度。

## 主体独立性

本包只决定流体纹样、颜料边界、转印、纸面吸收和纹理。书籍、花朵、书法、土耳其装饰和装帧页面都不是默认主体。

## 文件导航

- `identity.yaml`：来源、范围和主体边界
- `visual-signature.yaml`：流体、构图、色彩和纸面
- `reproduction.yaml`：从水面到纸张的构建顺序
- `prompts/`：基础 Prompt 与负面约束
- `palette/palette.json`：色彩角色
- `evaluation.yaml`：主体独立性与视觉签名检查
- `references/manifest.csv`、`provenance.yaml`：参考来源和权利边界

## 来源与版权

本包参考[大都会艺术博物馆关于大理石纹纸的介绍](https://www.metmuseum.org/ja/perspectives/marbled-paper)和[大英博物馆的纸张浮彩藏品说明](https://www.britishmuseum.org/collection/object/W_1991-0620-0-3)，提取颜料漂浮、梳理和转印的过程特征。馆藏作品归原权利人所有；代表图是新的匿名场景，不是具体纸张的复制品，也不代表机构或艺术家的授权、合作或背书。

## 只使用此包

### 方式一：交给有生图能力的 Agent

把本目录交给 Agent，要求它先读取身份、视觉签名、复现说明、Prompt、调色板和评价文件，再编译你的主体、地点、画幅和用途。示例中的陶瓷器皿只用于展示转印效果，不应变成默认主体。

### 方式二：直接复制 Prompt

复制 `prompts/base.txt`，替换 `{SUBJECT}` 和 `{LOCATION}`；同时提交 `prompts/negative.txt`。需要更稳定的色相关系时，再参考调色板和复现说明。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，把基础 Prompt、负面约束和调色板一起提交。本仓库不托管密钥或在线生图服务。

### 方式四：本地模型 + ComfyUI

把基础 Prompt 和负面约束接入本地模型或 ComfyUI，按复现说明设置流体边界、梳理方向、纸面吸收和转印变化，生成后用 `evaluation.yaml` 复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图只用于理解视觉特征，不要复制原作纸张、文字、商标或标志。
