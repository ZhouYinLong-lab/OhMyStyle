# 亚历克·索思

[English](README.en.md)

![亚历克·索思代表图](gallery-16x9.jpg)

> **分类：** 摄影师  
> **媒介领域：** 摄影  
> **目录：** `style-packages/photographers/alec-soth`

## 简介

这个包提取大画幅彩色纪实摄影中的耐心观察、普通地点、宽阔留白和人与环境之间的安静距离。画面可以有轻微的不协调，却不靠戏剧化事件制造情绪。

## 策展短评

索思式的观看很少急着把地点解释清楚。道路、建筑、天空和远处的人各自保留一点距离，正是这些没有被填满的部分让画面产生余韵。代表图用了一个边缘地点来展示这种空间关系，但换成你的主题后，真正需要保留的是“让环境与主体共同说话”的耐心，而不是公路、郊外或某个国家的标志。

## 主体独立性

本包只决定摄影的观察方式、空间、光线、色彩和表面，不规定道路、汽车旅馆、草原、旗帜、美国地点或孤独人物。代表图中的郊外建筑和远处人物只是示例，使用者提供的主体优先。

## 使用前先看

- `identity.yaml`：范围与排除项
- `visual-signature.yaml`：换主体后仍应保留的视觉特征
- `reproduction.yaml`：摄影构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础约束
- `palette/palette.json`：色彩角色
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源与权利边界

## 来源与版权

本包参考[亚历克·索思官方网站的介绍](https://alecsoth.com/photography/about)，只提取可观察的摄影特征。外部照片及其图像权利仍归原权利人所有；代表图是新的原创场景，不复制具体照片，也不表示与摄影师、机构存在合作、授权或背书关系。详细边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库根目录的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

四种方式任选其一：

1. **交给有生图能力的 Agent**：把本目录交给 Agent，要求先读取身份、视觉签名、复现说明、Prompt、调色板和评估文件，再把你的主题编译成完整 Prompt；生成后按 `evaluation.yaml` 复核，不要只输入摄影师名字。
2. **直接复制 Prompt**：打开 `prompts/base.txt`，替换 `{SUBJECT}` 与 `{LOCATION}`；将 `prompts/negative.txt` 一并提交。
3. **配置 API Key 后提交生成**：在你自己的平台或编译工具中配置 API Key，提交基础 Prompt、负面约束、调色板和必要参考清单。本仓库不托管密钥或在线生图服务。
4. **本地模型 + ComfyUI**：把基础 Prompt 和负面约束接入工作流，按复现说明设置观察距离、留白、自然光和胶片表面；生成后用 `evaluation.yaml` 复核。

模型权重、密钥和生成图片由使用者自行管理。参考资料用于理解特征，不用于复制原作。
