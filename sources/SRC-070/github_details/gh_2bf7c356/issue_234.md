# [Issue #234] DeepEP currently support NVIDIA A800？

source: https://github.com/deepseek-ai/DeepEP/issues/234
state: closed | updated: 2026-09-20T01:56:39Z
labels: 

## 正文

Does DeepEP currently support multi-GPU configurations with NVIDIA A800?

## 评论 (1)

### LyricZhao · 2025-06-20

For intranode kernels, yes (with NVLink connections)! For internode kernels, currently not, but it is very easy to modify, we didn't do it just because we don't have such clusters to test.
