# Aubrey Beardsley

[中文版](README.md)

![Aubrey Beardsley style package representative](gallery-16x9.jpg)

> **Category:** artist  
> **Medium:** pen and brush in ink  
> **Path:** `style-packages/artists/aubrey-beardsley`

## Overview

This package extracts graphic rules from Beardsley's fin-de-siècle black-and-white illustration: establish hierarchy with solid ink masses and broad open paper, organize figures and objects with fluid calligraphic contour, and reserve dense detail for focal areas. The line-block print context also requires black and white shapes to remain distinct at reduced size.

The package controls line, black-white balance, detail density, and page space. It does not require Victorian dress, vines, literary characters, or ornamental frames.

## Distinction from nearby directions

- **Alphonse Mucha:** often builds colored planes, decorative figures, and poster layouts; this package stays with monochrome ink, decisive masses, and asymmetric open space.
- **Generic Gothic illustration:** skulls, pointed arches, and ominous props are not required. The signature lies in the organization of line and positive-negative shape.
- **Dense print hatching:** the goal is not uniform engraving detail; focal density must contrast clearly with quieter areas.

## Package contents

- `identity.yaml`: scope, open-subject policy, and exclusions
- `visual-signature.yaml`: traits that survive subject changes
- `reproduction.yaml`: allocate black and white, then build contour and focal detail
- `prompts/base.txt`, `prompts/negative.txt`: base prompt and negative constraints
- `palette/palette.json`: ink, paper white, and optional gray wash
- `evaluation.yaml`: checks for contrast, line, detail, and subject
- `references/manifest.csv`, `provenance.yaml`: museum sources and rights boundaries
- `examples/generated/`: unreviewed candidates are local-only by default

## Sources and rights

The references link to the Musée d'Orsay, Victoria and Albert Museum, and The Metropolitan Museum of Art. Source works are for research only; none are bundled or redrawn in this repository.

The representative image is an anonymous new scene, not an original, reproduction, or authorized work by Beardsley, and does not imply endorsement by a museum or artist estate.

## Use

Fill `{SUBJECT}`, `{LOCATION}`, and `{SUBJECT_ACTION}` in `prompts/base.txt`. Send the base prompt and negative constraints to your image workflow. Translate the user-supplied subject into monochrome graphic form; do not add period clothing, vines, literary narrative, or poster lettering by default.

Use `evaluation.yaml` to check whether the image works first as black-white masses, whether the contour has a deliberate calligraphic rhythm, and whether detail is concentrated at focal points. If the image turns into evenly dense line noise at smaller sizes, reduce texture and restore open paper.
