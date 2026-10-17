# American Luminism

[中文版](README.md)

![American Luminism representative](gallery-16x9.jpg)

> **Category:** art movement<br>
> **Domain:** painting<br>
> **Path:** `style-packages/movements/american-luminism`

## Overview

Sparse horizontal space, restrained edges, calm reflective planes, and precise atmospheric perspective capture natural light that feels clear and nearly still. The landscape in the demonstration is optional; the subject and setting in your prompt remain authoritative.

## Curatorial note

The calm of American Luminism comes from measured spatial layers and controlled reflected light, not from blurring the whole scene. Keep distance legible and let brushwork recede behind the light to distinguish it from Impressionist broken strokes and Romantic spectacle.

## Package files

- `identity.yaml`: scope, open subject policy, and exclusions
- `visual-signature.yaml`: traits that should remain stable across subjects
- `reproduction.yaml`: medium, materials, and construction order
- `prompts/base.txt`, `prompts/negative.txt`: base prompt and negative constraints
- `palette/palette.json`: color roles and values
- `evaluation.yaml`: post-generation checks
- `references/manifest.csv`, `provenance.yaml`: sources and rights boundaries

## Sources and rights

The references link to the National Gallery of Art's research catalogue and exhibition for *American Light: The Luminist Movement, 1850–1875*, and to a collection record from the Princeton University Art Museum. No source artwork is included. The visual rules emphasize sparse horizontal space, calm reflections, fine atmospheric perspective, and suppressed visible brushwork, separating the package from Romantic dramatic light and Impressionist stroke breakup.

## Use this package

Read `prompts/base.txt`, replace `{SUBJECT}` and `{LOCATION}`, and submit `prompts/negative.txt` alongside it. After generation, use `evaluation.yaml` to review subject adherence, spatial depth, reflected light, and surface control. The gallery and sample are newly generated and pending human review, not historical artworks.
