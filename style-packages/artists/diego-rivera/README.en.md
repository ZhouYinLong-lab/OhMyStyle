# Diego Rivera

[中文版](README.md)

![Diego Rivera representative image](gallery-16x9.jpg)

> **Category:** Artist  · **Domain:** painting
> **Path:** style-packages/artists/diego-rivera

## Overview

Organize images through mural-scale structure, clear contours, flat color fields, and a sense of public space while keeping the user’s subject open.

## Notes

Rivera’s mural language is designed to read from a distance: forms are clear, group relationships are legible, and color fields work with architectural structure to shape public space. This package extracts those compositional decisions without automatically adding workers, revolution, Mexican landmarks, or historical events.

## Visual signature

- Large-scale forms designed to read from a distance
- Clear contours and flat color fields jointly define structure
- Earth red, ochre, blue-green, and charcoal organize the public-space palette
- Figures or objects form mural-like group rhythms without prescribing a subject

## Subject independence

This package controls visual treatment, not the user's subject, object count, location, or story. The representative image is an anonymous demonstration. It does not add a recurring landmark, character, prop, or narrative event.

## Sources and rights

Research sources are linked for study and attribution. External works, photographs, game materials, trademarks, and platform pages remain with their respective rights holders. The generated demonstration is original and anonymous, not a source artwork or endorsement.

- [Diego Rivera artist profile](https://www.moma.org/artists/4942-diego-rivera)

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

## New architecture: public narrative mural registers (experimental)

[`art-direction.yaml`](art-direction.yaml) uses direction format 2.1.0 and applies to user-requested public narrative murals. The register rule activates only with `multiple-requested-activities`; `people-tools-or-system-interaction` controls the shared-scale rule. A single action is not split into panels, and the direction does not default to workers, factories, Mexican symbols, or political emblems.

```powershell
python tools/compile-style.py style-packages/artists/diego-rivera --direction package --context public-narrative-mural --subject "A panoramic community greenhouse project: neighbors tend seedlings, builders repair its roof, and water channels feed the crops" --output runs/style-v2/diego-rivera-job.json
```

This direction remains experimental; same-subject comparisons and stability across subjects still need human review.
