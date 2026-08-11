# Photo Abstract Editorial

## What it is

This is a “preserved photo plus abstract editorial” workflow. The input photo remains the main source of facts: the photo area carries the people, objects, architecture, landscape, and spatial information, while the adjacent abstract area extracts direction, color, scale, and structural relationships from that photo.

It is not a fixed-subject template or a default poster style. The input may be a person, object, building, or natural scene, and the result should change with the input.

## Processing logic

1. Observe the real subjects, spatial layers, and dominant colors in the photo.
2. Keep a clear photo area and protect the identity of its subject.
3. Translate observable spatial relationships into a small set of abstract shapes, lines, or planes.
4. Use whitespace and layout to form an editorial work; titles and other text layers are optional.

The workflow may change composition, color relationships, surface, and typographic hierarchy. It protects the input subject, user constraints, and photographic facts. An example location must never become a default location in later generations.

## Four ways to use it

1. **Give it to an image-capable Agent**: provide this directory and your photo, then describe which facts to preserve, the aspect ratio, and whether text is wanted.
2. **Copy the constraints into a Prompt**: read `workflow.yaml` and copy `purpose`, `allowed_axes`, and the protection rules into your Prompt; replace only your subject and layout request.
3. **Configure an API key and generate**: use an image-capable Agent or service with your own API key. Ask it to read this workflow before submitting the task.
4. **Use a local model with ComfyUI**: feed the original photo into separate layout, abstraction, and output-size nodes; do not let a style node replace the photo subject.

Confirm that you have the right to use the photo. After generation, check that the original subject remains recognizable, every abstract element has a basis in the photo, and no fixed unrequested object appeared.

## External boundary

This directory is an independently authored OhMyStyle compatibility contract. It does not contain the upstream project's skills, prompts, examples, or brand assets. To use the author's full workflow, obtain it from the [external project](https://github.com/ZzzLc0405/photo-abstract-editorial) and follow its license.
