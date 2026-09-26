# [Issue #4347] Qwen3-Next: sequential GDN paths (lax.scan recurrence, solve_triangular) bound TPU step time

source: https://github.com/AI-Hypercomputer/maxtext/issues/4347
state: open | updated: 2026-08-18T15:12:15Z
labels: 

## 正文

### Problem

In the Qwen3-Next Gated Delta Net (`jax_chunk_gated_delta_rule`), the two sequential computations dominate TPU step time:

- the inter-chunk recurrence runs as `lax.scan`, so the recurrent state round-trips HBM on every chunk step, and
- the UT-transform inverse `A = (I+S)^-1` uses `solve_triangular`, which substitutes row by row and barely uses the MXU.

Neither overlaps with other work, so they bound the step directly.

### Measurement

v5e-256, Qwen3-Next dense-8B config, seq 4096, bs 1, remat full (details in #4348):

| build | step time | tokens/s/device |
|---|---|---|
| main | 3.373s | 1,214 |
| #4348 (Pallas kernels) | **2.571s** | **1,593 (+31%)** |

Loss trajectories match to bf16 rounding level.


## 评论 (1)

### WandLZhang · 2026-08-18

Independent confirmation from a profile, on different hardware and a different config.

xplane capture, Qwen 3.5 dense 8B, v6e-8, sequence 8192, four steps at 2,548 ms each. `scan_layers` is on, so two `while` loops hold 98.8% of module time between them; those are the layer-scan wrapper and everything sits inside them. Op time with the wrapper excluded:

| Bucket | Share |
|---|---|
| fusions | 23.5% |
| matmul, the grouped-matmul MLP | 15.9% |
| **GatedDeltaNet state scan, `f32[1,32,128,128]`** | **11.9%** |
| layout and copies | 11.5% |
| other `while` loops | 7.8% |
| collectives | 5.1% |
| custom-call | 3.5% |
| splash attention | 2.7% |
| remainder, mostly broadcast and dynamic-update-slice | 18.1% |

Two things worth adding to the picture here.

**The step is matmul-starved.** A pure sharded bf16 matmul reaches 91.13% MFU on this hardware. 15.9% of the step in matmuls at 91.13% predicts 14.5% MFU, and the measured figure is 14.94%. The matmuls run near peak, so the headline MFU is set by how little of the step is matmul. Every millisecond the recurrence holds is a millisecond the MXU is idle.

**Attention is not competing for the time.** Splash is 2.7% at sequence 8192, because one layer in four is full attention. So the sequential paths you name are not being masked by anything.

Separately: #4348 measured +31% and was closed on 2026-08-14 by the stale bot after the CLA check went unsigned, not on technical grounds. Given the numbers above it looks worth reviving.

There may also be a second, cheaper lever. The inter-chunk recurrence is affine in the state:

```
h_new = exp(g_last) * h + k_g^T (u - w h) = (exp(g_last) I - k_g^T w) h + k_g^T u = A h + B
```

Affine maps compose associatively, so the scan is a prefix problem rather than a sequential one. I use that to shard the recurrence across devices in #4932, exact to 1.1e-08 against the stock scan. The same property should let `jax.lax.associative_scan` parallelise it within one device, without a custom kernel. I have not measured that and it would not beat a fused kernel on HBM traffic, but it is a much smaller change.

cc @mmcsa
