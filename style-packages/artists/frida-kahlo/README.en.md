# Frida Kahlo

[中文版](README.md)

![Frida Kahlo representative image](gallery-16x9.jpg)

> **Category:** artist
> **Domain:** painting
> **Path:** `style-packages/artists/frida-kahlo`

## Overview

This package extracts a clear and intimate psychological space built from frontal
presence, firm contour, shallow depth, saturated color blocks, and meaningful
relationships between objects. It does not turn self-portraits, traditional
clothing, monkeys, or medical imagery into default content.

## Curatorial note

The most useful lesson is the way ordinary things can acquire weight through
placement. A cup, cloth, or plant can feel almost like a character when it sits
inside a clear color field and a deliberate contour. Treat this as a method for
intimacy and relation, not as a set of exotic decorations.

## Subject independence

This package controls how an image is generated, not what it depicts. Your prompt
defines the people, objects, place, architecture, plants, and narrative. The cup
and cloth in the representative image are only a benchmark subject.

## Sources and rights

The Museo Frida Kahlo biography and timeline are used as a research source. External
works, photographs, trademarks, and web content remain with their rights holders;
this package stores source links and an original generated demonstration only.

## Use only this package

1. Give the directory to an image-capable Agent and ask it to read the YAML files,
   prompts, palette, and evaluation before compiling your own subject into a full
   prompt.
2. Copy `prompts/base.txt`, replace the subject, location, and aspect ratio, and
   submit `prompts/negative.txt` as the negative prompt when supported.
3. Submit the prompts, palette, and constraints through your own API tool after
   configuring your own API key. This repository does not host generation.
4. Connect the package to a local model or ComfyUI workflow and review the result
   against `evaluation.yaml`.
