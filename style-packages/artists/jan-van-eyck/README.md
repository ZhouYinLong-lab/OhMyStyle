# 扬·凡·艾克

[English](README.en.md)

![扬·凡·艾克 代表图](gallery-16x9.jpg)

> **分类：** 艺术家
> **媒介领域：** 绘画
> **目录：** `style-packages/artists/jan-van-eyck`

## 简介

细密油画、透明釉层和高精度细节；室内正面空间、镜面反射和精密小物共同构成静默的仪式感；深红、橄榄绿、木棕、蓝灰与珍珠白形成宝石般低亮色组。

这是一个可独立使用的风格包。它把可观察的媒介、构图、光线、色彩、表面、纹理和复现步骤整理成可执行规则，用于生成新的主题，不用于复制某一件具体作品。

## 策展短评

它最动人的地方是“细密油画、透明釉层和高精度细节；室内正面空间、镜面反射和精密小物共同构成静默的仪式感；深红、橄榄绿、木棕、蓝灰与珍珠白形成宝石般低亮色组”。画面不依赖固定场景，视觉秩序本身已经很清楚。

## 使用前先看

- `identity.yaml`：范围、对象和排除项
- `visual-signature.yaml`：跨主题仍应保持的视觉特征
- `reproduction.yaml`：媒介、材料和构建顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础 Prompt 与负面约束
- `palette/palette.json`：色彩角色与色值
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源和权利边界

## 新架构：釉层与材质光感（实验）

[`art-direction.yaml`](art-direction.yaml) 只在用户指定油画静物或近景材质研究，并显式声明 `glazed-material-observation` 时启用。它把不同材质在同一光源下的高光形状、边缘软硬、透明釉层的使用范围和细节密度写成可检查规则；不默认添加室内、镜子、人物、题字或象征物。

该方向的识别重点是材质各自如何接光，以及薄层颜色如何增加深度。它与苏巴朗方向的暗背景、强侧光和孤立静物不同，也不要求维米尔式的几何室内空间与窗光构图；凡·艾克方向关注多个物件之间细微但可辨的表面反应和选择性细节。

```powershell
python tools/compile-style.py style-packages/artists/jan-van-eyck --direction package --context glazed-material-observation --subject "A small green glass bottle, a folded cream linen cloth, and a tarnished brass key on a pale wooden tabletop, softly lit by a nearby window"
```

[`comparisons/`](comparisons/) 保存同题旧版与新方向 job、生图提示词和样图。当前样图里，新版玻璃和黄铜的高光更窄，亚麻和木面的明暗变化更柔和，细节也更集中；独立生成未固定随机种子，不是控制变量实验，差异不能视作所有模型下的必然效果。方向保持实验状态，等待视觉评审。

## 来源与版权

参考资料只用于研究和分析。外部作品、摄影作品、游戏画面、商标和平台页面仍归原权利人所有。生成示例是新的匿名场景，不是相关艺术家、摄影师、流派、学校或游戏的原作，也不代表合作、授权或背书关系。

详细来源和再分发边界见 [`provenance.yaml`](provenance.yaml)、[`references/manifest.csv`](references/manifest.csv) 以及仓库根目录的 [`NOTICE`](../../../NOTICE)。

## 只使用此包

四种方式可以按手边工具任选其一，不需要同时使用。

### 方式一：交给有生图能力的 Agent

把整个风格包目录上传给 Agent，或把本地目录路径交给它，并附上：

```text
请使用这个风格包帮助我生成图片。

请先读取本目录中的 identity.yaml、visual-signature.yaml、reproduction.yaml、
prompts/base.txt、prompts/negative.txt、palette/palette.json 和 evaluation.yaml。
请把文件中的规则整合到生成流程中，不要只把风格名称当作 Prompt，也不要复制参考作品。

我的生成需求是：
<填写人物、物体、场景、画幅和用途>

请先编译完整 Prompt，再调用你的生图能力。生成后按照 evaluation.yaml 检查风格特征、
构图、颜色、材质、AI 痕迹和需求遵循度，并说明仍然存在的风险。
```

### 方式二：直接复制 Prompt

打开 `prompts/base.txt`，替换主题、人物、物体、场景和画幅；将 `prompts/negative.txt` 作为负面 Prompt 一并提交到支持文本生图的平台。需要更稳定时，同时参考视觉签名和调色板。

### 方式三：配置 API Key 后提交生成

在你自己的生图平台或编译工具中配置 API Key，将基础 Prompt、负面约束、调色板和必要的参考清单一起提交。API Key 只保存在你的环境中；本仓库不代管密钥、不托管在线生图服务，也不承诺某个平台的免费额度或接口兼容性。

### 方式四：本地模型 + ComfyUI

将基础 Prompt 和负面约束接入本地模型或 ComfyUI 工作流；按调色板、复现说明和参考清单设置颜色、构图、材质与光线。生成后用 `evaluation.yaml` 做人工或自动复核。

模型权重、API Key 和生成图片由使用者自行管理。参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或标志。


