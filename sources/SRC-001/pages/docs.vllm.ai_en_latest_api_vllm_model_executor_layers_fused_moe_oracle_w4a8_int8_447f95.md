source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/w4a8_int8/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.oracle.w4a8_int8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8)

Functions:

-
–[backend_to_kernel_cls](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.backend_to_kernel_cls)Map W4A8Int8MoeBackend to kernel class.

-
–[convert_to_w4a8_int8_moe_format](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format)Pack INT4 MoE weights to KleidiAI format.

-
–[make_w4a8_int8_moe_kernel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_kernel)Create FusedMoEKernel for W4A8 Int8 MoE.

-
–[make_w4a8_int8_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_quant_config)Create FusedMoEQuantConfig for W4A8 Int8 MoE.

-
–[map_w4a8_int8_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.map_w4a8_int8_backend)Map user's MoEBackend to W4A8Int8MoeBackend.

-
–[pack_int4_weights_for_kleidi](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.pack_int4_weights_for_kleidi)Pack INT4 weights (stored as int8 in [-8,7]) to KleidiAI format.

-
–[select_w4a8_int8_moe_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.select_w4a8_int8_moe_backend)Select the primary W4A8 Int8 MoE backend.


##

`_get_priority_backends(moe_config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8._get_priority_backends)

Get available backends in priority order based on platform and config.

Currently only CPU INT4 backend is available for W4A8 INT8 MoE.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`


##

`backend_to_kernel_cls(backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.backend_to_kernel_cls)

Map W4A8Int8MoeBackend to kernel class.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`


##

`convert_to_w4a8_int8_moe_format(w13_weight, w2_weight, w13_weight_scale, w2_weight_scale, group_size, w13_bias=None, w2_bias=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format)

Pack INT4 MoE weights to KleidiAI format.

This function packs the INT4 weights (stored as int8 values) into the format expected by the KleidiAI dynamic_4bit_int_moe kernel.

Parameters:

-

(`w13_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format(w13_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[E, 2*IN, H] int8 tensor (int4 values in [-8,7])

-

(`w2_weight`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format(w2_weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[E, H, IN] int8 tensor (int4 values in [-8,7])

-

(`w13_weight_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format(w13_weight_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[E, 2*IN, H/g or 1] scale tensor

-

(`w2_weight_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format(w2_weight_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[E, H, IN/g or 1] scale tensor

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Quantization group size (-1 for channel-wise)

-

(`w13_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format(w13_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional [E, 2*IN] bias tensor

-

(`w2_bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.convert_to_w4a8_int8_moe_format(w2_bias))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional [E, H] bias tensor


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None,[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None]Tuple of (w13_packed, w2_packed) tensors


## Source code in `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`


##

`make_w4a8_int8_moe_kernel(moe_quant_config, moe_config, experts_cls, routing_tables=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_kernel)

Create FusedMoEKernel for W4A8 Int8 MoE.

Parameters:

-

(`moe_quant_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_kernel(moe_quant_config))

) –[FusedMoEQuantConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig)Quantization configuration

-

(`moe_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_kernel(moe_config))

) –[FusedMoEConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig)MoE configuration

-

(`experts_cls`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_kernel(experts_cls))

) –[type](https://docs.python.org/3/builtins/functions.html#type)[[FusedMoEExperts](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts)]Expert kernel class (should be CPUExpertsInt4)

-

(`routing_tables`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_kernel(routing_tables))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)] | None`None`

) –Optional routing tables for expert parallelism


Returns:

-

–[FusedMoEKernel](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEKernel)Configured FusedMoEKernel instance


## Source code in `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`


##

`make_w4a8_int8_moe_quant_config(block_shape=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_quant_config)

Create FusedMoEQuantConfig for W4A8 Int8 MoE.

Parameters:

-

(`block_shape`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.make_w4a8_int8_moe_quant_config(block_shape))

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –Quantization block shape (row, col). For channel-wise: (-1, 1) or None For group-wise: (1, group_size)


Returns:

-

–[FusedMoEQuantConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEQuantConfig)FusedMoEQuantConfig with appropriate settings for W4A8 Int8


## Source code in `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`


##

`map_w4a8_int8_backend(runner_backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.map_w4a8_int8_backend)

Map user's MoEBackend to W4A8Int8MoeBackend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`


##

`pack_int4_weights_for_kleidi(int4_as_int8, scales, bias, in_features, out_features, group_size)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.pack_int4_weights_for_kleidi)

Pack INT4 weights (stored as int8 in [-8,7]) to KleidiAI format.

Parameters:

-

(`int4_as_int8`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.pack_int4_weights_for_kleidi(int4_as_int8))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[out, in] int8 tensor with values in [-8, 7]

-

(`scales`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.pack_int4_weights_for_kleidi(scales))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[out, in//group_size] or [out, 1] for channel-wise

-

(`bias`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.pack_int4_weights_for_kleidi(bias))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None[out] optional bias

-

(`in_features`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.pack_int4_weights_for_kleidi(in_features))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Input dimension

-

(`out_features`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.pack_int4_weights_for_kleidi(out_features))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Output dimension

-

(`group_size`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.pack_int4_weights_for_kleidi(group_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Quantization group size (-1 for channel-wise)


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Packed weight tensor in KleidiAI format


## Source code in `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`


##

`select_w4a8_int8_moe_backend(config, weight_key, activation_key)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.select_w4a8_int8_moe_backend)

Select the primary W4A8 Int8 MoE backend.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.select_w4a8_int8_moe_backend(config))

) –[FusedMoEConfig](https://docs.vllm.ai/config/#vllm.model_executor.layers.fused_moe.config.FusedMoEConfig)MoE configuration

-

(`weight_key`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.select_w4a8_int8_moe_backend(weight_key))

) –[QuantKey](https://docs.vllm.ai/quantization/utils/quant_utils/#vllm.model_executor.layers.quantization.utils.quant_utils.QuantKey)| NoneWeight quantization key (should be one of kInt4W4A8Static*)

-

(`activation_key`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.w4a8_int8.select_w4a8_int8_moe_backend(activation_key))

) –[QuantKey](https://docs.vllm.ai/quantization/utils/quant_utils/#vllm.model_executor.layers.quantization.utils.quant_utils.QuantKey)| NoneActivation quantization key (currently unused for W4A8)


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[W4A8Int8MoeBackend,[type](https://docs.python.org/3/builtins/functions.html#type)[[FusedMoEExperts](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExperts)]]Tuple of (backend, kernel_class)


## Source code in `vllm/model_executor/layers/fused_moe/oracle/w4a8_int8.py`


|
|