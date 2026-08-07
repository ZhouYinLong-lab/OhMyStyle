# 参与贡献

[English](CONTRIBUTING.en.md)

感谢参与 OhMyStyle。仓库包含两个彼此独立维护的部分：

- `style-packages/`：带来源、复现规则和评估标准的可执行风格包，覆盖艺术家、摄影师、流派、学校、工艺、原创预设和游戏美术；
- `styles/`：为兼容原项目而保留的 110 个 `style.json` 继承预设，不代表 OhMyStyle 重新创作了其中的全部描述或预览图。

提交或再分发素材前，请阅读 [LICENSE](LICENSE)、[LICENSE-OHMYSTYLE.md](LICENSE-OHMYSTYLE.md) 和 [NOTICE](NOTICE)。

## 提交前必须确认

- 每一个外部来源都记录在 `provenance.yaml` 或 `references/manifest.csv` 中；
- 如果图片再分发权不清楚，使用来源链接和描述性元数据，不要直接把网上看到的作品下载进仓库；
- 不提交没有再分发许可的艺术作品、摄影作品、游戏截图、水印图、品牌素材、私有 Prompt 或数据集素材；
- 生图样例必须标明为生成内容，不得冒充参考艺术家、摄影师、流派或游戏的原作；
- 对在世艺术家或摄影师，只描述可观察、非排他性的视觉特征，不声称精确仿作、合作或授权；
- 继承预设的原始版权、许可证和署名信息必须保留。

## 新风格包的标准结构

新包应放在最具体的分类目录下：

```text
style-packages/<分类>/<id>/
├── package.yaml                 # 包身份、类别、领域、版本和文件索引
├── identity.yaml                # 范围、主体、排除项和实体来源
├── visual-signature.yaml        # 跨主题稳定的视觉特征
├── reproduction.yaml            # 媒介、材料和构建顺序
├── relations.yaml               # 相关流派、概念和边界
├── palette/palette.json         # 色彩角色和值
├── prompts/base.txt             # 基础 Prompt
├── prompts/negative.txt         # 负面约束
├── evaluation.yaml              # 生成后的检查标准
├── references/manifest.csv      # 来源、许可、署名和本地素材路径
├── provenance.yaml              # 研究状态和权利边界
├── resource.yaml                # 注册表资源契约
├── examples/generated/          # 待审核的匿名生图样例
├── examples/accepted/           # 通过人工审核的样例
├── examples/rejected/           # 可选的失败边界样例
├── gallery-16x9.jpg             # 原生横版 16:9 的已清权或新生成代表图
└── README.md / README.en.md     # 面向使用者的双语说明
```

支持的 `kind` 为 `artist`、`photographer`、`movement`、`school`、`technique`、`preset` 和 `game_art`；支持的 `domain` 为 `painting`、`photography`、`printmaking`、`design`、`game_art` 和 `hybrid`。

## 模板化创建方式

不要从现有艺术家或游戏包复制目录。使用脚手架会自动创建完整结构、双语 README、来源目录、Prompt、评估骨架、权利说明和代表图占位文件：

```powershell
python tools/new-style-package.py `
  --kind artist `
  --id coastal-noir `
  --name "中文风格名" `
  --domain painting `
  --summary "用可观察的媒介、构图、光线、色彩和表面规则描述这个独立风格包。"
```

脚手架会拒绝覆盖已有目录。没有来源参数时生成 L1 研究草稿；如果已有可追溯来源，可以同时生成 L2 包：

```powershell
python tools/new-style-package.py `
  --kind photographer `
  --id example-photography-package `
  --name "中文摄影风格名" `
  --domain photography `
  --summary "用可观察的镜头、构图、光线、色彩和颗粒规则描述这个摄影风格包。" `
  --source-url "https://example.org/source" `
  --source-title "来源页面或作品集标题" `
  --source-creator "作者或机构" `
  --source-attribution "使用时应保留的署名信息"
```

模板文件位于 [`templates/style-package`](templates/style-package)，其中 [`TEMPLATE.md`](templates/style-package/TEMPLATE.md) 解释每个文件的用途，英文说明见 [`TEMPLATE.en.md`](templates/style-package/TEMPLATE.en.md)。模板不在 `style-packages/` 下，因此不会被正式包扫描器收录。

创建后按以下顺序完善：

1. 替换所有 `TODO`，把身份、视觉签名、复现、调色板、评估和 Prompt 写成具体的、与主题无关的规则；
2. 在 `references/manifest.csv` 添加来源，并在 `provenance.yaml` 说明研究范围、署名和再分发边界；
3. 将代表图替换为原生横版 16:9（宽高比 16:9）的新生成、公共领域或明确允许再分发图片；不要先生成竖版图再裁成画廊图，也不要因为图片能在网上看到就直接打包；
4. 把新生成样例放在 `examples/generated/`，只有通过人工审核并附带元数据后才放入 `examples/accepted/`；
5. 发布已有包的修改时更新版本号和 `version.md`；
6. 运行完整校验后再提交 Pull Request。

## 校验命令

```powershell
python tools/scaffold-resource-manifests.py style-packages --force
python tools/build-registry.py
python tools/validate-package.py style-packages
python tools/validate-resources.py style-packages
python tools/validate-benchmarks.py style-packages
python -m unittest discover -s tests -v
python tools/validate.py
python scripts/validate-style-json.py
git diff --check
```

工程代码必须保持模型无关、风格无关。编译器、mask 适配器、预检和评估器不能把某一个艺术家、调色板、模型或生图平台写死。

## 继承的 `style.json` 预设

如果只是扩展兼容画廊，请修改：

```text
styles/<slug>/
├── style.json
├── README.md
└── preview.*
```

保持原有字段约定并运行：

```powershell
python scripts/validate-style-json.py
```

新内容优先放入 `style-packages/`，不要把继承条目静默改写成新的许可证或署名声明。

## Pull Request 清单

- [ ] 改动位于正确的风格包或工程层；
- [ ] 外部来源具有 URL、权利状态和署名信息；
- [ ] 没有加入未授权的作品、截图、Logo、品牌或私有素材；
- [ ] 生图样例已标为生成内容，且没有错误归属于参考对象；
- [ ] 代码和规则保持模型无关、风格无关；
- [ ] 相关校验和测试通过；
- [ ] 文档、示例和当前 Schema 一致；
- [ ] 原有许可证和版权声明得到保留。

如果无法确认素材是否可以再分发，请先提交 Issue，提供来源链接和使用计划，不要直接提交文件。
