# Manga Dossier Blueprint Poster

![Manga Dossier Blueprint Poster representative example](preview-16x9.jpg)


> **分类 / Category:** [继承的 110 个轻量预设 / Inherited 110 lightweight presets]
> **类型 / Type:** 继承的轻量预设 / inherited lightweight preset
> **包路径 / Package path:** `styles/manga-dossier-blueprint-poster`

## 简介（中文）

这是从原始 `AI-Visual-Prompt-Cookbook` 继承的轻量风格预设「Manga Dossier Blueprint Poster」。本仓库保留原有 `style.json`、预览图与兼容目录；此 README 只提供导航、使用方式和归属说明，不将继承内容重新宣称为 OhMyStyle 原创。

核心观察点：Layered editorial dossier layout with a dominant grayscale manga ink portrait, a smaller dynamic full-body figure, boxed inset panels, narrow annotation rails, and asymmetrical negative space.；Warm off-white paper base with visible speckles, scuffs, worn ink, photocopy grain, and distressed screenprint edges.；Limited palette led by charcoal black, cool grays, deep cobalt blue, desaturated navy, and bright cyan accents; color appears in panels, type, and kinetic energy marks rather than full-scene realism.；Oversized condensed all-caps sans-serif headline blocks with weathered ink texture, stacked title hierarchy, and compact microcopy labels in small uppercase type.

## Overview (English)

This is the inherited lightweight preset “Manga Dossier Blueprint Poster” from the original `AI-Visual-Prompt-Cookbook` catalog. OhMyStyle keeps its `style.json`, previews, and compatibility path; this README adds navigation and usage guidance without claiming authorship.

Key observations: Layered editorial dossier layout with a dominant grayscale manga ink portrait, a smaller dynamic full-body figure, boxed inset panels, narrow annotation rails, and asymmetrical negative space.; Warm off-white paper base with visible speckles, scuffs, worn ink, photocopy grain, and distressed screenprint edges.; Limited palette led by charcoal black, cool grays, deep cobalt blue, desaturated navy, and bright cyan accents; color appears in panels, type, and kinetic energy marks rather than full-scene realism.; Oversized condensed all-caps sans-serif headline blocks with weathered ink texture, stacked title hierarchy, and compact microcopy labels in small uppercase type.

## 来源与版权（中文）

参考资料只用于研究和风格拆解。外部作品的版权、商标、截图和平台页面仍归原权利人所有；本包不代表与相关艺术家、摄影师、游戏或机构存在合作关系。生成示例是新的匿名场景，不是原作者作品。

来源链接：

- [https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook](https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook)

具体权利边界请先阅读 `provenance.yaml` (if present) 和仓库根目录的 [`NOTICE`](../../NOTICE)。

## Sources and rights (English)

References are used for research and visual analysis. Copyright, trademarks, screenshots, and source pages remain with their respective rights holders. This package is independent and does not imply endorsement or affiliation. Generated examples are anonymous new scenes, not works by the referenced creator.

Source links:

- [https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook](https://github.com/VigoZhao/AI-Visual-Prompt-Cookbook)

Read `provenance.yaml` (if present) when present and the repository [`NOTICE`](../../NOTICE) before redistributing anything.

## 只使用此包 / Use only this package

### 方式一：下载风格包，复制生成 Prompt

下载本目录，打开 `styles/manga-dossier-blueprint-poster/style.json`，或查看 [`docs/copy-prompts/manga-dossier-blueprint-poster.md`](../../docs/copy-prompts/manga-dossier-blueprint-poster.md)。 把包内变量替换为你的主题，再将生成的 Prompt 复制到任意支持文字生图的平台。参考图、负面约束和可选参数见同目录文件。

Download this directory. Open `styles/manga-dossier-blueprint-poster/style.json`, or read [`docs/copy-prompts/manga-dossier-blueprint-poster.md`](../../docs/copy-prompts/manga-dossier-blueprint-poster.md). Fill in the variables and paste the resulting Prompt into an image model. Reference roles, negative constraints, and optional parameters are kept beside the package.

### 方式二：配置 API Key，一键生成

OhMyStyle 不托管用户密钥。配置你选择的模型提供商 API Key 后，继承预设没有结构化 API 编译器；可先生成 copy-prompt 文档，再将其中 Prompt 交给你自己的 API 适配器。

```bash
python scripts/generate-copy-prompts.py .
```

The inherited preset has no structured API compiler; generate its copy-prompt document first, then submit that Prompt through your own API adapter. Keep API keys outside the repository and let your chosen adapter submit the job to the model.

### 方式三：本地模型 + ComfyUI 工作流

将 `style.json`、预览图和 copy-prompt 文档作为 ComfyUI 的文字与参考输入；如需更细的控制，建议迁移到结构化 `style-packages/`。 像素、遮罩或构图约束优先使用包内的 reproduction 与 workflow 文件。

Use `style.json`, the preview, and the copy-prompt document as ComfyUI text/reference inputs. For finer control, migrate the preset into a structured `style-packages/` package. Use the package reproduction and workflow files when available. Model weights are not bundled; ComfyUI runs the models installed by the user.

## 包内文件 / Package files

- [style.json](style.json)
- [16:9 preview](preview-16x9.jpg)
- See the package visual signature and reproduction files for the complete constraint set.

## 免责声明 / Disclaimer

风格包描述的是可观察的媒介、构图、色彩、光线和表面决策，不保证任何模型得到完全相同的输出，也不鼓励复制受保护作品的具体构图、人物、文字或标志。

The package describes observable decisions in medium, composition, color, light, and surface. It does not guarantee identical output and does not authorize copying protected compositions, characters, text, or marks.
