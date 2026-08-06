# Quiet Documentary

[中文](README.md)

## Overview

Quiet Documentary is a photography style package for ordinary interiors,
people, and still life. It favors soft available light, low saturation, modest
contrast, observational distance, and enough visual breathing room for the
scene to feel lived-in rather than commercially staged.

## Core features

- soft natural or window light;
- low saturation with slightly cool neutrals;
- medium shots and environmental portraits;
- asymmetry and intentional negative space;
- moderate depth of field and subtle grain;
- natural skin, surfaces, and small imperfections.

## Suitable subjects

People in daily life, quiet interiors, personal workspaces, modest still lifes,
neighborhood scenes, and objects with visible signs of use.

## Not part of this style

Hard flash, oversaturated color, plastic skin, extreme bokeh, aggressive HDR,
centered product advertising, and dramatic cinematic rim lighting.

## Reproduction workflow

1. Read [`style.yaml`](style.yaml) for the machine-readable identity.
2. Use [`technique/parameters.yaml`](technique/parameters.yaml) as a starting
   direction, not a fixed camera recipe.
3. Start from [`prompts/base.txt`](prompts/base.txt) and add a variation.
4. Compare the result against the accepted and rejected example criteria.
5. Record every reference asset in [`metadata/sources.csv`](metadata/sources.csv)
   before adding it to the package.

## Evidence status

This initial package commits criteria and metadata only. External reference
images are not distributed with the package; the files in `references/` and
`examples/` describe the requirements for future additions.

## License

The package documentation and original metadata are covered by the repository
license. External references and examples must keep their own license and
attribution information as recorded in [`provenance.yaml`](provenance.yaml).

## Use only this package

1. Download this directory and read `style.yaml`, `visual-signature.yaml`, and
   `reproduction.yaml`.
2. Open `prompts/base.txt`, replace the subject variables, and consult
   `prompts/negative.txt` for exclusions.
3. Paste the Prompt into an image-generation service, configure your own API
   key and submit it, or import the Prompt, reference manifest, and palette
   into a local model or ComfyUI workflow.
4. Model weights, API keys, and generated images are managed by the user; this
   repository does not host an online image-generation service.
