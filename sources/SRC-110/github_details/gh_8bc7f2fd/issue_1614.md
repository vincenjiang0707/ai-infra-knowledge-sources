# [Issue #1614] Evalscope不支持ds-v4-flash压测

source: https://github.com/modelscope/evalscope/issues/1614
state: closed | updated: 2026-08-21T02:14:32Z
labels: 

## 正文

## 自查清单

在提交 issue 之前，请确保您已完成以下步骤:
- [ ] 我已仔细阅读了[相关使用说明文档](https://evalscope.readthedocs.io/zh-cn/latest/get_started/parameters.html)
- [ ] 我已查看了[常见问题解答](https://evalscope.readthedocs.io/zh-cn/latest/get_started/faq.html)
- [✔ ] 我已搜索并查看了现有的 issues，确认这不是一个重复的问题

## 问题描述

请简要描述您遇到的问题。

## EvalScope 版本（必填）
Version: 1.10.0

## 使用的工具
- [ ] Native / 原生框架
- [ ] Opencompass backend
- [ ✔] VLMEvalKit backend
- [ ] RAGEval backend
- [ ] Perf / 模型推理压测工具
- [ ] Arena / 竞技场模式

## 执行的代码或指令

evalscope perf \
  --parallel 1 10 50 100 200 \
  --number 10 20 100 200 400 \
  --model DeepSeek-V4-Flash-0731 \
  --url http://127.0.0.1:8801/v1/chat/completions \
  --api openai \
  --dataset random \
  --max-tokens 1024 \
  --min-tokens 1024 \
  --prefix-length 0 \
  --min-prompt-length 1024 \
  --max-prompt-length 1024 \
  --tokenizer-path ../ds-v4-flash-w4a8\
  --extra-args '{"ignore_eos": true}'

## 错误日志

tokenizer 不支持......................................

## 运行环境

- 操作系统：
- Python版本：

## 其他信息

如果有其他相关信息，请在此处提供。


## 评论 (1)

### Yunnglin · 2026-08-21

这个问题与 #1548 相同。DeepSeek V4 官方 tokenizer 未提供 Jinja 格式的 chat template，而 random 数据集必须指定 `--tokenizer-path`。可以参考[该方案](https://github.com/modelscope/evalscope/issues/1548#issuecomment-5290844392)，将对应的 `chat_template.jinja` 放入 `../ds-v4-flash-w4a8/` 模型目录后，保持原命令重新运行。
