# Piet Mondrian

[中文说明](README.md)

![Piet Mondrian representative image](gallery-16x9.jpg)

> **Category:** Artist  
> **Medium:** Painting  
> **Directory:** `style-packages/artists/piet-mondrian`

## Overview

Piet Mondrian’s visual language gives equal importance to line, plane, empty space, and a small set of high-clarity colors. The point is not to add a few colored squares, but to balance asymmetrical spacing, line weight, and color area. This package extracts those transferable relationships without fixing the user’s subject.

## Curatorial note

Its quiet tension is what makes the language useful: every line and color plane redistributes weight while the image remains calm. Keep that structural breathing room instead of copying a familiar rectangle arrangement.

## Subject independence

This package controls visual treatment, not the person, object, place, building, or story. The abstract representative image demonstrates the grid and color logic only; your prompt remains authoritative.

## Source and rights

Research entry: [The Museum of Modern Art artist archive](https://www.moma.org/artists/4057-piet-mondrian). No external artwork is bundled. The representative image is a new anonymous composition and is not a reproduction, endorsement, or licensed collaboration.

## Use only this package

### Method 1: Give it to an image-capable Agent

Provide this directory to the Agent and ask it to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/`, `palette/palette.json`, and `evaluation.yaml`, then compile your subject, aspect ratio, and use case into a complete prompt. Ask it to review the result against the evaluation file.

### Method 2: Copy the prompt

Open `prompts/base.txt`, replace `{{SUBJECT}}`, `{{ASPECT_RATIO}}`, and `{{USE_CASE}}`, and submit `prompts/negative.txt` alongside it when supported.

### Method 3: Submit through your own API key

Configure the API key in your own image service or compiler and submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the prompt, palette, and reproduction notes to a local model or ComfyUI workflow, then review the result with `evaluation.yaml`. Do not treat the representative image’s exact rectangle placement as a required composition.
