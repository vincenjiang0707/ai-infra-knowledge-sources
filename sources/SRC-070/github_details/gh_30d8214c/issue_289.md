# [Issue #289] Question about the scale factor layout

source: https://github.com/deepseek-ai/DeepGEMM/issues/289
state: closed | updated: 2026-04-17T02:35:49Z
labels: 

## 正文

Recently I am reading the code of sm100 fp8 GEMM. I have a question:
Why must the scale factor be MN-major? Is it because this provides better performance or is it due to hardware constraints? Thank you for your reply.

## 评论 (1)

### zheanxu · 2026-04-17

Hi! This is because every time TMA loads the scale factors, it needs to load a tile of `block_m * 1` or `block_n * 1`. This requires the scale factor data to be contiguous along the M or N dimension, hence the MN-major layout requirement.
