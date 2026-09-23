source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/qwen3_dflash/
lastmod: 2026-09-23

#

`vllm.model_executor.models.qwen3_dflash`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash)

Classes:

-
–[DFlashQwen3Attention](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Attention)Attention for DFlash speculative decoding.

-
–[DFlashQwen3ForCausalLM](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3ForCausalLM) -
–[DFlashQwen3Model](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Model)

Functions:

-
–[dflash_has_any_non_causal](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.dflash_has_any_non_causal)Whether the draft needs a non-causal-capable backend, resolved from config


##

`DFlashQwen3Attention`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Attention)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Attention for DFlash speculative decoding.

Context KVs are pre-inserted into the KV cache before the forward pass. This layer handles only query tokens via standard attention. Adapted from Qwen3Attention.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Attention.forward)DFlash attention assumes that the KV cache is already populated


## Source code in `vllm/model_executor/models/qwen3_dflash.py`


|
|

###

`forward(positions, hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Attention.forward)

DFlash attention assumes that the KV cache is already populated with the context K/V from the target model's hidden states. This forward op computes attention for the query tokens only. See also: precompute_and_store_context_kv

## Source code in `vllm/model_executor/models/qwen3_dflash.py`


##

`DFlashQwen3ForCausalLM`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3ForCausalLM)

Bases: `Qwen3ForCausalLM`


Methods:

-
–[get_draft_attn_causal](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3ForCausalLM.get_draft_attn_causal)Per-layer attention causality, aligned with

-
–[precompute_and_store_context_kv](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3ForCausalLM.precompute_and_store_context_kv)Precompute projected + RoPE'd K/V and write to cache.


## Source code in `vllm/model_executor/models/qwen3_dflash.py`


|
|

###

`_read_mask_embedding()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3ForCausalLM._read_mask_embedding)

Checks for an override mask embedding in `mask_embedding.pt`

and returns it.

Some checkpoints ship a separately-trained mask embedding for the mask token, which we use to overwrite the embedding for `mask_token_id`

. This helper checks for the file, loads the pytorch tensor, and returns the embedding to use.

Returns None if the override file is not present.

## Source code in `vllm/model_executor/models/qwen3_dflash.py`


###

`get_draft_attn_causal()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3ForCausalLM.get_draft_attn_causal)

Per-layer attention causality, aligned with get_draft_kv_cache_layer_names.

###

`precompute_and_store_context_kv(context_states, context_positions, context_slot_mapping=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3ForCausalLM.precompute_and_store_context_kv)

Precompute projected + RoPE'd K/V and write to cache.

## Source code in `vllm/model_executor/models/qwen3_dflash.py`


##

`DFlashQwen3Model`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Model)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[precompute_and_store_context_kv](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Model.precompute_and_store_context_kv)Precompute K/V for context states write them into each layer's KV cache.


## Source code in `vllm/model_executor/models/qwen3_dflash.py`


|
|

###

`_build_fused_kv_buffers()`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Model._build_fused_kv_buffers)

Build fused weight buffers for precompute_and_store_context_kv.

Must be called after weights are loaded. Stacks the KV-projection weights, K-norm weights, and RoPE parameters from every attention layer so that precompute_and_store_context_kv can run one fused GEMM for all layers at once. Also aliases the weight of the hidden_norm.

## Source code in `vllm/model_executor/models/qwen3_dflash.py`


###

`precompute_and_store_context_kv(context_states, context_positions, context_slot_mapping=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.DFlashQwen3Model.precompute_and_store_context_kv)

Precompute K/V for context states write them into each layer's KV cache.

Input context states are projected to K/V, normed, and have RoPE applied. Since the context shape is different than the query shape, we can't rely on the regular forward pass to apply torch.compile and CUDA graphs to this section. As such, this function is optimized to minimize the number of torch ops present: we use fused vLLM kernels for RMSNorm and RoPE, fuse the GEMM into one large projection, and avoid cloning buffers (with .contiguous()) where possible.

When context_slot_mapping is None (e.g. during dummy_run) only the computation runs, and no K/V is written to cache.

## Source code in `vllm/model_executor/models/qwen3_dflash.py`


|
|

##

`_dflash_layer_causal(config, layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash._dflash_layer_causal)

Resolve explicit causality before falling back to legacy layer defaults.

## Source code in `vllm/model_executor/models/qwen3_dflash.py`


##

`_resolve_layer_attention(config, layer_idx)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash._resolve_layer_attention)

Resolve `(sliding_window, causal)`

for one DFlash draft layer.

+----------------------+-------------------------+--------------------------------+ | Config | `layer_type`

| *`causal`

| +======================+=========================+================================+ | `layer_types`

| SWA if `use_swa`

| True if `layer_types[i]=SWA`

| | | else `layer_types[i]`

| else False | +----------------------+-------------------------+--------------------------------+ | `layer_types=None`

| SWA | False | | + `use_swa=True`

| | | +----------------------+-------------------------+--------------------------------+ | `layer_types=None`

| Full | False | | + `use_swa=False`

| | | +----------------------+-------------------------+--------------------------------+ * If `dflash_config.causal`

is set, its value overrides `causal`

for all layers.

This is to support a varied ecosystem of checkpoints, including: - XiaomiMiMo/MiMo-V2.5-Pro-FP4-DFlash (sets "use_swa", assumes non-causal) - z-lab/gemma-4-31B-it-DFlash (has mixed layer types, assumes causal only for SWA) - z-lab/Qwen3.5-9B-DFlash ("standard" DFlash, all full attn, assumes non-causal)

## Source code in `vllm/model_executor/models/qwen3_dflash.py`


##

`dflash_has_any_non_causal(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.qwen3_dflash.dflash_has_any_non_causal)

Whether the draft needs a non-causal-capable backend, resolved from config (config mirror of the model's `get_draft_attn_causal`

, usable pre-build).