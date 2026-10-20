# 迭戈·委拉斯开兹

[English](README.en.md)

![迭戈·委拉斯开兹 代表图](gallery-16x9.jpg)

> **分类：** 艺术家
> **类型：** 艺术家
> **目录：** `style-packages/artists/diego-velazquez`

## 简介

这是一个面向「迭戈·委拉斯开兹」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 策展短评

“以宫廷肖像和主体画的克制秩序为基础：深色空间中只保留必要的光，准确处理脸部与织物，并让宽松的笔触在轮廓边缘自然消散”决定了这个包的观看距离。人物、物体和环境都可以另行指定。

## 风格重点

以宫廷肖像和人物画的克制秩序为基础：深色空间中只保留必要的光，准确处理脸部与织物，并让宽松的笔触在轮廓边缘自然消散。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 参考来源

- [https://commons.wikimedia.org/wiki/File:Diego_Vel%C3%A1zquez_-_Las_Meninas.jpg](https://commons.wikimedia.org/wiki/File:Diego_Vel%C3%A1zquez_-_Las_Meninas.jpg)
- [https://commons.wikimedia.org/wiki/File:Retrato_de_Juan_Pareja](https://commons.wikimedia.org/wiki/File:Retrato_de_Juan_Pareja)
- [普拉多博物馆：容易理解的《宫娥》](https://www.museodelprado.es/en/whats-on/multimedia/las-meninas-diego-velazquez/c43f1c8d-e6c9-a8c2-44dc-0c9be2e10177)
- [伦敦国家美术馆：腓力四世肖像](https://www.nationalgallery.org.uk/paintings/diego-velazquez-philip-iv-of-spain)
- [大都会艺术博物馆：胡安·德·帕雷哈](https://www.metmuseum.org/art/collection/search/437869)

## 来源与版权

参考资料用于研究和视觉分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家或摄影师的原作，也不代表合作或授权关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库的 [`NOTICE`](../../../NOTICE)。

## 新架构：目光、纵深与选择性精确（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，仅在用户要求的室内肖像或群像中启用：以精细焦点作基础规则；调用者可按画面是否包含互动人物或可见纵深，分别声明 `multiple-people-or-person-engaged-with-subject`、`interior-with-visible-spatial-depth`，再启用视线关系或房间纵深规则。它不默认镜子、门口、宫廷服饰或特定群像布局；也不同于卡拉瓦乔方向以单一强光和近景动作作为中心。

```powershell
python tools/compile-style.py style-packages/artists/diego-velazquez --direction package --context observed-interior-portrait --subject "Three musicians rehearsing in a dim room, one listening while another checks the sheet music" --output runs/style-v2/diego-velazquez-job.json
```

此方向仍为实验规则；同题生图对照和跨主体稳定性待人工评审。

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

## 新旧架构视觉对照

查看[同题样图、编译任务和复核限制](comparisons/README.md)。该对照是单题材初步检查，方向仍处于实验状态。
