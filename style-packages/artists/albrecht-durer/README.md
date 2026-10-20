# 阿尔布雷希特·丢勒

> 类型：艺术家 · 领域：绘画


![阿尔布雷希特·丢勒代表图](gallery-16x9.jpg)

## 这个包抓住什么

以精确轮廓、细密排线、结构化明暗和纸面印痕组织画面。

丢勒的力量不在于把画面变成古典题材，而在于线条如何承担体积、材质和秩序。这个包把这种观察方法迁移到任意主体上。

## 视觉签名

- precise contour drawing
- fine cross-hatching
- structured value modeling
- paper and plate impression

## 主体独立性

这个包只负责视觉语言，不规定固定物体、人物、地点或故事。代表图中的内容只是演示主体。使用时请把 {SUBJECT}、{LOCATION} 和其他占位内容换成你的需求。

## 生成提示词

~~~
Apply a Northern Renaissance printmaking language: precise contour drawing, disciplined cross-hatching, measured value structure, tactile paper impression, and careful material description. Keep the requested subject, setting, count, and action unchanged; the style controls visual treatment only.
~~~

负面约束见 [prompts/negative.txt](prompts/negative.txt)，完整参数见 [reproduction.yaml](reproduction.yaml)。

## 参考与权利边界

本包依据公开机构或官方页面提取可观察的视觉线索，仅保存来源链接，不复制原作图像、角色、关卡、标志或版式：

- [大都会艺术博物馆：散步](https://www.metmuseum.org/art/collection/search/336219)

## 文件

- [identity.yaml](identity.yaml)
- [visual-signature.yaml](visual-signature.yaml)
- [prompts/](prompts/)
- [examples/generated/](examples/generated/)
- [evaluation.yaml](evaluation.yaml)

## 只使用这个包

1. 下载本目录，阅读 identity.yaml、visual-signature.yaml 和 reproduction.yaml。
2. 打开 prompts/base.txt，把主题替换成自己的内容；负面约束见 prompts/negative.txt。
3. 选择一种执行方式：把风格包交给具备生图能力的 Agent；复制 Prompt 到生图平台并配置自己的 API Key；或将 Prompt、参考清单和调色板导入本地模型与 ComfyUI 工作流。
4. 参考图只用于理解可观察特征，不要复制原作的具体构图、人物、文字、商标或可识别资产。
5. 模型、API Key、生成图片和存储由使用者自行管理；本仓库不托管在线生图服务。

## 新架构：刻线、明暗与材质（实验）

[`art-direction.yaml`](art-direction.yaml) 使用方向格式 2.1.0，把明暗写成随形线条：先确立轮廓，再用顺着形体的平行排线表现中间调，最深处才少量交叉加密；亮部保留纸白。调用者可通过 `rounded-folded-or-recessed-surface` 和 `multiple-visible-materials` 只启用对应表面的排线与材质线组规则。它不会自动加入历史人物、动物、宗教叙事或丢勒签名。

```powershell
python tools/compile-style.py style-packages/artists/albrecht-durer --direction package --subject "An ordinary ceramic cup on a windowsill" --output runs/style-v2/durer-job.json
```

方向仍处于实验状态。美国国家美术馆与大都会艺术博物馆关于版画线条和排线的资料支持这些观察；跨材质与跨题材表现仍待评审。

## 新旧架构视觉对照

查看[同题样图、编译任务和复核限制](comparisons/README.md)。该对照是单题材初步检查，方向仍处于实验状态。
