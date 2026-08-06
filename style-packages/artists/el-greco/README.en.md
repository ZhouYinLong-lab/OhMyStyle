# El Greco

[中文](README.md)

![El Greco representative image](gallery-16x9.jpg)

> **Category:** artists
> **Type:** artist
> **Path:** `style-packages/artists/el-greco`

## Overview

This independent style package for **El Greco** turns public references and observable decisions about medium, composition, color, light, material, and texture into executable constraints. It is intended for new subjects, not for reproducing a specific artwork.

## Visual focus

拉长形体、垂直升腾、冷色灵光与压缩空间. The prompt emphasizes these observable traits while requiring a new subject, arrangement, and object relationship.

See `visual-signature.yaml`, `reproduction.yaml`, `palette/palette.json`, and `evaluation.yaml` for the complete rule set.

## Reference source

- [El Greco / 晚期文艺复兴](https://commons.wikimedia.org/w/index.php?search=El+Greco+paintings&title=Special:MediaSearch&type=image)

## Rights and attribution

Reference links are provided for research and visual analysis only. External artworks, photographs, game images, trademarks, and platform pages remain the property of their respective rights holders. This package does not redistribute protected source works. The representative image is a new anonymous generated scene, not an original work by the named artist, photographer, designer, or game, and does not imply endorsement or authorization.

See [`provenance.yaml`](provenance.yaml), [`references/manifest.csv`](references/manifest.csv), and the repository [`NOTICE`](../../../NOTICE) for boundaries.

## Use this package only

1. Download this directory and read `identity.yaml`, `visual-signature.yaml`, and `reproduction.yaml`.
2. Open `prompts/base.txt` and replace the subject with your own; negative constraints are in `prompts/negative.txt`.
3. Choose an execution route: paste the prompt into an image service; configure your own API key and submit it to a prompt compiler; or import the prompt, references, and palette into a local model and ComfyUI.
4. Use references to understand observable traits only. Do not copy a source work's exact composition, people, text, trademark, or logo.

Model weights, API keys, and generated images are managed by the user; this repository does not host an online image-generation service.
