# [Issue #1512] 在MMMU数据集上评测Qwen3.6-35B-A3B得分79,官方是81.7。这是正常的ma

source: https://github.com/modelscope/evalscope/issues/1512
state: closed | updated: 2026-07-24T07:59:41Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [x] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [x] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [x] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

请简要描述您遇到的问题。

## EvalScope 版本（必填）
1.9.0

## 使用的工具
- [x] Native / 原生框架
- [ ] Opencompass backend
- [ ] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

请提供您执行的主要代码或指令。

## 错误日志

请粘贴完整的错误日志或控制台输出。

## 运行环境

- 操作系统：
- Python版本：

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (2)

### Yunnglin · 2026-07-24

你好，感谢反馈 👍79 vs 81.7 这种 2~3 个点的差距在多模态评测里基本属于正常范围，MMMU 对 prompt、答案抽取、采样参数、图片处理都比较敏感。不过你提供的信息太少（运行命令、参数、日志、环境都空着），暂时没法帮你定位具体原因。麻烦先补充完整的运行命令 / 配置（含 `generation_config`）、模型部署方式，以及 `outputs/<timestamp>/reviews/` 里几条判错样本，方便进一步排查。


### fancy1223 · 2026-07-24

谢谢解答～
