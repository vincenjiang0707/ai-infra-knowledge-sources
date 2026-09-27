# [Issue #4542] [Feature]: Kimi K3 TP12 kernels for saturated decode on GB300 NVL72

source: https://github.com/flashinfer-ai/flashinfer/issues/4542
state: open | updated: 2026-09-25T11:15:14Z
labels: feature request, needs-triage, op: linear attention

## 正文

### Before submitting

- [x] I have searched existing issues and this request has not been filed yet.

### Problem

Hi CAKE team! We are testing TP12 as a Kimi K3 decode configuration on a GB300 NVL72 rack and would like to check whether the uncovered shapes below fit the kind of problems CAKE wants to take on.

The target is the high-throughput decode regime: we increase decode batch size until the GB300 reaches its throughput saturation region. The relevant `B` is therefore empirical and depends on the complete runtime, sequence lengths, and memory footprint; it is not fixed in this request. The relevant operating range is the part of the batch sweep where aggregate decode throughput approaches its plateau.

## GB300 platform topology

![GB300 compute-tray connectivity](https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/_images/nvl72-ai-factory-03.png)

Source: [NVIDIA GB300 NVL Compute Tray](https://docs.nvidia.com/enterprise-reference-architectures/nvl72-ai-factory/latest/components.html#nvidia-gb300-nvl-compute-tray)

## Why TP12 exposes different shapes

Relevant Kimi K3 dimensions are:

```text
layers                         93
KDA / Gated-MLA layers         69 / 24
hidden size                    7168
KDA heads                      96
KDA head dimension             128
KDA convolution width          4
TP degree                      12
local KDA heads                8
routed latent width            3584
experts / selected experts     896 / 16
```

Our reading of the current public work is summarized below. Please correct us if any of these shapes are already covered on SM103a.

| Area | Public coverage we found | Shape left by TP12 |
|---|---|---|
| Full fused KDA decode | local heads 12/24/32/48/96 | `H=8, D=128` |
| Packed CAKE KDA (#4378) | `T=1, H=12, D=128`, post-convolution | `H=8`; throughput-scale batches |
| AlphaMoE router (#4339) | up to 512 experts, softmax-style routing | 896 experts with K3 sigmoid routing |
| K3 LatentMoE fused tail | TP8 and TP16 | TP12 |

### Requested outcome

We would be interested in any of the following independent kernel candidates. The full KDA decode shape is the main candidate; the other two can be considered separately.

## Shape A: full KDA decode with eight local heads

This is the main candidate. K3 runs this operation in 69 layers, so it remains important even when the GPU is driven by a large active batch.

The operation boundary we use is:

```text
packed projected input       BF16 [B, 3072]       # 3 * H * D
convolution state            BF16 [slots, 3072, 3]
recurrent state              BF16 [slots, 8, 128, 128]
state index                  INT32 [B]
raw output gate              BF16 [B, 8, 128]

width-4 causal convolution
  -> SiLU
  -> recurrent KDA update
  -> output gate + RMSNorm
  -> BF16 [1, B, 8, 128]
```

The relevant shape is `H=8, D=128, T=1` across the batch sweep where aggregate decode throughput approaches saturation on SM103a.

Indexed states, changing batch size, and CUDA Graph execution are part of the serving path. We are happy to adapt our integration to whichever ABI is most natural for CAKE or FlashInfer.

## Shape B: K3 routing in the throughput-saturated decode regime

This is a smaller, independent candidate. The routing rule differs from the currently published AlphaMoE router:

```text
logits                      FP32 [M, 896]
expert correction bias      FP32 [896]
selected experts            16

scores = sigmoid(logits)
ids = topk(scores + correction_bias, 16)
weights = gather(scores, ids)
weights = weights / reduce_sum(weights)

output weights              FP32 [M, 16]
output ids                  INT32 [M, 16]
```

The bias participates in selection but not in the returned weights. `M` follows the decode batch sweep through the throughput saturation region. This candidate is behind the KDA shape in priority.

## Optional: TP12 LatentMoE tail

There is also a TP12 gap in the fused LatentMoE tail. For our decode setup, we would first measure whether this remains worthwhile around the throughput saturation region.

The mathematical boundary is:

```text
routed_partial              BF16 [M, 3584] per TP rank
shared_partial              BF16 [M, 7168] per TP rank

latent = RMSNorm(AllReduce12(routed_partial))
output = latent @ up_weight.T + AllReduce12(shared_partial)
```

The unusual part of TP12 is that 7168 is not divisible by 12. If communication-aware multi-GPU kernels are currently of interest to CAKE, this could be considered separately.

### Target hardware

SM103 (B300, GB300)

### Inference engine

SGLang

### Affected model or model family

Kimi K3 - https://huggingface.co/moonshotai/Kimi-K3/raw/main/config.json

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

- CAKE tracker: <https://github.com/flashinfer-ai/flashinfer/issues/4254>
- packed `T=1, H=12` KDA: <https://github.com/flashinfer-ai/flashinfer/pull/4378>
- AlphaMoE router: <https://github.com/flashinfer-ai/flashinfer/pull/4339>
- Kimi K3 configuration: <https://huggingface.co/moonshotai/Kimi-K3/raw/main/config.json>

### Timing or release need

_No response_

## 评论 (10)

### yyihuang · 2026-08-16

@robin-fain Thank you for the detailed CAKE kernel request. I reopened this issue and linked it as a sub-issue of #4254 so we can track it independently.

### yyihuang · 2026-09-25

@robin-fain [PR #5531](https://github.com/flashinfer-ai/flashinfer/pull/5531) was merged on 2026-09-25 (UTC), delivering the experimental Cake Kimi-K3 fused MoE router on SM100/SM103.

- Routes FP32 logits `[M, 896]`: selects top-16 using `sigmoid(logits) + correction_bias`, then normalizes the selected unbiased sigmoid scores into routing weights. The bias affects selection only.
- Builds the expert-aligned grouped-GEMM route plan in the same launch, with `block_m` 8 or 16. The prepared runner supports allocation-free execution and CUDA Graph replay with updated values in the bound input buffers.
- Covers M = 1, 2, 4, ..., 8192 (powers of two); shapes outside this supported set raise `NotImplementedError`. The PR reports 44 tests per architecture and 28/28 source/export bitwise-validation rows on both B200 and GB300.
- Reported cold-L2 CUPTI geometric-mean speedup over SGLang `route_radix` + `moe_align_block_size` is 1.416x on B200 and 1.753x on GB300 across those 28 shapes.

This delivers Shape B (K3 routing) for the supported batch sizes. Shape A (full H8 fused KDA decode), the optional TP12 LatentMoE tail, and end-to-end TP12 saturation validation remain separate work.


### yyihuang · 2026-09-25

Kimi K3 TP12 (`num_heads == 8`) fused KDA decode for SM100/SM103 is up as https://github.com/flashinfer-ai/flashinfer/pull/5551 (tracker #4254, Linear CAKE-619).

- `fused_kda_decode(..., backend="cake")` now admits H=8: FP32-state rows route to the existing wide512 / high-work kernels; BF16-state rows ≥64 go to a new persistent stream kernel (grid = min(rows·8, 3·SMs), grid-stride (row, head) items, 2×32 KiB `cp.async.cg` ring one item ahead).
- Measured with the Cake evaluation contract (CUDA-graph, cold-L2, CUPTI, interleaved pairing against this repo's `cute-dsl` fused decode with only its Python head check lifted): B200 geomean 1.112× (BF16 1.07–1.35×, FP32 rows ≥512 at 94–99 % of the same-node copy bandwidth), B300 geomean 1.108× (BF16 1.07–1.32×); vs the FLA Triton chain 7.35× / 5.18×. One FP32 row per GPU pairs at 0.9945× (latency-bound rows at parity); the rest are strictly faster.
- In-repo `benchmarks/bench_cake_fused_kda_decode.py --shapes h8 --state-dtype {bfloat16,float32}`: every shape faster on both GPUs; B200 BF16 geomean 1.204× (min 1.069×), FP32 1.036× (min 1.002×); B300 BF16 1.191× (min 1.051×), FP32 1.039× (min 1.004×).
- Tests: 210 CPU dispatch + 44 GPU tests pass on B200 and B300.

### yyihuang · 2026-09-25

Round-4 update on https://github.com/flashinfer-ai/flashinfer/pull/5551 (Kimi K3 TP12 `num_heads == 8`, Cake backend, SM100/SM103):

- New two-CTA cluster route for FP32-state positive-unique rows 1–9 (`cluster2_wide_positive_f32{,_wide_slot_offsets}`, `__cluster_dims__(2,1,1)`, launched through `cudaLaunchKernelExC`): one (row, head) item is split by value tile across the pair with a DSMEM exchange of the gated-RMSNorm sum of squares. It closes the last parity rows from the previous update.
- Cake evaluation contract (interleaved CUDA-graph cold-L2 CUPTI pairing vs this repo's `cute-dsl` fused decode with only the Python head check lifted, 34 shapes): B200 geomean 1.117×, min 1.001×, 34/34 shapes strictly faster; B300 geomean 1.117×, min 1.004×, 34/34 strictly faster. Cluster rows 1–8: 1.06–1.11× (B200) / 1.05–1.11× (B300).
- In-repo `benchmarks/bench_cake_fused_kda_decode.py --shapes h8`: every shape faster on both GPUs; B200 BF16 geomean 1.199× (min 1.058×), FP32 1.049× (min 1.002×); B300 BF16 1.192× (min 1.051×), FP32 1.055× (min 1.004×).
- Tests: 218 CPU dispatch + 47 GPU tests pass on B200 and B300 (`nvcr.io/nvidia/pytorch:26.01-py3`); synccheck and racecheck clean on 12 witnesses per GPU including the cluster route.


### yyihuang · 2026-09-25

@robin-fain [PR #5548](https://github.com/flashinfer-ai/flashinfer/pull/5548) was merged on 2026-09-25 (UTC), as a performance follow-up to the Cake Kimi-K3 fused router delivered in [PR #5531](https://github.com/flashinfer-ai/flashinfer/pull/5531).

- Removes a redundant per-thread device fence before the cooperative grid synchronization in the M256 and M512/M1024/M2048 routes on SM100/SM103. The grid join supplies the required release/acquire synchronization.
- Preserves the routing semantics, expert-aligned plans, public APIs, and supported shape set.
- The PR reports paired same-node improvements over the previous programs of about 3% at M256, 5–7% at M512, 5% at M1024, and 3–4% at M2048 on B200 and GB300.
- Validation reported in the PR includes 44 public tests per architecture, bitwise source/export parity on all 28 shapes per architecture, and passing synchronization/race sanitizer checks.

This is a performance follow-up for Shape B (K3 routing); the H8 fused KDA and TP12 LatentMoE-tail requests remain separate.


### yyihuang · 2026-09-25

Round-5 update on https://github.com/flashinfer-ai/flashinfer/pull/5551 (Kimi K3 TP12 `num_heads == 8`, Cake backend, SM100/SM103):

- New FP32 positive-unique route for rows 10–18 (`wide512_regcap128_positive_f32{,_wide_slot_offsets}`): the wide512 kernel built with `__launch_bounds__(512, 1)` so ptxas may use 128 registers per thread; while the (row, head) grid fits one CTA per SM the two-CTA cap buys nothing and the wider cap keeps more scattered slot loads in flight (B200, random 8192-slot pools, rows 10/14/16/18: 5.12/5.47/5.63/5.95 us vs 5.25/5.70/5.86/6.14 us).
- Cake evaluation contract (interleaved CUDA-graph cold-L2 CUPTI pairing vs this repo's `cute-dsl` fused decode with only the Python head check lifted, 34 shapes): B200 geomean 1.121×, min 1.0023× (`f32_rows1024`), 34/34 shapes strictly faster; B300 geomean 1.122×, min 1.0037× (`f32_rows4096`), 34/34 strictly faster. FP32 rows-16 serving shape: 1.103× (B200) / 1.061× (B300).
- In-repo `benchmarks/bench_cake_fused_kda_decode.py --shapes h8`: every shape faster on both GPUs; B200 BF16 geomean 1.200× (min 1.060×), FP32 1.059× (min 1.002×); B300 BF16 1.194× (min 1.063×), FP32 1.059× (min 1.004×).
- Tests: 222 CPU dispatch + 49 GPU tests pass on B200 and B300 (`nvcr.io/nvidia/pytorch:26.01-py3`); synccheck and racecheck clean on 13 witnesses per GPU including the new route.
- The remaining ~0.4 us of the two-CTA cluster route (rows 1–9) was attributed (0.13 us RMS exchange + 0.32 us deferred conv write-back) and four write-back variants stayed within noise; that form is unchanged.


### yyihuang · 2026-09-26

Round 6 of the Cake H=8 fused decode (tracker #4254, PR #5551 head `0d4a8055c`, Cake MR !906 head `0524f1794e8`), on the user's bar that every FP32 H=8 row in 10–37 must beat `cute-dsl` on both compact and random 8192-slot pools.

- Adopted: the FP32 `wide512` / 128-register 64-bit slot-offset twins now bind one pointer per CTA for the slot's state and conv cache and index with 32-bit offsets (their per-access 64-bit address arithmetic cost 0.4–0.5 us at two CTAs per SM). Random 8192-slot pools on B200, rows 19/20/24/28/32/37: 1.083/1.063/1.083/1.079/0.977/1.024× vs cute (rows 28 and 37 were 1.008–1.020× and 0.970–0.980×). Two sanitizer witnesses cover the twins on 8192-slot pools (15 witnesses, synccheck + racecheck clean on both GPUs).
- Closed with measurements (all oracle-correct): the 256-thread direct fallback, three orderings of the tile-0 state loads, a co-resident CTA stagger probe, and a TMA form staging the 64 KiB state tile through `cp.async.bulk` into shared memory (+1.5–2.5 us on both GPUs, largest at two CTAs per SM).
- Contract (34 shapes, paired CUPTI): B300 geomean 1.120×, min 1.0026×, 34/34 strictly faster; B200 geomean 1.122×, 33/34 — `f32_rows32` (compact pool) 0.996× / 0.997× in two samples (1.004× in round 5 with a byte-identical route). Mid-band matrices rows 10–37: B300 beats cute on every row and both pools (1.007–1.096×); B200 beats cute at rows 10–28 by 1.04–1.11× and pairs with it at rows 32–37 (0.975–1.027× across three samples) — the memory-system floor both kernels share. FlashInfer in-repo bench: every shape faster on both GPUs (B200 BF16 gm 1.201× / FP32 1.051×; B300 1.190× / 1.047×).

Evidence (host/path/size/SHA-256) is in the Cake design doc; merges are the owner's call.


### yyihuang · 2026-09-26

@robin-fain [PR #5551](https://github.com/flashinfer-ai/flashinfer/pull/5551) was merged on 2026-09-26 (UTC), delivering the Shape A Kimi-K3 TP12 fused KDA decode kernel.

- `fused_kda_decode(..., backend="cake")` now supports `H=8, D=128, T=1` on SM100/SM103 (B200/B300): width-4 causal convolution, SiLU, recurrent KDA update, and gated RMSNorm, with BF16 input/output and BF16 or FP32 recurrent state.
- Supports indexed state pools, batch-dependent dispatch, null/padded rows, and CUDA Graph replay. The PR reports 222 CPU dispatch tests and 49 GPU tests passing per architecture, plus clean synccheck/racecheck runs on 15 witnesses per GPU.
- The latest reported 34-shape cold-L2 CUPTI comparison against `cute-dsl` gives geometric-mean speedups of 1.122x on B200 and 1.120x on B300. B300 wins all 34 rows; B200 wins 33/34, with compact-pool `f32_rows32` near parity at 0.996x.

This delivers the single-step H=8 kernel boundary requested here. It does not add H=8 multi-token speculative decode or the optional TP12 LatentMoE tail, and kernel benchmarks do not establish full-model SGLang throughput saturation. The router candidate is covered separately by the earlier notifications.


### yyihuang · 2026-09-26

@robin-fain Merged: https://github.com/flashinfer-ai/flashinfer/pull/5564

This is a performance follow-up to #5531 / #5548 for **Shape B: Kimi-K3 routing**, targeting the largest supported batches on SM100/SM103 (B200/GB300).

- Optimizes the four combinations of `M = 4096 / 8192` and `block_m = 8 / 16` with warp-per-row top-16 selection and paired expert-segment sorting, using four CTAs per SM on both architectures.
- Preserves routing over FP32 `[M, 896]` logits: bias affects selection only, returned weights normalize the selected unbiased sigmoid scores, and ties prefer the lower expert ID. Expert-aligned route plans, public APIs, and the supported shape set are unchanged; the other 24 shape programs per architecture are unchanged.
- The PR reports source-side paired speedups over #5548 of **1.206–1.319x on B200** (geomean 1.266x) and **1.144–1.186x on GB300** (geomean 1.163x) across the four affected shapes. These are incremental kernel improvements over the previous Cake router.

Reported validation includes 44 package tests per architecture, bitwise source/export parity on all 28 shapes per architecture, and clean synccheck/racecheck runs.

This improves the router candidate for the specified batch sizes. Full-model throughput saturation, H8 KDA decode, and the optional TP12 LatentMoE tail are separate scopes.


### yyihuang · 2026-09-26

@robin-fain Merged: https://github.com/flashinfer-ai/flashinfer/pull/5568

This follows #5564 for **Shape B: Kimi-K3 routing** on SM100/SM103 (B200/GB300).

- Optimizes the 12 routed shapes with M = 256/512/1024/2048/4096/8192 and `block_m` = 8/16 using split cooperative barriers and, for the largest batches, a warp-level shortcut in the first radix-selection round.
- Preserves top-16 selection over 896 biased sigmoid scores, normalization of the selected unbiased weights, tie ordering, and expert-aligned route plans. APIs and the supported shape set are unchanged; the 16 smaller shape routes keep the same kernel logic.
- The PR reports paired kernel speedups over #5564 of approximately 1.057–1.061x geometric mean across the 12 affected shapes, with every changed row faster in both runs on each architecture.

Reported validation includes bitwise source/export parity on all 28 shapes per architecture, 44 package tests per architecture, and clean synccheck/racecheck runs.

This improves the router candidate. H8 KDA decode, the optional TP12 LatentMoE tail, and full-model throughput-saturation measurements remain separate scopes.
