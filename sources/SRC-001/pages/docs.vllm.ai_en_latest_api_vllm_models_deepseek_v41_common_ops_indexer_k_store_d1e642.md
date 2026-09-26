source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v41/common/ops/indexer_k_store/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v41.common.ops.indexer_k_store`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store)

Indexer K production for DeepSeek V4.1 kv-source layers.

In v4.1 the index key is derived from the *main* compressor's latent: `k = k_norm(wk(latent))`

(reference model.py Indexer.forward), then RoPE'd at the group's first-token position and MXFP4/FP8-quantized into the paged indexer K cache. The `wk(latent)`

GEMM runs in torch; this kernel fuses the remaining k_norm → RoPE → quant → paged store, one program per token.

Unlike the legacy (v4.0) indexer path there is no per-token pooling from a compressor state cache: the latent already stands for a whole group, so only group-boundary tokens `(position + 1) % compress_ratio == 0`

produce a key.

Functions:

-
–[indexer_k_norm_rope_store](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store)k_norm → RoPE → quant → paged store for indexer keys.


##

`indexer_k_norm_rope_store(k_pre, positions, cos_sin_cache, rms_norm_weight, rms_norm_eps, k_cache, kv_slot_mapping, compress_ratio, use_fp4_cache)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store)

k_norm → RoPE → quant → paged store for indexer keys.

Parameters:

-

(`k_pre`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(k_pre))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_tokens, 128] bf16, the

`wk(latent)`

projection. Only group-boundary rows are read. -

(`positions`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(positions))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_tokens] int64 token positions.

-

(`cos_sin_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(cos_sin_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[max_pos, rope_head_dim] GPT-J layout (cos half, then sin half), from the layer's compress-RoPE instance.

-

(`rms_norm_weight`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(rms_norm_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[128] k_norm weight.

-

(`rms_norm_eps`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(rms_norm_eps))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Epsilon of the k_norm RMSNorm.

-

(`k_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(k_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)uint8 paged indexer cache [num_blocks, block_size, row_bytes].

-

(`kv_slot_mapping`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(kv_slot_mapping))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_tokens] slots in the indexer cache (-1 = skip).

-

(`compress_ratio`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(compress_ratio))

) –[int](https://docs.python.org/3/builtins/functions.html#int)group size; keys are emitted at group boundaries.

-

(`use_fp4_cache`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v41.common.ops.indexer_k_store.indexer_k_norm_rope_store(use_fp4_cache))

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)MXFP4 (2 nibbles/byte + ue8m0 per 32) when True, else per-token FP8 with a single fp32 scale.