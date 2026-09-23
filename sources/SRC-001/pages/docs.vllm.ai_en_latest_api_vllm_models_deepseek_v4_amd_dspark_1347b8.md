source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/amd/dspark/
lastmod: 2026-09-23

#

`vllm.models.deepseek_v4.amd.dspark`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark)

DSpark draft model for DeepSeek-V4 on ROCm/AMD (gfx950).

ROCm port of `nvidia/dspark.py`

. Follows the same nvidia->amd recipe used for `amd/mtp.py`

:

- import
`DeepseekV4DecoderLayer`

from the AMD`.model`

(aiter/triton attention + MHC CustomOp path) instead of the nvidia one; - route the MHC head through the
`HCHeadOp`

CustomOp dispatcher (aiter / tilelang / triton / torch) instead of calling the tilelang kernels directly, and gate the trailing`mhc_post`

on`use_fused_mhc`

(True when AITER or TileLang fused MHC is available; False only on the torch fallback); - drop the mega-MoE weight path (
`make_deepseek_v4_expert_params_mapping`

/`use_mega_moe`

/`finalize_mega_moe_weights`

do not exist in amd/model.py).

Everything else — the semi-autoregressive drafting hooks, the Markov head, the sliding-window context-KV insert, and the checkpoint `mtp.*`

weight remap — is pure torch / Triton and shared with the nvidia implementation unchanged.

Classes:

##

`DSparkDeepseekV4ForCausalLM`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4ForCausalLM)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[compute_confidence](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4ForCausalLM.compute_confidence)Per-position acceptance probability for each drafted token.

-
–[compute_logits](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4ForCausalLM.compute_logits)Base logits U_k = lm_head(norm(head_hidden)).

-
–[load_weights](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4ForCausalLM.load_weights)Load the

`mtp.{0,1,2}.*`

draft weights from the target checkpoint.

## Source code in `vllm/models/deepseek_v4/amd/dspark.py`


|
|

###

`_remap_dspark_name(name)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4ForCausalLM._remap_dspark_name)

Map a checkpoint `mtp.{i}.*`

name to this model's parameter path.

Returns None for non-mtp weights (owned by the target model).

## Source code in `vllm/models/deepseek_v4/amd/dspark.py`


###

`compute_confidence(head_hidden, markov_embed)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4ForCausalLM.compute_confidence)

Per-position acceptance probability for each drafted token.

## Source code in `vllm/models/deepseek_v4/amd/dspark.py`


###

`compute_logits(hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4ForCausalLM.compute_logits)

Base logits U_k = lm_head(norm(head_hidden)).

###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4ForCausalLM.load_weights)

Load the `mtp.{0,1,2}.*`

draft weights from the target checkpoint.

Non-mtp weights (embed/head/main layers) belong to the target model and are skipped here. `embed_tokens`

/`lm_head`

are aliased from the target.

## Source code in `vllm/models/deepseek_v4/amd/dspark.py`


|
|

##

`DSparkDeepseekV4Model`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4Model)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[combine_hidden_states](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4Model.combine_hidden_states)main_x = main_norm(main_proj(concat of target aux hidden states)).

-
–[precompute_and_store_context_kv](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4Model.precompute_and_store_context_kv)Insert the sliding-window context KV for every draft layer.


## Source code in `vllm/models/deepseek_v4/amd/dspark.py`


|
|

###

`combine_hidden_states(aux_hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4Model.combine_hidden_states)

main_x = main_norm(main_proj(concat of target aux hidden states)).

`aux_hidden_states`

is [T, hidden_size * len(target_layer_ids)].

## Source code in `vllm/models/deepseek_v4/amd/dspark.py`


###

`precompute_and_store_context_kv(main_x, context_positions, context_slot_mappings=None)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark.DSparkDeepseekV4Model.precompute_and_store_context_kv)

Insert the sliding-window context KV for every draft layer.

Mirrors the reference DSparkAttention: each layer derives its context KV from the SAME projected target hidden `main_x`

, via that layer's own `wkv`

+ `kv_norm`

+ RoPE + quant, then writes it at the layer's context slots.

`context_slot_mappings`

is a per-layer list (each entry is the context slot mapping for that layer's kv-cache group, since the hybrid manager may place draft layers in different groups). `None`

(or a `None`

entry) runs the projection to reserve workspace but writes nothing (profiling).

## Source code in `vllm/models/deepseek_v4/amd/dspark.py`


##

`_insert_context_kv(attn, kv, positions, slot_mapping)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.amd.dspark._insert_context_kv)

RoPE + quant + paged-cache insert of (already kv_norm'd) context KV.

Reuses the DSV4 fused insert ops (which also process a query; we pass a dummy query and discard it, since context tokens have no query). Mirrors `DeepseekV4Attention._fused_qnorm_rope_kv_insert`

.