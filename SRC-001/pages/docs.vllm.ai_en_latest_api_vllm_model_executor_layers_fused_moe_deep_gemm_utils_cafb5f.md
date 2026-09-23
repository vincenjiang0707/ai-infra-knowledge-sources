source: https://docs.vllm.ai/en/latest/api/vllm/model_executor/layers/fused_moe/deep_gemm_utils/
lastmod: 2026-09-23

#

`vllm.model_executor.layers.fused_moe.deep_gemm_utils`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.deep_gemm_utils)

Taken from https://github.com/ModelTC/LightLLM/blob/8ed97c74c18f11505b048b1ba00ba5c0cef8bff6/lightllm/common/fused_moe/deepep_scatter_gather.py and updated to fit vllm needs and terminology.

Functions:

-
–[compute_aligned_M](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.deep_gemm_utils.compute_aligned_M)Return

`M_sum`

only (backward-compat wrapper). -
–[compute_aligned_M_and_alignment](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.deep_gemm_utils.compute_aligned_M_and_alignment)Return (M_sum, alignment_used).


##

`compute_aligned_M(M, num_topk, local_num_experts, alignment, expert_tokens_meta)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.deep_gemm_utils.compute_aligned_M)

Return `M_sum`

only (backward-compat wrapper).

Equivalent to :func:`compute_aligned_M_and_alignment`

's first return value. Existing downstream callers and the warmup path that only size a workspace use this. Call sites that need the actual per-expert alignment (to wrap GEMMs in `mk_alignment_scope`

) should use :func:`compute_aligned_M_and_alignment`

instead.

## Source code in `vllm/model_executor/layers/fused_moe/deep_gemm_utils.py`


##

`compute_aligned_M_and_alignment(M, num_topk, local_num_experts, alignment, expert_tokens_meta)`

[¶](https://docs.vllm.ai#vllm.model_executor.layers.fused_moe.deep_gemm_utils.compute_aligned_M_and_alignment)

Return (M_sum, alignment_used).

`alignment_used`

may be smaller than the caller-supplied `alignment`

on SM100/SM120 when DeepGEMM can JIT a smaller BLOCK_M for the per-call expected_m. Callers that index by block size (e.g. `M_sum // block_m`

) or assert workspace alignment must use the returned `alignment_used`

, not their original `alignment`

argument.

Prefer this over the int-returning :func:`compute_aligned_M`

when the GEMM call site needs to wrap itself in `mk_alignment_scope`

or otherwise reason about the actual per-expert padding.