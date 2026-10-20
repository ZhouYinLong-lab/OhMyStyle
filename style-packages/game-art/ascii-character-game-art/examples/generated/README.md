# Deterministic ASCII render

![逐格字符渲染的洞穴场景](ascii-cave-grid.png)

This is a deterministic rasterization of the literal character source in [`../ascii-cave-grid.txt`](../ascii-cave-grid.txt), not an image model's approximation. Every visible mark maps to a source glyph and grid cell. The job, output hash, font metadata, and source hash are recorded in [`direction-job.json`](direction-job.json) and [`render-manifest.json`](render-manifest.json).

**Review scope:** the renderer preserves the 100-column by 36-row source grid and uses a monospaced font. This confirms literal construction for this sample; scene readability and generalization to new subjects remain under review, so the package direction stays experimental.
