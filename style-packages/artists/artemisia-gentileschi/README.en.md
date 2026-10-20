# Artemisia Gentileschi

[中文版](README.md)

![Artemisia Gentileschi representative](gallery-16x9.jpg)

> **Category:** artist
> **Domain:** painting
> **Path:** `style-packages/artists/artemisia-gentileschi`

## Overview

A reference-backed package for Artemisia Gentileschi, built around dramatic tenebrism, forceful diagonals, and physical narrative energy.

This is an independently usable style package. It turns observable medium,
composition, lighting, color, surface, texture, and reproduction decisions into
executable guidance for new subjects. It is not intended to reproduce a specific
work.

## Curatorial note

“close action, strong diagonals, sculptural bodies, and a dark field punctuated by warm colour” is the useful entry point: it arranges the image’s breathing room before the subject arrives.

## Read before use

- `identity.yaml`: scope, subjects, and exclusions
- `visual-signature.yaml`: features that should survive a subject change
- `reproduction.yaml`: medium, materials, and construction order
- `prompts/base.txt`, `prompts/negative.txt`: prompt constraints
- `palette/palette.json`: color roles and values
- `evaluation.yaml`: post-generation checks
- `references/manifest.csv`, `provenance.yaml`: sources and rights boundaries

## Sources and rights

References are used for research and visual analysis. External artworks,
photographs, game imagery, trademarks, and platform pages remain the property of
their respective rights holders. Generated examples are new anonymous scenes and
are not original works by, or endorsements from, the referenced person, movement,
school, or game.

See [`provenance.yaml`](provenance.yaml),
[`references/manifest.csv`](references/manifest.csv), and the repository
[`NOTICE`](../../../NOTICE) for source and redistribution boundaries.

## Use only this package

Choose one of the following methods.

### Method 1: Give the package to an image-capable Agent

Upload this package directory to an Agent, or provide its local path, and ask:

```text
Use this style package to help me generate an image.

First read identity.yaml, visual-signature.yaml, reproduction.yaml,
prompts/base.txt, prompts/negative.txt, palette/palette.json, and evaluation.yaml.
Compile their rules into the generation process. Do not use only the style name
as a prompt and do not copy a reference work.

My image request is:
<subject, objects, scene, aspect ratio, and purpose>

Compile the full prompt first, then generate the image. After generation, check
style features, composition, color, material, AI artifacts, and request adherence
against evaluation.yaml, and report remaining risks.
```

### Method 2: Copy the prompts

Replace the subject, objects, scene, and aspect ratio in `prompts/base.txt` and
send `prompts/negative.txt` as the negative prompt. Use the visual signature and
palette for tighter control.

### Method 3: Submit through your own API tool

Configure your API key in your own image platform or prompt compiler, then submit
the base prompt, negative constraints, palette, and any required reference list.
The repository does not host a generation service or manage API keys.

### Method 4: Local model + ComfyUI

Connect the prompts to a local model or ComfyUI workflow. Use the palette,
reproduction notes, and reference manifest to set color, composition, material,
and lighting. Review the output against `evaluation.yaml`.

Users manage model weights, API keys, and generated images themselves. References
are for observable traits only; do not copy a source work's exact composition,
figures, text, trademark, or logo.

## New architecture: embodied action and diagonal composition (experimental)

`art-direction.yaml` uses direction format 2.1.0 and applies to user-requested figure actions. It uses body, arm, and object directions to make the action immediate and legible, while preserving local form and color in shadow. The counter-diagonal rule activates only when the caller declares `opposing-force-action`, so ordinary gestures are not forced into a resistance pattern. It does not default to a woman protagonist, violence, a religious story, or a famous pose. Unlike the Caravaggio direction's single strong light and tactile surface, this direction prioritizes action lines and the space needed to read the gesture.

```powershell
python tools/compile-style.py style-packages/artists/artemisia-gentileschi --direction package --context figure-action --context opposing-force-action --subject "A person catching a brass pot before it falls in a dim kitchen" --output runs/style-v2/artemisia-gentileschi-job.json
```

This direction remains experimental; generated comparisons and stability across subjects still need human review.

## Legacy and direction comparison

See [the same-subject samples, compiled jobs, and review limitations](comparisons/README.md). This is a preliminary single-subject check; the direction remains experimental.
