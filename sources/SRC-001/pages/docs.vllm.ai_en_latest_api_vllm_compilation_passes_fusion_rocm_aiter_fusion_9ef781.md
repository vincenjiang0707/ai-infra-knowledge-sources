source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/rocm_aiter_fusion/
lastmod: 2026-09-23

#

`vllm.compilation.passes.fusion.rocm_aiter_fusion`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion)

Classes:

-
–[AddAiterRMSNormPadPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AddAiterRMSNormPadPattern)This pattern replaces an aiter_rmsnorm_with_add & a pad op

-
–[AiterFusedAddRMSFp8GroupQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterFusedAddRMSFp8GroupQuantPattern)This pattern fuses aiter rms_norm_with_add & group fp8 quant custom ops

-
–[AiterFusedAddRMSNormDynamicQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterFusedAddRMSNormDynamicQuantPattern)AITER RMSNorm Fused Add + Dynamic Quantization pattern.

-
–[AiterRMSFp8GroupQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterRMSFp8GroupQuantPattern)This pattern fuses aiter rms_norm & group fp8 quant custom

-
–[AiterRMSNormDynamicQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterRMSNormDynamicQuantPattern)AITER RMSNorm + Dynamic Quantization pattern.

-
–[AiterRMSNormGatedFp8GroupQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterRMSNormGatedFp8GroupQuantPattern)Matches decomposed RMSNormGated + reshape + group FP8 quant and replaces

-
–[AiterSiluMulFp8GroupQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterSiluMulFp8GroupQuantPattern)This pattern fuses aiter silu_and_mul & group fp8 quant custom

-
–[DoubleAiterRMSFp8GroupQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.DoubleAiterRMSFp8GroupQuantPattern)Pattern matching

`rms_norm`

whose output feeds*two*distinct -
–[DoubleAiterRMSFp8GroupQuantViewPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.DoubleAiterRMSFp8GroupQuantViewPattern)View-tolerant variant of

`DoubleAiterRMSFp8GroupQuantPattern`

. -
–[MLADualRMSNormFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.MLADualRMSNormFusionPass)Post-grad PatternMatcher pass that fuses paired q / kv RMS norms in

-
–[MLADualRMSNormPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.MLADualRMSNormPattern)Fuse paired q_a_layernorm + kv_a_layernorm in MLA attention into

-
–[MLADualRMSPerTokenQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.MLADualRMSPerTokenQuantPattern)Fuse the MLA FP8 attention path -- q-latent RMSNorm + FP8

*per-token*quant -
–[RocmAiterRMSNormQuantFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterRMSNormQuantFusionPass)This pass fuses aiter rms_norm & vllm/aiter quant custom ops

-
–[RocmAiterSiluMulFp8GroupQuantFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterSiluMulFp8GroupQuantFusionPass)This pass fuses a pre-defined set of custom ops into fused ops.

-
–[RocmAiterTritonAddRMSNormPadFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterTritonAddRMSNormPadFusionPass)This pass replaces an AITER CK RMSNorm + residual add and a pad op


##

`AddAiterRMSNormPadPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AddAiterRMSNormPadPattern)

This pattern replaces an aiter_rmsnorm_with_add & a pad op with a custom triton_add_rmsnorm_pad op from AITER.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`AiterFusedAddRMSFp8GroupQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterFusedAddRMSFp8GroupQuantPattern)

Bases: `AiterRMSNormQuantPattern`


This pattern fuses aiter rms_norm_with_add & group fp8 quant custom ops into a aiter rms_norm_with_add_group_fp8_quant op.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`AiterFusedAddRMSNormDynamicQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterFusedAddRMSNormDynamicQuantPattern)

Bases: `AiterRMSNormQuantPattern`


AITER RMSNorm Fused Add + Dynamic Quantization pattern.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`AiterRMSFp8GroupQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterRMSFp8GroupQuantPattern)

Bases: `AiterRMSNormQuantPattern`


This pattern fuses aiter rms_norm & group fp8 quant custom ops into an aiter rms_norm_group_fp8_quant op.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`AiterRMSNormDynamicQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterRMSNormDynamicQuantPattern)

Bases: `AiterRMSNormQuantPattern`


AITER RMSNorm + Dynamic Quantization pattern.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`AiterRMSNormGatedFp8GroupQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterRMSNormGatedFp8GroupQuantPattern)

Bases: `AiterRMSNormQuantPattern`


Matches decomposed RMSNormGated + reshape + group FP8 quant and replaces with rocm_aiter_fused_rms_gated_fp8_group_quant.

The norm operates per-head, on either (N*H, D) or (N, H, D). The compiler folds the reshape chain so after norm the result goes through reshape->merge->quant. The pattern reshapes to (N, H*D) before calling MatcherQuantFP8 so that _quantize_group_native sees the full hidden dim and computes the correct num_groups.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


|
|

##

`AiterSiluMulFp8GroupQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.AiterSiluMulFp8GroupQuantPattern)

Bases: [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)

This pattern fuses aiter silu_and_mul & group fp8 quant custom ops into an aiter silu_and_mul_group_fp8_quant op.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`DoubleAiterRMSFp8GroupQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.DoubleAiterRMSFp8GroupQuantPattern)

Bases: `AiterRMSNormQuantPattern`


Pattern matching `rms_norm`

whose output feeds *two* distinct `rocm_aiter_group_fp8_quant`

consumers, replacing it with two independent fused `rms_norm_group_fp8_quant`

ops.

Repeating the rms_norm in the replacement is preferable to leaving the fused 16-bit rms output materialized for two unfused quant consumers, and matches what the previous manual graph surgery achieved by cloning the rms_norm node.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`DoubleAiterRMSFp8GroupQuantViewPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.DoubleAiterRMSFp8GroupQuantViewPattern)

Bases: `AiterRMSNormQuantPattern`


View-tolerant variant of `DoubleAiterRMSFp8GroupQuantPattern`

.

Matches the same 1-to-2 fan-out, but with a `view`

/`reshape`

between the `rms_norm`

output and the two `rocm_aiter_group_fp8_quant`

consumers::

```
rms_norm -> view -> rocm_aiter_group_fp8_quant
\-> view -> rocm_aiter_group_fp8_quant
```


This shape arises in DeepSeek-V3.2's MLA indexer q_c norm, where the FP8 linear path's 2D-flatten boilerplate (`Fp8BlockScaledMMLinearKernel.apply_weights`

) inserts a view between the rms_norm output and each FP8 group quant op. The non-view sibling pattern silently no-ops on this graph because the pattern matcher requires the in-graph and in-pattern node shapes to align.

The trace_fn runs Inductor's `view_to_reshape`

post-grad pass to normalize `view`

to `reshape`

in both the pattern and the input graph, widening the match without touching the no-view sibling.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


|
|

##

`MLADualRMSNormFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.MLADualRMSNormFusionPass)

Bases: [VllmFusionPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass)

Post-grad PatternMatcher pass that fuses paired q / kv RMS norms in MLA attention into `fused_mla_dual_rms_norm`

backed by aiter's `fused_qk_rmsnorm`

HIP kernel.

The FP8 attention path is also handled via :class:`MLADualRMSPerTokenQuantPattern`

, which fuses the q-latent RMSNorm + FP8 per-token quant together with the kv-latent RMSNorm into `fused_mla_dual_rms_norm_per_token_quant`

backed by aiter's `fused_qk_rmsnorm_per_token_quant`

HIP kernel.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`MLADualRMSNormPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.MLADualRMSNormPattern)

Bases: [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)[..., [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]

Fuse paired q_a_layernorm + kv_a_layernorm in MLA attention into AITER's `fused_qk_rmsnorm`

HIP kernel.

Target FX-graph pattern (unfused, `vllm_ir`

stage)::

```
gemm -> split_with_sizes([q_dim, kv_dim])
+-- q_c -> vllm_ir.rms_norm(q_c, q_w, eps)
+-- kv_lora -> split_with_sizes([kv_c_dim, k_pe_dim])
+-- kv_c -> vllm_ir.rms_norm(kv_c, kv_w, eps)
+-- k_pe
```


The pattern covers the connected subgraph rooted at the first `split_with_sizes`

(which produces `q_c`

and `kv_lora`

), through the two `rms_norm`

calls, and the `k_pe`

passthrough.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


|
|

##

`MLADualRMSPerTokenQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.MLADualRMSPerTokenQuantPattern)

Bases: [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)[..., [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]

Fuse the MLA FP8 attention path -- q-latent RMSNorm + FP8 *per-token* quant plus kv-latent RMSNorm -- into AITER's `fused_qk_rmsnorm_per_token_quant`

.

With a per-token FP8 `q_b_proj`

(Quark / ModelOpt), the earlier `RocmAiterRMSNormQuantFusionPass`

folds the q side into `rocm_aiter_rmsnorm_fused_dynamic_quant`

and leaves the kv side a plain `vllm_ir.rms_norm`

. This pattern matches that asymmetric pair::

```
gemm -> split_with_sizes([q_dim, kv_dim])
+-- q_c -> rocm_aiter_rmsnorm_fused_dynamic_quant -> (q_fp8, q_scale)
+-- kv_lora -> split_with_sizes([kv_c_dim, k_pe_dim])
+-- kv_c -> vllm_ir.rms_norm -> kv_normed (bf16)
+-- k_pe
```


## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


|
|

##

`RocmAiterRMSNormQuantFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterRMSNormQuantFusionPass)

Bases: [VllmPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass)

This pass fuses aiter rms_norm & vllm/aiter quant custom ops into a fused rms_norm_quant op. It also supports fused_add_rms_norm.

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


|
|

##

`RocmAiterSiluMulFp8GroupQuantFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterSiluMulFp8GroupQuantFusionPass)

Bases: [VllmFusionPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass)

This pass fuses a pre-defined set of custom ops into fused ops. It uses the torch pattern matcher to find the patterns and replace them.

Because patterns can only be registered once, the pass is a singleton. This will be addressed in a future version of PyTorch: https://github.com/pytorch/pytorch/pull/139321#issuecomment-2452354980

## Source code in `vllm/compilation/passes/fusion/rocm_aiter_fusion.py`


##

`RocmAiterTritonAddRMSNormPadFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.rocm_aiter_fusion.RocmAiterTritonAddRMSNormPadFusionPass)

Bases: [VllmPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternMatcherPass)

This pass replaces an AITER CK RMSNorm + residual add and a pad op with an triton_add_rmsnorm_pad op from AITER.