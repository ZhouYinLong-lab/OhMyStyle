# Braid Hand-Painted Puzzle Game Art

[中文](README.md)

![Braid Hand-Painted Puzzle Game Art representative image](gallery-16x9.jpg)

> **Category:** Game art  · **Medium:** Game art
> **Directory:** style-packages/game-art/braid-hand-painted-puzzle

## Overview

Layered translucent particles, hand-painted backgrounds, soft edges, and richly detailed nature create a 2D puzzle world that feels like a living painting.

## A short note

This package draws on indie-game practices that combine hand-painted environments, translucent particles, and readable puzzle spaces. It translates those observations into reusable decisions about layered 2D space and legible traversal, supported by lighting, surfaces, and spatial structure. It does not import a source work’s subject, composition, or story.

## Visual signature

- Layered 2D spaces with readable routes
- Hand-painted backgrounds with translucent particles
- Organic color transitions and soft edges
- Rich environmental detail without a fixed character or story

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
