# [Issue #5007] [Tracking] Unified paged-prefill API (experimental) — owner, scope, graduation plan

source: https://github.com/flashinfer-ai/flashinfer/issues/5007
state: open | updated: 2026-09-19T18:13:43Z
labels: needs-triage, experimental

## 正文

Tracking issue required by the experimental policy (#4880) for the unified paged-prefill API in PR #4015.

## Owner

Yang Xu (@YangXu1990uiuc).

## Why experimental

The API is a new public contract for paged prefill (one canonical metadata form, init-time `resolve()` with per-backend exclusion reasons, one LSE contract, reject-or-correct validation) that routes to the **existing** fa2/fa3, cuDNN, and trtllm-gen kernels. The contract is under review with vLLM/SGLang; the shape of `plan()`/`run()` may still change based on that review, so it ships without compatibility guarantees first.

Public entry: `flashinfer.attention.unified` (`resolve_paged_prefill`, `UnifiedPagedPrefill`), marked `@flashinfer_experimental_api`. Implementation: `flashinfer/experimental/paged_prefill/` laid out like `flashinfer/mla/_batch_mla/` (#4697). Tests: `tests/experimental/test_unified_prefill_*.py` (conformance matrix + reject-or-correct fuzzer).

## Relationship to `BatchPrefillWithPagedKVCacheWrapper`

The new API supersedes the wrapper. Plan of record (strangler pattern):

- **0.7**: new API ships experimental; the wrapper gets a *soft* deprecation notice in its docstring and docs (no runtime warning). The wrapper is frozen to bug fixes.
- **0.8**: new API graduates (tag removal, no import-path change); the wrapper emits `DeprecationWarning` once per instance and becomes a thin shim over the same controller/backends.
- Removal no earlier than two minor releases after the warning lands.

## Graduation criteria (target: 0.8)

- [ ] fp8 KV cache with per-tensor scales (vLLM `--kv-cache-dtype fp8`, SGLang `k_scale_float`) as a capability axis with fuzzer coverage; NVFP4 KV as follow-up
- [ ] layer constants (`sm_scale`, `window_left`, `logits_soft_cap`) accepted at `run()` so one plan serves layers with different hyperparameters
- [ ] LSE base and layout declared at plan time (`base2`/`basee`, `(tokens, heads)`/`(heads, tokens)`), kernel-native where free
- [ ] CUDA-graph replan protocol (reserved metadata buffers, transactional staging) equivalent to the Batch MLA design
- [ ] heuristic order seeded from benchmark data (measured 2026-09-07 on SM100, b=8/q=1024/kv=4096/32:8 heads/D128/page16: cuDNN 352 us < trtllm-gen 375 us < fa2 1543 us on HND; on NHD cuDNN falls to 886 us, so layout must feed ranking)
- [ ] cuDNN direct `cu_seq_len` path exercised in CI (needs cuDNN >= 9.25, cudnn-frontend >= 1.27; venv verified on 9.27/1.28)
- [ ] at least one serving engine (vLLM or SGLang) confirms migration or has a PR open
- [ ] docs page for the new API and the "which paged-prefill API" note

## Findings so far attributable to the fuzzer

- #4014 (merged): cuDNN graph-cache key omitted `attn_scale`.
- #4663 follow-through: cuDNN LSE base change double-folded in the adapter; caught as 14/14 "SILENT WRONG LSE" on H100 + SM100, fixed in #4015.

Related: #3605 (Release-Quality Action Plan, Stream 1c), #4697 / #4037 (Batch MLA backend architecture), #4880 (experimental policy).

<!-- note to self: claude::d6f47b32-e07c-43ec-9755-cd807049d528 — "tracker #3605 status refresh 2026-09-06 / PR #4015 rebase + experimental isolation"
cwd /home/scratch.yanxu_libs/flashinfer · workspace /tmp/claude-25653/wt-4015 -->


## 评论 (5)

### YangXu1990uiuc · 2026-09-07

Naming settled in #4015: `flashinfer.prefill.PagedAttention` / `PagedAttentionMetadata` / `resolve_paged_attention` (final; import path will not change at graduation). Contract shape settled: `plan(metadata, ..., lse_mode=)` + `run(..., sm_scale=)`. Remaining criteria above are additive.

### YangXu1990uiuc · 2026-09-07

fp8 KV axis landed in #4015 (kv_dtype + k_scale/v_scale at run). Measured support for bf16-q + e4m3-KV: **fa2 only**; fa3 (no JIT variant), cuDNN (rejects mixed fp8), trtllm-gen (no kernel) cannot — that is a kernel-side gap, not an API one, and explains vLLM's mock-dequantized-cache workaround. fp8-q paths (fa3, trtllm-gen, cuDNN) remain an undeclared axis.

### YangXu1990uiuc · 2026-09-08

CUDA-graph re-plan protocol landed in #4015 (reserved storage + transactional staging, tests on all four backends). Graduation-required items now: engine confirmation only (fp8 KV, graph re-plan, docs done). Fuzzer tally +1: cuDNN prefill graph-cache key omitted strides / KV dtype / bound offsets (HND graph replayed on NHD K/V), fixed in #4015.

### 0z5a · 2026-09-19

Hi @YangXu1990uiuc  , I’d like to help with the serving-engine graduation item for the unified paged-prefill API.

Rather than changing the API work in #4015, I’d like to take a narrow vLLM integration slice based on the current contract.

My proposed first scope is:

opt-in integration only, with no default backend behavior change;
native FA2 paged-prefill first;
BF16/FP16 on SM89 as the initial hardware envelope;
reuse vLLM’s existing metadata/planning lifecycle rather than create a second source of truth;
correctness coverage through the real vLLM metadata path;
then multi-worker / TP and CUDA-graph replan coverage once the basic adapter is stable.

I specifically don’t want to duplicate the unified API implementation or the engine-shaped mock integration already in #4015 — the goal would be a real downstream vLLM patch.

If the vLLM migration is not already owned by someone, I’d like to take this integration slice.

### 0z5a · 2026-09-19

The real vLLM integration this issue graduates toward is now open as a draft: https://github.com/vllm-project/vllm/pull/57709 (opt-in, default off, prefill only; decode untouched).

What it wires: `PagedAttentionMetadata.dense(...)` built from the CPU mirrors vLLM already owns (no new hot-path D2H), a `Resolution` pinned once and passed back to every `plan()`, `plan()` per build, `run(..., out=)` writing the caller's preallocated prefill slice, `sm_scale` per run, and `lse_mode="none"`. Pinned dependency: #4015 head `a05ffb0865a9a4b51609f09174cde4e423bfd290`; the adapter raises with that revision in the message if the API is absent or drifted, and never falls back silently.

Status of the prototype itself on an L20 (SM89, runtime `flashinfer-python==0.6.18`): the API is reachable and correct through the vLLM metadata path.

- API-level probe (no vLLM), six configurations against an independent fp32 causal reference built by gathering K/V from the page table: single short, exact page, page−1, page+1, mixed lengths with a non-contiguous page table, multi-page. All six resolved `backend=fa2`, `max_abs_err` 6.6e-3 … 8.4e-3.
- Adapter suite against vLLM v0.29.0: 14 passed / 0 failed at the pre-warmup revision; the warmup revision adds 5 cases.
- Engine A/B on the L20 (`Qwen/Qwen3-0.6B`, `page_size=16`, `kv_layout=NHD`, one fresh server per arm, order A→P→P→A, 16 requests per workload at concurrency 4, greedy, prefix caching off, four warmup requests):

| workload | metric | opt-in off | opt-in on | delta |
|---|---|---|---|---|
| in=512/out=16 | TTFT mean | 125.4 ms | 61.9 ms | −50.6% (2.03x) |
| in=512/out=16 | prefill throughput | 10 465 tok/s | 17 964 tok/s | +71.6% |
| in=3072/out=16 | prefill throughput | 28 822 tok/s | 31 841 tok/s | +10.5% |
| in=3072/out=16 | request wall mean | 423.4 ms | 371.5 ms | +12.2% |

Two things worth feeding back into the prototype, both measured rather than argued:

1. Without warmup the identical comparison reads as a regression (prefill throughput 12 876 → 9 582 tok/s at 512, 36 136 → 20 892 tok/s at 3072) because the first requests pay the one-time JIT/plan cost. The integration now issues one bounded synthetic plan+run at engine init (opt-in only, before `/health`, never inside capture) and logs its duration. If the prototype wants to own that, a documented "prepare artifacts" entry point would be the natural place.
2. The long-prompt TTFT difference is inside the noise of this measurement, so the honest claim is "short-prompt prefill gain, long-prompt throughput gain, TTFT parity" — not a uniform win. TP2/TP4, CUDA graph/replan, over-capacity rejection and plan/metadata CPU time are still not run.

One API gap hit while integrating: the controller allocates its own 128 MiB workspace, so an engine gets one scratch buffer per metadata builder with no way to inject an existing workspace. Not a blocker here (144 MiB total, resident before the real KV tensors), but an injection point would help engines that already own a scratch pool.

