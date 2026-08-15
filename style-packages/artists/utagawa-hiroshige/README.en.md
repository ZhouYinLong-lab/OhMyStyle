# Utagawa Hiroshige

[中文](README.md)

![Utagawa Hiroshige representative image](gallery-16x9.jpg)

> **Category:** Artist  · **Medium:** 木版画
> **Directory:** style-packages/artists/utagawa-hiroshige

## Overview

以远近层叠、季节气候、留白与裁切式视角组织木版画画面，强调空气、节奏和自然形体的简洁秩序。

## A short note

江户时代风景版画中的气候观察、构图裁切和色面节奏. The package is best understood as a transferable set of visual decisions: 裁切式不对称取景, supported by light, surface, and spatial structure. It extracts observable traits without importing the subject, composition, or story of a source work.

## Visual signature

- 裁切式不对称取景
- 天气与空气透视作为主要空间信号
- 靛蓝与灰蓝色层配合简洁木刻线
- 主体保持开放，不自动加入名胜或人物故事

## Subject independence

This package controls visual treatment only. It does not choose the user's people, objects, locations, quantities, actions, or story. The representative image and benchmark subject are demonstrations, not default generation requirements. No landmark, character, building, prop, game level, or narrative event is inserted automatically.

## Sources and rights

Sources are used for research and attribution. External artworks, photographs, game images, trademarks, and platform pages remain with their respective rights holders. The generated example is an original anonymous scene, not an original work by the referenced artist, photographer, movement, technique, or game, and does not imply endorsement or affiliation.

- [Morning Glories](https://www.metmuseum.org/art/collection/search/39648)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository NOTICE (../../../NOTICE) for source and redistribution notes.

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
