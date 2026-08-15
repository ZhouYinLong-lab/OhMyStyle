# Pictorialism

[中文版](README.md)

![Pictorialism representative](gallery-16x9.jpg)

> **Category:** movement  · **Domain:** photography
> **Path:** style-packages/movements/pictorialism

## Overview

以摄影的柔焦、纹理纸面、手工印相和朦胧的光线表达摄影的绘画性，同时保留摄影构图与暗房过程的可观察线索。

## Curatorial note

画意摄影最有意思的地方，是它曾经主动争论“照片要不要像照片”。柔焦、纸张纹理和手工干预不是装饰，而是把摄影从记录推向感受。这个包适合处理雾、逆光、湿地和安静人物，但不把任何固定风景或梦境当作默认主体。

## Subject independence

This package controls how an image is generated, not what it depicts. People, objects, places, architecture, plants, vehicles, and narrative come from the user's prompt. The representative image is only a demonstration and must not become a default subject.

## Visual signature

- 柔化边缘保留清晰的主结构
- 黑白、棕褐或低饱和色调均可
- diffused backlight, mist, or overcast light with a gentle luminous veil
- textured paper, soft-focus optical rendering, and subtle handmade print irregularity

## Sources and rights

References are used for research and visual analysis. External artworks, photographs, game imagery, trademarks, and platform pages remain the property of their respective rights holders. The generated example is a new anonymous scene and is not an original work by, or endorsement from, the referenced source.

- [国际画意摄影](https://www.metmuseum.org/essays/international-pictorialism)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for redistribution boundaries.

## Use only this package

1. Give this directory to an image-capable Agent and ask it to read the YAML files, prompts, palette, and evaluation before compiling a prompt.
2. Copy prompts/base.txt, replace the subject and location, and send prompts/negative.txt as the negative prompt.
3. Submit the compiled prompt through your own API tool after configuring your own API key; this repository does not host generation.
4. Connect the prompt, palette, reproduction notes, and reference manifest to a local model or ComfyUI workflow.

Do not copy a source work's exact composition, figures, text, trademark, logo, game asset, or fixed subject. Users manage model weights, API keys, generated images, and storage themselves.
