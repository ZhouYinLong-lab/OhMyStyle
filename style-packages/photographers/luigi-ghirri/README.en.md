# Luigi Ghirri

[中文版](README.md)

![Luigi Ghirri representative image](gallery-16x9.jpg)

> **Category:** Photographer　**Medium:** Restrained color photography　**Directory:** `style-packages/photographers/luigi-ghirri`

## Overview

Luigi Ghirri often turns ordinary places into questions about images themselves. Walls, models, signs, roads, and distant views shift gently in scale, while color stays quiet, soft, and ordered. This package extracts observation distance, color relationships, and the tension between reality and representation—not a travel location.

## Curatorial note

What I like is the restraint. The image does not rush to prove that it has atmosphere; a faded wall, a horizontal line, or an oddly scaled shape gradually changes the act of looking. State the subject clearly first, then let the photographic language remain quiet instead of stacking nostalgia words.

## Subject independence

This package controls observation distance, composition, daylight, color, and grain. Maps, models, coastlines, Italian buildings, and tourist landmarks are not defaults.

## File guide

- `identity.yaml`: source, scope, and subject boundaries
- `visual-signature.yaml`: distance, composition, color, and light
- `reproduction.yaml`: capture and grading order
- `prompts/`: base prompt and negative constraints
- `palette/palette.json`: color roles
- `evaluation.yaml`: subject-independence and signature checks
- `references/manifest.csv`, `provenance.yaml`: source and rights boundaries

## Sources and rights

The package references [MoMA’s Luigi Ghirri record](https://www.moma.org/artists/39882-luigi-ghirri) and the [Fondazione Luigi Ghirri biography](https://fondazioneluigighirri.it/en/artist/biography). Original photographs remain with their rights holders. The representative image is a new anonymous scene, not a copy or endorsement.

## Use only this package

### Method 1: Give it to an image-capable Agent

Give the Agent this directory and ask it to read the identity, visual signature, reproduction notes, prompts, palette, and evaluation file before compiling your subject, location, aspect ratio, and intended use. Ask it to check that the quiet distance is preserved rather than adding maps, models, or landmarks.

### Method 2: Copy the Prompt

Copy `prompts/base.txt`, replace `{SUBJECT}` and `{LOCATION}`, and submit `prompts/negative.txt` as the negative prompt. Use the visual signature and palette when you need tighter color control.

### Method 3: Configure an API key and submit

Configure your API key in your own image platform or compiler, then submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the base and negative prompts to a local model or ComfyUI workflow. Follow the reproduction notes for daylight, ordinary observation distance, stable midtones, and fine grain, then review with `evaluation.yaml`.

Model weights, API keys, and generated images remain under the user’s control. Use references to understand visual characteristics; do not copy a source photograph’s composition, person, text, trademark, or logo.
