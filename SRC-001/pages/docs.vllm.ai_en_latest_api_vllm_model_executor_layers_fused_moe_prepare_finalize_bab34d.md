source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.prepare_finalize`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize)

Modules:

-
–[batched](https://docs.vllm.ai/batched/#vllm.model_executor.layers.fused_moe.prepare_finalize.batched) -
–[deepep_ht](https://docs.vllm.ai/deepep_ht/#vllm.model_executor.layers.fused_moe.prepare_finalize.deepep_ht) -
–[deepep_ll](https://docs.vllm.ai/deepep_ll/#vllm.model_executor.layers.fused_moe.prepare_finalize.deepep_ll) -
–[deepep_v2](https://docs.vllm.ai/deepep_v2/#vllm.model_executor.layers.fused_moe.prepare_finalize.deepep_v2) -
–[flashinfer_nvlink_one_sided](https://docs.vllm.ai/flashinfer_nvlink_one_sided/#vllm.model_executor.layers.fused_moe.prepare_finalize.flashinfer_nvlink_one_sided) -
–[flashinfer_nvlink_two_sided](https://docs.vllm.ai/flashinfer_nvlink_two_sided/#vllm.model_executor.layers.fused_moe.prepare_finalize.flashinfer_nvlink_two_sided) -
–[moonep](https://docs.vllm.ai/moonep/#vllm.model_executor.layers.fused_moe.prepare_finalize.moonep)MoonEP (https://github.com/MoonshotAI/MoonEP) prepare/finalize.

-
–[mori](https://docs.vllm.ai/mori/#vllm.model_executor.layers.fused_moe.prepare_finalize.mori) -
–[naive_dp_ep](https://docs.vllm.ai/naive_dp_ep/#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep) -
–[nixl_ep](https://docs.vllm.ai/nixl_ep/#vllm.model_executor.layers.fused_moe.prepare_finalize.nixl_ep)

Classes:

-
–[BatchedPrepareAndFinalize](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.BatchedPrepareAndFinalize)A reference prepare/finalize class that reorganizes the tokens into

-
–[MoEPrepareAndFinalizeNaiveDPEPModular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNaiveDPEPModular)Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.

-
–[MoEPrepareAndFinalizeNaiveDPEPMonolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNaiveDPEPMonolithic)Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.


##

`BatchedPrepareAndFinalize`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.BatchedPrepareAndFinalize)

Bases: [FusedMoEPrepareAndFinalizeModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular)

A reference prepare/finalize class that reorganizes the tokens into expert batched format, i.e. E x max_num_tokens x K. This is the format that the batched dispatch/combine kernels use.

## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/batched.py`


|
|

##

`MoEPrepareAndFinalizeNaiveDPEPModular`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNaiveDPEPModular)

Bases: [FusedMoEPrepareAndFinalizeModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular)

Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.

Uses Torch AR/RS or AR for dispatch/combine operations, applied to the topk weights and ids.

Methods:

-
–[prepare](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNaiveDPEPModular.prepare)Quantize and Dispatch Topk Weights and Topk Ids.


## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep.py`


|
|

###

`prepare(a1, topk_weights, topk_ids, num_experts, expert_map, apply_router_weight_on_input, quant_config, defer_input_quant=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNaiveDPEPModular.prepare)

Quantize and Dispatch Topk Weights and Topk Ids.

## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep.py`


##

`MoEPrepareAndFinalizeNaiveDPEPMonolithic`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNaiveDPEPMonolithic)

Bases: [FusedMoEPrepareAndFinalizeMonolithic](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeMonolithic)

Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.

Uses Torch AR/RS or AR for dispatch/combine operations, applied to the router logits (the MoE kernel runs the router internally).

Methods:

-
–[prepare](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNaiveDPEPMonolithic.prepare)Quantize and Dispatch Router Logits.


## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep.py`


###

`prepare(a1, router_logits, quant_config, defer_input_quant=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.MoEPrepareAndFinalizeNaiveDPEPMonolithic.prepare)

Quantize and Dispatch Router Logits.