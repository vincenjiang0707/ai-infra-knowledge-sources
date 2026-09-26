# [Issue #132] The replacement of deep_gemm.wgrad_gemm_fp8_fp8_fp32_nt after Add more GPU architectures support (#112)

source: https://github.com/deepseek-ai/DeepGEMM/issues/132
state: closed | updated: 2025-10-09T01:08:10Z
labels: 

## 正文

Hello,

Thanks for adding the backward support! But the original backward kernel wgrad_gemm_fp8_fp8_fp32_nt is removed by #112.
Which kernel should I use with latest main branch?

Thanks!

## 评论 (3)

### LyricZhao · 2025-07-30

Sorry, we currently remove it and plan to add a faster impl for that later. Maybe in the next two weeks.

### haochengxi · 2025-10-07

Hi, are there any updates on the weight gradient kernel? Thanks for the amazing work!

### LyricZhao · 2025-10-09

Already included in `fp8_gemm_nt` (https://github.com/deepseek-ai/DeepGEMM/blob/main/csrc/apis/gemm.hpp#L14) with `recipe=(1, 1, 128)`. Kernel code: https://github.com/deepseek-ai/DeepGEMM/blob/main/deep_gemm/include/deep_gemm/impls/sm90_fp8_gemm_1d2d.cuh.

Closing this issue now.
