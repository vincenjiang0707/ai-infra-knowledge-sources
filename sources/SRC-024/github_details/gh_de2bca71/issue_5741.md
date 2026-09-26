# [Issue #5741] [Defect]: Unified_attention produces wrong output using SPLIT_UNMASKED_LOOP=1 and SLIDING_WINDOW=1

source: https://github.com/ROCm/aiter/issues/5741
state: open | updated: 2026-09-22T18:24:59Z
labels: 

## 正文

In #4761, The new `SPLIT_UNMASKED_LOOP` tends to eliminate masks for causal attention, by introducing a new loop for unmask-safe tiles from start to the 'mask+unmasked mixed'(END) tile, then the regular masked Loop. This however doesn't work well with SLIDING_WINDOW, which requires masking at both START and END. Users can currently use it attending "out of window" KV.

## Worked example: union vs intersection

The general argument above is easier to check on one small block. Take
`context_len C = 8`, `SLIDING_WINDOW W = 8`, `BLOCK_Q = 4`, `TILE_SIZE T = 2`,
block rows `qpos = 0..3` (`lo = 0`, `hi = 3`).

Per-row admissible key ranges, `l(qpos) = C + qpos - W + 1` and
`u(qpos) = C + qpos`:

```
row 0:  [1,  8]
row 1:  [2,  9]
row 2:  [3, 10]
row 3:  [4, 11]
         ^       lows increase with qpos, slope 1
```

Two different questions can be asked about this block, and they have
different answers:

| question | answer | bound | binding row |
|---|---|---|---|
| **A.** Which tiles does the block need *at all*? | `[1, 11]` — the **union** | `l(lo) = 1` | `lo` |
| **B.** Which tiles need *no mask for any row*? | `[4, 8]` — the **intersection** | `l(hi) = 4` | `hi` |

`tile_start` (L275) is the answer to **A**: `floor(l(lo)/T) = floor(1/2) = 0`.
That is correct for A — row 0 genuinely needs key 1, which lives in tile 0, and
the comment at L270 says "union" outright.

L297 is asking **B**. The right answer is `ceil(l(hi)/T) = ceil(4/2) = 2`.
It is handed `0`.

`unmasked_tile_end` (L294) = `floor((C + lo + 1)/T) = floor(9/2) = 4`, which is
correct: `u(lo) = 8`, tile 3 = keys {6,7} fits, tile 4 = keys {8,9} does not.

So the fast loop runs tiles `[0, 4)` = keys 0..7 with no mask, when it should
run tiles `[2, 4)` = keys 4..7. Tiles 0 and 1 are the damage:

```
key:          0    1    2    3  |  4    5    6    7
row 0 [1, 8]  X   ok   ok   ok  |  ok   ok   ok   ok
row 1 [2, 9]  X    X   ok   ok  |  ok   ok   ok   ok
row 2 [3,10]  X    X    X   ok  |  ok   ok   ok   ok
row 3 [4,11]  X    X    X    X  |  ok   ok   ok   ok
              ^^^^^^^^^^^^^^^^     ^
              claimed unmasked     intersection starts here (key 4)
              10 violations
```
There is currently no rule enforcing user to disable `SPLIT_UNMASKED_LOOP` with sliding window attention.

## Reproduction

gfx1151. Gemma-4-style sliding geometry: `head_size=256`, 16 Q / 8 KV heads,
`block_size=64`, bf16 Q+KV, `q_tokens=512`, `kv_len=1536`, `SLIDING_WINDOW=1024`,
validated against a naive reference. `num_warps=8`, `num_stages=1`,
`waves_per_eu=0`.

| BLOCK_M | BLOCK_Q | TILE_SIZE | `SPLIT=1` rel err | `SPLIT=0` |
|--------:|--------:|----------:|------------------:|----------:|
| 32  | 16 | 16 | 3.9e-01 | ok |
| 32  | 16 | 32 | 3.7e-01 | ok |
| 32  | 16 | 64 | 4.4e-01 | ok |
| 64  | 32 | 16 | 3.7e-01 | ok |
| 64  | 32 | 32 | 3.7e-01 | ok |
| 64  | 32 | 64 | 4.4e-01 | ok |
| 128 | 64 | 16 | 4.4e-01 | ok |
| 128 | 64 | 32 | 4.4e-01 | ok |
| 128 | 64 | 64 | 4.4e-01 | ok |

## Suggested fixes:
1. Guard `SPLIT_UNMASKED_LOOP` with no `SLIDING_WINDOW` assertion. Easy, and immediate fix. Sliding window attn is bounded with growing context-len, so probably not a big bottleneck.
2. Actually support SLIDING_WINDOW by adding another masked loop in front, for the correct behavior.

## 评论 (4)

### amd-xavierwang · 2026-09-21

@vorapolsiloai @cagrikymk . I can issue a fix based on your suggestions how to proceed, as I noticed there is still open PR #5158.

### vorapolsiloai · 2026-09-22

@amd-xavierwang Thanks for the detailed analysis and reproduction. I agree that option 1 is the right immediate fix.

When I tested [PR #4761](https://github.com/ROCm/aiter/pull/4761), the workload was non-windowed, and the enabled configs were intentionally restricted to non-windowed attention. I therefore missed that the kernel still allowed this invalid combination to be selected manually or by a future config. Good catch.

I suggest adding a compile-time assertion next to the existing shuffled-KV guard:

```
tl.static_assert(
    not (SPLIT_UNMASKED_LOOP and SLIDING_WINDOW > 0),
    "SPLIT_UNMASKED_LOOP does not support sliding-window attention",
)
```
It would also be good to add focused coverage confirming that:

- SPLIT_UNMASKED_LOOP=1 with sliding window is rejected.
- Sliding-window attention with the split disabled still matches the reference.
- The existing non-windowed split path remains unchanged.

The configurations in [PR #4761](https://github.com/ROCm/aiter/pull/4761) and [PR #5598](https://github.com/ROCm/aiter/pull/5598) already keep the split disabled for sliding-window cases, so the tested results are unaffected.

Since you found the issue and offered to fix it, please go ahead with the PR and tag me for review. If you would prefer me to implement it, just let me know. 

@cagrikymk what do you think?

### cagrikymk · 2026-09-22

@vorapolsiloai @amd-xavierwang This makes sense.

I think we can do that for now, unless we have very large sliding window cases that requires getting rid of masking in the hot loop.

I guess we need to also scan existing configs and make sure any case that has the masked split also has a matching SWA so we dont hit there.

Another alternative is to fall back to SPLIT_UNMASKED_LOOP=0, if SWA exists.

### amd-xavierwang · 2026-09-22

Thanks for the insights. I think I am going to do the following:
1. Adding kernel level assertion like @vorapolsiloai suggested. Undoubted. Strongest assertion.
2. I just used agent to check all existing configs. So far #4761 is the only one that use the UNMASK flag so we don't have existing bugs in upstream yet. I am also thinking whether we should implement the fallback: I don't think CI so far covers all config cases, so we might accidentally allow new PRs with this bug. We should not rely on reviewers to remember this problem manually.

One other question not related to this issue: Does it make sense if I add in support for non-causal attn into unified_attn? @cagrikymk 
