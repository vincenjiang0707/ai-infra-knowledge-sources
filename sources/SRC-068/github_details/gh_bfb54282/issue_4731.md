# [Issue #4731] [sm120] NVFP4 KV: masked multi-token XQA verify (q_len_per_req>1) is intermittently ~3x slower, cancelling the MTP speedup; q_len=1 is fine

source: https://github.com/flashinfer-ai/flashinfer/issues/4731
state: open | updated: 2026-09-19T07:40:14Z
labels: bug, needs-triage, model: qwen3.5 / 3.6 / 3.8, op: attention

## 正文

## Summary

On sm_120 (RTX PRO 6000 Blackwell), `xqa_batch_decode_with_kv_cache` with **NVFP4 KV** (`kv_cache_sf` provided) behaves correctly and at normal speed for `q_len_per_req=1`, but with masked multi-token speculative verify (`q_len_per_req=4` + `mask` + `q_cu_seq_lens` from MTP k=3) draft acceptance intermittently collapses: final outputs stay correct (rejection sampling), yet the accepted-token rate drops enough to roughly double the number of decode steps, with strongly bimodal end-to-end decode speed (35–107 tok/s across otherwise identical runs; the FA2 route on the same stack gives a stable ~104).

Because `q_len_per_req=1` is healthy and the FA2 path with the same cache contents is healthy at all q lengths, the suspect is the masked multi-query fp4 path (verify logits for later in-block positions), rather than cache layout or scale handling.

## Environment

- flashinfer-python / flashinfer-cubin **0.6.16.post3**, torch 2.13.0+cu130, CUDA 13.0, sm_120 (RTX PRO 6000 Blackwell Workstation, 96 GB), native Linux.
- Integration: vLLM v0.27.2-era tree with vllm-project/vllm#46329 applied (NVFP4 KV on sm12x, HND layout, linear per-block V scale factors), model Qwen3.8-27B hybrid (16 full-attention layers, GQA 24/4, head_dim 256), MTP `num_speculative_tokens=3`, 262k context.

## Call pattern

Per decode step (uniform batch, CUDA-graph captured):

```python
xqa_batch_decode_with_kv_cache(
    query=q_bf16,                        # [batch*4, 24, 256]
    kv_cache=(k_data_u8, v_data_u8),     # HND, [pages, 4, page, 128] packed fp4
    kv_cache_sf=(k_sf, v_sf),            # linear per-block SF views (strided)
    workspace_buffer=...,
    block_tables=..., seq_lens=..., max_seq_len=...,
    bmm1_scale=softmax_scale * k_scale, bmm2_scale=v_scale,
    kv_layout="HND",
    q_len_per_req=4,
    mask=draft_block_mask,
    q_cu_seq_lens=cu_lens,
)
```

## Observations

| configuration | result |
|---|---|
| q_len_per_req=1 (no spec decode), nvfp4 | correct, ~63–66 tok/s ≈ raw forward rate |
| q_len_per_req=4 + mask, **fp8** KV, same stack | stable, acceptance 0.494/pos, ~110 tok/s |
| q_len_per_req=4 + mask, **nvfp4** KV | correct outputs, but acceptance collapses intermittently; decode steps ~2x; bimodal 35–107 tok/s |
| same nvfp4 cache read via FA2 paged prefill route | stable, acceptance 0.459/pos, ~104 tok/s |

Needle-in-haystack through the nvfp4 XQA path is 8/8 at ~24.5k and ~257k tokens (temperature 0), so plain retrieval/reads are fine; the degradation is specific to the masked multi-token verify scores.

## Ask

Is the masked multi-query path expected to support fp4 KV on sm_120, and if so, does the mask/e4m3-scale handling differ from the q=1 path in a way that could perturb later-position logits? Happy to build a standalone reproducer (fixed cache contents, q=4 masked call vs 4 sequential q=1 calls, compare logits) if that is the most useful next step — guidance on the expected tolerances for that comparison would help.


## 评论 (3)

### ima-helikoptaaa · 2026-09-01

Ran a standalone synthetic test on RTX PRO 6000 (sm120, cap 12.0) with flashinfer 0.6.17 / torch 2.13.0+cu130. Used `nvfp4_attention_sm120_quantize_qkv` to pack the KV cache so the byte layout matches what the kernel expects.

Results at batch=2, Q_HEADS=16, KV_HEADS=2, HEAD_DIM=128, PAGE_SIZE=16, SEQ_LEN=512:

- fp4 q=4 masked (causal mask, q_cu_seq_lens set) ran without error and produced outputs at the same magnitude as fp4 q=1 (~4.9 vs ~4.7 norm). No crash, no garbage position.
- Per-position error vs 4x individual q=1 calls was 0.37-0.43 abs for fp4 and 0.32-0.42 for fp8, comparable across all four positions. Later positions showed no special degradation vs position 0.
- 100 iterations with varied queries, threshold 1.0: 0 failures, max error 0.77.

So the kernel machinery at these shapes does not show the divergence pattern on sm120. A few things I could not exercise though. My test uses a synthetically populated paged KV cache, not the KV cache written by the real model's prefill path, so any bug tied to how token scales are interleaved across pages would not show up here. Also my box runs the model with fp8_e4m3 KV so I could not trigger the path through a live inference run. If the issue only manifests at model-scale shapes or with the real page-layout written during prefill, this test would miss it.

Happy to try larger shapes or a specific config that was known to trigger it if that would help narrow things down.

### ssubbotin · 2026-09-17

@ima-helikoptaaa Thank you for putting real sm120 hardware on this. Your negative result is more useful than it looks, because going back over the archived counters from that session I have to correct my own report: the title is wrong. Correcting that first, then the shapes, since the two are connected.

## The acceptance claim does not survive the counters

I still have the Prometheus scrapes bracketing the MTP window of the 2026-08-25 session. Deltas, same box (RTX PRO 6000 Blackwell, sm_120), same model, MTP k=3, `--max-model-len 262144`:

| arm | acceptance/pos | accepted per draft | decode tok/s per run |
|---|---|---|---|
| nvfp4, **XQA** decode, MTP | **0.530** | 1.589 | 35.0 / 46.7 / 53.4 / 71.2 / 75.2 / 107.1 |
| nvfp4, FA2 decode, MTP | 0.459 | 1.378 | 90.7 / 100.1 / 102.3 / 104.1 / 109.8 / 121.7 |
| fp8, FA2 decode, MTP | 0.494 | 1.482 | 103.3 / 113.3 / 126.7 |
| nvfp4, XQA decode, **no MTP** | n/a | n/a | 28.5* / 56.1 / 63.7 / 66.4 |

<sub>*first request of the arm, TTFT 15.9 s, warm-up. Runs are 1000 completion tokens each off an 8k-token prefix, temperature 0.7, cache-busted per run.</sub>

Acceptance on the XQA route is the highest of the three arms, at 0.530/pos and 1.59 accepted tokens per draft. It does not degrade. What degrades is throughput: the runs span 35 to 107 tok/s against a 90 to 122 band on the FA2 route reading the same cache, with nothing varying between runs but RNG.

The tell I should have led with is the last row. **MTP buys almost nothing on the XQA route**: 1.59 accepted tokens per draft, and the median decode rate barely moves from the no-MTP baseline (71.2 vs 63.7). On FA2, comparable acceptance produces the speedup you would expect.

So this is not a numerics or mask-handling bug, and the outputs were never wrong. The masked multi-token verify call intermittently costs about as much wall time as the tokens it saves. That makes your result the expected one: an absolute-error comparison of a q=4 masked call against 4 sequential q=1 calls *should* pass. Sorry for sending you after the wrong quantity.

Suggested retitle: "[sm120] NVFP4 KV: masked multi-token XQA verify is intermittently ~3x slower, cancelling the MTP speedup".

## Why head_dim 128 could not show it either

`test_xqa_batch_decode_nvfp4_kv` hardcodes `head_dim = 256`, and that is the only shape the nvfp4 XQA path is built for. The 128 configuration in your script is a different kernel specialization, so it would not have shown the effect whatever the effect turned out to be.

## The coverage gap this configuration sits in

On main, the nvfp4 matrix in `tests/attention/test_xqa_batch_decode.py` is:

```
(batch, q_len_per_req, page_size, num_kv_heads, head_grp_size)
(1, 1,  16, 2, 4)
(1, 1,  32, 2, 4)
(4, 4,  64, 4, 2)    <- the only q_len_per_req > 1 row
(1, 1,  64, 2, 4)
(1, 1,  64, 2, 8)
(1, 1, 128, 2, 4)
```

with `kv_layout` restricted to NHD and `max_in_kv_len=300`. Against that, my configuration misses every axis on the multi-token side:

| axis | covered at q_len_per_req > 1 | this report |
|---|---|---|
| page_size | 64 | **2848** |
| head_grp_size | 2 | 6 (24 q heads / 4 kv heads) |
| kv_layout | NHD only | **HND** |
| sequence length | ~300 | 24k to 257k |

Page size is where I would look first. vLLM does not get to choose it freely for this model: the stack is hybrid, the attention page has to be at least as large as the mamba page, and the engine resolves that with `Setting attention block size to 2848 tokens to ensure that attention page size is >= mamba page size`. That is 22x the largest page size in the test matrix, and it means a 24k-token request is roughly 9 pages. If the decode kernel partitions work per page, then a handful of very large pages is a pathological shape for occupancy, and "sometimes the SMs are fed, sometimes they are not" is the kind of mechanism that produces a 3x spread on identical inputs while leaving every output correct.

That block-size line is from a current build of the same model with the same flags on this box. The August build used the same model and `--max-model-len`, and the value is forced by the model's mamba page size rather than by anything I set, so it held then too; I will confirm it from the boot log next time I bring that branch up.

## If you want another attempt at a repro

head_dim 256, HND, `q_len_per_req=4` with a chain mask, `num_kv_heads=4`, `head_grp_size=6`, page_size large (2848 to match exactly, though I would expect the trend to appear by 512), and sequence lengths in the tens of thousands so that each request is only single digits of pages. Measure per-call wall time across many calls rather than the output delta, and keep the call CUDA-graph captured if you can: an eager loop with a fresh workspace per call may well be perfectly stable.

## Status downstream

vllm-project/vllm#46329 now routes sm12x nvfp4 decode to the FlashInfer-native FA2 path and never selects the dedicated XQA kernel, so no vLLM user is exposed to this today. The issue is about the kernel rather than about anyone being blocked.

@bkryu #2638 was closed on exactly the lesson that head_dim 256 had no coverage in the bf16 matrix. Given that the nvfp4 matrix tests one multi-token row, at one page size, in one layout, would a page_size axis above 128 and an HND row be worth adding there? I can run any matrix you want on this card.


### ssubbotin · 2026-09-19

Two follow-ups on my own comment, one confirming a number I left hedged and one withdrawing a comparison I should not have made.

**The page size is confirmed at 2848, on both builds.** I said I would check this from a boot log rather than assert it. The current head of vllm-project/vllm#46329 logs `Setting attention block size to 2848 tokens to ensure that attention page size is >= mamba page size` on the nvfp4 arm, and so does the backport image the August measurements in this issue were taken on, same model and `--max-model-len 262144`. So the configuration behind this report really is page_size 2848, against a test matrix whose largest nvfp4 page size is 128.

Worth adding, because it sharpens rather than repeats the coverage point: an fp8 control on the same box and flags resolves to **1600**, not 2848. The attention page has to be at least the mamba page, and nvfp4 halves the per-token attention bytes, so it takes proportionally more tokens to reach that floor. The consequence is that on a hybrid model like this one the nvfp4 path does not merely land outside the tested page sizes, it is pushed *further* outside them than any other KV dtype, by construction. It is not a configuration a user chooses.

(The fp8 control also resolves to a different decode backend on current main, so this is not a clean isolation of page size alone.)

**Correction: I should not have ranked the arms by acceptance.** I wrote that XQA acceptance was "the highest of the three arms, at 0.530/pos", against 0.459 on the FA2 route. Those counters come from windows bracketing different amounts of work, 4,993 drafts against 2,524, and by their file naming they covered different benchmark sets. Acceptance depends on what is being generated, so comparing the arms that way is not supported by what I measured.

What the XQA window does support on its own is the part the retitle rests on: 0.530 per position over 4,993 drafts, 1.589 accepted tokens per draft, per-position 0.717 / 0.505 / 0.367. That is an ordinary spec-decode profile, not a collapse, which is why the original title was wrong. The throughput finding is unaffected: 35 to 107 tok/s across runs differing only in RNG, against 90 to 122 on the FA2 route reading the same cache, and 63.7 with MTP disabled entirely on the XQA route.

