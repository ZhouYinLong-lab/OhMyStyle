# Style Package Expansion Workflow

This document defines the standard expansion workflow for OhMyStyle. Batch size is determined by the actual scope of the work; every package needs independent research, a representative image, bilingual user documentation, and verifiable visual rules.

## 1. Batch rules

- A formal expansion batch must plan and register the packages it actually intends to deliver. Editing index files does not count as adding packages, and repeated boilerplate packages are not acceptable.
- A batch may span one or more top-level categories, but every package must declare its `category`, `kind`, research target, and style boundaries.
- Each package is an independent delivery unit: complete and validate one package, then commit that package. Batch-level gallery, index, and count updates are made after package work is complete.
- If a batch scope changes, record the reason, completed count, and follow-up plan. An incomplete batch must not be marked complete by default.
- A composite is not an independent style package; it only references existing base packages.

Use [`templates/expansion-batch.yaml`](../templates/expansion-batch.yaml) for the batch record. Real records should normally live under `batches/YYYY-MM-batch-XX.yaml` and be checked with the validator.

## 2. Per-package workflow

### 2.1 Research original works before extracting style

Artist, photographer, movement, school, craft, and game-art packages must begin with traceable original works or first-hand visual material. Text-only descriptions are not enough for a mature style package.

Research should establish:

1. where the references come from, including title, creator or institution, and URL;
2. the rights status and whether the image may be included in the repository;
3. which observable features remain stable across subjects, such as medium, edges, composition, light, color, material, space, or grain;
4. which features belong only to one work and must not enter the base prompt;
5. how generated samples are labeled so they are not mistaken for originals or official works.

Record the research in `references/manifest.csv` and `provenance.yaml`. Keep original references separate from newly generated samples and label both clearly.

### 2.2 Define a subject-independent style contract

A style package specifies how an image is rendered, not what it must depict. The base prompt must:

- use `{SUBJECT}` and `{LOCATION}` placeholders;
- retain the subject-independence contract and set `identity.yaml` to `scope.subject_policy: open`;
- describe only medium, composition, light, color, material, texture, space, and edge behavior;
- avoid making bridges, houses, people, cities, flowers, vehicles, landmarks, or fixed narratives the default subject;
- keep concrete scenes in `examples/` or benchmarks and label them as test inputs.

Even when a package is named after a game, series, or creator, it may extract stable visual rules but must not force a recurring location, character, or prop into every generation.

### 2.3 Generate native representative images and samples

- Every package needs a natively composed horizontal 16:9 `gallery-16x9.jpg`; do not generate a portrait image and crop, stretch, or assemble it into a gallery image.
- The representative image should demonstrate the style rather than only one fixed object; use a neutral, replaceable subject when possible.
- Put new generations in `examples/generated/`. Move them to `examples/accepted/` only after human review, with model, prompt, date, and generation status recorded.
- Do not disguise originals, game screenshots, photographs, or artwork as generated samples. Do not package material whose redistribution rights are unclear.

### 2.4 Complete user documentation

Every package must provide `README.md` and `README.en.md` for users, explaining:

- which visual features the package controls;
- which subjects it does not impose;
- source and rights boundaries;
- how to use the generation prompt, negative constraints, and variables;
- how to run it with an Agent, hosted API, or local model;
- how the representative image and generated samples are labeled.

## 3. Per-package acceptance gates

| Gate | Requirement |
| --- | --- |
| Research | Original works or first-hand visual material with traceable sources |
| Rights | Complete `provenance.yaml` and `references/manifest.csv`; no unlicensed redistribution |
| Structure | All template files, version data, and registry data are consistent |
| Style | The base prompt describes visual rules only and uses an `open` subject policy |
| Images | Native 16:9 representative image and at least one labeled generated sample |
| Docs | Bilingual user-facing READMEs; Chinese is not a sentence-by-sentence machine translation |
| Validation | Package, resource, benchmark, subject-independence, and test checks pass |

## 4. Commits and batch states

Recommended per-package commit format:

```text
feat: add style package <category>/<id>
```

One package gets one commit. Batch-level index, root gallery, and count updates may use a separate integration commit after all 20 packages are complete; that commit does not replace the package commits.

Recommended batch states:

```text
planning -> research -> building -> review -> complete
```

A batch may be marked `complete` only when every package registered in the batch passes the package gates, batch validation passes, the root README is updated, and `git diff --check` is clean.

## 5. Batch validation

Run this after creating or updating a batch record:

```powershell
python tools/validate-expansion-batch.py batches/2026-08-batch-01.yaml
```

The validator checks at least:

- at least one unique package ID is listed and no IDs are duplicated;
- category plan counts match the package list;
- completed batches contain package directories, `package.yaml`, representative images, and bilingual READMEs;
- each completed package records sources, validation status, and its own commit.

The batch record describes work status; it does not duplicate style content. The package directories remain the source of truth for style rules.
