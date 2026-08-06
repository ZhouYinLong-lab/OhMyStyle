# RPG Maker Pixel Art + Turner Atmosphere

[中文](README.md)

![RPG Maker Pixel Art + Turner Atmosphere example](gallery-16x9.jpg)

## What this is

A cross-style recipe is not an independent artist, photographer, or movement. It combines multiple packages by explicit responsibilities such as zone, medium, lighting, or palette. It does not turn several names into an undefined blended label.

## Composition mode

Current mode: `stack`

- `game-art/rpg-maker-pixel-art`: medium; Keep raster medium and sprite edges authoritative.
- `artists/jmw-turner`: lighting; Borrow atmospheric light logic without replacing pixel geometry.

## Mechanism

- `stack`: separate packages own separate dimensions, such as pixel medium and painted atmosphere.
- `blend`: weighted rules share a dimension while preserving the main structure.
- `contrast`: packages are assigned to separate zones so color, material, or texture rules do not contaminate one another.

See `composite.yaml` for constraints. Generated example:

![Cross-style example](examples/generated/anonymous-v1.png)

## Use only this package

1. Download this directory and read `composite.yaml` and the referenced base packages.
2. Open `prompts/base.txt`, replace the subject with your own idea, and use `prompts/negative.txt` for exclusions.
3. Choose one execution path: paste the Prompt into an image platform; configure your own API key and submit a compiled job; or import the Prompt, reference manifest, and palette into a local model or ComfyUI workflow.
4. Use references to understand observable decisions. Do not copy a source work's exact composition, people, text, trademarks, or marks.

Model weights, API keys, and generated images remain under the user's control; this repository is not an online image-generation service.
