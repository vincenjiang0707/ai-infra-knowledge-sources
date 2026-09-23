source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/moe_fused_mul_sum/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.moe_fused_mul_sum`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum)

Functions:

-
–[moe_fused_mul_sum](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum.moe_fused_mul_sum)Fused kernel for MoE (Mixture of Experts) to perform weighted summation


##

`moe_fused_mul_sum(inputs, topk_weights, outputs=None, topk_ids=None, expert_map=None, num_valid_tokens=None)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum.moe_fused_mul_sum)

Fused kernel for MoE (Mixture of Experts) to perform weighted summation of expert outputs.

Parameters:

-

(`inputs`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum.moe_fused_mul_sum(inputs))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The output from experts. Shape: (num_tokens, top_k, hidden_size).

-

(`topk_weights`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum.moe_fused_mul_sum(topk_weights))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)The weights assigned to each expert for each token. Shape: (num_tokens, top_k).

-

(`outputs`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum.moe_fused_mul_sum(outputs))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional pre-allocated output tensor. Shape: (num_tokens, hidden_size).

-

(`topk_ids`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum.moe_fused_mul_sum(topk_ids))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional indices of the top-k experts. Shape: (num_tokens, top_k). A value of -1 marks a slot the expert GEMM skipped; those slots are excluded from the sum. When provided, rows with all top ids < 0 (worst-case padding) are skipped and their output rows left untouched. Required when

`expert_map`

is provided. -

(`expert_map`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum.moe_fused_mul_sum(expert_map))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional mapping for Expert Parallelism. A value < 0 indicates an invalid token/expert pair that will be skipped. Only needed when

`topk_ids`

may contain non-local expert ids; if every non-(-1) id is already a local expert, leave it None to skip the redundant per-slot lookup. -

(`num_valid_tokens`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.moe_fused_mul_sum.moe_fused_mul_sum(num_valid_tokens))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)| None`None`

) –Optional device scalar (1-element tensor) holding the number of real token rows (num_recv for a decode dispatch). When provided, rows past it are left untouched, so the static cudagraph grid never sums stale padding rows. Pass the token count, not token*top_k.


Returns:

## Source code in `vllm/model_executor/layers/fused_moe/moe_fused_mul_sum.py`


|
|