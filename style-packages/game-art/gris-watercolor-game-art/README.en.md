# GRIS Watercolor Game Art

> Type: game_art · Domain: game_art

## What this package captures

以透明水彩层、渐变色域、柔和边缘和可读路径组织具有游戏空间感的画面。

This package borrows the spatial treatment of a watercolor 2D environment; it does not require a character, ruins, or a specific narrative in every image.

## Visual signature

- transparent watercolor layers
- gradual palette transitions
- soft atmospheric edges
- readable 2D traversal space

## Subject independence

This package controls visual language only. It does not prescribe a fixed object, person, location, or story. The representative image is an anonymous demonstration. Replace {SUBJECT}, {LOCATION}, and other placeholders with your own request.

## Generation prompt

~~~
Apply an original hand-painted 2D game-art language associated with translucent watercolor layers, gradual color transitions, soft atmospheric edges, and a clear readable spatial path. Preserve the user's subject and action; do not add a named character, game interface, specific level, ruins, forest, or story event unless requested.
~~~

See [prompts/negative.txt](prompts/negative.txt) for negative constraints and [reproduction.yaml](reproduction.yaml) for the full reproduction contract.

## Reference and rights boundary

The package extracts observable visual cues from public institutional or official pages. It stores source links only and does not copy source artworks, characters, levels, logos, or layouts:

- [Nomada Studio: Studio](https://nomada.studio/studio/)

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
