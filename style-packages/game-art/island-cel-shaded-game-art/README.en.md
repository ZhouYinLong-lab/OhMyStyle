# Island Cel-Shaded Game Art

[中文](README.md)

![Island Cel-Shaded Game Art representative image](gallery-16x9.jpg)

> **Category:** game_art  · **Domain:** game_art
> **Directory:** style-packages/game-art/island-cel-shaded-game-art

## Overview

以清晰卡通渲染、夸张但可读的轮廓、明亮海天色彩和绘画般的三维表面建立轻快而完整的游戏空间。

## Curatorial note

这类游戏美术把三维空间处理得像一幅清楚、明亮、带有绘画感的插画：轮廓可读，色块大胆，海天和建筑都保持轻快的形体关系。这个包提取卡通渲染和海岛色彩，不会固定生成海盗、木船、角色或某个游戏地图。

## Visual signature

- 清楚的前中后景和可读的游戏空间; 轮廓、路径和地标形体优先于细碎写实纹理; 画面保持轻快的视觉节奏和大色块平衡
- 海蓝、天空青、暖沙色和明亮绿植形成清爽关系; 阴影偏彩色而非纯黑; 强调色用于可交互或视觉重点，但不强制指定对象
- 明亮的自然日光，柔和但明确的卡通阴影，避免写实电影式压暗
- 简化而有绘画感的三维表面，边缘清楚，材质差异通过色块和形体表达

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

- [Nintendo: Iwata Asks: The Legend of Zelda: The Wind Waker HD](https://iwataasks.nintendo.com/interviews/wiiu/wind-waker/0/0/)

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
