# Weegee

[中文](README.md)

![Weegee representative image](gallery-16x9.jpg)

> **Category:** photographer  · **Domain:** photography
> **Directory:** style-packages/photographers/weegee

## Overview

以夜间闪光、直接的新闻现场、强烈黑白反差和未经修饰的街头瞬间建立紧迫而具体的观察感。

## Curatorial note

维吉的照片有一种近距离的现场感，光线不负责美化，而是把人物、街道和偶然发生的动作一下子推到观者面前。这个包借用直接闪光、黑白反差和新闻式取景，但不生成案件、警车或纽约地标。

## Visual signature

- 近距离、略带侵入性的现场取景; 人物动作和环境线索共同构成信息; 保留偶然遮挡、偏心和不完美的瞬间
- 以黑白为主，黑位明确、亮部直接; 彩色变体只保留少量现场色，不使用统一电影调色; 反光路面和浅色服装承担视觉闪点
- 相机轴线附近的直接闪光，前景清楚，背景快速退入暗部
- 新闻照片般的清晰颗粒、硬质高光和真实街面反射

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

- [International Center of Photography: Weegee: Society of the Spectacle](https://www.icp.org/exhibitions/weegee-society-spectacle)

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
