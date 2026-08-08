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

## 扩充批次

后续扩充按实际范围划分批次，不设固定包数量，也不以修改几个索引文件或复制模板来凑数。先用 [`templates/expansion-batch.yaml`](templates/expansion-batch.yaml) 登记独立包和分类计划，再按“研究 → 建包 → 生图 → 审核 → 校验”的顺序完成。每个包单独提交一个 commit；批次画廊、总 README 和统计更新使用独立的批次集成 commit。

每个包必须先获取可追溯的原作品或一手视觉资料，再提取跨主题稳定的视觉规则；只使用文字介绍不能作为成熟包的唯一依据。不能再分发的作品只保留来源链接和描述，不能把桥梁、房屋、人物、城市、花卉、车辆、地标或固定叙事写进基础 Prompt。批次状态和验收门槛见[风格包扩充工作流](docs/EXPANSION-WORKFLOW.md)；批次清单可运行：

```powershell
python tools/validate-expansion-batch.py batches/2026-08-batch-01.yaml
```

清单必须含至少一个不同包 ID，分类计划与包清单一致；只有登记的全部包都通过来源、权利、结构、主体独立性、代表图、双语 README 和完整校验后，才能标记为 `complete`。

创建后按以下顺序完善：

1. 替换所有 `TODO`，把身份、视觉签名、复现、调色板、评估和 Prompt 写成具体的、与主体无关的规则；基础 Prompt 必须保留 `{SUBJECT}` / `{LOCATION}` 占位符，并包含主体独立契约；
2. 不得把桥梁、房屋、城市、人物、花卉、车辆、地标或固定叙事写成默认生成内容。具体场景只能放在 `examples/` 或 benchmark，并明确标注为测试示例；
3. 在 `references/manifest.csv` 添加来源，并在 `provenance.yaml` 说明研究范围、署名和再分发边界；
4. 将代表图替换为原生横版 16:9（宽高比 16:9）的新生成、公共领域或明确允许再分发图片；不要先生成竖版图再裁成画廊图，也不要因为图片能在网上看到就直接打包；
5. 把新生成样例放在 `examples/generated/`，只有通过人工审核并附带元数据后才放入 `examples/accepted/`；
6. 发布已有包的修改时更新版本号和 `version.md`；
7. 运行完整校验后再提交 Pull Request。

批次级工作还必须满足：清单中的每个实际包条目都能追溯到包路径、单包 commit 和总画廊链接；未完成的包不得只通过更新总 README 来宣称完成。

## 校验命令

```powershell
python tools/scaffold-resource-manifests.py style-packages --force
python tools/build-registry.py
python tools/validate-package.py style-packages
python tools/validate-resources.py style-packages
python tools/validate-benchmarks.py style-packages
python tools/validate-subject-independence.py style-packages
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
- [ ] 基础 Prompt 与具体主体无关，示例场景没有混入基础规则；
- [ ] 原有许可证和版权声明得到保留。

如果无法确认素材是否可以再分发，请先提交 Issue，提供来源链接和使用计划，不要直接提交文件。
