# Stained Glass

[中文版](README.md)

![Stained Glass representative](gallery-16x9.jpg)

> **Category:** technique  · **Domain:** hybrid
> **Path:** style-packages/techniques/stained-glass

## Overview

以玻璃分片、铅线分格、透光色块和投影色彩构成视觉语言。它可以服务抽象、建筑、人物或普通物体，不绑定宗教图像、教堂或固定故事。

## Curatorial note

彩绘玻璃的魅力来自两个方向同时发生：白天，颜色被光穿过；结构上，铅线又把画面切成清楚的分格。这个包适合做材料实验，也适合把一个普通主体放进有秩序的透光环境里。颜色要有玻璃的厚度、边缘和投影，而不是一层平面渐变。

## Subject independence

This package controls how an image is generated, not what it depicts. People, objects, places, architecture, plants, vehicles, and narrative come from the user's prompt. The representative image is only a demonstration and must not become a default subject.

## Visual signature

- 分格线建立清楚的几何骨架
- 宝石蓝、琥珀、红和紫以有限色块出现
- backlit or side-lit daylight that casts bounded colored shadows onto nearby surfaces
- thick translucent glass, lead seams, slight waviness, edge thickness, and small imperfections

## Sources and rights

References are used for research and visual analysis. External artworks, photographs, game imagery, trademarks, and platform pages remain the property of their respective rights holders. The generated example is a new anonymous scene and is not an original work by, or endorsement from, the referenced source.

- [馆藏与工艺资源](https://stainedglassmuseum.com/collections)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for redistribution boundaries.

## Use only this package

1. Give this directory to an image-capable Agent and ask it to read the YAML files, prompts, palette, and evaluation before compiling a prompt.
2. Copy prompts/base.txt, replace the subject and location, and send prompts/negative.txt as the negative prompt.
3. Submit the compiled prompt through your own API tool after configuring your own API key; this repository does not host generation.
4. Connect the prompt, palette, reproduction notes, and reference manifest to a local model or ComfyUI workflow.

Do not copy a source work's exact composition, figures, text, trademark, logo, game asset, or fixed subject. Users manage model weights, API keys, generated images, and storage themselves.
