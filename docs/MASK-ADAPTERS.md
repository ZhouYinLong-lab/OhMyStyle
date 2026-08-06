# Mask adapters and safe automatic segmentation

The runtime separates two jobs:

1. A model adapter supplies semantic masks for the *same rendered image*.
2. `tools/mask-from-color.py` intersects those masks with a target color in
   CIELAB and removes unsafe pixels before `tools/recolor-lab.py` runs.

This keeps a weak image model useful without trusting it to perform exact
color engineering. The adapter does not need to be tied to a vendor. Any
provider can export the following manifest:

```json
{
  "image_sha256": "sha256-of-the-render",
  "classes": {
    "skin": "masks/skin.png",
    "hair": "masks/hair.png",
    "hands": "masks/hands.png",
    "jewelry": "masks/jewelry.png",
    "glasses": "masks/glasses.png"
  }
}
```

All masks must be same-size grayscale PNGs. The hash is mandatory in
production because a mask from a different render is unsafe to reuse.

## Person safety profile

For complex portraits the color threshold is never the only signal. The
`person` profile requires protected semantic masks for skin, face, hair, eyes,
lips, hands, jewelry, and glasses. Target-color seeds overlapping those masks
are removed and the command fails closed if the provider omitted any required
class. Border-connected regions, isolated noise, and white specular pixels are
also removed.

## Reflective safety profile

For glass, metal, lacquer, and wet surfaces, the adapter treats near-white
low-chroma pixels as *reflection candidates*, not as material color. The tool
writes a separate reflection mask for inspection and refuses the result when
reflection loss leaves too little material or when reflective ambiguity is too
high. It does not invent a transparent-object mask from color alone.

Example:

```powershell
python tools/mask-from-color.py render.png masks/shirt.png `
  --target-hex 0070FC `
  --safety-profile person `
  --manifest provider/manifest.json `
  --report runs/mask-report.json `
  --reflection-mask masks/shirt-reflections.png
```

Exit code `2` means the mask was written for inspection but rejected by the
safety gates. `--allow-review` is available for manual review workflows; it
must not be used for unattended exact-color postprocessing.

The goal is not to promise perfect segmentation from pixels alone. The goal
is to make ambiguity explicit, preserve material highlights, prevent skin and
hair contamination, and stop the pipeline before an unsafe recolor becomes a
false success.
