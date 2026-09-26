source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/router/cpu_router/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.router.cpu_router`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.cpu_router)

Router for CPU MoE experts.

This is the routing logic that used to live inline in each CPU FusedMoEExpertsMonolithic.apply() (see git history of experts/cpu_moe.py); factoring it out into a proper FusedMoERouter is what lets CPU MoE experts be FusedMoEExpertsModular like every other backend. The math below is unchanged from that prior inline version -- this is a relocation, not a rewrite.

Classes:

-
–[CPURouter](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.cpu_router.CPURouter)Router covering every routing scheme CPU MoE experts support: plain


Functions:

-
–[select_experts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.cpu_router.select_experts)Routing helper for the CPU MoE experts that still use the monolithic


##

`CPURouter`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.cpu_router.CPURouter)

Bases: [BaseRouter](https://docs.vllm.ai/base_router/#vllm.model_executor.layers.fused_moe.router.base_router.BaseRouter)

Router covering every routing scheme CPU MoE experts support: plain softmax top-k, grouped top-k (with an optional correction bias), an arbitrary custom_routing_function, and DeepSeek V4's sqrtsoftplus scheme (bias-corrected or hash-routed via the ported biased_topk_cpu/ hash_topk_cpu kernels). All of the above except sqrtsoftplus are plain torch ops so Dynamo traces straight through into them like it did when this logic lived inline in FusedMoEExpertsMonolithic.apply() -- no new compile boundary is introduced here.

## Source code in `vllm/model_executor/layers/fused_moe/router/cpu_router.py`


|
|

##

`_sqrtsoftplus_bias_topk(router_logits, top_k, renormalize, e_score_correction_bias, routed_scaling_factor, input_ids, hash_indices_table)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.cpu_router._sqrtsoftplus_bias_topk)

DeepSeek V4's routing: weight = sqrt(softplus(logit)); expert selection uses a bias-corrected score (weight + correction_bias), but the returned weight for each selected expert is the *unbiased* value (the "noaux_tc" pattern -- bias steers selection only). Always renormalizes selected weights to sum to `routed_scaling_factor`

, matching the reference Triton kernel (vllm/model_executor/layers/fused_moe/router/dsv4_topk.py).

When `hash_indices_table`

is given (hash-routed layers), expert selection instead comes from `hash_indices_table[input_ids]`

-- the bias-corrected-score topk is skipped entirely, matching the CUDA reference kernel (`dsv4HashTopkSoftplusSqrt`

).

Backed by the ported SGLang AVX512 kernels `biased_topk_cpu`

(the correction-bias path) and `hash_topk_cpu`

(the hash-routed-layer path); see csrc/cpu/sgl-kernels/topk.cpp.

## Source code in `vllm/model_executor/layers/fused_moe/router/cpu_router.py`


##

`select_experts(hidden_states, router_logits, top_k, use_grouped_topk, renormalize, topk_group=None, num_expert_group=None, custom_routing_function=None, scoring_func='softmax', routed_scaling_factor=1.0, e_score_correction_bias=None, input_ids=None, hash_indices_table=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.router.cpu_router.select_experts)

Routing helper for the CPU MoE experts that still use the monolithic contract and so must compute routing themselves from `router_logits`

(the zentorch-accelerated path and the ARM W4A8 dynamic-quant kernel, kept monolithic since zentorch/Arm hardware isn't available to validate a modular migration here). Modular CPU experts get routing from `CPURouter`

instead; this is a thin wrapper around the same logic for the two classes that can't use it.