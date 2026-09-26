source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/bailing_moe_v3/
lastmod: 2026-09-24

vLLM implementation for BailingMoeV3ForCausalLM.

The HuggingFace reference model mixes MLA full-attention layers with Kimi Delta Attention linear layers and Bailing MoE blocks. This file keeps the V3 module/weight names aligned with the reference implementation while reusing vLLM's parallel linear layers, MLA kernel, KDA kernel and fused MoE loader.

Functions:

Pad a block-FP8 MLP so each TP shard contains whole quant blocks.

## Source code in `vllm/model_executor/models/bailing_moe_v3.py`


| def _get_block_fp8_mlp_padded_intermediate_size(
quant_config: QuantizationConfig | None,
intermediate_size: int,
prefix: str,
) -> int:
"""Pad a block-FP8 MLP so each TP shard contains whole quant blocks."""
if not _is_block_fp8_config(quant_config):
return intermediate_size
block_size = quant_config.weight_block_size
assert block_size is not None
alignments: list[int] = []
if not _is_fp8_module_excluded(quant_config, f"{prefix}.gate_up_proj"):
alignments.append(int(block_size[0]))
if not _is_fp8_module_excluded(quant_config, f"{prefix}.down_proj"):
alignments.append(int(block_size[1]))
if not alignments:
return intermediate_size
tp_size = get_tensor_model_parallel_world_size()
tp_alignment = tp_size * lcm(*alignments)
return (intermediate_size + tp_alignment - 1) // tp_alignment * tp_alignment
|

##

`_is_fp8_module_excluded(quant_config, prefix)`


Match Ling's abbreviated FP8 exclusions against mapped vLLM prefixes.

## Source code in `vllm/model_executor/models/bailing_moe_v3.py`


| def _is_fp8_module_excluded(
quant_config: QuantizationConfig | None,
prefix: str,
) -> bool:
"""Match Ling's abbreviated FP8 exclusions against mapped vLLM prefixes."""
if not _is_block_fp8_config(quant_config):
return False
return is_layer_skipped(
prefix=prefix,
ignored_layers=quant_config.ignored_layers,
fused_mapping=quant_config.packed_modules_mapping,
match_mode=quant_config.ignored_layers_match_mode,
)
|

##

`_maybe_remap_ling_mxfp4_weight_names(weights, quant_config)`


Map Ling's MXFP4 expert scales to Mxfp4MoEMethod parameters.

## Source code in `vllm/model_executor/models/bailing_moe_v3.py`


| def _maybe_remap_ling_mxfp4_weight_names(
weights: Iterable[tuple[str, torch.Tensor]],
quant_config: QuantizationConfig | None,
) -> Iterable[tuple[str, torch.Tensor]]:
"""Map Ling's MXFP4 expert scales to Mxfp4MoEMethod parameters."""
if isinstance(quant_config, Fp8Config) and quant_config.store_dtype == "mxfp4":
return _LING_MXFP4_WEIGHTS_MAPPER.apply(weights)
return weights
|

##

`_pad_block_fp8_mlp_checkpoint_tensor(quant_config, name, loaded_weight, intermediate_size, padded_intermediate_size)`


Zero-pad an MLP checkpoint tensor on its intermediate dimension.

## Source code in `vllm/model_executor/models/bailing_moe_v3.py`


| def _pad_block_fp8_mlp_checkpoint_tensor(
quant_config: QuantizationConfig,
name: str,
loaded_weight: torch.Tensor,
intermediate_size: int,
padded_intermediate_size: int,
) -> torch.Tensor:
"""Zero-pad an MLP checkpoint tensor on its intermediate dimension."""
if padded_intermediate_size == intermediate_size:
return loaded_weight
block_size = getattr(quant_config, "weight_block_size", None)
assert block_size is not None
if ".down_proj." in name:
if name.endswith(".bias"):
return loaded_weight
dim = 1
block = int(block_size[1])
logical_shards = 1
elif any(
projection in name
for projection in (".gate_proj.", ".up_proj.", ".gate_up_proj.")
):
dim = 0
block = int(block_size[0])
logical_shards = 2 if ".gate_up_proj." in name else 1
else:
return loaded_weight
if name.endswith(".weight_scale_inv"):
expected_shard_size = (intermediate_size + block - 1) // block
target_shard_size = (padded_intermediate_size + block - 1) // block
elif name.endswith((".weight", ".bias")):
expected_shard_size = intermediate_size
target_shard_size = padded_intermediate_size
else:
return loaded_weight
current_size = loaded_weight.shape[dim]
if current_size % logical_shards != 0:
raise ValueError(
f"Cannot split {name} dimension {current_size} into "
f"{logical_shards} logical shards."
)
current_shard_size = current_size // logical_shards
if current_shard_size == target_shard_size:
return loaded_weight
if current_shard_size != expected_shard_size:
raise ValueError(
f"Cannot pad {name}: expected each logical intermediate dimension "
f"to be {expected_shard_size}, but got {current_shard_size}."
)
padded_shards: list[torch.Tensor] = []
for shard in loaded_weight.split(current_shard_size, dim=dim):
pad_shape = list(shard.shape)
pad_shape[dim] = target_shard_size - current_shard_size
padded_shards.extend([shard, shard.new_zeros(pad_shape)])
return torch.cat(padded_shards, dim=dim)
|

##

`bailing_v3_kda_attention(q_proj_states, k_proj_states, v_proj_states, g1, beta, core_attn_out, layer_name)`


Run Bailing V3's KDA state update outside the compiled graph.

## Source code in `vllm/model_executor/models/bailing_moe_v3.py`


| def bailing_v3_kda_attention(
q_proj_states: torch.Tensor,
k_proj_states: torch.Tensor,
v_proj_states: torch.Tensor,
g1: torch.Tensor,
beta: torch.Tensor,
core_attn_out: torch.Tensor,
layer_name: str,
) -> None:
"""Run Bailing V3's KDA state update outside the compiled graph."""
forward_context: ForwardContext = get_forward_context()
layer = forward_context.no_compile_layers[layer_name]
layer._forward(
q_proj_states=q_proj_states,
k_proj_states=k_proj_states,
v_proj_states=v_proj_states,
g1=g1,
beta=beta,
core_attn_out=core_attn_out,
)
|