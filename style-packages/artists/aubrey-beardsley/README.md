# 奥布里·比亚兹莱

[English](README.en.md)

![奥布里·比亚兹莱风格包代表图](gallery-16x9.jpg)

> **分类：** 艺术家  
> **媒介：** 钢笔与毛笔墨水插画  
> **目录：** `style-packages/artists/aubrey-beardsley`

## 简介

本包从比亚兹莱的世纪末黑白插画中提炼图形规则：以明确的黑色墨块与大面积留白建立主次，用富有书写感的流动轮廓组织人物和物件，只在焦点区域保留密集细节。线版印刷的媒介背景也要求黑白形状在缩小后仍能清楚分辨。

这个包控制线条、黑白比例、细节密度与版面空间，不强制加入维多利亚服饰、藤蔓、文学人物或装饰边框。

## 与相近方向区分

- **阿尔丰斯·穆夏：** 常以彩色平面、装饰性人物和海报版式构成画面；本包坚持黑白墨线、明确墨块和非对称留白。
- **普通哥特式插画：** 本包不靠骷髅、尖拱或阴森道具表达风格，识别核心是线条与正负形的组织。
- **版画式密集排线：** 不追求全画面均匀刻线；细节密度需要集中、疏密反差明确。

## 包内文件

- `identity.yaml`：风格范围、主体开放策略与排除项
- `visual-signature.yaml`：跨主题保持的视觉特征
- `reproduction.yaml`：先分配黑白形，再组织轮廓与局部细节
- `prompts/base.txt`、`prompts/negative.txt`：基础提示与负面约束
- `palette/palette.json`：墨色、纸白与可选灰洗
- `evaluation.yaml`：黑白比例、线条、疏密和主体检查
- `references/manifest.csv`、`provenance.yaml`：博物馆来源与权利边界
- `examples/generated/`：未审核候选图仅保存在本地，不默认进入版本库

## 来源与版权

参考清单链接到奥赛博物馆、维多利亚与阿尔伯特博物馆以及大都会艺术博物馆的资料。清单中的原作仅供研究，本仓库不收录或重绘这些原作。

代表图是匿名新场景，不是比亚兹莱原作、复刻或授权作品，也不代表博物馆或艺术家遗产机构背书。

## 使用

在 `prompts/base.txt` 中填写 `{SUBJECT}`、`{LOCATION}` 和 `{SUBJECT_ACTION}`。将基础提示与负面约束一起交给绘图工作流。该包应将用户提供的主体转译成黑白图形，不应擅自添加复古服装、花藤、文学叙事或海报文字。

生成后用 `evaluation.yaml` 检查画面是否先以黑白块面成立、轮廓是否有明确的书写节奏、细节是否集中于焦点。若缩小后全画面变成同样密度的线噪声，应减少纹理并扩大留白。

## 新架构：墨块、书写性轮廓与留白（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，把方向拆为三个可观察规则：先让黑白正负形在缩略尺寸成立；再以有粗细变化的书写性墨线组织轮廓；最后把精细线条限制在少数焦点。黑白墨块是基础规则；调用者可声明 `readable-outer-silhouette-or-overlap` 和 `distinct-focal-passage`，按需启用轮廓与焦点细节规则。它不要求装饰边框、藤蔓、哥特道具或文学人物，与穆夏的彩色海报框架方向有明确区别。

```powershell
python tools/compile-style.py style-packages/artists/aubrey-beardsley --direction package --context black-and-white-ink-illustration --subject "A small moth resting on a cracked teacup on a plain shelf" --output runs/style-v2/aubrey-beardsley-job.json
```

该规则仍为实验状态；同题生图对照及跨主体稳定性待人工评审。

## 新旧架构视觉对照

查看[同题样图、编译任务和复核限制](comparisons/README.md)。该对照是单题材初步检查，方向仍处于实验状态。
