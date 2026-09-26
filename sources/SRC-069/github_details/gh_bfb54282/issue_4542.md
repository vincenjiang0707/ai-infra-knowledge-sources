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

## 评论 (3)

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

