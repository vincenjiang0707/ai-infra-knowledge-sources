# [Issue #5293] [Perf] pa_decode_sparse: BLOCK_K=64 is suboptimal above the CU count — up to +43 % on gfx950 with a load-dependent choice

source: https://github.com/ROCm/aiter/issues/5293
state: open | updated: 2026-09-07T19:02:30Z
labels: 

## 正文

`pa_decode_sparse` hardcodes `BLOCK_K = 64` (attention/pa_decode_sparse.py, gfx950 gluon driver). On MI355X this is only the right choice while the launch fits on the CUs — above that, `BLOCK_K = 32` is faster by up to **43 %**, with identical numerics.

## Measurements

MI355X (gfx950), 64 heads, head_dim 512 (448 NoPE + 64 RoPE), packed fp8 cache, top-k 2048 per query, `has_invalid=False`. Times are the minimum of 5 rounds × 15 iterations.

| queries | K=64 | K=32 | better | delta |
|---|---|---|---|---|
| 1–16 | 62–64 µs | 62–65 µs | K=64 | 0.4–1.2 % |
| 24 | 78.4 | 72.8 | **K=32** | 7.6 % |
| 28 / 30 / 32 | 73–77 | 90–96 | K=64 | 19.2 % |
| 34 / 36 | 122–131 | 103–116 | **K=32** | 12.9–18.6 % |
| 48 | 121.7 | 110.3 | **K=32** | 11.1 % |
| 60 / 64 | 131–134 | 165 | K=64 | 19.0–19.9 % |
| 68 / 72 | 204–207 | 170–193 | **K=32** | 6.0–21.6 % |
| 96 | 218.9 | 193.1 | **K=32** | 13.0 % |
| **128** | 264.5 | **186.9** | **K=32** | **41.5 %** |
| 192 | 403.2 | 354.2 | **K=32** | 13.8 % |
| 256 | 552.1 | 399.5 | **K=32** | 38.2 % |

Max abs deviation against a torch reference is 0.000061 for **both** variants — this is purely a scheduling effect, not a numerics tradeoff.

## Why it is not monotonic in `num_queries`

The switch tracks the number of CTAs, not the query count:

```
ctas = num_queries * num_splits * heads_blocks
```

`num_splits` comes from `_decode_num_splits`, so e.g. 32 queries can launch fewer CTAs than 34. Sorting the same data by `ctas` makes it monotonic, and the threshold lands exactly on the CU count (`get_num_sms()` = 256 here):

```
BLOCK_K = 32 if ctas > get_num_sms() else 64
```

This predicts **21 of 21** measured load points correctly. Intuition: while every CTA gets its own CU, the larger block (4 warps, 64 KB LDS) does more work per CU; once multiple waves are needed, the smaller block (2 warps, 32 KB) packs better and hides the gather latency.

## Suggested change

In the gfx950 driver, replace the constant with the rule above. Wired in, it stays within ±0.6 % of the per-point optimum from 24 queries upward:

| queries | vs fixed K=64 | vs per-point optimum |
|---|---|---|
| 24 | +7.7 % | +0.5 % |
| 48 | +10.9 % | +0.1 % |
| 96 | +12.8 % | +0.2 % |
| **128** | **+43.2 %** | +0.5 % |
| 192 | +13.4 % | +0.1 % |
| 256 | +39.0 % | −0.0 % |

Note that `num_splits` must be computed before `BLOCK_K` (it is currently derived after), and `get_num_sms()` should be hoisted to module scope — at 62 µs kernel time a per-call lookup is measurable in microbenchmarks, though not in production where the decode runs inside a CUDA graph.

## Things that did not help (same setup)

- `GSPT` (bytes per thread in the gather layout): 16 is optimal; 8 costs 14 %, 32 costs 45 % at K=64.
- `waves_per_eu` 1 / 2 / 4: −4 % / −4 % / −69 %.
- Cache modifier `.cs` instead of `.cg`: does not compile.
- Forcing `kv_splits`: the automatic choice is already optimal at 64+ queries; more splits cost up to 45 %.

Happy to open a PR if the rule looks right to you — and glad to re-measure on other shapes (different head counts, top-k, or a bf16 cache) if that would help.


## 评论 (1)

### stefanskiasan · 2026-09-07

Follow-up on my own report, to keep the priority honest: **the microbenchmark
above stands, but it does not translate into end-to-end throughput on a real
deployment**, and I think that is worth recording before anyone spends
implementation time on it.

## What I measured since

Production setup: GLM-5.3 (full, `glm_moe_dsa`), Quark MXFP4 + FP8 attention,
MI355X, TP4, top-k 2048, MTP k=4, 128 concurrent.

Switching `BLOCK_K` 64 → 32 through the whole server, **caches disabled**:

| load | BLOCK_K=64 | BLOCK_K=32 | delta |
|---|---|---|---|
| 128 concurrent | 1474.9 tok/s | 1476.3 tok/s | **0.09 %** |
| 8 concurrent | 651.5 tok/s | 652.6 tok/s | **0.17 %** |

Flat. An earlier internal number of +1.5 % turned out to be a prefix-cache
artifact (the two arms had different cache hit rates), which is a mistake worth
flagging on its own — a throughput A/B on this kind of kernel is meaningless
unless the prefix cache and any KV connector are switched off.

## Why the two results are not in conflict

`pa_decode_sparse` is simply not a dominant term in our decode profile. Two
independent findings on the same setup:

- the sparse decode path uses only ~7 % of available HBM bandwidth — it is
  gather-latency bound, not throughput bound, so tile-width changes move a
  small term
- decode as a whole is issue-bound here (~16 % execution), which caps what any
  single-kernel improvement can return end-to-end

So the kernel-level gain is real and the numbers in the issue body were taken
carefully, but the model-level payoff on a GLM-5.3-class workload is under the
measurement noise. If someone is weighing this against other work, that ratio
matters more than the 43 %.

Still worth fixing in my view — a load-dependent choice is strictly better than
a hardcoded 64, and the rule is three lines — but as cleanup, not as a
throughput win. I did not carry it as a local patch for exactly that reason.

