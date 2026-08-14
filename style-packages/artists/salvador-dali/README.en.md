# Salvador Dalí

[中文说明](README.md)

![Salvador Dalí representative image](gallery-16x9.jpg)

> **Category:** Artist  
> **Medium:** Painting  
> **Directory:** `style-packages/artists/salvador-dali`

## Overview

Salvador Dalí often placed an almost exacting realistic surface inside relationships that do not fully obey ordinary reality. The disruption may come from scale, shadow, connection, or time rather than a pile of strange objects. This package transfers that lucid strangeness without fixing melting clocks, deserts, animals, or portraits.

## Curatorial note

The useful tension is that everything is easy to see but not fully explainable. The quieter the scene, the stronger a local impossibility becomes. Change one or two relationships and let the ordinary subject stay intact; if every corner transforms, the dream becomes decoration.

## Subject independence

This package controls visual treatment, not the person, object, place, building, or story. The courtyard and transformed forms in the representative image are benchmark subjects only.

## Source and rights

Research entry: [The Museum of Modern Art artist archive](https://www.moma.org/artists/1364-salvador-dali). No external artwork is bundled. The representative image is a new anonymous scene and is not a reproduction, endorsement, or licensed collaboration.

## Use only this package

### Method 1: Give it to an image-capable Agent

Provide this directory and ask the Agent to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/`, `palette/palette.json`, and `evaluation.yaml`, then compile your subject, setting, aspect ratio, and use case. Ask it to keep the anomalous relation limited and subject-serving.

### Method 2: Copy the prompt

Open `prompts/base.txt`, replace `{{SUBJECT}}`, `{{ASPECT_RATIO}}`, and `{{USE_CASE}}`, and submit `prompts/negative.txt` alongside it when supported.

### Method 3: Submit through your own API key

Configure the API key in your own image service or compiler and submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the prompt, palette, and reproduction notes to a local model or ComfyUI workflow, then review realism, anomaly, subject preservation, and artifacts with `evaluation.yaml`.
