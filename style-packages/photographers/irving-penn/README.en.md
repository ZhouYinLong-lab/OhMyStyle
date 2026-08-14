# Irving Penn

[中文说明](README.md)

![Irving Penn representative image](gallery-16x9.jpg)

> **Category:** Photographer  
> **Medium:** Photography  
> **Directory:** `style-packages/photographers/irving-penn`

## Overview

Irving Penn often placed people, garments, or ordinary objects in highly controlled studio settings. Backgrounds stay quiet so that shape, material, shadow, and negative space carry the image. This package extracts that precise restraint without fixing a portrait, fashion item, paper object, or ceramic vessel.

## Curatorial note

The language feels like turning down every unnecessary sound until materials can speak for themselves. It is useful when an image needs refinement and order without relying on gold filters or expensive props. Shadow boundaries and spacing matter more than decoration.

## Subject independence

This package controls photographic treatment, not the person, object, place, garment, or story. The paper and vessel in the representative image are benchmark subjects only.

## Source and rights

Research entry: [The Museum of Modern Art artist archive](https://www.moma.org/artists/4548-irving-penn). No external artwork is bundled. The representative image is a new anonymous scene and is not a reproduction, endorsement, or licensed collaboration.

## Use only this package

### Method 1: Give it to an image-capable Agent

Provide this directory and ask the Agent to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/`, `palette/palette.json`, and `evaluation.yaml`, then compile your subject, aspect ratio, and use case. Ask it to review subject independence, materials, and artifacts.

### Method 2: Copy the prompt

Open `prompts/base.txt`, replace `{{SUBJECT}}`, `{{ASPECT_RATIO}}`, and `{{USE_CASE}}`, and submit `prompts/negative.txt` alongside it when supported.

### Method 3: Submit through your own API key

Configure the API key in your own image service or compiler and submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the prompt, palette, and reproduction notes to a local model or ComfyUI workflow, then review with `evaluation.yaml`. Do not treat the representative props as required subjects.
