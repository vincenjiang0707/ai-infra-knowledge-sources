source: https://docs.vllm.ai/en/latest/api/vllm/distributed/eplb/policy/abstract/
lastmod: 2026-09-24

#

`vllm.distributed.eplb.policy.abstract`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract)

Classes:

##

`AbstractEplbPolicy`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[rebalance_experts](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy.rebalance_experts)Entry point for expert-parallelism load balancer.


## Source code in `vllm/distributed/eplb/policy/abstract.py`


###

`rebalance_experts(weight, num_replicas, num_groups, num_nodes, num_ranks, old_global_expert_indices=None)`

`abstractmethod`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy.rebalance_experts)

Entry point for expert-parallelism load balancer.

Parameters:

-

(`weight`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy.rebalance_experts(weight))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[layers, num_logical_experts], the load statistics for all logical experts

-

(`num_replicas`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy.rebalance_experts(num_replicas))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of physical experts, must be a multiple of

`num_ranks`

-

(`num_groups`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy.rebalance_experts(num_groups))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of expert groups

-

(`num_nodes`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy.rebalance_experts(num_nodes))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of server nodes

-

(`num_ranks`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy.rebalance_experts(num_ranks))

) –[int](https://docs.python.org/3/builtins/functions.html#int)number of ranks, must be a multiple of

`num_nodes`

-

(`old_global_expert_indices`

[¶](https://docs.vllm.ai#vllm.distributed.eplb.policy.abstract.AbstractEplbPolicy.rebalance_experts(old_global_expert_indices))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –[layers, num_logical_experts], the old global expert indices. Used to avoid unnecessary weight copying for experts moving within one rank.


Returns:

-
(`physical_to_logical_map`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[layers, num_replicas], the expert index of each replica