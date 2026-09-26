# [Issue #79] Input Tensor Precision

source: https://github.com/ScalingIntelligence/KernelBench/issues/79
state: closed | updated: 2025-11-05T08:07:05Z
labels: enhancement

## 正文

To go in more detail

Right now we use PyTorch's default `FP32` as default input tensor precision for the initial version of KernelBench.

Imo I think we should support more precision, especially `BF16`, to enable better TensorCore usage. 

We might need to update the associated prompt context and tolerance as well!

## 评论 (1)

### simonguozirui · 2025-11-05

Addressed in #80. thanks for @hqjenny and @charleshong3 for the suggestion and @PaliC and @nathanjpaek for helping.
