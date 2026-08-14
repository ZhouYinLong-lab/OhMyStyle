# Paper-cut Puppet 2D Game Art

[中文说明](README.md)

![Paper-cut Puppet 2D Game Art representative image](gallery-16x9.jpg)

> **Category:** Game art  
> **Medium:** Cut paper and 2D puppet animation  
> **Directory:** `style-packages/game-art/paper-cut-puppet-game-art`

## Overview

This direction treats a game image as a set of paper layers that can be separated, moved, and recombined. Cut edges, joints, pasted shapes, ink lines, and layer shadows establish a shallow stage. Unlike a paper-craft diorama, the emphasis is not on a small 3D model but on the silhouette, rhythm, and animatability of a 2D scene.

## Curatorial note

Paper has an honest limitation: every layer must decide where it belongs, and every joint must remain readable. That limitation keeps the image from becoming a pile of decorative detail. First decide which layers the user's subject needs, then let shadows explain front and back. If every object becomes a thick model, the lightness of paper and the reading speed of 2D game art disappear.

## Subject independence

This package controls paper separation, cut edges, articulated forms, shallow stage depth, and 2D readability. It does not prescribe a puppet, theatre, child's room, war story, or specific character. The character and outdoor platform in the representative image are only benchmark subjects.

## Sources and rights

The research entry is the [official Cosmic Top Secret website](https://www.cosmictopsecretgame.com/). The repository does not bundle external game assets. The representative image is newly generated and anonymous, not a game screenshot and not an endorsement or collaboration.

## Use this package only

### Method 1: Give it to an image-capable Agent

Give this directory to an Agent. Ask it to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/`, `palette/palette.json`, and `evaluation.yaml`, then compile your subject, aspect ratio, and purpose. Review the paper layers, cut edges, joint structure, and 2D game readability after generation.

### Method 2: Copy the Prompt directly

Open `prompts/base.txt`, replace `{{SUBJECT}}`, `{{ASPECT_RATIO}}`, and `{{USE_CASE}}`, and submit `prompts/negative.txt` as well on platforms that support negative prompts.

### Method 3: Configure an API key and submit

Configure an API key in your own image service or compiler, then submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the prompts, palette, and reproduction notes to a local model or ComfyUI workflow. Use `evaluation.yaml` for review; do not treat the character or outdoor platform in the representative image as a default subject.
