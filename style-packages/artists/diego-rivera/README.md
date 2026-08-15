# 迭戈·里维拉

[English](README.en.md)

![迭戈·里维拉代表图](gallery-16x9.jpg)

> **分类：** 艺术家  · **媒介领域：** 绘画
> **目录：** style-packages/artists/diego-rivera

## 简介

以壁画式大尺度结构、清晰轮廓、平面色块和公共空间的叙事组织画面，同时保持用户主体开放。

## 一点观察

里维拉的壁画语言重视远距离可读性：形体明确，群组关系清楚，色块和建筑结构共同承载公共空间的节奏。这个包只提取壁画式构图、轮廓和色面，不自动加入工人、革命、墨西哥地标或历史事件。

## 视觉签名

- 适合远距离阅读的大尺度形体组织
- 清晰轮廓与平面色块共同承担结构
- 土红、赭黄、蓝绿和灰黑形成公共空间色彩
- 人物或物体群组具有壁画式节奏，但不规定主体

## 主体独立性

本包只决定视觉处理方式，不决定用户要生成的人物、物体、地点、数量或故事。代表图和测试题材只是演示，不会成为默认内容；不会自动加入固定地标、角色、建筑、道具、宗教场景、游戏关卡或叙事事件。

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、技法、学院或游戏的原作，也不代表合作、授权或背书关系。

- [迭戈·里维拉艺术家资料](https://www.moma.org/artists/4942-diego-rivera)

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
