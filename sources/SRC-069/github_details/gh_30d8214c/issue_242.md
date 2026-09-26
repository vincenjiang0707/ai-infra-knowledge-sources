# [Issue #242] [Bug] Incorrect usage of SM100ArchSpec in sm90_bf16_k_grouped_gemm

source: https://github.com/deepseek-ai/DeepGEMM/issues/242
state: closed | updated: 2026-01-06T01:56:55Z
labels: 

## 正文

I noticed a potential copy-paste error in this function `sm90_bf16_k_grouped_gemm`, the code currently uses SM100ArchSpec to calculate the block sizes for TMA descriptors. Since this file is intended for SM90 implementation, this appears to be incorrect.

https://github.com/deepseek-ai/DeepGEMM/blob/9b680f428484625f4f35dc3617f134187c6bcd4a/csrc/jit_kernels/impls/sm90_bf16_gemm.hpp#L259-L274


## 评论 (1)

### zheanxu · 2026-01-06

Thanks for the heads up! Fixed in #270 
