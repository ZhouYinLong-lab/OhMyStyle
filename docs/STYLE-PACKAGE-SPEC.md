# Style Package Specification

OhMyStyle stores a style as a reproducible package rather than as a prompt and
some images. A package separates four responsibilities:

1. `style.yaml` defines the visual identity and machine-readable constraints.
2. References and examples show what the style is, including accepted and
   rejected results.
3. Technique and prompt files describe how to reproduce the style.
4. Provenance and license files explain where every inherited or external asset
   came from and whether it can be redistributed.

## Package layout

```text
style-packages/<category>/<style-id>/
├── README.md
├── package.yaml
├── identity.yaml
├── visual-signature.yaml
├── reproduction.yaml
├── relations.yaml
├── references/
│   └── manifest.csv
├── palette/
│   └── palette.json
├── prompts/
│   ├── base.txt
│   ├── variations.txt
│   └── negative.txt
├── examples/
│   ├── accepted/
│   ├── generated/
│   └── rejected/
├── evaluation.yaml
├── provenance.yaml
└── resource.yaml                 # machine-readable resource contract
```

The canonical executable packages live under `style-packages/`. The
`styles/quiet-documentary/` directory is retained as a compatibility example
for the earlier `style.yaml` layout, not as the current package contract. A
package may add images only after their source, creator, license, attribution,
and redistribution status have been recorded in `references/manifest.csv` and
`provenance.yaml`.

Folder-level placeholder README files and a standalone `version.md` are not
part of the package contract. Keep explanations in the package-level README
and machine-readable metadata in YAML/JSON files; add a subdirectory README
only when it contains information that is not represented elsewhere.

## Compatibility with the original collection

The existing `styles/*/style.json` folders remain supported as the legacy
AI-Visual-Prompt-Cookbook format. They are not silently converted because the
new package format has a different purpose and adds provenance, technical
parameters, and evaluation evidence. New executable packages should use
`package.yaml` and the schema in [`schema/package.schema.json`](../schema/package.schema.json).

## Versioning

Package versions use `MAJOR.MINOR.PATCH`:

- major: the definition or interpretation changes materially;
- minor: new dimensions, examples, or compatible metadata are added;
- patch: wording, ranges, or source metadata are corrected.

Use `tools/validate.py` before publishing. The bilingual package gallery and
package entry-point READMEs are static Markdown files maintained alongside the
package. When adding a package, update its category gallery, language switch,
representative image, and package README links together so the change remains
reviewable in a pull request.
