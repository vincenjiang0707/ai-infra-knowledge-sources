source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/model_loader/ep_weight_filter/
lastmod: 2026-09-23

#

`vllm.model_executor.model_loader.ep_weight_filter`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter)

Filter out non-local expert weights during loading to avoid redundant I/O.

In DP+EP deployments each rank only needs its own expert shard. Skipping non-local expert tensors *before* they are read from disk eliminates the majority of storage I/O for MoE models (experts typically account for ~85-90 % of total weight bytes).

Functions:

-
–[compute_local_expert_ids](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.compute_local_expert_ids)Compute the set of global expert ids owned by

*ep_rank*. -
–[parse_expert_id](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.parse_expert_id)Return the expert id embedded in

*weight_name*, or`None`

if it is -
–[should_skip_weight](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.should_skip_weight)Return

`True`

if*weight_name*is an expert weight that does not

##

`compute_local_expert_ids(num_experts, ep_size, ep_rank, placement='linear')`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.compute_local_expert_ids)

Compute the set of global expert ids owned by *ep_rank*.

Returns `None`

when EP is not active (`ep_size <= 1`

), meaning all experts are local and no filtering should be performed.

The distribution logic mirrors :func:`vllm.model_executor.layers.fused_moe.layer.determine_expert_map`

.

Parameters:

-

(`num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.compute_local_expert_ids(num_experts))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of experts in the layer.

-

(`ep_size`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.compute_local_expert_ids(ep_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Expert parallel world size.

-

(`ep_rank`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.compute_local_expert_ids(ep_rank))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Rank whose local expert ids are computed.

-

(`placement`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.compute_local_expert_ids(placement))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'linear'`

) –`"linear"`

for contiguous assignment,`"round_robin"`

for interleaved assignment.

## Source code in `vllm/model_executor/model_loader/ep_weight_filter.py`


##

`parse_expert_id(weight_name)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.parse_expert_id)

Return the expert id embedded in *weight_name*, or `None`

if it is not an per-expert weight.

Returns `None`

for dense weights (attention, layernorm, embedding), shared experts, and 3D fused-expert tensors where all experts are stored in a single tensor without a numeric expert id in the name.

## Source code in `vllm/model_executor/model_loader/ep_weight_filter.py`


##

`should_skip_weight(weight_name, local_expert_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.model_loader.ep_weight_filter.should_skip_weight)

Return `True`

if *weight_name* is an expert weight that does not belong to the local rank and should be skipped during loading.