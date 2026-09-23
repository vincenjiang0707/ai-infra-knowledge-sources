source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/allreduce_rms_fusion/
lastmod: 2026-09-23

#

`vllm.compilation.passes.fusion.allreduce_rms_fusion`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion)

Classes:

-
–[AiterAllreduceFusedAddRMSNormGroupQuantFP8Pattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AiterAllreduceFusedAddRMSNormGroupQuantFP8Pattern)`fused_add`

variant of`AiterAllreduceFusedRMSNormGroupQuantFP8Pattern`

. -
–[AiterAllreduceFusedAddRMSNormGroupQuantWithIndexerPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AiterAllreduceFusedAddRMSNormGroupQuantWithIndexerPattern)Indexer-fan-out variant of

`AiterAllreduceFusedAddRMSNormGroupQuantFP8Pattern`

. -
–[AiterAllreduceFusedAddRMSNormOutputOnlyPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AiterAllreduceFusedAddRMSNormOutputOnlyPattern)Match the add-RMSNorm form when its residual output is dead.

-
–[AiterAllreduceFusedRMSNormGroupQuantFP8Pattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AiterAllreduceFusedRMSNormGroupQuantFP8Pattern)Fuse AllReduce + RMSNorm + per-group FP8 quant into a single AITER

-
–[AllReduceFusedAddGemmaRMSNormPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddGemmaRMSNormPattern)Gemma-style variant of AllReduceFusedAddRMSNormPattern (with residual).

-
–[AllReduceFusedAddRMSNormPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormPattern)This pattern replaces the allreduce + rms norm (with residual)

-
–[AllReduceFusedAddRMSNormStaticQuantFP8Pattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormStaticQuantFP8Pattern)This pattern replaces the allreduce + rms norm (with residual)

-
–[AllReduceFusedAddRMSNormStaticQuantNVFP4Pattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormStaticQuantNVFP4Pattern)This pattern replaces the allreduce + rms norm (with residual)

-
–[AllReduceFusedRMSNormStaticQuantFP8Pattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedRMSNormStaticQuantFP8Pattern)This pattern replaces the allreduce + rms norm (without residual)

-
–[AllReduceFusedRMSNormStaticQuantNVFP4Pattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedRMSNormStaticQuantNVFP4Pattern)This pattern replaces the allreduce + rms norm (without residual)

-
–[AllReduceGemmaRMSNormPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceGemmaRMSNormPattern)Gemma-style variant of AllReduceRMSNormPattern (no residual).

-
–[AllReduceRMSNormPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceRMSNormPattern)This pattern replaces the allreduce + rms norm (without residual)

-
–[FlashInferFusedAllReduceParams](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.FlashInferFusedAllReduceParams)Parameters for FlashInfer fused allreduce operations.


##

`AiterAllreduceFusedAddRMSNormGroupQuantFP8Pattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AiterAllreduceFusedAddRMSNormGroupQuantFP8Pattern)

Bases: `BasePattern`

, [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)

`fused_add`

variant of `AiterAllreduceFusedRMSNormGroupQuantFP8Pattern`

.

Targets the dominant DSv3.2-style post-attention / post-MLP path: `all_reduce -> fused_add_rms_norm -> group_fp8_quant`

. Returns the FP8 quant output, the residual carry-over, and the per-group scale.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


|
|

##

`AiterAllreduceFusedAddRMSNormGroupQuantWithIndexerPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AiterAllreduceFusedAddRMSNormGroupQuantWithIndexerPattern)

Bases: `BasePattern`

, [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)

Indexer-fan-out variant of `AiterAllreduceFusedAddRMSNormGroupQuantFP8Pattern`

.

Targets the DSv3.2 post-attention / post-MLP path where the post-AR normed activation has two consumers: a per-group FP8 quant for `fused_qkv_a_proj`

*and* a bf16 `rocm_unquantized_gemm`

for the indexer `wk_weights_proj`

. The single-consumer pattern above cannot fire when this fan-out is present, so without this pattern the standalone FP8 quant kernel survives unfused (~535us / decode step on DSv3.2 MI355X TP4).

Lowers to `rocm_aiter_fused_allreduce_rmsnorm_quant_per_group_with_bf16_norm`

(the `emit_bf16=True`

variant of the AR+RMS+QUANT launcher, which returns FP8 quant + scales + bf16 normed activations in one kernel) and rewires the indexer GEMM onto the emitted bf16 norm output. The RMS output is also a graph output in DSv3.2's residual carry; it is returned as a pattern output so the matcher can substitute the bf16 norm in its place.

The trailing FP8 group-quant is matched via `MatcherQuantFP8`

(consistent with the sibling patterns above), which traces both `QuantFP8.forward_hip`

and `forward_native`

paths and so matches whichever op the call site lowers to (`vllm.rocm_aiter_group_fp8_quant`

).

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


|
|

##

`AiterAllreduceFusedAddRMSNormOutputOnlyPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AiterAllreduceFusedAddRMSNormOutputOnlyPattern)

Bases: `AiterAllreduceFusedAddRMSNormPattern`


Match the add-RMSNorm form when its residual output is dead.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`AiterAllreduceFusedRMSNormGroupQuantFP8Pattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AiterAllreduceFusedRMSNormGroupQuantFP8Pattern)

Bases: `BasePattern`

, [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)

Fuse AllReduce + RMSNorm + per-group FP8 quant into a single AITER custom op.

Matches the AR-side analogue of `AiterRMSFp8GroupQuantPattern`

in `rocm_aiter_fusion.py`

: `all_reduce -> rms_norm -> group_fp8_quant`

fans out into `rocm_aiter_fused_allreduce_rmsnorm_quant_per_group`

.

Without this pattern, `RocmAiterAllReduceFusionPass`

would fuse the `all_reduce + rms_norm`

half (PR #41825 wires that), but the trailing `rocm_aiter_group_fp8_quant`

would still launch as a separate kernel. That standalone quant accounts for ~535us / decode step on DSv3.2 MI355X TP4 -- this pattern eliminates it by absorbing the quant into the AR epilogue. Group size 128 matches the FP8 block-scaled MM kernel used by DSv3.2's linear weights.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


|
|

##

`AllReduceFusedAddGemmaRMSNormPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddGemmaRMSNormPattern)

Bases: `BasePattern`


Gemma-style variant of AllReduceFusedAddRMSNormPattern (with residual).

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`AllReduceFusedAddRMSNormPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormPattern)

Bases: `BasePattern`


This pattern replaces the allreduce + rms norm (with residual) with fused flashinfer implementation. Applies to o_proj + rmsnorm after attn and mlp + rmsnorm before attn.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


|
|

##

`AllReduceFusedAddRMSNormStaticQuantFP8Pattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormStaticQuantFP8Pattern)

Bases: `BasePattern`


This pattern replaces the allreduce + rms norm (with residual) + static fp8 quant with fused flashinfer implementation. Applies to o_proj + rmsnorm after attn + quant and mlp + rmsnorm + quant before attn.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


|
|

##

`AllReduceFusedAddRMSNormStaticQuantNVFP4Pattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedAddRMSNormStaticQuantNVFP4Pattern)

Bases: `BasePattern`


This pattern replaces the allreduce + rms norm (with residual) + static nvfp4 quant with fused flashinfer implementation. Applies to o_proj + rmsnorm after attn + quant and mlp + rmsnorm + quant before attn.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


|
|

##

`AllReduceFusedRMSNormStaticQuantFP8Pattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedRMSNormStaticQuantFP8Pattern)

Bases: `BasePattern`


This pattern replaces the allreduce + rms norm (without residual) + static fp8 quant with fused flashinfer implementation. Applies to allreduce + rmsnorm + quant before attn in the first Transformer block.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`AllReduceFusedRMSNormStaticQuantNVFP4Pattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceFusedRMSNormStaticQuantNVFP4Pattern)

Bases: `BasePattern`


This pattern replaces the allreduce + rms norm (without residual) + static nvfp4 quant with fused flashinfer implementation. Applies to allreduce + rmsnorm + quant before attn in the first Transformer block.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


|
|

##

`AllReduceGemmaRMSNormPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceGemmaRMSNormPattern)

Bases: `BasePattern`


Gemma-style variant of AllReduceRMSNormPattern (no residual).

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`AllReduceRMSNormPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.AllReduceRMSNormPattern)

Bases: `BasePattern`


This pattern replaces the allreduce + rms norm (without residual) with fused flashinfer implementation. Applies to allreduce + rmsnorm before attn in the first Transformer block.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`FlashInferFusedAllReduceParams`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion.FlashInferFusedAllReduceParams)

Parameters for FlashInfer fused allreduce operations.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`_fused_ar_workspace_hidden_dim(config)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion._fused_ar_workspace_hidden_dim)

Widest hidden size across the target and (optional) draft models.

The FlashInfer allreduce+RMSNorm workspace is a process-global singleton created eagerly at pass construction and reused by every model. Under speculative decoding the draft shares it, so it must fit the larger of the two hidden sizes; a draft wider than the target otherwise overflows the target-sized buffer (vLLM #52023).

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`_norm_input_weight_dtype_match(match)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion._norm_input_weight_dtype_match)

Prevent fusion when the norm input and weight dtypes differ (e.g. a Gemma fp32 weight.float()+1 gamma), covering rms_norm and fused_add_rms_norm.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`_view_flashinfer_nvfp4_scale_out_as_int32(scale_out)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion._view_flashinfer_nvfp4_scale_out_as_int32)

View FlashInfer's NVFP4 scale buffer back as vLLM's int32 format.

## Source code in `vllm/compilation/passes/fusion/allreduce_rms_fusion.py`


##

`_view_nvfp4_scale_out_for_flashinfer(scale_out)`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.allreduce_rms_fusion._view_nvfp4_scale_out_for_flashinfer)

View vLLM's packed NVFP4 scale buffer as FP8 for FlashInfer.