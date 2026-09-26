source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/rms_quant_fusion/
lastmod: 2026-09-24

#

`vllm.compilation.passes.fusion.rms_quant_fusion`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion)

Classes:

-
–[FusedAddRMSNormNvfp4QuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion.FusedAddRMSNormNvfp4QuantPattern)Fuse add-RMSNorm with NVFP4 quantization for either scale layout.

-
–[FusedRMSQuantKey](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion.FusedRMSQuantKey)Named tuple for identifying the type of RMSNorm + quant fusion.

-
–[RMSNormQuantFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion.RMSNormQuantFusionPass)This pass fuses rms_norm & quant custom ops into a fused rms_norm_quant op.


##

`FusedAddRMSNormNvfp4QuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion.FusedAddRMSNormNvfp4QuantPattern)

Fuse add-RMSNorm with NVFP4 quantization for either scale layout.

## Source code in `vllm/compilation/passes/fusion/rms_quant_fusion.py`


|
|

##

`FusedRMSQuantKey`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion.FusedRMSQuantKey)

Bases: [NamedTuple](https://docs.python.org/3/library/typing.html#typing.NamedTuple)

Named tuple for identifying the type of RMSNorm + quant fusion. quant: type of quantization fused_add: does the op also perform the residual add

## Source code in `vllm/compilation/passes/fusion/rms_quant_fusion.py`


##

`RMSNormQuantFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion.RMSNormQuantFusionPass)

Bases: [VllmPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass)

This pass fuses rms_norm & quant custom ops into a fused rms_norm_quant op. It also supports fused_add_rms_norm.

## Source code in `vllm/compilation/passes/fusion/rms_quant_fusion.py`


|
|

##

`_flashinfer_fused_add_rms_norm_nvfp4_quant(result, result_block_scale, residual, input, weight, input_global_scale, block_scale_unswizzled, is_sf_swizzled_layout, epsilon)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion._flashinfer_fused_add_rms_norm_nvfp4_quant)

FlashInfer fused add + RMSNorm + NVFP4 quantization.

## Source code in `vllm/compilation/passes/fusion/rms_quant_fusion.py`


##

`_rms_input_weight_dtype_match(match)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rms_quant_fusion._rms_input_weight_dtype_match)

Prevent fusion when rms_norm input and weight dtypes differ.