source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/cpu_moe/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.experts.cpu_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe)

CPU fused MoE experts.

Classes:

-
–[ArmCPUExpertsInt8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.ArmCPUExpertsInt8)Arm INT8 MoE with per-token activation and channelwise weight quantization.

-
–[ArmCPUUnquantizedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.ArmCPUUnquantizedExperts)Arm NEON grouped-gemm unquantized MoE experts.

-
–[CPUExpertsFp8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsFp8)CPU FP8 W8A16 block-quantized modular MoE experts.

-
–[CPUExpertsFp8W8A8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsFp8W8A8)CPU FP8 W8A8 block-quantized modular MoE experts.

-
–[CPUExpertsInt4](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsInt4)CPU INT4 W4A16 group-quantized modular MoE experts.

-
–[CPUExpertsInt8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsInt8)CPU INT8 W8A8 per-channel weight / dynamic per-token activation

-
–[CPUExpertsMxfp4](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsMxfp4)CPU MXFP4 W4A16 modular MoE experts.

-
–[CPUUnquantizedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUUnquantizedExperts)Portable vector grouped-gemm unquantized MoE experts.

-
–[PowerCPUExpertsInt8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.PowerCPUExpertsInt8)POWER VSX INT8 MoE with per-token activation and channelwise weight quant.

-
–[PowerCPUUnquantizedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.PowerCPUUnquantizedExperts)PowerPC VSX grouped-gemm unquantized MoE experts.

-
–[X86CPUUnquantizedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.X86CPUUnquantizedExperts)x86 AMX grouped-gemm unquantized MoE experts.

-
–[ZenCPUExpertsInt8](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.ZenCPUExpertsInt8)AMD Zen INT8 MoE with per-token activation and channelwise weight


Functions:

-
–[prepare_fp8_moe_layer_for_cpu](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_fp8_moe_layer_for_cpu)VNNI-prepack FP8 MoE weights for CPU kernel.

-
–[prepare_fp8_w8a8_moe_layer_for_cpu](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_fp8_w8a8_moe_layer_for_cpu)Prepack FP8 W8A8 MoE weights for CPU kernel.

-
–[prepare_int4_moe_layer_for_cpu](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu)Repack INT4 MoE weights via convert_weight_packed_scale_zp for CPU.

-
–[prepare_int8_moe_layer_for_cpu](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int8_moe_layer_for_cpu)Prepack INT8 MoE weights for the current CPU architecture.

-
–[prepare_mxfp4_moe_layer_for_cpu](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_mxfp4_moe_layer_for_cpu)VNNI-prepack MXFP4 MoE weights and repack scales for CPU AMX kernel.


##

`ArmCPUExpertsInt8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.ArmCPUExpertsInt8)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Arm INT8 MoE with per-token activation and channelwise weight quantization.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

##

`ArmCPUUnquantizedExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.ArmCPUUnquantizedExperts)

Bases: [CPUUnquantizedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUUnquantizedExperts)

Arm NEON grouped-gemm unquantized MoE experts.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`CPUExpertsFp8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsFp8)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

CPU FP8 W8A16 block-quantized modular MoE experts.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

##

`CPUExpertsFp8W8A8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsFp8W8A8)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

CPU FP8 W8A8 block-quantized modular MoE experts.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

##

`CPUExpertsInt4`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsInt4)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

CPU INT4 W4A16 group-quantized modular MoE experts.

Weights are int4 (packed), activations are bf16/fp16. Internally uses int8 compute via fused_experts_cpu with INT4_W4A8.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

##

`CPUExpertsInt8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsInt8)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

CPU INT8 W8A8 per-channel weight / dynamic per-token activation modular MoE experts.

Methods:

-
–[process_weights_after_loading](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsInt8.process_weights_after_loading)VNNI-prepack INT8 MoE weights for CPU kernel.


## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

###

`process_weights_after_loading(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsInt8.process_weights_after_loading)

VNNI-prepack INT8 MoE weights for CPU kernel.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`CPUExpertsMxfp4`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUExpertsMxfp4)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

CPU MXFP4 W4A16 modular MoE experts.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

##

`CPUUnquantizedExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUUnquantizedExperts)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Portable vector grouped-gemm unquantized MoE experts.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

###

`_pad_moe_intermediate(layer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUUnquantizedExperts._pad_moe_intermediate)

Zero-pad the per-partition MoE intermediate dim of both weights and the expert bias, see `_padded_intermediate_size`

.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`PowerCPUExpertsInt8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.PowerCPUExpertsInt8)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

POWER VSX INT8 MoE with per-token activation and channelwise weight quant.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

##

`PowerCPUUnquantizedExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.PowerCPUUnquantizedExperts)

Bases: [CPUUnquantizedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUUnquantizedExperts)

PowerPC VSX grouped-gemm unquantized MoE experts.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`X86CPUUnquantizedExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.X86CPUUnquantizedExperts)

Bases: [CPUUnquantizedExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.CPUUnquantizedExperts)

x86 AMX grouped-gemm unquantized MoE experts.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`ZenCPUExpertsInt8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.ZenCPUExpertsInt8)

Bases: [FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

AMD Zen INT8 MoE with per-token activation and channelwise weight quantization, dispatched through zentorch.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


|
|

##

`prepare_fp8_moe_layer_for_cpu(w13, w2)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_fp8_moe_layer_for_cpu)

VNNI-prepack FP8 MoE weights for CPU kernel.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`prepare_fp8_w8a8_moe_layer_for_cpu(w13, w2, w13_scale, w2_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_fp8_w8a8_moe_layer_for_cpu)

Prepack FP8 W8A8 MoE weights for CPU kernel.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`prepare_int4_moe_layer_for_cpu(w13_packed, w2_packed, w13_scale, w2_scale, quant_algo=CPUQuantAlgo.GPTQ, w13_zeros=None, w2_zeros=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu)

Repack INT4 MoE weights via convert_weight_packed_scale_zp for CPU.

Parameters:

-

(`w13_packed`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu(w13_packed))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[E, K//8, 2*I] int32 (packed int4)

-

(`w2_packed`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu(w2_packed))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[E, I//8, K] int32 (packed int4)

-

(`w13_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu(w13_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[E, num_groups, 2*I] float16/bf16

-

(`w2_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu(w2_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[E, num_groups, K] float16/bf16

-

(`quant_algo`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu(quant_algo))`CPUQuantAlgo`

, default:`GPTQ`

) –CPUQuantAlgo.GPTQ or CPUQuantAlgo.AWQ

-

(`w13_zeros`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu(w13_zeros))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional [E, num_groups, N//8] int32 packed zeros. If None, synthetic zeros are created for symmetric quant.

-

(`w2_zeros`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int4_moe_layer_for_cpu(w2_zeros))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –optional [E, num_groups, N//8] int32 packed zeros. If None, synthetic zeros are created for symmetric quant.


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)](blocked_w13, blocked_w2, blocked_s13, blocked_s2, blocked_z13, blocked_z2)


## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`prepare_int8_moe_layer_for_cpu(w13, w2)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_int8_moe_layer_for_cpu)

Prepack INT8 MoE weights for the current CPU architecture.

## Source code in `vllm/model_executor/layers/fused_moe/experts/cpu_moe.py`


##

`prepare_mxfp4_moe_layer_for_cpu(w13, w2, w13_scale, w2_scale)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.cpu_moe.prepare_mxfp4_moe_layer_for_cpu)

VNNI-prepack MXFP4 MoE weights and repack scales for CPU AMX kernel.