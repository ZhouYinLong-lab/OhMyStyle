# 让·米歇尔·巴斯奎特

[English](README.en.md)

![让·米歇尔·巴斯奎特代表图](gallery-16x9.jpg)

> **分类：** 艺术家  
> **媒介领域：** 绘画  
> **目录：** `style-packages/artists/jean-michel-basquiat`

## 简介

这个包提取粗粝的混合媒介表面、断裂形体、强势手绘线条、压缩空间和少量高张力色块。它适合让画面保留手工制作的不整齐，同时让主体在符号化、抽象化的视觉秩序中保持可辨认。

## 策展短评

巴斯奎特式的力量不只来自某个符号，而来自画面像是在现场不断被添加、擦除和重新组织。代表图用抽象墙面展示这种材料感：黑线负责把松散的色块拢住，磨损底色又让结构保持开放。换成你的主体后，应迁移的是线、面和表面之间的张力，而不是固定的街道、文字或图标。

## 主体独立性

本包只决定视觉处理，不规定人物、物体、地点、建筑、植物或故事。代表图中的抽象墙面只是示例；皇冠、骷髅、街道、涂鸦文字等都不是默认内容。使用者提供的主体和构图要求优先。

## 使用前先看

- `identity.yaml`：范围与排除项
- `visual-signature.yaml`：换主体后仍应保留的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础约束
- `palette/palette.json`：色彩角色
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源与权利边界

## 新架构：用户文字与标记层级（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，仅在用户明确提供画面中的文字或符号并声明 `user-authored-mark-hierarchy` 时启用。它把用户给出的内容按大小、颜色、位置和手绘线条组织层级；只有调用者声明 `requested-mark-intervention` 时，才允许对指定标记执行划线、圈出、重复或遮挡。`rough-mixed-media-surface` 控制粗粝手绘表面的辅助规则。没有用户输入时，不添加任何字、皇冠、骷髅、解剖图、署名或文化暗示。MoMA 与惠特尼的馆方资料分别记录了文字、色块和手绘标记的交织，以及划掉文字用于吸引注意的做法；本方向只转译这些形式关系，不借用原作信息或话语。

它与普通涂鸦墙或干净的海报字体排版都不同：内容由用户决定，手绘线、色块和局部划改形成层级，留白和底材仍可见。重点是“如何强调指定内容”，而不是随机堆字或套用固定符号。

```powershell
python tools/compile-style.py style-packages/artists/jean-michel-basquiat --direction package --context user-authored-mark-hierarchy --context requested-mark-intervention --context rough-mixed-media-surface --subject "A small yellow portable radio with the exact handwritten words RADIO, SIGNAL, and QUIET; cross out only QUIET once; include one blue square and one red circle; no other text"
```

[`comparisons/`](comparisons/) 保存旧版与新方向 job、提示词和样图。新方向样图以旧图为构图参考，便于检查指定文字层级和局部划改；生成仍有随机性，文字是否准确须以图片实际结果为准。方向保持实验状态，等待视觉评审。

## 来源与版权

本包参考[现代艺术博物馆的艺术家资料](https://www.moma.org/artists/370-jean-michel-basquiat)，只提取可观察的视觉特征。外部作品及其图像权利仍归原权利人所有；代表图是新的原创抽象场景，不复制具体作品，也不表示与艺术家、机构存在合作、授权或背书关系。详细边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 和仓库根目录的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

四种方式任选其一：

1. **交给有生图能力的 Agent**：把本目录交给 Agent，要求先读取身份、视觉签名、复现说明、Prompt、调色板和评估文件，再把你的主题编译成完整 Prompt；生成后按 `evaluation.yaml` 复核，不要只输入风格名称。
2. **直接复制 Prompt**：打开 `prompts/base.txt`，替换 `{SUBJECT}` 与 `{LOCATION}`；将 `prompts/negative.txt` 一并提交。
3. **配置 API Key 后提交生成**：在你自己的平台或编译工具中配置 API Key，提交基础 Prompt、负面约束、调色板和必要参考清单。本仓库不托管密钥或在线生图服务。
4. **本地模型 + ComfyUI**：把基础 Prompt 和负面约束接入工作流，按复现说明设置线条、色块、压缩空间和表面；生成后用 `evaluation.yaml` 复核。

模型权重、密钥和生成图片由使用者自行管理。参考资料用于理解特征，不用于复制原作。
