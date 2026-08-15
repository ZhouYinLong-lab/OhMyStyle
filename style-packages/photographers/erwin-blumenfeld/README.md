# 埃尔温·布卢门菲尔德

> 类型：摄影师 · 领域：摄影

## 这个包抓住什么

以几何裁切、透明叠层、负片感、明暗反差和摄影实验重组现实。

布卢门菲尔德的实验性很适合转译为生成规则：先保证摄影逻辑，再用裁切、叠层和反转改变观看方式。

## 视觉签名

- graphic cropping
- transparent overlays
- solarization or negative-like tonal reversal
- hard and soft light contrast

## 主体独立性

这个包只负责视觉语言，不规定固定物体、人物、地点或故事。代表图中的内容只是演示主体。使用时请把 {SUBJECT}、{LOCATION} 和其他占位内容换成你的需求。

## 生成提示词

~~~
Apply an experimental mid-century photographic language: graphic crop, transparent optical layers, selective tonal reversal, controlled hard-soft light contrast, and a clean studio-to-surreal transition. Preserve the user-supplied subject and avoid fashion branding or a fixed portrait scenario.
~~~

负面约束见 [prompts/negative.txt](prompts/negative.txt)，完整参数见 [reproduction.yaml](reproduction.yaml)。

## 参考与权利边界

本包依据公开机构或官方页面提取可观察的视觉线索，仅保存来源链接，不复制原作图像、角色、关卡、标志或版式：

- [MoMA: Erwin Blumenfeld](https://www.moma.org/artists/618-erwin-blumenfeld)

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
