# El Lissitzky

[中文](README.md)

![El Lissitzky representative image](gallery-16x9.jpg)

> **Category:** Artist  · **Medium:** 绘画与设计
> **Directory:** style-packages/artists/el-lissitzky

## Overview

以几何构造、空间投影、斜向动力和工程化版式建立视觉秩序，适合抽象图形、建筑表面与信息结构。

## A short note

莫斯科与柏林先锋派语境中的几何构成、空间投影和工程化视觉思维. The package is best understood as a transferable set of visual decisions: 几何块面与斜向向量建立视觉力场, supported by light, surface, and spatial structure. It extracts observable traits without importing the subject, composition, or story of a source work.

## Visual signature

- 几何块面与斜向向量建立视觉力场
- 强色作为结构节点而非综合色滤镜
- 模块化版式不绑定文字或固定题材
- 平面与投影同时保持清晰边缘

## Subject independence

This package controls visual treatment only. It does not choose the user's people, objects, locations, quantities, actions, or story. The representative image and benchmark subject are demonstrations, not default generation requirements. No landmark, character, building, prop, game level, or narrative event is inserted automatically.

## Sources and rights

Sources are used for research and attribution. External artworks, photographs, game images, trademarks, and platform pages remain with their respective rights holders. The generated example is an original anonymous scene, not an original work by the referenced artist, photographer, movement, technique, or game, and does not imply endorsement or affiliation.

- [El Lissitzky](https://www.moma.org/artists/3569-el-lissitzky)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository NOTICE (../../../NOTICE) for source and redistribution notes.

## New architecture: Proun axonometric space (experimental)

[`art-direction.yaml`](art-direction.yaml) uses direction format 2.1.0 and adopts one focused direction from Lissitzky's Proun works of 1919–1927: flat color planes and geometric volumes share one imagined space. Callers can declare `geometric-blocks-or-volumes-in-imagined-space` and `color-planes-distinguish-constructed-space` as applicable to activate axonometric or color-space rules. This is neither all of Constructivism nor the Bauhaus paper-cutting method. Red squares, slogans, stars, and political symbols are not defaults.

```powershell
python tools/compile-style.py style-packages/artists/el-lissitzky --direction package --context pictorial-architectonic-space --subject "A small reading lamp represented as a planar shade and a few interlocking geometric volumes" --output runs/style-v2/el-lissitzky-job.json
```

This direction remains experimental; same-subject and cross-subject visual review is pending.

## Use this package only

Choose one of the following methods; they are alternatives rather than steps to perform all at once.

### Method 1: Give the package to an image-capable Agent

Upload the package directory or provide its local path. Ask the Agent to read identity.yaml, visual-signature.yaml, reproduction.yaml, prompts/base.txt, prompts/negative.txt, palette/palette.json, and evaluation.yaml; compile the rules into your request, avoid copying reference art, generate the image, and review it against evaluation.yaml.

### Method 2: Copy the prompt directly

Open [prompts/base.txt](prompts/base.txt), replace the subject, objects, scene, and aspect ratio, and submit it with [prompts/negative.txt](prompts/negative.txt) to a text-to-image platform.

### Method 3: Configure an API key and submit a generation task

Configure an API key in your own image service or prompt compiler, then submit the base prompt, negative constraints, palette, and reference manifest. This repository does not manage secrets or host an online image service.

### Method 4: Local model + ComfyUI

Connect the base prompt and negative constraints to a local model or ComfyUI workflow. Use the palette and reproduction notes to set color, composition, material, and light. Review the output with [evaluation.yaml](evaluation.yaml).

Model weights, API keys, and generated images remain the user's responsibility. References explain observable features; do not copy a source work's exact composition, person, text, trademark, or logo.

## Legacy and direction comparison

See [the same-subject samples, compiled jobs, and review limitations](comparisons/README.md). This is a preliminary single-subject check; the direction remains experimental.
