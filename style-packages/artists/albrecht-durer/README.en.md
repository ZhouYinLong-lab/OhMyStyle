# Albrecht Durer

> Type: artist · Domain: painting

## What this package captures

以精确轮廓、细密排线、结构化明暗和纸面印痕组织画面。

Durer's strength is not a fixed historical subject but the way line carries volume, material, and order. This package transfers that method to any user-supplied subject.

## Visual signature

- precise contour drawing
- fine cross-hatching
- structured value modeling
- paper and plate impression

## Subject independence

This package controls visual language only. It does not prescribe a fixed object, person, location, or story. The representative image is an anonymous demonstration. Replace {SUBJECT}, {LOCATION}, and other placeholders with your own request.

## Generation prompt

~~~
Apply a Northern Renaissance printmaking language: precise contour drawing, disciplined cross-hatching, measured value structure, tactile paper impression, and careful material description. Keep the requested subject, setting, count, and action unchanged; the style controls visual treatment only.
~~~

See [prompts/negative.txt](prompts/negative.txt) for negative constraints and [reproduction.yaml](reproduction.yaml) for the full reproduction contract.

## Reference and rights boundary

The package extracts observable visual cues from public institutional or official pages. It stores source links only and does not copy source artworks, characters, levels, logos, or layouts:

- [The Metropolitan Museum of Art: The Promenade](https://www.metmuseum.org/art/collection/search/336219)

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
