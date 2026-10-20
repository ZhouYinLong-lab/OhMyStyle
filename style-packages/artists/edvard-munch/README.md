# 爱德华·蒙克

[English](README.en.md)

![爱德华·蒙克 代表图](gallery-16x9.jpg)

> **分类：** 艺术家
> **类型：** 艺术家
> **目录：** `style-packages/artists/edvard-munch`

## 简介

这是一个面向「爱德华·蒙克」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 策展短评

这个方向的气质落在“用心理色彩、承载身体张力的轮廓、压缩的空间和反复出现的有机或建筑节奏表达情绪；重点是视觉心理，不复制任何标志性构图”上。保住这条线索，换成新的主体也能成立。

## 风格重点

用心理色彩、承载身体张力的轮廓、压缩的空间和反复出现的有机或建筑节奏表达情绪；重点是视觉心理，不复制任何标志性构图。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 参考来源

- [https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Scream_-_Google_Art_Project.jpg](https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_The_Scream_-_Google_Art_Project.jpg)
- [https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Madonna_(1894-1895).jpg](https://commons.wikimedia.org/wiki/File:Edvard_Munch_-_Madonna_(1894-1895).jpg)

## 来源与版权

参考资料用于研究和视觉分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家或摄影师的原作，也不代表合作或授权关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库的 [`NOTICE`](../../../NOTICE)。

## 新架构：心理色彩与环境节奏（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，聚焦蒙克 1890 年代部分象征主义与表现主义作品，并仅在用户声明 `psychological-expressionist-scene` 时启用。它把颜色的情绪作用和主体与环境之间的曲线节奏写成可检查规则；只有调用者声明 `compressed-space-supports-emotion` 时，才应用局部空间压缩规则。不会默认加入焦虑表情、孤独人物、海岸、桥或夕阳，也不复现《呐喊》的构图。

它与梵高方向以顺着物体表面的笔触、颜料厚度和冷暖笔触关系为重点不同；蒙克方向更关注色彩关系如何设定情绪，以及轮廓与环境如何共同承载这种情绪。

```powershell
python tools/compile-style.py style-packages/artists/edvard-munch --direction package --context psychological-expressionist-scene --subject "A tired traveler sitting in a quiet room beside a closed window" --output runs/style-v2/edvard-munch-job.json
```

此方向仍为实验规则，跨题材和同题生图评审尚未完成。

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
