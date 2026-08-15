# 皇家美术学院学校

[English](README.en.md)

![皇家美术学院学校代表图](gallery-16x9.jpg)

> **分类：** 设计学校  · **媒介领域：** 学院训练与工作室实践
> **目录：** style-packages/schools/royal-academy-schools

## 简介

以长期工作室实践、写生训练、材料研究和个人视觉语言发展组织创作过程，强调训练方法而非固定画面题材。

## 一点观察

学院包不是某一种固定画风，而是一套强调观察、反复制作、材料判断和个人实践的训练倾向。这个包把严谨观察与工作室决策转成生成约束，不自动加入石膏像、裸体写生或古典建筑。

## 视觉签名

- 观察先于装饰的形体判断
- 工作室式材料意识和反复推敲
- 受控构图、比例和明暗关系
- 保留个人笔触或材料选择，而不是套用统一滤镜

## 主体独立性

本包只决定视觉处理方式，不决定用户要生成的人物、物体、地点、数量或故事。代表图和测试题材只是演示，不会成为默认内容；不会自动加入固定地标、角色、建筑、道具、宗教场景、游戏关卡或叙事事件。

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、技法、学院或游戏的原作，也不代表合作、授权或背书关系。

- [皇家美术学院学校历史资料](https://royal-academy-production-asset.s3.amazonaws.com/uploads/6feabd1b-80a0-4806-a2b8-f1b44ba1c595/RA%20Schools%20Background%20and%20History%2020.5.24.pdf)

详细来源和再分发边界见 [provenance.yaml](provenance.yaml)、[references/manifest.csv](references/manifest.csv) 以及仓库根目录的 [NOTICE](../../../NOTICE)。

## 只使用此包

四种方式可以按手边工具任选其一，不需要同时使用。

### 方式一：交给有生图能力的 Agent

把整个风格包目录上传给 Agent，或把本地目录路径交给它，并附上：

~~~
请使用这个风格包帮助我生成图片。
请先读取 identity.yaml、visual-signature.yaml、reproduction.yaml、prompts/base.txt、
prompts/negative.txt、palette/palette.json 和 evaluation.yaml。
请把文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。
我的生成需求是：<填写人物、物体、场景、画幅和用途>
请先编译完整 Prompt，再调用你的生图能力。生成后按照 evaluation.yaml 检查风格特征、
构图、颜色、材质、AI 痕迹和需求遵循度，并说明仍然存在的风险。
~~~

### 方式二：直接复制 Prompt

打开 [prompts/base.txt](prompts/base.txt)，替换主题、人物、物体、场景和画幅；将 [prompts/negative.txt](prompts/negative.txt) 作为负面 Prompt 一并提交到支持文本生图的平台。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，将基础 Prompt、负面约束、调色板和必要的参考清单一起提交。本仓库不代管密钥、不托管在线生图服务。

### 方式四：本地模型 + ComfyUI

将基础 Prompt 和负面约束接入本地模型或 ComfyUI 工作流；按调色板、复现说明和参考清单设置颜色、构图、材质与光线。生成后用 [evaluation.yaml](evaluation.yaml) 做复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。
