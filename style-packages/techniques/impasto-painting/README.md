# 厚涂绘画

[English](README.en.md)

![厚涂绘画代表图](gallery-16x9.jpg)

> **分类：** 工艺与媒介  · **媒介领域：** 绘画技法
> **目录：** style-packages/techniques/impasto-painting

## 简介

以明显堆叠的颜料厚度、可见笔触与调色刀痕塑造光线和表面，让画面纹理成为构图与体积的一部分。

## 一点观察

厚涂颜料、可见笔触和反光表面共同构成的触觉性绘画技法。我更愿意把它看成一组可迁移的视觉决定：真实可见的颜料厚度，再由光线、表面和空间共同完成画面。这个包提取可观察特征，不把某个作品的题材、构图或故事一起带入。

## 视觉签名

- 真实可见的颜料厚度
- 笔触方向与体积、光线绑定
- 高光通过颜料堆叠而不是发光滤镜产生
- 纹理密度随主体和构图变化

## 主体独立性

本包只决定视觉处理方式，不决定用户要生成的人物、物体、地点、数量或故事。代表图和测试题材只是演示，不会成为默认内容；不会自动加入固定地标、角色、建筑、道具、宗教场景、游戏关卡或叙事事件。

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、技法、流派或游戏的原作，也不代表合作、授权或背书关系。

- [Impasto](https://www.moma.org/collection/terms/impasto)

详细来源和再分发边界见 [provenance.yaml](provenance.yaml)、[references/manifest.csv](references/manifest.csv) 以及仓库根目录的 NOTICE (../../../NOTICE)。

## 只使用此包

四种方式可以按手边工具任选其一，不需要同时使用。

### 方式一：交给有生图能力的 Agent

把整个风格包目录上传给 Agent，或把本地目录路径交给它，并要求它先读取 identity.yaml、visual-signature.yaml、reproduction.yaml、prompts/base.txt、prompts/negative.txt、palette/palette.json 和 evaluation.yaml；把这些规则编译进你的需求，不要复制参考作品；生成后按照 evaluation.yaml 复核风格、构图、颜色、材质、AI 痕迹和需求遵循度。

### 方式二：直接复制 Prompt

打开 [prompts/base.txt](prompts/base.txt)，替换主题、人物、物体、场景和画幅；将 [prompts/negative.txt](prompts/negative.txt) 作为负面 Prompt 一并提交到支持文本生图的平台。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，将基础 Prompt、负面约束、调色板和必要的参考清单一起提交。本仓库不代管密钥、不托管在线生图服务。

### 方式四：本地模型 + ComfyUI

将基础 Prompt 和负面约束接入本地模型或 ComfyUI 工作流；按调色板、复现说明和参考清单设置颜色、构图、材质与光线。生成后用 [evaluation.yaml](evaluation.yaml) 做复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。
