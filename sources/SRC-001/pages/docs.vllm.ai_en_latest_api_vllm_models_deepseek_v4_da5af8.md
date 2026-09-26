source: https://docs.vllm.ai/en/latest/api/vllm/models/deepseek_v4/
lastmod: 2026-09-24

#

`vllm.models.deepseek_v4`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4)

DeepSeek V4 model — hardware-isolated entry point.

The actual implementation lives under `nvidia/`

and `amd/`

; this module picks the right one for the current platform and re-exports the public classes used by the model registry and quantization config lookup.

Modules:

-
–[amd](https://docs.vllm.ai/amd/#vllm.models.deepseek_v4.amd) -
–[attention](https://docs.vllm.ai/attention/#vllm.models.deepseek_v4.attention)DeepseekV4 MLA Attention Layer.

-
–[common](https://docs.vllm.ai/common/#vllm.models.deepseek_v4.common) -
–[compressor](https://docs.vllm.ai/compressor/#vllm.models.deepseek_v4.compressor) -
–[cpu](https://docs.vllm.ai/cpu/#vllm.models.deepseek_v4.cpu) -
–[nvidia](https://docs.vllm.ai/nvidia/#vllm.models.deepseek_v4.nvidia) -
–[quant_config](https://docs.vllm.ai/quant_config/#vllm.models.deepseek_v4.quant_config)Quantization config for DeepSeek V4.

-
–[sparse_mla](https://docs.vllm.ai/sparse_mla/#vllm.models.deepseek_v4.sparse_mla)DeepSeek-V4 FlashMLA sparse backend, metadata, and metadata builder.

-
–[vl_stub](https://docs.vllm.ai/vl_stub/#vllm.models.deepseek_v4.vl_stub)Stub for platforms where the DeepSeek-V4 vision variant is unsupported.

-
–[xpu](https://docs.vllm.ai/xpu/#vllm.models.deepseek_v4.xpu)

Classes:

-
–[DSparkDeepseekV4ForCausalLM](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM) -
–[DeepSeekV4MTP](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepSeekV4MTP) -
–[DeepseekV4FP8Config](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4FP8Config)FP8 config for DeepSeek V4 with expert-dtype-aware MoE dispatch.

-
–[DeepseekV4ForCausalLM](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4ForCausalLM) -
–[DeepseekV4ForConditionalGeneration](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4ForConditionalGeneration)Multimodal entry point for DeepSeek-V4 checkpoints with a vision tower.


##

`DSparkDeepseekV4ForCausalLM`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[compute_confidence](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM.compute_confidence)Per-position acceptance probability for each drafted token.

-
–[compute_logits](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM.compute_logits)Base logits U_k = lm_head(norm(head_hidden)).

-
–[load_weights](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM.load_weights)Load the

`mtp.{0,1,2}.*`

draft weights from the target checkpoint.

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


|
|

###

`_remap_dspark_name(name)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM._remap_dspark_name)

Map a checkpoint `mtp.{i}.*`

name to this model's parameter path.

Returns None for non-mtp weights (owned by the target model).

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


###

`compute_confidence(head_hidden, markov_embed)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM.compute_confidence)

Per-position acceptance probability for each drafted token.

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


###

`compute_logits(hidden_states)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM.compute_logits)

Base logits U_k = lm_head(norm(head_hidden)).

###

`load_weights(weights)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DSparkDeepseekV4ForCausalLM.load_weights)

Load the `mtp.{0,1,2}.*`

draft weights from the target checkpoint.

Non-mtp weights (embed/head/main layers) belong to the target model and are skipped here. `embed_tokens`

/`lm_head`

are aliased from the target.

## Source code in `vllm/models/deepseek_v4/nvidia/dspark.py`


|
|

##

`DeepSeekV4MTP`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepSeekV4MTP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

## Source code in `vllm/models/deepseek_v4/nvidia/mtp.py`


|
|

###

`_rewrite_spec_layer_name(spec_layer, name)`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepSeekV4MTP._rewrite_spec_layer_name)

Rewrite the weight name to match the format of the original model. Add .mtp_block for modules in transformer layer block for spec layer and rename shared layer weights to be top level.

## Source code in `vllm/models/deepseek_v4/nvidia/mtp.py`


##

`DeepseekV4FP8Config`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4FP8Config)

Bases: [Fp8Config](https://docs.vllm.ai/model_executor/layers/quantization/fp8/#vllm.model_executor.layers.quantization.fp8.Fp8Config)

FP8 config for DeepSeek V4 with expert-dtype-aware MoE dispatch.

DeepSeek V4 checkpoints always use FP8 block quantization for linear/attention layers. The MoE expert weights vary by checkpoint: - `expert_dtype="fp4"`

(e.g. DeepSeek-V4-Flash): MXFP4 experts with ue8m0 (e8m0fnu) FP8 linear scales. - `expert_dtype="fp8"`

(e.g. DeepSeek-V4-Flash-Base): FP8 block experts with float32 FP8 linear scales.

The dispatch and the linear scale dtype are both keyed off `expert_dtype`

from the model's hf_config; missing values default to `"fp4"`

so existing FP4 checkpoints stay unchanged.

NOTE: `expert_dtype`

is resolved lazily because this config is constructed during VllmConfig setup, before `set_current_vllm_config`

is active. Reading hf_config eagerly in `__init__`

would always see the default `"fp4"`

and silently misroute Flash-Base checkpoints.

## Source code in `vllm/models/deepseek_v4/quant_config.py`


|
|

###

`_is_quark_mxfp4_ocp(hf_quant_cfg)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4FP8Config._is_quark_mxfp4_ocp)

True for AMD-Quark exports whose global scheme is MXFP4.

## Source code in `vllm/models/deepseek_v4/quant_config.py`


##

`DeepseekV4ForCausalLM`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4ForCausalLM)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsPP](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsEagle3](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle3)

, [SupportsLoRA](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)`DeepseekV4MixtureOfExperts`


Methods:

-
–[get_mtp_target_hidden_states](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4ForCausalLM.get_mtp_target_hidden_states)Pre-hc_head residual stream buffer (max_num_batched_tokens,


## Source code in `vllm/models/deepseek_v4/nvidia/model.py`


|
|

###

`get_mtp_target_hidden_states()`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4ForCausalLM.get_mtp_target_hidden_states)

Pre-hc_head residual stream buffer (max_num_batched_tokens, hc_mult * hidden_size) for the MTP draft model. Populated by forward(); valid after each target step.

## Source code in `vllm/models/deepseek_v4/nvidia/model.py`


##

`DeepseekV4ForConditionalGeneration`

[¶](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4ForConditionalGeneration)

Bases:

, [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

, [SupportsMultiModal](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsMultiModal)

, [SupportsPP](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsPP)

, [SupportsEagle3](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsEagle3)[SupportsLoRA](https://docs.vllm.ai/model_executor/models/interfaces/#vllm.model_executor.models.interfaces.SupportsLoRA)

Multimodal entry point for DeepSeek-V4 checkpoints with a vision tower.

`SupportsEagle3`

(aux hidden-state plumbing for MTP/DSpark drafters) delegates through `language_model`

via the protocol defaults.

Methods:

-
–[get_mm_mapping](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4ForConditionalGeneration.get_mm_mapping)Get the module prefixes in the multimodal model.

-
–[get_mtp_target_hidden_states](https://docs.vllm.ai#vllm.models.deepseek_v4.DeepseekV4ForConditionalGeneration.get_mtp_target_hidden_states)Pre-hc_head residual stream buffer for the MTP/DSpark draft model.


## Source code in `vllm/models/deepseek_v4/common/vl_model.py`


|
|