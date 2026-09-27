# [Issue #4464] [Feature] 现在可以支持Qwen3.5 4bit 量化吗？

source: https://github.com/InternLM/lmdeploy/issues/4464
state: open | updated: 2026-03-26T05:06:20Z
labels: 

## 正文

### Motivation

现在可以支持Qwen3.5 4bit 量化吗？我看官方文档中4bit 的还是不行，但是github上更新日志是支持。

### Related resources

_No response_

### Additional context

_No response_

## 评论 (1)

### lvhan028 · 2026-03-26

lmdeploy lite 模块还没有加 qwen3.5 的支持。
不过，lmdeploy turbomind 引擎可以支持 qwen3.5 awq 模型推理了。
https://huggingface.co/QuantTrio/Qwen3.5-35B-A3B-AWQ
