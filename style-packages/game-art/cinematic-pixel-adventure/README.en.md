# Cinematic Pixel Adventure Art

[中文](README.md)

![Cinematic Pixel Adventure Art representative image](gallery-16x9.jpg)

> **Category:** game-art
> **Directory:** `style-packages/game-art/cinematic-pixel-adventure`

## Overview

This independent package turns public research and observable decisions about medium, composition, color, light, material, and texture into executable constraints for new subjects. It is not intended to copy a specific work.

## Style focus

Combines small readable sprites, broad skies, layered distance, and warm-cool environmental light for cinematic space; narrative use is optional and the direction also works for environments, still lifes, and backgrounds.

## Sources

- [《To the Moon》官方商店页面](https://store.steampowered.com/app/206440/To_the_Moon/)
- [《Impostor Factory》官方商店页面](https://store.steampowered.com/app/1182620/Impostor_Factory/)

## Rights and provenance

Sources are used for research and visual analysis. External works and hosted pages remain with their respective rights holders. The generated example is a new anonymous scene and does not imply affiliation or endorsement.

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
