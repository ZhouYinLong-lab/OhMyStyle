# Braid Hand-Painted Puzzle Game Art

[中文](README.md)

![Braid Hand-Painted Puzzle Game Art representative image](gallery-16x9.jpg)

> **Category:** Game art  · **Medium:** 游戏美术
> **Directory:** style-packages/game-art/braid-hand-painted-puzzle

## Overview

以层叠半透明颗粒、手绘背景、柔和边缘和高密度自然细节制造像活画一样的二维谜题空间。

## A short note

独立游戏中手绘环境、半透明粒子和可读谜题空间的视觉实践. The package is best understood as a transferable set of visual decisions: 二维空间层叠与可玩路径可读性, supported by light, surface, and spatial structure. It extracts observable traits without importing the subject, composition, or story of a source work.

## Visual signature

- 二维空间层叠与可玩路径可读性
- 手绘背景结合半透明颗粒
- 有机色阶和柔和边界
- 环境细节丰富但不依赖固定角色或故事

## Subject independence

This package controls visual treatment only. It does not choose the user's people, objects, locations, quantities, actions, or story. The representative image and benchmark subject are demonstrations, not default generation requirements. No landmark, character, building, prop, game level, or narrative event is inserted automatically.

## Sources and rights

Sources are used for research and attribution. External artworks, photographs, game images, trademarks, and platform pages remain with their respective rights holders. The generated example is an original anonymous scene, not an original work by the referenced artist, photographer, movement, technique, or game, and does not imply endorsement or affiliation.

- [Braid, Anniversary Edition](https://braid-game.com/)

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
