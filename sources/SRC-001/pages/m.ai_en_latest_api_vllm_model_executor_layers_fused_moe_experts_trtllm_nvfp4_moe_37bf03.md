source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe)

Classes:

-
–[TrtLlmNvFp4ExpertsBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase)NvFp4 TRTLLM-Gen MoE kernels. Supports modular and monolithic interface.

-
–[TrtLlmNvFp4ExpertsModular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsModular)Modular version of the implementation (just the experts).

-
–[TrtLlmNvFp4ExpertsMonolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsMonolithic)Monolithic version of the kernel (router + experts).


##

`TrtLlmNvFp4ExpertsBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase)

NvFp4 TRTLLM-Gen MoE kernels. Supports modular and monolithic interface.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`


|
|

###

`_quantize_per_token_input(hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._quantize_per_token_input)

NVFP4-quantize activations with a per-token global scale.

Returns `(packed_fp4, block_scale, per_token_scale)`

.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`


###

`_supports_activation(activation)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._supports_activation)

Supports SITU only when the installed FlashInfer exposes it.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`


###

`_supports_current_device()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._supports_current_device)

Supports only Blackwell-family GPUs.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`


###

`_supports_no_act_and_mul()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._supports_no_act_and_mul)

###

`_supports_quant_scheme(weight_key, activation_key)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase._supports_quant_scheme)

Supports Nvfp4 quantization.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`


##

`TrtLlmNvFp4ExpertsModular`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsModular)

Bases:

, [TrtLlmNvFp4ExpertsBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase)[FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

Modular version of the implementation (just the experts).

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`


|
|

###

`_supports_parallel_config(moe_parallel_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsModular._supports_parallel_config)

The modular implementation supports all parallel configs.

##

`TrtLlmNvFp4ExpertsMonolithic`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsMonolithic)

Bases:

, [TrtLlmNvFp4ExpertsBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsBase)[FusedMoEExpertsMonolithic](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic)

Monolithic version of the kernel (router + experts).

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_nvfp4_moe.py`


|
|

###

`_supports_parallel_config(moe_parallel_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_nvfp4_moe.TrtLlmNvFp4ExpertsMonolithic._supports_parallel_config)

The modular implementation should be used for the Dp/Ep or EPLB case.