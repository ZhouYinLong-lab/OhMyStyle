# Pierre Bonnard

[中文版](README.md)

![Pierre Bonnard representative image](gallery-16x9.jpg)

> **Category:** Artist  · **Domain:** painting
> **Path:** style-packages/artists/pierre-bonnard

## Overview

Organize intimate everyday scenes through color vibration, decorative planes, and shifting interior light, giving ordinary subjects a warmth like memory.

## Notes

This package transfers observable visual decisions to a user-supplied subject. It does not add a fixed object, place, character, landmark, or narrative event.

## Visual signature

- Decorative planes and gently compressed space
- Neighboring pink, ochre, warm green, and blue-violet hues in subtle vibration
- Light shifts gradually across objects, as if filtered through memory
- Visible, flexible brushwork and tactile fabric surfaces

## Subject independence

The package controls how an image is rendered, not what the user must render. The representative image is an anonymous demonstration. Keep the requested subject, count, location, and story unchanged.

## Sources and rights

Research sources are linked for attribution and study. External works, photographs, game images, trademarks, and platform pages remain with their respective rights holders. The generated demonstration is original and anonymous; it is not an original work by, nor an endorsement from, the cited source.

- [Pierre Bonnard artist profile](https://www.moma.org/artists/665-pierre-bonnard)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for the rights boundary.

## Use only this package

Choose one of the following methods based on the tools you have available.

### Method 1: Give the package to an image-capable Agent

Upload this package directory to an Agent, or provide its local path, and ask:

~~~
Use this style package to help me generate an image.

First read identity.yaml, visual-signature.yaml, reproduction.yaml,
prompts/base.txt, prompts/negative.txt, palette/palette.json, and evaluation.yaml.
Integrate the package rules into the workflow; do not rely on the style name alone or copy a reference work.

My image request is:
<subject, objects, scene, aspect ratio, and purpose>

Compile the full prompt first, then generate the image. After generation, check style features,
composition, color, material, AI artifacts, and request adherence against evaluation.yaml, and report remaining risks.
~~~

### Method 2: Copy the Prompt

Open [prompts/base.txt](prompts/base.txt), replace the subject, people, objects, scene, and aspect ratio, then submit [prompts/negative.txt](prompts/negative.txt) as a negative prompt to a text-to-image platform. For more consistent results, also consult the visual signature and palette.

### Method 3: Generate through your own API

Configure your API key in your own image platform or prompt compiler, then submit the base prompt, negative constraints, palette, and any required references. Keep the API key in your environment; this repository does not manage keys or host an image-generation service.

### Method 4: Local model + ComfyUI

Connect the prompts to a local model or ComfyUI workflow. Use the palette, reproduction notes, and reference manifest to guide color, composition, material, and lighting. Review the result against [evaluation.yaml](evaluation.yaml).

Users manage model weights, API keys, and generated images themselves. References are for observable traits only; do not copy a source work’s composition, figures, text, trademarks, or logos.

## Experimental direction: mirror as a second viewpoint

The optional [`art-direction.yaml`](art-direction.yaml) activates only when the user requests an interior or still life with a mirror. The frame crops a shifted reflected view of the same subject, letting reflection and direct view reorganize the room while preserving object count and identity. It does not add a mirror, person, or bathroom by default, and does not reproduce a source painting's mirror placement or figure arrangement. See [`comparisons/`](comparisons/README.md) for a vase still-life probe. This direction remains experimental.
