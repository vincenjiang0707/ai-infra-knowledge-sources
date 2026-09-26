# [Issue #21] Inefficient baseline

source: https://github.com/ScalingIntelligence/KernelBench/issues/21
state: closed | updated: 2026-01-20T04:18:14Z
labels: 

## 正文

https://github.com/ScalingIntelligence/KernelBench/blob/a548072f2d6223e7d98e5fd8c99fa4d766c4160d/KernelBench/level1/12_Matmul_with_diagonal_matrices_.py#L23

Here the baseline implementation is too inefficient, allowing [people to claim they can achieve a 55x speedup](https://pub.sakana.ai/ai-cuda-engineer/leaderboard)

A possible way would be: `return A.unsqueeze(1) * B`

## 评论 (2)

### simonguozirui · 2026-01-18

I agree with this observation (causing a huge speedup easily) and have been wanting to update this for a long time. 
The goal of a benchmark is to make it [hard to beat](https://ofir.io/How-to-Build-Good-Language-Modeling-Benchmarks/).
Will put in a fix soon.

### simonguozirui · 2026-01-20

Addressed in #127. Thanks so much for the suggestion (and also discussion with @jordan-benjamin regarding this), and the broadcast version is more suitable as a baseline. 

Also took a look at the upper/lower triangular matmul problems Level 1 [14, 15]. They use `torch.triu(torch.matmul(A, B))` which is the standard PyTorch approach since there's no simple broadcasting equivalent for triangular matmul. While cuBLAS does provide specialized [TRMM](https://docs.nvidia.com/cuda/cublas/?utm_source=chatgpt.com#cublas-t-trmm) kernels for this case, they are not exposed through PyTorch, so leveraging them would require custom kernels.
