source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/experts/marlin_moe/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.experts.marlin_moe`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe)

Fused MoE utilities for GPTQ.

Classes:

-
–[BatchedMarlinExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.BatchedMarlinExperts)Batched Marlin-based fused MoE expert implementation.

-
–[MarlinExperts](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.MarlinExperts)Marlin-based fused MoE expert implementation.


Functions:

-
–[batched_fused_marlin_moe](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.batched_fused_marlin_moe)This function massages the inputs so the batched hidden_states can be

-
–[fused_marlin_moe](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe)This function computes a Mixture of Experts (MoE) layer using two sets of


##

`BatchedMarlinExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.BatchedMarlinExperts)

Bases: `MarlinExpertsBase`


Batched Marlin-based fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`


|
|

##

`MarlinExperts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.MarlinExperts)

Bases:

, [LoRAExpertsMixin](https://docs.vllm.ai/lora_experts_mixin/#vllm.model_executor.layers.fused_moe.experts.lora_experts_mixin.LoRAExpertsMixin)`MarlinExpertsBase`


Marlin-based fused MoE expert implementation.

## Source code in `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`


|
|

##

`batched_fused_marlin_moe(hidden_states, expert_num_tokens, w1, w2, bias1, bias2, w1_scale, w2_scale, quant_type_id, apply_router_weight_on_input=False, global_num_experts=-1, activation=MoEActivation.SILU, expert_map=None, input_global_scale1=None, input_global_scale2=None, global_scale1=None, global_scale2=None, w1_zeros=None, w2_zeros=None, workspace=None, intermediate_cache13=None, intermediate_cache2=None, output=None, input_dtype=None, activation_func=None, activation_config=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.batched_fused_marlin_moe)

This function massages the inputs so the batched hidden_states can be presented as a 2D contiguous tensor that could be used with _fused_marlin_moe.

Note that both batched_fused_marlin_moe and fused_marlin_moe ultimately use `ops.moe_wna16_marlin_gemm`

for the gemm operation and `ops.moe_mna16_marlin_gemm`

supports only 2D contiguous hidden_states. Note that the moe_align_block_size function indicates, - What rows of the A matrix (hidden_states) to access during the matmul, via sorted_ids output. - What expert_id to use for each block matmul, via expert_ids output.

In the batched version, the tokens are already grouped/batched by experts they subscribe to. Due to this, we can represent the batched hidden_states tensor of shape [B, MAX_TOKENS_PER_BATCH, K] as a 2D tensor of shape, [B * MAX_TOKENS_PER_BATCH, K]. We may treat this a 2D contiguous tensor with topk=1 as each token (row in the tensor) subscribes to exactly one expert_id (which is the batch_id). With the expert_num_tokens tensor, that indicates how many tokens are actually valid in each batch, the batched_moe_align_block_size function constructs the sorted_ids and expert_ids tensors, so only relevant/valid rows of A (hidden_states) are accessed and are processed with the correct expert_ids.

## Source code in `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`


|
|

##

`fused_marlin_moe(hidden_states, w1, w2, bias1, bias2, w1_scale, w2_scale, topk_weights, topk_ids, quant_type_id, apply_router_weight_on_input=False, global_num_experts=-1, activation=MoEActivation.SILU, activation_func=None, moe_sum=None, expert_map=None, input_global_scale1=None, input_global_scale2=None, global_scale1=None, global_scale2=None, w1_zeros=None, w2_zeros=None, workspace=None, intermediate_cache13=None, intermediate_cache2=None, output=None, input_dtype=None, activation_config=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe)

This function computes a Mixture of Experts (MoE) layer using two sets of weights, w1 and w2, and top-k gating mechanism.

Parameters:

-

(`hidden_states`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(hidden_states))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The input tensor to the MoE layer.

-

(`w1`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(w1))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The first set of expert weights.

-

(`w2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(w2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The second set of expert weights.

-

(`bias1`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(bias1))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneOptional bias for the first GEMM.

-

(`bias2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(bias2))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| NoneOptional bias for the second GEMM.

-

(`w1_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(w1_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Scale to be used for w1.

-

(`w2_scale`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(w2_scale))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Scale to be used for w2.

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Top-k weights.

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(topk_ids))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Indices of topk-k elements.

-

(`quant_type_id`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(quant_type_id))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Id of the

`ScalarType`

the expert weights are quantized to. Determines the 4- or 8-bit Marlin kernel path. -

(`apply_router_weight_on_input`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(apply_router_weight_on_input))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –Apply the topk weights to the input rather than the output. Only valid when topk is 1.

-

(`global_num_experts`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(global_num_experts))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`-1`

) –Total number of experts across all expert parallel shards. -1 means the local expert count.

-

(`activation`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(activation))

, default:[MoEActivation](https://docs.vllm.ai/activation/#vllm.model_executor.layers.fused_moe.activation.MoEActivation)`SILU`

) –Activation applied between the two GEMMs.

-

(`activation_func`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(activation_func))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None`None`

) –Override for the activation implementation.

-

(`moe_sum`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(moe_sum))

, default:[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)| None`None`

) –Override for the final reduction over the topk dimension. Defaults to

`ops.moe_sum`

/`torch.sum`

. -

(`expert_map`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(expert_map))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Maps global expert indices to the local expert space of this expert parallel shard.

-

(`input_global_scale1`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(input_global_scale1))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –NVFP4 global input scale for the first GEMM.

-

(`input_global_scale2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(input_global_scale2))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –NVFP4 global input scale for the second GEMM.

-

(`global_scale1`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(global_scale1))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –NVFP4 global weight scale for w1.

-

(`global_scale2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(global_scale2))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –NVFP4 global weight scale for w2.

-

(`w1_zeros`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(w1_zeros))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional zero points to be used for w1.

-

(`w2_zeros`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(w2_zeros))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional zero points to be used for w2.

-

(`workspace`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(workspace))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Scratch buffer for the Marlin kernels.

-

(`intermediate_cache13`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(intermediate_cache13))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Scratch buffer for the first and third intermediate activations.

-

(`intermediate_cache2`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(intermediate_cache2))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Scratch buffer for the second intermediate activation.

-

(`output`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(output))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Tensor to write the result into. A new tensor is allocated when omitted.

-

(`input_dtype`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(input_dtype))

, default:[dtype](https://pytorch.org/docs/stable/tensor_attributes.html#torch.dtype)| None`None`

) –dtype the activations are quantized to. A 1-byte dtype raises the M block size to at least 16.

-

(`activation_config`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.experts.marlin_moe.fused_marlin_moe(activation_config))

, default:[ApplyMoEActivationConfig](https://docs.vllm.ai/activation/#vllm.model_executor.layers.fused_moe.activation.ApplyMoEActivationConfig)| None`None`

) –Extra configuration forwarded to the activation.


Returns:

-

–[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)torch.Tensor: The output tensor after applying the MoE layer.


## Source code in `vllm/model_executor/layers/fused_moe/experts/marlin_moe.py`


|
|