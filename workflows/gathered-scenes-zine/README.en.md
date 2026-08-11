# Gathered Scenes Zine

## What it is

This workflow turns a photo into a zine-like scene work through two explicit variants:

- **Preserve photo**: keep the photo as the factual anchor, then organize the page with abstract shapes, structural color, and paper layers.
- **Scene distillation**: do not keep the source pixels; extract the scene's semantic core, emotional tension, and visual metaphor, then rebuild a paper artwork.

Both variants begin with user input. Neither one defines a default place, person, story, or object. The same workflow can process a kitchen, street, coast, interior, or an abstract object.

## Processing logic

Observe the input, separate facts from impressions, remove irrelevant detail, translate space, color, direction, and feeling into paper elements, then compose through layout, whitespace, and surface layers.

With Scene Distillation, the result is a re-creation based on the input scene and should not be described as a direct record of the source photo. With Preserve Photo, the photo subject and factual relations take priority over decorative expansion.

## Four ways to use it

1. **Give it to an image-capable Agent**: provide this directory, the photo, and the selected variant. Ask the Agent to read `workflow.yaml` and produce a checkable task brief before generation.
2. **Copy the constraints into a Prompt**: combine the selected variant's `purpose`, workflow stages, and protection rules in a Prompt. Supply your own subject; do not copy an example subject.
3. **Configure an API key and generate**: give the workflow to an image-capable Agent with your own API key. Add an independent style package only when a visual language is wanted.
4. **Use a local model with ComfyUI**: use image input and layout nodes for Preserve Photo; use reference and redraw nodes for Scene Distillation while keeping the open-subject rule in the text constraints.

Confirm that you have the right to use the photo. After generation, check subject independence, variant execution, unrequested places or objects, and whether the paper elements remain explainably related to the input.

## External boundary

This directory is an independently authored OhMyStyle workflow contract. It does not contain the upstream project's skills, prompts, examples, or brand assets. Obtain the full external project from the [author's current repository](https://github.com/Zeejay0/gathered-scenes-zine-skill) and follow its personal non-commercial license. The originally supplied URL with `04` is retained only as a historical link.
