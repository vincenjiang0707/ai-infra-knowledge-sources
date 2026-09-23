source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe)

Classes:

-
–[TrtLlmBf16ExpertsBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsBase)BF16 unquantized TRTLLM-Gen MoE kernels. Shared base for modular and

-
–[TrtLlmBf16ExpertsModular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsModular)BF16 unquantized TRTLLM-Gen MoE kernels. Supports modular interface.

-
–[TrtLlmBf16ExpertsMonolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsMonolithic)BF16 unquantized TRTLLM-Gen MoE kernels. Supports monolithic interface.


Functions:

-
–[view_as_block_major_k](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.view_as_block_major_k)View packed storage, including legacy 4D IPC cache entries.


##

`TrtLlmBf16ExpertsBase`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsBase)

BF16 unquantized TRTLLM-Gen MoE kernels. Shared base for modular and monolithic interfaces.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`


###

`_supports_activation(activation)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsBase._supports_activation)

Supports SiLU (gated) and RELU^2 (non-gated) activations.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`


###

`_supports_current_device()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsBase._supports_current_device)

Supports only Blackwell-family GPUs.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`


###

`_supports_no_act_and_mul()`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsBase._supports_no_act_and_mul)

###

`_supports_quant_scheme(weight_key, activation_key)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsBase._supports_quant_scheme)

Supports only unquantized inputs.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`


##

`TrtLlmBf16ExpertsModular`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsModular)

Bases:

, [TrtLlmBf16ExpertsBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsBase)[FusedMoEExpertsModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsModular)

BF16 unquantized TRTLLM-Gen MoE kernels. Supports modular interface.

Methods:

-
–[moe_problem_size](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsModular.moe_problem_size)Override to handle 4D BlockMajorK weights (E, K/bk, Mn, bk).


## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`


|
|

###

`moe_problem_size(a1, w1, w2, topk_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsModular.moe_problem_size)

Override to handle 4D BlockMajorK weights (E, K/bk, Mn, bk).

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`


##

`TrtLlmBf16ExpertsMonolithic`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsMonolithic)

Bases:

, [TrtLlmBf16ExpertsBase](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsBase)[FusedMoEExpertsMonolithic](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEExpertsMonolithic)

BF16 unquantized TRTLLM-Gen MoE kernels. Supports monolithic interface.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`


|
|

###

`_supports_parallel_config(moe_parallel_config)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.TrtLlmBf16ExpertsMonolithic._supports_parallel_config)

Monolithic kernel supports no-all2all and AG/RS paths.

## Source code in `vllm/model_executor/layers/fused_moe/experts/trtllm_bf16_moe.py`


##

`view_as_block_major_k(weight)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.trtllm_bf16_moe.view_as_block_major_k)

View packed storage, including legacy 4D IPC cache entries.