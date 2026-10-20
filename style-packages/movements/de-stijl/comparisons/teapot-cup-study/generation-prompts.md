# Generation prompts used for the De Stijl comparison

The two prompts below are the actual prompts passed to the built-in image generation tool. Calls were independent, used no reference images, and requested one 16:9 landscape view each.

## Legacy package arm

```text
Create one landscape 16:9 image. User subject: 横版 16:9，一只白色陶瓷茶壶和一只茶杯并排放在普通桌面上，背景简洁，无文字。 Apply the legacy De Stijl package prompt: an original modernist rectangular composition, black horizontal and vertical structural lines dividing white space, a small number of red, blue, and yellow rectangular color fields, asymmetrical architectural balance and clear negative space. Keep the teapot and cup recognizable as the only objects. Do not add diagonal forms, gradients, realistic cast shadows, ornament, plastic 3D appearance, readable text, logo, or a copy of any canonical De Stijl artwork. Single image, not a comparison panel.
```

## Structured direction arm

```text
Create one landscape 16:9 image, one single view. USER SUBJECT: 横版 16:9，一只白色陶瓷茶壶和一只茶杯并排放在普通桌面上，背景简洁，无文字。 Keep exactly one white ceramic teapot and one white ceramic teacup as recognizable requested objects; keep the background simple and add no other props. Apply these structured De Stijl direction rules as visual treatment only: represent the objects with clear orthogonal relations and flat color planes; build asymmetrical balance from horizontal and vertical axes, open space, and a few unequal rectangles without copying a canonical grid; use warm white as the open ground, near-black for structural lines, and restrained red, blue, or yellow as separated color planes, with rare gray transitions. Maintain the requested tabletop still life and 16:9 composition. No diagonal forms, gradients, realistic cast shadows, ornament, extra objects, readable text, logo, or copied artwork. Single image, not a comparison panel.
```

The compiled provider-neutral jobs are archived as `legacy-job.json` and `direction-job.json`. These are the package compiler records; the exact prompts above include the shared user task and generation-tool formatting used for each call.
