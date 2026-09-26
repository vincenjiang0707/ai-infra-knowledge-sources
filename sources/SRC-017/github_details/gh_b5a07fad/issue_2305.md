# [Issue #2305] [Issue]: Blackwell symmetric ReduceScatter selects a slower launch

source: https://github.com/NVIDIA/nccl/issues/2305
state: open | updated: 2026-07-25T20:46:51Z
labels: 

## 正文

## How is this issue impacting you?

Lower performance than expected.

## Share Your Debug Logs

Nsight Systems shows one NCCL kernel per timed operation and no D2D or P2P payload copy:

```text
2 ranks, 2 MiB output/rank:
  current   ReduceScatter_LD,   11 CTAs x 512 threads
  faster    ReduceScatter_LD,   64 CTAs x 512 threads

4 ranks, 4 MiB output/rank:
  current   ReduceScatter_LDMC,  6 CTAs x 512 threads
  faster    ReduceScatter_LD,   64 CTAs x 512 threads
```

Raw `.nsys-rep` files, extracted launch/copy tables, topology, logs, and analysis scripts are available for maintainer review.

## Steps to Reproduce the Issue

Build NCCL `master` at `5067397c` and upstream `nccl-tests` at `a0b82b2`. `-R 2` allocates/registers symmetric windows. For ReduceScatter, `-b` is aggregate input, so output/rank is `input_bytes / ranks`.

```bash
# DP2: 2 MiB output/rank
./build/reduce_scatter_perf \
  -g 2 -R 2 -b 4M -e 4M -w 20 -n 100 -c 5 -d bfloat16 -o sum -x 0

NCCL_SYM_KERNEL=ReduceScatter_LD NCCL_SYM_CTAS=64 \
./build/reduce_scatter_perf \
  -g 2 -R 2 -b 4M -e 4M -w 20 -n 100 -c 5 -d bfloat16 -o sum -x 0

# DP4: 4 MiB output/rank
./build/reduce_scatter_perf \
  -g 4 -R 2 -b 16M -e 16M -w 20 -n 100 -c 5 -d bfloat16 -o sum -x 0

NCCL_SYM_KERNEL=ReduceScatter_LD NCCL_SYM_CTAS=64 \
./build/reduce_scatter_perf \
  -g 4 -R 2 -b 16M -e 16M -w 20 -n 100 -c 5 -d bfloat16 -o sum -x 0
```

Fresh out-of-place results:

| GPU | Ranks | Output/rank | Current | Forced existing LD64 | Prepared patch |
|---|---:|---:|---:|---:|---:|
| GB200 | 2 | 2 MiB | 33.12 us | 13.84 us | 13.79 us |
| GB200 | 4 | 4 MiB | 43.67 us | 31.98 us | 31.97 us |
| GB300 | 2 | 2 MiB | 32.74 us | 13.27 us | 13.40 us |
| GB300 | 4 | 4 MiB | 42.97 us | 31.71 us | 31.78 us |

This table is a quick BF16 upstream `nccl-tests` reproducer with one process controlling the local GPUs; `-c 5` requests five correctness-check iterations. Absolute timings are not directly comparable to the authoritative FP32 one-process-per-rank paired campaign in PR #2307.

All runs report zero wrong and zero out-of-bounds values. A separate one-process-per-rank campaign with six balanced allocations confirms the selection improvement with 95% confidence intervals excluding parity.

## NCCL Version

`2.30.7+cuda12.9`, public `master` commit `5067397c2676d5aed50042fc39e5c8ee96eb0027`.

## Your platform details

```text
GPUs:       NVIDIA GB200 (SM100) and NVIDIA GB300 (SM103)
Topology:   one Grace Blackwell node, 4 GPUs, NV18 between each GPU pair
Driver:     580.173.02
Container:  vllm/vllm-openai:v0.25.1-aarch64-cu129
Ranks:      2 or 4; reproduction uses one process controlling local GPUs
```

## Error Message & Behavior

There is no correctness error or NCCL warning. The default symmetric selector is slower than a manually selected existing symmetric launch and, at the DP2 gate on GB200, only reaches parity with ordinary Ring/LL after tuning.

The current LSA model predicts direct-load saturation with too few CTAs and uses an optimistic LDMC model at four ranks. Measurement on both GB200 and GB300 shows that LD continues scaling to 64 CTAs and overtakes LDMC at conservative crossovers:

```text
2 ranks: 2 MiB output/rank
4 ranks: 4 MiB output/rank
```

Implementation PR: #2307.

I prepared a host-side selector patch limited to one-node Blackwell, registered-input single-work ReduceScatter SUM under the default CTA policy. It uses raw bytes so scheduler-cell padding cannot activate a threshold early, and preserves explicit kernel/CTA settings, communicator CTA bounds, EFFICIENCY/ZERO, other rank counts/reductions, multi-work batches, and multi-node selection.

Would maintainers prefer this narrow measured correction, or a recalibration of the generic symmetric LSA model?

Related issues:

- #2280 asks about tuning symmetric kernels through `NCCL_SYM_CTAS`; the desired outcome here is an effective default rather than application-side tuning.
- #2293 discusses the symmetric multicast cost-model coefficients; this report provides measured Blackwell crossover data and a narrowly gated correction.

Concrete consumer: merged [vLLM #46703](https://github.com/vllm-project/vllm/pull/46703) adds opt-in NCCL symmetric AllGather/ReduceScatter for MoE dispatch/combine. This report makes a primitive-level NCCL claim, not an end-to-end vLLM claim.

## 评论 (1)

### xiaofanl-nvidia · 2026-07-25

++ @jbachan to review whether the comments above about the manual tuning could be helpful. 
++ @tarudoodi to take a look at the issue from tuning PoV. 
