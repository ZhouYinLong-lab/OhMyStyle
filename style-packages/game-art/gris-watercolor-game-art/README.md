# 灰烬水彩游戏美术

> 类型：游戏美术 · 领域：游戏美术

## 这个包抓住什么

以透明水彩层、渐变色域、柔和边缘和可读路径组织具有游戏空间感的画面。

这个包借鉴的是二维水彩环境的空间处理，不要求每张图都出现角色、废墟或特定叙事。

## 视觉签名

- transparent watercolor layers
- gradual palette transitions
- soft atmospheric edges
- readable 2D traversal space

## 主体独立性

这个包只负责视觉语言，不规定固定物体、人物、地点或故事。代表图中的内容只是演示主体。使用时请把 {SUBJECT}、{LOCATION} 和其他占位内容换成你的需求。

## 生成提示词

~~~
Apply an original hand-painted 2D game-art language associated with translucent watercolor layers, gradual color transitions, soft atmospheric edges, and a clear readable spatial path. Preserve the user's subject and action; do not add a named character, game interface, specific level, ruins, forest, or story event unless requested.
~~~

负面约束见 [prompts/negative.txt](prompts/negative.txt)，完整参数见 [reproduction.yaml](reproduction.yaml)。

## 参考与权利边界

本包依据公开机构或官方页面提取可观察的视觉线索，仅保存来源链接，不复制原作图像、角色、关卡、标志或版式：

- [Nomada Studio: Studio](https://nomada.studio/studio/)

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
