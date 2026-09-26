source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/oracle/mxfp4/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.oracle.mxfp4`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4)

Functions:

-
–[convert_gpt_oss_weight_to_mxfp4_moe_kernel_format](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.convert_gpt_oss_weight_to_mxfp4_moe_kernel_format)Convert loaded weights into backend-specific kernel format.

-
–[convert_weight_to_mxfp4_moe_kernel_format](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.convert_weight_to_mxfp4_moe_kernel_format)Convert loaded weights into backend-specific kernel format.

-
–[make_mxfp4_moe_kernel](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.make_mxfp4_moe_kernel)Create a FusedMoEKernel for the given MXFP4 backend.

-
–[make_mxfp4_moe_quant_config](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.make_mxfp4_moe_quant_config)Create a FusedMoEQuantConfig for the given MXFP4 backend.

-
–[map_mxfp4_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.map_mxfp4_backend)Map a moe_backend string to its candidate Mxfp4MoeBackends.

-
–[mxfp4_round_up_hidden_size_and_intermediate_size](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.mxfp4_round_up_hidden_size_and_intermediate_size)Round up hidden_size and intermediate_size based on backend requirements.

-
–[select_deepseek_v4_mxfp4_moe_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.select_deepseek_v4_mxfp4_moe_backend)Select the MXFP4 MoE backend with MXFP8 activation as top priority.

-
–[select_mxfp4_moe_backend](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.select_mxfp4_moe_backend)Select the primary MXFP4 MoE backend.


##

`_backend_activation_key(backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4._backend_activation_key)

Map backend to its activation key (FP8, MXFP8, or None for BF16).

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`_filter_by_activation(backends, requested_activation_key)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4._filter_by_activation)

Pick variants matching `requested_activation_key`

; without one, prefer BF16 if the list has any, else keep the list as-is so explicit non-BF16 picks (e.g. the `_afp8`

aliases) still land.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`_get_priority_backends()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4._get_priority_backends)

Get available backends in priority order. SM100+ prefers DeepGEMM FP4 / TRTLLM MXFP8; SM90 falls through to Triton_unfused or Marlin (the backend-level `is_supported_config`

check filters by device capability).

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`_get_priority_backends_for_gpt_oss()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4._get_priority_backends_for_gpt_oss)

Available backends in priority order, BF16-act variant before activation-quantized variant within each vendor family.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`_requires_qwen38_tep8_emulation(config, activation_key)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4._requires_qwen38_tep8_emulation)

Avoid the inaccurate native gfx950 kernel for Qwen3.8 TEP8.

Qwen3.8 Flash Next's routed experts use the distinctive `E=512, H=2560, N=640`

W4A4 shape. With eight-way expert parallelism, AITER operates on 64 local experts and pads `N`

to 768. That native path is not numerically reliable on gfx950, while OCP MX emulation preserves model accuracy. Keep this guard exact so other MXFP4 shapes and smaller EP configurations retain the native backend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`_resolve_activation_key(model_activation_key)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4._resolve_activation_key)

Combine the model-supplied activation key with the user override. Raises on conflict (both set and disagreeing).

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`_user_moe_activation_override()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4._user_moe_activation_override)

User's MoE activation override from quantization_config, or None.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`convert_gpt_oss_weight_to_mxfp4_moe_kernel_format(mxfp4_backend, layer, w13_weight, w2_weight, w13_weight_scale, w2_weight_scale, w13_bias=None, w2_bias=None, w13_input_scale=None, w2_input_scale=None, _cache_permute_indices=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.convert_gpt_oss_weight_to_mxfp4_moe_kernel_format)

Convert loaded weights into backend-specific kernel format.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


|
|

##

`convert_weight_to_mxfp4_moe_kernel_format(mxfp4_backend, layer, w13_weight, w2_weight, w13_weight_scale, w2_weight_scale, w13_bias=None, w2_bias=None, _cache_permute_indices=None, activation=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.convert_weight_to_mxfp4_moe_kernel_format)

Convert loaded weights into backend-specific kernel format.

Supports DeepGEMM, FlashInfer, TRTLLM MXFP8, Triton and Marlin backends.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


|
|

##

`make_mxfp4_moe_kernel(moe_quant_config, moe_config, experts_cls, mxfp4_backend, routing_tables=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.make_mxfp4_moe_kernel)

Create a FusedMoEKernel for the given MXFP4 backend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`make_mxfp4_moe_quant_config(mxfp4_backend, w1_scale, w2_scale, gemm1_alpha=None, gemm1_beta=None, swiglu_limit=None, w1_bias=None, w2_bias=None, a1_scale=None, a2_scale=None, layer=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.make_mxfp4_moe_quant_config)

Create a FusedMoEQuantConfig for the given MXFP4 backend.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


|
|

##

`map_mxfp4_backend(runner_backend)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.map_mxfp4_backend)

Map a moe_backend string to its candidate Mxfp4MoeBackends.

Vendor families return all activation variants; the caller picks one via `activation_key`

and `is_supported_config`

.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`mxfp4_round_up_hidden_size_and_intermediate_size(backend, hidden_size, intermediate_size, activation=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.mxfp4_round_up_hidden_size_and_intermediate_size)

Round up hidden_size and intermediate_size based on backend requirements.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`select_deepseek_v4_mxfp4_moe_backend(config)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.select_deepseek_v4_mxfp4_moe_backend)

Select the MXFP4 MoE backend with MXFP8 activation as top priority. Falls back through BF16 and other backends.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


##

`select_mxfp4_moe_backend(config, activation_key=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.select_mxfp4_moe_backend)

Select the primary MXFP4 MoE backend.

Parameters:

-

(`config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.select_mxfp4_moe_backend(config))

) –[FusedMoEConfig](https://docs.vllm.ai/#vllm.model_executor.layers.fused_moe.FusedMoEConfig)MoE configuration

-

(`activation_key`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.oracle.mxfp4.select_mxfp4_moe_backend(activation_key))

, default:[QuantKey](https://docs.vllm.ai/quantization/utils/quant_utils/#vllm.model_executor.layers.quantization.utils.quant_utils.QuantKey)| None`None`

) –Optional activation quantization key. If provided, overrides the default activation key for backend selection. Use kFp8StaticTensorSym for W4A8 scheme.


Note: Shape-specific fallbacks may still occur at runtime.

## Source code in `vllm/model_executor/layers/fused_moe/oracle/mxfp4.py`


|
|