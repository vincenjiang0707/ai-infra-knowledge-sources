# [Issue #208] Does DeepSeek V3.2 indexer logit kernels have an API for implementing bfloat16

source: https://github.com/deepseek-ai/DeepGEMM/issues/208
state: closed | updated: 2026-04-27T05:56:18Z
labels: 

## 正文

(empty)

## 评论 (1)

### zheanxu · 2025-10-22

Not currently supported, and we don't have plans to implement this. FP8 precision already provides adequate accuracy for indexer.
