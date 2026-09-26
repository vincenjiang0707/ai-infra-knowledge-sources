source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/transformers/fusers/moe/
lastmod: 2026-09-24

#

`vllm.model_executor.models.transformers.fusers.moe`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe)

MoE fuser: route an HF MoE block through `FusedMoE`

with vLLM's own routing.

Classes:

-
–[MoEBlockFuser](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser)Fuser for MoE block

`experts`

,`gate`

and`shared_experts`

(optional). -
–[SharedExpertMLP](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.SharedExpertMLP)Wraps an HF shared expert, applying the output gating it is paired with.


##

`MoEBlockFuser`

`dataclass`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser)

Fuser for MoE block `experts`

, `gate`

and `shared_experts`

(optional).

Methods:

-
–[gate](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser.gate)Rebuild the HF gate as a

`GateLinear`

for vLLM's fused MoE. -
–[rewrite_forward](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser.rewrite_forward)Rewrite

`moe_block.forward`

to route through vLLM's fused MoE. -
–[shared_experts](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser.shared_experts)Build the HF shared expert (and its optional gate)


## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


|
|

###

`_match_router(gate)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser._match_router)

Matches `topk(score(linear(x)))`

, `score`

being `softmax`

/`sigmoid`

.

Returns the scoring function and the dtype the router computes in.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


###

`_match_shared_experts(graph, experts)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser._match_shared_experts)

Detects the shared expert and its optional gate by dataflow.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


###

`gate(moe_block, prefix, out_dtype=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser.gate)

Rebuild the HF gate as a `GateLinear`

for vLLM's fused MoE.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


###

`rewrite_forward(moe_block)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser.rewrite_forward)

Rewrite `moe_block.forward`

to route through vLLM's fused MoE.

###

`shared_experts(moe_block, prefix)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.MoEBlockFuser.shared_experts)

Build the HF shared expert (and its optional gate) as a `SharedExpertMLP`

for vLLM's fused MoE.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


##

`SharedExpertMLP`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe.SharedExpertMLP)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Wraps an HF shared expert, applying the output gating it is paired with.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


##

`_forced_dtype(nodes)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe._forced_dtype)

The floating dtype `nodes`

cast to, if any.

Computations that must run in higher precision say so in their forward (e.g. `hidden_states.type(torch.float32)`

), so the dtype is readable from the graph even when the config does not name it.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


##

`_is_scalar_gate(module)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe._is_scalar_gate)

A linear projecting to a single logit (the shared-expert sigmoid gate).

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


##

`_moe_block_forward(self, hidden_states)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe._moe_block_forward)

Standard MoE block forward.

Routing and any shared experts are handled inside `self.experts: MoERunner`

.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


##

`_own_returns(node)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe._own_returns)

`return`

statements in `node`

's own scope, not in nested functions.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


##

`_reaches(node, key)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe._reaches)

Returns the set of nodes reachable from `node`

by following `key`

edges.

## Source code in `vllm/model_executor/models/transformers/fusers/moe.py`


##

`_returns_tuple(cls)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.transformers.fusers.moe._returns_tuple)

Does `cls.forward()`

return a tuple?