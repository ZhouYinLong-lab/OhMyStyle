# 交叉风格功能

[English](README.en.md)

交叉风格不作为独立风格出现在主画廊中。它是一种可选组合功能：用户可以把两个或多个独立风格包分配到不同角色、区域或维度，生成更复杂但仍可解释的结果。

## 功能

- `stack`：不同风格负责不同维度，例如媒介、光线或空间层次。
- `blend`：按权重融合相同维度的色彩、光线或表面规则。
- `contrast`：把风格分配到不同区域，避免规则互相污染。

## 使用方式

先选择基础风格包，再打开交叉包的 `composite.yaml`，按照其中的角色、区域、权重和禁止项编译 Prompt。没有明确选择时，运行时会根据基础包的职责自动选择 `stack`、`blend` 或 `contrast`。

## 示例

<table>
<tr>
<td width="33%" valign="top" align="center"><a href="rpg-maker-x-gauguin/README.md"><img src="rpg-maker-x-gauguin/examples/generated/anonymous-v1.png" width="230" alt="RPG Maker Foreground + Gauguin Background example"></a><br><strong>RPG Maker Foreground + Gauguin Background</strong><br><a href="rpg-maker-x-gauguin/README.md">打开 README</a></td>
<td width="33%" valign="top" align="center"><a href="rpg-maker-x-turner/README.md"><img src="rpg-maker-x-turner/examples/generated/anonymous-v1.png" width="230" alt="角色扮演游戏像素美术 + Turner Atmosphere example"></a><br><strong>角色扮演游戏像素美术 + Turner Atmosphere</strong><br><a href="rpg-maker-x-turner/README.md">打开 README</a></td>
<td width="33%" valign="top" align="center"><a href="vermeer-x-monet/README.md"><img src="vermeer-x-monet/examples/generated/anonymous-v1.png" width="230" alt="Vermeer Light + Monet Color example"></a><br><strong>Vermeer Light + Monet Color</strong><br><a href="vermeer-x-monet/README.md">打开 README</a></td>
</tr>
</table>
