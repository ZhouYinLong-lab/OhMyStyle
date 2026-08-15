# 凹版照相制版

> 类型：工艺与媒介 · 领域：版画与印刷

## 这个包抓住什么

以连续灰阶、油墨密度、纸面吸收和细密颗粒把摄影转化为有物质感的印刷图像。

凹版照相制版的魅力在灰阶和纸墨关系，不在于默认生成旧报纸或历史纪实。

## 视觉签名

- continuous gray scale
- ink density in shadow
- matte paper absorption
- fine plate grain

## 主体独立性

这个包只负责视觉语言，不规定固定物体、人物、地点或故事。代表图中的内容只是演示主体。使用时请把 {SUBJECT}、{LOCATION} 和其他占位内容换成你的需求。

## 生成提示词

~~~
Render the user's subject as an original photogravure-inspired image: continuous tonal scale, dense but open ink shadows, matte paper absorption, fine plate grain, and restrained monochrome or warm duotone. Keep the subject, location, and action exactly as requested; do not add a newspaper, war story, or text.
~~~

负面约束见 [prompts/negative.txt](prompts/negative.txt)，完整参数见 [reproduction.yaml](reproduction.yaml)。

## 参考与权利边界

本包依据公开机构或官方页面提取可观察的视觉线索，仅保存来源链接，不复制原作图像、角色、关卡、标志或版式：

- [美国国会图书馆：凹版照相制版工艺](https://www.loc.gov/static/collections/world-war-i-rotogravures/articles-and-essays/the-rotogravure-process/)

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
