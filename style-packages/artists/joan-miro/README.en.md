# Joan Miró

[中文](README.md)

![Joan Miró representative image](gallery-16x9.jpg)

> **Category:** artists
> **Type:** artist
> **Path:** `style-packages/artists/joan-miro`

## Overview

This independent style package for **Joan Miró** turns public references and observable decisions about medium, composition, color, light, material, and texture into executable constraints. It is intended for new subjects, not for reproducing a specific artwork.

## Curatorial note

“biomorphic line, open ground, primary colour islands, and a light asymmetry that keeps the field alive” sets the viewing distance. People, objects, and places can change independently.

## Visual focus

生物形态线条、留白、原色岛屿与轻盈非对称. The prompt emphasizes these observable traits while requiring a new subject, arrangement, and object relationship.

See `visual-signature.yaml`, `reproduction.yaml`, `palette/palette.json`, and `evaluation.yaml` for the complete rule set.

## Reference sources

- [MoMA: Joan Miró](https://www.moma.org/artists/4016-joan-miro)
- [MoMA: Daphnis and Chloé](https://www.moma.org/collection/works/61026)

## New architecture: suspended biomorphic forms and open color field (experimental)

[`art-direction.yaml`](art-direction.yaml) uses direction format 2.1.0 and activates only for a user-requested abstract or stylized arrangement when `suspended-biomorphic-sign-field` is declared. Asymmetrical spacing and negative space are base rules; callers can add `user-requested-drawn-line-with-separate-abstract-forms` or `user-requested-limited-color-abstract-composition` to activate line-connection or local-color guidance as applicable. No stars, eyes, birds, people, letters, or moons are added by default.

This differs from af Klint's axis, spiral, and geometric-biomorphic structure, and from Mondrian's orthogonal grid. The Miró direction keeps a looser relationship among curved line, separate color forms, and open ground. MoMA's notes on Miró's sign language, curvilinear lines, and biomorphic forms provide formal context without copying any specific symbol or arrangement.

```powershell
python tools/compile-style.py style-packages/artists/joan-miro --direction package --context suspended-biomorphic-sign-field --subject "One black crescent, one red triangle, one cobalt-blue irregular oval, and one thin black curved line on a warm-white ground; keep all four marks distinct and leave generous open space"
```

[`comparisons/`](comparisons/) contains legacy and direction jobs, prompts, and sample images. With the legacy image as a composition reference, the direction result extends the curve into a clearer path beneath the color forms while keeping the shapes separate with open ground between them. Image generation remains stochastic; the direction is experimental pending visual review.

## Rights and attribution

Reference links are provided for research and visual analysis only. External artworks, photographs, game images, trademarks, and platform pages remain the property of their respective rights holders. This package does not redistribute protected source works. The representative image is a new anonymous generated scene, not an original work by the named artist, photographer, designer, or game, and does not imply endorsement or authorization.

See [`provenance.yaml`](provenance.yaml), [`references/manifest.csv`](references/manifest.csv), and the repository [`NOTICE`](../../../NOTICE) for boundaries.

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
