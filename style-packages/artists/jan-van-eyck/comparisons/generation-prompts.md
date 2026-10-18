# Generation prompts

Both calls requested the same objects, setting, and 16:9 landscape framing. They were generated separately without a fixed random seed or shared latent state.

## Legacy package

> Create a 16:9 landscape oil painting of exactly these three objects: a small green glass bottle, a folded cream linen cloth, and a tarnished brass key on a pale wooden tabletop, softly lit by a nearby window. No other objects, no mirror, no person, no writing, no border, no watermark. Legacy package treatment: quiet Northern Renaissance-inspired oil painting, carefully observed object shapes, deep but restrained color, fine detail across the still life, natural window light, polished glass and metal reflections, textured linen and wood. Keep a simple independent composition and do not imitate any named painting.

## `glazed-material-observation`

> Create a 16:9 landscape oil painting of exactly the same three objects and setting: a small green glass bottle, a folded cream linen cloth, and a tarnished brass key on a pale wooden tabletop, softly lit by a nearby window. No other objects, no mirror, no person, no writing, no border, no watermark. Apply the material-observation direction: distinguish the green glass with restrained transparency and a narrow controlled highlight; show the brass key with a few small warm reflected accents, not a mirror-like shine; render the folded linen with broad soft transitions and selective light-catching folds; let the wood have quiet grain and low sheen. Use subtle translucent color layers to deepen selected greens and shadows while preserving local colors. Keep fine marks localized to edges, folds, and light catches; leave secondary planes calm. Keep the single soft window light and exact object count. New independent composition, no imitation of a named painting.

Generated files are `legacy.png` and `direction.png`, each 1672 × 941 pixels (approximately 16:9).
