source: https://docs.vllm.ai/en/latest/api/vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent/
lastmod: 2026-09-23

#

`vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent)

Functions:

-
–[fused_recurrent_gated_delta_rule](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule)Args:

-
–[token_stride](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.token_stride)Token stride (elements) of a

`[B, T, H, D]`

or`[B, T, H]`

tensor.

##

`fused_recurrent_gated_delta_rule(q, k, v, g, beta=None, scale=None, initial_state=None, inplace_final_state=True, cu_seqlens=None, ssm_state_indices=None, num_accepted_tokens=None, use_qk_l2norm_in_kernel=False)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule)

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)queries of shape

`[B, T, H, K]`

. -

(`k`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)keys of shape

`[B, T, H, K]`

. -

(`v`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(v))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)values of shape

`[B, T, HV, V]`

. GVA is applied if`HV > H`

. -

(`g`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(g))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)g (decays) of shape

`[B, T, HV]`

. -

(`beta`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(beta))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –betas of shape

`[B, T, HV]`

. -

(`scale`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(scale))`Optional[`

, default:[int](https://docs.python.org/3/builtins/functions.html#int)]`None`

) –Scale factor for the RetNet attention scores. If not provided, it will default to

`1 / sqrt(K)`

. Default:`None`

. -

(`initial_state`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(initial_state))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –Initial state of shape

`[N, HV, V, K]`

for`N`

input sequences. For equal-length input sequences,`N`

equals the batch size`B`

. Default:`None`

. -

(`inplace_final_state`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(inplace_final_state))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –bool: Whether to store the final state in-place to save memory. Default:

`True`

. -

(`cu_seqlens`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(cu_seqlens))

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)`None`

) –Cumulative sequence lengths of shape

`[N+1]`

used for variable-length training, consistent with the FlashAttention API. -

(`ssm_state_indices`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(ssm_state_indices))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –Indices to map the input sequences to the initial/final states.

-

(`num_accepted_tokens`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.fused_recurrent_gated_delta_rule(num_accepted_tokens))`Optional[`

, default:[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]`None`

) –Number of accepted tokens for each sequence during decoding.


Returns:

-
(`o`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Outputs of shape

`[B, T, HV, V]`

. -
(`final_state`


) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)Final state of shape

`[N, HV, V, K]`

.

Examples:: >>> import torch >>> import torch.nn.functional as F >>> from einops import rearrange >>> from fla.ops.gated_delta_rule import fused_recurrent_gated_delta_rule # inputs with equal lengths >>> B, T, H, HV, K, V = 4, 2048, 4, 8, 512, 512 >>> q = torch.randn(B, T, H, K, device='cuda') >>> k = F.normalize(torch.randn(B, T, H, K, device='cuda'), p=2, dim=-1) >>> v = torch.randn(B, T, HV, V, device='cuda') >>> g = F.logsigmoid(torch.rand(B, T, HV, device='cuda')) >>> beta = torch.rand(B, T, HV, device='cuda').sigmoid() >>> h0 = torch.randn(B, HV, V, K, device='cuda') >>> o, ht = fused_gated_recurrent_delta_rule( q, k, v, g, beta, initial_state=h0, ) # for variable-length inputs, the batch size `B`

is expected to be 1 and `cu_seqlens`

is required >>> q, k, v, g, beta = map(lambda x: rearrange(x, 'b t ... -> 1 (b t) ...'), (q, k, v, g, beta)) # for a batch with 4 sequences, `cu_seqlens`

with 5 start/end positions are expected >>> cu_seqlens = q.new_tensor([0, 2048, 4096, 6144, 8192], dtype=torch.int32) >>> o_var, ht_var = fused_gated_recurrent_delta_rule( q, k, v, g, beta, initial_state=h0, cu_seqlens=cu_seqlens )

## Source code in `vllm/models/glm5next/nvidia/ops/third_party/kda/fused_recurrent.py`


|
|

##

`token_stride(x)`

[¶](https://docs.vllm.ai#vllm.models.glm5next.nvidia.ops.third_party.kda.fused_recurrent.token_stride)

Token stride (elements) of a `[B, T, H, D]`

or `[B, T, H]`

tensor.

The recurrent kernel walks tokens with this stride and addresses heads densely inside a token, so each token's `[H, D]`

(or `[H]`

) block must be contiguous, tokens must not overlap, and with `B > 1`

sequence `n`

must start at token `n * T`

(dense batch). Column slices of a wider per-token projection buffer satisfy this and are consumed in place.