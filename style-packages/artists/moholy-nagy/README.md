# 拉斯洛·莫霍利-纳吉

[English](README.en.md)

![拉斯洛·莫霍利-纳吉代表图](gallery-16x9.jpg)

> **分类：** 艺术家　**媒介：** 绘画、摄影与设计的跨媒介实验　**目录：** `style-packages/artists/moholy-nagy`

## 简介

拉斯洛·莫霍利-纳吉把光、透明材料、摄影和几何构成放在同一张工作台上。这个包关注的是光如何切割空间、透明层如何制造关系，以及黑白结构中少量纯色如何成为方向感。

它可以迁移到人物、物体、建筑或抽象主题。几何片段和透明投影是视觉方法，不是每次都要出现的具体物件。

## 策展短评

这个风格最有意思的地方，是它不把“实验性”交给随机故障，而是交给材料之间的秩序。先留出一块干净的空白，再让透明片、直线和投影彼此咬合，画面会像一台正在运行的光学装置。

## 主体独立性

本包只决定视觉处理，不决定人物、物体、地点或故事。你的 Prompt 提供什么主体，生成结果就应围绕什么主体；包豪斯、机械装置、实验室和海报都不是默认内容。

## 文件导航

- `identity.yaml`：来源、范围和主体边界
- `visual-signature.yaml`：构图、光线、色彩、表面和纹理
- `reproduction.yaml`：从主体轮廓到透明投影的构建顺序
- `prompts/`：基础 Prompt 与负面约束
- `palette/palette.json`：色彩角色
- `evaluation.yaml`：主体独立性与视觉签名检查
- `references/manifest.csv`、`provenance.yaml`：参考来源和权利边界

## 来源与版权

本包参考[现代艺术博物馆关于《黑白灰光的游戏》](https://www.moma.org/collection/works/50114)的馆藏资料，提取可观察的媒介和视觉方法。参考作品仍归原权利人所有；本包中的代表图是新的匿名场景，不是原作复制品，也不代表艺术家或博物馆的授权、合作或背书。

## 只使用此包

### 方式一：交给有生图能力的 Agent

把本目录交给 Agent，并告诉它先读取 `identity.yaml`、`visual-signature.yaml`、`reproduction.yaml`、`prompts/`、`palette/palette.json` 和 `evaluation.yaml`，再把你的主体、地点、画幅和用途编译成最终 Prompt。生成后按 `evaluation.yaml` 检查，不要把示例中的透明片或几何物件当成固定要求。

### 方式二：直接复制 Prompt

复制 `prompts/base.txt`，替换 `{SUBJECT}` 和 `{LOCATION}`；同时提交 `prompts/negative.txt`。需要更稳定的色彩和结构时，再参考调色板与视觉签名。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，把基础 Prompt、负面约束、调色板和必要的参考清单一起提交。本仓库不托管密钥或在线生图服务。

### 方式四：本地模型 + ComfyUI

把基础 Prompt 和负面约束接入本地模型或 ComfyUI；按复现说明设置透明层、方向光、投影和黑白结构，生成后用 `evaluation.yaml` 复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图用于理解视觉特征，不要复制原作构图、人物、文字、商标或标志。
