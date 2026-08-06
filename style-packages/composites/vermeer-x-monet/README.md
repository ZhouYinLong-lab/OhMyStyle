# Vermeer Light + Monet Color

![Vermeer Light + Monet Color representative example](../../artists/johannes-vermeer/examples/accepted/anonymous-v1.png)


> **分类 / Category:** [交叉风格配方 / Cross-style recipes]
> **类型 / Type:** 交叉风格配方 / cross-style recipe
> **包路径 / Package path:** `style-packages/composites/vermeer-x-monet`

## 简介（中文）

这是一个独立的交叉风格配方「Vermeer Light + Monet Color」。它只引用已有风格包，并通过角色、权重和约束定义组合关系，不复制基础包的文字或参考资源。

核心观察点：Demonstrate weighted blending of two palette and light signatures.

## Overview (English)

This is an independent cross-style recipe, “Vermeer Light + Monet Color”. It references existing packages and defines their roles, weights, and constraints without copying their text or reference assets.

Key observations: Demonstrate weighted blending of two palette and light signatures.

## 来源与版权（中文）

参考资料只用于研究和风格拆解。外部作品的版权、商标、截图和平台页面仍归原权利人所有；本包不代表与相关艺术家、摄影师、游戏或机构存在合作关系。生成示例是新的匿名场景，不是原作者作品。

来源链接：

- No external source is redistributed; see the package provenance file.

具体权利边界请先阅读 `provenance.yaml` (if present) 和仓库根目录的 [`NOTICE`](../../../NOTICE)。

## Sources and rights (English)

References are used for research and visual analysis. Copyright, trademarks, screenshots, and source pages remain with their respective rights holders. This package is independent and does not imply endorsement or affiliation. Generated examples are anonymous new scenes, not works by the referenced creator.

Source links:

- No external source is redistributed; see the package provenance file.

Read `provenance.yaml` (if present) when present and the repository [`NOTICE`](../../../NOTICE) before redistributing anything.

## 只使用此包 / Use only this package

### 方式一：下载风格包，复制生成 Prompt

下载本目录，打开 `style-packages/composites/vermeer-x-monet/prompts/base.txt`，替换变量后复制。 把包内变量替换为你的主题，再将生成的 Prompt 复制到任意支持文字生图的平台。参考图、负面约束和可选参数见同目录文件。

Download this directory. Open `style-packages/composites/vermeer-x-monet/prompts/base.txt`, fill in its variables, and paste the result. Fill in the variables and paste the resulting Prompt into an image model. Reference roles, negative constraints, and optional parameters are kept beside the package.

### 方式二：配置 API Key，一键生成

OhMyStyle 不托管用户密钥。配置你选择的模型提供商 API Key 后，编译器只生成 provider-neutral 任务；再由你选择的 API 适配器提交，仓库不保存密钥。

```bash
python tools/compile-style.py style-packages/composites/vermeer-x-monet --subject "你的主题" --profile weak --output tmp/vermeer-x-monet-job.json
```

The compiler emits a provider-neutral job; your chosen API adapter submits it. The repository never stores your key. Keep API keys outside the repository and let your chosen adapter submit the job to the model.

### 方式三：本地模型 + ComfyUI 工作流

将 `prompts/`、`references/`、`palette/` 和生成的 job 导入本地模型工作流；模型权重由用户自行安装。 像素、遮罩或构图约束优先使用包内的 reproduction 与 workflow 文件。

Import `prompts/`, `references/`, `palette/`, and the compiled job into a local workflow; users install their own model weights. Use the package reproduction and workflow files when available. Model weights are not bundled; ComfyUI runs the models installed by the user.

## 包内文件 / Package files

- [composite.yaml](composite.yaml)
- [`artists/johannes-vermeer`](../../artists/johannes-vermeer/README.md) — role: `palette`
- [`artists/claude-monet`](../../artists/claude-monet/README.md) — role: `palette`

## 免责声明 / Disclaimer

风格包描述的是可观察的媒介、构图、色彩、光线和表面决策，不保证任何模型得到完全相同的输出，也不鼓励复制受保护作品的具体构图、人物、文字或标志。

The package describes observable decisions in medium, composition, color, light, and surface. It does not guarantee identical output and does not authorize copying protected compositions, characters, text, or marks.
