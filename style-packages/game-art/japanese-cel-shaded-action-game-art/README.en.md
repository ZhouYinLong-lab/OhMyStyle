# Japanese Cel-Shaded Action Game Art

[中文版](README.md)

![Japanese cel-shaded action game art representative image](gallery-16x9.jpg)

> **Category:** Game art  
> **Medium:** 2D painting language combined with real-time 3D rendering  
> **Directory:** style-packages/game-art/japanese-cel-shaded-action-game-art

## Overview

This package extracts a hybrid method common to modern action games: three-dimensional space carries volume, perspective, and occlusion, while a two-dimensional painting language carries contours, stepped values, and motion rhythm. It is neither a generic anime filter nor a model painted with a few flat colors.

## Curatorial note

What I like here is the treatment of momentum. Even without a fighting character, perspective, garment direction, contour work, and stepped shading keep the scene moving forward. Establish the subject and camera first, then decide which edges deserve a hand-drawn touch.

## Subject independence

This package controls cel shading, three-dimensional space, contours, value bands, and action energy. It does not prescribe a character, weapon, mech, place, or story. The courier and vehicle in the representative image are benchmark subjects only.

## Sources and rights

Research includes the [Arc System Works official work page](https://www.arcsystemworks.com/game/guilty-gear-strive/). No external game assets are bundled. The representative image is a new anonymous scene, not a frame from a specific game and not an endorsement or affiliation.

## Use only this package

### Method 1: Give the package to an image-capable Agent

Give the complete package directory to an Agent. Ask it to read identity.yaml, visual-signature.yaml, reproduction.yaml, prompts, palette/palette.json, and evaluation.yaml, then compile your subject, location, aspect ratio, and purpose into the generation task.

### Method 2: Copy the prompt

Copy prompts/base.txt, replace the subject, location, and aspect ratio, and submit prompts/negative.txt with it.

### Method 3: Configure an API key

Configure an API key in your own image service or compiler, then submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the prompt, palette, and reproduction notes to a local model or ComfyUI. Use evaluation.yaml to check value bands, three-dimensional volume, perspective, and subject leakage.
