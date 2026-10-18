# Stereoscopic Photography

[中文版](README.md)

![Stereoscopic Photography representative image](gallery-16x9.jpg)

> **Category:** Technique and media  · **Domain:** photography
> **Path:** style-packages/techniques/stereoscopic-photography

## Overview

Recreate early stereoscopic viewing with paired images from slightly different viewpoints, card-like presentation, and visible parallax.

## Notes

Stereoscopic photography is not a “vintage filter”; its spatial illusion comes from presenting two slightly different viewpoints together. This package controls the paired format, parallax, and viewing logic without adding tourist landmarks, historical figures, or period narratives.

## Visual signature

- Paired left-right views in a clear card-like layout
- Spatial depth created by slight horizontal parallax
- Restrained tones of silver prints or hand coloring
- Comparable details that differ subtly between the two views

## Subject independence

This package controls visual treatment, not the user's subject, object count, location, or story. The representative image is an anonymous demonstration. It does not add a recurring landmark, character, prop, or narrative event.

## Sources and rights

Research sources are linked for study and attribution. External works, photographs, game materials, trademarks, and platform pages remain with their respective rights holders. The generated demonstration is original and anonymous, not a source artwork or endorsement.

- [Stereoscopic photography and photographic processes](https://www.vam.ac.uk/info/collection-selection-boxes-photography-processes-and-techniques)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE).

## Use only this package

Choose one of the following methods based on the tools you have available.

### Method 1: Give the package to an image-capable Agent

Upload this package directory to an Agent, or provide its local path, and ask:

~~~
Use this style package to help me generate an image.
First read identity.yaml, visual-signature.yaml, reproduction.yaml, prompts/base.txt,
prompts/negative.txt, palette/palette.json, and evaluation.yaml.
Integrate the package rules into the workflow; do not rely on the style name alone or copy a reference work.
My image request is:<subject, objects, scene, aspect ratio, and purpose>
Compile the full prompt first, then generate the image. After generation, check style features,
composition, color, material, AI artifacts, and request adherence against evaluation.yaml, and report remaining risks.
~~~

### Method 2: Copy the Prompt

Open [prompts/base.txt](prompts/base.txt), replace the subject, people, objects, scene, and aspect ratio, then submit [prompts/negative.txt](prompts/negative.txt) as a negative prompt to a text-to-image platform.

### Method 3: Generate through your own API

Configure your API key in your own image platform or prompt compiler, then submit the base prompt, negative constraints, palette, and any required references. This repository does not manage keys or host an image-generation service.

### Method 4: Local model + ComfyUI

Connect the prompts to a local model or ComfyUI workflow. Use the palette, reproduction notes, and reference manifest to guide color, composition, material, and lighting. Review the result against [evaluation.yaml](evaluation.yaml).

Users manage model weights, API keys, and generated images themselves. References are for observable traits only; do not copy a source work’s composition, figures, text, trademarks, or logos.
