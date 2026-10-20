# 克劳德·莫奈

[English](README.en.md)

![克劳德·莫奈 代表图](gallery-16x9.jpg)

> **分类：** 艺术家
> **类型：** 艺术家
> **目录：** `style-packages/artists/claude-monet`

## 简介

这是一个面向「克劳德·莫奈」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 策展短评

先把“围绕转瞬即逝的光线与空气色彩组织画面，用松散而可见的笔触捕捉普通景物在不同时间里的变化，避免厚重轮廓和过度强调的笔触表演”做准，其他内容可以留给你的 Prompt。这样换一个主题，风格仍不会散掉。

## 风格重点

围绕转瞬即逝的光线与空气色彩组织画面，用松散而可见的笔触捕捉普通景物在不同时间里的变化，避免厚重轮廓和过度强调的笔触表演。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 新版方向（实验）

`art-direction.yaml` 使用方向格式 2.1.0，将新版方向拆为条件光色、相邻色触、选择性大气边缘、依表面变化的笔触、普通母题构图，以及仅在显式声明 `series-request` 时启用的系列观察规则。它强调同一时刻里天气与光线如何改变画面，不等同于整体粉彩滤镜、均匀柔焦或随处撒点。

这与索罗亚方向的区分是：莫奈优先表现天气和时段造成的综合色彩、空气距离和相邻色触；索罗亚优先表现明确日光方向、可追溯的反射光和清楚的明暗分组。两者都能表现户外光线，但不能互换成同一套暖亮或蓝紫滤镜。

新版规则为实验状态，需显式启用；省略 `--direction` 时仍走原有包路径：

```powershell
python tools/compile-style.py style-packages/artists/claude-monet --direction package --context daylight --subject "A small stone footbridge beside a quiet pond under cool, overcast autumn daylight; no lilies or people" --output runs/monet-v2-job.json
```

生图效果尚未完成评审。用 `evaluation.yaml` 对比至少两个不同天气或时段，并确认没有擅自加入睡莲、教堂、干草堆等固定母题。

## 参考来源

- [https://commons.wikimedia.org/wiki/File:Claude_Monet_-_The_Magpie_-_Google_Art_Project.jpg](https://commons.wikimedia.org/wiki/File:Claude_Monet_-_The_Magpie_-_Google_Art_Project.jpg)
- [https://www.nga.gov/artworks/52186-argenteuil](https://www.nga.gov/artworks/52186-argenteuil)
- [Musée d'Orsay：Monet and changing weather, time, and season](https://www.musee-orsay.fr/en/program/whats-on/exhibitions/presentation/lucas-arruda-quimporte-le-paysage)
- [Musée d'Orsay：Wind Effect, Series of Poplars](https://www.musee-orsay.fr/en/artworks/effet-de-vent-serie-des-peupliers-119429)
- [National Gallery of Art：Claude Monet](https://www.nga.gov/artists/1726-claude-monet)

## 来源与版权

参考资料用于研究和视觉分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家或摄影师的原作，也不代表合作或授权关系。

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

请把这些文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。如采用新版方向，须显式按其适用条件和拒绝条件执行；默认路径保持原有提示内容。

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
