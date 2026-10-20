# Jean-Auguste-Dominique Ingres

[中文版](README.md)

![Jean-Auguste-Dominique Ingres representative image](gallery-16x9.jpg)

> **Category:** Artist  · **Domain:** painting
> **Path:** style-packages/artists/jean-auguste-dominique-ingres

## Overview

Build a composed neoclassical visual language through clear, supple contours, restrained value shifts, and idealized formal order.

## Notes

This package transfers observable visual decisions to a user-supplied subject. It does not add a fixed object, place, character, landmark, or narrative event.

## Visual signature

- Clear, continuous, and supple contour lines
- Idealized yet measured proportion and pose
- Restrained value modeling on smooth surfaces
- Calm light tones with a few dark structural accents

## Subject independence

The package controls how an image is rendered, not what the user must render. The representative image is an anonymous demonstration. Keep the requested subject, count, location, and story unchanged.

## New architecture: contour-led figure study (experimental)

[`art-direction.yaml`](art-direction.yaml) uses direction format 2.1.0 and activates only for a user-requested painted figure when `contour-led-figure-study` is declared. A supple outer contour establishes the pose; a few interior lines describe structure and folds; restrained value shifts add volume. The shallow-background rule applies only when the caller declares `quiet-background-permitted`. It does not automatically elongate the body, change body type or pose, or add classical costume, nudity, or allegory. The Musée d'Orsay's note on Ingres's *La Source* describes curved contours, simplified modeling, and shallow space; this direction uses those observable formal relationships without copying the figure or pose.

This differs from Delacroix's color conflict and action-driven brushwork: contour and pose should read first, with marks and shadows kept controlled. It also differs from Van Eyck's material-reflection rules; this direction handles figure edges and economical volume.

```powershell
python tools/compile-style.py style-packages/artists/jean-auguste-dominique-ingres --direction package --context contour-led-figure-study --subject "An adult seated sideways on a simple wooden chair, wearing a long rust-red coat, one hand resting on a closed blue book, against a pale quiet wall"
```

[`comparisons/`](comparisons/) contains same-subject legacy and direction jobs, prompts, and sample images. The direction image uses the legacy image as a composition reference, keeping the figure, pose, clothing, and object positions aligned so contour and value rules are easier to inspect. Image generation remains stochastic, so this does not guarantee the same result across models. The direction remains experimental pending visual review.

## Sources and rights

Research sources are linked for attribution and study. External works, photographs, game images, trademarks, and platform pages remain with their respective rights holders. The generated demonstration is original and anonymous; it is not an original work by, nor an endorsement from, the cited source.

- [Jean-Auguste-Dominique Ingres collection record](https://www.metmuseum.org/fr/art/collection/search/337364)

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
