# Vermeer Light + Monet Color

[English](README.en.md)

![Vermeer Light + Monet Color 示例](gallery-16x9.jpg)

## 这是什么

交叉风格不是独立的艺术家、摄影师或流派，而是一种把多个风格包按角色组合的功能。它只在明确的区域、媒介、光线或色彩职责上复用基础包的规则，避免把多个名称简单拼接成一个模糊风格。

## 组合模式

当前模式：`blend`

- `artists/johannes-vermeer`：palette，Preserve calm interior light and readable object structure.
- `artists/claude-monet`：palette，Contribute chromatic temperature variation without flattening form.

## 使用机制

- `stack`：不同基础包负责不同维度，例如像素包负责媒介和边缘，绘画包负责天空或光线。
- `blend`：按权重融合相同维度的规则，同时保留主要结构。
- `contrast`：将基础包分配到不同区域，避免颜色、材质或笔触互相污染。

约束见 `composite.yaml`。生成示例：

![交叉风格示例](gallery-16x9.jpg)

## 只使用此包

1. 下载本目录，阅读 `identity.yaml`、`visual-signature.yaml` 和 `reproduction.yaml`。
2. 打开 `prompts/base.txt`，把主题替换为你自己的内容；负面约束见 `prompts/negative.txt`。
3. 选择一种执行方式：直接复制 Prompt 到生图平台；配置自己的 API Key 后提交编译任务；或将 Prompt、参考清单和调色板导入本地模型与 ComfyUI。
4. 参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。

模型权重、API Key 和生成图片由使用者自行管理；本仓库不托管在线生图服务。
