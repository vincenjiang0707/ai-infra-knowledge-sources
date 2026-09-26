# [Issue #37] Intra-node compute-communication overlap without SM cores

source: https://github.com/deepseek-ai/DeepEP/issues/37
state: closed | updated: 2026-09-18T10:16:13Z
labels: 

## 正文

Hi,

Are you also doing compute communication overlap without SM cores in the intra-node case? I tried searching in your codebase but didn't find the implementation. Could you please clarify or point out the implementation to me?

Thanks!!

## 评论 (7)

### LyricZhao · 2025-03-04

We don't have an impl for **normal** intranode kernels, but you can try the **low-latency** kernels (with RDMA enabled, NVLink disabled, **one-node supported**).

We plan to support intranode low-latency NVLink protocol later, currently only RDMA is supported.

### rajagond · 2025-03-04

Thanks for the reply.

Additionally, why are you not doing that for prefill? Also, since decoding is memory-bound, wouldn't breaking it into two or more microbatches be inefficient?

### LyricZhao · 2025-03-04

> Additionally, why are you not doing that for prefill?

Because it is not doable with current impls. Prefill kernels require a lot of extra computation.

> Also, since decoding is memory-bound, wouldn't breaking it into two or more microbatches be inefficient?

Sorry, I don't understand your problem? Decoding kernels naturally support two-microbatch overlapping, and V3/R1 online services are compute-bound (attn and MoE). Which part do you think is memory-bound?

### LyricZhao · 2025-03-04

Ah, I understand it now. You can refer to the day-6 report of our open-source week. The batch size is 256, splitting into 2 microbatches of 128, making the system compute-bound for most of the kernels.

### rajagond · 2025-03-04

That makes sense. Deepseek-v3/R1 is large, so 256 seems sufficient.

### VincentHITlemon · 2025-03-07

> We plan to support intranode low-latency NVLink protocol later, currently only RDMA is supported.

@LyricZhao IIUC NVLINK latency should be lower than RDMA latency, so why is RDMA supported firstly instead of NVLINK? Is it the benefits of supporting NVLINK are not very obvious because most experts are distributed in different nodes?

### LyricZhao · 2025-03-07

The large EP (128-320) was decided at V3 design phase. With such number of EP ranks, NVLink is not reachable within a node but forwarding between RDMA and NVLink has no benefit. So only RDMA is needed (unless you only have 8 ranks with NVLink connected).
