# Albumen Printing

[中文](README.md)

![Albumen Printing representative image](gallery-16x9.jpg)

> **Category:** Technique and medium
> **Domain:** printmaking

## Overview

This package translates observable visual decisions associated with Albumen Printing into reusable generation rules. It is designed for new subjects, not for copying a specific source work.

## Curatorial note

The appeal of albumen printing is not把照片做旧，而在于它让细节落在一层薄而有光泽的表面上：高光温和，暗部带褐色，纸张和银盐共同决定了画面的呼吸。它适合迁移到新的主体，不要求每次都出现旧肖像或历史建筑。

## Subject independence

This package decides how to render, not what to render. The user's people, objects, places, buildings, plants, vehicles, and narrative remain authoritative. Motifs in the source discussion are optional research cues, not default subjects.

## Files to read first

- `identity.yaml`: scope and exclusions
- `visual-signature.yaml`: visual rules that should survive a subject change
- `reproduction.yaml`: medium, materials, and build order
- `prompts/base.txt` and `prompts/negative.txt`: generation constraints
- `palette/palette.json`: color roles
- `evaluation.yaml`: review criteria
- `references/manifest.csv` and `provenance.yaml`: source and rights boundary

## Source and rights

The source link is recorded for research and analysis. External artworks, photographs, games, trademarks, and platform pages remain with their respective rightsholders. The representative image is a new anonymous scene and is not an original work of the referenced artist, movement, technique, or game.

See `provenance.yaml`, `references/manifest.csv`, and the repository root `NOTICE` for the detailed boundary.

## Use only this package

Choose one of the four methods below. They use the same package rules and do not require the methods to be combined.

### Method 1: give it to an image-capable Agent

Upload this package directory to an image-capable Agent, or give it the local path, then ask it to read the structured files before generating.

~~~text
Please use this style package. Read identity.yaml, visual-signature.yaml, reproduction.yaml, prompts/base.txt, prompts/negative.txt, palette/palette.json, and evaluation.yaml first. Keep my subject and do not copy any reference work. My generation request is: <subject, scene, aspect ratio, and purpose>. Compile the prompt, generate the image, then review it against evaluation.yaml.
~~~

### Method 2: copy the prompts

Open `prompts/base.txt`, replace the subject and scene, and submit it together with `prompts/negative.txt` to a text-to-image platform.

### Method 3: configure an API key

Configure the API key in your own image platform or compiler, then submit the base prompt, negative constraints, palette, and any required references. This repository does not store keys or host a generation service.

### Method 4: local model + ComfyUI

Connect the prompts and palette to a local model or ComfyUI workflow. Use `evaluation.yaml` to review subject preservation, style signature, and unwanted artifacts.

Model weights, API keys, and generated images are managed by the user.
