source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/routed_experts_capturer/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.routed_experts_capturer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer)

Classes:

-
–[RoutedExpertsCapturer](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.RoutedExpertsCapturer)Worker-side capturer for routed experts, lives on GPU.


Functions:

-
–[bind_routed_experts_capturer](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.bind_routed_experts_capturer)Attach capture callbacks to the target model's MoE routers.


##

`RoutedExpertsCapturer`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.RoutedExpertsCapturer)

Worker-side capturer for routed experts, lives on GPU.

Layer-level hooks call :meth:`capture`

inside the forward pass. Routing rows owned by this DP rank are written into a preallocated device buffer.

The device buffer uses `int32`

. Stable snapshots use the narrowest dtype that can represent every logical expert ID.

## Invariants

- One instance per worker; shape is fixed at init and covers the worst-case step (
`max_num_batched_tokens`

tokens). - Every routed layer overwrites the current step's token rows.

Methods:

-
–[capture](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.RoutedExpertsCapturer.capture)Capture expert routing decisions for a specific layer.

-
–[snapshot_routing_data](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.RoutedExpertsCapturer.snapshot_routing_data)Return a stable snapshot of the current routing data.


## Source code in `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`


|
|

###

`capture(layer_id, topk_ids)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.RoutedExpertsCapturer.capture)

Capture expert routing decisions for a specific layer.

Under data parallelism, `topk_ids`

may have four different batch layouts depending on where the DP combine happens and whether Expert Parallelism (EP) or Sequence Parallelism (SP) is active for the MoE layer: - `n == total`

(naive dispatch): all DP ranks' tokens are concatenated before routing; we slice out this rank's span using the cumulative per-rank counts. - `n == token_num_per_dp`

(modular-kernel path): DP combine happens inside `quant_method.apply`

; `select_experts`

only ever sees this rank's tokens, so we take the whole tensor. - `n == sum(dp_metadata.local_sizes)`

(naive DP+EP dispatch): sequence-parallel shards from every DP rank are gathered through the flattened EP group. The shard sizes include CUDA-graph / SP padding, so we use them to locate this DP rank's unpadded rows. - `n == ceil(token_num_per_dp / tp_size)`

(SP + modular-kernel path): tokens were split along dim=0 across the TP group by `_sequence_parallel_context`

(`moe_runner_base.py:_sequence_parallel_context`

), so each TP rank only sees its shard. We all-gather along dim=0 to reconstruct this DP rank's full routing tensor. SP pads with ceil-div (see `_compute_sp_num_tokens`

in `forward_context.py`

), so the gathered tensor may contain a few trailing padding rows which are trimmed by the downstream `[:token_num_per_dp]`

slice.

Parameters:

-

(`layer_id`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.RoutedExpertsCapturer.capture(layer_id))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The layer index.

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.RoutedExpertsCapturer.capture(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Tensor of shape (batch_size, num_routed_experts).


## Source code in `vllm/model_executor/layers/fused_moe/routed_experts_capturer.py`


|
|

###

`snapshot_routing_data(num_tokens)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.RoutedExpertsCapturer.snapshot_routing_data)

Return a stable snapshot of the current routing data.

##

`bind_routed_experts_capturer(model, capturer)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.routed_experts_capturer.bind_routed_experts_capturer)

Attach capture callbacks to the target model's MoE routers.