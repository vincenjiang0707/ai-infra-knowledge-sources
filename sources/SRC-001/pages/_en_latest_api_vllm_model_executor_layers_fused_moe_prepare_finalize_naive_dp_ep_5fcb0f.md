source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep)

Classes:

-
–[MoEPrepareAndFinalizeNaiveDPEPModular](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep.MoEPrepareAndFinalizeNaiveDPEPModular)Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.

-
–[MoEPrepareAndFinalizeNaiveDPEPMonolithic](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep.MoEPrepareAndFinalizeNaiveDPEPMonolithic)Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.


##

`MoEPrepareAndFinalizeNaiveDPEPModular`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep.MoEPrepareAndFinalizeNaiveDPEPModular)

Bases: [FusedMoEPrepareAndFinalizeModular](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeModular)

Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.

Uses Torch AR/RS or AR for dispatch/combine operations, applied to the topk weights and ids.

Methods:

-
–[prepare](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep.MoEPrepareAndFinalizeNaiveDPEPModular.prepare)Quantize and Dispatch Topk Weights and Topk Ids.


## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep.py`


|
|

###

`prepare(a1, topk_weights, topk_ids, num_experts, expert_map, apply_router_weight_on_input, quant_config, defer_input_quant=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep.MoEPrepareAndFinalizeNaiveDPEPModular.prepare)

Quantize and Dispatch Topk Weights and Topk Ids.

## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep.py`


##

`MoEPrepareAndFinalizeNaiveDPEPMonolithic`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep.MoEPrepareAndFinalizeNaiveDPEPMonolithic)

Bases: [FusedMoEPrepareAndFinalizeMonolithic](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.FusedMoEPrepareAndFinalizeMonolithic)

Naive Prepare/Finalize for Dp/Ep case for Modular Kernels.

Uses Torch AR/RS or AR for dispatch/combine operations, applied to the router logits (the MoE kernel runs the router internally).

Methods:

-
–[prepare](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep.MoEPrepareAndFinalizeNaiveDPEPMonolithic.prepare)Quantize and Dispatch Router Logits.


## Source code in `vllm/model_executor/layers/fused_moe/prepare_finalize/naive_dp_ep.py`


###

`prepare(a1, router_logits, quant_config, defer_input_quant=False)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.prepare_finalize.naive_dp_ep.MoEPrepareAndFinalizeNaiveDPEPMonolithic.prepare)

Quantize and Dispatch Router Logits.