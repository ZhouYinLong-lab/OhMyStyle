# Contributing to OhMyStyle

Thank you for contributing to OhMyStyle. The repository contains two related
but separately maintained systems:

- `style-packages/` contains executable, provenance-aware style packages for
  reproducing artists, photographers, movements, schools, techniques,
  presets, and game-art directions.
- `styles/` contains the inherited `style.json` gallery retained for
  compatibility with the original project. It is a legacy catalog, not a
  claim that OhMyStyle authored every inherited description or preview.

Please read [LICENSE](LICENSE), [LICENSE-OHMYSTYLE.md](LICENSE-OHMYSTYLE.md),
and [NOTICE](NOTICE) before adding or redistributing material.

## Before opening a change

- Record where every external reference came from in `provenance.yaml` or the
  relevant manifest.
- Prefer a source link and descriptive metadata when image redistribution
  rights are not clear. Do not commit a downloaded artwork merely because it
  is easy to find online.
- Do not add copyrighted artworks, screenshots, watermarked images, private
  prompts, brand assets, or dataset material without a documented right to
  redistribute it.
- Generated examples must be marked as generated and must not be presented as
  works by the referenced artist or photographer.
- Do not turn a living artist's or photographer's name into an exact imitation
  claim. Describe observable, non-exclusive characteristics and use the
  package's scope and attribution fields.
- Keep inherited material's original notices. Do not replace or remove the
  original copyright and license files.

## Executable style packages

New reproducible packages belong under the most specific domain directory:

```text
style-packages/<domain>/<slug>/
├── package.yaml
├── identity.yaml
├── visual-signature.yaml
├── reproduction.yaml
├── relations.yaml
├── palette/palette.json
├── prompts/base.txt
├── prompts/negative.txt
├── evaluation.yaml
├── references/manifest.csv
├── provenance.yaml
└── examples/generated/anonymous-v1.png
```

The package schema currently supports `artist`, `photographer`, `movement`,
`school`, `technique`, `preset`, and `game_art`. A package should make the
following independently reviewable:

- identity, scope, aliases, and exclusions;
- observable visual signatures rather than vague adjectives alone;
- composition, material, lighting, color, and reproduction guidance;
- negative constraints and evaluation criteria;
- reference-image provenance, rights status, and attribution;
- anonymous generated examples that demonstrate the package without claiming
  to be an original work by the referenced person or movement.

Validate a package set with:

```powershell
python tools/validate-package.py style-packages
```

Do not hard-code one visual style, palette, artist, photographer, or model
into the runtime. The compiler, mask adapters, preflight checks, and
evaluation tools must remain reusable across packages.

## Legacy `style.json` entries

If you are extending the inherited gallery, add or update one entry under:

```text
styles/<slug>/
├── style.json
├── README.md
└── preview.*
```

Keep the existing field conventions and run:

```powershell
python scripts/validate-style-json.py
```

For new work, prefer `style-packages/` so provenance, reproduction guidance,
evaluation, and rights boundaries are explicit. Do not silently convert an
inherited entry into a new license or attribution statement.

## Engineering changes

Changes to tools, schemas, adapters, or evaluators should include tests for
the behavior they change. In particular:

- keep model and style selection outside generic runtime logic;
- test deterministic preflight and failure reporting;
- test mask dimensions, image hashes, protected-region handling, and
  reflective-material safety gates;
- test color/luminance evaluation without assuming a particular palette;
- document any dependency, model, or hardware assumptions.

Run the full local checks before submitting:

```powershell
python -m unittest discover -s tests -v
python tools/validate-package.py style-packages
python tools/validate.py
python scripts/validate-style-json.py
git diff --check
```

## Pull request checklist

- [ ] The change is scoped to the correct package or engineering layer.
- [ ] External references have source URLs and rights/provenance metadata.
- [ ] No unlicensed artwork, screenshot, logo, or private material was added.
- [ ] Generated images are labeled as generated and are not misattributed.
- [ ] The implementation remains model-agnostic and style-agnostic.
- [ ] Relevant validators and tests pass.
- [ ] Documentation and examples match the current schema.
- [ ] License and attribution notices were preserved.

If you are unsure whether an asset can be redistributed, open an issue with a
link and a description of the intended use instead of committing the asset.
