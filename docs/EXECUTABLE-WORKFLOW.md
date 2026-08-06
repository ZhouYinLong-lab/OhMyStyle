# Executable Style Package Workflow

Style Packages are now intended to be executable specifications, not prompt
collections. The local workflow has four stages:

```text
package data -> compile-style.py -> provider-neutral job -> model adapter
                                      -> generated image
                                     -> evaluate-render.py -> human review
```

Install the local validation dependencies with:

```bash
python -m pip install -r requirements-dev.txt
```

## 1. Compile a job

```bash
python tools/compile-style.py \
  style-packages/presets/high-chroma-color-pairing \
  --subject "a ceramic chair in a quiet studio" \
  --pair cobalt-warm-yellow \
  --profile weak \
  --references palette \
  --output tmp/chair-job.json
```

The compiler reads the package palette, reproduction rules, prompt files, and
the manifest. It returns the exact local reference paths selected for the job.
For the contrast-color package, the default reference is the matching color
card; floral references are not silently passed as subject templates.

`--profile weak` emits shorter, explicit object/color assignments for models
that perform poorly with abstract art-direction language. The output is
provider-neutral so an adapter can map it to an image API, a local UI, or a
manual workflow.

## 2. Evaluate a render

```bash
python tools/evaluate-render.py \
  style-packages/presets/high-chroma-color-pairing \
  path/to/render.png \
  --pair cobalt-warm-yellow \
  --profile same-luminance
```

The baseline evaluator uses Pillow and does not require a model. It reports
pair coverage, dominant/counter area share, approximate luminance, luminance
delta, edge variation, and unassigned high-chroma pixels. When a package gives
parseable area ranges, the dominant/counter area ratio is also a hard check.
These are screening
signals, not semantic proof; human review remains required for object identity,
material realism, and overall visual quality.

The package currently has explicit profiles for `default`, `flat-poster`, and
`same-luminance`. This prevents a visually attractive but technically invalid
render from being treated as a successful reproduction.

For a task with colors that are not part of the package palette, use explicit
HEX overrides and a CIELAB threshold:

```bash
python tools/evaluate-render.py \
  style-packages/presets/high-chroma-color-pairing \
  path/to/portrait.png \
  --profile same-luminance \
  --dominant-hex 0070FC \
  --counter-hex C85400 \
  --max-lstar-delta 2
```

The evaluator reports both normalized luminance and CIELAB `L*`; the latter is
the gate to use for equal-lightness tests. A visually improved render can still
remain rejected when the measured `L*` difference is too large.

For hard-color tasks, the preflight plan may require deterministic correction
after a mask is available:

```bash
python tools/recolor-lab.py input.png output.png \
  --mask shirt-mask.png \
  --target-hex 0070FC \
  --texture-strength 0.12
```

The tool changes only the masked region, locks its hue/chroma to the target,
and keeps low-amplitude texture around the target L*. Background regions can be
processed with `--texture-strength 0` for a uniform fill. A mask must be
explicit; automatic recoloring without a region boundary is unsafe for faces,
hair, skin, and reflective materials.

## 3. Record a run

```bash
python tools/record-run.py \
  style-packages/presets/high-chroma-color-pairing \
  path/to/render.png \
  --pair cobalt-warm-yellow \
  --profile default \
  --status pending \
  --notes "Review color separation and material fidelity"
```

Run manifests are written under the ignored local `runs/` directory. They keep
the package, image hash, evaluation output, and human review status together.
Use `--copy-image` only when a local run archive is useful; accepted examples
still require explicit approval before entering a package directory.

## Model adapter contract

An adapter should accept the compiled JSON and preserve four things:

1. the exact subject;
2. the compiled color assignment;
3. the selected reference images and their declared usage;
4. the negative prompt and hard constraints.

The adapter may shorten or reorder language for a provider, but it must not
silently remove a hard constraint. Provider-specific API calls are intentionally
not part of the baseline tools so the repository remains usable with strong,
weak, local, and hosted models.
