# Francis Bacon

[中文说明](README.md)

![Francis Bacon representative image](gallery-16x9.jpg)

> **Category:** Artist  
> **Medium:** 20th-century modern figurative oil painting  
> **Directory:** `style-packages/artists/francis-bacon`

## Overview

Francis Bacon often begins with a recognizable form, then changes the stability of the image through compressed space, displaced contours, overpainting, and scraping. Architectural frames can remain hard while the edge of a figure or object appears dragged through time. This package transfers that tension, color conflict, and visible painting process without making portraits, screaming faces, or flesh imagery default content.

## Curatorial note

What I enjoy here is the feeling that the structure remains while safety has disappeared. Unease does not come from piling on detail; it comes from shifting an ordinary chair, wall, or object slightly in proportion and space. Keep the subject recognizable first, then decide where it needs to be erased or pulled. Starting with random distortion usually makes the image weightless.

## Subject independence

This package controls compressed space, local distortion, color-field conflict, and oil-paint process. It does not prescribe a person, portrait, crucifix, arena, flesh, or story. The chair and interior in the representative image are only benchmark subjects.

## Sources and rights

The research entry is the [Museum of Modern Art Francis Bacon archive](https://www.moma.org/artists/272-francis-bacon). The repository does not bundle external artworks. The representative image is a newly generated anonymous scene, not a reproduction of a specific work and not an endorsement or collaboration.

## New architecture: enclosed space and localized contour shift (experimental)

[`art-direction.yaml`](art-direction.yaml) uses direction format 2.1.0 and is enabled only when the user declares `enclosed-figurative-tension`. It compresses space around a user-supplied subject with a simple frame and shifts contours in a few places while requiring the subject to stay recognizable. Visible overpainting and scraping activate only when the caller declares `visibly-expressive-oil-surface-requested`.

This differs from Goya's direction, which shapes psychological presence through expression, facial detail, and dark-ground brushwork. Bacon's direction centers the relation between an enclosing spatial frame and localized contour shifts. It does not automatically add a person, screaming, violence, a cross, or an arena.

```powershell
python tools/compile-style.py style-packages/artists/francis-bacon --direction package --context enclosed-figurative-tension --subject "A ceramicist holding a clay bowl beside a tall wooden frame in a quiet studio" --output runs/style-v2/francis-bacon-job.json
```

This direction remains experimental; same-subject and cross-subject visual review is pending.

## Use this package only

### Method 1: Give it to an image-capable Agent

Give this directory to an Agent. Ask it to read `identity.yaml`, `visual-signature.yaml`, `reproduction.yaml`, `prompts/`, `palette/palette.json`, and `evaluation.yaml`, then compile your subject, aspect ratio, and purpose. Review subject legibility, whether distortions have structural reasons, and whether a fixed motif has appeared.

### Method 2: Copy the Prompt directly

Open `prompts/base.txt`, replace `{{SUBJECT}}`, `{{ASPECT_RATIO}}`, and `{{USE_CASE}}`, and submit `prompts/negative.txt` as well on platforms that support negative prompts.

### Method 3: Configure an API key and submit

Configure an API key in your own image service or compiler, then submit the base prompt, negative constraints, and palette. This repository does not host keys or an online image service.

### Method 4: Local model + ComfyUI

Connect the prompts, palette, and reproduction notes to a local model or ComfyUI workflow. Use `evaluation.yaml` for review; do not treat the chair or interior in the representative image as a default subject.

## Legacy and direction comparison

See [the actual legacy and direction outputs, compiled prompts, and review notes](comparisons/README.md).
