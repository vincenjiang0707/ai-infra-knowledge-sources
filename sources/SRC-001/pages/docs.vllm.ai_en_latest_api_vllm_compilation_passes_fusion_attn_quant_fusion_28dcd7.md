source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/attn_quant_fusion/
lastmod: 2026-09-24

#

`vllm.compilation.passes.fusion.attn_quant_fusion`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion)

Classes:

-
–[AttnFp8StaticQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.AttnFp8StaticQuantPattern)Fusion for Attention+Fp8StaticQuant.

-
–[AttnNvfp4QuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.AttnNvfp4QuantPattern)Fusion for Attention+Nvfp4Quant.

-
–[AttnQuantFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.AttnQuantFusionPass)This pass fuses post-attention quantization onto attention if supported.

-
–[RocmAttnFp8StaticQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.RocmAttnFp8StaticQuantPattern)Fuse AITER static quantization while preserving its scale output.


##

`AttnFp8StaticQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.AttnFp8StaticQuantPattern)

Bases: [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)[..., [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor) | [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]

Fusion for Attention+Fp8StaticQuant.

Only triggers when the attention implementation returns True in `fused_output_quant_supported()`

. If the pattern is found, the Fp8StaticQuant op will be removed from the graph, and its scale will be passed into Attention op as the `output_scale`

argument.

## Source code in `vllm/compilation/passes/fusion/attn_quant_fusion.py`


|
|

##

`AttnNvfp4QuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.AttnNvfp4QuantPattern)

Bases: [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)[..., [tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), [Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]]

Fusion for Attention+Nvfp4Quant.

Only triggers when the attention implementation returns True in `fused_output_quant_supported()`

. If the pattern is found, the Nvfp4Quant op will be removed from the graph, and its scale will be passed into Attention op as the `output_scale`

argument.

## Source code in `vllm/compilation/passes/fusion/attn_quant_fusion.py`


|
|

##

`AttnQuantFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.AttnQuantFusionPass)

Bases: [VllmFusionPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass)

This pass fuses post-attention quantization onto attention if supported.

It uses the pattern matcher and matches each layer manually, as strings cannot be wildcarded. This also lets us check support on attention layers upon registration instead of during pattern matching.

Currently, only static fp8 quant is supported, but patterns could easily be added for other quant schemes and dtypes. The bigger hurdle for wider support are attention kernels, which need to support fusing output quant.

## Source code in `vllm/compilation/passes/fusion/attn_quant_fusion.py`


##

`RocmAttnFp8StaticQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.RocmAttnFp8StaticQuantPattern)

Bases: [AttnFp8StaticQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.attn_quant_fusion.AttnFp8StaticQuantPattern)

Fuse AITER static quantization while preserving its scale output.