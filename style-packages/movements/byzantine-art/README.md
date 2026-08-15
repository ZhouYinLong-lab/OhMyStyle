# 拜占庭艺术

[English](README.en.md)

![拜占庭艺术 代表图](gallery-16x9.jpg)

> **分类：** 艺术流派与历史时期  · **媒介领域：** 绘画
> **目录：** style-packages/movements/byzantine-art

## 简介

以正面秩序、金色或深色背景、稳定轮廓、象征性尺度和克制的平面层次建立超越日常空间的视觉庄严感。

## 一点观察

拜占庭艺术的庄严不只来自金色，也来自正面秩序、稳定轮廓和被压缩的空间。这个包把视觉重点放在平面层次、象征性光泽和仪式感构图上，不自动生成圣像、教堂或宗教人物。

## 视觉签名

- 稳定、正面、近似仪式性的排列；空间深度被压缩，主体轮廓优先；以对称或近对称建立持续的视觉安定感
- 金色、深蓝、暗红和赭色形成象征性色彩关系；高光集中而克制，不制造写实金属反射；背景可简化为深色或金色的平面场
- 均匀而正面的光线，强调轮廓和色面，不使用强烈自然阴影
- 平滑的矿物色层、细密装饰性纹理和局部金属光泽

## 主体独立性

本包只决定“怎么生成”，不决定“生成什么”。人物、物体、地点、建筑、植物、车辆和叙事由你的 Prompt 决定；代表图和测试题材只是演示，不会成为默认内容。这个包不会自动加入固定地标、角色、族群、宗教场景、游戏关卡或故事事件。

## 使用前先看

- [identity.yaml](identity.yaml)：范围、对象和排除项
- [visual-signature.yaml](visual-signature.yaml)：跨主题仍应保持的视觉特征
- [reproduction.yaml](reproduction.yaml)：媒介、材料和构建顺序
- [prompts/base.txt](prompts/base.txt)、[prompts/negative.txt](prompts/negative.txt)：基础 Prompt 与负面约束
- [palette/palette.json](palette/palette.json)：色彩角色与色值
- [evaluation.yaml](evaluation.yaml)：生成后的检查标准
- [references/manifest.csv](references/manifest.csv)、[provenance.yaml](provenance.yaml)：来源和权利边界

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、流派、技法或游戏的原作，也不代表合作、授权或背书关系。

- [大都会艺术博物馆：拜占庭艺术资料](https://www.metmuseum.org/met-publications/the-arts-of-byzantium-the-metropolitan-museum-of-art-bulletin-v-58-no-4-spring-2001)

详细来源和再分发边界见 [provenance.yaml](provenance.yaml)、[references/manifest.csv](references/manifest.csv) 以及仓库根目录的 [NOTICE](../../../NOTICE)。

## 只使用此包

四种方式可以按手边工具任选其一，不需要同时使用。

### 方式一：交给有生图能力的 Agent

把整个风格包目录上传给 Agent，或把本地目录路径交给它，并附上：

~~~
请使用这个风格包帮助我生成图片。

请先读取本目录中的 identity.yaml、visual-signature.yaml、reproduction.yaml、
prompts/base.txt、prompts/negative.txt、palette/palette.json 和 evaluation.yaml。
请把文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。

我的生成需求是：
<填写人物、物体、场景、画幅和用途>

请先编译完整 Prompt，再调用你的生图能力。生成后按照 evaluation.yaml 检查风格特征、
构图、颜色、材质、AI 痕迹和需求遵循度，并说明仍然存在的风险。
~~~

### 方式二：直接复制 Prompt

打开 [prompts/base.txt](prompts/base.txt)，替换主题、人物、物体、场景和画幅；将 [prompts/negative.txt](prompts/negative.txt) 作为负面 Prompt 一并提交到支持文本生图的平台。需要更稳定时，同时参考视觉签名和调色板。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，将基础 Prompt、负面约束、调色板和必要的参考清单一起提交。API Key 只保存在你的环境中；本仓库不代管密钥、不托管在线生图服务。

### 方式四：本地模型 + ComfyUI

将基础 Prompt 和负面约束接入本地模型或 ComfyUI 工作流；按调色板、复现说明和参考清单设置颜色、构图、材质与光线。生成后用 [evaluation.yaml](evaluation.yaml) 做人工或自动复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。
