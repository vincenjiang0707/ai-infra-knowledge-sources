# [Issue #590] Poor HybridEP performance on dual-node 16x B300 GPUs - IB bandwidth significantly lower than expected

source: https://github.com/deepseek-ai/DeepEP/issues/590
state: open | updated: 2026-04-28T09:53:37Z
labels: 

## 正文

I'm experiencing poor performance with HybridEP on a dual-node setup with 16 B300 GPUs (8 GPUs per node). The Roce bandwidth is significantly lower than expected, causing performance degradation in cross-node communication.

Environment
```yaml
Hardware: Dual-node setup, 16x NVIDIA B300 GPUs (8 GPUs per node)
Network: RoCE + NVLink (NVL) 
Test Configuration：
```
  Processes per node: 8
  Token size: 4096
  Local experts: 8
  Hidden size: 7168
  Node num: 2
  Nranks: 16
Performance Data

BF16 performance
Operation | NVL Bandwidth | IB Bandwidth | Ratio (IB/NVL)
-- | -- | -- | --
Dispatch (torch API) | ~13.6 GB/s | ~4.98 GB/s | 36.6%
Dispatch+permute | ~34.5 GB/s | ~12.6 GB/s | 36.5%
Combine (torch API) | ~133 GB/s | ~49 GB/s | 36.8%
Combine+unpermute | ~196 GB/s | ~71.8 GB/s | 36.6%
Dispatch kernel | ~160-282 GB/s | ~58-103 GB/s | ~36%
Combine kernel | ~234-245 GB/s | ~86-89 GB/s | ~37%

FP8 performance

Operation | NVL Bandwidth | IB Bandwidth | Ratio (IB/NVL)
-- | -- | -- | --
Dispatch (torch API) | ~66-69 GB/s | ~25 GB/s | ~37%
Dispatch+permute | ~65-69 GB/s | ~24.9 GB/s | ~37%
Combine (torch API) | ~201-212 GB/s | ~76.4 GB/s | ~37%
Combine+unpermute | ~101-107 GB/s | ~38.5 GB/s | ~37%
Dispatch kernel | ~78-133 GB/s | ~28-48 GB/s | ~37%
Combine kernel | ~264-286 GB/s | ~97-103 GB/s | ~37%


The HybridEP performance for EP 16 is much worse than DeepEP。During HybridEP running, there is no log except performance log。 how can I debug this issue ? 




## 评论 (2)

### alpha-baby · 2026-04-17

# EP 16 hybrid-ep performance

@Autumn1998 Could you please advise if the performance from my testing meets expectations? I tuned the configuration parameters, and this set currently appears to deliver the best performance.


env ：

```
"NUM_OF_TOKENS_PER_CHUNK_DISPATCH_API=64"
"NUM_OF_TOKENS_PER_CHUNK_COMBINE_API=64"
"NUM_OF_TOKENS_PER_CHUNK_PREPROCESSING_API=64"
"NUM_SMS_DISPATCH=24"
"NUM_SMS_COMBINE=24"
"NUM_BLOCKS_PERMUTE=124"
"NUM_BLOCKS_UNPERMUTE=124"
"CUDA_HOME=/usr/local/cuda"
"HIDDEN_DIM=7168"
"MAX_NUM_OF_TOKENS_PER_RANK=4096"
"NUM_TOKENS_PER_RANK=4096"
"NUM_LOCAL_EXPERTS=8"
"TOPK=8"
"NVSHMEM_DEBUG=WARN"
"NCCL_DEBUG=WARN"

```

```
MASTER_ADDR=xxxx MASTER_PORT=29500 WORLD_SIZE=2 RANK=0 NUM_OF_TOKENS_PER_CHUNK_DISPATCH_API=64 NUM_OF_TOKENS_PER_CHUNK_COMBINE_API=64 NUM_OF_TOKENS_PER_CHUNK_PREPROCESSING_API=64 NUM_SMS_DISPATCH=24 NUM_SMS_COMBINE=24 NUM_BLOCKS_PERMUTE=124 NUM_BLOCKS_UNPERMUTE=124 CUDA_HOME=/usr/local/cuda HIDDEN_DIM=7168 MAX_NUM_OF_TOKENS_PER_RANK=4096 NUM_TOKENS_PER_RANK=4096 NUM_LOCAL_EXPERTS=8 TOPK=8 NVSHMEM_DEBUG=WARN NCCL_DEBUG=WARN nohup python3 /root/hybrid-ep/tests/test_hybrid_ep.py --num-processes 8  > /tmp/bench_mark.txt 2>&1 &
```

```
dispatch kernel (BF16)(NVL):                     149.24 GB/s, avg_t=2638.9 us [min=2609.0, max=2671.0]
combine kernel(NVL):                             135.98 GB/s, avg_t=2896.4 us [min=2862.0, max=3111.0]
dispatch kernel (BF16)(RDMA):                    44.38 GB/s, avg_t=2638.9 us [min=2609.0, max=2671.0]
combine kernel(RDMA):                            40.43 GB/s, avg_t=2896.4 us [min=2862.0, max=3111.0]
dispatch (BF16):                                 136.54 GB/s (NVL), t: 2884.3 us [min=2884.1, max=2884.6], nvl_recv_bytes: 393.84 MB
dispatch (BF16):                                 40.60 GB/s (RDMA), t: 2884.3 us [min=2884.1, max=2884.6], rdma_send_bytes: 117.11 MB
combine:                                         128.92 GB/s (NVL), t: 3054.8 us [min=3054.6, max=3055.0], combine_send_bytes: 393.84 MB
combine:                                         38.34 GB/s (RDMA), t: 3054.8 us [min=3054.6, max=3055.0], rdma_recv_bytes: 117.11 MB
dispatch+permute (BF16):                         126.49 GB/s (NVL), t: 3113.6 us [min=3113.3, max=3113.8], nvl_recv_bytes: 393.84 MB
dispatch+permute (BF16):                         37.61 GB/s (RDMA), t: 3113.6 us [min=3113.3, max=3113.8], rdma_send_bytes: 117.11 MB
combine+unpermute:                               106.80 GB/s (NVL), t: 3687.6 us [min=3686.8, max=3687.9], combine_send_bytes: 393.84 MB
combine+unpermute:                               31.76 GB/s (RDMA), t: 3687.6 us [min=3686.8, max=3687.9], rdma_recv_bytes: 117.11 MB
fused dispatch+permute (BF16):                   123.63 GB/s (NVL), t: 3185.7 us [min=3185.5, max=3186.0], nvl_recv_bytes: 393.84 MB
fused dispatch+permute (BF16):                   36.76 GB/s (RDMA), t: 3185.7 us [min=3185.5, max=3186.0], rdma_send_bytes: 117.11 MB
fused combine+unpermute:                         128.32 GB/s (NVL), t: 3069.1 us [min=3068.8, max=3069.5], combine_send_bytes: 393.84 MB
fused combine+unpermute:                         38.16 GB/s (RDMA), t: 3069.1 us [min=3068.8, max=3069.5], rdma_recv_bytes: 117.11 MB

=== Kernel Benchmark (BF16, 16 ranks) ===
  Non-fused:  dispatch_kernel only  |  combine_kernel only
  Fused:      fused_permute_dispatch_kernel only  |  fused_combine_unpermute_kernel only
dispatch kernel (BF16)(NVL):                     149.24 GB/s, avg_t=2638.9 us [min=2609.0, max=2671.0]
combine kernel(NVL):                             135.98 GB/s, avg_t=2896.4 us [min=2862.0, max=3111.0]
dispatch kernel (BF16)(RDMA):                    44.38 GB/s, avg_t=2638.9 us [min=2609.0, max=2671.0]
combine kernel(RDMA):                            40.43 GB/s, avg_t=2896.4 us [min=2862.0, max=3111.0]
fused dispatch+permute kernel (BF16)(NVL):       147.96 GB/s, avg_t=2661.8 us [min=2649.0, max=2673.0]
fused combine+unpermute kernel(NVL):             130.83 GB/s, avg_t=3010.2 us [min=2943.0, max=3168.0]
fused dispatch+permute kernel (BF16)(RDMA):      44.00 GB/s, avg_t=2661.8 us [min=2649.0, max=2673.0]
fused combine+unpermute kernel(RDMA):            38.90 GB/s, avg_t=3010.2 us [min=2943.0, max=3168.0]

=== Correctness Check (FP8, 16 ranks) ===
  dispatch+combine API: PASS
  dispatch_with_permute + combine_with_unpermute API (non-fused): PASS
  dispatch_with_permute + combine_with_unpermute API (fused): PASS

=== Torch API Benchmark (FP8, 16 ranks) ===
  Non-permute:  dispatch = dispatch_kernel + d2d + misc
                combine  = d2d + combine_kernel + misc
  Permute:      dispatch = dispatch_kernel + permute_kernel + misc
                combine  = unpermute_kernel + combine_kernel + misc
  Fused:        dispatch = fused_permute_dispatch_kernel + misc
                combine  = fused_combine_unpermute_kernel + misc
  (misc = device_sync, update_flag, etc.)
dispatch (FP8):                                  119.64 GB/s (NVL), t: 1707.3 us [min=1707.1, max=1707.5], nvl_recv_bytes: 204.26 MB
dispatch (FP8):                                  35.38 GB/s (RDMA), t: 1707.3 us [min=1707.1, max=1707.5], rdma_send_bytes: 60.40 MB
combine:                                         119.84 GB/s (NVL), t: 3305.4 us [min=3305.2, max=3305.6], combine_send_bytes: 396.13 MB
combine:                                         18.27 GB/s (RDMA), t: 3305.4 us [min=3305.2, max=3305.6], rdma_recv_bytes: 60.40 MB
dispatch+permute (FP8):                          105.03 GB/s (NVL), t: 1944.7 us [min=1944.4, max=1945.4], nvl_recv_bytes: 204.26 MB
dispatch+permute (FP8):                          31.06 GB/s (RDMA), t: 1944.7 us [min=1944.4, max=1945.4], rdma_send_bytes: 60.40 MB
combine+unpermute:                               110.22 GB/s (NVL), t: 3594.0 us [min=3593.4, max=3594.3], combine_send_bytes: 396.13 MB
combine+unpermute:                               16.81 GB/s (RDMA), t: 3594.0 us [min=3593.4, max=3594.3], rdma_recv_bytes: 60.40 MB
fused dispatch+permute (FP8):                    119.36 GB/s (NVL), t: 1711.2 us [min=1711.0, max=1711.5], nvl_recv_bytes: 204.26 MB
fused dispatch+permute (FP8):                    35.30 GB/s (RDMA), t: 1711.2 us [min=1711.0, max=1711.5], rdma_send_bytes: 60.40 MB
fused combine+unpermute:                         121.03 GB/s (NVL), t: 3273.1 us [min=3272.8, max=3273.4], combine_send_bytes: 396.13 MB
fused combine+unpermute:                         18.45 GB/s (RDMA), t: 3273.1 us [min=3272.8, max=3273.4], rdma_recv_bytes: 60.40 MB

=== Kernel Benchmark (FP8, 16 ranks) ===
  Non-fused:  dispatch_kernel only  |  combine_kernel only
  Fused:      fused_permute_dispatch_kernel only  |  fused_combine_unpermute_kernel only
dispatch kernel (FP8)(NVL):                      143.47 GB/s, avg_t=1423.7 us [min=1420.0, max=1430.0]
combine kernel(NVL):                             136.18 GB/s, avg_t=2908.9 us [min=2853.0, max=3075.0]
dispatch kernel (FP8)(RDMA):                     42.43 GB/s, avg_t=1423.7 us [min=1420.0, max=1430.0]
combine kernel(RDMA):                            20.76 GB/s, avg_t=2908.9 us [min=2853.0, max=3075.0]
fused dispatch+permute kernel (FP8)(NVL):        139.93 GB/s, avg_t=1459.7 us [min=1453.0, max=1466.0]
fused combine+unpermute kernel(NVL):             131.87 GB/s, avg_t=3003.9 us [min=2908.0, max=3098.0]
fused dispatch+permute kernel (FP8)(RDMA):       41.38 GB/s, avg_t=1459.7 us [min=1453.0, max=1466.0]
fused combine+unpermute kernel(RDMA):            20.11 GB/s, avg_t=3003.9 us [min=2908.0, max=3098.0]

```

# my machine

B300 +   CX8 (800Gb/s)

```
root@gpulingjun010006136067:/tmp# nvidia-smi topo -m
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    NIC0    NIC1    NIC2    NIC3    NIC4    NIC5    NIC6    NIC7    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      NV18    NV18    NV18    NV18    NV18    NV18    NV18    PXB     NODE    NODE    NODE    SYS     SYS     SYS     SYS     0-63,128-191    0               N/A
GPU1    NV18     X      NV18    NV18    NV18    NV18    NV18    NV18    NODE    PXB     NODE    NODE    SYS     SYS     SYS     SYS     0-63,128-191    0               N/A
GPU2    NV18    NV18     X      NV18    NV18    NV18    NV18    NV18    NODE    NODE    PXB     NODE    SYS     SYS     SYS     SYS     0-63,128-191    0               N/A
GPU3    NV18    NV18    NV18     X      NV18    NV18    NV18    NV18    NODE    NODE    NODE    PXB     SYS     SYS     SYS     SYS     0-63,128-191    0               N/A
GPU4    NV18    NV18    NV18    NV18     X      NV18    NV18    NV18    SYS     SYS     SYS     SYS     PXB     NODE    NODE    NODE    64-127,192-255  1               N/A
GPU5    NV18    NV18    NV18    NV18    NV18     X      NV18    NV18    SYS     SYS     SYS     SYS     NODE    PXB     NODE    NODE    64-127,192-255  1               N/A
GPU6    NV18    NV18    NV18    NV18    NV18    NV18     X      NV18    SYS     SYS     SYS     SYS     NODE    NODE    PXB     NODE    64-127,192-255  1               N/A
GPU7    NV18    NV18    NV18    NV18    NV18    NV18    NV18     X      SYS     SYS     SYS     SYS     NODE    NODE    NODE    PXB     64-127,192-255  1               N/A
NIC0    PXB     NODE    NODE    NODE    SYS     SYS     SYS     SYS      X      NODE    NODE    NODE    SYS     SYS     SYS     SYS
NIC1    NODE    PXB     NODE    NODE    SYS     SYS     SYS     SYS     NODE     X      NODE    NODE    SYS     SYS     SYS     SYS
NIC2    NODE    NODE    PXB     NODE    SYS     SYS     SYS     SYS     NODE    NODE     X      NODE    SYS     SYS     SYS     SYS
NIC3    NODE    NODE    NODE    PXB     SYS     SYS     SYS     SYS     NODE    NODE    NODE     X      SYS     SYS     SYS     SYS
NIC4    SYS     SYS     SYS     SYS     PXB     NODE    NODE    NODE    SYS     SYS     SYS     SYS      X      NODE    NODE    NODE
NIC5    SYS     SYS     SYS     SYS     NODE    PXB     NODE    NODE    SYS     SYS     SYS     SYS     NODE     X      NODE    NODE
NIC6    SYS     SYS     SYS     SYS     NODE    NODE    PXB     NODE    SYS     SYS     SYS     SYS     NODE    NODE     X      NODE
NIC7    SYS     SYS     SYS     SYS     NODE    NODE    NODE    PXB     SYS     SYS     SYS     SYS     NODE    NODE    NODE     X 

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_bond_0
  NIC1: mlx5_bond_1
  NIC2: mlx5_bond_2
  NIC3: mlx5_bond_3
  NIC4: mlx5_bond_4
  NIC5: mlx5_bond_5
  NIC6: mlx5_bond_6
  NIC7: mlx5_bond_7
```

hybrid-ep version:

<img width="2702" height="2208" alt="Image" src="https://github.com/user-attachments/assets/f36b8bce-603d-4439-8ef2-632be75067bf" />

### Autumn1998 · 2026-04-28

The original hybrid EP implementation was not adapted for dual-port devices like CX8, so there will be performance issues. I believe your configuration is fine — this is purely a design issue with HEP. For this reason we introduced the nixl backend. We will fix these issues as soon as possible, and we sincerely apologize for any inconvenience caused
