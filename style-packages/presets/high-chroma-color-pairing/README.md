# 高纯度撞色

[English](README.en.md)

![高纯度撞色 代表图](gallery-16x9.jpg)

> **分类：** 原创预设
> **类型：** 原创视觉预设
> **目录：** `style-packages/presets/high-chroma-color-pairing`

## 简介

这是一个面向「高纯度撞色」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 风格重点

这是一个不绑定主体的色彩方向预设：用明确的高纯度互补配色、浅色或深色反底、受控的面积比例和清晰的材质区分组织画面，不模拟某位艺术家的外观。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 完整生成示例

下面的示例保留完整的竖版画面，不使用横版画廊缩略图的裁切方式。顶部的 `gallery-16x9.jpg` 仅用于分类画廊展示；这张图用于观察人物、服装与背景之间的完整撞色关系。

<p align="center">
  <img src="examples/accepted/color-pairing-portrait.png" width="560" alt="高纯度撞色完整竖版生成示例">
</p>

## 参考来源

- [https://www.bilibili.com/video/BV1acjF68E6N/?spm_id_from=333.1387.favlist.content.click&vd_source=dc8a446ed48dbc0e71281a3db9654692](https://www.bilibili.com/video/BV1acjF68E6N/?spm_id_from=333.1387.favlist.content.click&vd_source=dc8a446ed48dbc0e71281a3db9654692)
- [https://www.bilibili.com/video/BV1qe4y1d71z?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2589621-cb5r7.1785986300627.4&vd_source=dc8a446ed48dbc0e71281a3db9654692](https://www.bilibili.com/video/BV1qe4y1d71z?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2589621-cb5r7.1785986300627.4&vd_source=dc8a446ed48dbc0e71281a3db9654692)

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

参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。模型权重、API Key 和生成图片由使用者自行管理。## 策展短评

“这是一个不绑定主体的色彩方向预设：用明确的高纯度互补配色、浅色或深色反底、受控的面积比例和清晰的材质区分组织画面，不模拟某位艺术家的外观”是很好的入口：它先安排画面的呼吸，再让具体内容进入。

## 简介

这是一个面向「高纯度撞色」的独立风格包。它把公开作品、研究资料和可观察的媒介、构图、色彩、光线、材质与纹理决策整理为可执行约束，用于生成新的主题，不用于复制某一幅具体作品。

## 风格重点

这是一个不绑定主体的色彩方向预设：用明确的高纯度互补配色、浅色或深色反底、受控的面积比例和清晰的材质区分组织画面，不模拟某位艺术家的外观。

完整规则见 `visual-signature.yaml`、`reproduction.yaml`、`palette/palette.json` 和 `evaluation.yaml`。

## 完整生成示例

下面的示例保留完整的竖版画面，不使用横版画廊缩略图的裁切方式。顶部的 `gallery-16x9.jpg` 仅用于分类画廊展示；这张图用于观察人物、服装与背景之间的完整撞色关系。

<p align="center">
  <img src="examples/accepted/color-pairing-portrait.png" width="560" alt="高纯度撞色完整竖版生成示例">
</p>

## 参考来源

- [https://www.bilibili.com/video/BV1acjF68E6N/?spm_id_from=333.1387.favlist.content.click&vd_source=dc8a446ed48dbc0e71281a3db9654692](https://www.bilibili.com/video/BV1acjF68E6N/?spm_id_from=333.1387.favlist.content.click&vd_source=dc8a446ed48dbc0e71281a3db9654692)
- [https://www.bilibili.com/video/BV1qe4y1d71z?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2589621-cb5r7.1785986300627.4&vd_source=dc8a446ed48dbc0e71281a3db9654692](https://www.bilibili.com/video/BV1qe4y1d71z?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2589621-cb5r7.1785986300627.4&vd_source=dc8a446ed48dbc0e71281a3db9654692)

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
