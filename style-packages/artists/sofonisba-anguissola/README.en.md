# Sofonisba Anguissola

[中文版](README.md)

![Sofonisba Anguissola representative](gallery-16x9.jpg)

> **Category:** artist<br>
> **Domain:** painting<br>
> **Path:** `style-packages/artists/sofonisba-anguissola`

## Overview

Clear yet gentle portrait modeling, attentive exchanges of gaze, and restrained fabric detail make expression and gesture carry the image. Portraiture is an optional test subject and never overrides the user's request.

## Curatorial note

These portraits build relationships through gaze and gesture; clothing and setting offer only the clues they need. Start by deciding how figures look and respond to one another, then reserve detail for the faces and hands that clarify that relationship.

## Package files

- `identity.yaml`: scope, open subject policy, and exclusions
- `visual-signature.yaml`: traits that should remain stable across subjects
- `reproduction.yaml`: medium, materials, and construction order
- `prompts/base.txt`, `prompts/negative.txt`: base prompt and negative constraints
- `palette/palette.json`: color roles and values
- `evaluation.yaml`: post-generation checks
- `references/manifest.csv`, `provenance.yaml`: sources and rights boundaries

## Sources and rights

The reference manifest links to collection records from The Metropolitan Museum of Art, Museo del Prado, and Nationalmuseum for research only. No historical artwork or collection photograph is included. The rules describe restrained tonal modeling, individualized expression, and selective detail without recreating a particular portrait or sitter.

## Use this package

Read `prompts/base.txt`, replace `{SUBJECT}` and `{LOCATION}`, and submit `prompts/negative.txt` alongside it. After generation, use `evaluation.yaml` to review prompt adherence, expression, medium, and detail control. You can also use the rules with your own API or local-model workflow; this repository does not host an image service or API keys.

The gallery and sample are newly generated and pending human review. They are not works by Anguissola and do not imply endorsement or authorization.
