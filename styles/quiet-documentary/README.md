# Quiet Documentary

[English](README.en.md)

## 简介

Quiet Documentary 是一个面向日常室内、人物和静物的纪实摄影风格包。它使用柔和的可用光、低饱和度、克制的反差和有观察距离的取景，让场景保留生活痕迹，而不是看起来像商业棚拍。

## 核心特征

- 自然光或窗光，方向柔和；
- 低饱和度与略偏冷的中性色；
- 中景、环境人像和不刻意摆拍的距离；
- 不对称构图与有意识的留白；
- 中等景深、轻微颗粒和真实的表面瑕疵；
- 保留自然肤色、使用痕迹和小尺度的不完美。

## 适合的主题

日常人物、安静室内、个人工作区、朴素静物、社区街景，以及带有使用痕迹的物件。

## 不属于此风格

硬闪光、过饱和色彩、塑料质感皮肤、极端背景虚化、强烈 HDR、居中的产品广告构图和戏剧化彩色轮廓光。

## 复现流程

1. 阅读 [`style.yaml`](style.yaml) 了解机器可读的风格身份。
2. 以 [`technique/parameters.yaml`](technique/parameters.yaml) 作为方向参考，不把它当作固定相机配方。
3. 从 [`prompts/base.txt`](prompts/base.txt) 开始，再加入自己的主题变化。
4. 对照 accepted 与 rejected 示例的标准检查结果。
5. 添加参考资料前，先在 [`metadata/sources.csv`](metadata/sources.csv) 记录来源。

## 证据状态

当前版本已经记录风格判定标准和元数据。外部参考图尚未随包分发；`references/` 与 `examples/` 中的说明文件记录了后续补充时应遵循的要求。

## 许可证

本包的文档和原创元数据遵循仓库许可证。外部参考资料和示例必须按照 [`provenance.yaml`](provenance.yaml) 记录各自的许可与署名信息。

## 只使用此包

1. 下载本目录，阅读 `style.yaml`、`visual-signature.yaml` 和 `reproduction.yaml`。
2. 打开 `prompts/base.txt`，替换主题变量；需要排除的内容参考 `prompts/negative.txt`。
3. 将 Prompt 直接复制到支持文字生图的平台，或配置自己的 API Key 后提交；也可以把 Prompt、参考清单和调色板导入本地模型或 ComfyUI。
4. 使用者自行管理模型权重、API Key 和生成图片；本仓库不托管在线生图服务。
