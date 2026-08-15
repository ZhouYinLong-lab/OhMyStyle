# Salted Paper Printing

[中文版](README.md)

![Salted Paper Printing representative](gallery-16x9.jpg)

> **Category:** technique
> **Domain:** photography
> **Path:** style-packages/techniques/salted-paper-printing

## Overview

Visible paper fibers, a matte surface, warm brown tones, and contact-print gray scale define an early photographic paper process.

This is an independently usable style package. It extracts observable visual language for new user-supplied subjects; objects, places, people, and stories in the representative image are not default requirements.

## Curatorial note

Salted paper printing does not merely tint a photograph brown; the paper participates in the image. Keep a faded warmth while preserving subject and tonal scale. Scratches, borders, and period props are not substitutes for the process.

## Subject independence

This package controls how an image is generated, not what it depicts. The user's people, objects, places, architecture, plants, vehicles, and narrative remain authoritative. The representative image demonstrates visual treatment only.

## Sources and rights

References are used for research and visual analysis. External artworks, photographs, game imagery, trademarks, and platform pages remain the property of their respective rights holders. The generated example is a new anonymous scene and is not an original work by, or an endorsement from, the referenced artist, movement, technique, or game.

See provenance.yaml and references/manifest.csv for source boundaries.

## Use only this package

### Method 1: Give the package to an image-capable Agent

Give this directory to an Agent and ask it to read identity.yaml, visual-signature.yaml, reproduction.yaml, prompts/base.txt, prompts/negative.txt, palette/palette.json, and evaluation.yaml before compiling your subject, location, aspect ratio, and purpose into a full prompt. Ask it to check the result against evaluation.yaml and never copy a reference work.

### Method 2: Copy the prompts

Open prompts/base.txt, replace the subject, location, and aspect-ratio requirement, then send prompts/negative.txt with it when the image service supports negative prompts.

### Method 3: Configure an API key and submit

Use your own image platform or compiler. Submit the base prompt, negative constraints, palette, and reference manifest together. You manage keys and generated images; this repository does not host an image service.

### Method 4: Local model and ComfyUI

Connect the base prompt and negative constraints to a local model or ComfyUI workflow. Use visual-signature.yaml, reproduction.yaml, and palette/palette.json to set visual parameters, then review the output with evaluation.yaml.
