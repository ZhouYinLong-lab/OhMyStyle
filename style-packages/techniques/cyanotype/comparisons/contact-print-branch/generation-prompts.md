# Generation prompts used for the cyanotype comparison

The two prompts below are the actual prompts passed to the built-in image-generation tool. Calls were independent, used no reference images, and requested one 16:9 landscape view each.

## Legacy package arm

```text
Create one landscape 16:9 image. User subject: 横版 16:9，一枝有三片叶和一朵白色花的植物枝条，以接触印相方式呈现于浅色纸面，背景简洁，无文字。 Apply the legacy cyanotype package prompt: an original flat blue contact print; present the user-specified plant subject as a light-sensitive object on handmade paper, with a monochrome range from deep Prussian blue to pale cyan blue, slightly diffused chemical edges and uneven paper. Keep exactly one branch, three leaves, and one white flower. No text, logo, props, second plant, or copy of a specific artwork. Single image, not a comparison panel.
```

## Structured direction arm

```text
Create one landscape 16:9 image, one single view. USER SUBJECT: 横版 16:9，一枝有三片叶和一朵白色花的植物枝条，以接触印相方式呈现于浅色纸面，背景简洁，无文字。 Preserve exactly one branch, three leaves, and one white flower on a pale paper ground. Apply the structured cyanotype direction as visual treatment only: make the plant a readable contact-print silhouette with deliberate negative space and visible paper margins; use Prussian blue for the darkest image areas, middle and diluted blues to separate tones, and warm paper or unexposed regions as clearly distinct ground. Keep the photochemical contact-print process, slight edge irregularity, and paper surface visible. Do not apply a uniform blue filter. No extra plant, vase, tools, writing, logo, or copied artwork. Single image, not a comparison panel.
```

The compiled provider-neutral jobs are archived as `legacy-job.json` and `direction-job.json`. They retain the package-derived prompt inputs and provenance recorded by the compiler.
