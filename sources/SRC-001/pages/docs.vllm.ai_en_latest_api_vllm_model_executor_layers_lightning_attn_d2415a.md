source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/lightning_attn/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.lightning_attn`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn)

Functions:

-
–[lightning_attention](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.lightning_attention)Apply lightning attention algorithm

-
–[linear_decode_forward_triton](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton)Perform linear attention decoding using Triton kernels.


##

`_linear_attn_decode_kernel(q_ptr, k_ptr, v_ptr, kv_cache_ptr, slope_rate, slot_idx, output_ptr, D, qkv_b_stride, qkv_h_stride, cache_b_stride, cache_h_stride, cache_d0_stride, cache_d1_stride, pad_slot_id, BLOCK_SIZE)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn._linear_attn_decode_kernel)

Kernel for linear attention decoding with KV cache.

This kernel computes attention for a single token using the KV cache.

## Source code in `vllm/model_executor/layers/lightning_attn.py`


|
|

##

`lightning_attention(q, k, v, ed, block_size=256, kv_history=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.lightning_attention)

Apply lightning attention algorithm to compute attention efficiently.

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.lightning_attention(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Query tensor of shape [batch, heads, seq_len, dim]

-

(`k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.lightning_attention(k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Key tensor of shape [batch, heads, seq_len, dim]

-

(`v`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.lightning_attention(v))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Value tensor of shape [batch, heads, seq_len, dim_v]

-

(`ed`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.lightning_attention(ed))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Decay rate tensor of shape [heads]

-

(`block_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.lightning_attention(block_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`256`

) –Size of blocks for block-sparse attention

-

(`kv_history`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.lightning_attention(kv_history))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional key-value history from previous computations


Returns:

## Source code in `vllm/model_executor/layers/lightning_attn.py`


##

`linear_decode_forward_triton(q, k, v, kv_caches, slope_rate, slot_idx, BLOCK_SIZE=32)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton)

Perform linear attention decoding using Triton kernels.

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Query tensor of shape [B, H, 1, D]

-

(`k`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton(k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Key tensor of shape [B, H, 1, D]

-

(`v`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton(v))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Value tensor of shape [B, H, 1, D]

-

(`kv_caches`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton(kv_caches))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Key-value cache tensor

-

(`slope_rate`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton(slope_rate))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Decay rate tensor

-

(`slot_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton(slot_idx))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Slot indices for batches

-

(`BLOCK_SIZE`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.lightning_attn.linear_decode_forward_triton(BLOCK_SIZE))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`32`

) –Size of blocks for processing


Returns:

-
(`output`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Attention output tensor