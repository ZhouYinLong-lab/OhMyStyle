# 露丝·伯恩哈德

[English](README.en.md)

![露丝·伯恩哈德代表图](gallery-16x9.jpg)

> **分类：** 摄影师  · **媒介领域：** 摄影
> **目录：** style-packages/photographers/ruth-bernhard

## 简介

以克制的黑白影调、雕塑般的轮廓、亲密的静物与人体观察建立安静而精确的摄影形体。

## 一点观察

形式主义黑白摄影中的形体、光线、负空间与亲密距离。我更愿意把它看成一组可迁移的视觉决定：雕塑般的黑白形体，再由光线、表面和空间共同完成画面。这个包提取可观察特征，不把某个作品的题材、构图或故事一起带入。

## 视觉签名

- 雕塑般的黑白形体
- 局部裁切与安静负空间
- 连续阶调而非高反差滤镜
- 近距离观察但不制造戏剧叙事

## 主体独立性

本包只决定视觉处理方式，不决定用户要生成的人物、物体、地点、数量或故事。代表图和测试题材只是演示，不会成为默认内容；不会自动加入固定地标、角色、建筑、道具、宗教场景、游戏关卡或叙事事件。

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、技法、流派或游戏的原作，也不代表合作、授权或背书关系。

- [Ruth Bernhard](https://www.moma.org/artists/516)

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
