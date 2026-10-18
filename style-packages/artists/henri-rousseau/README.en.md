# Henri Rousseau

[中文版](README.md)

![Henri Rousseau representative image](gallery-16x9.jpg)

> **Category:** artist
> **Domain:** painting
> **Path:** `style-packages/artists/henri-rousseau`

## Overview

This package extracts a lucid decorative order: flattened layers, crisp contour,
even illumination, vivid local color, and repeated botanical or structural shapes.
It does not make a tropical jungle the default subject.

## Curatorial note

The space does not rush toward distant realism. Leaves, walls, and sky stay on the
picture plane and relate through shape and color. That makes the package useful for
reorganizing an ordinary place into something calm, clear, and slightly strange,
without adding animals or an adventure plot.

## Subject independence

This package controls visual treatment, not subject matter. The greenhouse in the
representative image is a benchmark for layers, contour, and rhythm. Your prompt
still defines the people, objects, architecture, place, and story.

## Sources and rights

The Museum of Modern Art artist page is used as a research source. External works,
photographs, trademarks, and web content remain with their rights holders. This
repository stores a source link and an original generated demonstration only.

## New architecture: flat space and crisp natural detail (experimental)

[`art-direction.yaml`](art-direction.yaml) applies only when `flat-space-natural-detail` is explicitly declared. It translates Rousseau's direction into clear continuous contours, bounded color areas, overlapping but not fully naturalistic depth, and even diffuse light. Detailed natural forms appear only when the user requests a natural subject; the direction does not add a jungle, plants, animals, or adventure narrative by default.

This differs from Matisse's composition through cut-paper color shapes and positive-negative space, and from Moreau's fine curves, jewel-like color planes, and mysterious detail. Rousseau's direction emphasizes stable planar layers, defined forms, and even illumination; any slight spatial strangeness must preserve the requested subject count and layout.

```powershell
python tools/compile-style.py style-packages/artists/henri-rousseau --direction package --context flat-space-natural-detail --subject "One red watering can on an empty garden path"
```

[`comparisons/`](comparisons/) holds the compiled legacy and new-direction jobs, generation prompts, and sample images. Visual review is pending, so this direction remains experimental.

## Use only this package

1. Give the directory to an image-capable Agent and ask it to read the YAML files,
   prompts, palette, and evaluation before compiling your subject.
2. Copy `prompts/base.txt`, replace the subject, location, and aspect ratio, and
   use `prompts/negative.txt` when supported.
3. Submit the prompt, constraints, and palette through your own API tool after
   configuring your own key; this repository does not host generation.
4. Connect the package to a local model or ComfyUI workflow and review the output
   against `evaluation.yaml`.
