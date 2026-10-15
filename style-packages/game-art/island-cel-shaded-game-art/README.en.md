# Island Cel-Shaded Game Art

[中文](README.md)

![Island Cel-Shaded Game Art representative image](gallery-16x9.jpg)

> **Category:** game_art  · **Domain:** game_art
> **Directory:** style-packages/game-art/island-cel-shaded-game-art

## Overview

Clear cel shading, expressive but readable silhouettes, bright sea-and-sky colors, and painterly 3D surfaces create a buoyant, cohesive game world.

## Curatorial note

This direction treats 3D space like a clear, bright, painterly illustration: silhouettes stay readable, color blocks are bold, and coastlines, skies, and buildings retain light, graphic forms. The package captures cel shading and island color relationships without prescribing pirates, boats, characters, or a specific game map.

## Visual signature

- Clear foreground, middle ground, and background; readable game space; silhouettes, routes, and landmarks take priority over fine realistic texture; a buoyant rhythm balanced by large color shapes
- Sea blue, sky cyan, warm sand, and bright vegetation create a fresh palette; shadows lean toward color rather than pure black; accent colors mark interactive or focal areas without prescribing specific objects
- Bright natural daylight and soft but distinct cel-shaded shadows, without a dark photorealistic film grade
- Simplified, painterly 3D surfaces with crisp edges; color shapes and form distinguish materials

## Subject independence

This package controls how an image is rendered, not what must be rendered. The user’s people, objects, places, buildings, plants, vehicles, and narrative remain authoritative. The representative image is a demonstration, not a default subject. The package does not silently add a landmark, character, group, religious scene, game level, or story event.

## Files to read

- [identity.yaml](identity.yaml): scope and exclusions
- [visual-signature.yaml](visual-signature.yaml): transferable visual decisions
- [reproduction.yaml](reproduction.yaml): medium and construction sequence
- [prompts/base.txt](prompts/base.txt) and [prompts/negative.txt](prompts/negative.txt): prompt constraints
- [palette/palette.json](palette/palette.json): color roles
- [evaluation.yaml](evaluation.yaml): review criteria
- [references/manifest.csv](references/manifest.csv) and [provenance.yaml](provenance.yaml): source and rights boundary

## Source and rights

External artworks, photographs, trademarks, and platform pages remain the property of their respective rights holders. The generated example is an original anonymous scene and does not claim affiliation, authorization, endorsement, or exact imitation.

- [Nintendo: Iwata Asks: The Legend of Zelda: The Wind Waker HD](https://iwataasks.nintendo.com/interviews/wiiu/wind-waker/0/0/)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for the detailed boundary.

## Use this package only

Choose one of the following methods.

### 1. Give it to an image-capable Agent

Upload this directory or provide its local path, then ask the Agent to read the package files, compile the prompt, generate the image, and review it against [evaluation.yaml](evaluation.yaml).

### 2. Copy the prompt

Open [prompts/base.txt](prompts/base.txt), replace the subject and format, and submit it together with [prompts/negative.txt](prompts/negative.txt). Use the visual signature and palette when the model needs more guidance.

### 3. Submit through your own API key

Configure your provider or compiler with your own API key, then send the base prompt, negative constraints, palette, and relevant source manifest. The repository does not host a generation service or store credentials.

### 4. Local model and ComfyUI

Connect the prompts to your local model or ComfyUI workflow. Translate the palette, reproduction notes, and visual signature into nodes or conditioning, then review the result with [evaluation.yaml](evaluation.yaml).

Model weights, API keys, and generated images are managed by the user. References are for observable analysis; do not copy a source work’s exact composition, people, text, trademarks, or logos.
