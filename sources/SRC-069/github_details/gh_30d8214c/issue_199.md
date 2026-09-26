# [Issue #199] The comparison between cublaslt and deepgemm in test_fp8.py is unaligned

source: https://github.com/deepseek-ai/DeepGEMM/issues/199
state: closed | updated: 2026-04-27T05:55:06Z
labels: 

## 正文

It's great that PR #198 added cublas implementation to test_fp8.py, so we can directly observe the performance differences.
That said, I noticed the cublas implementation uses tensorwise scaling(cublas default behavior) instead of blockwise scaling, which makes the comparison with deepgemm less fair and potentially misleading.
Would it be possible to align the scaling strategy? I suppose cublas currently has supported the blockwise scaling strategy same with deepgemm: https://docs.nvidia.com/cuda/cublas/#element-1d-and-128x128-2d-block-scaling-for-fp8-data-types

## 评论 (1)

### zheanxu · 2026-04-27

Thanks for the detailed observation! This was intentional: we chose tensorwise scaling to keep the cuBLAS baseline simple and use it as a "no block scaling overhead" reference point for comparison. 
