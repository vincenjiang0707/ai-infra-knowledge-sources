source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/runner/shared_experts/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.runner.shared_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.runner.shared_experts)

Classes:

##

`SharedExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Methods:

-
–[maybe_forward_async](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts.maybe_forward_async)Enqueue shared experts on the aux stream without waiting for them.

-
–[wait](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts.wait)Block the main stream until

`maybe_forward_async`

output is ready.

## Source code in `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`


|
|

###

`maybe_forward_async(shared_experts_input)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts.maybe_forward_async)

Enqueue shared experts on the aux stream without waiting for them.

Returns true if the shared experts were enqueued, false otherwise. Call `wait`

to wait for the shared experts to finish if this returns true.

## Source code in `vllm/model_executor/layers/fused_moe/runner/shared_experts.py`


###

`wait()`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.runner.shared_experts.SharedExperts.wait)

Block the main stream until `maybe_forward_async`

output is ready.