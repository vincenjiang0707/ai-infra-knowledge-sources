# [Issue #2421] ncclAlltoAllConfig does not honor per-call maxCTAs

source: https://github.com/NVIDIA/nccl/issues/2421
state: open | updated: 2026-09-21T00:07:52Z
labels: 

## 正文

`ncclAlltoAllConfig` launches more CTAs than the per-call `maxCTAs` limit.

Reproduced with a custom NCCL 2.31.2 build on two GB300 GPUs on one node, using 8 MiB per peer and ordinary `cudaMalloc` buffers. The same communicators were reused for all cases, without communicator-level CTA overrides.

The relevant call is:

```cpp
ncclCollConfig_t config = NCCL_COLLCONFIG_INITIALIZER;
config.CTAPolicy = NCCL_CTA_POLICY_DEFAULT;
config.maxCTAs = 1;

ncclAlltoAllConfig(send, recv, 2097152, ncclFloat, comm, stream, &config);
```

Expected: the A2A kernel respects `maxCTAs`.

Observed using CUPTI concurrent-kernel activity:

| Per-call maxCTAs | AllReduce CTAs/kernel (Ring control) | AlltoAll CTAs/kernel |
| --- | ---: | ---: |
| unset | 32 | 32 |
| 1 | 1 | 32 |
| 8 | 8 | 32 |
| 32 | 32 | 32 |

A2A launches one `ncclDevKernel_SendRecv` kernel per GPU per call. These are individual kernel grid sizes, not totals across ranks or calls. Each group contains one collective per GPU communicator.

The counts were consistent across three measured calls on both GPUs. All output validation passed, and CUPTI reported no dropped records.

Source inspection of public master at `12df1a11` suggests the same issue: A2A is lowered into P2P tasks, but [`p2pTaskAppend`](https://github.com/NVIDIA/nccl/blob/12df1a11afad322be5a204a2db890161cbf8131d/src/enqueue/enqueue.cc#L2687-L2700) does not carry over the CTA bounds. Master was not tested at runtime.


## 评论 (2)

### 0z5a · 2026-09-19

Hi @ngoyal2707 , I'd be happy to take a look at this if nobody is already working on it.

I can first reproduce the per-call maxCTAs behavior on a multi-GPU setup, then trace where the CTA bounds are lost when All-to-All is lowered into P2P tasks.

### xiaofanl-nvidia · 2026-09-21

++ @yfguo is looking at this from our side. I'll add him to your PR as well. @0z5a 
