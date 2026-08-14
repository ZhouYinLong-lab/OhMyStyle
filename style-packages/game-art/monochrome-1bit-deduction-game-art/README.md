# 单色一位推理游戏美术

[English](README.en.md)

![单色一位推理游戏美术代表图](gallery-16x9.jpg)

> **分类：** 游戏美术  
> **媒介领域：** 复古计算机图形启发的二维推理游戏美术  
> **目录：** `style-packages/game-art/monochrome-1bit-deduction-game-art`

## 简介

这个方向把画面压缩到严格的黑白一位逻辑里：中间调不靠连续灰度，而靠点阵密度、像素簇和剪影建立。空间必须足够清楚，玩家才能从门、楼梯、材质和少量线索里读出关系。它和普通像素美术的差别在于，核心不是调色板数量，而是显示限制、抖动秩序和信息阅读。

## 策展短评

我喜欢这种视觉的克制。颜色被拿走以后，光线、材质和空间都要用很少的黑白关系重新说明，画面反而更容易留下记忆。使用时要先保证场景能走、能看、能找线索，再决定点阵密度；如果所有区域都被噪点填满，一位风格就会变成不可读的黑白纹理。

## 主体独立性

本包只决定一位显示、抖动密度、剪影、透视和线索可读性，不规定船只、海洋、海员、尸体、谋杀案或具体角色。代表图中的建筑通道只是测试主体，新的生成应以用户需求和游戏用途为准。

## 来源与版权

研究入口为[《Return of the Obra Dinn》官方网站](https://obradinn.com/)，并参考[开发者关于一位美术的访谈文章](https://blog.playstation.com/archive/2019/10/17/lucas-pope-on-the-challenge-of-creating-return-of-the-obra-dinns-art-style/)。仓库不打包外部游戏资产；代表图是新的匿名场景，不是具体游戏画面，也不表示合作、授权或背书关系。

## 只使用此包

### 方式一：交给有生图能力的 Agent

把本目录交给 Agent，让它先读取 `identity.yaml`、`visual-signature.yaml`、`reproduction.yaml`、`prompts/`、`palette/palette.json` 和 `evaluation.yaml`，再编译你的主体、画幅和用途。生成后检查一位逻辑、空间透视、抖动密度和线索可读性。

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，替换 `{{SUBJECT}}`、`{{ASPECT_RATIO}}` 和 `{{USE_CASE}}`；把 `prompts/negative.txt` 一并提交给支持负面 Prompt 的平台。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，提交基础 Prompt、负面约束和调色板。本仓库不托管密钥或在线生图服务。

### 方式四：本地模型 + ComfyUI

将 Prompt、调色板和复现说明接入本地模型或 ComfyUI，生成后用 `evaluation.yaml` 复核，不要把代表图里的建筑通道当成默认主体。
