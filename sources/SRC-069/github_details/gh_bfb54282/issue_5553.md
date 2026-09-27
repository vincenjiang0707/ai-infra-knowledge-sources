# [Issue #5553] SM120 sparse-MLA decode (DSv3.2 / GLM-NSA): chunks_per_block follows the call's total token count, so a request's output depends on the other requests in the step

source: https://github.com/flashinfer-ai/flashinfer/issues/5553
state: open | updated: 2026-09-25T22:16:30Z
labels: needs-triage

## 正文

## Summary

Through `trtllm_batch_decode_with_kv_cache_mla(..., sparse_mla_top_k=...)` the caller cannot set `chunks_per_block`, and the SM120 sparse-MLA decode chooses it from the total number of tokens in the call (`resolve_wave_cpb(tokens, head_blocks, chunks, requested, sm)`, `csrc/sparse_mla_sm120/attention_resolve.cu:20-39` on main `bf82326b`; the same algorithm in `csrc/sparse_mla_sm120_decode_dsv3_2.cu` in 0.6.18). The calibrated planner on main keys on the same total (`select_cpb(num_tokens, ...)`, `_calibration.py:341-376`). cpb changes how a query's candidates are split across CTAs and merged, so a request's output rows change when another request joins the decode step, although every query row is independent. Decode through this path is not batch invariant.

## Environment

- 2 × DGX Spark (GB10, SM121, 48 SMs), TP=2
- GLM-5.3-Flash NVFP4: 32 heads per rank, d_qk 576, `kv_scale_format="arbitrary_fp32"` (GLM-NSA), top-k 2,048, page 64, fp8_ds_mla KV
- vLLM `385dce36` (`FLASHINFER_MLA_SPARSE_SM120` backend), FlashInfer 0.6.18, `enable_flashinfer_autotune=False` (no autotune cache file)

## Observation

- The heuristic's choice on 48 SMs: T=1 → 2, T=2 → 3, T=4 → 6, T=8 → 15 (T = tokens in the call). With MTP depth 3 a sequence brings 1 token to a draft step and 4 to a verification step, so a second sequence changes T from 1 to 2 and from 4 to 8.
- The same query rows computed alone and with a second sequence's rows in the call (`sparse_mla_sm120_decode_dsv3_2`, fixed KV and indices): at the verification step all 128 rows (4 tokens × 32 heads) differ, at the draft step all 32 rows, max |Δ| 6.1e-5.
- With `chunks_per_block` passed explicitly the rows are bit-identical with or without the second sequence, in either order (verification step: each of 1, 2, 4, 6, 8, 15, 16, 32; draft step: 2 and 6). A value equal to the heuristic's (6 at T=4) is bit-identical to the unset call.

## What we do now

In vLLM's SM120 backend we take cpb from the tokens of one sequence (2 for a draft step, 6 for a verification step, the heuristic's own values for one sequence) and call `sparse_mla_sm120_decode_dsv3_2(..., chunks_per_block=cpb)` directly, which reproduces the public route's decode exactly for a request alone. That entry is only in the private module, and the public API has no argument for it.

## Request

Let callers pin the split: expose `chunks_per_block` through `trtllm_batch_decode_with_kv_cache_mla` / the public sparse-MLA API, or offer a batch-invariant policy that chooses it from the per-request query length instead of the call's token count.

## Side note: per-call cost of the public route (0.6.18)

In 0.6.18 each call through the public route builds a `_SparseMLAPagedAttentionRunner`, normalizes the segments, goes through the registered custom op and asks the AutoTuner (the heuristic's choice is not cached). Calling the decode entry directly with cpb set was 60 to 410 µs shorter per call in a synchronous microbenchmark on GB10. We did not see it in end-to-end decode tokens/s on our pair. main's refactor appears to remove most of this path; v0.7.0 still builds a wrapper per call.


## 评论 (1)

### Bizuayeu · 2026-09-25

Correction to "What we do now": that section does not describe our serving accurately. Our image routes the SM120 sparse-MLA backend through our own reference sparse-NoPE attention (`GLM53_REFERENCE_ATTENTION=1`), and the patched `forward_mqa` returns through it before the FlashInfer decode call. A trace of the running pair confirmed that every sparse-MLA forward took that route, so the per-sequence cpb code described there never ran in serving. We removed it in our 1.16.0 release.

Everything under Summary and Observation stands as reported, and so does the 60 to 410 µs figure in the side note. Those came from direct calls (the decode entry, or vLLM's `forward_mqa` with our route switched off) on one GB10 with one TP rank's shapes. The sentence "We did not see it in end-to-end decode tokens/s on our pair" should be disregarded; that path was not running. The request is unchanged.

