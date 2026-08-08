# 暖纸色静物

[中文](README.md)

![Representative image of 暖纸色静物](gallery-16x9.jpg)

> **Category:** 摄影
> **Directory:** `style-packages/presets/warm-paper-still-life`

## Overview

以暖象牙色纸面、手工边缘、天然物件和柔和侧光建立触感明确的静物预设。 The package turns medium, composition, lighting, palette, material, and surface decisions into executable rules that can be transferred to new subjects and scenes.

## Observable features

warm ivory paper, handmade edges, natural objects, tactile side light.

## References

- [OhMyStyle 项目说明](https://github.com/ZhouYinLong-lab/OhMyStyle)
- [本包的原创整理声明](https://github.com/ZhouYinLong-lab/OhMyStyle)

## Origin and rights

本包为 OhMyStyle 独立整理的原创预设，不指向某位艺术家、摄影师、学校或具体作品。 External works, school names, marks, and page content remain with their respective rights holders. The generated example is a new anonymous scene and does not imply endorsement or authorization.

## Use only this package

Choose one of the following methods; they do not need to be combined.

### Method 1: Give the package to an image-capable Agent

Upload this directory to an image-capable Agent, or provide its local path, and ask it to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/base.txt`, `prompts/negative.txt`, `palette/palette.json`, and `evaluation.yaml`. Ask the Agent to compile your brief into a complete prompt, generate a new scene, and review the result against `evaluation.yaml` without copying a reference work, mark, or composition.

### Method 2: Copy the prompt

Replace the subject, scene, aspect ratio, and purpose in `prompts/base.txt`; submit `prompts/negative.txt` as the negative prompt. Use the visual signature and palette when tighter control is needed.

### Method 3: Submit through an API-key workflow

Configure your own API key in the image platform or compiler, then submit this package’s base prompt, negative constraints, palette, and selected references. This repository does not host a generation service or manage secrets.

### Method 4: Local model + ComfyUI

Connect the prompts to a local model or ComfyUI workflow; use the palette, reference manifest, and reproduction rules as controls, then review the output with `evaluation.yaml`.

References are for observable feature study only. Do not reproduce source composition, people, text, marks, school emblems, or logos.
