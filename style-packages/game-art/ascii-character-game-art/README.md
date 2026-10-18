# ASCII 字符游戏美术

[English](README.en.md)

![ASCII 字符游戏美术 代表图](gallery-16x9.jpg)

> **分类：** 游戏美术
> **媒介领域：** 游戏美术
> **目录：** `style-packages/game-art/ascii-character-game-art`

## 简介

用字母、数字和标点构成空间、角色与材质，把字符栅格的密度、字体和对比关系作为主要图形语言。

这是一个可独立使用的风格包。它把可观察的媒介、构图、光线、色彩、表面、纹理和复现步骤整理成可执行规则，用于生成新的主题，不用于复制某一件具体作品。

## 策展短评

本包把ASCII 字符游戏美术的可观察规则拆成可迁移的构图、媒介、色彩和表面决策；只保留风格特征，不复刻来源作品。

## 主体独立性

本包只决定“怎么生成”，不决定“生成什么”。人物、物体、地点、建筑、植物、车辆和叙事由你的 Prompt 决定；本包中的具体场景只属于示例或测试，不会作为默认主体加入生成结果。

## 严格字符构建

字符画必须由固定宽度 ASCII 字符网格逐行堆叠构成。每个可见场景形状都要对应网格中的字符单元；最终图片只能把这些字符用等宽字体逐格栅格化，可为字符着色，但不能增加网格里不存在的形状。不能先生成一张普通图片，再叠加字符纹理或伪造字符效果。

本包代表图的源网格在 `examples/ascii-cave-grid.txt`，渲染器在 `render_gallery.py`。运行 `python render_gallery.py` 可从源网格重新生成 `gallery-16x9.jpg`。代表图中的洞穴、火把和角色均由字符堆叠绘出。

## 使用前先看

- `identity.yaml`：范围、对象和排除项
- `visual-signature.yaml`：跨主题仍应保持的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础 Prompt 与负面约束
- `palette/palette.json`：色彩角色与色值
- `evaluation.yaml`：生成后的检查标准
- `art-direction.yaml`：严格字格路线的可选实验方向；普通旧路径仍保持兼容
- `references/manifest.csv`、`provenance.yaml`：来源和权利边界

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、流派、学校或游戏的原作，也不代表合作、授权或背书关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 以及仓库根目录的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

四种方式可以按手边工具任选其一，不需要同时使用。

### 方式一：交给能输出字符网格的 Agent

把整个风格包目录上传给 Agent，或把本地目录路径交给它，并附上：

```text
请使用这个风格包帮助我构建字符画。

请先读取本目录中的 identity.yaml、visual-signature.yaml、reproduction.yaml、
prompts/base.txt、prompts/negative.txt、palette/palette.json 和 evaluation.yaml。
请把文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。

我的生成需求是：
<填写人物、物体、场景、画幅和用途>

请先输出固定宽度、仅含可打印 ASCII 字符的逐行网格。所有场景形状都必须由字符本身堆叠出来，
不得调用图像生成器画一张“看起来像字符画”的图片，也不得添加网格外的图形。需要图片时，
用本包的 render_gallery.py 作为栅格化实现参考。最后按照 evaluation.yaml 检查字符网格、
构图、颜色、材质和需求遵循度，并说明仍然存在的问题。
```

### 方式二：直接复制字符构建规则

打开 `prompts/base.txt`，替换主题、人物、物体、场景和画幅，要求模型输出固定宽度 ASCII 网格；不要把这组规则提交给普通文生图模型。需要图片时，使用等宽字体按字符单元渲染网格。`prompts/negative.txt` 列出了必须排除的近似做法。

### 方式三：通过 API 生成字符网格

在你自己的文本模型 API 或编译工具中配置 API Key，让模型返回字符网格，再由应用逐格栅格化。不要将网格交给文生图 API 重新绘制。API Key 只保存在你的环境中；本仓库不代管密钥、不托管在线服务，也不承诺某个平台的免费额度或接口兼容性。

### 方式四：本地模型 + ComfyUI

使用本地文本模型生成固定宽度字符网格，再通过代码或 ComfyUI 中严格逐字符渲染的节点输出图片。不要使用会重绘字符结构的图像生成节点。完成后用 `evaluation.yaml` 做人工或自动复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。

## 新架构：严格 ASCII 网格方向（实验）

[`art-direction.yaml`](art-direction.yaml) 把严格字符构建写成编译器可读的方向规则：先输出固定行列的纯 ASCII 字符源，再逐格用等宽字体栅格化。它仍处于实验状态；图像生成模型不能参与重绘。新版方向与旧版默认入口并存，只有显式指定 `--direction package` 才会使用它。

```powershell
python tools/compile-style.py style-packages/game-art/ascii-character-game-art --direction package --subject "One explorer holding a torch inside a cavern" --output runs/style-v2/ascii-job.json
python tools/render-ascii-grid.py runs/style-v2/ascii-job.json --source style-packages/game-art/ascii-character-game-art/examples/ascii-cave-grid.txt --font C:/Windows/Fonts/consola.ttf --output runs/style-v2/ascii-cave-render
```

渲染器只从字符源画出字符，不会补画网格外的轮廓、阴影或纹理。需要新题材时，先创作并检查字符源，再运行栅格器。当前方向固定 100 列、36 行；主体可读性和新题材迁移效果仍待人工评审。
