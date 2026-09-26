# [Issue #444] [Bug] SM120 m_grouped_fp8 contiguous kernel: illegal memory access at CUDA graph replay (eager + capture + identical-replay all clean)

source: https://github.com/deepseek-ai/DeepGEMM/issues/444
state: open | updated: 2026-09-18T00:49:51Z
labels: 

## 正文

## Description

The SM120 (consumer/workstation Blackwell) `m_grouped_fp8_fp4_gemm_nt_contiguous` kernel runs cleanly in eager mode across our full shape matrix, completes CUDA-graph **capture**, passes a full end-to-end quality probe — and then hits an **illegal memory access at graph replay** (`torch.cuda.CUDAGraph.replay()` → `CUDA_ERROR_ILLEGAL_ADDRESS`).

We believe this is the grouped-GEMM instance of the same family as #414 (`pack_ue8m0_to_int` not capture safe) and #431/#430 (missing tensormap drain): the SM120 1D1D kernels update tensormaps on-device (`ptx::tensor_map_replace_*` + publishing the updated tensormap to a GMEM buffer) inside the stream. Under graph capture the tensormap state from the first invocation is recorded; on replay a new batch has a different per-expert token distribution, so TMA consumes stale descriptors and reads out of bounds.

## Environment

- DeepGEMM: **0.1.5.post3** (wheel, nv_dev line with SM120 grouped support)
- GPU: NVIDIA RTX PRO 5000 72GB Blackwell (capability 12.0), single node TP8
- torch 2.13.0+cu130, CUDA 13.0
- Workload: GLM-5.3-Flash blockwise-FP8 MoE via sglang — G=288 experts, per-rank w13 N=512/K=4096 and w2 N=4096/K=256, ue8m0-packed scales on both operands (weights requantized to 2^k scales, activations quantized with column-major TMA-aligned packed scales)

## What works (eager, everything)

- The official `test_m_grouped_gemm_contiguous` shapes: 32/32 pass on this GPU
- Our exact production shapes (G=288, w13/w2, decode `expected_m_per_group` 1/32/113): all pass eager, outputs clean
- The same official-generator inputs inside `torch.cuda.graph` capture **and a single replay with identical inputs/shape**: passes (stale-descriptor hazard not exercised when nothing changes between capture and replay)

## What fails

1. sglang serve with the deep_gemm MoE runner: decode CUDA-graph **capture completes** (20 batch-size tiers), a 30-request prefill/generate quality probe **passes 30/30** (accept_len 2.99, matching the triton baseline) — then the first real decode step replaying the captured graph dies with `illegal memory access` at `full_cuda_graph_backend.py replay()`. With `CUDA_LAUNCH_BLOCKING=1` the report is stable.
2. Offline: any eager call sequence that changes `m_indices` / per-expert distribution between iterations while the same buffers are reused is the suspected trigger; we reproduced the crash deterministically inside the server and captured the exact kernel arguments via a one-shot dump right before the failure (available in the repro kit below).

## Evidence / repro kit

- Kernel-argument dump → offline replay reproduces the scale-format assertion (fixed on the sglang side, see sgl-project/sglang#39063 comment) and isolates this replay crash
- Gate-pass / replay-crash split: eager path fully functional, graph replay of a *changed* batch fails
- Scripts: argument dumper (monkeypatched dispatch entry), offline replayer, official-generator A/B harness, graph-capture harness — happy to attach or open a PR with a regression test

## Suspicion (for maintainers)

`sm120_fp8_fp4_gemm_1d1d.cuh` publishes updated tensormaps to GMEM per group switch; under graph capture these side effects are frozen. A capture-safe design likely needs either (a) persistent tensormap buffers whose contents are re-derived on replay from the (graph-external) `m_indices`/count tensors, or (b) falling back to static descriptors when captured. Related: #414 (pack kernel capture safety), #431 (tensormap drain port), and sgl-project/sglang#25551 (B300 graph-capture crash in the same integration path).

Happy to test any candidate fix on this hardware on short notice.


## 评论 (3)

### ZeroKernel798 · 2026-09-15

Hi @liaoruoxue — thanks for a very readable report. The capture-frozen-tensormap
mechanism is clear, and the way you split the evidence (eager ✓ / capture ✓ /
identical-input replay ✓ / changed-batch replay ✗) is what made it obvious this is a
capture-semantics problem rather than a plain correctness one.

I'd like to work on this. I have an 8× RTX PRO 5000 (SM120, 72GB), TP8 node — the same
card you're on — so I can reproduce and validate on matching hardware.

Four things before I start.

First, are you planning to open the PR yourself? You mentioned being happy to attach one
with a regression test. If that's still your plan I'll stay out and just follow the
thread — I'd rather not duplicate your work.

Second, where should this land? #431 bases on `nv_dev`, #447 bases on `nv_dev`, and the
repro itself is on the `nv_dev` line. #447 in particular is a ~22k-line SM120 / main-API
integration — opened 17 hours after your report, still moving as of 16:10 — and it
doesn't mention #444 or #431. Should I base a fix on current `nv_dev`, or wait for #447
to land first?

Third, on #431 — my read is that it's orthogonal to what you're hitting: #431 fixes an
in-flight-drain race (its own evidence is non-determinism on identical inputs), whereas
here everything is clean except a changed-batch replay. So I'd expect #431 not to move
your repro. But you have the repro and I don't, so — does it?

Either way I'll keep my change independent of it unless it's going to land first, rather
than binding my diff to someone else's 7 lines.

Separately: #431 was validated on a 5090 D. I'm on 8× PRO 5000, which is what this replay
path actually runs on here — happy to re-run its validation as a side task if that's
useful.

Fourth, if the answer to the first is no, I'd like to try approach (a) — re-deriving the
tensormap contents on replay from the graph-external `m_indices`/count tensors, so the
descriptors are never captured in a stale state. Approach (b) reads to me like it would
cost the grouped path its adaptivity, so I'd treat it as the fallback if (a) turns out
not to be feasible.

Your repro kit would save a lot of time — the argument dumper, offline replayer,
official-generator A/B harness and graph-capture harness. Would you be able to attach or
link the scripts?

I'll start by checking out `nv_dev` and reproducing the replay crash locally. If you'd
rather I not proceed, just say so and I'll stop.

### lucifer1004 · 2026-09-16

Analysis on the #447 branch: the m-grouped contiguous path performs **no** on-device tensormap mutation at all — every `tensor_map_replace_*` / GMEM-tensormap write sits inside the k-grouped-only branch (which additionally drains in-flight TMA before publishing, the #343 fix class). A/B/SF descriptors for m-grouped are host-built `__grid_constant__` values, and per-expert routing (`m_indices`) is re-read from GMEM on every launch/replay, so a replay with a new expert distribution cannot consume stale descriptor state.

Regression coverage for exactly this scenario: `test_sm120_quant_grouped_graph_mutation` captures a CUDA graph once, then replays it with *changed* expert distributions (lengths permuted per phase, including an all-empty phase) via in-place metadata copies — same pointer, new values — across m_indices/psum/masked modes. Clean on sm_120a, including under memcheck/racecheck subsets.


### liaoruoxue · 2026-09-18

Thanks both — update from our side with matching-hardware verification of #447 (head `b6acafe`), built from source on an RTX PRO 5000 72GB (SM120.0) node: **all 73 tests in `tests/test_sm120_gemm.py` pass, including `test_sm120_quant_grouped_graph_mutation`** (5:40 wall). That test covers exactly our original scenario — capture once, replay with changed expert distributions (permuted lengths, including an all-empty phase) — and it is clean on this hardware. This is consistent with @lucifer1004's analysis (host-built `__grid_constant__` descriptors, per-launch GMEM routing re-reads). Our original crash was observed on the nv_dev wheel (0.1.5.post3) via the sglang runner path, so from our perspective **#447 resolves #444 once merged — no separate fix PR needed from us.**

@ZeroKernel798 — we won't open a PR ourselves (bandwidth is on the serving side). Two things we can hand over:
- [Isolation chain](https://gist.github.com/liaoruoxue/3896b01696cb069f3215ab05dbd885c7) (eager → capture → same-input replay → changed-batch replay, our serving shape G=288/emp=32). Honest note: on our hardware the *synthetic* chain stays clean even on the affected wheel — the crash only reproduced from the exact dumped serving arguments.
- [Entry-point dump + offline replay method](https://gist.github.com/liaoruoxue/2d93ab35f9e242eb57a879b6ddba8efa) — the technique that reproduced it deterministically; generally useful for serving-side kernel crashes that resist synthetic repros.

We can validate any fix on matching 8×TP8 hardware — though given the above, review/validation of #447 itself may be the most useful contribution now.

Two build notes for anyone testing this branch from source (our stumbles; wheel installs unaffected): ① `pip install -e .` over a pre-existing deep_gemm wheel leaves the old package dir winning import resolution — force `PYTHONPATH` and verify `deep_gemm.__file__` before trusting any result; ② editable installs skip `prepare_includes` (third-party cutlass/deep_jit headers only get copied during wheel builds), so JIT nvcc fails on missing `cute/…` headers until they are copied manually.
