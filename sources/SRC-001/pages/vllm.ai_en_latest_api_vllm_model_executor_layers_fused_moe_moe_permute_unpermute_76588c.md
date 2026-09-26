source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/moe_permute_unpermute/
lastmod: 2026-09-24

#

`vllm.model_executor.layers.fused_moe.moe_permute_unpermute`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute)

Functions:

-
–[get_moe_permute_scratch](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.get_moe_permute_scratch)Share scratch across sequential layers in the current ubatch and lane.

-
–[moe_permute](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute)This function expands and permutes activation to gather uncontinuous tokens

-
–[moe_prepare_scatter](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_prepare_scatter)Generate expert offsets and shared scatter/unpermute destination indices.

-
–[moe_unpermute](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_unpermute)This function expands and permutes activation to gathering uncontinuous


##

`get_moe_permute_scratch(*, max_num_tokens, topk, num_experts, num_local_experts, device, hidden_size=None, hidden_dtype=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.get_moe_permute_scratch)

Share scratch across sequential layers in the current ubatch and lane.

Without a workspace manager, allocate new scratch for each call.

## Source code in `vllm/model_executor/layers/fused_moe/moe_permute_unpermute.py`


##

`moe_permute(hidden_states, a1q_scale, topk_ids, n_expert, n_local_expert=-1, expert_map=None, permuted_hidden_states=None, scratch=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute)

This function expands and permutes activation to gather uncontinuous tokens for each expert.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input tensor to the MoE layer.

-

(`a1q_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute(a1q_scale))`Optional[`

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]quant scale for hidden_states

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)topk expert route id for each token.

-

(`n_expert`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute(n_expert))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The number of expert.

-

(`n_local_expert`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute(n_local_expert))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`-1`

) –The number of expert in current EP rank.

-

(`expert_map`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute(expert_map))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –A tensor mapping expert indices from the global expert space to the local expert space of the expert parallel shard.

-

(`permuted_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute(permuted_hidden_states))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –Optional output tensor. If None, the output tensor will be created in this function.

-

(`scratch`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_permute(scratch))`Optional[MoEPermuteScratch]`

, default:`None`

) –Optional preallocated scratch buffers. Validated against hidden_states and topk_ids when given, otherwise the buffers are allocated in this function.


Returns: - permuted_hidden_states (torch.Tensor): permuted activation. - a1q_scale (Optional[torch.Tensor]): permuted quant scale for hidden_states if original scale not per-tensor scaling - expert_first_token_offset (torch.Tensor): offset of the first token of each expert for standard grouped gemm. - inv_permuted_idx (torch.Tensor): idx map for moe_unpermute. - permuted_idx (torch.Tensor): idx map from hidden to permuted_hidden.

## Source code in `vllm/model_executor/layers/fused_moe/moe_permute_unpermute.py`


|
|

##

`moe_prepare_scatter(topk_ids, expert_map, scratch)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_prepare_scatter)

Generate expert offsets and shared scatter/unpermute destination indices.

## Source code in `vllm/model_executor/layers/fused_moe/moe_permute_unpermute.py`


##

`moe_unpermute(out, permuted_hidden_states, topk_weights, inv_permuted_idx, expert_first_token_offset=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_unpermute)

This function expands and permutes activation to gathering uncontinuous tokens for each expert.

Parameters:

-

(`out`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_unpermute(out))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)output tensor

-

(`permuted_hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_unpermute(permuted_hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)permuted activation.

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_unpermute(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)topk expert route weight for each token.

-

(`inv_permuted_idx`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_unpermute(inv_permuted_idx))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)row idx map for moe_unpermute.

-

(`expert_first_token_offset`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_permute_unpermute.moe_unpermute(expert_first_token_offset))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –offset of the first token of each expert for grouped gemm.


- hidden_states (torch.Tensor): The reduced and unpermuted activation tensor.