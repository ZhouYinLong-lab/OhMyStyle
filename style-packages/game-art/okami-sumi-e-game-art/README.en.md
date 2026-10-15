# Ōkami Sumi-e Game Art

[中文版](README.md)

![Ōkami Sumi-e Game Art representative](gallery-16x9.jpg)

> **Category:** game_art  · **Domain:** game_art
> **Path:** style-packages/game-art/okami-sumi-e-game-art

## Overview

Calligraphic ink lines, tonal washes, paper texture, and a limited set of flat color areas define this game-art direction. Readable environmental layers and brush direction matter more than any specific character, level, mythic figure, or game interface.

## Curatorial note

This package treats ink wash as a way to build space, not merely as a paper-texture overlay. Lines of varying weight define contours and movement; diluted ink creates depth; small areas of color act like seals to draw attention. The user still chooses the subject, so the package does not automatically add wolves, shrines, or a specific game location.

## Subject independence

This package controls how an image is generated, not what it depicts. People, objects, places, architecture, plants, vehicles, and narrative come from the user's prompt. The representative image is only a demonstration and must not become a default subject.

## Visual signature

- Clearly separated foreground, middle ground, and background
- Ink black, blue-gray, and paper white form the structural palette
- graphic ink value separation with soft wash transitions and selective flat color accents
- fibrous paper grain, dry-brush edges, pooled ink, and visible brush direction

## Sources and rights

References are used for research and visual analysis. External artworks, photographs, game imagery, trademarks, and platform pages remain the property of their respective rights holders. The generated example is a new anonymous scene and is not an original work by, or endorsement from, the referenced source.

- [Official interview on the game’s ink-wash art direction](https://news.capcomusa.com/lets/browse/matsushita-san-answers-your-okamiden-questions)

See [provenance.yaml](provenance.yaml), [references/manifest.csv](references/manifest.csv), and the repository [NOTICE](../../../NOTICE) for redistribution boundaries.

## Use only this package

1. Give this directory to an image-capable Agent and ask it to read the YAML files, prompts, palette, and evaluation before compiling a prompt.
2. Copy prompts/base.txt, replace the subject and location, and send prompts/negative.txt as the negative prompt.
3. Submit the compiled prompt through your own API tool after configuring your own API key; this repository does not host generation.
4. Connect the prompt, palette, reproduction notes, and reference manifest to a local model or ComfyUI workflow.

Do not copy a source work's exact composition, figures, text, trademark, logo, game asset, or fixed subject. Users manage model weights, API keys, generated images, and storage themselves.
