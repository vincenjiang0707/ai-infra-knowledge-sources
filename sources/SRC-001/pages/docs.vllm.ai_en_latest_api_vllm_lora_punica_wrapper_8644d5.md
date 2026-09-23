source: https://docs.vllm.ai/en/latest/api/vllm/lora/punica_wrapper/
lastmod: 2026-09-23

#

`vllm.lora.punica_wrapper`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper)

Modules:

-
–[punica_base](https://docs.vllm.ai/punica_base/#vllm.lora.punica_wrapper.punica_base)Based on:

-
–[punica_cpu](https://docs.vllm.ai/punica_cpu/#vllm.lora.punica_wrapper.punica_cpu) -
–[punica_gpu](https://docs.vllm.ai/punica_gpu/#vllm.lora.punica_wrapper.punica_gpu)Based on:

-
–[punica_xpu](https://docs.vllm.ai/punica_xpu/#vllm.lora.punica_wrapper.punica_xpu)Based on:

-
–[utils](https://docs.vllm.ai/utils/#vllm.lora.punica_wrapper.utils)

Classes:

-
–[PunicaWrapperBase](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase)PunicaWrapperBase is designed to manage and provide metadata for the punica


##

`PunicaWrapperBase`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase)

Bases: [PunicaWrapperABC](https://docs.vllm.ai/punica_base/#vllm.lora.punica_wrapper.punica_base.PunicaWrapperABC)

PunicaWrapperBase is designed to manage and provide metadata for the punica kernel. The main function is to maintain the state information for Multi-LoRA, and to provide the interface for the punica.

Methods:

-
–[add_expand](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_expand)Performs GEMM for multiple slices of lora_b.

-
–[add_lora_embedding](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_embedding)Applies lora specifically for VocabParallelEmbeddingWithLoRA.

-
–[add_lora_fused_moe](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_fused_moe)Performs a fused forward computation for LoRA of

-
–[add_lora_linear](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear)Applicable to linear-related lora.

-
–[add_lora_logits](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_logits)Applies lora specifically for LogitsProcessorWithLoRA.

-
–[add_lora_w13](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_w13)Apply w13 LoRA to y (intermediate_cache1) in-place before activation.

-
–[add_lora_w2](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_w2)Apply w2 LoRA to y (intermediate_cache3) in-place before moe_sum.

-
–[add_shrink](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_shrink)Performs GEMM for multiple slices of lora_a.

-
–[moe_lora_align_block_size](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.moe_lora_align_block_size)Aligns tokens and experts into block-sized chunks for LoRA-based


Attributes:

-
([prefill_metadata](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.prefill_metadata)

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int),[int](https://docs.python.org/3/builtins/functions.html#int)]This property provides a convenient way to access the necessary

-
([sampler_indices](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.sampler_indices)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)This property is used to access the lora indices specifically for

-
([sampler_indices_padded](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.sampler_indices_padded)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)This property provides access to padded sampler indices.

-
([token_lora_indices](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.token_lora_indices)

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)This property provides the lora indices corresponding to each token


## Source code in `vllm/lora/punica_wrapper/punica_base.py`


|
|

###

`prefill_metadata`

`property`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.prefill_metadata)

This property provides a convenient way to access the necessary metadata for prefill-related kernel computations. 1. seq_start_locs: Tensor of sequence start positions. 2. seq_lengths: Tensor of sequence lengths. 3. lora_indices_per_batch: Tensor of lora indices, and an index of -1 means no lora should be applied. 4. batch_size: Batch size after clustering identical lora indices. 5. max_length: The maximum sequence length in the batch. 6. token_nums: The token numbers in the batch.

###

`sampler_indices`

`property`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.sampler_indices)

This property is used to access the lora indices specifically for LogitsProcessorWithLoRA.

###

`sampler_indices_padded`

`property`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.sampler_indices_padded)

This property provides access to padded sampler indices.

###

`token_lora_indices`

`property`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.token_lora_indices)

This property provides the lora indices corresponding to each token in the batch. An index of -1 means no lora should be applied.

###

`add_expand(y, x, lora_b_stacked, output_slices, offset_start=0, add_inputs=True, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_expand)

Performs GEMM for multiple slices of lora_b.

## Semantics

offset = offset_start for i in range(len(lora_b_stacked)): slice = output_slices[i] y[:, offset:offset+slice] += x[i] @ lora_b_stacked[i] offset += slice

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_expand(y))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor.

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_expand(x))`Union[`

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Input tensors

-

(`lora_b_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_expand(lora_b_stacked))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]lora_b's weight

-

(`output_slices`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_expand(output_slices))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Every slice's size

-

(`offset_start`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_expand(offset_start))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –The starting position of y, defaults to 0

-

(`add_inputs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_expand(add_inputs))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Defaults to True.


## Source code in `vllm/lora/punica_wrapper/punica_base.py`


###

`add_lora_embedding(y, x, lora_b_stacked, add_inputs=True, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_embedding)

Applies lora specifically for VocabParallelEmbeddingWithLoRA. and this layer only requires the expand operation. Semantics: y += x @ lora_b_stacked

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_embedding(y))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor.

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_embedding(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor.

-

(`lora_b_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_embedding(lora_b_stacked))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)lora_b's weights.

-

(`add_inputs`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_embedding(add_inputs))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –Default to True.


## Source code in `vllm/lora/punica_wrapper/punica_base.py`


###

`add_lora_fused_moe(y, x, lora_a_stacked, lora_b_stacked, topk_weights, sorted_token_ids, expert_ids, num_tokens_post_padded, max_lora_rank, top_k_num, shrink_config, expand_config, adapter_enabled, mul_routed_weight=False, fully_sharded=False, offset=0, token_lora_mapping=None)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_fused_moe)

Performs a fused forward computation for LoRA of Mixture-of-Experts (MoE) layer.

## Source code in `vllm/lora/punica_wrapper/punica_base.py`


###

`add_lora_linear(y, x, lora_a_stacked, lora_b_stacked, scale, output_slices, *, buffer=None, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear)

Applicable to linear-related lora.

## Semantics

for i in range(len(lora_a_stacked)): y[i] += ( x[i].unsqueeze(0) @ lora_a_stacked[indices[i], layer_idx, :, :] @ lora_b_stacked[indices[i], layer_idx, :, :] * scale ).squeeze(0)

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear(y))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor. Will be changed in-place.

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`lora_a_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear(lora_a_stacked))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]lora_a's weight.

-

(`lora_b_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear(lora_b_stacked))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]lora_b's weight.

-

(`scale`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear(scale))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Scaling factor.

-

(`output_slices`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear(output_slices))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int), ...]Every slice's size.

-

(`buffer`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_linear(buffer))`Optional[`

, default:[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]]`None`

) –Defaults to None.


## Source code in `vllm/lora/punica_wrapper/punica_base.py`


###

`add_lora_logits(y, x, lora_a_stacked, lora_b_stacked, scale, *, buffer=None, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_logits)

Applies lora specifically for LogitsProcessorWithLoRA.

## Semantics

buffer = (x @ lora_a_stacked) * scale y += buffer @ lora_b_stacked

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_logits(y))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Output tensor.

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_logits(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor.

-

(`lora_a_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_logits(lora_a_stacked))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)lora_a's weights.

-

(`lora_b_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_logits(lora_b_stacked))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)lora_b's weights.

-

(`scale`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_logits(scale))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Scaling factor.

-

(`buffer`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_logits(buffer))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –Default to None.


## Source code in `vllm/lora/punica_wrapper/punica_base.py`


###

`add_lora_w13(y, x, lora_a_stacked, lora_b_stacked, topk_ids, topk_weights, expert_map, w1, w2, num_tokens, top_k_num, max_loras, adapter_enabled, local_num_experts, top_k, num_slices, fully_sharded, use_tuned_config, add_inputs=True, token_lora_mapping=None)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_w13)

Apply w13 LoRA to y (intermediate_cache1) in-place before activation.

When `token_lora_mapping`

is provided it overrides the punica_wrapper's global mapping — used by EP+LoRA to pass the per-rank-local mapping after all-to-all dispatch.

Returns (sorted_token_ids_lora, expert_ids_lora, num_tokens_post_padded_lora, token_lora_mapping) for reuse by add_lora_w2.

## Source code in `vllm/lora/punica_wrapper/punica_base.py`


###

`add_lora_w2(y, x, lora_a_stacked, lora_b_stacked, topk_weights, sorted_token_ids_lora, expert_ids_lora, num_tokens_post_padded_lora, token_lora_mapping, num_tokens, w1, w2, top_k_num, max_loras, adapter_enabled, top_k, fully_sharded, tp_rank, use_tuned_config, add_inputs=True)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_lora_w2)

Apply w2 LoRA to y (intermediate_cache3) in-place before moe_sum.

Reuses routing tensors returned by add_lora_w13.

## Source code in `vllm/lora/punica_wrapper/punica_base.py`


###

`add_shrink(y, x, lora_a_stacked, scale, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_shrink)

Performs GEMM for multiple slices of lora_a.

Semantics: for i in range(len(lora_a_stacked)): y[i] += (x @ lora_a_stacked[i]) * scale

Parameters:

-

(`y`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_shrink(y))`Union[`

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...],[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]Output tensors

-

(`x`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_shrink(x))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Input tensor

-

(`lora_a_stacked`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_shrink(lora_a_stacked))

) –[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor), ...]lora_a's weights

-

(`scale`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.add_shrink(scale))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Scaling factor for the operation


## Source code in `vllm/lora/punica_wrapper/punica_base.py`


###

`moe_lora_align_block_size(topk_ids, num_tokens, block_size, num_experts, max_loras, adapter_enabled, expert_map=None, pad_sorted_ids=False, naive_block_assignment=False)`

[¶](https://docs.vllm.ai#vllm.lora.punica_wrapper.PunicaWrapperBase.moe_lora_align_block_size)

Aligns tokens and experts into block-sized chunks for LoRA-based mixture-of-experts (MoE) execution.