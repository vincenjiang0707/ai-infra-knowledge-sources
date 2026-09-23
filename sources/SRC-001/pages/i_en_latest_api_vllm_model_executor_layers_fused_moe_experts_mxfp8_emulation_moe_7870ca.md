source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/mxfp8_emulation_moe/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe)

MXFP8 (1x32 block, E8M0 scale) MoE experts on Triton.

`Mxfp8TritonExpertsBase`

stashes E8M0 weight scales for checkpoint layout. `Mxfp8EmulationTritonExperts`

dequantizes to BF16 and runs `TritonExperts`

for devices without a native MXFP8 MoE kernel (e.g. ROCm gfx942 / MI300).

Classes:

-
–[Mxfp8EmulationTritonExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe.Mxfp8EmulationTritonExperts)Dequantize MXFP8 weights to BF16 on the fly and run

`TritonExperts`

. -
–[Mxfp8TritonExpertsBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe.Mxfp8TritonExpertsBase)Shared MXFP8 MoE setup: stash E8M0 scales, clear scales on

`quant_config`

.

##

`Mxfp8EmulationTritonExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe.Mxfp8EmulationTritonExperts)

Bases: [Mxfp8TritonExpertsBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe.Mxfp8TritonExpertsBase)

Dequantize MXFP8 weights to BF16 on the fly and run `TritonExperts`

.

Methods:

-
–[activation](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe.Mxfp8EmulationTritonExperts.activation)Apply GEMM1 activation with quant-config alpha/beta/clamp.


## Source code in `vllm/model_executor/layers/fused_moe/experts/mxfp8_emulation_moe.py`


|
|

###

`activation(activation, output, input, **kwargs)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe.Mxfp8EmulationTritonExperts.activation)

Apply GEMM1 activation with quant-config alpha/beta/clamp.

## Source code in `vllm/model_executor/layers/fused_moe/experts/mxfp8_emulation_moe.py`


##

`Mxfp8TritonExpertsBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.mxfp8_emulation_moe.Mxfp8TritonExpertsBase)

Bases: [TritonExperts](https://docs.vllm.ai/triton_moe/#vllm.model_executor.layers.fused_moe.experts.triton_moe.TritonExperts)

Shared MXFP8 MoE setup: stash E8M0 scales, clear scales on `quant_config`

.