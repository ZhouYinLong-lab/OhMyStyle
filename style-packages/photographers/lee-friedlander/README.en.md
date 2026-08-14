# Lee Friedlander

[中文说明](README.md)

![Lee Friedlander representative image](gallery-16x9.jpg)

> **Category:** Photographer  
> **Medium:** Photography  
> **Directory:** `style-packages/photographers/lee-friedlander`

## Overview

Lee Friedlander’s street photographs often place reflections, window frames, cables, shadows, and cropped figures in one frame. The density is not there to create spectacle; it makes the viewer repeatedly relocate between foreground and background. This package transfers that layered observation without fixing a city, storefront, car, or pedestrian.

## Curatorial note

The language refuses to tidy the frame too much. Occlusion is not a defect and reflection is not decoration; both keep the friction of looking at a real place. Use a limited number of layers so complexity comes from plausible space rather than collage.

## Subject independence

This package controls observation and photographic treatment, not the city, person, building, vehicle, or event. The representative image is only a benchmark for reflection, occlusion, and monochrome density.

## Source and rights

Research entry: [The Museum of Modern Art artist archive](https://www.moma.org/artists/2002-lee-friedlander). No external artwork is bundled. The representative image is a new anonymous scene and is not a reproduction, endorsement, or licensed collaboration.

## Use only this package

### Method 1: Give it to an image-capable Agent

Provide this directory and ask the Agent to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/`, `palette/palette.json`, and `evaluation.yaml`, then compile your subject and setting. Add reflection or occlusion only when the scene supports it.

### Method 2: Copy the prompt

Open `prompts/base.txt`, replace `{{SUBJECT}}`, `{{ASPECT_RATIO}}`, and `{{USE_CASE}}`, and submit `prompts/negative.txt` alongside it when supported.

### Method 3: Submit through your own API key

Configure the API key in your own image service or compiler and submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the prompt, palette, and reproduction notes to a local model or ComfyUI workflow, then review reflection, occlusion, subject preservation, and artifacts with `evaluation.yaml`.
