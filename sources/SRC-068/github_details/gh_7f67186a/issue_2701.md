# [Issue #2701] [FA4-FP8] on the B300. Low utilization of TC FMA XFU during inference.

source: https://github.com/Dao-AILab/flash-attention/issues/2701
state: closed | updated: 2026-07-16T08:04:02Z
labels: 

## 正文

Has anyone been paying attention to this issue? Running FP8 on the B300, the NCU profiling results show very low utilization of TC FMA XFU. Are there any ways to increase these and thus improve TFLOPS?

| Pipe | BF16 B200 | BF16 B300 | FP8 B200 | **FP8 B300** |
|---|---:|---:|---:|---:|
| Tensor | 87.7% | 99.9% | 43.6% | **55.2%** |
| XU/SFU (exp) | 71.9% | 50.3% | 71.6% | **55.7%** |
| FMA | 20.0% | 13.1% | 20.6% | **14.9%** |
| ALU | 31.2% | 31.0% | 36.3% | 40.8% |
| Issue | 49.2% | 46.3% | 52.0% | 54.6% |
| SM busy | 90.1% | 98.3% | 69.2% | **60.4%** |
| Occupancy | 23.4% | 23.4% | 23.4% | 23.4% |

## 评论 (2)

### Johnsonms · 2026-07-11

Thanks for the detailed writeup and NCU data! I reproduced this on a B300 (sm_103), and the behavior is expected.

The FP8 forward is not tensor-core bound. BF16 already saturates the tensor pipe (~99%), but FP8 roughly halves the GEMM time while the softmax path (exp2/MUFU, TMEM traffic, row reductions) is largely precision-independent. As a result, softmax becomes co-critical and tensor utilization naturally drops to ~55%, even though throughput still improves (~1880 → ~2460 TFLOP/s, ~1.3×).

The constant 23.4% occupancy is not the bottleneck—BF16 reaches ~99% tensor utilization at the same occupancy. This persistent, warp-specialized kernel is limited by on-chip resources (registers, shared memory, and TMEM), leaving essentially no headroom to increase occupancy or deepen the pipeline.

I also checked several tuning directions (ex2 emulation, register rebalancing, and TMEM/pipeline tradeoffs), but all were neutral or regressed performance. So this is a kernel-level limitation, not a configuration issue. Improving beyond this would require restructuring the softmax critical path rather than changing runtime knobs.

A concrete first step in that direction just landed: #2696 uses `tcgen05.ld.red` to compute the softmax row-max during the S TMEM load, removing the software reduction. On a B300 I measured ~+5–6% on the FP8 forward (growing with sequence length; ~1.32× → ~1.39× vs BF16), with BF16 unchanged and outputs bit-identical across SplitKV / paged / GQA. It doesn't close the gap to 2× on its own—exp2 and the S-load latency are still the co-limiter—but it's the right kind of change, and further softmax-overlap work along these lines is what it'll take.

One caveat: this analysis is for long-context prefill. If your workload is decode (e.g., seqlen_q=1 with a large KV cache), the bottleneck shifts to KV-cache bandwidth, so the conclusions are different.

### Johnsonms · 2026-07-14

@Romaosir If you think it makes sense, could we please close this issue?
