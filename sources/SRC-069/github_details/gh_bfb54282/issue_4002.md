# [Issue #4002] [Bug] FA2 CUDA-graph no-split plans launch padded CTAs over uninitialized scheduler entries

source: https://github.com/flashinfer-ai/flashinfer/issues/4002
state: closed | updated: 2026-09-21T18:21:37Z
labels: needs-triage

## 正文

## Description

FA2 tensor-core decode can launch CUDA-graph blocks beyond the scheduler entries initialized by the planner when all of these hold:

- `enable_cuda_graph=True`
- `disable_split_kv=True`
- tensor-core FA2 path
- a uniform decode query length

The scheduler constructs entries only for real request, query-tile, and KV-tile work, then pads `padded_batch_size` with the split-KV occupancy target. Since split-KV is disabled, the planner neither initializes the padded scheduler tail nor creates `block_valid_mask`. The FA2 kernel uses `padded_batch_size` directly as grid-x.

The same mechanics remain on current main at `71d31b5a23a3c0394edb36330dec1ce2a0def365`:

- [One-token decode passes `uniform_q_len=0`](https://github.com/flashinfer-ai/flashinfer/blob/71d31b5a23a3c0394edb36330dec1ce2a0def365/flashinfer/decode.py#L1215-L1241)
- [The scheduler creates real entries and then pads grid-x](https://github.com/flashinfer-ai/flashinfer/blob/71d31b5a23a3c0394edb36330dec1ce2a0def365/include/flashinfer/attention/scheduler.cuh#L621-L680)
- [Validity storage is allocated only for split-KV](https://github.com/flashinfer-ai/flashinfer/blob/71d31b5a23a3c0394edb36330dec1ce2a0def365/include/flashinfer/attention/scheduler.cuh#L855-L878)
- [The kernel launches `padded_batch_size` blocks in grid-x](https://github.com/flashinfer-ai/flashinfer/blob/71d31b5a23a3c0394edb36330dec1ce2a0def365/include/flashinfer/attention/prefill.cuh#L4150-L4172)

## Reproduction and evidence

Tested on an H100 80GB SXM5 with 132 SMs, batch size 2, 16 query heads, 2 KV heads, head dimension 128, page size 1, one query row per request, and split-KV disabled.

The planner returned grid-x 132 although it initialized only two scheduler entries. Filling the page-locked integer workspace with `0xA5` before planning left the first tail entries at `0xA5A5A5A5`. The poisoned plan was inspected and intentionally not launched.

With a controlled zeroed tail, Nsight captured grid `(132, 1, 2)`, or 264 CTAs, while the exact initialized grid is `(2, 1, 2)`, or 4 CTAs. This demonstrates redundant execution. Reused nonzero workspace contents create a conditional stale-index correctness risk; this report does not claim unconditional output corruption.

For a uniform decode query length, the exact graph-stable grid is:

`batch_size * ceil((q_len_per_request * num_qo_heads / num_kv_heads) / cta_tile_q)`

## Expected behavior

A no-split CUDA-graph plan must not launch blocks whose scheduler entries were never initialized. When query length is a checked graph invariant, the planner can use the exact initialized grid. Ragged and split-KV paths should retain their current behavior.

## Proposed fixes

- Root planner fix: [flashinfer-ai/flashinfer#4794](https://github.com/flashinfer-ai/flashinfer/pull/4794)
- Guarded integration fix for SGLang's pinned FlashInfer release: [sgl-project/sglang#36785](https://github.com/sgl-project/sglang/pull/36785)


## 评论 (1)

### gf239 · 2026-09-12

Independent reproduction, plus a complementary fix for the memory-safety half.

I hit this from a different direction. `padded_batch_size` comes from `max_batch_size_if_split`, so it follows the SM count. Whether a plan pads at all is a property of the GPU.

On every card I tried, it pads by exactly the SM count:

| device | `padded_batch_size` | real CTAs | unmasked |
|---|---|---|---|
| RTX 4090 (128 SM) | 128 | 4 | 124 |
| RTX 6000 Ada (142 SM) | 142 | 4 | 138 |
| RTX 3080 (68 SM) | 68 | 4 | 64 |
| RTX 4050 Laptop (20 SM) | 20 | 4 | 16 |

With the pinned int workspace poisoned to stand in for an earlier plan, a graph-mode `plan(disable_split_kv=True)` then `run()` dies with `CUDA error: an illegal memory access was encountered`. All four cards, CUDA 12.6 and 13.0 alike.

On a fresh workspace the tail is zeros. The padding CTAs then redo request 0 / tile 0, which is idempotent. That is probably why this is rarely seen.

One more reachability route, possibly worth adding to the report: `_nvfp4_kv_requires_disabled_split_kv` (`prefill.py:1520`) sets `disable_split_kv` on its own for an NVFP4 KV cache on SM120/121, in both the paged and the ragged plan (`:2732`, `:4265`). Pairing that with `use_cuda_graph=True` lands here with no unusual argument. I have no SM120 part, so this one is from reading the code, not running it.

I opened #5176 for the memory-safety half: it materializes `block_valid_mask` whenever the launch is padded, so the padding CTAs exit early instead of reading stale indices.

It does not close this issue, on purpose. The expected behaviour stated here is that such blocks are not launched at all, and that is #4794. `dim3 nblks(padded_batch_size, ...)` is untouched by mine.

The two are complementary. #4794's guard cannot fire for either prefill wrapper today, since `prefill.py` passes `uniform_q_len = 0` at `:2209`, `:2741` and `:4274`. Happy to rebase in either order.

