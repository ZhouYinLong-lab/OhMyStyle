# 抽象几何霓虹：双几何体运动对照

> 单次同题对照；用于检查新版方向是否改变了可见处理，不代表新版质量更好或效果稳定。

## 图像

| 旧包编译 | 新版结构化方向 |
| --- | --- |
| ![旧包：蓝色立方体和橙红色圆环](legacy.png) | ![新版方向：蓝色立方体和橙红色圆环](direction.png) |

共同请求：横版 16:9，无文字。一个简洁的深色抽象空间里，一枚蓝色发光立方体与一个橙红色圆环沿左下到右上的对角线运动，只有这两个主体；几何边缘清晰，背景留有充足负空间。

## 观察结果

两张图都保留一枚蓝色立方体和一个橙红色圆环，沿左下至右上的方向排列；都使用暗底、蓝橙高亮、发光边缘和方向性光迹，没有加入文字或其他主体。新版图的对象略小，运动轨迹更细、更长，负空间更突出；旧包图的主体更大，光迹更宽。差异幅度有限，两张图整体视觉语言接近。

旧包在基线版本中已经包含几乎相同的几何、色彩、光迹和负空间说明。此结果说明新版编译保持了这些特征，但没有显示清楚的质量优势，也无法把有限差异归因于结构化格式本身。媒介、构图、色彩、光照、表面和节奏规则在两图中均可见；这只是单张结果的初步检查，不据此把规则或方向升级为 accepted。

## 生成记录

- 两组使用同一个中文请求，均不输入参考图，分别独立调用同一图像生成工具。
- `legacy-job.json` 与 `direction-job.json` 保存编译结果；`legacy-prompt.txt` 与 `direction-prompt.txt` 保存实际提交的提示文本（编译 Prompt 加负面约束）。新版任务记录方向文件哈希。
- 输出均为 1672 × 941 像素。工具未提供可核实的具体模型版本或随机种子；两次生成的随机状态无法匹配。
- 人工复核为单人、单次：对象数量、方向和无文字约束通过；新旧风格辨识优势未通过。需要多题材和重复生成后再判断稳定性。

## English note

This is a single same-subject comparison, not evidence of a quality advantage. Both outputs preserve one blue glowing cube and one orange-red ring on a dark diagonal motion axis. The structured-direction output uses slightly smaller objects, finer and longer trails, and more negative space; the legacy output uses larger subjects and broader trails. The visual difference is limited because the baseline package already contains nearly the same geometric, palette, trail, and spacing rules. The pair shows that the structured route retains those traits, but does not demonstrate a clear advantage. One reviewer checked subject count, layout, and visible rule cues. The generator did not expose a verifiable model version or seed, and each arm has one output.
