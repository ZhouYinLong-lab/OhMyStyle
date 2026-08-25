# Persona 4 Golden Game Art

[中文](README.md)

![Persona 4 Golden game art representative image](gallery-16x9.jpg)

> **Category:** Game art  · **Medium:** Game art<br>
> **Directory:** `style-packages/game-art/persona-4-golden`

## Overview

This package builds bright everyday spaces from sunny yellow, warm white, and leaf green, then adds post-rain reflections, distant haze, and a friendly human scale. It creates a subtle mystery without automatically adding a television, shopping street, rural town, or named character.

## A note from observation

The package is not a yellow filter. It starts with ordinary life: roads, low buildings, trees, and utility lines keep their scale and perspective. Wet surfaces and distant haze then change the air. The bright palette keeps the image approachable, while the uncertainty comes from space and weather rather than horror effects.

## Visual signature

- Sunny yellow, warm white, ochre, and leaf green as the bright main palette
- Everyday streets or environments with readable perspective and scale
- Wet reflections adding spatial depth after rain
- Distant soft haze creating restrained uncertainty
- Red, dark brown, or blue-gray used as small counterpoints

## Subject independence

The package controls visual treatment, not the user's subject, object count, location, action, or story. The street, bicycle, hills, and post-rain weather in the representative image are demonstration content only and are not part of the default prompt.

## Sources and rights

This package studies observable characteristics from the official source page. It does not copy game screenshots, characters, interfaces, logos, or a specific composition. The generated example is an original anonymous scene and does not imply authorization, collaboration, or endorsement by ATLUS or SEGA.

- [Official source page](https://persona.atlus.com/p4g/)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for source and redistribution boundaries.

## Use only this package

Choose any one of the following four methods:

### Method 1: Give it to an image-capable Agent

Give the complete package directory to an Agent. Ask it to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/base.txt`, `prompts/negative.txt`, `palette/palette.json`, and `evaluation.yaml` before compiling your subject. Review subject preservation, palette, composition, materials, and exclusions after generation.

### Method 2: Copy the Prompt

Open [prompts/base.txt](prompts/base.txt), replace `{subject}`, `{composition}`, and `{aspect_ratio}`, then submit it together with [prompts/negative.txt](prompts/negative.txt) to a text-to-image platform.

### Method 3: Submit through your own API key

Configure your own image platform or compiler with an API key, then submit the base prompt, negative constraints, palette, and any needed reference list. This repository does not host an image service or manage API keys.

### Method 4: Local model + ComfyUI

Feed the base prompt and negative constraints into a local model or ComfyUI workflow. Use the palette, reproduction notes, and reference manifest to control the sunny-yellow field, wet reflections, distant haze, and everyday scale. Add masks in the workflow when stronger local control is needed.

Model weights, API keys, and generated images remain under the user's control. Use references to study observable characteristics, not to copy a source work's composition, people, text, trademarks, or interface.
