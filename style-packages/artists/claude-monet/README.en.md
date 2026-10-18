# Claude Monet

[中文](README.md)

![Claude Monet representative image](gallery-16x9.jpg)

> **Category:** Artists
> **Type:** artist
> **Directory:** `style-packages/artists/claude-monet`

## Overview

This independent style package turns public references and observable decisions in medium, composition, color, light, material, and texture into executable constraints for new subjects. It is not intended to copy a particular source work.

## Curatorial note

Get “transient light, atmospheric colour, broken touches, and the changing appearance of ordinary motifs” right first; leave the actual content to your prompt. The style can then travel to another subject.

## Style focus

A reference-backed landscape painting profile focused on transient light, atmospheric color, broken touches, and the changing appearance of ordinary motifs rather than heavy contour or expressive impasto.

See `visual-signature.yaml`, `reproduction.yaml`, `palette/palette.json`, and `evaluation.yaml` for the complete rules.

## New direction (experimental)

`art-direction.yaml` separates condition-specific light and color, adjacent color notes, selective atmospheric edges, surface-dependent marks, ordinary-motif composition, and a series-observation rule used only when the user requests multiple images. It focuses on how weather and light alter one observed moment; it is not a global pastel filter, uniform blur, or random stippling.

The distinction from the Sorolla direction is deliberate: Monet foregrounds weather- and time-dependent color, atmospheric distance, and adjacent color notes. Sorolla foregrounds a readable daylight direction, traceable bounce light, and clearer value grouping. Both can depict outdoor light, but they do not reduce to the same warm-bright or blue-violet filter.

The new rules are experimental and opt-in. Omitting `--direction` retains the package's original path:

```powershell
python tools/compile-style.py style-packages/artists/claude-monet --direction package --context daylight --subject "A small stone footbridge beside a quiet pond under cool, overcast autumn daylight; no lilies or people" --output runs/monet-v2-job.json
```

Image results have not been reviewed. Use `evaluation.yaml` to compare at least two weather or time conditions, and check that the package does not add water lilies, cathedrals, haystacks, or other fixed motifs without being asked.

## Reference sources

- [https://commons.wikimedia.org/wiki/File:Claude_Monet_-_The_Magpie_-_Google_Art_Project.jpg](https://commons.wikimedia.org/wiki/File:Claude_Monet_-_The_Magpie_-_Google_Art_Project.jpg)
- [https://www.nga.gov/artworks/52186-argenteuil](https://www.nga.gov/artworks/52186-argenteuil)
- [Musée d'Orsay: Monet and changing weather, time, and season](https://www.musee-orsay.fr/en/program/whats-on/exhibitions/presentation/lucas-arruda-quimporte-le-paysage)
- [Musée d'Orsay: Wind Effect, Series of Poplars](https://www.musee-orsay.fr/en/artworks/effet-de-vent-serie-des-peupliers-119429)
- [National Gallery of Art: Claude Monet](https://www.nga.gov/artists/1726-claude-monet)

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
- art-direction.yaml (if opting into the new rules)
- reproduction.yaml
- prompts/base.txt
- prompts/negative.txt
- palette/palette.json
- evaluation.yaml

Integrate the rules from these files into the generation process. Do not treat the style name as the whole Prompt, and do not copy a reference work. If using the new direction, apply its conditions and rejection criteria explicitly; the default path retains the original prompt content.

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
