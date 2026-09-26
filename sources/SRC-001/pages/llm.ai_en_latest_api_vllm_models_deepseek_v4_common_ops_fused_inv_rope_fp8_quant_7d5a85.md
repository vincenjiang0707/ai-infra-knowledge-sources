source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant)

Fused inverse RoPE + block-scaled FP8 quantization kernel for DeepseekV4 attention.

Output scale format is pre-transformed (MN-major TMA-aligned; FP32 on SM90, INT32-packed UE8M0 on SM100) so fp8_einsum skips transform_sf_into_required_layout.

Functions:

-
–[fused_inv_rope_fp8_quant](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant)Fused inverse RoPE + block-scaled FP8 quantization.


##

`fused_inv_rope_fp8_quant(o, positions, cos_sin_cache, n_groups, heads_per_group, nope_dim=448, rope_dim=64, quant_group_size=128, tma_aligned_scales=False, quantize=True)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant)

Fused inverse RoPE + block-scaled FP8 quantization.

Parameters:

-

(`o`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(o))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Attention output [num_tokens, num_heads, head_dim] bf16.

-

(`positions`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Token positions [num_tokens] int64.

-

(`cos_sin_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(cos_sin_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Precomputed [max_pos, rope_dim] with cos||sin.

-

(`n_groups`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(n_groups))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of output groups.

-

(`heads_per_group`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(heads_per_group))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Heads per group.

-

(`nope_dim`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(nope_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`448`

) –Non-RoPE dimensions per head (default 448).

-

(`rope_dim`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(rope_dim))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`64`

) –RoPE dimensions per head (default 64).

-

(`quant_group_size`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(quant_group_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`128`

) –FP8 quantization block size (default 128).

-

(`tma_aligned_scales`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(tma_aligned_scales))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Output INT32 packed UE8M0 for SM100 (True) or FP32 for SM90 (False).

-

(`quantize`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.common.ops.fused_inv_rope_fp8_quant.fused_inv_rope_fp8_quant(quantize))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Quantize the rotated output to FP8 and return its scales.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Rotated output in [T, G, D] and its FP8 scales. The scale tensor is

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)empty when quantization is disabled.


## Source code in `vllm/models/deepseek_v4/common/ops/fused_inv_rope_fp8_quant.py`


|
|