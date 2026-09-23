source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/nvidia/dspark/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.nvidia.dspark`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark)

DSpark draft model for DeepSeek-V4 (semi-autoregressive speculative decoding).

See: qwen3_dspark.py for base architecture. This one is specialized to the DSV4 DSpark, which reuses the target model's architecture similarly to MTP.

To implement non-causal attention, we leverage the sparse attention implementation to include the future query tokens in the top-k indices for each query token.

Classes:

##

`DSparkDeepseekV4ForCausalLM`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4ForCausalLM)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[compute_confidence](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4ForCausalLM.compute_confidence)Per-position acceptance probability for each drafted token.

-
–[compute_logits](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4ForCausalLM.compute_logits)Base logits U_k = lm_head(norm(head_hidden)).

-
–[load_weights](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4ForCausalLM.load_weights)Load the

`mtp.{0,1,2}.*`

draft weights from the target checkpoint.

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


|
|

###

`_remap_dspark_name(name)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4ForCausalLM._remap_dspark_name)

Map a checkpoint `mtp.{i}.*`

name to this model's parameter path.

Returns None for non-mtp weights (owned by the target model).

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


###

`compute_confidence(head_hidden, markov_embed)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4ForCausalLM.compute_confidence)

Per-position acceptance probability for each drafted token.

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


###

`compute_logits(hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4ForCausalLM.compute_logits)

Base logits U_k = lm_head(norm(head_hidden)).

###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4ForCausalLM.load_weights)

Load the `mtp.{0,1,2}.*`

draft weights from the target checkpoint.

Non-mtp weights (embed/head/main layers) belong to the target model and are skipped here. `embed_tokens`

/`lm_head`

are aliased from the target.

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


|
|

##

`DSparkDeepseekV4Model`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4Model)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[combine_hidden_states](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4Model.combine_hidden_states)main_x = main_norm(main_proj(concat of target aux hidden states)).

-
–[precompute_and_store_context_kv](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4Model.precompute_and_store_context_kv)Insert the sliding-window context KV for every draft layer.


## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


|
|

###

`combine_hidden_states(aux_hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4Model.combine_hidden_states)

main_x = main_norm(main_proj(concat of target aux hidden states)).

`aux_hidden_states`

is [T, hidden_size * len(target_layer_ids)].

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


###

`precompute_and_store_context_kv(main_x, context_positions, context_slot_mappings=None)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark.DSparkDeepseekV4Model.precompute_and_store_context_kv)

Insert the sliding-window context KV for every draft layer.

Mirrors the reference DSparkAttention: each layer derives its context KV from the SAME projected target hidden `main_x`

, via that layer's own `wkv`

+ `kv_norm`

+ RoPE + quant, then writes it at the layer's context slots.

`context_slot_mappings`

is a per-layer list (each entry is the context slot mapping for that layer's kv-cache group, since the hybrid manager may place draft layers in different groups). `None`

(or a `None`

entry) runs the projection to reserve workspace but writes nothing (profiling).

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


##

`_duplicate_context_wkv_weights(weights, num_layers)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark._duplicate_context_wkv_weights)

Load every draft layer's WKV into the cross-layer projection.

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


##

`_insert_context_kv(attn, kv, positions, slot_mapping)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.nvidia.dspark._insert_context_kv)

RoPE + quant + paged-cache insert of (already kv_norm'd) context KV.

Reuses the DSV4 fused insert ops (which also process a query; we pass a dummy query and discard it, since context tokens have no query). Mirrors `DeepseekV4Attention._fused_qnorm_rope_kv_insert`

.