# Orientalism

[中文版](README.md)

![Orientalism representative](gallery-16x9.jpg)

> **Category:** movement  · **Domain:** painting
> **Path:** style-packages/movements/orientalism

## Overview

研究十九世纪欧洲艺术中的东方想象及其事实与幻想的交错，提取装饰性空间、暖土色、冷色阴影和材质细节，同时明确反对把族群、地点或异国情节写成默认主体。

## Curatorial note

这个词本身带有历史距离，不能只当作一组“异国情调”滤镜。包里保留它的历史语境：装饰性空间、旅行图像中的光线、织物和建筑细节，以及事实与想象之间的张力。生成时，主体和地点由使用者决定，避免把特定族群、宗教、服饰或殖民叙事当成模板。

## Subject independence

This package controls how an image is generated, not what it depicts. People, objects, places, architecture, plants, vehicles, and narrative come from the user's prompt. The representative image is only a demonstration and must not become a default subject.

## Visual signature

- 装饰性边框或建筑平面作为空间秩序
- 赭土、烟褐、沙金与深靛蓝形成温冷对照
- filtered directional light, dusty atmosphere, and cool shadow planes with controlled highlights
- aged paint, textile-like patterning, mineral walls, glazed ceramics, and carefully observed material accents

## Sources and rights

References are used for research and visual analysis. External artworks, photographs, game imagery, trademarks, and platform pages remain the property of their respective rights holders. The generated example is a new anonymous scene and is not an original work by, or endorsement from, the referenced source.

- [东方主义：事实与幻想之间](https://www.metmuseum.org/exhibitions/orientalism-between-fact-and-fantasy)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for redistribution boundaries.

## Use only this package

1. Give this directory to an image-capable Agent and ask it to read the YAML files, prompts, palette, and evaluation before compiling a prompt.
2. Copy prompts/base.txt, replace the subject and location, and send prompts/negative.txt as the negative prompt.
3. Submit the compiled prompt through your own API tool after configuring your own API key; this repository does not host generation.
4. Connect the prompt, palette, reproduction notes, and reference manifest to a local model or ComfyUI workflow.

Do not copy a source work's exact composition, figures, text, trademark, logo, game asset, or fixed subject. Users manage model weights, API keys, generated images, and storage themselves.
