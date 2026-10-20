# 胡安·米罗

[English](README.en.md)

![胡安·米罗代表图](gallery-16x9.jpg)

> **分类：** 艺术家
> **类型：** 艺术家
> **目录：** `style-packages/artists/joan-miro`

## 简介

这是一个面向「胡安·米罗」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 策展短评

“生物形态线条、留白、原色岛屿与轻盈非对称”决定了这个包的观看距离。人物、物体和环境都可以另行指定。

## 风格重点

生物形态线条、留白、原色岛屿与轻盈非对称。Prompt 会优先表达这些可观察特征，同时保留新主题、新构图和新的对象关系。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 参考来源

- [MoMA：胡安·米罗艺术家资料](https://www.moma.org/artists/4016-joan-miro)
- [MoMA：Daphnis and Chloé](https://www.moma.org/collection/works/61026)

## 新架构：悬置的有机形与开放色场（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，只在用户要求抽象或风格化形体组合并声明 `suspended-biomorphic-sign-field` 时启用。不对称间距和留白是基础规则；调用者可按需声明 `user-requested-drawn-line-with-separate-abstract-forms` 和 `user-requested-limited-color-abstract-composition`，启用线条连接或局部色块规则。不会自动加入星星、眼睛、鸟、人物、文字、月亮等固定图像。

这与克林特依靠轴线、螺旋和几何—有机对照建立结构的方法不同，也不同于蒙德里安的正交网格；米罗方向让曲线、分离色形和开放底色形成较松动的视觉关系。MoMA 对米罗符号语言、曲线和生物形态的说明可作形式依据，但不复用任何具体符号或构图。

```powershell
python tools/compile-style.py style-packages/artists/joan-miro --direction package --context suspended-biomorphic-sign-field --subject "One black crescent, one red triangle, one cobalt-blue irregular oval, and one thin black curved line on a warm-white ground; keep all four marks distinct and leave generous open space"
```

[`comparisons/`](comparisons/) 保存旧版与新方向 job、提示词及样图；新版以旧图作构图参考，曲线从色形下方延展为更清楚的视觉路径，形体仍彼此分离并留有空地。生成有随机性，方向保持实验状态，待视觉评审。

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
