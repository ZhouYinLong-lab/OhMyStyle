# 阿尔布雷希特·丢勒

> 类型：艺术家 · 领域：绘画

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
