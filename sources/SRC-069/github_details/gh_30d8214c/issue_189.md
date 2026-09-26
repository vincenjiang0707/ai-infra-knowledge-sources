# [Issue #189] 关于Wgrad 计算中 fp8_gemm_nt 输入量化方式的疑问与实验观察

source: https://github.com/deepseek-ai/DeepGEMM/issues/189
state: closed | updated: 2026-01-16T09:16:47Z
labels: 

## 正文

您好，我在研究DeepGEMM中用于权重梯度计算 `Wgrad = grad_output^T @ input` 的FP8量化实现时，遇到一个与输入张量量化策略相关的性能差异问题，希望得到您的帮助。

根据DeepSeek V3技术报告中的描述，在计算此类梯度时，通常会对 grad_output 和 input 两个输入张量采用 per-token (或per-channel) 的量化策略。然而，我在一个简化的对照实验中发现，对第二个输入张量使用 per-block 量化，反而比 per-token 量化获得了更高的数值精度。

1. B采用per channel(token) quantization
2. B采用per block quantization
```
import torch
from deep_gemm.utils.math import per_block_cast_to_fp8, per_token_cast_to_fp8, per_channel_cast_to_fp8
from deep_gemm import fp8_gemm_nn, fp8_gemm_nt
from deep_gemm.testing.numeric import calc_diff

x = torch.randn(256,128, device="cuda")
y = torch.randn(256,128, device="cuda")  # K,N
out = torch.empty((256,256), device=x.device, dtype=torch.bfloat16)
b_out = torch.empty((256,256), device=x.device, dtype=torch.bfloat16)

fp8_x = per_token_cast_to_fp8(x.contiguous(), use_ue8m0=True)
fp8_y = per_token_cast_to_fp8(y.contiguous(), use_ue8m0=True)  
block_y = per_block_cast_to_fp8(y, use_ue8m0=True)
ref = x @ y.t()
fp8_gemm_nt(fp8_x, fp8_y, out, c=None, recipe=(1,1,128))
fp8_gemm_nt(fp8_x, block_y, b_out, c=None)
print("1d1d diff:", calc_diff(ref, out))
print("1d2d diff:", calc_diff(ref, b_out))
```

出人意料的是, 我发现当B采用per block quantization的时候表现更好.
```
1d1d diff: tensor(0.0067, device='cuda:0', dtype=torch.float64)
1d2d diff: tensor(0.0007, device='cuda:0', dtype=torch.float64)
```
实验结果表明，使用 per-block 量化第二个输入张量，其结果的数值误差显著低于 per-token 量化。

基于此，我有两个问题希望请教：

技术报告理解：我对报告中梯度计算量化策略的理解（即对两个输入都使用 per-token 量化）是否准确？是否存在我遗漏的上下文或细节？

性能差异根源：若我的理解无误，为何在此场景下 per-block 量化会表现更优？这是否意味着在 fp8_gemm_nt 的 kernel 实现中，对第二个输入张量的量化方式有特殊要求或优化？

感谢您的时间与帮助！我期待能更深入地理解其中的设计原理。




## 评论 (2)

### HoshinoAkua · 2025-09-10

抱歉, 忘了说了, 我的显卡是H20, 和ds的pre-training用的都是H系列的显卡

### zheanxu · 2025-09-25

目前 DeepGEMM 没有 SM90 1D1D Kernel（应该很快会添加），上述代码 1d1d 调用的实际是 1D2D Kernel，读取到的 Scaling Factor 不正确，所以计算有误。
FP8 GEMM 典型的 diff 就是 7e-4 左右，如果正确实现 1d1d diff 也应该是 7e-4 左右。
torch.randn 产生的值比较小，此时不管使用什么量化策略，diff 都应该差不多。但是在一些存在极端值的情况下，一般来说量化的粒度越细越好
