# [Issue #4658] [Feature Request] cute-dsl MLA decode: extend cum_seq_lens_q support (follow-up to #3131 / #3238)

source: https://github.com/flashinfer-ai/flashinfer/issues/4658
state: open | updated: 2026-09-25T02:16:47Z
labels: needs-triage, priority: should have (P1)

## 正文

#3131 noted that `is_var_seq` already exists but is "only used in cute-dsl
backend". #3238 added `cum_seq_lens_q`/`max_q_len` for the `trtllm-gen`
path, and explicitly rejects it for cute-dsl:

    if backend == "cute-dsl":
        raise ValueError("cute-dsl MLA does not support cum_seq_lens_q")

Now that trtllm-gen's varlen-query decode is landed and consumed downstream
(sgl-project/sglang#35807), is cum_seq_lens_q support for cute-dsl on the
roadmap, or is there a specific blocker?

Context: sglang requires cute-dsl (or tokenspeed) instead of trtllm-gen for
decode-context-parallelism (DCP) configs (arg_groups/overrides.py enforces
this for Kimi-K3), so DCP users currently can't benefit from the
varlen-decode fix that non-DCP trtllm-gen configs now get.

## 评论 (2)

### shyeh25 · 2026-08-21

cc @nvpohanh @leejnau

### yyihuang · 2026-09-27

@shyeh25 Merged: https://github.com/flashinfer-ai/flashinfer/pull/5577

This adds an experimental **Cake variable-query MLA decode + DCP** implementation on SM100/SM103 (B200/B300). The package explicitly tracks this request and follows the CuTe-DSL variable-Q DCP contract from #4719.

- Explicit APIs: `flashinfer.mla.cake_mla_varq_dcp_decode` and `prepare_cake_mla_varq_dcp_decode`. They accept compact queries with `cum_seq_lens_q` / `max_q_len`, rank-local KV lengths, `cp_world` / `cp_rank`, and global causal bounds.
- Query and KV cache share BF16 or FP8 E4M3 dtype, with 512 latent + 64 RoPE channels, up to 128 heads, and registered routes for page sizes 32/64/128. Results are BF16 output plus natural-log FP32 LSE; empty local rows return zero output and `-inf` LSE for cross-rank merging.
- Prepared runners use caller-owned buffers and support CUDA Graph replay. Cross-rank communication/merging and FP8 query quantization remain caller responsibilities.

The PR reports **1.1791x B200 / 1.1817x GB300 geometric-mean speedup** over CuTe-DSL on 24 measured performance rows, all faster on both GPUs; package tests report 22 passed / 3 skipped per GPU.

This delivers an explicitly selected Cake alternative. It does not change SGLang backend selection or automatically add DCP support to the existing `trtllm_batch_decode_with_kv_cache_mla(..., backend="cake")` route. Downstream integration and validation remain separate.
