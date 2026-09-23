source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/topk_weight_and_reduce/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.topk_weight_and_reduce`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce)

Classes:

-
–[TopKWeightAndReduceContiguous](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceContiguous)TopKWeightAndReduce implementation for a fused_experts output

-
–[TopKWeightAndReduceDelegate](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceDelegate)Useful in the case when some FusedMoEExpertsModular

-
–[TopKWeightAndReduceNaiveBatched](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceNaiveBatched)TopKWeightAndReduce implementation for a fused_experts output

-
–[TopKWeightAndReduceNoOP](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceNoOP)The fused_experts outputs have already been weight applied and reduced.


##

`TopKWeightAndReduceContiguous`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceContiguous)

Bases: [TopKWeightAndReduce](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.TopKWeightAndReduce)

TopKWeightAndReduce implementation for a fused_experts output of shape (m, topk, K)

## Source code in `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`


##

`TopKWeightAndReduceDelegate`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceDelegate)

Bases: [TopKWeightAndReduce](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.TopKWeightAndReduce)

Useful in the case when some FusedMoEExpertsModular implementation does not perform weight application and reduction but cannot address the needs of all the compatible PrepareAndFinalize implementations. For example, BatchedTritonExperts is compatible with both batched PrepareAndFinalize implementations like DeepEPLLPrepareAndFinalize and BatchedPrepareAndFinalize. Some PrepareAndFinalize implementations do the weight-application + reduction as part of the combine kernel, while BatchedPrepareAndFinalize needs an explicit implementation. To facilitate this case, the BatchedTritonExperts could use TopKWeightAndReduceDelegate so the PrepareAndFinalize implementations could choose how to weight + reduce.

## Source code in `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`


##

`TopKWeightAndReduceNaiveBatched`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceNaiveBatched)

Bases: [TopKWeightAndReduce](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.TopKWeightAndReduce)

TopKWeightAndReduce implementation for a fused_experts output of shape (num_experts, batch_size, K)

## Source code in `vllm/model_executor/layers/fused_moe/topk_weight_and_reduce.py`


##

`TopKWeightAndReduceNoOP`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.topk_weight_and_reduce.TopKWeightAndReduceNoOP)

Bases: [TopKWeightAndReduce](https://docs.vllm.ai/modular_kernel/#vllm.model_executor.layers.fused_moe.modular_kernel.TopKWeightAndReduce)

The fused_experts outputs have already been weight applied and reduced. This implementation is a no-op.