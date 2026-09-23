source: https://docs.vllm.ai/en/latest/api/vllm/ir/ops/
lastmod: 2026-09-23

#

`vllm.ir.ops`

[¶](https://docs.vllm.ai#vllm.ir.ops)

Modules:

-
–[activation](https://docs.vllm.ai/activation/#vllm.ir.ops.activation) -
–[layernorm](https://docs.vllm.ai/layernorm/#vllm.ir.ops.layernorm)

Functions:

-
–[fused_add_rms_norm](https://docs.vllm.ai#vllm.ir.ops.fused_add_rms_norm)Fused add and weighted root-mean-square layer normalization.

-
–[gelu_and_mul_sparse](https://docs.vllm.ai#vllm.ir.ops.gelu_and_mul_sparse)Apply Gaussian sparsification, GELU, and gated multiplication.

-
–[rms_norm](https://docs.vllm.ai#vllm.ir.ops.rms_norm)Weighted root-mean-square layer normalization.


##

`fused_add_rms_norm(x, x_residual, weight, epsilon, variance_size=None)`

[¶](https://docs.vllm.ai#vllm.ir.ops.fused_add_rms_norm)

Fused add and weighted root-mean-square layer normalization.

## Source code in `vllm/ir/ops/layernorm.py`


##

`gelu_and_mul_sparse(x, std_multiplier, approximate='none')`

[¶](https://docs.vllm.ai#vllm.ir.ops.gelu_and_mul_sparse)

Apply Gaussian sparsification, GELU, and gated multiplication.

## Source code in `vllm/ir/ops/activation.py`


##

`rms_norm(x, weight, epsilon, variance_size=None)`

[¶](https://docs.vllm.ai#vllm.ir.ops.rms_norm)

Weighted root-mean-square layer normalization.