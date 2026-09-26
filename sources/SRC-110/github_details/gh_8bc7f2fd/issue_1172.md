# [Issue #1172] 支持自定义多模态数据集的音频和视频

source: https://github.com/modelscope/evalscope/issues/1172
state: closed | updated: 2026-08-19T09:46:16Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [ ] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

请简要描述您遇到的问题。

## EvalScope 版本（必填）
v1.4.0

## 使用的工具
- [ ] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令
\evalscope-main\evalscope\benchmarks\general_vmcq\general_vmcq_adapter.py文件
看到多模态自定义数据集中只支持了图片

<img width="3200" height="1916" alt="Image" src="https://github.com/user-attachments/assets/e6b24113-dde3-48fd-8f14-e0580f18d4b1" />



## 评论 (3)

### Yunnglin · 2026-03-31

支持音频输入，暂不支持视频输入

### AuFlow · 2026-04-13

看到多模态的通用问答类是支持音频的，选择题类好像并没有支持哎，请问后续有支持视频输入的计划嘛？


### Yunnglin · 2026-04-29

后续计划支持
