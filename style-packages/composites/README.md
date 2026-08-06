# Cross-style composite recipes

Each folder in this directory is a small, data-only recipe that references
existing executable style packages. It does not copy their prompts or assets.
The normal package runtime remains independent from this layer; a composite is
compiled only when the user explicitly requests several style bases together.

## Three modes

- `stack`: assign each base a different role, such as `medium`, `lighting`, or
  `composition`. Each role remains authoritative in its own dimension.
- `blend`: merge compatible bases within a shared dimension using normalized
  `weight` values. This is useful for two palette or two lighting signatures.
- `contrast`: assign each base to an explicit `zone`, such as `foreground` and
  `background`. Zone boundaries prevent a medium or surface rule from leaking
  across the whole image.

When `mode` is omitted, the runtime infers it in this order: explicit zones
become `contrast`; repeated roles or blend hints become `blend`; otherwise the
recipe defaults to `stack`. `auto.default_mode` can provide a deliberate
fallback, while `auto.hints` can make the intent explicit.

## Recipe fields

`bases[].package` is a relative path under `style-packages/`. `role` describes
the style dimension being contributed. `weight` is used by `blend` and is
normalized at compile time. `zone` is required by `contrast`. `capabilities`
and `incompatibilities` provide machine-readable conflict checks. `overrides`,
`constraints.must`, `constraints.avoid`, and `conflicts.policy` make the final
composition auditable instead of silently concatenating prompts.

The compiler accepts `fail`, `warn`, or `resolve` conflict policies. A `fail`
policy stops before prompt generation; `warn` records the conflict in the
compiled job; `resolve` records the requested resolution rules for a future
provider adapter. No style-specific branch is hard-coded in the runtime.
