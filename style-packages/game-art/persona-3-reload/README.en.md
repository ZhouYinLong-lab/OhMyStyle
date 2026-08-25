# Persona 3 Reload Game Art

[中文](README.md)

![Persona 3 Reload game art representative image](gallery-16x9.jpg)

> **Category:** Game art  · **Medium:** Game art<br>
> **Directory:** `style-packages/game-art/persona-3-reload`

## Overview

This package organizes nocturnal scenes with deep navy, cobalt blue, and cool violet, then adds clear silhouettes, urban structural geometry, restrained warm accents, and controlled atmosphere. It supports quiet urban fantasy game imagery without automatically adding a moon, school, train, or named character.

## A note from observation

The signature is not a blue filter. Blue controls the space: architecture and roads establish the skeleton, cool ambient light unifies materials, and warm color appears only as a local visual beat. The language can therefore transfer to a building, still life, or portrait without carrying over a fixed scene.

## Visual signature

- Deep navy, cobalt blue, and cool violet as the main value structure
- Urban structures, wires, rails, or roads used as graphic geometry
- Cool moonlit ambience with readable silhouettes
- Small amber accents reserved for local light or reflection
- Clean digital edges with restrained texture and haze

## Subject independence

The package controls visual treatment, not the user's subject, object count, location, action, or story. The platform, moon, city, wires, and figure in the representative image are demonstration content only and are not part of the default prompt.

## Sources and rights

This package studies observable characteristics from the official source page. It does not copy game screenshots, characters, interfaces, logos, or a specific composition. The generated example is an original anonymous scene and does not imply authorization, collaboration, or endorsement by ATLUS or SEGA.

- [Official source page](https://persona.atlus.com/p3r/index.html?lang=enbuy)

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

Feed the base prompt and negative constraints into a local model or ComfyUI workflow. Use the palette, reproduction notes, and reference manifest to control the cool-blue values, limited warm light, silhouettes, and spatial layers. Add masks in the workflow when stronger local control is needed.

Model weights, API keys, and generated images remain under the user's control. Use references to study observable characteristics, not to copy a source work's composition, people, text, trademarks, or interface.
