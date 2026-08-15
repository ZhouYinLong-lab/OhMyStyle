# 射线主义

[English](README.en.md)

![射线主义代表图](gallery-16x9.jpg)

> **分类：** 艺术流派与历史时期  
> **媒介领域：** 20世纪初俄国先锋绘画  
> **目录：** style-packages/movements/rayonism

## 简介

射线主义把光线、运动和色彩交叠成独立的绘画结构。它并不是把一个太阳形状放在画面中心，也不是普通的放射渐变；真正重要的是来自多个方向的线束如何互相穿过，透明色面如何把主体拆成新的空间关系。

## 策展短评

这个包适合那些不想让抽象只剩下“好看的颜色”的画面。它会迫使色彩承担方向，迫使线条承担空间，也让主体在被拆开之后仍然留下可追踪的骨架。使用时，主体可以很普通，变化发生在观看方式。

## 主体独立性

本包只决定先锋绘画媒介、交错线束、色场叠加和画布表面，不规定人物、物体、地点或故事。代表图中的抽象色场只是测试主体。

## 来源与版权

研究入口包括[苏格兰国家美术馆的射线主义术语页](https://www.nationalgalleries.org/art-and-artists/glossary-terms/rayismrayonism)和[现代艺术博物馆相关作品记录](https://www.moma.org/collection/works/80480?sov_referrer=theme&theme_id=5102)。仓库不打包外部作品；代表图是新的匿名抽象画面，不是具体原作，也不表示合作、授权或背书关系。

## 只使用此包

### 方式一：交给有生图能力的 Agent

把整个风格包目录交给 Agent，先读取 identity.yaml、visual-signature.yaml、reproduction.yaml、prompts、palette/palette.json 和 evaluation.yaml，再把你的主体、画幅和用途编译进生成任务。

### 方式二：直接复制 Prompt

复制 prompts/base.txt，替换主体和画幅；把 prompts/negative.txt 一并提交。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，提交基础 Prompt、负面约束和调色板。本仓库不托管密钥或在线生图服务。

### 方式四：本地模型 + ComfyUI

将 Prompt、调色板和复现说明接入本地模型或 ComfyUI，生成后用 evaluation.yaml 检查交错方向、色带层次、绘画表面和固定题材泄漏。
