# 琼·米切尔

[English](README.en.md)

![琼·米切尔代表图](gallery-16x9.jpg)

> **分类：** 艺术家
> **媒介领域：** 绘画
> **目录：** `style-packages/artists/joan-mitchell`

## 简介

以大面积留白、强烈而断续的笔触、滴落与擦拭痕迹，把可辨认的景观记忆转化为开放的抽象空间。

这是一个可独立使用的风格包。它把可观察的媒介、构图、光线、色彩、表面、纹理和复现步骤整理成可执行规则，用于生成新的主题，不用于复制某一件具体作品。

## 策展短评

这类画面最动人的地方，是颜料既像在描述空间，又始终拒绝把空间说完。先留下大块安静的底色，再用几组有方向的笔触建立速度、重量和停顿，最后用擦拭与滴落保留手的痕迹。主体可以很普通，重要的是它要经得住这套节奏的重新组织。

## 主体独立性

本包只决定“怎么生成”，不决定“生成什么”。人物、物体、地点、建筑、植物、车辆和叙事由你的 Prompt 决定；本包中的具体场景只属于示例或测试，不会作为默认主体加入生成结果。

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

## 新架构：互相回应的色彩笔触群（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，只在用户要求抽象笔触画面并声明 `counterposed-color-stroke-groups` 时启用。笔触群方向与颜料重量是基础规则；只有用户允许保留未覆盖底色时，才声明 `open-field-or-visible-unpainted-ground` 启用留白节奏规则。不会自动画出地平线、树木、水面或花朵。琼·米切尔基金会记录了她在厚涂、薄层、线状笔触和颜色关系上的变化，国家美术馆资料也描述了横向笔触与斜向、竖向笔触的交错。

这与米罗把独立色形和曲线符号悬置在开放底色上的方向不同，也与波洛克式满幅滴洒纹理不同：米切尔方向以不同笔触群的色彩重量和疏密间隔构成节奏，保留可见的画布空地。

```powershell
python tools/compile-style.py style-packages/artists/joan-mitchell --direction package --context counterposed-color-stroke-groups --subject "A horizontal abstract field with cobalt and olive horizontal strokes at left, short yellow vertical strokes near center, and a violet diagonal cluster at right, separated by broad warm-white ground; no objects or horizon"
```

[`comparisons/`](comparisons/) 保存旧版与新方向 job、提示词和样图；新版以旧图作构图参考，笔触厚薄和群落反向关系更明显，底色间隔仍保留。样图的厚涂效果偏强，已列为评审点。方向保持实验状态，待视觉评审。

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
