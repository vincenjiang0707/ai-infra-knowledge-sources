# [Issue #4323] [Feature]: DCP-aware interface and behaviour for `trtllm_mha` to support DCP + Spec

source: https://github.com/flashinfer-ai/flashinfer/issues/4323
state: closed | updated: 2026-09-25T02:12:39Z
labels: feature request, priority: must have (P0), needs-triage

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

We are adding DCP (decode context parallelism) + speculative decoding for GQA models in SGLang
(sgl-project/sglang#32795, sgl-project/sglang#32858), which requires

1. Strided KV ownership. Local key `c` on rank `r` = global pos `c * cp_world + r`. Kernel sees only this rank’s shard + local page table / `seq_lens`
2. Support `return_lse`
3. Global causal masking via `causal_seqs` + `cp_world` + `cp_rank`

What we'd want is roughly what #4178 did for MLA: `cp_world`, `cp_rank`, and a
`causal_seqlens_kv_global` carrying the global per-request KV length, with the
per-row bound worked out inside the kernel.  

See  [DCP design document ](https://docs.google.com/document/d/1pjBSID0palpuI7rx8Ck7Z0BcyzBXAgnkDrf9uQg0uqU/edit?tab=t.0#heading=h.9w6mfr2kxls6) or our [blog](https://www.lmsys.org/blog/2026-07-27-kimi-k3-day0-support/#decode-context-parallelism:~:text=next%20part%20covers.-,Decode%3A%20context%20parallelism,-Decode%20is%20where) for more details on how KV is sharded across ranks

Longer note: For DCP (non-spec), we currently shard the token dimension
round-robin — local key `c` on rank `r` is global position `c*cp_world + r` —
and build a compacted page table plus rank-local `seq_lens` host-side, so the
kernel never sees the striding. `trtllm_batch_decode_with_kv_cache` already
returns the partial LSE we need for the cross-rank merge, and plain DCP decode
works today. However it breaks at `q_len_per_req > 1`, which is what we need for spec decode. With
`L` draft tokens, query row `j` of request `i` should see local keys up to `floor((S_i + j - r) / cp_world) + 1`. That steps by one every `cp_world` rows, so it isn't the affine `seq_len - L + j + 1` the kernel derives internally, and no single `seq_lens` value per request expresses it. We can't precompute it host-side either without a per-row length tensor, which breaks our CUDA graph static buffers.

### Requested outcome

Add DCP + Spec support for `trtllm_batch_decode_with_kv_cache` (or other cutedsl MHA backends ?)

### Target hardware

SM100 (B200, GB200), SM103 (B300, GB300)

### Inference engine

SGLang

### Affected model or model family

_No response_

### Workload and configuration

- Data type and quantization:
- Batch size or request concurrency:
- Sequence lengths or token counts:
- Parallelism: TP / EP / DP / PP / disaggregated
- Relevant shapes: heads, head dimension, hidden size, experts, top-k, page size, or other
- Environment: output of `python -m flashinfer.collect_env`


### Current workaround

_No response_

### Impact

_No response_

### Acceptance criteria

_No response_

### Related work, dependencies, or suggested scope

_No response_

### Timing or release need

_No response_

## 评论 (5)

### nvpohanh · 2026-08-05

@leejnau could you bring this up with FlashInfer team?

I see several options:

(1) Extend the current trtllm-gen MHA/GQA kernels to support DCP features.
OR 
(2) Add CuteDSL MHA/GQA kernels to support DCP features, BUT with comparable perf with trtllm-gen MHA/GQA kernels.



### nvpohanh · 2026-08-05

@yyihuang do you have thoughts about which option you plan to take to approach to this question? thanks!

### anjoj0 · 2026-08-23

Our DFlash speculative-decoding and multi-device prefill/decode work highlights a few semantic constraints that may help the DCP + Spec design:

1. With round-robin KV ownership, each speculative query row can have a different local causal bound. A single per-request `seq_lens` cannot represent this; the bound should be derived from the global length, query-row index, `cp_world`, and `cp_rank` inside the kernel (or represented by a device-resident per-row tensor).
2. Sparse/strided ownership metadata, page tables, and lengths should remain device-resident and graph-stable. Rebuilding them on the host or synchronizing per step would remove much of the benefit of speculative decoding.
3. The partial attention output and LSE should have a documented merge contract, including empty local KV and the LSE base, so the cross-rank reduction is numerically well-defined.
4. Acceptance tests should use independent query rows, ragged lengths, prefix-shared/permuted pages, short contexts, and CUDA-graph replay rather than only the single-token decode case.

We do not have an SM100 environment to benchmark a FlashInfer kernel directly, but we can contribute workload-level validation and API review based on our DFlash and P/D-separation experiments.

### yyihuang · 2026-09-25

@kpham-sgl Update for this request: [feat(cake_fmha): add native Blackwell DCP speculative decode](https://github.com/flashinfer-ai/flashinfer/pull/4518) was merged on 2026-08-27 (UTC).

The DCP + speculative-decode route requested here is merged.

- Adds cp_world, cp_rank and causal_seqlens_kv_global to trtllm_batch_decode_with_kv_cache and selects the native Cake route when DCP metadata is supplied.
- Implements round-robin KV ownership and per-query-row causal bounds, with O=0 / LSE=-inf for empty local rows. Caller-owned buffers and prewarmed workspace support CUDA Graph replay.

The returned LSE for this route is base 2; use the documented cross-rank merge convention. Supported dtype/head/page/query-length profiles are listed in the PR.


### yyihuang · 2026-09-25

@kpham-sgl Update for this request: [fix(cake_attention): enable DCP on SM107 and skip unsupported VSA tests](https://github.com/flashinfer-ai/flashinfer/pull/5111) was merged on 2026-09-14 (UTC).

The merged DCP speculative-attention route now also admits SM107.

- Uses the existing sm100f family target on SM107 while retaining the SM100/SM103 target selections.
- Adds architecture-selection and JIT-source coverage; the family-target route requires CUDA 12.9 or newer.

This is an architecture-support follow-up to the DCP functionality, not a change to its causal-mask or LSE contract.

