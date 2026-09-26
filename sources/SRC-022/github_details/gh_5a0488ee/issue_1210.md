# [Issue #1210] Bandwidth Equations

source: https://github.com/ROCm/rccl/issues/1210
state: closed | updated: 2024-07-08T21:12:07Z
labels: 

## 正文

Hi Everyone,

I am going through the RCCL and learning how it predicts the best performance and protocol for a given coll. I am using a single node system with 4 MI300X GPUs. I ran an AllGather coll with these variables set: `NCCL_DEBUG=TRACE NCCL_DEBUG_FLAGS=TRACE NCCL_DEBUG_SUBSYS=ALL`. 

RCCL determines the BW of a XGMI link as 48GB/s. Detailed logs show the exact topology:

```

=== System : maxBw 48.0 totalBw 144.0 ===
…
XGMI[48.0]
…
==========================================
```

This 48 is coming from 

`ncclTopoXGMISpeed in rccl/src/graph/topo.h`

which considers the BW of 48GB/s for XGMI of all gfx94 devices. A quick look at [here](https://rocm.docs.amd.com/en/docs-6.0.2/reference/gpu-arch/gpu-arch-spec-overview.html) shows these are MI300A and MI300X devices. [MI300A platform](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300a-data-sheet.pdf) shows 64GB/s connectivity as well as 128GB/s bidirectional bandwidth of [MI300X platform](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/data-sheets/amd-instinct-mi300x-platform-data-sheet.pdf). So how is this 48GB/s calculated for gfx94 devices?

Best,
Alireza

## 评论 (3)

### gilbertlee-amd · 2024-07-02

Hi @arkhadem,

After protocol and error correction overheads, the max theoretical per-direction bandwidth for gfx94 devices is 48GB/s.  The 64GB/s you've pointed to is raw bandwidth.


### arkhadem · 2024-07-02

Thanks a lot for your insight.

The protocol bandwidth utilization depends on many factors. For example, if data is being transferred on only one direction of the XGMI, we should suppose that the bandwidth utilization is more than 75% (48GB/s) because no ack packet is being transferred on the opposite direction. Is this 75% utilization measured with both directions sending data and maximum coalescing (maximum number of payload flits in a packet) and utilization in the thread-level?

### gilbertlee-amd · 2024-07-08

Hi @arkhadem  - Yes.  the 75% assumes data being transferred in both directions.  If it were only one direction, we'd expect closer to 83.3%
