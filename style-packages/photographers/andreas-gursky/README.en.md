# Andreas Gursky

[中文说明](README.md)

![Andreas Gursky representative image](gallery-16x9.jpg)

> **Category:** Photographer  
> **Medium:** Large-scale contemporary color photography  
> **Directory:** `style-packages/photographers/andreas-gursky`

## Overview

Andreas Gursky often pulls the viewing distance back so architecture, infrastructure, terrain, or crowds become a coherent system. Repeated modules, horizontal color bands, and readable local details coexist. This package transfers that sense of scale, information density, and color organization without turning warehouses, parking lots, or offices into default subjects.

## Curatorial note

What interests me here is the tension between an orderly distant view and the small traces that remain when the image is inspected closely. The subject does not need to become a single hero object; it can find its place inside a larger structure. Look for repetition, layering, or queues in the user's subject before choosing an elevated viewpoint. If those conditions are absent, keep the composition clear instead of forcing a grid.

## Subject independence

This package controls viewpoint, scale, repetition, color zoning, and photographic resolution. It does not prescribe a person, building, facility, location, or story. The logistics scene in the representative image is only a benchmark subject.

## Sources and rights

The research entry is the [Museum of Modern Art exhibition archive](https://www.moma.org/calendar/exhibitions/170). The repository does not bundle external artworks. The representative image is a newly generated anonymous scene, not a reproduction of a specific work and not an endorsement or collaboration.

## Use this package only

### Method 1: Give it to an image-capable Agent

Give this directory to an Agent. Ask it to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/`, `palette/palette.json`, and `evaluation.yaml`, then compile your subject, aspect ratio, and purpose. After generation, use the evaluation file to check subject independence, scale, and whether repetition supports the subject.

### Method 2: Copy the Prompt directly

Open `prompts/base.txt`, replace `{{SUBJECT}}`, `{{ASPECT_RATIO}}`, and `{{USE_CASE}}`, and submit `prompts/negative.txt` as well on platforms that support negative prompts.

### Method 3: Configure an API key and submit

Configure an API key in your own image service or compiler, then submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the prompts, palette, and reproduction notes to a local model or ComfyUI workflow. Use `evaluation.yaml` for review; do not treat the logistics scene in the representative image as a default subject.
