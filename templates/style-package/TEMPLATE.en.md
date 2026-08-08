# Style package template

[中文版](TEMPLATE.md)

This directory is the canonical template for an executable style package. It is
not itself a publishable package. Create a package with
`tools/new-style-package.py` under `style-packages/<category>/<id>/`; do not
rename and submit this directory directly.

```powershell
python tools/new-style-package.py `
  --kind artist `
  --id your-style-id `
  --name "Chinese style name" `
  --domain painting `
  --summary "At least 30 characters describing observable medium, composition, lighting, color, or surface rules."
```

Add `--source-url`, `--source-title`, `--source-creator`, and
`--source-attribution` to create an L2 link-backed manifest. Without a source,
the command creates an L1 research draft. Replace all `TODO` values, verify
rights and provenance, and replace `gallery-16x9.svg`. The representative
image must be composed natively as a horizontal 16:9 image; do not generate a
portrait first and crop or stretch it into a gallery card. Then run the checks
in `CONTRIBUTING.en.md` before submitting.

The template maps to these package files:

- `package.yaml`: identity, category, domain, version, and file index;
- `identity.yaml`: scope, subjects, exclusions, and entity sources;
- `visual-signature.yaml`: visual features that survive a subject change;
- `reproduction.yaml`: medium, materials, and construction order;
- `relations.yaml`: related movements, concepts, and boundaries;
- `palette/palette.json`: color roles and values;
- `prompts/`: base prompt and negative constraints;
- `evaluation.yaml`: post-generation checks;
- `references/` and `provenance.yaml`: sources, attribution, and redistribution boundaries;
- `examples/`: anonymous generated samples awaiting review, accepted samples, and optional failures;
- `resource.yaml`: maturity and registry contract;
- `README.md` and `README.en.md`: user-facing bilingual documentation.

## Subject-independence requirement

`prompts/base.txt` must contain the subject-independence contract and use the
`{SUBJECT}` and `{LOCATION}` placeholders. A style package describes only
medium, composition, lighting, color, material, texture, and edge behavior.
Concrete content such as bridges, houses, people, cities, flowers, or vehicles
belongs only in `examples/` or benchmarks. `identity.yaml` must set
`scope.subject_policy` to `open`.

`gallery-16x9.svg` is only a neutral placeholder. Replace it before publication
with a natively composed horizontal 16:9 generated, public-domain, or
explicitly redistributable representative image. The package README and the
root gallery both use this horizontal representative image directly.
