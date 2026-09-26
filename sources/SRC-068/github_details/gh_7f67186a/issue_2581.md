# [Issue #2581] Support head_dim=512 on SM89 (Ada) for Gemma 4 global attention layers

source: https://github.com/Dao-AILab/flash-attention/issues/2581
state: open | updated: 2026-09-09T22:05:36Z
labels: 

## 正文

## Feature request

Add a `head_dim=512` forward path in FlashAttention for **compute capability 8.9 (Ada — L40, L40S, RTX 4090)**.

## Why

Google's Gemma 4 ships a hybrid attention design with 4 global-attention layers at `head_dim=512` (alongside 26 layers at `head_dim=256`, which FA2 already handles cleanly). On SM89, `flash_attn_varlen_func` currently rejects `head_dim=512` outright — the model can't use FlashAttention for those layers at all.

## Why a separate ask from #2427

#2427 tracks `head_dim=512` generically. The path being explored there is **FA4 / cute** kernels, which depend on Hopper TMA + WGMMA. FA3 and FA4 are gated to compute capability ≥ 8 **excluding 8.6 and 8.9**, so anything that lands in FA4 will not reach Ada GPUs.

For SM89 the realistic path is **extending FA2** (or a dedicated SM89 kernel) to handle `head_dim=512`. We understand this is harder:
- No TMA — global→shared loads have to be hand-staged.
- No WGMMA — smaller MMA tiles → tighter SMEM budget for a 512-wide head.

## What would be sufficient

A `head_dim=512` forward path (varlen + paged-KV) on SM89, FP16/BF16 Q/K/V, with FP8 KV-cache support if feasible. Prefill is the more painful case for long-context Gemma 4 inference; decode is a bonus. Causal-mask + sliding-window support to match the rest of FA2.

## 评论 (5)

### bghira · 2026-06-20

TriAttention for Gemma4 is pretty nice, at least.

### ShuaiShao93 · 2026-06-20

> TriAttention for Gemma4 is pretty nice, at least.

We mainly use vllm. Does vllm use triattention as the backend?

### maya-undefined · 2026-08-18

I've started work on this...

### drew-chen · 2026-09-05

@maya-undefined are you still working on this? otherwise I can take a look

edit: I've decided to take a look at this more myself

### maya-undefined · 2026-09-09

@drew-chen yes, i'm still working on it.

I have managed to implement this feature but it requires more optimization
