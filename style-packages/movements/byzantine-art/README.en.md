# Byzantine Art

[中文](README.md)

![Byzantine Art representative image](gallery-16x9.jpg)

> **Category:** movement  · **Domain:** painting
> **Directory:** style-packages/movements/byzantine-art

## Overview

以正面秩序、金色或深色背景、稳定轮廓、象征性尺度和克制的平面层次建立超越日常空间的视觉庄严感。

## Curatorial note

拜占庭艺术的庄严不只来自金色，也来自正面秩序、稳定轮廓和被压缩的空间。这个包把视觉重点放在平面层次、象征性光泽和仪式感构图上，不自动生成圣像、教堂或宗教人物。

## Visual signature

- 稳定、正面、近似仪式性的排列; 空间深度被压缩，主体轮廓优先; 以对称或近对称建立持续的视觉安定感
- 金色、深蓝、暗红和赭色形成象征性色彩关系; 高光集中而克制，不制造写实金属反射; 背景可简化为深色或金色的平面场
- 均匀而正面的光线，强调轮廓和色面，不使用强烈自然阴影
- 平滑的矿物色层、细密装饰性纹理和局部金属光泽

## Subject independence

This package controls how an image is rendered, not what must be rendered. The user’s people, objects, places, buildings, plants, vehicles, and narrative remain authoritative. The representative image is a demonstration, not a default subject. The package does not silently add a landmark, character, group, religious scene, game level, or story event.

## Files to read

- [identity.yaml](identity.yaml): scope and exclusions
- [visual-signature.yaml](visual-signature.yaml): transferable visual decisions
- [reproduction.yaml](reproduction.yaml): medium and construction sequence
- [prompts/base.txt](prompts/base.txt) and [prompts/negative.txt](prompts/negative.txt): prompt constraints
- [palette/palette.json](palette/palette.json): color roles
- [evaluation.yaml](evaluation.yaml): review criteria
- [references/manifest.csv](references/manifest.csv) and [provenance.yaml](provenance.yaml): source and rights boundary

## Source and rights

External artworks, photographs, trademarks, and platform pages remain the property of their respective rights holders. The generated example is an original anonymous scene and does not claim affiliation, authorization, endorsement, or exact imitation.

- [The Metropolitan Museum of Art: The Arts of Byzantium](https://www.metmuseum.org/met-publications/the-arts-of-byzantium-the-metropolitan-museum-of-art-bulletin-v-58-no-4-spring-2001)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for the detailed boundary.

## Use this package only

Choose one of the following methods.

### 1. Give it to an image-capable Agent

Upload this directory or provide its local path, then ask the Agent to read the package files, compile the prompt, generate the image, and review it against [evaluation.yaml](evaluation.yaml).

### 2. Copy the prompt

Open [prompts/base.txt](prompts/base.txt), replace the subject and format, and submit it together with [prompts/negative.txt](prompts/negative.txt). Use the visual signature and palette when the model needs more guidance.

### 3. Submit through your own API key

Configure your provider or compiler with your own API key, then send the base prompt, negative constraints, palette, and relevant source manifest. The repository does not host a generation service or store credentials.

### 4. Local model and ComfyUI

Connect the prompts to your local model or ComfyUI workflow. Translate the palette, reproduction notes, and visual signature into nodes or conditioning, then review the result with [evaluation.yaml](evaluation.yaml).

Model weights, API keys, and generated images are managed by the user. References are for observable analysis; do not copy a source work’s exact composition, people, text, trademarks, or logos.
