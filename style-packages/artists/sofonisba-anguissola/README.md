# 索福尼斯巴·安圭索拉

[English](README.en.md)

![索福尼斯巴·安圭索拉代表图](gallery-16x9.jpg)

> **分类：** 艺术家<br>
> **媒介领域：** 绘画<br>
> **目录：** `style-packages/artists/sofonisba-anguissola`

## 简介

以清晰而柔和的肖像塑造、敏锐的目光交流和克制的衣料细节呈现人物关系，让表情与手势承担叙事。人物肖像只是可选测试主题，不会覆盖用户指定的主体。

## 策展短评

这里的肖像靠目光和手势建立关系，华服与背景只提供必要线索。用这套规则时，可以先决定人物之间如何看、如何回应，再把细节留给最能说明关系的脸和手。

## 文件导览

- `identity.yaml`：风格范围、开放主体策略与排除项
- `visual-signature.yaml`：跨主题稳定的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础 Prompt 与负面约束
- `palette/palette.json`：色彩角色和值
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源与权利边界

## 来源与权利

来源清单链接至大都会艺术博物馆、普拉多博物馆和瑞典国家博物馆的馆藏资料，仅用于研究。仓库不包含历史原作或馆藏照片。视觉规则概括克制的色调塑造、个体化表情和选择性细节，不复刻任何特定肖像或人物。

## 使用此包

读取 `prompts/base.txt`，替换 `{SUBJECT}` 与 `{LOCATION}`，并一并提交 `prompts/negative.txt`。生成后按 `evaluation.yaml` 检查需求遵循、人物表达、媒介感和细节控制。也可在自己的 API 或本地模型工作流中使用；本仓库不托管生图服务或 API Key。

代表图和样例是新生成内容，尚待人工审核，不是安圭索拉的作品，也不代表授权或背书。
