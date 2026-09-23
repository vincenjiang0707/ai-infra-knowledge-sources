source: https://docs.vllm.ai/en/latest/api/vllm/compilation/passes/fusion/add_rms_fusion/
lastmod: 2026-09-23

#

`vllm.compilation.passes.fusion.add_rms_fusion`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion)

Classes:

-
–[AddRMSNormFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion.AddRMSNormFusionPass)Fuse residual Add and RMSNorm emitted separately by the Transformers backend.

-
–[FusedAddRMSNormReshapePattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion.FusedAddRMSNormReshapePattern)Move a prefix-flatten before fused add RMSNorm.

-
–[RMSNormReshapeFusionPass](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion.RMSNormReshapeFusionPass)Move the Transformers backend's post-RMSNorm flatten before the norm

-
–[RMSNormReshapePattern](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion.RMSNormReshapePattern)Move a prefix-flatten before RMSNorm.


##

`AddRMSNormFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion.AddRMSNormFusionPass)

Bases: [VllmFusionPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass)

Fuse residual Add and RMSNorm emitted separately by the Transformers backend.

## Source code in `vllm/compilation/passes/fusion/add_rms_fusion.py`


##

`FusedAddRMSNormReshapePattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion.FusedAddRMSNormReshapePattern)

Bases: [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)

Move a prefix-flatten before fused add RMSNorm.

## Source code in `vllm/compilation/passes/fusion/add_rms_fusion.py`


##

`RMSNormReshapeFusionPass`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion.RMSNormReshapeFusionPass)

Bases: [VllmFusionPatternMatcherPass](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmFusionPatternMatcherPass)

Move the Transformers backend's post-RMSNorm flatten before the norm for downstream 2D fusions.

## Source code in `vllm/compilation/passes/fusion/add_rms_fusion.py`


##

`RMSNormReshapePattern`

[¶](https://docs.vllm.ai#vllm.compilation.passes.fusion.add_rms_fusion.RMSNormReshapePattern)

Bases: [VllmPatternReplacement](https://docs.vllm.ai/vllm_inductor_pass/#vllm.compilation.passes.vllm_inductor_pass.VllmPatternReplacement)

Move a prefix-flatten before RMSNorm.