# [Issue #4905] [Feature] 咱们最新版本的lmdeploy可以加载这个 Qwen3.8-Flash吗？

source: https://github.com/InternLM/lmdeploy/issues/4905
state: open | updated: 2026-09-11T13:33:04Z
labels: 

## 正文

### Motivation

咱们最新版本的lmdeploy可以加载这个 Qwen3.8-Flash吗？
https://huggingface.co/Qwen/Qwen3.8-Flash-Next

### Related resources

_No response_

### Additional context

_No response_

## 评论 (2)

### lvhan028 · 2026-08-31

这个还没有支持

### modelpath-dev · 2026-09-11

I will take this issue. Please assign it to me.

The request is to check if the latest version of `lmdeploy` can load the `Qwen3.8-Flash` model from Hugging Face. First, I would verify if the model is compatible with the current loading mechanisms in `lmdeploy`. I would inspect the model loading code, likely in a module related to model integration, to ensure it supports the architecture and format of `Qwen3.8-Flash`. If not, I would propose a small change to add support for this specific model.

