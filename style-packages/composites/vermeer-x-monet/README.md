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

本交叉包引用 `composite.yaml` 中列出的基础风格包；使用时请同时下载本目录和这些基础包。

### 方式一：交给具备生图能力的 Agent

把本目录和 `bases` 中列出的基础风格包一起提供给 Agent。让 Agent 先读取 `composite.yaml`、各基础包的 `README.md`、`visual-signature.yaml`、`reproduction.yaml`、`prompts/base.txt` 和 `prompts/negative.txt`，再把你的主题编译为本交叉包对应的模式。

必须保留：

- 基础包承担的角色；
- `zone` 区域分配；
- 权重；
- `constraints.must` 和 `constraints.avoid`；
- 不同风格之间的边界。

### 方式二：编译后复制 Prompt

在仓库根目录运行：

```bash
python tools/compile-composite.py \
  style-packages/composites/vermeer-x-monet \
  --subject "把这里替换为你的主题" \
  --mode auto \
  --profile generic
```

把输出 JSON 中的 `prompt` 和 `negative_prompt` 复制到你使用的生图平台。`--mode auto` 会使用组合包声明的模式；也可以显式指定 `stack`、`blend` 或 `contrast`。

### 方式三：配置 API Key 后提交生成任务

使用自己的生图平台或 API 客户端，将编译结果中的 Prompt、负面约束、主题变量和参考资源提交给模型。OhMyStyle 只负责风格包和任务编译，不托管 API Key，也不提供在线生图服务。

### 方式四：本地模型 + ComfyUI

将编译后的 Prompt 和负面 Prompt 导入本地模型或 ComfyUI，并同时提供基础风格包的参考图、调色板和结构约束。对于 `contrast`，如果模型执行不稳定，可以在 ComfyUI 中手动增加区域 mask；交叉包本身不会自动生成 mask。

参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。

模型权重、API Key 和生成图片由使用者自行管理。
