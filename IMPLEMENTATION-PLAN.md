# Executable Style Package System

## Objective

Turn the repository from a descriptive style catalog into a model-agnostic
style reproduction toolkit. A package must be able to produce a compiled
generation brief, select the right reference assets, record a render run, and
evaluate measurable constraints before a sample is accepted.

## Decisions

- Keep package data declarative; runtime tools live in `tools/`.
- Do not hard-code one image model. Model adapters emit provider-neutral JSON
  plus a prompt and reference paths; provider-specific adapters can be added
  later.
- Use local deterministic checks first: Pillow for image statistics and
  PyYAML/JSON for package loading. Optional semantic models are not required
  for the baseline workflow.
- Treat reference images according to their declared role. The contrast-color
  package uses palette cards as color references; floral images are not subject
  templates.
- A generated image is never accepted only because it looks attractive. It
  needs a run record, measurable checks, and human review status.

## Implementation slices

1. Package loader and prompt compiler.
2. Reference selector and provider-neutral run manifest.
3. Image evaluator for palette, flatness, luminance, and basic area metrics.
4. CLI workflow and tests using the contrast-color package.
5. Documentation and package-specific evaluation thresholds.

## Acceptance criteria

- `python tools/compile-style.py ...` reads a package and writes a model-neutral
  generation brief with selected references.
- `python tools/evaluate-render.py ...` produces machine-readable metrics and
  pass/fail results without requiring a model API.
- A sample run can be recorded under an ignored local `runs/` directory without
  adding generated images to Git by accident.
- The contrast-color package exposes explicit hard constraints for pure flat
  color and same-luminance tests.
- Existing validators and all new tests pass.

## Progress

- [x] Repository and existing package structure inspected.
- [x] Add executable package loader/compiler.
- [x] Add reference selection and run manifest.
- [x] Add deterministic render evaluator.
- [x] Add tests and documentation.
- [x] Add CIELAB custom-color checks after reviewing the equal-lightness portrait.
- [x] Add preflight strategy selection and deterministic masked Lab recoloring.
- [x] Validate, commit, and push the iteration.
