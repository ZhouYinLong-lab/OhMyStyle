# Vermeer Light + Monet Color

[中文](README.md)

![Vermeer Light + Monet Color example](examples/generated/anonymous-v1.png)

## What this is

A cross-style recipe is not an independent artist, photographer, or movement. It combines multiple packages by explicit responsibilities such as zone, medium, lighting, or palette. It does not turn several names into an undefined blended label.

## Composition mode

Current mode: `blend`

- `artists/johannes-vermeer`: palette; Preserve calm interior light and readable object structure.
- `artists/claude-monet`: palette; Contribute chromatic temperature variation without flattening form.

## Mechanism

- `stack`: separate packages own separate dimensions, such as pixel medium and painted atmosphere.
- `blend`: weighted rules share a dimension while preserving the main structure.
- `contrast`: packages are assigned to separate zones so color, material, or texture rules do not contaminate one another.

See `composite.yaml` for constraints. Generated example:

![Cross-style example](gallery-16x9.jpg)

## Use only this package

This composite references the base packages listed in `composite.yaml`. Download this directory together with those base packages.

### Method 1: give it to an image-capable Agent

Provide the composite directory and every base package listed under `bases`. Ask the Agent to read `composite.yaml`, each base package's `README.md`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/base.txt`, and `prompts/negative.txt`, then compile your subject using the declared composition mode.

The Agent must preserve:

- each base package's role;
- `zone` assignments;
- weights;
- `constraints.must` and `constraints.avoid`;
- the boundaries between styles.

### Method 2: compile and copy the Prompt

From the repository root:

```bash
python tools/compile-composite.py \
  style-packages/composites/vermeer-x-monet \
  --subject "replace this with your subject" \
  --mode auto \
  --profile generic
```

Copy the resulting `prompt` and `negative_prompt` fields into your image platform. `--mode auto` uses the recipe's declared mode; you may also force `stack`, `blend`, or `contrast`.

### Method 3: submit through your own API key

Use your own image platform or API client to submit the compiled prompt, negative constraints, subject variables, and reference resources. OhMyStyle only provides the package and compilation logic; it does not host an image API or store API keys.

### Method 4: local model + ComfyUI

Import the compiled prompt and negative prompt into a local model or ComfyUI workflow, together with the base packages' references, palettes, and structural constraints. For `contrast`, add a regional mask manually when stronger separation is required; the composite package does not generate masks automatically.

Use references to understand observable decisions. Do not copy a source work's exact composition, people, text, trademarks, or marks.

Model weights, API keys, and generated images remain under the user's control.
