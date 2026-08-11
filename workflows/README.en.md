# Creative workflows

A style package answers “which visual language should the image use?” A creative workflow answers “how should input material become a finished work?” They can be used together, but they have different responsibilities. A workflow must not quietly add a fixed place, person, object, or story, and a style package must not override the workflow's protection of source material.

## Available workflows

| Workflow | Input | Output direction | Keeps source pixels |
| --- | --- | --- | --- |
| [Photo Abstract Editorial](photo-abstract-editorial/README.en.md) | One photo | Photo plus an abstract editorial layout | Yes |
| [Gathered Scenes Zine](gathered-scenes-zine/README.en.md) | One photo | A photo-preserving zine layout or a distilled paper artwork | Variant-dependent |

## How workflows and style packages work together

Compile them in this order:

```text
Input photo
   ↓
Choose a creative workflow
   ↓
Decide whether source pixels remain
   ↓
Choose one independent style package (optional)
   ↓
Project only the package's allowed visual axes
   ↓
Check subject, rights, aspect ratio, and unrequested elements
```

For example, use the photo-preserving variant of Gathered Scenes Zine to establish the layout, then add a print or collage package for the paper surface. You can also use the workflow without any style package. A workflow name is not a style name, and an example subject is not a default generation subject.

## Four ways to use a workflow

1. **Give it to an image-capable Agent**: provide the workflow directory, your photo, and your goal. Ask the Agent to read `workflow.yaml` before compiling the task. Add a style package only when a visual language is needed.
2. **Copy the constraints into a Prompt**: read `purpose`, `allowed_axes`, and the protection rules in `workflow.yaml`; replace only the subject, text, and aspect ratio.
3. **Use an API-capable Agent**: configure your own model API key and let the Agent read the workflow and style package. OhMyStyle does not host models, keys, or generated images.
4. **Use a local model with ComfyUI**: connect the input photo, workflow constraints, reference manifest, and output size to separate local nodes. Keep the subject-protection nodes in place.

## External workflow integrations

OhMyStyle records compatibility with two external projects but does not copy their skills, prompts, examples, or brand assets:

- [Photo Abstract Editorial external project](../integrations/README.en.md#photo-abstract-editorial)
- [Gathered Scenes Zine external project](../integrations/README.en.md#gathered-scenes-zine)

Their licenses are different from OhMyStyle's license. Obtain external materials from the original repositories and follow their terms. The integration records only document provenance, compatibility, and the no-copy boundary.

## Minimum contribution requirements

- Define explicit input, output, variants, and protection rules.
- Keep `subject_policy.default_subjects` empty.
- Treat objects, places, people, and stories as user input or test subjects, never as default workflow content.
- For external projects, record only links and license information.
- Start from [`templates/workflow-package`](../templates/workflow-package) and run `python tools/validate-workflow.py`.
