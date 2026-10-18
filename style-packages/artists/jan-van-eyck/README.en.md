# Jan van Eyck

[中文版](README.md)

![Jan van Eyck representative](gallery-16x9.jpg)

> **Category:** artist
> **Domain:** painting
> **Path:** `style-packages/artists/jan-van-eyck`

## Overview

A reference-backed package for Jan van Eyck, built around microscopic oil detail, reflected light, and quiet interior symbolism.

This is an independently usable style package. It turns observable medium,
composition, lighting, color, surface, texture, and reproduction decisions into
executable guidance for new subjects. It is not intended to reproduce a specific
work.

## Curatorial note

Its strongest pull comes from “frontal space, reflective surfaces, transparent layers, and precise small details with quiet ritual weight”. The visual order remains clear without a fixed scene.

## Read before use

- `identity.yaml`: scope, subjects, and exclusions
- `visual-signature.yaml`: features that should survive a subject change
- `reproduction.yaml`: medium, materials, and construction order
- `prompts/base.txt`, `prompts/negative.txt`: prompt constraints
- `palette/palette.json`: color roles and values
- `evaluation.yaml`: post-generation checks
- `references/manifest.csv`, `provenance.yaml`: sources and rights boundaries

## New architecture: glazing and material-specific light (experimental)

[`art-direction.yaml`](art-direction.yaml) activates only for a user-requested oil-painted still life or close material study when `glazed-material-observation` is explicitly declared. It makes highlight shape, edge softness, selective translucent layers, and detail density inspectable for different materials under one light source. It does not add an interior, mirror, person, inscription, or symbolic object by default.

The defining focus is how each material receives the same light and how thin color layers add depth. This differs from Zurbarán's dark ground, strong side light, and isolated still life, and does not require Vermeer's geometric interior or window-lit composition. The Van Eyck direction focuses on subtle but distinct surface responses and selective detail across multiple objects.

```powershell
python tools/compile-style.py style-packages/artists/jan-van-eyck --direction package --context glazed-material-observation --subject "A small green glass bottle, a folded cream linen cloth, and a tarnished brass key on a pale wooden tabletop, softly lit by a nearby window"
```

[`comparisons/`](comparisons/) contains legacy and direction jobs, generation prompts, and sample images. In this pair, the direction result has narrower highlights on glass and brass, softer transitions on linen and wood, and more localized detail. The images were generated independently without a fixed random seed, so the difference is not guaranteed across models. The direction remains experimental pending visual review.

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


