# Contributing

[中文版](CONTRIBUTING.md)

Thank you for contributing to OhMyStyle. The repository contains two separately maintained systems:

- `style-packages/`: executable, provenance-aware packages for artists, photographers, movements, schools, techniques, original presets, and game-art directions;
- `styles/`: the 110 inherited `style.json` presets retained for compatibility with the original project. Their descriptions and previews are not all authored by OhMyStyle.

Read [LICENSE](LICENSE), [LICENSE-OHMYSTYLE.md](LICENSE-OHMYSTYLE.md), and [NOTICE](NOTICE) before adding or redistributing material.

## Before submitting a change

- Record every external source in `provenance.yaml` or `references/manifest.csv`.
- Use source links and descriptive metadata when image redistribution rights are unclear. Do not commit an artwork merely because it is visible online.
- Do not add unlicensed artworks, photographs, game screenshots, watermarked images, brand assets, private prompts, or dataset material.
- Mark generated examples as generated. Never present them as original works by the referenced artist, photographer, movement, or game.
- For living artists and photographers, describe observable, non-exclusive characteristics. Do not claim exact imitation, collaboration, authorization, or endorsement.
- Preserve the original notices, licenses, and attribution for inherited material.

## Canonical style-package structure

New packages belong under the most specific category directory:

```text
style-packages/<category>/<id>/
├── package.yaml                 # identity, kind, domain, version, file index
├── identity.yaml                # scope, subjects, exclusions, sources
├── visual-signature.yaml        # subject-independent visual features
├── reproduction.yaml            # medium, materials, construction order
├── relations.yaml               # related movements, concepts, boundaries
├── palette/palette.json         # color roles and values
├── prompts/base.txt             # base prompt
├── prompts/negative.txt         # negative constraints
├── evaluation.yaml              # post-generation checks
├── references/manifest.csv      # sources, rights, attribution, local paths
├── provenance.yaml              # research status and rights boundaries
├── resource.yaml                # registry resource contract
├── examples/generated/          # anonymous examples awaiting review
├── examples/accepted/           # human-reviewed examples
├── examples/rejected/           # optional failure-boundary examples
├── gallery-16x9.jpg             # native horizontal 16:9 cleared or newly generated image
└── README.md / README.en.md     # user-facing bilingual documentation
```

Supported `kind` values are `artist`, `photographer`, `movement`, `school`, `technique`, `preset`, and `game_art`. Supported `domain` values are `painting`, `photography`, `printmaking`, `design`, `game_art`, and `hybrid`.

## Template-based creation

Do not copy an existing artist or game package. Use the scaffold command to create the complete structure, bilingual READMEs, reference directories, prompts, evaluation scaffold, rights notes, and a representative-image placeholder:

```powershell
python tools/new-style-package.py `
  --kind artist `
  --id coastal-noir `
  --name "Chinese style name" `
  --domain painting `
  --summary "Describe the package with observable medium, composition, lighting, color, and surface rules."
```

The command refuses to overwrite an existing directory. Without source arguments it creates an L1 research draft. When a traceable source is available, create an L2 package with a link-only source record:

```powershell
python tools/new-style-package.py `
  --kind photographer `
  --id example-photography-package `
  --name "Chinese photography style name" `
  --domain photography `
  --summary "Describe the package with observable camera, composition, lighting, color, and grain rules." `
  --source-url "https://example.org/source" `
  --source-title "Source page or portfolio title" `
  --source-creator "Creator or institution" `
  --source-attribution "Required attribution"
```

The template lives in [`templates/style-package`](templates/style-package). [`TEMPLATE.md`](templates/style-package/TEMPLATE.md) explains every file, and [`TEMPLATE.en.md`](templates/style-package/TEMPLATE.en.md) provides the English version. The template is outside `style-packages/`, so it is not discovered as a publishable package.

Complete a new package in this order:

1. Replace every `TODO` with concrete, subject-independent rules for identity, visual signature, reproduction, palette, evaluation, and prompts. The base prompt must retain `{SUBJECT}` / `{LOCATION}` placeholders and the subject-independence contract.
2. Do not make a bridge, house, city, person, flower, vehicle, landmark, or fixed narrative the default generated content. Concrete scenes belong in `examples/` or benchmarks and must be labeled as test examples.
3. Add source rows to `references/manifest.csv` and explain scope, attribution, and redistribution boundaries in `provenance.yaml`.
4. Replace the representative image with a natively composed horizontal 16:9 generated, public-domain, or explicitly redistributable image. Do not crop a portrait image into a gallery card, and do not bundle an image merely because it is visible online.
5. Put new generated samples in `examples/generated/`. Move an image to `examples/accepted/` only after human review and metadata are present.
6. Update the version and `version.md` when changing a published package.
7. Run the complete validation set before opening a pull request.

## Validation commands

```powershell
python tools/scaffold-resource-manifests.py style-packages --force
python tools/build-registry.py
python tools/validate-package.py style-packages
python tools/validate-resources.py style-packages
python tools/validate-benchmarks.py style-packages
python tools/validate-subject-independence.py style-packages
python -m unittest discover -s tests -v
python tools/validate.py
python scripts/validate-style-json.py
git diff --check
```

Engineering changes must remain model-agnostic and style-agnostic. Do not hard-code one artist, palette, model, or image platform into the compiler, mask adapters, preflight checks, or evaluators.

## Inherited `style.json` presets

For compatibility-gallery changes, update:

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

Prefer `style-packages/` for new work. Do not silently convert inherited material into a new license or attribution statement.

## Pull request checklist

- [ ] The change is scoped to the correct package or engineering layer.
- [ ] External references have URLs, rights status, and attribution metadata.
- [ ] No unlicensed artwork, screenshot, logo, brand asset, or private material was added.
- [ ] Generated samples are labeled and not misattributed.
- [ ] The implementation remains model-agnostic and style-agnostic.
- [ ] Relevant validators and tests pass.
- [ ] Documentation, examples, and schemas agree.
- [ ] The base prompt is subject-independent and example scenes are not mixed into its rules.
- [ ] Existing licenses and notices are preserved.

If redistribution rights are unclear, open an issue with the source link and intended use instead of committing the file.
