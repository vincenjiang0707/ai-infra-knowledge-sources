# [Issue #2293] [Question]: Inconsistent busMultiplier for MC kernels: why 0.55*nRanks only for AllGather and ReduceScatter?

source: https://github.com/NVIDIA/nccl/issues/2293
state: open | updated: 2026-08-10T16:04:05Z
labels: question

## 正文

### Question

I noticed an inconsistency in the busBytes and busMultiplier assignments for different symmetric kernel types in the NCCL codebase.

For ncclSymkKernelId_AllReduce_AGxLL_R and ncclSymkKernelId_AllReduce_AGxLLMC_R, the busMultiplier is set to 1.1 for the MC variant to "beat non-MC LL":
```cpp
case ncclSymkKernelId_AllReduce_AGxLL_R:
    busBytes = nRanks * nBytes * LL_BusFactor;
    break;
case ncclSymkKernelId_AllReduce_AGxLLMC_R:
    busBytes = nRanks * nBytes * LL_BusFactor;
    busMultiplier = 1.1; // To beat non-MC LL
    break;
```

For ncclSymkKernelId_AllReduce_RSxLDMC_AGxSTMC, the busMultiplier is set to nRanks:
```C++
case ncclSymkKernelId_AllReduce_RSxLDMC_AGxSTMC:
    busBytes = nBytes / nRanks + nBytes;
    busMultiplier = nRanks;
    nMaxBlocks = nMaxBlocksNvls;
    break;
```

For ncclSymkKernelId_AllGather_LLMC and ncclSymkKernelId_ReduceScatter_LDMC, however, the busMultiplier is set to 0.55 * nRanks:
```c++
case ncclSymkKernelId_AllGather_TmaSTMC:
case ncclSymkKernelId_AllGather_STMC:
    busBytes = (nRanks - 1) * nBytes; // Wrong. Should be nRanks*nBytes but we want to beat non-MC.
    busMultiplier = 0.55 * nRanks;
    nMaxBlocks = nMaxBlocksNvls;
    break;

case ncclSymkKernelId_ReduceScatter_LDMC:
    busBytes = (nRanks - 1) * nBytes; // Wrong. Should be nRanks*nBytes but we want to beat non-MC.
    busMultiplier = 0.55 * nRanks;
    nMaxBlocks = nMaxBlocksNvls;
    break;
```
I'm trying to understand the rationale behind this design choice:

1. **Why does busMultiplier scale with nRanks for AllGather and ReduceScatter MC (0.55 * nRanks), but remains a constant (1.1) for the AllReduce AGxLLMC variant?** Both are MC kernels with similar "beat non-MC" goals.

2. **More importantly, why is there an internal inconsistency even within AllReduce itself?**

- AllReduce_AGxLLMC_R uses busMultiplier = 1.1.

- AllReduce_RSxLDMC_AGxSTMC uses busMultiplier = nRanks.
Given that both are AllReduce operations under the MC protocol, what fundamentally differentiates their cost models to justify this drastic difference (constant vs. linear in nRanks)?

3. **Where do the magic numbers 1.1 and 0.55 come from?** Are these empirically derived from micro-benchmarks on specific hardware (e.g., NVLink bandwidth, SM occupancy), or are they theoretical correction factors? Specifically for 0.55 * nRanks, if the effective bus traffic is busBytes * busMultiplier, that yields (nRanks - 1) * nBytes * 0.55 * nRanks, which seems to grow quadratically with nRanks. Is this intentionally modeling serialization overhead or shared resource contention on NVLS-capable hardware?

It would be extremely helpful if the maintainers could shed some light on the intended cost-model logic here, or point to any documentation that explains how these coefficients are calibrated for different algorithm/protocol combinations (AGxLLMC vs RSxLDMC_AGxSTMC, etc.).

Thank you!



## 评论 (3)

### xiaofanl-nvidia · 2026-07-19

@shenyt-sanshui 

To provide some general background, the current tuning for symmetric kernels is sometimes meaningful but sometimes based on heuristics so it could be difficult to explain. +CC @jbachan @KaimingOuyang to be aware of the user's questions in this area. But I'm not sure how much we want to fully explain everything right now. 

We are currently working on overhauling the symmetric kernel tuning in NCCL right now so this part of the code will see some changes in the near future. So your questions might be automatically answered (or become not relevant) in a couple of months.. 

### shenyt-sanshui · 2026-07-21

Hi @xiaofanl-nvidia, thank you very much for your quick and informative reply.

I completely understand that the current tuning for symmetric kernels is a mix of meaningful models and heuristics, and that a full explanation may not be straightforward at this point. I also appreciate the heads‑up that this part of the code is being overhauled – that certainly puts things into perspective.

That said, while I was studying the existing cost‑model logic, I formed three specific interpretations about how busMultiplier is chosen (using the figure in this issue as a reference). **I would be very grateful if you could just briefly confirm whether my understanding is broadly correct.**

Here are my understandings:

<img width="1325" height="583" alt="Image" src="https://github.com/user-attachments/assets/aebece09-6c80-418c-864e-193d2945588f" />


**1. For ncclSymkKernelId_AllReduce_RSxLDMC_AGxSTMC:**
  Each SM triggers `(1 + nRanks)` writes and `(1 + nRanks)` reads across the two stages, so the bus traffic(`busMultiplier`) is effectively scaled by `nRanks`.
 **The fact that it is not set to `nRanks + 1` seems to be a heuristic choice** – is that fair to say?

**2. For ncclSymkKernelId_ReduceScatter_LDMC (stage 1 in the figure):**
Each SM issues only 1 read but nRanks writes. The bottleneck is on the read side, so a discount factor (0.55) is applied to nRanks, even though writes do consume extra bandwidth. Again, this looks like a heuristic adjustment – is that correct?

**3. For the busMultiplier = 1.1 case** (e.g., AllReduce_AGxLLMC_R):
It appears to be purely a heuristic constant – also correct?

**So in all three scenarios, it seems that the busMultiplier values are ultimately determined by heuristics rather than a strictly analytical bus‑traffic model.** I just wanted to verify that I’m not misreading the intent behind these coefficients.

Thank you again for your time and for the overall context!




### keithc-nvi · 2026-08-10

> 1. For ncclSymkKernelId_AllReduce_RSxLDMC_AGxSTMC:
Each SM triggers (1 + nRanks) writes and (1 + nRanks) reads across the two stages, so the bus traffic(busMultiplier) is effectively scaled by nRanks.
The fact that it is not set to nRanks + 1 seems to be a heuristic choice – is that fair to say?

>2. For ncclSymkKernelId_ReduceScatter_LDMC (stage 1 in the figure):
Each SM issues only 1 read but nRanks writes. The bottleneck is on the read side, so a discount factor (0.55) is applied to nRanks, even though writes do consume extra bandwidth. Again, this looks like a heuristic adjustment – is that correct?

>3. For the busMultiplier = 1.1 case (e.g., AllReduce_AGxLLMC_R):
It appears to be purely a heuristic constant – also correct?

Yes, the model is not an exact replica of the NCCL implementation nor of the hardware, but a generalized model that is there to push NCCL in the correct direction when selecting which kernel to use.  Model freedoms are taken to get the model to do the right thing at the right time, like some of the options shown above, but this is an area of constant improvement as it is not easy to get the model to do everything at the right time for all platforms.  As @xiaofanl-nvidia said, a model overhead is in development so these will likely change in the coming releases. 
