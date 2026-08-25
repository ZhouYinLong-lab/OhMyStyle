# 女神异闻录5皇家版游戏美术

[English](README.en.md)

![女神异闻录5皇家版游戏美术代表图](gallery-16x9.jpg)

> **分类：** 游戏美术  · **媒介领域：** 游戏美术<br>
> **目录：** `style-packages/game-art/persona-5-royal`

## 简介

以朱红、近黑和纸白建立高对比三色系统，配合斜切、重叠色块、硬朗剪影和局部印刷纹理，形成强烈的编辑化动势。它适合需要时尚感、行动感和版式冲击的画面，但不会自动加入面具、扑克牌、枪械、怪盗或特定城市。

## 一点观察

这个包最值得保留的是“颜色和版式一起工作”：朱红负责推动视线，近黑负责切出结构，纸白负责呼吸和分隔。斜线与拼贴不是装饰，而是决定画面节奏的骨架。只保留红黑而拿掉这些关系，结果就会退化成普通的双色滤镜。

## 视觉签名

- 朱红、近黑和纸白构成核心三色系统
- 斜切、切角和重叠平面制造编辑化动势
- 硬朗剪影与清楚的版式层级并存
- 网点、纸张磨损或刷痕只出现在局部层
- 红色集中在主体、路径或视觉焦点

## 主体独立性

本包只决定视觉处理方式，不决定用户要生成的人物、物体、地点、数量或故事。代表图中的桥、人物、纸片和城市几何体只是演示内容，不会进入默认 Prompt。

## 来源与版权

本包参考官方资料页提取可观察的视觉特征，不复制游戏截图、角色、界面、徽标或具体构图。生成示例是新的匿名场景，不代表 ATLUS 或 SEGA 的授权、合作或背书。

- [官方资料页](https://persona.atlus.com/p5r/?lang=en)

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

将基础 Prompt 和负面约束接入本地模型或 ComfyUI；按调色板、复现说明和参考清单设置红黑白层级、斜切方向、拼贴关系和局部印刷质感。需要更强的局部控制时，再由工作流补充 mask。

模型权重、API Key 和生成图片由使用者自行管理。参考资料只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或界面。
