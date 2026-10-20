# Berthe Morisot

[中文版](README.md)

![Berthe Morisot representative](gallery-16x9.jpg)

> **Category:** artist<br>
> **Domain:** painting<br>
> **Path:** `style-packages/artists/berthe-morisot`

## Overview

High-key color, quick open brushwork, softened edges, and shifting daylight let figures and surroundings mingle through light strokes. This package controls visual treatment only; your prompt determines the subject, setting, count, and purpose.

## Curatorial note

Morisot’s images can feel as if their light is still moving: contours need not close before a few strokes bring a form into view. Keep essential structure clear while letting selected edges dissolve into their surroundings.

## Package files

- `identity.yaml`: scope, subject policy, and exclusions
- `visual-signature.yaml`: traits that should remain stable across subjects
- `reproduction.yaml`: medium, materials, and construction order
- `prompts/base.txt`, `prompts/negative.txt`: base prompt and negative constraints
- `palette/palette.json`: color roles and values
- `evaluation.yaml`: post-generation checks
- `references/manifest.csv`, `provenance.yaml`: sources and rights boundaries

## Sources and rights

The reference manifest links to collection records from The Metropolitan Museum of Art and the National Gallery of Art for visual research. No Morisot artwork or collection photograph is included. The package abstracts observable brushwork, tonal range, and edge handling without reproducing a specific work, sitter, or composition. The gallery image and sample are newly generated scenes, not historical artworks.

## Use this package

Give the full directory to an image-capable agent, or read `prompts/base.txt` and replace `{SUBJECT}` and `{LOCATION}`. Submit `prompts/negative.txt` alongside it. After generation, use `evaluation.yaml` to review subject legibility, brushwork, light, and color. The rules can also be used with your own API or local-model workflow; this repository does not host an image service or API keys.

The representative image and sample are currently pending human review. Do not present them as works by Morisot or use them to reconstruct a specific painting in the reference list.

## New architecture: gesture-led brushwork and open edges (experimental)

[`art-direction.yaml`](art-direction.yaml) uses direction format 2.1.0 and lets strokes follow a figure's turn, the fall of cloth, and nearby forms. It keeps facial and hand anchors readable while selectively releasing contours. The visible-ground rule applies only when the caller declares `light-ground-open-margin-allowed`. The direction focuses on how marks describe movement, where edges stop, and how the canvas keeps breathing room. Monet's direction centers on a specified moment's weather and light-color conditions and mark-making by surface; Morisot's direction does not assume weather effects or landscape series.

```powershell
python tools/compile-style.py style-packages/artists/berthe-morisot --direction package --context open-brush-figure-painting --context light-ground-open-margin-allowed --subject "A person turning while holding a loose white scarf beside an open window" --output runs/style-v2/berthe-morisot-job.json
```

This direction remains experimental; same-subject comparisons and stability across subjects still need human review.
