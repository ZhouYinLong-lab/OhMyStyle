# 耶鲁艺术学院

[中文](README.md)

![Representative image of 耶鲁艺术学院](gallery-16x9.jpg)

> **Category:** 设计学院
> **Directory:** `style-packages/schools/yale-school-of-art`

## Overview

以研究、批判讨论、媒介专注和高度个人化的工作室实践形成当代学院气质。 The package turns medium, composition, lighting, palette, material, and surface decisions into executable rules that can be transferred to new subjects and scenes.

## Observable features

research and critique, medium-specific practice, personal studio language, architectural clarity.

## References

- [耶鲁艺术学院官方历史页面](https://www.art.yale.edu/about/history)
- [OhMyStyle 项目说明](https://github.com/ZhouYinLong-lab/OhMyStyle)

## Origin and rights

本包提取的是学校公开历史与教学传统中的可观察方法，不复制任何单一作品、校徽、课程页面排版或在校作品。 External works, school names, marks, and page content remain with their respective rights holders. The generated example is a new anonymous scene and does not imply endorsement or authorization.

## Use only this package

Choose one of the following methods; they do not need to be combined.

### Method 1: Give the package to an image-capable Agent

Upload this directory to an image-capable Agent, or provide its local path, and ask it to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/base.txt`, `prompts/negative.txt`, `palette/palette.json`, and `evaluation.yaml`. Ask the Agent to compile your brief into a complete prompt, generate a new scene, and review the result against `evaluation.yaml` without copying a reference work, mark, or composition.

### Method 2: Copy the prompt

Replace the subject, scene, aspect ratio, and purpose in `prompts/base.txt`; submit `prompts/negative.txt` as the negative prompt. Use the visual signature and palette when tighter control is needed.

### Method 3: Submit through an API-key workflow

Configure your own API key in the image platform or compiler, then submit this package’s base prompt, negative constraints, palette, and selected references. This repository does not host a generation service or manage secrets.

### Method 4: Local model + ComfyUI

Connect the prompts to a local model or ComfyUI workflow; use the palette, reference manifest, and reproduction rules as controls, then review the output with `evaluation.yaml`.

References are for observable feature study only. Do not reproduce source composition, people, text, marks, school emblems, or logos.
