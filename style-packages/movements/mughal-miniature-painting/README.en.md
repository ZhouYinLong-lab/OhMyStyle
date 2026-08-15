# Mughal Miniature Painting

[中文版](README.md)

![Mughal Miniature Painting representative image](gallery-16x9.jpg)

> **Category:** Movement and historical period　**Medium:** Opaque watercolor and ink on paper　**Directory:** `style-packages/movements/mughal-miniature-painting`

## Overview

Mughal miniature painting combines precise contours, paper-based color, layered shallow space, and close observation of the natural world. It can hold a great deal of detail while keeping the boundary, scale, and breathing room of each layer under control. This package studies the paper, mark-making, and spatial organization rather than treating court narratives as requirements.

## Curatorial note

Its order does not come from emptiness; it comes from giving every small area a place. I like to establish a border and a few planes first, then concentrate detail in selected zones. The result has hand-worked density without becoming uniformly crowded.

## Subject independence

This package controls paper medium, contour, layered space, palette, and detail density. Palaces, emperors, hunts, gardens, animals, and writing are not defaults.

## File guide

- `identity.yaml`: source, scope, and subject boundaries
- `visual-signature.yaml`: contour, space, palette, and detail hierarchy
- `reproduction.yaml`: construction order from border to local detail
- `prompts/`: base prompt and negative constraints
- `palette/palette.json`: color roles
- `evaluation.yaml`: subject-independence and signature checks
- `references/manifest.csv`, `provenance.yaml`: source and rights boundaries

## Sources and rights

The package studies observable paper, contour, and miniature-painting methods in [The Metropolitan Museum of Art’s Shah Jahan Album essay](https://www.metmuseum.org/essays/the-shah-jahan-album) and its [discussion of royal-hunt paintings](https://www.metmuseum.org/zh/perspectives/depicting-the-royal-hunt). Collection works remain with their rights holders. The representative image is a new anonymous scene, not a copied folio or endorsement.

## Use only this package

### Method 1: Give it to an image-capable Agent

Give the Agent this directory and ask it to read the identity, visual signature, reproduction notes, prompts, palette, and evaluation file before compiling your subject, location, aspect ratio, and intended use. Tell it not to treat palaces, royalty, hunts, gardens, or writing as defaults.

### Method 2: Copy the Prompt

Copy `prompts/base.txt`, replace `{SUBJECT}` and `{LOCATION}`, and submit `prompts/negative.txt` as the negative prompt. Use the visual signature and palette for tighter paper and detail control.

### Method 3: Configure an API key and submit

Configure your API key in your own image platform or compiler, then submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the base and negative prompts to a local model or ComfyUI workflow. Follow the reproduction notes for paper, contour, shallow space, and localized detail, then review with `evaluation.yaml`.

Model weights, API keys, and generated images remain under the user’s control. Use references to understand visual characteristics; do not copy a source folio’s composition, person, text, trademark, or logo.
