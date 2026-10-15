# Beautiful Decay Survival Game Art

[中文版](README.md)

![Beautiful Decay Survival Game Art representative image](gallery-16x9.jpg)

> **Category:** Game art  · **Domain:** game_art
> **Path:** style-packages/game-art/last-of-us-cinematic-survival

## Overview

Natural light, vegetation reclaiming built environments, restrained blue-gray atmosphere, and grounded materials create a survival-game world where beauty and decay coexist.

## Notes

This package transfers observable visual decisions to a user-supplied subject. It does not add a fixed object, place, character, landmark, or narrative event.

## Visual signature

- Explorable spaces shaped by natural light
- Vegetation and built structures reveal layers of time
- Blue-gray atmosphere, damp surfaces, and selective warm accents
- Realistic materials and restrained cinematic framing

## Subject independence

The package controls how an image is rendered, not what the user must render. The representative image is an anonymous demonstration. Keep the requested subject, count, location, and story unchanged.

## Sources and rights

Research sources are linked for attribution and study. External works, photographs, game images, trademarks, and platform pages remain with their respective rights holders. The generated demonstration is original and anonymous; it is not an original work by, nor an endorsement from, the cited source.

- [Survival-game art direction reference](https://www.naughtydog.com/blog/celebrating_the_10th_anniversary_of_the_last_of_us)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for the rights boundary.

## Use only this package

Choose any one of the four methods that fits your tools; you do not need to use them all.

### Method 1: Give the package to an image-capable Agent

Upload the style package directory to an image-capable agent, or provide its local path, together with these instructions:

~~~
Use this style package to help me generate an image.

First read identity.yaml, visual-signature.yaml, reproduction.yaml,
prompts/base.txt, prompts/negative.txt, palette/palette.json, and evaluation.yaml in this directory.
Integrate the rules from those files into the generation workflow. Do not use only the style name as a prompt or copy a reference work.

My image requirements are:
<subject, objects, setting, aspect ratio, and purpose>

Compile the complete prompt before generating the image. Then use evaluation.yaml to review the style traits,
composition, color, materials, generative artifacts, and adherence to the request. Report any remaining risks.
~~~

### Method 2: Copy the Prompt

Open [prompts/base.txt](prompts/base.txt) and replace the subject, people, objects, setting, and aspect ratio. Submit [prompts/negative.txt](prompts/negative.txt) as a negative prompt on a text-to-image platform that supports it. For more consistent results, also consult the visual signature and palette.

### Method 3: Generate through your own API

Configure your API key in your own image-generation platform or prompt compiler, then submit the base prompt, negative constraints, palette, and any needed references. Keep your API key in your own environment; this repository does not store keys or host an online image-generation service.

### Method 4: Local model + ComfyUI

Add the base prompt and negative constraints to a local model or ComfyUI workflow. Use the palette, reproduction notes, and reference manifest to guide color, composition, materials, and lighting. Review the result manually or automatically with [evaluation.yaml](evaluation.yaml).

Users manage their own model weights, API keys, and generated images. Reference images are for understanding observable traits; do not copy a source work’s exact composition, people, text, trademarks, or logos.
