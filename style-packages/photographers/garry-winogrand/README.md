# 加里·维诺格兰德

[English](README.en.md)

![加里·维诺格兰德代表图](gallery-16x9.jpg)

> **分类：** 摄影师  
> **媒介领域：** 摄影  
> **目录：** `style-packages/photographers/garry-winogrand`

## 简介

这个包提取三十五毫米街头观察、贴近现场的距离感、活跃的斜线、相互穿插的动作和没有被整理干净的瞬间。它适合让画面像偶然被看见，而不是像完成姿势后摆拍出来。

它不规定城市、人群、地标或公共交通。新的主题仍由使用者决定，包只负责观看方式、裁切、影调、胶片表面和时间感。

## 策展短评

维诺格兰德式的力量常常来自“还差一点就看清”的瞬间：人物彼此遮挡，画面边缘突然闯入一个动作，地平线也不必端正。它不把街头变成背景板，而是把观看者放回人流之中。代表图保留这种靠近和不稳定，但没有把纽约或某种固定人群写成必要条件。

## 主体独立性

你的主题、人物、物体、地点和叙事优先。本包只负责摄影媒介、观察距离、取景、影调、胶片颗粒和动作关系。代表图中的人行道与行走者只是示例，不会自动出现在新的生成结果里。

## 使用前先看

- `identity.yaml`：范围与排除项
- `visual-signature.yaml`：换主体后仍应保留的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础约束
- `palette/palette.json`：影调角色
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源与权利边界

## 来源与版权

展览介绍和馆藏页面只用于研究可观察特征。外部摄影作品及其图像权利仍归原权利人所有；本包不捆绑外部作品，也不复制某张照片的构图、人物或地点。代表图是新的匿名场景，不代表与摄影师或机构存在合作、授权或背书关系。

来源： [大都会艺术博物馆的加里·维诺格兰德展览介绍](https://www.metmuseum.org/exhibitions/listings/2014/garry-winogrand)。详细边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库根目录的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

### 方式一：交给有生图能力的 Agent

把本目录上传给 Agent，或提供本地路径，并告诉它：先读取身份、视觉签名、复现说明、Prompt、影调、评估文件，再把你的主题编译成完整 Prompt。要求它只使用包中的观察和摄影规则，不添加城市、人群或地标等固定题材，并在生成后按 `evaluation.yaml` 检查。

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，替换主题、地点和画幅；把 `prompts/negative.txt` 一并作为负面约束。需要更稳定时，同时参考视觉签名和影调表。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，再提交基础 Prompt、负面约束、影调和必要的参考清单。本仓库不托管密钥，也不提供在线生图服务。

### 方式四：本地模型 + ComfyUI

把基础 Prompt 和负面约束接入本地模型或 ComfyUI 工作流，按复现说明设置取景、影调、胶片颗粒和动作关系，生成后用 `evaluation.yaml` 复核。

模型权重、密钥和生成图片由使用者自行管理。参考资料用于理解特征，不用于复制原作。
