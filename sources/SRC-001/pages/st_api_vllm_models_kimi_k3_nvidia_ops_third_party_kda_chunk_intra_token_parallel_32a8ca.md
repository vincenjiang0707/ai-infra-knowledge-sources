source: https://docs.vllm.ai/en/latest/api/vllm/models/kimi_k3/nvidia/ops/third_party/kda/chunk_intra_token_parallel/
lastmod: 2026-09-24

#

`vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel)

Functions:

-
–[chunk_kda_fwd_intra_token_parallel](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel)Token-parallel implementation: each token gets its own thread block.


##

`chunk_kda_fwd_intra_token_parallel(q, k, gk, beta, Aqk, Akk, scale, cu_seqlens=None, chunk_size=64, sub_chunk_size=16)`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel)

Token-parallel implementation: each token gets its own thread block. Supports both fixed-length and variable-length sequences. Reduces wasted computation on padding.

Writes directly to Aqk and Akk tensors (in-place).

Parameters:

-

(`q`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(q))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[B, T, H, K]

-

(`k`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(k))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[B, T, H, K]

-

(`gk`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(gk))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[B, T, HV, K] cumsum of gates (HV >= H for GVA)

-

(`beta`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(beta))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[B, T, HV]

-

(`Aqk`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(Aqk))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[B, T, HV, BT] output tensor to write to

-

(`cu_seqlens`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(cu_seqlens))`LongTensor | None`

, default:`None`

) –cumulative sequence lengths for variable-length input

-

(`Akk`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(Akk))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)[B, T, HV, BC] output tensor for diagonal blocks (fp32)

-

(`scale`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(scale))

) –[float](https://docs.python.org/3/builtins/functions.html#float)attention scale

-

(`chunk_size`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(chunk_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`64`

) –BT (default 64)

-

(`sub_chunk_size`

[¶](https://docs.vllm.ai#vllm.models.kimi_k3.nvidia.ops.third_party.kda.chunk_intra_token_parallel.chunk_kda_fwd_intra_token_parallel(sub_chunk_size))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`16`

) –BC (default 16)