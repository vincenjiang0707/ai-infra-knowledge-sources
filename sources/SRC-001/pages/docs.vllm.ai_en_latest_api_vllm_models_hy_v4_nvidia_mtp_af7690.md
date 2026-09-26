source: https://docs.vllm.ai/en/latest/api/vllm/models/hy_v4/nvidia/mtp/
lastmod: 2026-09-24

#

`vllm.models.hy_v4.nvidia.mtp`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp)

Multi-token prediction (MTP) head for HY V4 (NVIDIA).

Classes:

-
–[HYV4MTP](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP)HY V4 MTP draft head.

-
–[HYV4MultiTokenPredictor](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MultiTokenPredictor)Owns the MTP draft blocks and their shared embedding / logits path.

-
–[HYV4MultiTokenPredictorLayer](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MultiTokenPredictorLayer)A single MTP draft block.

-
–[HYV4SharedHead](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4SharedHead)Holds the draft LM head shared with the target model.


##

`HYV4MTP`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

HY V4 MTP draft head.

Not a pipeline-parallel stage: the draft head always runs on a single rank, matching `DeepseekV32MTP`

/ `KimiK3MTP`

/ `HYV3MTP`

.

Methods:

-
–[set_topk_indices_buffer](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP.set_topk_indices_buffer)Share the target sparse-index buffer with every draft consumer.


## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


|
|

###

`_load_expert_weight(name, loaded_weight, params_dict, loaded_params, split_expert_params_mapping, fused_expert_param_names, num_experts)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP._load_expert_weight)

Load one routed-expert weight in either checkpoint layout.

Parameters:

-

(`name`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP._load_expert_weight(name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Weight name already rewritten to draft-module naming.

-

(`loaded_weight`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP._load_expert_weight(loaded_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The checkpoint tensor.

-

(`params_dict`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP._load_expert_weight(params_dict))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)The draft model's named parameters.

-

(`loaded_params`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP._load_expert_weight(loaded_params))

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]Set updated with the parameters that received a value.

-

(`split_expert_params_mapping`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP._load_expert_weight(split_expert_params_mapping))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str),[int](https://docs.python.org/3/builtins/functions.html#int),[str](https://docs.python.org/3/builtins/stdtypes.html#str)]]Mapping for the per-expert layout.

-

(`fused_expert_param_names`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP._load_expert_weight(fused_expert_param_names))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[str](https://docs.python.org/3/builtins/stdtypes.html#str)],[str](https://docs.python.org/3/builtins/stdtypes.html#str)]`(mlp_prefix, tag) -> param name`

for the all-experts-packed layout. -

(`num_experts`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP._load_expert_weight(num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of routed experts.


Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True when the weight was consumed (even if this rank holds none of

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)the addressed experts).


## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


|
|

###

`set_topk_indices_buffer(topk_indices_buffer)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MTP.set_topk_indices_buffer)

Share the target sparse-index buffer with every draft consumer.

Proposers that walk `named_modules()`

instead of calling this reach the same consumers via `HYV4MLAAttention.topk_indices_buffer`

.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`HYV4MultiTokenPredictor`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MultiTokenPredictor)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Owns the MTP draft blocks and their shared embedding / logits path.

Methods:

-
–[compact_topk_indices](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MultiTokenPredictor.compact_topk_indices)Move the top-k rows at

`slot_ids`

to the front of the buffer. -
–[set_skip_topk](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MultiTokenPredictor.set_skip_topk)Toggle the draft indexer for

`index_share_for_mtp_iteration`

.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


|
|

###

`compact_topk_indices(slot_ids)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MultiTokenPredictor.compact_topk_indices)

Move the top-k rows at `slot_ids`

to the front of the buffer.

Step 0 writes one row per query token of the multi-token batch, while steps 1+ decode a single token per request and index the buffer from 0. Without this gather they would read another token's rows.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


###

`set_skip_topk(skip)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MultiTokenPredictor.set_skip_topk)

Toggle the draft indexer for `index_share_for_mtp_iteration`

.

The proposer clears the flag for draft step 0 so the MTP layer builds its own top-k indices, then sets it for steps 1+ so they reuse what step 0 wrote into the shared buffer instead of re-running the indexer.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`HYV4MultiTokenPredictorLayer`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4MultiTokenPredictorLayer)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

A single MTP draft block.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`HYV4SharedHead`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp.HYV4SharedHead)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Holds the draft LM head shared with the target model.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`_create_mtp_quant_config(hf_config, backbone_quant_config=None)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._create_mtp_quant_config)

Create the quantization config for the MTP layers.

The MTP quantization algorithm is given by the `mtp_quant_algo`

field in `config.json`

, independently of the backbone's quantization. Supported values are `"FP8"`

, `"NONE"`

(inherit the backbone) and `"BF16"`

/ `"FP16"`

(unquantized). A missing or `"NONE"`

value falls back to the backbone config.

Parameters:

-

(`hf_config`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._create_mtp_quant_config(hf_config))`PreTrainedConfig`

) –The draft model's HF config.

-

(`backbone_quant_config`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._create_mtp_quant_config(backbone_quant_config))

, default:[QuantizationConfig](https://docs.vllm.ai/model_executor/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| None`None`

) –The target model's quantization config.


Returns:

-

–[QuantizationConfig](https://docs.vllm.ai/model_executor/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| NoneThe quantization config to use for the MTP layers, or None when the MTP

-

–[QuantizationConfig](https://docs.vllm.ai/model_executor/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| Nonelayers are unquantized.


## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`_extend_layer_types(layer_types, layer_idx, fallback)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._extend_layer_types)

Pad a per-layer config list so`layer_idx`

is addressable.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`_get_spec_layer_idx_from_weight_name(config, weight_name)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._get_spec_layer_idx_from_weight_name)

Return the MTP layer index a checkpoint weight belongs to, or None.

Compatible with`num_nextn_predict_layers`

of 1 and 2 for a single MTP head, matching how the HY V4 checkpoints are exported.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`_prepare_mtp_fp8_expert_scale(quant_config, name, loaded_weight)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._prepare_mtp_fp8_expert_scale)

Normalize block-wise FP8 expert scale names and dtypes.

## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`_remap_mtp_quant_exclusions(quant_config, mtp_start_layer_idx, num_mtp_layers)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._remap_mtp_quant_exclusions)

Translate checkpoint-named MTP quant exclusions to draft prefixes.

`modules_to_not_convert`

/ `exclude_modules`

name MTP modules the way the checkpoint does (`model.mtp_layers.0.self_attn.linear_gate`

), while the draft model builds them under `model.layers.<num_hidden_layers + i>`

. `is_layer_skipped`

compares prefixes for exact equality, so without this translation an excluded MTP module gets a quant method even though its checkpoint weight is BF16 with no `weight_scale`

/ `weight_scale_inv`

companion: the scale then keeps its `finfo(float32).min`

sentinel and the layer silently produces garbage.

The list lives under a different attribute per config class, hence the lookup over `_MTP_QUANT_EXCLUSION_ATTRS`

.

Parameters:

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._remap_mtp_quant_exclusions(quant_config))

) –[QuantizationConfig](https://docs.vllm.ai/model_executor/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| NoneThe MTP quantization config to widen.

-

(`mtp_start_layer_idx`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._remap_mtp_quant_exclusions(mtp_start_layer_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Index of the first MTP layer in the draft model.

-

(`num_mtp_layers`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._remap_mtp_quant_exclusions(num_mtp_layers))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of MTP layers.


Returns:

-

–[QuantizationConfig](https://docs.vllm.ai/model_executor/layers/quantization/#vllm.model_executor.layers.quantization.QuantizationConfig)| NoneA shallow copy with the translated exclusions, or the input unchanged.


## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


|
|

##

`_resolve_fused_expert_param(param_base, ckpt_suffix, params_dict)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._resolve_fused_expert_param)

Map a fused expert checkpoint suffix onto a draft parameter name.

Fused checkpoints pack every expert into one tensor and name the companion scales by suffixing the projection (`experts.gate_up_proj_scale_inv`

), while the draft model owns `experts.routed_experts.w13_weight`

plus a separate `..._scale_inv`

parameter. Dropping the suffix would push the scale into the weight parameter and leave the scale at its sentinel init.

Parameters:

-

(`param_base`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._resolve_fused_expert_param(param_base))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Draft parameter holding the packed weight.

-

(`ckpt_suffix`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._resolve_fused_expert_param(ckpt_suffix))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)Checkpoint text following the projection name.

-

(`params_dict`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._resolve_fused_expert_param(params_dict))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)The draft model's named parameters.


Returns:

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneThe matching draft parameter name, or None when there is none.


## Source code in `vllm/models/hy_v4/nvidia/mtp.py`


##

`_should_skip_missing_mtp_scale_param(quant_config, name)`

[¶](https://docs.vllm.ai#vllm.models.hy_v4.nvidia.mtp._should_skip_missing_mtp_scale_param)

Whether an unmatched scale parameter can be silently ignored.