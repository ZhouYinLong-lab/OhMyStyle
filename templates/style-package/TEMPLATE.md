# 风格包模板说明

[English](TEMPLATE.en.md)

本目录是可执行风格包的标准模板，不是一个可发布的风格包。正式包应由
`tools/new-style-package.py` 创建到 `style-packages/<分类>/<id>/`，不要直接
把本目录改名后提交。

```powershell
python tools/new-style-package.py `
  --kind artist `
  --id your-style-id `
  --name "中文风格名" `
  --domain painting `
  --summary "至少三十个字符，并描述可观察的媒介、构图、光线、色彩或表面规则。"
```

提供 `--source-url`、`--source-title`、`--source-creator` 和
`--source-attribution` 后，创建器会自动生成 L2 来源清单；否则生成 L1
研究草稿。生成完成后替换所有 `TODO`，核对来源与权利，替换
`gallery-16x9.svg`。代表图必须从生成阶段就采用原生横版 16:9 构图；不要先生成竖版图，再裁切或拉伸成画廊图。再按
`CONTRIBUTING.md` 执行校验。

后续扩充按实际范围划分批次。先复制并填写 [`templates/expansion-batch.yaml`](../expansion-batch.yaml) 中的包条目，再逐包完成本模板；一个包一个 commit，不能用批次 README 或画廊索引替代实际包内容。

模板文件对应正式包中的：

- `package.yaml`：包身份、类别、领域、版本和文件索引；
- `identity.yaml`：范围、主体、排除项和实体来源；
- `visual-signature.yaml`：跨主题稳定的视觉特征；
- `reproduction.yaml`：媒介、材料和构建顺序；
- `relations.yaml`：相关流派、概念和边界；
- `palette/palette.json`：颜色角色和值；
- `prompts/`：基础 Prompt 与负面约束；
- `evaluation.yaml`：生成后的检查项；
- `references/`、`provenance.yaml`：参考来源、署名和再分发边界；
- `examples/`：待审核、通过和失败的匿名生成样例；
- `resource.yaml`：注册表使用的成熟度和资源契约；
- `README.md`、`README.en.md`：面向使用者的双语说明。

## 主体独立性要求

`prompts/base.txt` 必须包含主体独立契约，并使用 `{SUBJECT}` 与 `{LOCATION}` 占位符。风格包只描述媒介、构图、光线、色彩、材质、纹理和边缘行为；桥梁、房屋、人物、城市、花卉、车辆等具体内容只能作为 `examples/` 或 benchmark 的测试场景。`identity.yaml` 中的 `scope.subject_policy` 必须为 `open`。

模板中的 `gallery-16x9.svg` 只是占位图。发布前必须替换为原生横版 16:9、已生成、公共领域
或明确允许再分发的代表图；风格包 README 和总 README 画廊都直接使用这张横版代表图。
