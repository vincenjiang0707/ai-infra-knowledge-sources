source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/models/iquest_loopcoder/
lastmod: 2026-09-23

#

`vllm.model_executor.models.iquest_loopcoder`

[¶](https://docs.vllm.ai#vllm.model_executor.models.iquest_loopcoder)

Inference-only LoopCoder model compatible with HuggingFace weights.

Classes:

-
–[LoopGateProjection](https://docs.vllm.ai#vllm.model_executor.models.iquest_loopcoder.LoopGateProjection)Gate projection for mixed attention in Loop 2+.


##

`LoopGateProjection`

[¶](https://docs.vllm.ai#vllm.model_executor.models.iquest_loopcoder.LoopGateProjection)

Bases: [Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html#torch.nn.Module)

Gate projection for mixed attention in Loop 2+.

Computes: g = sigmoid(linear(Q)) for each head independently. This gate determines how much to use Loop1's KV (global) vs current loop's KV (local).

Supports tensor parallelism: each GPU handles a subset of heads. The weight matrix has shape [num_heads, head_dim] and is split along the head dimension.

Methods:

-
–[forward](https://docs.vllm.ai#vllm.model_executor.models.iquest_loopcoder.LoopGateProjection.forward)Compute gate values from query tensor.


## Source code in `vllm/model_executor/models/iquest_loopcoder.py`


|
|

###

`forward(query)`

[¶](https://docs.vllm.ai#vllm.model_executor.models.iquest_loopcoder.LoopGateProjection.forward)

Compute gate values from query tensor.

Parameters:

-

(`query`

[¶](https://docs.vllm.ai#vllm.model_executor.models.iquest_loopcoder.LoopGateProjection.forward(query))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_heads, num_tokens, head_dim] (vLLM flattened format) where num_heads is the number of heads on this TP rank and num_tokens = batch * seq_len


Returns:

-
(`gate`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[num_tokens, num_heads * head_dim] (flattened format matching q shape)