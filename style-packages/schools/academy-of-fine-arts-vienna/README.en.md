# Academy of Fine Arts Vienna

> Type: design_school · Domain: painting

## What this package captures

以观察、比例、结构素描、受控明暗和完成度优先的学院训练组织画面。

Academic art is a training method rather than a fixed subject list. This package emphasizes structure, light, and finish.

## Visual signature

- careful proportion
- observational drawing
- controlled chiaroscuro
- resolved material edges

## Subject independence

This package controls visual language only. It does not prescribe a fixed object, person, location, or story. The representative image is an anonymous demonstration. Replace {SUBJECT}, {LOCATION}, and other placeholders with your own request.

## Generation prompt

~~~
Apply an academic fine-art training language: accurate proportion, studied structure, controlled chiaroscuro, resolved edges, and deliberate material observation. Keep the user's subject and context unchanged; do not insert an academy, classroom, or historical narrative.
~~~

See [prompts/negative.txt](prompts/negative.txt) for negative constraints and [reproduction.yaml](reproduction.yaml) for the full reproduction contract.

## Reference and rights boundary

The package extracts observable visual cues from public institutional or official pages. It stores source links only and does not copy source artworks, characters, levels, logos, or layouts:

- [Academy of Fine Arts Vienna: History](https://www.akbild.ac.at/en/university/history)

## Files

- [identity.yaml](identity.yaml)
- [visual-signature.yaml](visual-signature.yaml)
- [prompts/](prompts/)
- [examples/generated/](examples/generated/)
- [evaluation.yaml](evaluation.yaml)

## Use this package only

1. Download this directory and read identity.yaml, visual-signature.yaml, and reproduction.yaml.
2. Open prompts/base.txt, then replace the subject with your own request; negative constraints are in prompts/negative.txt.
3. Choose one execution method: give the package to an image-capable Agent; copy the prompt to an image platform with your own API key; or import the prompt, reference list, and palette into a local model and ComfyUI workflow.
4. Use references to understand observable features. Do not copy the source composition, people, text, trademarks, or identifiable assets.
5. The user manages the model, API key, generated images, and storage. This repository does not host an online image service.
