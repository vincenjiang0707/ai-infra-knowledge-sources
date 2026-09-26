# [Issue #331] Intra-node NCCL P2P bandwidth on A100 with NVLink 3.0 limited to ~72 GB/s (vs 100 GB/s theoretical)

source: https://github.com/NVIDIA/nccl-tests/issues/331
state: open | updated: 2025-07-17T19:29:37Z
labels: 

## 正文

Hello,

We are benchmarking intra-node unidirectional peer-to-peer bandwidth using sendrecv_perf from NCCL Tests v2.16.4 on an NVIDIA A100-based system. Despite using GPUs connected via NVLink 3.0 (theoretically capable of 100 GB/s unidirectional), we only observe a maximum of ~71–73 GB/s bandwidth in the best case.

We’d like to understand if this performance is expected due to software or architectural limits, or if something is misconfigured in our environment.

We tested both transports:

- P2P/CUMEM
- P2P/direct

but results showed identical peak performance (~72–73 GB/s), even though we expected P2P/direct (which avoids memory staging) to be faster.

**Results**

```shell
# nThread 2 nGpus 1 minBytes 8 maxBytes 2147483648 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 4063850 on   lrdn2296 device  0 [0000:1d:00] NVIDIA A100-SXM-64GB
#  Rank  1 Group  0 Pid 4063850 on   lrdn2296 device  1 [0000:56:00] NVIDIA A100-SXM-64GB
lrdn2296:4063850:4063850 [0] NCCL INFO Bootstrap : Using ib0:10.128.42.1<0>
lrdn2296:4063850:4063850 [0] NCCL INFO cudaDriverVersion 12010
lrdn2296:4063850:4063850 [1] NCCL INFO NCCL version 2.22.3+cuda12.2
lrdn2296:4063850:4063871 [0] NCCL INFO NET/Plugin: Could not find: libnccl-net.so. Using internal network plugin.
lrdn2296:4063850:4063872 [1] NCCL INFO NET/Plugin: Could not find: libnccl-net.so. Using internal network plugin.
lrdn2296:4063850:4063871 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB [1]mlx5_1:1/IB [2]mlx5_2:1/IB [3]mlx5_3:1/IB [RO]; OOB ib0:10.128.42.1<0>
lrdn2296:4063850:4063871 [0] NCCL INFO Using network IB
lrdn2296:4063850:4063872 [1] NCCL INFO Using network IB
lrdn2296:4063850:4063872 [1] NCCL INFO ncclCommInitRank comm 0xb981910 rank 1 nranks 2 cudaDev 1 nvmlDev 1 busId 56000 commId 0xf6bfaf5466e2b71f - Init START
lrdn2296:4063850:4063871 [0] NCCL INFO ncclCommInitRank comm 0xb94bf80 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 1d000 commId 0xf6bfaf5466e2b71f - Init START
lrdn2296:4063850:4063871 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to NVL
lrdn2296:4063850:4063871 [0] NCCL INFO Setting affinity for GPU 0 to ffff
lrdn2296:4063850:4063872 [1] NCCL INFO Setting affinity for GPU 1 to ffff
lrdn2296:4063850:4063871 [0] NCCL INFO comm 0xb94bf80 rank 0 nRanks 2 nNodes 1 localRanks 2 localRank 0 MNNVL 0
lrdn2296:4063850:4063872 [1] NCCL INFO comm 0xb981910 rank 1 nRanks 2 nNodes 1 localRanks 2 localRank 1 MNNVL 0
lrdn2296:4063850:4063871 [0] NCCL INFO Channel 00/08 :    0   1
lrdn2296:4063850:4063871 [0] NCCL INFO Channel 01/08 :    0   1
lrdn2296:4063850:4063871 [0] NCCL INFO Channel 02/08 :    0   1
lrdn2296:4063850:4063871 [0] NCCL INFO Channel 03/08 :    0   1
lrdn2296:4063850:4063871 [0] NCCL INFO Channel 04/08 :    0   1
lrdn2296:4063850:4063871 [0] NCCL INFO Channel 05/08 :    0   1
lrdn2296:4063850:4063871 [0] NCCL INFO Channel 06/08 :    0   1
lrdn2296:4063850:4063872 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0 [2] 0/-1/-1->1->-1 [3] 0/-1/-1->1->-1 [4] -1/-1/-1->1->0 [5] -1/-1/-1->1->0 [6] 0/-1/-1->1->-1 [7] 0/-1/-1->1->-1
lrdn2296:4063850:4063871 [0] NCCL INFO Channel 07/08 :    0   1
lrdn2296:4063850:4063871 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1 [2] -1/-1/-1->0->1 [3] -1/-1/-1->0->1 [4] 1/-1/-1->0->-1 [5] 1/-1/-1->0->-1 [6] -1/-1/-1->0->1 [7] -1/-1/-1->0->1
lrdn2296:4063850:4063872 [1] NCCL INFO NCCL_BUFFSIZE set by environment to 4194304.
lrdn2296:4063850:4063872 [1] NCCL INFO P2P Chunksize set to 524288
lrdn2296:4063850:4063871 [0] NCCL INFO P2P Chunksize set to 524288
lrdn2296:4063850:4063872 [1] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
lrdn2296:4063850:4063872 [1] NCCL INFO 8 coll channels, 8 collnet channels, 0 nvls channels, 8 p2p channels, 8 p2p channels per peer
lrdn2296:4063850:4063871 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
lrdn2296:4063850:4063871 [0] NCCL INFO 8 coll channels, 8 collnet channels, 0 nvls channels, 8 p2p channels, 8 p2p channels per peer
lrdn2296:4063850:4063871 [0] NCCL INFO CC Off, Multi-GPU CC Off, workFifoBytes 1048576
lrdn2296:4063850:4063872 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so libnccl-net.so. Using internal tuner plugin.
lrdn2296:4063850:4063872 [1] NCCL INFO ncclCommInitRank comm 0xb981910 rank 1 nranks 2 cudaDev 1 nvmlDev 1 busId 56000 commId 0xf6bfaf5466e2b71f - Init COMPLETE
lrdn2296:4063850:4063872 [1] NCCL INFO Init timings: rank 1 nranks 2 total 0.06 (kernels 0.00, bootstrap 0.03, allgathers 0.00, topo 0.03, graphs 0.00, connections 0.00, rest 0.00)
lrdn2296:4063850:4063871 [0] NCCL INFO ncclCommInitRank comm 0xb94bf80 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 1d000 commId 0xf6bfaf5466e2b71f - Init COMPLETE
lrdn2296:4063850:4063871 [0] NCCL INFO Init timings: rank 0 nranks 2 total 0.06 (kernels 0.00, bootstrap 0.03, allgathers 0.00, topo 0.03, graphs 0.00, connections 0.00, rest 0.00)
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
lrdn2296:4063850:4063882 [0] NCCL INFO Channel 00/1 : 0[0] -> 1[1] via P2P/direct pointer/read
lrdn2296:4063850:4063882 [0] NCCL INFO Channel 01/1 : 0[0] -> 1[1] via P2P/direct pointer/read
lrdn2296:4063850:4063883 [1] NCCL INFO Channel 00/1 : 1[1] -> 0[0] via P2P/direct pointer/read
lrdn2296:4063850:4063882 [0] NCCL INFO Channel 02/1 : 0[0] -> 1[1] via P2P/direct pointer/read
lrdn2296:4063850:4063883 [1] NCCL INFO Channel 01/1 : 1[1] -> 0[0] via P2P/direct pointer/read
lrdn2296:4063850:4063882 [0] NCCL INFO Channel 03/1 : 0[0] -> 1[1] via P2P/direct pointer/read
lrdn2296:4063850:4063883 [1] NCCL INFO Channel 02/1 : 1[1] -> 0[0] via P2P/direct pointer/read
lrdn2296:4063850:4063882 [0] NCCL INFO Channel 04/1 : 0[0] -> 1[1] via P2P/direct pointer/read
lrdn2296:4063850:4063883 [1] NCCL INFO Channel 03/1 : 1[1] -> 0[0] via P2P/direct pointer/read
lrdn2296:4063850:4063882 [0] NCCL INFO Channel 05/1 : 0[0] -> 1[1] via P2P/direct pointer/read
lrdn2296:4063850:4063883 [1] NCCL INFO Channel 04/1 : 1[1] -> 0[0] via P2P/direct pointer/read
lrdn2296:4063850:4063882 [0] NCCL INFO Channel 06/1 : 0[0] -> 1[1] via P2P/direct pointer/read
lrdn2296:4063850:4063883 [1] NCCL INFO Channel 05/1 : 1[1] -> 0[0] via P2P/direct pointer/read
lrdn2296:4063850:4063882 [0] NCCL INFO Channel 07/1 : 0[0] -> 1[1] via P2P/direct pointer/read
lrdn2296:4063850:4063883 [1] NCCL INFO Channel 06/1 : 1[1] -> 0[0] via P2P/direct pointer/read
lrdn2296:4063850:4063883 [1] NCCL INFO Channel 07/1 : 1[1] -> 0[0] via P2P/direct pointer/read
           8             2     float     sum      -1     9.85    0.00    0.00      0     9.90    0.00    0.00    N/A
          16             4     float     sum      -1     9.76    0.00    0.00      0     9.87    0.00    0.00    N/A
          32             8     float     sum      -1     9.88    0.00    0.00      0    10.00    0.00    0.00    N/A
          64            16     float     sum      -1     9.86    0.01    0.01      0     9.94    0.01    0.01    N/A
         128            32     float     sum      -1     9.94    0.01    0.01      0     9.98    0.01    0.01    N/A
         256            64     float     sum      -1     9.96    0.03    0.03      0     9.90    0.03    0.03    N/A
         512           128     float     sum      -1    10.02    0.05    0.05      0     9.98    0.05    0.05    N/A
        1024           256     float     sum      -1    10.35    0.10    0.10      0     9.86    0.10    0.10    N/A
        2048           512     float     sum      -1    10.33    0.20    0.20      0    10.18    0.20    0.20    N/A
        4096          1024     float     sum      -1    11.07    0.37    0.37      0    10.78    0.38    0.38    N/A
        8192          2048     float     sum      -1    12.28    0.67    0.67      0    11.92    0.69    0.69    N/A
       16384          4096     float     sum      -1    13.08    1.25    1.25      0    12.82    1.28    1.28    N/A
       32768          8192     float     sum      -1    13.35    2.45    2.45      0    14.02    2.34    2.34    N/A
       65536         16384     float     sum      -1    15.66    4.18    4.18      0    14.34    4.57    4.57    N/A
      131072         32768     float     sum      -1    19.45    6.74    6.74      0    18.48    7.09    7.09    N/A
      262144         65536     float     sum      -1    24.17   10.85   10.85      0    28.11    9.32    9.32    N/A
      524288        131072     float     sum      -1    30.84   17.00   17.00      0    30.84   17.00   17.00    N/A
     1048576        262144     float     sum      -1    45.34   23.13   23.13      0    44.67   23.48   23.48    N/A
     2097152        524288     float     sum      -1    71.38   29.38   29.38      0    66.54   31.52   31.52    N/A
     4194304       1048576     float     sum      -1    108.9   38.50   38.50      0    99.41   42.19   42.19    N/A
     8388608       2097152     float     sum      -1    180.6   46.44   46.44      0    178.5   47.00   47.00    N/A
    16777216       4194304     float     sum      -1    330.2   50.81   50.81      0    335.3   50.03   50.03    N/A
    33554432       8388608     float     sum      -1    631.3   53.15   53.15      0    636.5   52.72   52.72    N/A
    67108864      16777216     float     sum      -1   1215.9   55.19   55.19      0   1218.8   55.06   55.06    N/A
   134217728      33554432     float     sum      -1   1833.5   73.20   73.20      0   1867.6   71.87   71.87    N/A
   268435456      67108864     float     sum      -1   3655.1   73.44   73.44      0   3635.9   73.83   73.83    N/A
   536870912     134217728     float     sum      -1   7460.2   71.97   71.97      0   7371.4   72.83   72.83    N/A
  1073741824     268435456     float     sum      -1    14892   72.10   72.10      0    14616   73.47   73.47    N/A
  2147483648     536870912     float     sum      -1    29935   71.74   71.74      0    29466   72.88   72.88    N/A
lrdn2296:4063850:4063850 [0] NCCL INFO comm 0xb94bf80 rank 0 nranks 2 cudaDev 0 busId 1d000 - Destroy COMPLETE
lrdn2296:4063850:4063850 [1] NCCL INFO comm 0xb981910 rank 1 nranks 2 cudaDev 1 busId 56000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 24.3607 
#
```


**Topology**

<details>
  <summary>Click me</summary>

```shell
nvidia-smi topo -m
        GPU0    GPU1    GPU2    GPU3    NIC0    NIC1    NIC2    NIC3    CPU Affinity    NUMA Affinity
GPU0     X      NV4     NV4     NV4     PXB     SYS     SYS     SYS     0       0-1
GPU1    NV4      X      NV4     NV4     SYS     PXB     SYS     SYS     0       0-1
GPU2    NV4     NV4      X      NV4     SYS     SYS     PXB     SYS     0       0-1
GPU3    NV4     NV4     NV4      X      SYS     SYS     SYS     PXB     0       0-1
NIC0    PXB     SYS     SYS     SYS      X      SYS     SYS     SYS
NIC1    SYS     PXB     SYS     SYS     SYS      X      SYS     SYS
NIC2    SYS     SYS     PXB     SYS     SYS     SYS      X      SYS
NIC3    SYS     SYS     SYS     PXB     SYS     SYS     SYS      X 

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_0
  NIC1: mlx5_1
  NIC2: mlx5_2
  NIC3: mlx5_3
```
</details>

## 评论 (2)

### sjeaugey · 2025-07-15

NVLink effective bandwidth is 20GB/s per NVLink. 25GB/s is wire-level speed, not accounting for overhead. So, your target should be 80GB/s.

On top of that, 2 GPUs performance always tends to be a bit under, so your numbers aren't that bad. You may want to try with NCCL_MIN_CTAS=8 to see if you get closer to 80 (just as an experiment, don't set that in production).

### mredenti · 2025-07-17

> NVLink effective bandwidth is 20GB/s per NVLink. 25GB/s is wire-level speed, not accounting for overhead. So, your target should be 80GB/s.
> 
> On top of that, 2 GPUs performance always tends to be a bit under, so your numbers aren't that bad. You may want to try with NCCL_MIN_CTAS=8 to see if you get closer to 80 (just as an experiment, don't set that in production).

I see, thank you @sjeaugey . Setting the env variable `NCCL_MIN_CTAS=8` does not improve the results. I will test the send recv on all 4 gpus next 
