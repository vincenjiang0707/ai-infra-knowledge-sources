# [Issue #224] AttributeError: module 'deep_gemm' has no attribute 'gemm_fp8_fp8_bf16_nt'

source: https://github.com/deepseek-ai/DeepGEMM/issues/224
state: closed | updated: 2025-12-05T09:00:26Z
labels: 

## 正文

We encountered an error during testing on the H100:

```
Traceback (most recent call last):
  File "/home/sr5/***/gemm_fp8.py", line 23, in <module>
    deep_gemm.gemm_fp8_fp8_bf16_nt(
**AttributeError: module 'deep_gemm' has no attribute 'gemm_fp8_fp8_bf16_nt'**

```
The source code is as follows:
```
import torch
import deep_gemm

M, K, N = 4096, 7168, 2112

lhs_data = torch.randn(M, K, device="cuda")
lhs_fp8, lhs_scale = deep_gemm.per_token_cast_to_fp8(lhs_data) # 使用库函数进行转换

# 输入矩阵RHS (Right-Hand Side)，形状为 [N, K] (注意：函数默认预期B矩阵是转置的，即nt格式)
rhs_data = torch.randn(N, K, device="cuda")
rhs_fp8, rhs_scale = deep_gemm.per_block_cast_to_fp8(rhs_data, use_ue8m0=True) # 使用库函数进行转换

output = torch.empty(M, N, dtype=torch.bfloat16, device="cuda")

deep_gemm.gemm_fp8_fp8_bf16_nt(
    (lhs_fp8, lhs_scale), 
    (rhs_fp8, rhs_scale), 
    output
)

```
I'd like to know where the problem lies; is it that I'm using it incorrectly?

## 评论 (1)

### LyricZhao · 2025-12-05

It is `fp8_gemm_nt` not `gemm_fp8_fp8_bf16_nt`.
