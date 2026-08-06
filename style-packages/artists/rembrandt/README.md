# Rembrandt van Rijn

![Rembrandt van Rijn representative example](examples/accepted/anonymous-v1.png)


> **分类 / Category:** [艺术家 / Artists]
> **类型 / Type:** 艺术家 / artist
> **包路径 / Package path:** `style-packages/artists/rembrandt`

## 简介（中文）

这是一个面向「Rembrandt van Rijn」的独立 艺术家。它把公开作品、研究资料和可观察视觉特征整理成可执行约束，重点关注 `medium, composition, lighting, palette, surface, texture`，用于生成新场景，而不是复制某一幅原作。

核心观察点：place a figure or gesture inside a large dark field with a clear light path；use asymmetrical balance and quiet surrounding space；let hands, face, fabric, or an object carry the narrative focus；deep umber

## Overview (English)

This is an independent artist package for “Rembrandt van Rijn”. It turns public references, research material, and observable visual decisions into executable constraints focused on `medium, composition, lighting, palette, surface, texture`. It is intended for new scenes, not copies of a named artwork.

Key observations: place a figure or gesture inside a large dark field with a clear light path; use asymmetrical balance and quiet surrounding space; let hands, face, fabric, or an object carry the narrative focus; deep umber

## 来源与版权（中文）

参考资料只用于研究和风格拆解。外部作品的版权、商标、截图和平台页面仍归原权利人所有；本包不代表与相关艺术家、摄影师、游戏或机构存在合作关系。生成示例是新的匿名场景，不是原作者作品。

来源链接：

- [https://commons.wikimedia.org/wiki/File:Rembrandt_-_Aristotle_with_a_Bust_of_Homer_-_Google_Art_Project.jpg](https://commons.wikimedia.org/wiki/File:Rembrandt_-_Aristotle_with_a_Bust_of_Homer_-_Google_Art_Project.jpg)
- [https://commons.wikimedia.org/wiki/File:Andromeda,_Rembrandt_van_Rijn,_1630-1631,_Mauritshuis,_The_Hague.jpg](https://commons.wikimedia.org/wiki/File:Andromeda,_Rembrandt_van_Rijn,_1630-1631,_Mauritshuis,_The_Hague.jpg)
- [https://www.rijksmuseum.nl/en/collection/object/Isaac-and-Rebecca-Known-as-The-Jewish-Bride--019c1265e6dbf108d4587ab2b7c02c66](https://www.rijksmuseum.nl/en/collection/object/Isaac-and-Rebecca-Known-as-The-Jewish-Bride--019c1265e6dbf108d4587ab2b7c02c66)

具体权利边界请先阅读 [`provenance.yaml`](provenance.yaml) 和仓库根目录的 [`NOTICE`](../../../NOTICE)。

## Sources and rights (English)

References are used for research and visual analysis. Copyright, trademarks, screenshots, and source pages remain with their respective rights holders. This package is independent and does not imply endorsement or affiliation. Generated examples are anonymous new scenes, not works by the referenced creator.

Source links:

- [https://commons.wikimedia.org/wiki/File:Rembrandt_-_Aristotle_with_a_Bust_of_Homer_-_Google_Art_Project.jpg](https://commons.wikimedia.org/wiki/File:Rembrandt_-_Aristotle_with_a_Bust_of_Homer_-_Google_Art_Project.jpg)
- [https://commons.wikimedia.org/wiki/File:Andromeda,_Rembrandt_van_Rijn,_1630-1631,_Mauritshuis,_The_Hague.jpg](https://commons.wikimedia.org/wiki/File:Andromeda,_Rembrandt_van_Rijn,_1630-1631,_Mauritshuis,_The_Hague.jpg)
- [https://www.rijksmuseum.nl/en/collection/object/Isaac-and-Rebecca-Known-as-The-Jewish-Bride--019c1265e6dbf108d4587ab2b7c02c66](https://www.rijksmuseum.nl/en/collection/object/Isaac-and-Rebecca-Known-as-The-Jewish-Bride--019c1265e6dbf108d4587ab2b7c02c66)

Read [`provenance.yaml`](provenance.yaml) when present and the repository [`NOTICE`](../../../NOTICE) before redistributing anything.

## 只使用此包 / Use only this package

### 方式一：下载风格包，复制生成 Prompt

下载本目录，打开 `style-packages/artists/rembrandt/prompts/base.txt`，替换变量后复制。 把包内变量替换为你的主题，再将生成的 Prompt 复制到任意支持文字生图的平台。参考图、负面约束和可选参数见同目录文件。

Download this directory. Open `style-packages/artists/rembrandt/prompts/base.txt`, fill in its variables, and paste the result. Fill in the variables and paste the resulting Prompt into an image model. Reference roles, negative constraints, and optional parameters are kept beside the package.

### 方式二：配置 API Key，一键生成

OhMyStyle 不托管用户密钥。配置你选择的模型提供商 API Key 后，编译器只生成 provider-neutral 任务；再由你选择的 API 适配器提交，仓库不保存密钥。

```bash
python tools/compile-style.py style-packages/artists/rembrandt --subject "你的主题" --profile weak --output tmp/rembrandt-job.json
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
