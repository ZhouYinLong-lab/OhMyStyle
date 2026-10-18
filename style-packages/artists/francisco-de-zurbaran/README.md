# 弗朗西斯科·德·苏巴朗

[English](README.en.md)

![弗朗西斯科·德·苏巴朗 代表图](gallery-16x9.jpg)

> **分类：** 艺术家
> **媒介领域：** 绘画
> **目录：** `style-packages/artists/francisco-de-zurbaran`

## 简介

静物与人物的雕塑性油画；孤立主体、安静的几何体和大面积暗背景制造修道院式静默；炭黑、灰白、赭褐、暗红和少量金黄形成克制色组。

这是一个可独立使用的风格包。它把可观察的媒介、构图、光线、色彩、表面、纹理和复现步骤整理成可执行规则，用于生成新的主题，不用于复制某一件具体作品。

## 策展短评

我会先看“静物与主体的雕塑性油画；孤立主体、安静的几何体和大面积暗背景制造修道院式静默；炭黑、灰白、赭褐、暗红和少量金黄形成克制色组”。它把观看节奏定下来，题材可以按你的需要替换。

## 使用前先看

- `identity.yaml`：范围、对象和排除项
- `visual-signature.yaml`：跨主题仍应保持的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础 Prompt 与负面约束
- `palette/palette.json`：色彩角色与色值
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源和权利边界

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、流派、学校或游戏的原作，也不代表合作、授权或背书关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 以及仓库根目录的 [`NOTICE`](../../../NOTICE)。

## 新架构：静物秩序与聚焦侧光（实验）

[`art-direction.yaml`](art-direction.yaml) 仅在显式声明 `ordered-object-still-life` 时启用。它围绕用户指定的物件组织留白，以单一侧光呈现体积和材质差异；不会默认添加柑橘、玫瑰、器皿或宗教意象。

这不同于卡拉瓦乔方向用强烈明暗对照组织近景人物和戏剧性动作，也不同于培根方向通过空间框架与轮廓偏移制造张力。苏巴朗方向关注的是稀疏物件之间的秩序、静态侧光及材质辨析。

```powershell
python tools/compile-style.py style-packages/artists/francisco-de-zurbaran --direction package --context ordered-object-still-life --subject "One blue ceramic teapot and a folded linen cloth on a plain wooden table"
```

可查看 [`comparisons/`](comparisons/) 中的旧版/新版编译提示词和示意图。该方向仍为实验规则，示意图不是实际模型渲染结果。

## 只使用此包

四种方式可以按手边工具任选其一，不需要同时使用。

### 方式一：交给有生图能力的 Agent

把整个风格包目录上传给 Agent，或把本地目录路径交给它，并附上：

```text
请使用这个风格包帮助我生成图片。

请先读取本目录中的 identity.yaml、visual-signature.yaml、reproduction.yaml、
prompts/base.txt、prompts/negative.txt、palette/palette.json 和 evaluation.yaml。
请把文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。

我的生成需求是：
<填写人物、物体、场景、画幅和用途>

请先编译完整 Prompt，再调用你的生图能力。生成后按照 evaluation.yaml 检查风格特征、
构图、颜色、材质、AI 痕迹和需求遵循度，并说明仍然存在的风险。
```

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，替换主题、人物、物体、场景和画幅；将 `prompts/negative.txt` 作为负面 Prompt 一并提交到支持文本生图的平台。需要更稳定时，同时参考视觉签名和调色板。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，将基础 Prompt、负面约束、调色板和必要的参考清单一起提交。API Key 只保存在你的环境中；本仓库不代管密钥、不托管在线生图服务，也不承诺某个平台的免费额度或接口兼容性。

### 方式四：本地模型 + ComfyUI

将基础 Prompt 和负面约束接入本地模型或 ComfyUI 工作流；按调色板、复现说明和参考清单设置颜色、构图、材质与光线。生成后用 `evaluation.yaml` 做人工或自动复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。


