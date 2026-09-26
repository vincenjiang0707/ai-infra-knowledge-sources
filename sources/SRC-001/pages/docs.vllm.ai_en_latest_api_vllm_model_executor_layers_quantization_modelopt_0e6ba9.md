source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/quantization/modelopt/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.quantization.modelopt`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt)

Classes:

-
–[CkptCtx](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.CkptCtx)Per-checkpoint facts a QuantKey cannot carry.

-
–[FormatScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme)Optional per-format hooks that compose

*around*the QuantKey schemes. -
–[KDynamicNoParam](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KDynamicNoParam)Dynamic activation with no stored scale (W8A8): quantized at runtime in

-
–[KFp8Block128](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KFp8Block128)128x128 block-static FP8 weight ('PbWo'). Weight-role only. ModelOpt

-
–[KFp8StaticChannel](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KFp8StaticChannel)Per-channel static FP8 weight (the 'PcPt' weight). Weight-role only —

-
–[KFp8StaticTensor](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KFp8StaticTensor)Plain per-tensor static FP8 — bivalent: serves BOTH the weight slot and

-
–[KMxfp8Static](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KMxfp8Static)MXFP8 weight: fp8-e4m3 values + per-32-block e8m0 (uint8) scale.

-
–[KNvfp4Dynamic](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KNvfp4Dynamic)NVFP4 activation scheme (W4A4). Has a static global input scale on disk;

-
–[KNvfp4Static](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KNvfp4Static)NVFP4 weight scheme (W4A4 and W4A16 share it). Weight-role only today.

-
–[ModelOptFp8Config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptFp8Config)Config class for ModelOpt FP8.

-
–[ModelOptFp8MoEMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptFp8MoEMethod)MoE method for ModelOpt FP8.

-
–[ModelOptKVCacheMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptKVCacheMethod)Supports loading kv-cache scaling factors from FP8 or NVFP4 checkpoints.

-
–[ModelOptLinearMethod](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptLinearMethod)Generic, format-agnostic ModelOpt linear method. Holds a weight scheme +

-
–[ModelOptMixedPrecisionConfig](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMixedPrecisionConfig)Config class for ModelOpt MIXED_PRECISION.

-
–[ModelOptMxFp8Config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMxFp8Config)Config class for ModelOpt MXFP8.

-
–[ModelOptMxFp8FusedMoE](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMxFp8FusedMoE)FlashInfer TRTLLM MXFP8 block-scale MoE for ModelOpt checkpoints.

-
–[ModelOptNvFp4Config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4Config)Config class for ModelOpt FP4.

-
–[ModelOptNvFp4FusedMoE](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE)MoE Method for FP4 Quantization.

-
–[ModelOptQuantConfigBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase) -
–[QuantKeyScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)One scheme per QuantKey. Selected by key

*content*; the base supplies the -
–[RuntimeDtypes](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.RuntimeDtypes)Runtime/model dtypes kernels need — format-agnostic.

-
–[Shapes](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.Shapes)Layer geometry from create_weights args.


Functions:

-
–[algos_owned_by](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.algos_owned_by)The linear algos a given config accepts, for its quant_algo validation.

-
–[build_linear_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.build_linear_method)Construct the linear method for

`algo`

. -
–[maybe_fuse_global_scales](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.maybe_fuse_global_scales)Alpha = input_global_scale * weight_global_scale, presence-gated.

-
–[resolve](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.resolve)Turn a sub-config into (QuantSpec, CkptCtx, format_scheme).

-
–[select_linear_kernel](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.select_linear_kernel)Thin family dispatcher on the weight key: nvfp4 / mxfp8 / fp8.


##

`CkptCtx`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.CkptCtx)

Per-checkpoint facts a QuantKey cannot carry.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`FormatScheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme)

Optional per-format hooks that compose *around* the QuantKey schemes.

Extension seam for residue that belongs to a format as a whole rather than a single QuantKey — an extra parameter the weight/activation schemes don't cover, or a tweak before/after their `process`

. All hooks default to no-ops; most formats need none (they are a pure `(weight, activation)`

key pair). To add one: subclass, override the hooks you need, and return an instance from the format's `resolve()`

branch — no change to `ModelOptLinearMethod`

itself.

Methods:

-
–[apply](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.apply)Wrap the kernel's forward.

`kernel_apply(layer, x, bias) -> Tensor`

. -
–[extra_weights](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.extra_weights)Register format-level params (after the key schemes' weights).

-
–[kernel_weight_shape](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.kernel_weight_shape)Return the weight shape the selected kernel will receive.

-
–[post_process](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.post_process)Run after the key schemes'

`process`

, before the kernel's. -
–[pre_process](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.pre_process)Run before the key schemes'

`process`

.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


###

`apply(layer, x, bias, kernel_apply)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.apply)

Wrap the kernel's forward. `kernel_apply(layer, x, bias) -> Tensor`

.

Default: delegate unchanged. A format whose residue lives at compute time (e.g. run the GEMM on a padded weight then slice the output back to its logical width, #53132-style) overrides this and calls `kernel_apply`

in the middle.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


###

`extra_weights(layer, shapes, ctx, wl)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.extra_weights)

###

`kernel_weight_shape(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.kernel_weight_shape)

###

`post_process(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme.post_process)

##

`KDynamicNoParam`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KDynamicNoParam)

Bases: [QuantKeyScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)

Dynamic activation with no stored scale (W8A8): quantized at runtime in the kernel. NOT the same as activation=None (weight-only) — init_fp8 needs a non-None activation key. Activation-role only. Serves the fp8 per-token, fp8 per-block, and mxfp8 dynamic activation keys.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`KFp8Block128`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KFp8Block128)

Bases: [QuantKeyScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)

128x128 block-static FP8 weight ('PbWo'). Weight-role only. ModelOpt exports the scale 4-D [out_blk,1,in_blk,1]; process squeezes to 2-D. No transpose (block kernel keeps [out,in]).

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`KFp8StaticChannel`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KFp8StaticChannel)

Bases: [QuantKeyScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)

Per-channel static FP8 weight (the 'PcPt' weight). Weight-role only — there is no static per-channel *activation* today.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`KFp8StaticTensor`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KFp8StaticTensor)

Bases: [QuantKeyScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)

Plain per-tensor static FP8 — bivalent: serves BOTH the weight slot and the activation slot (W8A8). One key in both QuantSpec slots.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

##

`KMxfp8Static`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KMxfp8Static)

Bases: [QuantKeyScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)

MXFP8 weight: fp8-e4m3 values + per-32-block e8m0 (uint8) scale. Weight-role only. process is validate-only plus an idempotency guard.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

##

`KNvfp4Dynamic`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KNvfp4Dynamic)

Bases: [QuantKeyScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)

NVFP4 activation scheme (W4A4). Has a static global input scale on disk; the per-group scale is computed at runtime inside the kernel.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`KNvfp4Static`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.KNvfp4Static)

Bases: [QuantKeyScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)

NVFP4 weight scheme (W4A4 and W4A16 share it). Weight-role only today.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

##

`ModelOptFp8Config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptFp8Config)

Bases: [ModelOptQuantConfigBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase)

Config class for ModelOpt FP8.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`ModelOptFp8MoEMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptFp8MoEMethod)

Bases: [FusedMoEMethodBase](https://docs.vllm.ai/fused_moe/#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase)

MoE method for ModelOpt FP8. Supports loading FP8 checkpoints with static weight scale and activation scale.

Parameters:

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptFp8MoEMethod(quant_config))

) –[ModelOptFp8Config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptFp8Config)The ModelOpt quantization config.


## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

##

`ModelOptKVCacheMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptKVCacheMethod)

Bases: [BaseKVCacheMethod](https://docs.vllm.ai/kv_cache/#vllm.model_executor.layers.quantization.kv_cache.BaseKVCacheMethod)

Supports loading kv-cache scaling factors from FP8 or NVFP4 checkpoints.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`ModelOptLinearMethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptLinearMethod)

Bases: [LinearMethodBase](https://docs.vllm.ai/linear/#vllm.model_executor.layers.linear.LinearMethodBase)

Generic, format-agnostic ModelOpt linear method. Holds a weight scheme + an activation scheme (from the QuantSpec pair) and an optional `FormatScheme`

, runs a fixed lifecycle, selects the kernel from the pair, and applies.

Registered for weight_loader_v2 (like every ModelOpt linear method) so the `BasevLLMParameter`

params route through the v2 fused loader, not the legacy shape-assert path.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

##

`ModelOptMixedPrecisionConfig`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMixedPrecisionConfig)

Bases: [ModelOptQuantConfigBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase)

Config class for ModelOpt MIXED_PRECISION.

Supports checkpoints where different layers use different quantization algorithms (e.g., FP8 for dense layers and NVFP4 for MoE experts). The per-layer algorithm is specified in the `quantized_layers`

dict inside `config.json`

's `quantization_config`

(preferred) or the legacy `hf_quant_config.json`

.

Methods:

-
–[get_quant_method](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMixedPrecisionConfig.get_quant_method)Return quantize-method based on layer.


## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

###

`_resolve_quant_algo(prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMixedPrecisionConfig._resolve_quant_algo)

Look up the quant_algo for a vLLM-side layer prefix.

Tries three strategies in order: 1. Direct lookup in `quantized_layers`

. 2. Packed/fused-layer lookup (unfuse via `packed_modules_mapping`

). 3. Prefix-based lookup for RoutedExperts (any child key starts with `prefix + "."`

).

Returns the upper-cased quant_algo string, or *None* if the prefix is not found.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

###

`get_quant_method(layer, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMixedPrecisionConfig.get_quant_method)

Return quantize-method based on layer.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`ModelOptMxFp8Config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMxFp8Config)

Bases: [ModelOptQuantConfigBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase)

Config class for ModelOpt MXFP8.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

##

`ModelOptMxFp8FusedMoE`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMxFp8FusedMoE)

Bases: [FusedMoEMethodBase](https://docs.vllm.ai/fused_moe/#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase)

FlashInfer TRTLLM MXFP8 block-scale MoE for ModelOpt checkpoints.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

###

`_check_weight_dtypes(layer)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMxFp8FusedMoE._check_weight_dtypes)

Validate weight and scale dtypes before processing.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


###

`_dequant_mxfp8_weights_to_bf16(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptMxFp8FusedMoE._dequant_mxfp8_weights_to_bf16)

One-time MXFP8->BF16 weight dequant for the emulation path.

On devices without a native MXFP8 MoE kernel (e.g. gfx942 / MI300), `Mxfp8EmulationTritonExperts`

otherwise dequantizes every expert weight to BF16 on *every* forward step -- the dominant cost (conc1 ~1.3 tok/s). Doing the dequant once here and replacing the MXFP8 parameters with BF16 makes the MoE run exactly like a plain BF16 checkpoint (full precision, no per-step dequant); SwiGLU-OAI is still applied by the experts' `activation()`

override. The MXFP8 weights are freed by `replace_parameter`

(BF16 is 2x their size; the small E8M0 scale tensors are left in place, unused).

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`ModelOptNvFp4Config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4Config)

Bases: [ModelOptQuantConfigBase](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase)

Config class for ModelOpt FP4.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

##

`ModelOptNvFp4FusedMoE`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE)

Bases: [FusedMoEMethodBase](https://docs.vllm.ai/fused_moe/#vllm.model_executor.layers.fused_moe.FusedMoEMethodBase)

MoE Method for FP4 Quantization.

Parameters:

-

(`quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE(quant_config))

) –[ModelOptNvFp4Config](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4Config)NVFP4 Quant Config


Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE.process_weights_after_loading)Convert NVFP4 MoE weights into kernel format and setup the kernel.

-
–[uses_weight_scale_2_pattern](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE.uses_weight_scale_2_pattern)FP4 variants use 'weight_scale_2' pattern for per-tensor weight scales.


## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

###

`_build_moe_kernel(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE._build_moe_kernel)

Build the modular MoE kernel from the (already in-format) weights.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


###

`_restore_padded_moe_dims(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE._restore_padded_moe_dims)

Recover the padded `moe_config`

dims from the exported weights.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE.process_weights_after_loading)

Convert NVFP4 MoE weights into kernel format and setup the kernel.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


###

`uses_weight_scale_2_pattern()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptNvFp4FusedMoE.uses_weight_scale_2_pattern)

##

`ModelOptQuantConfigBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase)

Bases: [QuantizationConfig](https://docs.vllm.ai/base_config/#vllm.model_executor.layers.quantization.base_config.QuantizationConfig)

Methods:

-
–[is_layer_excluded](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase.is_layer_excluded)Check if a layer should be excluded from quantization.


## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


|
|

###

`_extract_modelopt_quant_algo(hf_quant_cfg)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase._extract_modelopt_quant_algo)

Extract upper-cased quant_algo from a modelopt config.

Returns the quant_algo string (upper-cased), or None if the config is not a modelopt config.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


###

`is_layer_excluded(prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.ModelOptQuantConfigBase.is_layer_excluded)

Check if a layer should be excluded from quantization.

Handles both exact matching (for fused layers) and ModelOpt wildcard matching.

The ModelOpt exclude_modules list is a list of wildcards.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`QuantKeyScheme`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.QuantKeyScheme)

One scheme per QuantKey. Selected by key *content*; the base supplies the `role`

from the slot it fills the key into (wkey->WEIGHT, akey->ACT).

Every scheme branches on `role`

explicitly and `reject`

s any role it has not validated — never falling through to the wrong role's registration, which would allocate the wrong parameters and produce garbage silently.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`RuntimeDtypes`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.RuntimeDtypes)

Runtime/model dtypes kernels need — format-agnostic.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`Shapes`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.Shapes)

Layer geometry from create_weights args.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`_DropInputScale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt._DropInputScale)

Bases: [FormatScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme)

Interim: register then drop a W4A16 checkpoint's on-disk input_scale.

Kept for backward compat with previously-exported ModelOpt checkpoints.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`_Fp8PbWoPartialBlock`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt._Fp8PbWoPartialBlock)

Bases: [FormatScheme](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.FormatScheme)

FP8_PB_WO output width that is not a multiple of 128 (a partial trailing block; e.g. GLM's replicated `fused_qkv_a_proj`

= 2048 + 576 = 2624).

The block kernel needs full 128-blocks, so pad the weight up to the block boundary with zeros before the kernel's post-load, then slice the GEMM output back to the logical width. This is #53132's approach, expressed as the format's compute-time residue on the generic method. The cdiv-sized scale from `KFp8Block128`

already matches the padded block count, so only the weight rows and the output need adjusting.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`algos_owned_by(config_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.algos_owned_by)

The linear algos a given config accepts, for its quant_algo validation.

##

`build_linear_method(config, algo, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.build_linear_method)

Construct the linear method for `algo`

.

Returns a bespoke method if one is registered in `LINEAR_METHOD_BUILDERS`

, else the generic `ModelOptLinearMethod`

built from `resolve(algo, config, prefix)`

. Single indirection point shared by the homogeneous and mixed-precision dispatch, so a new format plugs in without editing either `get_quant_method`

.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`maybe_fuse_global_scales(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.maybe_fuse_global_scales)

Alpha = input_global_scale * weight_global_scale, presence-gated.

W4A4 has both -> computed; W4A16 has no input_global_scale -> skipped.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`resolve(algo, subcfg, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.resolve)

Turn a sub-config into (QuantSpec, CkptCtx, format_scheme).

Strictly read-only over `subcfg`

: in mixed precision the same sub-config is shared with the MoE method, so writing back would leak a linear-only change into MoE.

## Source code in `vllm/model_executor/layers/quantization/modelopt.py`


##

`select_linear_kernel(spec, layer, rt, weight_shape=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.quantization.modelopt.select_linear_kernel)

Thin family dispatcher on the weight key: nvfp4 / mxfp8 / fp8.