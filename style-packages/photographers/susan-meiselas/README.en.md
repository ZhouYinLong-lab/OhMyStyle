# Susan Meiselas

[中文](README.md)

![Susan Meiselas representative](gallery-16x9.jpg)

> **Category:** Photographer  
> **Domain:** Photography  
> **Path:** `style-packages/photographers/susan-meiselas`

## Overview

This package extracts the patience of long-form documentary work, people placed within their environments, field relationships, natural color, and human-scale viewing distance. It keeps the sense that life is continuing without turning the subject into a news event or fixed social scene.

It does not prescribe war, carnival, protest, country, or community. The user chooses the subject; the package controls observation, context, tone, and photographic surface.

## Curatorial note

Meiselas’s work suggests that documentary strength does not come only from one intense instant. It also comes from staying with a place long enough for gestures, walls, roads, and distances between people to become information. The representative image uses an ordinary gathering to show that relation; what should transfer is respect for context, not a country or event.

## Subject independence

Your subject, people, objects, place, and narrative remain authoritative. This package controls documentary medium, viewing distance, environmental context, natural color, and film surface. The courtyard and gathering in the representative image are examples only and are not added to new generations.

## Read before use

- `identity.yaml`: scope and exclusions
- `visual-signature.yaml`: traits that survive a subject change
- `reproduction.yaml`: medium, materials, and build order
- `prompts/base.txt`, `prompts/negative.txt`: prompt constraints
- `palette/palette.json`: color roles
- `evaluation.yaml`: post-generation checks
- `references/manifest.csv`, `provenance.yaml`: sources and rights boundaries

## Sources and rights

Photographer and institutional pages are used to study observable traits. External photographs and their images remain the property of their rights holders; this package does not bundle external works or copy a specific photograph’s composition, people, or event. The representative image is a new anonymous scene and does not imply collaboration, authorization, or endorsement.

Source: [Susan Meiselas at Magnum Photos](https://www.magnumphotos.com/photographer/susan-meiselas/). See [`provenance.yaml`](provenance.yaml), [`references/manifest.csv`](references/manifest.csv), and the repository [`NOTICE`](../../../NOTICE).

## Use only this package

### Method 1: Give the package to an image-capable Agent

Upload this directory or provide its local path. Ask the Agent to read the identity, visual signature, reproduction, prompt, palette, and evaluation files first, then compile your subject into a complete prompt. Tell it to use only the package’s documentary and contextual rules, avoid forced wars, carnivals, and protests, and review the result against `evaluation.yaml`.

### Method 2: Copy the prompts

Open `prompts/base.txt`, replace the subject, location, and aspect ratio, and send `prompts/negative.txt` as the negative prompt. Use the signature and palette for tighter control.

### Method 3: Submit through your own API tool

Configure an API key in your own image platform or compiler, then submit the base prompt, negative constraints, palette, and required reference list. This repository does not host a generation service or manage keys.

### Method 4: Local model + ComfyUI

Connect the prompts to a local model or ComfyUI workflow. Use the reproduction notes to set relationships, context, natural color, and photographic surface, then review the output with `evaluation.yaml`.

Users manage model weights, keys, and generated images. References are for understanding traits, not for copying source photographs.
