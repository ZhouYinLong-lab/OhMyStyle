# High-Chroma Color Pairing

_本包没有单独打包的代表图；请查看所引用基础包的示例。 / No standalone preview is bundled; see the referenced base package examples._


> **分类 / Category:** [原创预设 / Original presets]
> **类型 / Type:** 原创视觉预设 / original visual preset
> **包路径 / Package path:** `style-packages/presets/high-chroma-color-pairing`

## 简介（中文）

这是一个面向「High-Chroma Color Pairing」的独立 原创视觉预设。它把公开作品、研究资料和可观察视觉特征整理成可执行约束，重点关注 `composition, lighting, palette, surface`，用于生成新场景，而不是复制某一幅原作。

核心观察点：color_masses_establish_hierarchy_before_texture；dominant_mass_occupies_more_area_than_counter_mass；counter_mass_is_intentional_and_easy_to_locate；keep_open_negative_space_around_the_main_color_event

## Overview (English)

This is an independent original visual preset package for “High-Chroma Color Pairing”. It turns public references, research material, and observable visual decisions into executable constraints focused on `composition, lighting, palette, surface`. It is intended for new scenes, not copies of a named artwork.

Key observations: color_masses_establish_hierarchy_before_texture; dominant_mass_occupies_more_area_than_counter_mass; counter_mass_is_intentional_and_easy_to_locate; keep_open_negative_space_around_the_main_color_event

## 来源与版权（中文）

参考资料只用于研究和风格拆解。外部作品的版权、商标、截图和平台页面仍归原权利人所有；本包不代表与相关艺术家、摄影师、游戏或机构存在合作关系。生成示例是新的匿名场景，不是原作者作品。

来源链接：

- [https://www.bilibili.com/video/BV1acjF68E6N/?spm_id_from=333.1387.favlist.content.click&vd_source=dc8a446ed48dbc0e71281a3db9654692](https://www.bilibili.com/video/BV1acjF68E6N/?spm_id_from=333.1387.favlist.content.click&vd_source=dc8a446ed48dbc0e71281a3db9654692)
- [https://www.bilibili.com/video/BV1qe4y1d71z?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2589621-cb5r7.1785986300627.4&vd_source=dc8a446ed48dbc0e71281a3db9654692](https://www.bilibili.com/video/BV1qe4y1d71z?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2589621-cb5r7.1785986300627.4&vd_source=dc8a446ed48dbc0e71281a3db9654692)

具体权利边界请先阅读 [`provenance.yaml`](provenance.yaml) 和仓库根目录的 [`NOTICE`](../../../NOTICE)。

## Sources and rights (English)

References are used for research and visual analysis. Copyright, trademarks, screenshots, and source pages remain with their respective rights holders. This package is independent and does not imply endorsement or affiliation. Generated examples are anonymous new scenes, not works by the referenced creator.

Source links:

- [https://www.bilibili.com/video/BV1acjF68E6N/?spm_id_from=333.1387.favlist.content.click&vd_source=dc8a446ed48dbc0e71281a3db9654692](https://www.bilibili.com/video/BV1acjF68E6N/?spm_id_from=333.1387.favlist.content.click&vd_source=dc8a446ed48dbc0e71281a3db9654692)
- [https://www.bilibili.com/video/BV1qe4y1d71z?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2589621-cb5r7.1785986300627.4&vd_source=dc8a446ed48dbc0e71281a3db9654692](https://www.bilibili.com/video/BV1qe4y1d71z?spm_id_from=333.788.recommend_more_video.1&trackid=web_related_0.router-related-2589621-cb5r7.1785986300627.4&vd_source=dc8a446ed48dbc0e71281a3db9654692)

Read [`provenance.yaml`](provenance.yaml) when present and the repository [`NOTICE`](../../../NOTICE) before redistributing anything.

## 只使用此包 / Use only this package

### 方式一：下载风格包，复制生成 Prompt

下载本目录，打开 `style-packages/presets/high-chroma-color-pairing/prompts/base.txt`，替换变量后复制。 把包内变量替换为你的主题，再将生成的 Prompt 复制到任意支持文字生图的平台。参考图、负面约束和可选参数见同目录文件。

Download this directory. Open `style-packages/presets/high-chroma-color-pairing/prompts/base.txt`, fill in its variables, and paste the result. Fill in the variables and paste the resulting Prompt into an image model. Reference roles, negative constraints, and optional parameters are kept beside the package.

### 方式二：配置 API Key，一键生成

OhMyStyle 不托管用户密钥。配置你选择的模型提供商 API Key 后，编译器只生成 provider-neutral 任务；再由你选择的 API 适配器提交，仓库不保存密钥。

```bash
python tools/compile-style.py style-packages/presets/high-chroma-color-pairing --subject "你的主题" --profile weak --output tmp/high-chroma-color-pairing-job.json
```

The compiler emits a provider-neutral job; your chosen API adapter submits it. The repository never stores your key. Keep API keys outside the repository and let your chosen adapter submit the job to the model.

### 方式三：本地模型 + ComfyUI 工作流

将 `prompts/`、`references/`、`palette/` 和生成的 job 导入本地模型工作流；模型权重由用户自行安装。 像素、遮罩或构图约束优先使用包内的 reproduction 与 workflow 文件。

Import `prompts/`, `references/`, `palette/`, and the compiled job into a local workflow; users install their own model weights. Use the package reproduction and workflow files when available. Model weights are not bundled; ComfyUI runs the models installed by the user.

## 包内文件 / Package files

- [package.yaml](package.yaml)
- [provenance.yaml](provenance.yaml)
- [reference manifest](references/manifest.csv)
- See the package visual signature and reproduction files for the complete constraint set.

## 免责声明 / Disclaimer

风格包描述的是可观察的媒介、构图、色彩、光线和表面决策，不保证任何模型得到完全相同的输出，也不鼓励复制受保护作品的具体构图、人物、文字或标志。

The package describes observable decisions in medium, composition, color, light, and surface. It does not guarantee identical output and does not authorize copying protected compositions, characters, text, or marks.
