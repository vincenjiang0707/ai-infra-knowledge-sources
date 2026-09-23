source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_qk_norm_rope/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_qk_norm_rope`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope)

Fused QK-RMSNorm + (partial) RoPE + gate copy Triton kernel.

Currently used by the Qwen3.5 attention path (`attn_output_gate`

with NeoX-style partial RoPE). The unfused reference sequence is `split -> GemmaRMSNorm -> RoPE -> gate chunk`

; this collapses it into a single Triton launch. See :func:`fused_qk_rmsnorm_rope_gate`

.

Functions:

-
–[fused_qk_rmsnorm_rope_gate](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate)Fused split + QK-RMSNorm + (partial) RoPE + gate copy for Qwen attn.


##

`fused_qk_rmsnorm_rope_gate(q_gate, k, q_weight, k_weight, cos_sin_cache, positions, eps, num_q_heads, num_kv_heads, head_dim, rotary_dim, mrope_section=None, norm_beta=0.0)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate)

Fused split + QK-RMSNorm + (partial) RoPE + gate copy for Qwen attn.

Parameters:

-

(`q_gate`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(q_gate))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(n_tokens, num_q_heads * 2 * head_dim) -- per head: [q|gate]

-

(`k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(n_tokens, num_kv_heads * head_dim)

-

(`q_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(q_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(head_dim,) RMSNorm weight

-

(`k_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(k_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(head_dim,) RMSNorm weight

-

(`cos_sin_cache`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(cos_sin_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(max_pos, rotary_dim) packed [cos|sin]

-

(`positions`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(n_tokens,) or (3, n_tokens) int32 or int64

-

(`eps`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)RMSNorm epsilon

-

(`num_q_heads`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(num_q_heads))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of Q heads (after TP split)

-

(`num_kv_heads`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(num_kv_heads))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of KV heads (after TP split)

-

(`head_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(head_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)per-head dimension

-

(`rotary_dim`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(rotary_dim))

) –[int](https://docs.python.org/3/builtins/functions.html#int)rotary dimension; must be even and <= head_dim

-

(`mrope_section`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(mrope_section))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] |[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –interleaved T/H/W frequency counts for 2D positions

-

(`norm_beta`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_qk_norm_rope.fused_qk_rmsnorm_rope_gate(norm_beta))

, default:[float](https://docs.python.org/3/builtins/functions.html#float)`0.0`

) –scalar added to the RMSNorm weight


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)(q_out, k_out, gate_out) -- all contiguous (n_tokens, heads * head_dim).

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`gate_out`

is the raw (pre-sigmoid) gate.

## Source code in `vllm/model_executor/layers/fused_qk_norm_rope.py`


|
|