# [Issue #321] question about megamoe

source: https://github.com/deepseek-ai/DeepGEMM/issues/321
state: closed | updated: 2026-04-30T07:43:41Z
labels: 

## 正文

hello~ I have some questions about the two comments in the code.

1. "Only use first 16 lanes for address" — I see that stmatrix.x4 is used, which seems to require all 32 lanes to provide addresses. [link0](https://github.com/deepseek-ai/DeepGEMM/blob/main/deep_gemm/include/deep_gemm/impls/sm100_fp8_fp4_mega_moe.cuh#L1163)
2. What does the phrase 'One warp per row' mean in there? I personally feel that one warp processes two tokens. [link1](https://github.com/deepseek-ai/DeepGEMM/blob/main/deep_gemm/include/deep_gemm/impls/sm100_fp8_fp4_mega_moe.cuh#L1186)

thx~

## 评论 (1)

### zheanxu · 2026-04-30

Thanks for your careful review. You're right — both comments are outdated after recent code changes. We'll update them to reflect the current behavior. Appreciate you pointing this out!

