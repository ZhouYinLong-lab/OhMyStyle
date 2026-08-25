# 女神异闻录3重制版游戏美术

[English](README.en.md)

![女神异闻录3重制版游戏美术代表图](gallery-16x9.jpg)

> **分类：** 游戏美术  · **媒介领域：** 游戏美术<br>
> **目录：** `style-packages/game-art/persona-3-reload`

## 简介

以深海军蓝、钴蓝和冷紫组织夜间空间，配合清晰剪影、都市建筑骨架、克制的暖色点光和适度空气感。它适合表现安静、疏离、带有都市幻想气息的游戏画面，但不会自动加入月亮、学校、列车或特定角色。

## 一点观察

这个包最有辨识度的地方不是“蓝色滤镜”，而是蓝色如何参与空间组织：建筑和道路先形成清楚骨架，冷色环境光把不同材质放进同一个夜间系统，暖色只在局部承担节拍。这样换成建筑、静物或人物时，视觉语言仍然能成立。

## 视觉签名

- 深海军蓝、钴蓝和冷紫构成主要色阶
- 都市结构、电线、栏杆或道路形成图形骨架
- 冷色月光与清晰轮廓保持空间可读性
- 少量暖琥珀光只作为局部光源或反射
- 数字绘画边缘干净，纹理和雾气保持克制

## 主体独立性

本包只决定视觉处理方式，不决定用户要生成的人物、物体、地点、数量或故事。代表图中的高架平台、月亮、城市、电线和人物只是演示内容，不会进入默认 Prompt。

## 来源与版权

本包参考官方资料页提取可观察的视觉特征，不复制游戏截图、角色、界面、徽标或具体构图。生成示例是新的匿名场景，不代表 ATLUS 或 SEGA 的授权、合作或背书。

- [官方资料页](https://persona.atlus.com/p3r/index.html?lang=enbuy)

详细来源和再分发边界见 [provenance.yaml](provenance.yaml)、[references/manifest.csv](references/manifest.csv) 以及仓库根目录的 [NOTICE](../../../NOTICE)。

## 只使用此包

四种方式可以任选其一，不需要同时使用：

### 方式一：交给有生图能力的 Agent

把整个风格包目录交给 Agent，并要求它先读取 `identity.yaml`、`visual-signature.yaml`、`reproduction.yaml`、`prompts/base.txt`、`prompts/negative.txt`、`palette/palette.json` 和 `evaluation.yaml`，再把规则编译进你的主题。生成后检查主体、色彩、构图、材质和禁用项。

### 方式二：直接复制 Prompt

打开 [prompts/base.txt](prompts/base.txt)，替换 `{subject}`、`{composition}` 和 `{aspect_ratio}`；将 [prompts/negative.txt](prompts/negative.txt) 一并提交到支持文本生图的平台。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，将基础 Prompt、负面约束、调色板和必要的参考清单一起提交。本仓库不代管密钥，也不托管在线生图服务。

### 方式四：本地模型 + ComfyUI

将基础 Prompt 和负面约束接入本地模型或 ComfyUI；按调色板、复现说明和参考清单设置冷蓝色阶、局部暖光、轮廓和空间层次。需要更强的局部控制时，再由工作流补充 mask。

模型权重、API Key 和生成图片由使用者自行管理。参考资料只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或界面。
