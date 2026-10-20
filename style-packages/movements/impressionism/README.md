# 印象主义

[English](README.en.md)

![印象主义代表图](gallery-16x9.jpg)

> **分类：** 艺术流派与历史时期
> **类型：** 艺术流派
> **目录：** `style-packages/movements/impressionism`

## 简介

这是一个面向「印象主义」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 风格重点

瞬时光、破碎笔触、反射色与户外空气。Prompt 会优先表达这些可观察特征，同时保留新主题、新构图和新的对象关系。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 新版方向（实验）

`art-direction.yaml` 使用方向格式 2.1.0，描述印象主义作为一个**流派层级**的共享方法：快速可见的绘画动作、受光线影响的局部颜色，以及即时但经过安排的构图。只有调用者声明 `visible-reflective-surface` 时，才应用依据反射来源组织彩色阴影的规则。它不规定所有画家使用同一种笔触，也不把点彩画法自动当作印象主义的标准答案。

这与莫奈个人包不同：莫奈包聚焦某一位画家的天气观察、系列母题与远近空气变化；本包只保留多位参与者共有的技法倾向，并允许题材与构图变化。它也不同于索罗亚包的强方向日光与明确反射光，以及新印象主义的系统分点排列。需要特定画家时，应选择对应艺术家包。

新版规则尚处实验状态，需显式启用；不传 `--direction` 时，仍使用已有提示词：

```powershell
python tools/compile-style.py style-packages/movements/impressionism --direction package --context daylight --context visible-reflective-surface --subject "A neighborhood street market after rain, vendors arranging crates, muted spring daylight" --output runs/impressionism-v2-job.json
```

评审时至少比较三种不同主体，并改变光照条件；确认快速笔触与局部光色仍可见，同时没有自动长出睡莲、舞者、咖啡馆等艺术家个人母题。

## 参考来源

- [Various artists / 19世纪后期](https://commons.wikimedia.org/w/index.php?search=Impressionism+painting&title=Special:MediaSearch&type=image)
- [The Metropolitan Museum of Art: Impressionism: Art and Modernity](https://www.metmuseum.org/pt/essays/impressionism-art-and-modernity)
- [National Gallery, London: Guide to Impressionism](https://www.nationalgallery.org.uk/paintings/learn-about-art/guide-to-impressionism?viewPage=1)
- [Musée d'Orsay: Paris 1874, Inventing Impressionism](https://www.musee-orsay.fr/en/node/278990)

## 来源与版权

参考链接只用于研究和视觉分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有；本包不重新分发受版权保护的原作。代表图是新的匿名生成场景，不是相关艺术家、摄影师、设计师或游戏的原作，也不代表合作或授权关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

四种方式可以按手边的工具任选其一，不需要同时使用。

### 方式一：交给有生图能力的 Agent

把整个风格包目录上传给具备生图能力的 Agent，或把本地目录路径交给它，并附上下面的任务说明：

```
请使用这个风格包帮助我生成图片。

请先读取本目录中的：
- identity.yaml
- visual-signature.yaml
- art-direction.yaml（如需启用新版规则）
- reproduction.yaml
- prompts/base.txt
- prompts/negative.txt
- palette/palette.json
- evaluation.yaml

请把这些文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。
使用新版方向时，请保留流派层级的共享方法，不要擅自套用某一位画家的标志母题或构图。

我的生成需求是：
<填写人物、物体、场景、画幅和用途>

请先把我的需求编译成完整 Prompt，再调用你的生图能力生成图片。生成后，请按照 evaluation.yaml 检查风格特征、构图、颜色、材质、AI 痕迹和 Prompt 遵循度；如果发现明显问题，请说明问题并进行一次针对性修正。
```

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，将其中的主题、人物、物体、场景和画幅替换为自己的需求；把 `prompts/negative.txt` 中的限制作为负面 Prompt 一并提交到支持文本生图的平台。需要更稳定时，同时参考 `visual-signature.yaml` 和 `palette/palette.json`。

### 方式三：配置 API Key 后提交生成

在你使用的生图平台或自己的编译工具中配置 API Key，将本包的基础 Prompt、负面约束、调色板和必要的参考图一起提交。API Key 只保存在你自己的环境中；本仓库不代管密钥、不托管在线生成服务，也不承诺某个平台的免费额度或接口兼容性。

### 方式四：本地模型 + ComfyUI

将 `prompts/base.txt` 和 `prompts/negative.txt` 接入本地模型或 ComfyUI 工作流；按 `palette/palette.json` 调整颜色，按 `references/manifest.csv` 选择参考图，并用 `reproduction.yaml` 中的参数约束构图、材质和光线。生成后可用 `evaluation.yaml` 做人工或自动复核。

参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。模型权重、API Key 和生成图片由使用者自行管理。## 策展短评

“瞬时光、破碎笔触、反射色与户外空气”决定了这个包的观看距离。人物、物体和环境都可以另行指定。

## 简介

这是一个面向「印象主义」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 风格重点

瞬时光、破碎笔触、反射色与户外空气。Prompt 会优先表达这些可观察特征，同时保留新主题、新构图和新的对象关系。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 参考来源

- [Various artists / 19世纪后期](https://commons.wikimedia.org/w/index.php?search=Impressionism+painting&title=Special:MediaSearch&type=image)

## 来源与版权

参考链接只用于研究和视觉分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有；本包不重新分发受版权保护的原作。代表图是新的匿名生成场景，不是相关艺术家、摄影师、设计师或游戏的原作，也不代表合作或授权关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

四种方式可以按手边的工具任选其一，不需要同时使用。

### 方式一：交给有生图能力的 Agent

把整个风格包目录上传给具备生图能力的 Agent，或把本地目录路径交给它，并附上下面的任务说明：

```
请使用这个风格包帮助我生成图片。

请先读取本目录中的：
- identity.yaml
- visual-signature.yaml
- reproduction.yaml
- prompts/base.txt
- prompts/negative.txt
- palette/palette.json
- evaluation.yaml

请把这些文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。

我的生成需求是：
<填写人物、物体、场景、画幅和用途>

请先把我的需求编译成完整 Prompt，再调用你的生图能力生成图片。生成后，请按照 evaluation.yaml 检查风格特征、构图、颜色、材质、AI 痕迹和 Prompt 遵循度；如果发现明显问题，请说明问题并进行一次针对性修正。
```

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，将其中的主题、人物、物体、场景和画幅替换为自己的需求；把 `prompts/negative.txt` 中的限制作为负面 Prompt 一并提交到支持文本生图的平台。需要更稳定时，同时参考 `visual-signature.yaml` 和 `palette/palette.json`。

### 方式三：配置 API Key 后提交生成

在你使用的生图平台或自己的编译工具中配置 API Key，将本包的基础 Prompt、负面约束、调色板和必要的参考图一起提交。API Key 只保存在你自己的环境中；本仓库不代管密钥、不托管在线生成服务，也不承诺某个平台的免费额度或接口兼容性。

### 方式四：本地模型 + ComfyUI

将 `prompts/base.txt` 和 `prompts/negative.txt` 接入本地模型或 ComfyUI 工作流；按 `palette/palette.json` 调整颜色，按 `references/manifest.csv` 选择参考图，并用 `reproduction.yaml` 中的参数约束构图、材质和光线。生成后可用 `evaluation.yaml` 做人工或自动复核。

参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。模型权重、API Key 和生成图片由使用者自行管理。
