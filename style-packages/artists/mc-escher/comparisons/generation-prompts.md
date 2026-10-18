# Generation prompts and review

Both images were generated with the built-in OpenAI image generation tool on 2026-10-19. The same chair-and-side-table subject was used for both; only the active package direction and its compiled execution constraints differed. They are generated demonstrations, not outputs from an external art model and not source artworks.

## Legacy prompt

Create a new anonymous horizontal 16:9 printmaking illustration for a visual-comparison test. SUBJECT: one plain wooden dining chair beside one small square side table, standing on a simple floor against an empty wall. Use only those two objects; no people, animals, stairs, towers, windows, or writing. Apply restrained monochrome woodcut / lithograph language: ivory paper, black engraved contour, measured directional hatching, crisp plane boundaries. Preserve recognizable object silhouettes and an ordinary quiet interior. Use the base package's broad spatial play: allow a subtle optical inconsistency somewhere in the overall arrangement, but do not copy a known Escher composition or use a famous motif. Keep graphic, finely printed, no photorealism, no text, no logo, no watermark.

## Optional direction prompt

Create a new anonymous horizontal 16:9 printmaking illustration for a visual-comparison test. SUBJECT: exactly one plain wooden dining chair beside exactly one small square side table, standing on a simple floor against an empty wall. Keep chair and table recognizable and preserve their ordinary functions. Use restrained monochrome woodcut / lithograph language: ivory paper, black engraved contour, measured directional hatching, crisp plane boundaries. Follow the optional art direction 'single impossible junction': all floor, wall, table, and chair connections remain coherent in one ordinary perspective system EXCEPT exactly one bounded join where the front-right chair leg meets its seat; at that one joint, make the edge order/depth connection visibly contradict itself. Keep the paradox small, local, and inspectable. Do not introduce any other impossible lines or forms. No people, animals, stairs, towers, windows, tessellation, metamorphosis, famous Escher motif, text, logo, watermark, glossy CGI, or photorealism.

## Review

- Both images keep the two requested furniture objects recognizable and use a restrained monochrome printed line style.
- The optional-direction image puts a small edge-order ambiguity at the seat/front-right leg junction; the rest of the furniture and room remain coherent enough to read.
- The difference is modest. This is consistent with the intentionally local rule, but the image generator does not provide a mathematically verifiable perspective construction.
- Do not treat this pair as proof that the model will always isolate the contradiction to one joint. For exact geometry, use a deterministic vector or 3D construction and review the requested joint directly.
- No external artwork was used as an image input. Institutional context is recorded in `provenance.yaml`; the generated pair is a new anonymous scene.
