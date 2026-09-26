# [Issue #355] test deviceImpl And got error 'an illegal memory access was encountered'

source: https://github.com/NVIDIA/nccl-tests/issues/355
state: open | updated: 2025-10-31T07:58:29Z
labels: 

## 正文

I set `-D 1 -R 2 -V 24`


```shell
# nccl-tests version 2.17.6 nccl-headers=22807 nccl-library=22807
# Collective test starting: alltoall_perf
# nThread 1 nGpus 1 minBytes 2097152 maxBytes 2097152 step: 0(bytes) warmup iters: 0 iters: 1 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid  62767 on node0 device  0 [0000:19:00] NVIDIA H800
#  Rank  1 Group  0 Pid  62768 on node0 device  1 [0000:3b:00] NVIDIA H800
#  Rank  2 Group  0 Pid  62769 on node0 device  2 [0000:4c:00] NVIDIA H800
#  Rank  3 Group  0 Pid  62770 on node0 device  3 [0000:5d:00] NVIDIA H800
#  Rank  4 Group  0 Pid  62771 on node0 device  4 [0000:9b:00] NVIDIA H800
#  Rank  5 Group  0 Pid  62772 on node0 device  5 [0000:bb:00] NVIDIA H800
#  Rank  6 Group  0 Pid  62773 on node0 device  6 [0000:cb:00] NVIDIA H800
#  Rank  7 Group  0 Pid  62774 on node0 device  7 [0000:db:00] NVIDIA H800
#  Rank  8 Group  0 Pid  36788 on node1 device  0 [0000:19:00] NVIDIA H800
#  Rank  9 Group  0 Pid  36789 on node1 device  1 [0000:3b:00] NVIDIA H800
#  Rank 10 Group  0 Pid  36790 on node1 device  2 [0000:4c:00] NVIDIA H800
#  Rank 11 Group  0 Pid  36791 on node1 device  3 [0000:5d:00] NVIDIA H800
#  Rank 12 Group  0 Pid  36792 on node1 device  4 [0000:9b:00] NVIDIA H800
#  Rank 13 Group  0 Pid  36793 on node1 device  5 [0000:bb:00] NVIDIA H800
#  Rank 14 Group  0 Pid  36794 on node1 device  6 [0000:cb:00] NVIDIA H800
#  Rank 15 Group  0 Pid  36795 on node1 device  7 [0000:db:00] NVIDIA H800
NCCL version 2.28.7+cuda13.0
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw  #wrong     time   algbw   busbw  #wrong                     
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)             (us)  (GB/s)  (GB/s)                             
     2097152         32768     float    none      -1 node0: Test CUDA failure common.cu:389 'an illegal memory access was encountered'
 .. node0 pid 62767: Test failure common.cu:519
 .. node0 pid 62767: Test failure common.cu:532
 .. node0 pid 62767: Test failure common.cu:704
 .. node0 pid 62767: Test failure alltoall.cu:348
 .. node0 pid 62767: Test failure common.cu:718
 .. node0 pid 62767: Test failure common.cu:1368
```

## 评论 (5)

### AddyLaddy · 2025-10-30

I believe those first two A2A device kernels are limited to a single NVLink domain:

```
    case 1: // NvlAlltoAllKernel
    case 2: // NvlAlltoAllKernelOptimized
```

The GIN kernels are multi-domain capable:

```
    case 3: // GinAlltoAllKernel
    case 4: // HybridAlltoAllKernel (LSA+GIN)
```

@shanedsnyder Can you confirm my understanding?



### Qizhi697 · 2025-10-30

`-D 3 -R 2 -V 1`   |   `-D 3 -R 2 -V 16`
I have two machines, each equipped with `8 H100 GPUs` and `8 CX7` cards. When performing an `alltoall_perf` operation with `16 ranks` and a data size of `2M`, I observed that the bw with the `-V 1` parameter is `20 GB/s`, while the bw with the default  `-V 16` parameter is only `10 GB/s`. Is this reasonable? And how should I understand this?

### shanedsnyder · 2025-10-30

@AddyLaddy that is correct. For alltoall, kernels 1&2 rely on CUDA P2P connections between ranks, else you'll get IMA errors like in the original issue. Kernels 3&4 should work on multi-node (and also single node actually, using the NICs for comm instead of NVL, etc.).

### shanedsnyder · 2025-10-30

> I observed that the bw with the `-V 1` parameter is `20 GB/s`, while the bw with the default `-V 16` parameter is only `10 GB/s`. Is this reasonable? And how should I understand this?

@Qizhi697 a couple of things:

1. It is actually not an unexpected result that scaling CTAs (with -V param) results in lower performance here. This simple GIN kernel uses a single network context (and also a single signal), and piling more and more CTAs onto this context/signal will increase contention and slow things down. I've found that, in general, capping CTAs at the GIN context count gives best performance for GIN in most cases -- given that this kernel is hard-coded for a single context, using more than one CTA effectively has no benefit.
2. This simple GIN-only kernel (-D 3) will use the NICs for comm, even within the same node as other peers -- GIN does not internally have mechanisms that fallback to faster local transports for local peers. That will almost certainly limit your attained bandwidth compared to traditional alltoall implementation (-D 0) that knows to use e.g., NVL for local peers and network for remote peers. We do have a hybrid LSA+GIN kernel (-D 4) that should be much better by using GIN only for remote peers and using LSA for local peers -- it will still fall short of traditional host-based APIs as the LSA portion of the kernel is not currently optimized (we plan to do this in the future).

To address 1), we may offer a further optimized GIN kernel that uses more contexts by default (4), allowing you to use at least 4 CTAs effectively. It should deliver a bit better performance (especially at larger peer counts), but honestly this simple GIN kernel that we have now should still be very competitive performance-wise -- it turns out GIN doesn't need a ton of compute to push performance since most of the  data transfer is offloaded, it's more about managing contention for network resources (e.g., contexts).

### Qizhi697 · 2025-10-31

@shanedsnyder  Thank you for your detailed response.
Additionally, I tested the bandwidth bottleneck for large sizes(4G) and found that in 2-nodes(16 ranks) `alltoall_perf`, the CPU-proxy bandwidth can reach `80GB`, whereas GIN only reaches `50GB`. Is this result expected?
