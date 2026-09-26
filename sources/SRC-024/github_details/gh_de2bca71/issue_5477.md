# [Issue #5477] gfx950 paged MQA logits: next_n spends the tile on program count, leaving the kernel's own M-efficiency curve unused (M=32 vs 1.53x at M=128)

source: https://github.com/ROCm/aiter/issues/5477
state: open | updated: 2026-09-15T01:38:08Z
labels: 

## 正文

## Summary

On gfx950, `deepgemm_fp8_paged_mqa_logits` launches `grid = batch_size * next_n * SplitKV`, and each program runs its own `[heads, HiddenDim] x [HiddenDim, KVBlockSize]` MFMA over its own walk of the K cache. Under speculative decoding the `next_n` dimension therefore multiplies the *program count* rather than the *tile*: with DeepSeek-V4.1-Flash (`index_n_heads = 32`, DSpark 5-token MTP, so `next_n = 6`) that is six independent M=32 GEMMs per K block where one M=192 GEMM would do.

The kernel's own M-scaling says what that costs, and it is not small.

## Measurement

MI355X (gfx950, 256 CU), aiter 0.1.21.post2, `_gluon_deepgemm_fp8_paged_mqa_logits_preshuffle`, `Preshuffle=True`, `KVBlockSize=128`, `ChunkK=256`, `WavePerEU=2`, `HiddenDim=128`, batch 16, `next_n` 6, uniform context 131072, `max_model_len` 1048576.

Timed by CUDA-graph replay. Worth flagging for anyone reproducing: a plain host loop measures the Python wrapper (~250 us per call of views, dtype splits and the compile-cache lookup) and not the kernel, which is enough to hide the entire effect.

Varying `heads` — and therefore `ChunkQ`, and therefore M — at **identical K-cache traffic**, since K traffic does not depend on the head count:

| heads (= ChunkQ = M) | time | per unit of work |
|---:|---:|---:|
| 32 | 139.1 us | 139.1 us |
| 64 | 219.2 us | 109.6 us |
| 128 | 362.8 us | 90.7 us |

Per unit of work, M=64 is **1.27x** more efficient than M=32, and M=128 is **1.53x**. The curve is monotone and has not flattened by M=128.

Our configuration sits at the worst point of it: M=32, with the `next_n` factor spent on program count.

## This is not a bandwidth problem

The obvious reading of `grid = batch * next_n * SplitKV` is that the K cache is streamed `next_n` times, and we initially assumed the fix was to stop re-reading it. That turns out to be wrong, and we would rather save you the experiment.

We built both variants in plain Triton, identical in every respect except whether `next_n` sits in the grid or inside the K loop, both validated to 5.6e-6 against a torch reference:

| variant | HBM bytes requested | time |
|---|---:|---:|
| per-`next_n` programs | 1711 MB | 284 us |
| shared K walk | 327 MB | 308 us |

Asking for 5.2x fewer bytes is *slightly slower*. The re-reads are already absorbed by cache — the programs sharing a K range are `batch_size` apart in program ID, so they are co-resident and hit in L2/LLC.

The same conclusion falls out of the numbers above: doubling heads doubles the compute at constant K bytes and costs only 1.5x the time, so the kernel is substantially compute-bound at this operating point, not bandwidth-bound. At `next_n=1` it reaches 5.4 TB/s of essential traffic (68% of the 8 TB/s spec peak), which is a good number; at `next_n=6` the extra time is per-token MFMA and epilogue work, not extra traffic.

## The ask

Tile `next_n` into the M dimension so one K block feeds all speculative tokens — a single M = `next_n * heads` MFMA (192 here) instead of `next_n` separate M = `heads` MFMAs — with the epilogue reducing per head-group and emitting one output row per token.

The per-token epilogue work is irreducible: each speculative token needs its own `k_scale` product, ReLU, weight, causal bound (`context_length - next_n + pid_next_n`) and output row. Only the GEMM shape changes.

Sizing this honestly: the table above is measured by *adding* work (more heads), whereas fusing `next_n` reorganizes the *same* work into a larger tile, and the epilogue differs — M=128 does one 128-way reduction into one output row, while fused `next_n` needs six 32-way reductions into six rows. So we would not expect the full 1.53x. But the direction and the rough magnitude look solid, and even the M=64 point (1.27x) applied to a kernel that is 5.9% of our decode step is worth having.

## Ruled out already

- **`VarCtxSchedule`.** The persistent-grid variant looks like the answer for ragged batches, and our contexts are ragged (costing about 27% efficiency relative to uniform). It is **1.7x slower** in every shape we tried, so it is not a workaround. vLLM does not pass it, which appears to be correct.
- **Doing it caller-side.** `next_n` cannot be folded into `heads` from outside, because the kernel weight-sums across `ChunkQ` and each speculative token needs its own logits row.
- **Reimplementing in plain Triton.** Our version of the same algorithm runs at 1.1–1.3 TB/s against this kernel's 2.4–2.6 TB/s, a 2.2x gap. The tuning in the gluon kernel is not something a caller can reproduce, which is why this is a request rather than a patch.

## Environment

MI355X x8 (gfx950, 256 CU, 288 GiB), ROCm 7.x nightly, aiter 0.1.21.post2, triton 3.5, vLLM `0.28.1rc1.dev681+ge7edf17ce`, DeepSeek-V4.1-Flash TP4, `index_n_heads` 32, `index_head_dim` 128, `index_topk` 512, DSpark 5-token MTP (`next_n = 6`), `FULL_AND_PIECEWISE` cudagraph mode.

Called from vLLM at `vllm/v1/attention/ops/rocm_aiter_mla_sparse.py` (`rocm_fp8_paged_mqa_logits`), which passes `ChunkK=256`, `Preshuffle=block_size > 1`, `KVBlockSize=block_size`, `WavePerEU=2`.

Happy to test a branch on this hardware and workload.


## 评论 (1)

### Fangzhou-Ai · 2026-09-15

I extended the existing MQA-logits test in #5434 instead of opening a duplicate PR.

Test commit: [Fangzhou-Ai/aiter@45bf94c](https://github.com/Fangzhou-Ai/aiter/commit/45bf94c8d6cb2d9505d11a9eeb0a382fc4b482f0)

The test now covers:

- prefill and paged decode;
- eager and HIP-graph capture/replay;
- `C={1,2,4,8,16,32,64,128}`, `next_n={1..6}`, and contexts from 10K to 1M;
- native `[C,next_n,H,D]` and serving-style flattened `[C*next_n,1,H,D]` decode, with repeated block tables and per-token causal ends;
- page sizes 32/64 plus the page-128 issue reproducer;
- sampled FP32 numerical references at page/ChunkK seams, exact causal `-inf` checks, and poisoned unwritten tails.

On MI355X/gfx950 with PyTorch `2.12.0+rocm10.0.0` and Triton 3.8, all 2,400 requested matrix cases passed with `err=0`: 576 native/page128 decode cases, 576 flattened/page64 cases, 576 flattened/page32 cases, and 672 prefill cases. An additional 12-case unaligned `N=513` page-seam sweep also passed.

Exact `C=16`, `next_n=6`, `N=131072`, page-128 result:

| Layout | Eager | HIP graph | Error |
|---|---:|---:|---:|
| native | 139.005 us | 138.099 us | 0 |
| flattened | 231.587 us | 230.578 us | 0 |

This gives the kernel change a correctness matrix for both the native layout targeted here and the currently flattened serving call. AI assistance was used to prepare and validate the test; the patch still needs human review before submission.

