# Style Package Specification

See the [art style architecture guide](ARCHITECTURE.en.md) for the full content
model, execution paths, and the distinction between formal packages and v2 pilots.

OhMyStyle stores a style as a reproducible package rather than as a prompt and
some images. A package separates four responsibilities:

1. `package.yaml` identifies the package; `identity.yaml` and
   `visual-signature.yaml` define its scope and visual rules.
2. References and examples show what the style is, including accepted and
   rejected results.
3. Technique and prompt files describe how to reproduce the style.
4. Provenance and license files explain where every inherited or external asset
   came from and whether it can be redistributed.

The [art-style architecture proposal](ART-STYLE-PACK-ARCHITECTURE.md) describes
a draft approach to evidence-linked visual rules, scoped school practices,
strict media constraints, and comparative evaluation. Its study files are
design examples. Runnable v2 directions use a separate
[`art-direction.schema.json`](../schema/art-direction.schema.json) contract
and an explicit compiler option; see the [pilot guide](../experiments/style-v2/README.md).

## Package layout

```text
style-packages/<category>/<style-id>/
├── README.md
├── package.yaml
├── art-direction.yaml           # optional, explicitly compiled v2 rules
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

A package may register a v2 direction file as `files.art_direction` in
`package.yaml`. The optional field preserves existing manifests. It does not
change legacy compilation; select the registered file explicitly with
`python tools/compile-style.py <package> --direction package --subject "..."`.
See the [architecture guide](ARCHITECTURE.md#v2-direction).

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
