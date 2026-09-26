source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/act_quant_fusion/
lastmod: 2026-09-24

#

`vllm.compilation.passes.fusion.act_quant_fusion`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion)

Classes:

-
–[ActivationQuantFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.ActivationQuantFusionPass)This pass fuses a pre-defined set of custom ops into fused ops.

-
–[ActivationQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.ActivationQuantPattern)Base class for Activation+Quant fusions.

-
–[SiluMulBlockQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.SiluMulBlockQuantPattern)Fusion for SiluMul+BlockQuant (FP8 dynamic per-group) Pattern.

-
–[SiluMulFp8StaticQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.SiluMulFp8StaticQuantPattern)Fusion for SiluMul+Fp8StaticQuant Pattern.

-
–[SiluMulNvfp4QuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.SiluMulNvfp4QuantPattern)Fusion for SiluMul+Nvfp4Quant Pattern.


##

`ActivationQuantFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.ActivationQuantFusionPass)

Bases: [VllmFusionPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass)

This pass fuses a pre-defined set of custom ops into fused ops. It uses the torch pattern matcher to find the patterns and replace them.

Because patterns can only be registered once, the pass is a singleton. This will be addressed in a future version of PyTorch: https://github.com/pytorch/pytorch/pull/139321#issuecomment-2452354980

## Source code in `vllm/compilation/passes/fusion/act_quant_fusion.py`


##

`ActivationQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.ActivationQuantPattern)

Bases: [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)

Base class for Activation+Quant fusions. Should not be used directly.

## Source code in `vllm/compilation/passes/fusion/act_quant_fusion.py`


##

`SiluMulBlockQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.SiluMulBlockQuantPattern)

Bases: [ActivationQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.ActivationQuantPattern)

Fusion for SiluMul+BlockQuant (FP8 dynamic per-group) Pattern. Supports group_size 128 and 64 via QuantKey. Parameterized on is_scale_transposed for different scale layouts.

## Source code in `vllm/compilation/passes/fusion/act_quant_fusion.py`


|
|

##

`SiluMulFp8StaticQuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.SiluMulFp8StaticQuantPattern)

Bases: [ActivationQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.ActivationQuantPattern)

Fusion for SiluMul+Fp8StaticQuant Pattern.

## Source code in `vllm/compilation/passes/fusion/act_quant_fusion.py`


##

`SiluMulNvfp4QuantPattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.SiluMulNvfp4QuantPattern)

Bases: [ActivationQuantPattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.act_quant_fusion.ActivationQuantPattern)

Fusion for SiluMul+Nvfp4Quant Pattern.