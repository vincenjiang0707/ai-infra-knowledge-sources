# [Issue #41] Support StreamK when scheduling

source: https://github.com/deepseek-ai/DeepGEMM/issues/41
state: closed | updated: 2025-11-21T08:12:22Z
labels: 

## 正文

Could DeepGEMM support StreamK schedule while K > 3N in some situation?  That will make gemm faster. Like this issue: https://github.com/vllm-project/vllm/pull/12978

## 评论 (2)

### LyricZhao · 2025-03-05

We may later (no sure the date) add such support, currently no plan. Thanks for your feedback, anyway :)

### Insideyyy · 2025-09-05

We added split-k optimization in PR #186, which delivers notable speedups when `m x n` is too small to saturate SMs.
