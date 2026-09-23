source: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/policy/
lastmod: 2026-09-23

#

`vllm.distributed.eplb.policy`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy)

Modules:

Classes:

##

`AbstractEplbPolicy`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[rebalance_experts](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy.rebalance_experts)Entry point for expert-parallelism load balancer.


## Source code in `vllm/distributed/eplb/policy/abstract.py`


###

`rebalance_experts(weight, num_replicas, num_groups, num_nodes, num_ranks, old_global_expert_indices=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy.rebalance_experts)

Entry point for expert-parallelism load balancer.

Parameters:

-

(`weight`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy.rebalance_experts(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[layers, num_logical_experts], the load statistics for all logical experts

-

(`num_replicas`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy.rebalance_experts(num_replicas))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of physical experts, must be a multiple of

`num_ranks`

-

(`num_groups`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy.rebalance_experts(num_groups))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of expert groups

-

(`num_nodes`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy.rebalance_experts(num_nodes))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of server nodes

-

(`num_ranks`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy.rebalance_experts(num_ranks))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of ranks, must be a multiple of

`num_nodes`

-

(`old_global_expert_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.AbstractEplbPolicy.rebalance_experts(old_global_expert_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –[layers, num_logical_experts], the old global expert indices. Used to avoid unnecessary weight copying for experts moving within one rank.


Returns:

-
(`physical_to_logical_map`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[layers, num_replicas], the expert index of each replica


## Source code in `vllm/distributed/eplb/policy/abstract.py`


##

`DefaultEplbPolicy`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy)

Bases: [AbstractEplbPolicy](https://docs.vllm.ai/abstract/#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy)

Methods:

-
–[balanced_packing](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.balanced_packing)Pack n weighted objects to m packs, such that each bin contains exactly

-
–[preserve_intragpu_slots](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.preserve_intragpu_slots)Reorder the new mapping per GPU so that experts that remain on the same GPU

-
–[rebalance_experts](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts)Entry point for expert-parallelism load balancer.

-
–[rebalance_experts_hierarchical](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts_hierarchical)Parameters

-
–[replicate_experts](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.replicate_experts)Replicate

`num_log`

experts to`num_phy`

replicas, such that the maximum

## Source code in `vllm/distributed/eplb/policy/default.py`


|
|

###

`balanced_packing(weight, num_packs)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.balanced_packing)

Pack n weighted objects to m packs, such that each bin contains exactly n/m objects and the weights of all packs are as balanced as possible.

Parameters:

Returns:

-
(`pack_index`


) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)[X, n], the pack index of each item

-
(`rank_in_pack`


) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)[X, n], the rank of the item in the pack


## Source code in `vllm/distributed/eplb/policy/default.py`


###

`preserve_intragpu_slots(phy2log, num_ranks, old_phy2log)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.preserve_intragpu_slots)

Reorder the new mapping per GPU so that experts that remain on the same GPU keep their previous slot positions when possible. Incoming experts to that GPU fill any remaining available slots. This is applied only when the number of GPUs is unchanged and the slots per GPU remain the same between the old and new mappings.

## Source code in `vllm/distributed/eplb/policy/default.py`


|
|

###

`rebalance_experts(weight, num_replicas, num_groups, num_nodes, num_ranks, old_global_expert_indices=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts)

Entry point for expert-parallelism load balancer.

Parameters:

-

(`weight`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[layers, num_logical_experts], the load statistics for all logical experts

-

(`num_replicas`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts(num_replicas))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of physical experts, must be a multiple of

`num_gpus`

-

(`num_groups`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts(num_groups))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of expert groups

-

(`num_nodes`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts(num_nodes))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of server nodes, where the intra-node network (e.g, NVLink) is faster

-

(`num_ranks`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts(num_ranks))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of ranks, must be a multiple of

`num_nodes`

-

(`old_global_expert_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts(old_global_expert_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –[layers, num_logical_experts], the old global expert indices. Used to avoid unnecessary weight copying for experts moving within one rank.


```
phy2log: [layers, num_replicas], the expert
index of each replica
```


## Source code in `vllm/distributed/eplb/policy/default.py`


###

`rebalance_experts_hierarchical(weight, num_physical_experts, num_groups, num_nodes, num_gpus)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.rebalance_experts_hierarchical)

Parameters weight: [num_moe_layers, num_logical_experts] num_physical_experts: number of physical experts after replication num_groups: number of expert groups num_nodes: number of server nodes, where the intra-node network (e.g, NVLink) is faster num_gpus: number of GPUs, must be a multiple of `num_nodes`


Returns:

-
(`phy2log`


) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)[layers, num_replicas], the expert index of each replica


## Source code in `vllm/distributed/eplb/policy/default.py`


|
|

###

`replicate_experts(weight, num_phy)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.DefaultEplbPolicy.replicate_experts)

Replicate `num_log`

experts to `num_phy`

replicas, such that the maximum load of all replicas is minimized.

Parameters:

Returns:

-
(`phy2log`


) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)[X, num_phy], logical expert id of each physical expert

-
(`logcnt`


) –[ndarray](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray)[X, num_log], number of replicas for each logical expert