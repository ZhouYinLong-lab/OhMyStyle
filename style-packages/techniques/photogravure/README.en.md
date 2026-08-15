# Photogravure

> Type: technique · Domain: printmaking

## What this package captures

以连续灰阶、油墨密度、纸面吸收和细密颗粒把摄影转化为有物质感的印刷图像。

Photogravure is defined by the relationship between tonal range, ink, and paper—not by an automatic newspaper or historical-documentary subject.

## Visual signature

- continuous gray scale
- ink density in shadow
- matte paper absorption
- fine plate grain

## Subject independence

This package controls visual language only. It does not prescribe a fixed object, person, location, or story. The representative image is an anonymous demonstration. Replace {SUBJECT}, {LOCATION}, and other placeholders with your own request.

## Generation prompt

~~~
Render the user's subject as an original photogravure-inspired image: continuous tonal scale, dense but open ink shadows, matte paper absorption, fine plate grain, and restrained monochrome or warm duotone. Keep the subject, location, and action exactly as requested; do not add a newspaper, war story, or text.
~~~

See [prompts/negative.txt](prompts/negative.txt) for negative constraints and [reproduction.yaml](reproduction.yaml) for the full reproduction contract.

## Reference and rights boundary

The package extracts observable visual cues from public institutional or official pages. It stores source links only and does not copy source artworks, characters, levels, logos, or layouts:

- [Library of Congress: The Rotogravure Process](https://www.loc.gov/static/collections/world-war-i-rotogravures/articles-and-essays/the-rotogravure-process/)

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
