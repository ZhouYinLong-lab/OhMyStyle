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
├── examples/generated/              # staging area for anonymous examples
├── examples/accepted/               # human-reviewed examples only
├── gallery-16x9.jpg                 # representative image, rights-cleared or generated
└── README.md / README.en.md
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

### Create a package with the contributor workflow

Use the canonical template instead of copying an existing artist or game
package. The command creates the complete directory, bilingual README files,
reference folders, prompt files, evaluation scaffold, rights notes, and a
neutral representative-image placeholder:

```powershell
python tools/new-style-package.py `
  --kind artist `
  --id coastal-noir `
  --name "中文风格名" `
  --domain painting `
  --summary "用可观察的媒介、构图、光线、色彩和表面规则描述这个独立风格包。"
```

The supported `--kind` values are `artist`, `photographer`, `movement`,
`school`, `technique`, `preset`, and `game_art`. The `--domain` values are
`painting`, `photography`, `printmaking`, `design`, `game_art`, and `hybrid`.
The package id must be lowercase kebab-case and must match its directory name.

If a traceable source is already available, provide it while creating the
package. This records a link-only manifest row and starts the package at L2:

```powershell
python tools/new-style-package.py `
  --kind photographer `
  --id example-photography-package `
  --name "中文摄影风格名" `
  --domain photography `
  --summary "用可观察的镜头、构图、光线、色彩和颗粒规则描述这个摄影风格包。" `
  --source-url "https://example.org/source" `
  --source-title "来源页面或作品集标题" `
  --source-creator "作者或机构" `
  --source-attribution "使用时应保留的署名信息"
```

Without a source URL, the command creates an L1 research draft. Fill the
source manifest and provenance before opening a pull request; do not use a
placeholder URL as evidence. Replace `gallery-16x9.svg` with a representative
image that is generated, public-domain, or otherwise cleared for redistribution.
Do not download a reference artwork merely because it is visible online.

The expected update sequence is:

1. Create the package with `tools/new-style-package.py`.
2. Replace every `TODO` in identity, visual signature, reproduction, palette,
   evaluation, and prompts with concrete, subject-independent rules.
3. Add source rows to `references/manifest.csv` and explain their role and
   rights in `provenance.yaml`. Keep protected images link-only unless their
   redistribution permission is documented.
4. Add generated examples to `examples/generated/`. Move only independently
   authored, human-reviewed images to `examples/accepted/`, with metadata.
5. Rebuild resource manifests and the registry, then run the checks below.
6. Update the package version and `version.md` when a published package changes.

The template itself is maintained at [`templates/style-package`](templates/style-package)
and is deliberately outside `style-packages/`, so it is not discovered as a
publishable package.

Validate a package set with:

```powershell
python tools/scaffold-resource-manifests.py style-packages --force
python tools/build-registry.py
python tools/validate-package.py style-packages
python tools/validate-resources.py style-packages
python tools/validate-benchmarks.py style-packages
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
