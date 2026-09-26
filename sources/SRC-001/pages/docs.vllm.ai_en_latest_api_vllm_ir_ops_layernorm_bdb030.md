source: https://docs.vllm.ai/en/latest/api/vllm/ir/ops/layernorm/
lastmod: 2026-09-24

#

`vllm.ir.ops.layernorm`

[¶](https://docs.vllm.ai#vllm.ir.ops.layernorm)

Functions:

-
–[fused_add_rms_norm](https://docs.vllm.ai#vllm.ir.ops.layernorm.fused_add_rms_norm)Fused add and weighted root-mean-square layer normalization.

-
–[rms_norm](https://docs.vllm.ai#vllm.ir.ops.layernorm.rms_norm)Weighted root-mean-square layer normalization.


##

`fused_add_rms_norm(x, x_residual, weight, epsilon, variance_size=None)`

[¶](https://docs.vllm.ai#vllm.ir.ops.layernorm.fused_add_rms_norm)

Fused add and weighted root-mean-square layer normalization.

## Source code in `vllm/ir/ops/layernorm.py`


##

`rms_norm(x, weight, epsilon, variance_size=None)`

[¶](https://docs.vllm.ai#vllm.ir.ops.layernorm.rms_norm)

Weighted root-mean-square layer normalization.