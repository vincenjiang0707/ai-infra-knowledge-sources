# [Issue #595] [Feature Request] Support Expert-Choice Routing via Native Expert-Centric API (`[num_experts, capacity]`)

source: https://github.com/deepseek-ai/DeepEP/issues/595
state: open | updated: 2026-09-19T09:26:26Z
labels: 

## 正文

## Background

Expert-Choice routing (Zhou et al., *Mixture-of-Experts with Expert Choice Routing*, NeurIPS 2022) inverts standard Token-Choice routing: instead of tokens selecting experts, each expert selects its top-C preferred tokens. 

This paradigm is increasingly adopted in large-scale models, such as EC-DiT (*EC-DIT: Scaling Diffusion Transformers with Adaptive Expert-Choice Routing*, ICLR 2025). In configurations with 64 or 128 experts, a popular token can be selected by well over 32 experts.

## Current Limitation & Performance Bottleneck
DeepEP currently enforces a Token-centric design where `topk_idx` expects a shape of `[num_tokens, num_topk]`. Mapping Expert-Choice outputs back to this Token-centric format introduces two critical issues:

1. **Assertion Failure:** A single token selected by >32 experts triggers `EP_DEVICE_ASSERT(num_topk <= 32)` (e.g., `intranode.cu#L408`).
2. **Padding Overhead (Structural Inefficiency):** To map Expert-Choice to `[num_tokens, num_topk]`, `num_topk` must equal the maximum number of times *any* single token is selected. Because token selection distribution is highly skewed in EC routing, the resulting `topk_idx` tensor will be extremely sparse, filled with padding (e.g., `-1`). Processing this padded tensor through the current dense kernels wastes registers, shared memory, and memory bandwidth.

## Proposed Solutions

**Solution 1: Native Expert-Centric API (Preferred)**
Introduce a new set of dispatch/combine APIs that natively accept Expert-centric indices. 

* **Input Shape:** `token_indices` of shape `[num_experts, expert_capacity]`.
* **Advantages:** Directly aligns with the output format of Expert-Choice models, avoiding expensive inverse mapping.
    * Completely eliminates padding overhead and structural sparsity.
    * Bypasses the `num_topk <= 32` constraint naturally, as the iteration is over capacity rather than a variable number of experts per token.
* **Expected API Behavior:**

  ```python
  # Expert-Choice directly produces selected token indices
  token_indices = torch.randint(0, num_tokens, (num_experts, capacity), dtype=torch.int32, device="cuda")
  expert_weights = torch.randn(num_experts, capacity, device="cuda")

  # New dispatch interface
  buffer.dispatch_expert_choice(x, token_indices=token_indices, weights=expert_weights, ...)
  ```

**Solution 2: Relax num_topk Limit with Sparse Branching (Alternative / Fallback)**
If adding a new API surface is temporarily out of scope, the existing `[num_tokens, num_topk]` API can be modified to tolerate EC routing.
* **Implementation**: Remove or increase the `EP_DEVICE_ASSERT(num_topk <= 32)`. To mitigate the padding overhead described above, the CUDA kernels (`intranode.cu` / `internode.cu`) must be updated with dynamic branching to early-exit (break) warp execution when encountering padding indices (-1), minimizing invalid memory accesses.
* **Drawback**: This remains suboptimal due to the unavoidable pre-processing mapping overhead and register pressure from large `num_topk` loops.

## 评论 (1)

### 0z5a · 2026-09-19

I’d like to work on this.
@niyunsheng 

For a first PR, I’d prefer to keep the scope around the routing contract and metadata path rather than immediately modifying every transport kernel.
