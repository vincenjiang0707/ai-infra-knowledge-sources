# [Issue #4775] [Feature] qwen3.5可以turbo后端可以开启prefill cache吗

source: https://github.com/InternLM/lmdeploy/issues/4775
state: open | updated: 2026-07-24T15:34:04Z
labels: 

## 正文

### Motivation

qwen3.5可以turbo后端可以开启prefill_cache吗 禁用多模态后可以吗

### Related resources

_No response_

### Additional context

_No response_

## 评论 (2)

### lvhan028 · 2026-07-23

main分支，turbomind 已经支持了 qwen3.5 prefix caching, both text and multimodal.

### janelu9 · 2026-07-23

> main分支，turbomind 已经支持了 qwen3.5 prefix caching, both text and multimodal.

同学们测下来 提升不多 没有vllm开启prefill cache后快的明显,什么问题
