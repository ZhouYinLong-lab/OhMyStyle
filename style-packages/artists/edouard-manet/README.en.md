# Édouard Manet

[中文](README.md)

![Édouard Manet representative image](gallery-16x9.jpg)

> **Category:** artist  · **Domain:** painting
> **Directory:** style-packages/artists/edouard-manet

## Overview

以平直而有张力的色面、现代生活的截取感、清晰轮廓和不完全抛光的笔触打破传统画面秩序。

## Curatorial note

马奈有一种把画面拉回眼前的力量：色块不总是被柔和地过渡，人物和物件像刚刚被看到，既具体又带着未完成感。这个包强调平面色面、现代截取和轮廓张力，不自动加入巴黎街景、咖啡馆或特定人物。

## Visual signature

- 像被偶然截取的现代生活片段; 主体与背景之间保持清楚的平面关系; 避免过度解释空间，让视觉重心停留在形体和色面
- 黑、白、灰与一两个明确色块并置; 肤色和材料色保持直接，不做过度综合色; 暗部偏平而不全部压成黑色
- 自然或室内光线直接落在形体上，明暗关系清楚但不过度塑造
- 可见而克制的笔触，边缘在清楚和松动之间变化

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

- [The Metropolitan Museum of Art: Édouard Manet (1832–1883)](https://www.metmuseum.org/fr/essays/edouard-manet-1832-1883)

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
