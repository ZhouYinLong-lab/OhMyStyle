# 视觉对照

- `legacy.png`：按蒙德里安基础包生成的连续网格与彩色区块版本。
- `direction.png`：在同一图像上应用 `mondrian-syncopated-route-grid` 后的分段节奏版本。
- `legacy-job.json`、`direction-job.json`：对应的 provider-neutral 编译任务。
- `generation-prompts.md`：生图指令、观察记录和限制。

两张图使用同一个虚构抽象交通网络。新版把连续彩色线段改成错拍短段，减少黑色网格的统治感；路线仍沿原来的水平/垂直路径排列。它只测试风格迁移，不可用于导航；规则仍待其他网络形状复测。
