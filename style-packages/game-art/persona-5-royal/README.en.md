# Persona 5 Royal Game Art

[中文](README.md)

![Persona 5 Royal game art representative image](gallery-16x9.jpg)

> **Category:** Game art  · **Medium:** Game art<br>
> **Directory:** `style-packages/game-art/persona-5-royal`

## Overview

This package builds a high-contrast three-color system from vermilion red, near-black, and paper white. Diagonal cuts, overlapping planes, bold silhouettes, and selective print texture create editorial momentum. It supports stylish, energetic imagery without automatically adding a mask, playing card, gun, phantom thief, or named city.

## A note from observation

The important part is how color and layout work together: red moves the eye, near-black cuts structure, and paper white creates breathing room. Diagonals and collage are not decoration; they are the rhythm of the image. Keeping only red and black would reduce the package to an ordinary duotone filter.

## Visual signature

- Vermilion red, near-black, and paper white as the core three-color system
- Diagonal cuts, cropped corners, and overlapping planes for editorial momentum
- Bold silhouettes with clear layout hierarchy
- Halftone, paper wear, or brush marks confined to selected layers
- Red concentrated on the subject, route, or visual focal point

## Subject independence

The package controls visual treatment, not the user's subject, object count, location, action, or story. The bridge, figure, paper pieces, and city geometry in the representative image are demonstration content only and are not part of the default prompt.

## Sources and rights

This package studies observable characteristics from the official source page. It does not copy game screenshots, characters, interfaces, logos, or a specific composition. The generated example is an original anonymous scene and does not imply authorization, collaboration, or endorsement by ATLUS or SEGA.

- [Official source page](https://persona.atlus.com/p5r/?lang=en)

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

Feed the base prompt and negative constraints into a local model or ComfyUI workflow. Use the palette, reproduction notes, and reference manifest to control the red-black-white hierarchy, diagonal direction, collage relationships, and local print texture. Add masks in the workflow when stronger local control is needed.

Model weights, API keys, and generated images remain under the user's control. Use references to study observable characteristics, not to copy a source work's composition, people, text, trademarks, or interface.
