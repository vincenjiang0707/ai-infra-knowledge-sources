# [Issue #367] question about fp8fp4 mega moe weights load

source: https://github.com/deepseek-ai/DeepGEMM/issues/367
state: open | updated: 2026-06-29T09:51:33Z
labels: 

## 正文

why smem_sfb full barrier need to * 2:https://github.com/deepseek-ai/DeepGEMM/blob/54e22612409371d6364144b69086735beb54e98b/deep_gemm/include/deep_gemm/impls/sm100_fp8_fp4_mega_moe.cuh#L757

## 评论 (1)

### xuzhiyuan1 · 2026-06-29

2-SM UMMA
