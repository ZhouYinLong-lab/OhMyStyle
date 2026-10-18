# Jean-Michel Basquiat

[中文](README.md)

![Jean-Michel Basquiat representative image](gallery-16x9.jpg)

> **Category:** Artist  
> **Medium:** Painting  
> **Directory:** `style-packages/artists/jean-michel-basquiat`

## Overview

This package extracts rough mixed-media surfaces, fractured forms, forceful hand-drawn lines, compressed space, and selective high-tension color blocks. It keeps the image visibly made by hand while allowing a user-supplied subject to remain legible.

## Curatorial note

The energy here does not come from one mandatory symbol. It comes from a surface that appears to be added to, scraped back, and reorganized in place. The representative image uses an abstract wall only to show that material tension: black marks gather the loose planes, while the worn ground keeps the structure open. Transfer the relationships between line, plane, and surface—not a fixed street, word, or icon.

## Subject independence

The package controls visual treatment, not the subject, location, objects, characters, or story. The abstract wall is only an example. Crowns, skulls, streets, and graffiti lettering are not default content. User instructions remain authoritative.

## Source and rights

The package refers to [the Museum of Modern Art artist record](https://www.moma.org/artists/370-jean-michel-basquiat) for research and extracts observable visual characteristics only. External works remain with their rights holders. The representative image is an original abstract scene, not a reproduction or endorsement. See [`provenance.yaml`](provenance.yaml), [`references/manifest.csv`](references/manifest.csv), and the root [`NOTICE`](../../../NOTICE).

## New architecture: user-authored text and mark hierarchy (experimental)

[`art-direction.yaml`](art-direction.yaml) activates only when the user supplies words or symbols for the image and declares `user-authored-mark-hierarchy`. It organizes those exact elements through scale, color, placement, and hand-drawn marks. Crossing out, circling, repeating, or obscuring applies only to elements the user designates. Without user input, add no text, crown, skull, anatomy diagram, signature, or cultural reference. MoMA and the Whitney document the interplay of text, color planes, and hand marks, and the use of crossing-out to draw attention; this direction transfers only those formal relationships, not source content or statements.

This is distinct from both a generic graffiti wall and a clean poster-typography grid: the user controls the content, while hand-drawn line, color planes, and localized intervention establish emphasis against visible ground and quiet gaps.

```powershell
python tools/compile-style.py style-packages/artists/jean-michel-basquiat --direction package --context user-authored-mark-hierarchy --subject "A small yellow portable radio with the exact handwritten words RADIO, SIGNAL, and QUIET; cross out only QUIET once; include one blue square and one red circle; no other text"
```

[`comparisons/`](comparisons/) contains legacy and direction jobs, prompts, and sample images. The direction sample uses the legacy image as a composition reference to inspect text hierarchy and localized strike-through. Image generation remains stochastic, so check the actual output for text accuracy. The direction remains experimental pending visual review.

## Use only this package

1. **Give it to an image-capable Agent:** provide this directory and ask the Agent to read the identity, visual signature, reproduction, prompts, palette, and evaluation files before compiling your subject-specific prompt.
2. **Copy the Prompt:** replace `{SUBJECT}` and `{LOCATION}` in `prompts/base.txt`, and submit `prompts/negative.txt` as the negative prompt.
3. **Use your own API key:** submit the base prompt, negative constraints, palette, and relevant references through your chosen service. This repository does not host keys or image generation.
4. **Use a local model + ComfyUI:** wire the prompts into your workflow, reproduce the line, color-plane, compressed-space, and surface rules, then review with `evaluation.yaml`.

Models, keys, and generated images remain under the user's control. References are for feature analysis, not copying.
