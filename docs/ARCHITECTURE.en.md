# OhMyStyle art style package architecture

[中文](ARCHITECTURE.md) · [Back to README](../README.en.md)

This guide explains how artistic content is organized and what the current implementation actually executes. See the [art architecture proposal (Chinese)](ART-STYLE-PACK-ARCHITECTURE.md) for research and the [v2 pilot guide (Chinese)](../experiments/style-v2/README.md) for runnable examples.

## 1. What a package describes

An art style package describes visual decisions that can transfer to different subjects: how to construct form, organize values and color, handle edges and materials, and reproduce those relationships through a particular process. The user supplies the subject, count, setting, composition, and purpose separately.

For example, a sunlit oil direction can require reflected color to shape shadows and brushwork to follow turning surfaces. A wooden chair in a courtyard should still express those decisions without acquiring an unrequested beach or boat.

One artist can have several periods, media, or practices; a school can have several teaching methods. A source name identifies the research subject. The package must further define which practice it selects.

| Source category | Scope to declare | Differences to observe |
| --- | --- | --- |
| Artist | Period, medium, selected practice | Relationships between form, light, color, marks, and edges |
| Photographer | Practice, scene conditions, imaging method | Viewpoint, timing, distance, light, and tone |
| Movement | Historical scope and selected branch | Shared formal principles and distinctions from adjacent movements |
| School | Specific course, workshop, or teaching method | Material operations, structural exploration, and design process |
| Technique or medium | Materials, tools, production limits | Marks and forms produced by the process |
| Game art | Representation and technical constraints | Pixel or glyph construction, silhouettes, space, interactive readability |
| Original preset | Authorial intent and choices | Repeatable visual relationships and explicit exclusions |

These are authoring requirements, not a claim that every existing package has already passed this review.

## 2. Five layers of artistic content

**Scope and intent → visual rules → references and counterexamples → production and execution → review across subjects.**

| Layer | Question | Content to retain |
| --- | --- | --- |
| Scope and intent | Which practice and conditions does this direction select? | Medium, period or method, pillars, applicable and incompatible conditions |
| Visual rules | What decisions should the creator make? | Instructions, observable results, failure conditions, importance, rule IDs |
| References and counterexamples | What supports the definition and its distinctions? | Source records, analysis, source/generated distinctions, rights |
| Production and execution | How are the decisions implemented? | Construction sequence, prompts, provider capabilities, deterministic settings |
| Review across subjects | Do the decisions persist and remain distinguishable? | Complete runs, rule reviews, failures, applicability exceptions |

Each rule pairs a creation instruction with an observable result and rejection condition. For example, the [Sorolla pilot](../style-packages/artists/joaquin-sorolla/art-direction.yaml) requires directional daylight and reflected color to explain form; a uniform warm wash does not satisfy it.

Evidence records distinguish institutional descriptions, direct visual observation, curatorial inference, and original design intent. A source link alone does not establish visual validation. `joint_checks` connects several rules so that reflected color, value groups, and brushwork explain the same forms coherently.

## 3. Repository responsibilities

| Location | Responsibility |
| --- | --- |
| `catalog/` | Source entities such as people and institutions |
| `style-packages/<category>/<id>/` | Current independent executable packages |
| `style-packages/composites/` | Recipes assigning different packages to different roles |
| `styles/` | The 110 inherited lightweight presets in their existing format |
| `experiments/style-v2/` | Three manually authored directions outside the formal catalog |
| `tasks/` | A particular subject, composition, aspect ratio, and task constraints |
| `workflows/` | Observation, distillation, and composition of input material |
| `skill/` and root `SKILL.md` | Agent and session interface protocols |
| `schema/` and `tools/` | Contracts, loading, compilation, rendering, and evaluation tools |
| `reports/` | Recorded inventories and implementation results |
| `runs/` | Local jobs and candidates, ignored by Git by default |

Composite recipes assign medium, lighting, color, foreground, or background roles through `stack`, `blend`, or `contrast`. See the [composition guide](../style-packages/composites/README.en.md).

## 4. Current formal packages: multiple artifact files

~~~text
style-packages/<category>/<id>/
├── README.md / README.en.md
├── package.yaml
├── resource.yaml
├── identity.yaml
├── visual-signature.yaml
├── reproduction.yaml
├── relations.yaml
├── palette/palette.json
├── prompts/base.txt / negative.txt / variations.txt
├── references/manifest.csv
├── provenance.yaml
├── evaluation.yaml
├── gallery-16x9.jpg
└── examples/accepted / generated / rejected
~~~

| Artifact | Content |
| --- | --- |
| `package.yaml` | Package ID, version, classification, artifact entry points |
| `resource.yaml` | Resource type, maturity, dimensions, evidence declarations |
| `identity.yaml` | Interpretation, scope, open subject policy, exclusions |
| `visual-signature.yaml` | Composition, lighting, color, marks, material behavior |
| `reproduction.yaml` | Production sequence and technical constraints |
| `relations.yaml` | Neighboring directions and distinctions |
| `palette/palette.json` | Color roles and values, or optional palette pairs |
| `prompts/` | Base and negative text used by the current compiler, plus other prompt artifacts |
| Reference manifest and provenance | Sources, analytical roles, rights boundaries |
| Evaluation and examples | Criteria, candidates, accepted or rejected examples |

`package.yaml` may optionally declare `files.art_direction` to register new
rules as a package artifact. Registration alone does not change legacy
compilation; callers must explicitly pass `--direction package`. Packages
without this field require no conversion and retain their current path. This
allows gradual adoption while preserving old files for compatibility and
retrieval.

See the [package specification](STYLE-PACKAGE-SPEC.md) and [resource architecture](RESOURCE-ARCHITECTURE.md) for the detailed contracts.

### Loading a file does not mean compiling all of its content

The legacy compiler loads the package artifacts, but its final prompts primarily use `prompts/base.txt`, `prompts/negative.txt`, and the selected palette pair. It **does not automatically expand all visual signature rules into prompt instructions**. `prompts/variations.txt` is not an automatic input to this compilation path either.

Retrieval flattens visual signature content into search terms. An Agent reading files directly may use additional rules. Retrieval, direct Agent reading, and compiled model input therefore need separate inspection. Save the actual prompts and input assets submitted to the model; editing a YAML file alone does not establish an execution change.

## 5. v2 pilots: explicitly selected directions

v2 keeps the formal package and registers an optional `art_direction` artifact. A direction may live in an experiment folder until it is ready to register. Sorolla, Bauhaus, ASCII, and Van Gogh now register optional experimental directions in their formal packages. The library is not automatically converted.

| Field | Responsibility |
| --- | --- |
| `base_package` | Explicitly selected formal package identity and source records |
| `scope`, `pillars` | Medium, representation, limits, editorial intent |
| `rules` | Identified instructions, observable results, failure conditions, evidence |
| `active_rule_ids` | Authored selection, including every core rule |
| `joint_checks` | Requirements connecting multiple active rules |
| `sources` | Base source IDs, institutional links, local source artifacts, original requirements |
| `execution` | Route, mandatory requirements, exclusions |

The contract is [art-direction.schema.json](../schema/art-direction.schema.json); the compiler is [art_direction_runtime.py](../tools/art_direction_runtime.py).

The compiled job separates four kinds of information:

- **Positive prompt:** user subject and details, medium, representation, active rule instructions, joint instructions, production requirements.
- **Negative prompt:** explicitly authored rule and execution `avoid` text.
- **Review:** scope, rule text, observable results, rejection conditions, sources.
- **Traceability:** direction path and SHA-256, active rule IDs, declared contexts.

`applies_when` is a natural language authoring note. The implementation checks caller-declared required and incompatible contexts; it does not infer applicability from the subject or select rules automatically. Research sources are not automatically supplied as reference images.

This stage supports `profile=generic` and `references=none`, without legacy palette pairs. HTTP/MCP sessions and composite compilation retain the legacy path. Enable v2 explicitly through CLI `--direction` or Python `direction_path`. Directions may live in the experiment directory, or be registered through `package.yaml` `files.art_direction` and selected with `--direction package`.

Compile the same package in both modes to inspect prompts and rule metadata.
With reference images disabled in both jobs:

~~~powershell
python tools/compile-style.py style-packages/artists/joaquin-sorolla --subject "A wooden chair in a plain courtyard in afternoon daylight, no people, water, or coast" --references none --output runs/compare/sorolla-legacy.json
python tools/compile-style.py style-packages/artists/joaquin-sorolla --direction package --context daylight --subject "A wooden chair in a plain courtyard in afternoon daylight, no people, water, or coast" --output runs/compare/sorolla-direction.json
~~~

Compare `prompt`, `negative_prompt`, and `review.rules` individually. This
checks compilation inputs, not image quality; the two formats need not produce
the same prompt wording.

| Pilot | Main relationships | Route |
| --- | --- | --- |
| [Sorolla sunlit oil](../style-packages/artists/joaquin-sorolla/art-direction.yaml) | Daylight, reflected color, value groups, directional marks | `text_only`, declare `daylight` |
| [Bauhaus paper method](../style-packages/schools/bauhaus/art-direction.yaml) | Cutting, tearing, folding, supports, openings, shadows | `text_only`, declare `paper-study` |
| [Literal ASCII grid](../style-packages/game-art/ascii-character-game-art/art-direction.yaml) | Real glyphs, fixed cells, density, negative space | `deterministic_grid` |
| [Van Gogh directional strokes](../style-packages/artists/vincent-van-gogh/art-direction.yaml) | Surface-following marks, local cool-warm relationships, visible impasto | `text_only` |
| [Morandi quiet tonality](../style-packages/artists/giorgio-morandi/art-direction.yaml) | Close values, measured intervals, shallow space, selective soft edges | `text_only` |
| [Hopper architectural light](../style-packages/artists/edward-hopper/art-direction.yaml) | Everyday architectural planes, directional shadows, spatial distance | `text_only` |
| [Agnes Martin hand-drawn grid](../style-packages/artists/agnes-martin/art-direction.yaml) | Nonfigurative fine grid, subdued field, hand-made variation | `text_only`, declare `abstract-field` |
| [Caravaggio embodied chiaroscuro](../style-packages/artists/caravaggio/art-direction.yaml) | Close staging, single-source chiaroscuro, tactile realism | `text_only` |
| [Hiroshige atmospheric landscape](../style-packages/artists/utagawa-hiroshige/art-direction.yaml) | Weather layers, cropped foreground, travel scale, woodblock gradation | `text_only`, declare `landscape-view` |
| [Hokusai graphic contour and planes](../style-packages/artists/katsushika-hokusai/art-direction.yaml) | Silhouette hierarchy, registered color planes, deliberate crop, paper-shaped negative space | `text_only` |
| [Friedrich human scale and vastness](../style-packages/artists/caspar-david-friedrich/art-direction.yaml) | Open space, finite human scale, selective visibility of distance | `text_only`, declare `landscape-view` |
| [O'Keeffe close observation and form](../style-packages/artists/georgia-okeeffe/art-direction.yaml) | Enlarged user-selected form, simplified color shapes, form-following negative space | `text_only`, declare `close-observation` |
| [Riley serial rhythm and perceptual motion](../style-packages/artists/bridget-riley/art-direction.yaml) | Geometric progression, adjacent contrast, flat-plane optical movement | `text_only`, declare `abstract-field` |
| [Dürer engraved line and value structure](../style-packages/artists/albrecht-durer/art-direction.yaml) | Contour first, form-following hatch, paper highlights, material-specific line groups | `text_only` |
| [Mucha ornamental poster hierarchy](../style-packages/artists/alphonse-mucha/art-direction.yaml) | Subject-to-frame hierarchy, contour-linked curves, flat lithographic color, user-controlled text | `text_only`, declare `ornamental-poster` |
| [Anna Ancher domestic window light](../style-packages/artists/anna-ancher/art-direction.yaml) | One window-light path, reflected color across room planes, ordinary domestic scale | `text_only`, declare `window-lit-interior` |
| [Artemisia embodied action composition](../style-packages/artists/artemisia-gentileschi/art-direction.yaml) | Countering diagonals, close action staging, local color retained in shadow | `text_only`, declare `figure-action` |
| [Beardsley ink mass and negative space](../style-packages/artists/aubrey-beardsley/art-direction.yaml) | Black-white positive and negative shapes, calligraphic contour, selective focal detail | `text_only`, declare `black-and-white-ink-illustration` |
| [Morisot gesture and open-edge painting](../style-packages/artists/berthe-morisot/art-direction.yaml) | Gesture-led strokes, selective released edges, visible ground, variable finish density | `text_only`, declare `open-brush-figure-painting` |
| [Rivera public narrative registers](../style-packages/artists/diego-rivera/art-direction.yaml) | Connected narrative registers, shared scale for people and environment, distance-readable color planes | `text_only`, declare `public-narrative-mural` |
| [Velázquez gaze, depth, and selective precision](../style-packages/artists/diego-velazquez/art-direction.yaml) | Gaze organizes group relationships, dark values create room depth, focal details against broad passages | `text_only`, declare `observed-interior-portrait` |
| [Degas oblique observation and spatial crop](../style-packages/artists/edgar-degas/art-direction.yaml) | Oblique viewpoint, asymmetric framing, spatial planes, and legible transitional poses | `text_only`, declare `observed-figure-scene` |
| [Schiele contour tension and exposed ground](../style-packages/artists/egon-schiele/art-direction.yaml) | Directional contour, tension between form and paper ground, sparse dry color | `text_only`, declare `expressive-contour-study` |
| [Munch subjective color and environmental rhythm](../style-packages/artists/edvard-munch/art-direction.yaml) | Local psychological color, curves linking subject and setting, selective spatial compression | `text_only`, declare `psychological-expressionist-scene` |
| [Lissitzky Proun axonometric space](../style-packages/artists/el-lissitzky/art-direction.yaml) | Planes and volumes in shared space, coherent axonometric relations, color as spatial cue | `text_only`, declare `pictorial-architectonic-space` |
| [El Greco vertical lift and flickering form](../style-packages/artists/el-greco/art-direction.yaml) | Selective elongation, staged upward composition, local color contrast and brush rhythm | `text_only`, declare `vertical-lift-composition` |
| [Kahlo frontal presence and personal symbolic relations](../style-packages/artists/frida-kahlo/art-direction.yaml) | Frontal portrait presence, shallow space, relationships among user-specified objects | `text_only`, declare `intimate-symbolic-portrait` |
| [Cassatt figure and decorative plane](../style-packages/artists/mary-cassatt/art-direction.yaml) | Modeled figure against flatter pattern, decorative color planes, scene-led viewpoint | `text_only`, declare `patterned-domestic-figure-scene` |
| [Turner weather, light, and motion](../style-packages/artists/jmw-turner/art-direction.yaml) | Graduated atmospheric depth, layered warm-cool light, one legible movement vector | `text_only`, declare `atmospheric-weather-motion` |
| [Goya psychological portrait and selective brushwork](../style-packages/artists/francisco-goya/art-direction.yaml) | Expression and posture, contrasting mark scale, restrained value separation | `text_only`, declare `psychological-portrait` |
| [Wood regional landscape pattern and vertical rhythm](../style-packages/artists/grant-wood/art-direction.yaml) | Rolling land with upright forms, path-led composition, controlled regional detail | `text_only`, declare `composed-regional-landscape` |
| [Manet direct color and compressed scene](../style-packages/artists/edouard-manet/art-direction.yaml) | Adjacent color patches, deliberate spatial compression, selective contours and brushwork | `text_only`, declare `modern-life-color-plane` |
| [Delacroix chromatic motion and brushwork](../style-packages/artists/eugene-delacroix/art-direction.yaml) | Warm-cool interaction, legible action vector, material-sensitive brush rhythm | `text_only`, declare `chromatic-dynamic-scene` |
| [Bacon enclosed space and localized distortion](../style-packages/artists/francis-bacon/art-direction.yaml) | Frame-compressed space, localized contour shift, visible overpaint and scrape layers | `text_only`, declare `enclosed-figurative-tension` |
| [Zurbarán ordered still life and focused side light](../style-packages/artists/francisco-de-zurbaran/art-direction.yaml) | Spacing of user-specified objects, single lateral light, restrained ground, and material distinction | `text_only`, declare `ordered-object-still-life` |
| [Richter layered veil and squeegee erasure](../style-packages/artists/gerhard-richter/art-direction.yaml) | Preserve recognition anchors while directional dragging and selective layer removal shift between image and abstraction | `text_only`, declare `layered-image-veil` |
| [de Chirico measured void, spatial dislocation, and geometric shadows](../style-packages/artists/giorgio-de-chirico/art-direction.yaml) | Quiet negative space, one bounded perspective mismatch, and long shadows create a readable spatial enigma | `text_only`, declare `metaphysical-spatial-enigma` |
| [Klimt modeled figure and ornamental field](../style-packages/artists/gustav-klimt/art-direction.yaml) | Legible modeled figure beside region-specific flat ornament and selective metallic surface | `text_only`, declare `modeled-figure-ornamental-field` |
| [Moreau symbolic line, jewel-like color, and enigma](../style-packages/artists/gustave-moreau/art-direction.yaml) | Precise arabesque line, jewel-like planes, and selective detail create imaginative mystery around a legible subject | `text_only`, declare `symbolic-line-color-enigma` |
| [Matisse cut-paper color construction](../style-packages/artists/henri-matisse/art-direction.yaml) | Opaque flat shapes, crisp cut-like edges, and intentional negative space create a lively visual rhythm | `text_only`, declare `cut-paper-color-construction` |
| [af Klint axial spiral and biomorphic order](../style-packages/artists/hilma-af-klint/art-direction.yaml) | One axis and bounded cyclical geometry link geometric and biomorphic forms within matte color fields | `text_only`, declare `axial-symbolic-abstraction` |
| [Rousseau flat space and crisp natural detail](../style-packages/artists/henri-rousseau/art-direction.yaml) | Clear contours, bounded color, overlapping planes, and diffuse light without default jungle subject matter | `text_only`, declare `flat-space-natural-detail` |
| [Courbet tactile matter and grounded scale](../style-packages/artists/gustave-courbet/art-direction.yaml) | Unidealized subject, material-congruent impasto, and weight-bearing ground | `text_only`, declare `tactile-material-realism` |
| [Seurat measured composition and divided-color marks](../style-packages/artists/georges-seurat/art-direction.yaml) | Stable silhouettes, deliberate intervals, plane-sensitive separated marks, and optical light | `text_only`, declare `measured-chromatic-composition` |
| [Aivazovsky radiant sea light and wave direction](../style-packages/artists/ivan-aivazovsky/art-direction.yaml) | Broken reflection path, direction-sensitive water marks, and atmospheric sea-sky depth | `text_only`, declare `radiant-sea-light-path` |
| [Van Eyck glazing and material-specific light](../style-packages/artists/jan-van-eyck/art-direction.yaml) | Distinct material highlights under shared light, selective translucent layers, and localized detail | `text_only`, declare `glazed-material-observation` |
| [Ingres contour-led figure study](../style-packages/artists/jean-auguste-dominique-ingres/art-direction.yaml) | Supple contours organize pose, restrained smooth modeling, and shallow quiet space | `text_only`, declare `contour-led-figure-study` |
| [Basquiat user-authored text and mark hierarchy](../style-packages/artists/jean-michel-basquiat/art-direction.yaml) | Organizes only user-supplied words and symbols; localizes strike-through and preserves legibility | `text_only`, declare `user-authored-mark-hierarchy` |
| [Miró suspended biomorphic forms and open color field](../style-packages/artists/joan-miro/art-direction.yaml) | Keeps curve and color forms distinct, balanced by asymmetric spacing and negative space | `text_only`, declare `suspended-biomorphic-sign-field` |
| [Mitchell counterposed color-stroke groups](../style-packages/artists/joan-mitchell/art-direction.yaml) | Directional groups vary paint weight and color, creating counter-rhythm with open-ground pauses | `text_only`, declare `counterposed-color-stroke-groups` |
| [Vermeer quiet cityscape with banded depth](../style-packages/artists/johannes-vermeer/art-direction.yaml) | User-requested cityscapes organized by horizontal zones, light-dark depth, and sparse reflections | `text_only`, declare `quiet-cityscape-banded-depth` |
| [Kollwitz compressed figure-group print](../style-packages/artists/kathe-kollwitz/art-direction.yaml) | User-specified group action organized around its contact point with bold masses and paper-white cuts; no inferred relationship or story | `text_only`, declare `compressed-figure-group-print` |
| [Malevich diagonal drift and counterweight](../style-packages/artists/kazimir-malevich/art-direction.yaml) | Geometric planes move along an off-center diagonal and counterbalance through scale and uneven intervals | `text_only`, declare `diagonal-drift-counterweight` |
| [Leonardo layered hand-mechanics study](../style-packages/artists/leonardo-da-vinci/art-direction.yaml) | Comparative hand views, aligned wrist and joint axes, and separated surface and skeletal structures | `text_only`, declare `layered-hand-mechanics-study` |
| [Carrington three-state material metamorphosis](../style-packages/artists/leonora-carrington/art-direction.yaml) | User-requested source, transition, and changed forms with detail focused at the transformation | `text_only`, declare `three-state-material-metamorphosis` |
| [Bourgeois visible textile mending](../style-packages/artists/louise-bourgeois/art-direction.yaml) | Stitches cross actual joins, with repair and textile relief focused at connections | `text_only`, declare `visible-mending-textile-assembly` |
| [Chagall floating pair with chromatic echo](../style-packages/artists/marc-chagall/art-direction.yaml) | Two unequal forms float along a loose diagonal and share a small repeating accent hue | `text_only`, declare `chromatic-echo-floating-pair` |
| [Escher single impossible junction](../style-packages/artists/mc-escher/art-direction.yaml) | A user-specified object has one localized perspective contradiction while its remaining structure stays readable | `text_only`, declare `single-impossible-junction` |
| [Michelangelo counterturned weight-bearing figure](../style-packages/artists/michelangelo-buonarroti/art-direction.yaml) | One standing figure is anchored by a weight-bearing leg, with a controlled opposing turn through pelvis and shoulders | `text_only`, declare `counterturned-weight-bearing-figure` |
| [Moholy-Nagy transparent-plane shadow study](../style-packages/artists/moholy-nagy/art-direction.yaml) | One translucent plane, one directional light, and one principal cast shadow form a sparse optical relation | `text_only`, declare `photogram-shadow-study` |
| [Nicolas de Staël performance gesture blocks](../style-packages/artists/nicolas-de-stael/art-direction.yaml) | User-requested dancers or musicians become a few angled color masses with sparse action cues | `text_only`, declare `dance-or-music-performance` |
| [Rockwell reaction chain around a shared prop](../style-packages/artists/norman-rockwell/art-direction.yaml) | A single shared event links a small group through one initiating gesture and differentiated reactions | `text_only`, declare `reaction-chain-around-shared-prop` |
| [Picasso single object in multiple viewpoints](../style-packages/artists/pablo-picasso/art-direction.yaml) | Front, side, or top views meet within one recognizable object silhouette while the surrounding space stays quiet | `text_only`, declare `single-object-multiple-viewpoints` |
| [Cézanne tilted tabletop object balance](../style-packages/artists/paul-cezanne/art-direction.yaml) | Tilt the requested support plane and balance user-specified objects through contact and color relationships | `text_only`, declare `tilted-tabletop-still-life` |
| [Gauguin outlined figure and selective ground texture](../style-packages/artists/paul-gauguin/art-direction.yaml) | A user-specified figure uses a continuous contour and flat color while one limited ground patch has looser surface handling | `text_only`, declare `single-figure-flat-ground` |

## 6. Execution routes

~~~mermaid
flowchart TD
    A[User subject and details] --> B[Legacy package compiler]
    P[Formal package] --> B
    A --> C[Explicit v2 direction]
    P --> C
    D[direction.yaml] --> C
    B --> E[Image job and actual prompts]
    C --> F{Production route}
    F -->|text_only| E
    E --> G[External image model]
    F -->|deterministic_grid| H[Human or text model authors glyph source]
    H --> I[Fixed cells and explicit monospace font]
    G --> J[Subject, medium and rule review]
    I --> J
~~~

`text_only` means no reference images in this stage. Compilation creates a job; users select and configure the actual image model.

ASCII requires literal source text before rasterization. The renderer draws only a uniform background and individual glyphs. It rejects non-ASCII input, wrong row counts, excessive line widths, blank scenes, and unsuitable fonts or cell sizes. It outputs a lossless PNG, normalized source grid, and a record with source, font, environment, and pixel hashes. A new subject does not automatically rewrite an existing source grid. An image model's approximate character painting does not satisfy this route.

See the [pilot commands (Chinese)](../experiments/style-v2/README.md) and [Skill interface guide](../skill/README.en.md).

## 7. Quality and differentiation

Review the requested subject, count, layout, and exclusions first; then check medium and production constraints. Review applicable core rules, supporting rules, and joint relationships separately. Preserve failures and use multiple subjects and repeated outputs to inspect stability.

Compare specific visual relationships with neighboring artists, movements, or school methods. Names and textual similarity alone do not establish artistic differentiation. Hold the subject, model version, aspect ratio, and generation settings constant across name-only, legacy-package, and new-rule arms. The initial phase excludes research images. See the [comparison protocol](design/art-style-pack-v2/comparison-plan.yaml).

The existing maturity contract is L0 descriptor, L1 structured description, L2 reference-backed executable package, L3 accepted generation and review evidence, and L4 interoperability evidence across providers or adapters. Existing maturity does not establish validation of newly authored v2 rules.

The initial three pilots remain `experimental` with review `pending`; directions registered since then also remain experimental. Jobs have been compiled and a literal ASCII source rasterized. Illustrative previews are not provider-backed comparison evidence, and maturity has not been upgraded. See the [initial implementation record](../reports/style-v2-implementation.json).

## 8. Versions and migration

The preserved baseline is branch `codex/style-v1-preserved` and tag `style-v1-snapshot-2026-10-18` at commit `59d9aa10ee9eeaedf3b815688d00f3e553ef31ea`. The implementation started on `codex/style-pack-v2` and is now included in `main`. Continue development on `main`; retain the old baseline for comparison. The formal library has not been bulk migrated.

Proceed through manual direction authoring, saved compiled inputs, comparison runs, rule reviews, and a decision on wider adoption. Scripts handle structure, references, and records; artistic interpretation and differences require research and review. See the [migration assessment (Chinese)](ART-STYLE-MIGRATION-ASSESSMENT.md) and [baseline worktree instructions (Chinese)](../experiments/style-v2/README.md#版本保留与回退).
