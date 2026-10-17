# 朱利安学院

[English](README.en.md)

![朱利安学院代表图](gallery-16x9.jpg)

> **分类：** 艺术与摄影学校<br>
> **媒介领域：** 绘画<br>
> **目录：** `style-packages/schools/academie-julian`

## 简介

朱利安学院是巴黎的私人艺术教学机构。本包提炼其工作室式训练方式：观察、起稿、检查比例、反复修订，再完成必要的细节。它描述的是创作方法，不要求每张图都出现教室、画架或学生。

## 策展短评

这套风格的重点不在一间复古画室，而在画面如何被一步步建立：先看形体和比例，再比较明暗，最后决定哪里需要收细。保留少量有效的起稿痕迹，会让观察和修订过程仍可见。

## 文件导览

- `identity.yaml`：范围、开放主体策略与排除项
- `visual-signature.yaml`：跨主题稳定的训练方法特征
- `reproduction.yaml`：材料与工作顺序
- `prompts/base.txt`、`prompts/negative.txt`：基础 Prompt 与负面约束
- `palette/palette.json`：仅供画室示例参考的颜色
- `evaluation.yaml`：生成后的检查标准
- `references/manifest.csv`、`provenance.yaml`：来源与权利边界

## 来源与权利

来源清单链接至奥赛博物馆对玛丽·巴什基尔采夫及其作品《一次会议》的资料，以及大都会艺术博物馆关于十九世纪法国女性艺术家的文章。奥赛资料说明她曾在朱利安学院学习，并介绍该校为女性提供模特写生课程的历史。仓库不包含馆藏作品或照片。

## 使用此包

读取 `prompts/base.txt`，替换 `{SUBJECT}` 与 `{LOCATION}`，并一并提交 `prompts/negative.txt`。此包应以观察、比例、明暗分组和选择性修订影响你指定的主体，不会自行添加学生、模特、画室或时代服饰。生成后按 `evaluation.yaml` 检查需求遵循和过程痕迹。

代表图和样例是新生成的画室场景，尚待人工审核，不是档案图像，也不是朱利安学院学生的历史作品。
