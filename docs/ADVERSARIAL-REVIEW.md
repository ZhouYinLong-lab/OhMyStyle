# Adversarial Review of the Render Workflow

## Findings

| Risk | Attack | Consequence | Fix |
| --- | --- | --- | --- |
| High | Give exact HEX/L* constraints directly to a stochastic image model | The model improves visual separation by changing exposure and violates the measurable requirement | Preflight selects a hybrid strategy and requires deterministic color/mask post-processing |
| High | Generate first and evaluate afterward | Failures consume a full generation attempt and encourage blind retries | `preflight-render.py` blocks generation until the execution plan is valid |
| Medium | Treat a fuzzy brief as a single long prompt | Product scale, safe crop, title space, and clothing detail compete silently | Render task stores product bounds, safe zones, target aspects, and review gates |
| Medium | Use a style package without recording selected references | A later run cannot prove which palette card or work image was used | Compiled jobs and run records include explicit reference paths and SHA-256 image hashes |
| Low | Call a metric a proof of artistic quality | A color pass can still be semantically or aesthetically wrong | Keep automated checks as screening gates and require human review after measurement |

## New operating rule

The system must choose the rendering strategy before a model call:

- `hybrid_model_plus_deterministic_postprocess` for exact colors, uniform
  backgrounds, equal-lightness constraints, and other measurable pixel rules;
- `model_first_with_layout_guard` for ambiguous art direction where the main
  risk is interpretation, crop safety, product scale, or mood.

For the first strategy, `tools/recolor-lab.py` is the deterministic correction
stage. It requires explicit masks so the system never silently recolors skin,
hair, glass, or reflections.

Retries are no longer the default recovery mechanism. A failed hard gate means
the task needs a better deterministic stage or a revised task specification.
