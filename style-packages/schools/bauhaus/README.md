# 包豪斯

[English](README.en.md)

![包豪斯代表图](gallery-16x9.jpg)

> **分类：** 艺术与摄影学校
> **目录：** `style-packages/schools/bauhaus`

## 简介

这是一个面向「包豪斯」的独立风格包。它把公开资料与可观察的媒介、构图、色彩、光线、材质和纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 风格重点

强调几何秩序、基本形、原色关系、功能结构与负空间；可以用于平面、空间、产品和抽象构成，不复制具体设计作品。

## 参考来源

- [包豪斯德绍官方历史介绍](https://www.bauhaus.de/en/das-bauhaus/)
- [MoMA 包豪斯收藏检索](https://www.moma.org/collection/?q=bauhaus)

## 来源与版权

参考资料用于研究和视觉分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不代表合作或授权关系。

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
- art-direction.yaml（仅当任务明确要求纸材研究方向）
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

参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。模型权重、API Key 和生成图片由使用者自行管理。## 策展短评

我会先看“强调几何秩序、基本形、原色关系、功能结构与负空间；可以用于平面、空间、产品和抽象构成，不复制具体设计作品”。它把观看节奏定下来，题材可以按你的需要替换。

## 简介

这是一个面向「包豪斯」的独立风格包。它把公开资料与可观察的媒介、构图、色彩、光线、材质和纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 风格重点

强调几何秩序、基本形、原色关系、功能结构与负空间；可以用于平面、空间、产品和抽象构成，不复制具体设计作品。

## 参考来源

- [包豪斯德绍官方历史介绍](https://www.bauhaus.de/en/das-bauhaus/)
- [MoMA 包豪斯收藏检索](https://www.moma.org/collection/?q=bauhaus)

## 来源与版权

参考资料用于研究和视觉分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不代表合作或授权关系。

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

## 可选实验方向：预备课程纸材研究

包内的 [`art-direction.yaml`](art-direction.yaml) 记录一条范围有限的纸材构成方法：以切、撕、折解释形体，检查纸面连续性、连接、开口和投影。它转译的是与约瑟夫·阿尔伯斯预备课程相关的纸材练习，不代表包豪斯整体的统一视觉风格。该方向仍处于实验阶段，须显式声明 `paper-study` 上下文；普通包豪斯任务仍使用原有风格签名和 Prompt。

官方课程介绍记载了使用纸张并通过切、撕、折探索材料、无需胶水的练习；德绍包豪斯基金会的练习档案也记录了纸材结构、切割、压折、稳定性与材料经济性。这里把这些资料转写为可观察的构图规则，规则的视觉效果仍待跨题材评审。

```powershell
python tools/compile-style.py style-packages/schools/bauhaus --direction package --context paper-study --subject "A small paper pavilion made from one sheet using cuts and folds, with a clear opening" --output runs/style-v2/bauhaus-paper-job.json
```

编译结果是交给生图工具使用的任务描述，不会自动调用生图服务。生成图只用于视觉研究，不能证明纸结构真实可制作或承重。
