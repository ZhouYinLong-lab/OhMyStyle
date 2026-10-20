# Vincent van Gogh

[中文](README.md)

![Vincent van Gogh representative image](gallery-16x9.jpg)

> **Category:** Artists
> **Type:** artist
> **Directory:** `style-packages/artists/vincent-van-gogh`

## Overview

This independent style package turns public references and observable decisions in medium, composition, color, light, material, and texture into executable constraints for new subjects. It is not intended to copy a particular source work.

## Curatorial note

Its strongest pull comes from “directional strokes, complementary colour, thick material paint, and motion carried through sky, ground, and form”. The visual order remains clear without a fixed scene.

## Style focus

A post-impressionist painting profile built from observed directional strokes, high-chroma complementary color, thick material paint, and expressive motion in sky, vegetation, and ground without copying a named composition.

See `visual-signature.yaml`, `reproduction.yaml`, `palette/palette.json`, and `evaluation.yaml` for the complete rules.

## Reference sources

- [https://commons.wikimedia.org/wiki/File:VanGogh-starry_night.jpg](https://commons.wikimedia.org/wiki/File:VanGogh-starry_night.jpg)
- [https://commons.wikimedia.org/wiki/File:Vincent_van_Gogh_-_Olive_Trees_-_Google_Art_Project.jpg](https://commons.wikimedia.org/wiki/File:Vincent_van_Gogh_-_Olive_Trees_-_Google_Art_Project.jpg)
- [https://www.moma.org/collection/works/79802?artist_id=2206&page=1&sov_referrer=artist](https://www.moma.org/collection/works/79802?artist_id=2206&page=1&sov_referrer=artist)

## Sources and rights

References are used for research and visual analysis. External artworks, photographs, game imagery, trademarks, and source pages remain with their respective rights holders. Generated examples are anonymous new scenes, not works by the referenced creator, and do not imply endorsement or authorization.

See [`provenance.yaml`](provenance.yaml), [`references/manifest.csv`](references/manifest.csv), and the repository [`NOTICE`](../../../NOTICE) for source and redistribution boundaries.

## Use only this package

Choose any one of the four methods below. They are alternatives, not steps that must all be completed.

### Method 1: Give the package to an image-capable Agent

Upload the entire style-package directory to an Agent that can generate images, or provide its local path, together with the following instruction:

```
Use this style package to help me generate an image.

First read:
- identity.yaml
- visual-signature.yaml
- reproduction.yaml
- prompts/base.txt
- prompts/negative.txt
- palette/palette.json
- evaluation.yaml

Integrate the rules from these files into the generation process. Do not treat the style name as the whole Prompt, and do not copy a reference work.

My generation request is:
<describe the subject, people, objects, scene, aspect ratio, and intended use>

First compile my request into a complete Prompt, then use your image-generation capability. After generating, check the result against evaluation.yaml for style characteristics, composition, color, material, AI artifacts, and Prompt adherence. If there are clear problems, explain them and make one targeted correction.
```

### Method 2: Copy the Prompt directly

Open `prompts/base.txt` and replace its subject, people, objects, scene, and aspect ratio with your own request. Submit the constraints in `prompts/negative.txt` as the negative Prompt on an image platform that supports text-to-image generation. For more consistent results, also consult `visual-signature.yaml` and `palette/palette.json`.

### Method 3: Configure your API key and submit a job

Configure your API key in the image platform or in your own Prompt compiler, then submit the base Prompt, negative constraints, palette, and any necessary references together. Keep the API key in your own environment. This repository does not store keys, host an online generation service, or promise free quota or compatibility with any particular provider.

### Method 4: Local model + ComfyUI

Connect `prompts/base.txt` and `prompts/negative.txt` to a local model or ComfyUI workflow. Use `palette/palette.json` for color targets, `references/manifest.csv` to choose references, and `reproduction.yaml` to constrain composition, materials, and lighting. Use `evaluation.yaml` for manual or automated review after generation.

Use references to understand observable characteristics. Do not copy a source work's exact composition, people, text, trademarks, or marks. Model weights, API keys, and generated images remain under your control.

## New architecture: directional strokes and impasto (experimental)

[`art-direction.yaml`](art-direction.yaml) uses direction format 2.1.0 and separates mark direction, local cool-warm color structure, and visible paint load into reviewable rules. Stroke families change with the surface instead of turning the whole image into one swirl; blue-yellow relationships follow the subject and light. Stars, cypresses, villages, and sunflowers are not automatic motifs. Callers can declare `close-view-of-painted-surface` only for close framing to activate extra checks on localized impasto edges. This direction remains experimental, and the legacy package prompt stays unchanged by default.

```powershell
python tools/compile-style.py style-packages/artists/vincent-van-gogh --direction package --subject "A wind-bent orchard after rain, with a figure walking along a path" --output runs/style-v2/van-gogh-job.json
```

Compilation does not call an image-generation service. Museum collection records support the observations about blue-yellow relationships, gestural marks, and thick paint. Transfer to new subjects and differentiation from neighboring artist packages still need image review.

## Legacy and direction comparison

See [the same-subject samples, compiled jobs, and review limitations](comparisons/README.md). This is a preliminary single-subject check; the direction remains experimental.
