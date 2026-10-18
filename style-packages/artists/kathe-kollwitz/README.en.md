# Käthe Kollwitz

[中文](README.md)

![Käthe Kollwitz representative image](gallery-16x9.jpg)

> **Category:** Artist  
> **Medium:** Black-and-white printmaking and charcoal drawing  
> **Directory:** style-packages/artists/kathe-kollwitz

## Overview

Käthe Kollwitz treated printmaking as a direct, weight-bearing visual language. Dense networks of lines, solid black masses, and a limited gray scale turn ordinary forms into clear structures with emotional pressure. This package extracts the relationship between line, value, and paper rather than prescribing a subject of suffering.

## Curatorial note

What I value here is the sense that fewer colors can make a form feel heavier. Start with the subject’s silhouette and center of gravity, then let line carry material and feeling. A grayscale filter alone is not enough; the important decisions are where black settles, where gray stops, and how the paper keeps the hand of the process visible.

## Subject independence

The package controls printmaking medium, value structure, line behavior, and paper texture. It does not prescribe a person, object, location, or story. The studio objects in the representative image are only a benchmark subject.

## Optional direction: compressed figure group

`art-direction.yaml` registers an experimental compositional direction for multi-figure scenes with a user-specified interaction or shared action. It gathers figure weight around that point of contact, uses black masses and selective paper-white cuts to clarify the action, and subordinates background detail. It does not infer kinship, grief, conflict, or political narrative. Explicitly declare `compressed-figure-group-print` when compiling this direction.

### Generated comparison using the same scene

Both images show two adults lifting one wooden crate together. The right image is a direction-guided edit of the left: the background is simplified into larger dark masses and the figures, crate, and arm gestures are more concentrated. The model still changes details, especially the crate and clothing marks, so this pair illustrates a direction difference rather than deterministic rendering.

| Legacy default path | New figure-group direction |
| --- | --- |
| ![Kollwitz legacy figure-group sample](comparisons/legacy.png) | ![Kollwitz figure-group direction sample](comparisons/direction.png) |

Compiled jobs: [`legacy-job.json`](comparisons/legacy-job.json), [`direction-job.json`](comparisons/direction-job.json). Generation prompts and review notes: [`generation-prompts.md`](comparisons/generation-prompts.md).

## Source and rights

Research begins with the [Museum of Modern Art Käthe Kollwitz archive](https://www.moma.org/collection/artists/3201). The repository does not bundle external artworks. The representative image is a new anonymous scene and is not a reproduction, endorsement, or collaboration.

## Use this package alone

### Method 1: Give it to an image-capable Agent

Give the complete package directory to an Agent. Ask it to read identity.yaml, visual-signature.yaml, reproduction.yaml, prompts/, palette/palette.json, and evaluation.yaml before compiling your subject, aspect ratio, and use case.

### Method 2: Copy the Prompt

Copy prompts/base.txt, replace the subject, location, and aspect ratio, and submit prompts/negative.txt as the negative prompt when supported.

### Method 3: Configure an API key

Configure your own image platform or compiler with its API key, then submit the base prompt, negative constraints, and palette. OhMyStyle does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Feed the prompt, palette, and reproduction notes into a local model or ComfyUI workflow. Use evaluation.yaml to review line structure, value range, subject legibility, and subject leakage.
