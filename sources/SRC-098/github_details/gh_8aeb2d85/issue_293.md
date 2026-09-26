# [Issue #293] It is not possible to determine whether this bandwidth value is normal.

source: https://github.com/NVIDIA/nccl-tests/issues/293
state: open | updated: 2025-03-11T02:49:23Z
labels: 

## 正文

Hello.

Let me inform you of the equipment information first.

Server: R7525
CPU:AMD EPYC 7352 24-Core Processor 2EA
MEM:256GB
GPU:A100 40GB PCIe 1EA
Compute Network : ConnectX6 HDR Infiniband adapter 1EA
PCI: Gen4

OS:ubuntu22.04
kernel:5.15.0-134-generic
nvidia-driver:550.54.14
CUDA tool kit:12.4
OFED:MLNX_OFED_LINUX-24.10-1.1.4.0 
NCCL:2.21.5-1+cuda12.4
HPC-X:hpcx-v2.18-gcc-mlnx_ofed-ubuntu22.04-cuda12-x86_64

topo
```
root@test1:/# nvidia-smi topo -m
        GPU0    GPU1    NIC0    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      SYS     SYS     24-47,72-95     1               N/A
GPU1    SYS      X      SYS     24-47,72-95     1               N/A
NIC0    SYS     SYS      X

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
```

We are conducting an nccl-test with the two equipment above, but the bandwidth is not coming out as well as I thought.
```
root@test1:/# mpirun --allow-run-as-root -np 2 -H 192.168.160.111:1,192.168.160.112:1 --bind-to socket -x NCCL_DEBUG=INFO -x NCCL_NET_GDR_LEVEL=SYS -x NCCL_SHM_DISABLE=1 -x LD_LIBRARY_PATH  /nccl-tests/build/all_reduce_perf -b 8 -e 1G -f 2 -g 1
# nThread 1 nGpus 1 minBytes 8 maxBytes 1073741824 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid   5425 on      test1 device  0 [0x81] NVIDIA A100-PCIE-40GB
#  Rank  1 Group  0 Pid   4962 on      test2 device  0 [0x81] NVIDIA A100-PCIE-40GB
test1:5425:5425 [0] NCCL INFO Bootstrap : Using eno1:192.168.160.111<0>
test1:5425:5425 [0] NCCL INFO cudaDriverVersion 12040
NCCL version 2.21.5+cuda12.4
test2:4962:4962 [0] NCCL INFO cudaDriverVersion 12040
test2:4962:4962 [0] NCCL INFO Bootstrap : Using eno1:192.168.160.112<0>
test1:5425:5439 [0] NCCL INFO Plugin Path : /hpcx-v2.18-gcc-mlnx_ofed-ubuntu22.04-cuda12-x86_64/nccl_rdma_sharp_plugin/lib/libnccl-net.so
test1:5425:5439 [0] NCCL INFO P2P plugin IBext_v8
test2:4962:4975 [0] NCCL INFO Plugin Path : /hpcx-v2.18-gcc-mlnx_ofed-ubuntu22.04-cuda12-x86_64/nccl_rdma_sharp_plugin/lib/libnccl-net.so
test2:4962:4975 [0] NCCL INFO P2P plugin IBext_v8
test1:5425:5439 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB/SHARP [RO]; OOB eno1:192.168.160.111<0>
test1:5425:5439 [0] NCCL INFO Using non-device net plugin version 0
test1:5425:5439 [0] NCCL INFO Using network IBext_v8
test2:4962:4975 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB/SHARP [RO]; OOB eno1:192.168.160.112<0>
test2:4962:4975 [0] NCCL INFO Using non-device net plugin version 0
test2:4962:4975 [0] NCCL INFO Using network IBext_v8
test1:5425:5439 [0] NCCL INFO DMA-BUF is available on GPU device 0
test1:5425:5439 [0] NCCL INFO ncclCommInitRank comm 0x563a62844c90 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0x4f7e9367046f0f0 - Init START
test2:4962:4975 [0] NCCL INFO ncclCommInitRank comm 0x55629db45410 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0x4f7e9367046f0f0 - Init START
test1:5425:5439 [0] NCCL INFO comm 0x563a62844c90 rank 0 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
test1:5425:5439 [0] NCCL INFO Channel 00/02 :    0   1
test1:5425:5439 [0] NCCL INFO Channel 01/02 :    0   1
test1:5425:5439 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1
test1:5425:5439 [0] NCCL INFO P2P Chunksize set to 131072
test2:4962:4975 [0] NCCL INFO comm 0x55629db45410 rank 1 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
test2:4962:4975 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1
test2:4962:4975 [0] NCCL INFO P2P Chunksize set to 131072
test1:5425:5439 [0] NCCL INFO NCCL_SHM_DISABLE set by environment to 1.
test1:5425:5439 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to SYS
test2:4962:4975 [0] NCCL INFO NCCL_SHM_DISABLE set by environment to 1.
test2:4962:4975 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to SYS
test1:5425:5439 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [receive] via NET/IBext_v8/0/GDRDMA
test1:5425:5439 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [receive] via NET/IBext_v8/0/GDRDMA
test2:4962:4975 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [receive] via NET/IBext_v8/0/GDRDMA
test1:5425:5439 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [send] via NET/IBext_v8/0/GDRDMA
test2:4962:4975 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [receive] via NET/IBext_v8/0/GDRDMA
test1:5425:5439 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [send] via NET/IBext_v8/0/GDRDMA
test2:4962:4975 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [send] via NET/IBext_v8/0/GDRDMA
test2:4962:4975 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [send] via NET/IBext_v8/0/GDRDMA
test1:5425:5439 [0] NCCL INFO Connected all rings
test1:5425:5439 [0] NCCL INFO Connected all trees
test1:5425:5439 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
test1:5425:5439 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
test2:4962:4975 [0] NCCL INFO Connected all rings
test2:4962:4975 [0] NCCL INFO Connected all trees
test2:4962:4975 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
test2:4962:4975 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
test2:4962:4975 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2, using internal tuner instead.
test2:4962:4975 [0] NCCL INFO ncclCommInitRank comm 0x55629db45410 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0x4f7e9367046f0f0 - Init COMPLETE
test1:5425:5439 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2, using internal tuner instead.
test1:5425:5439 [0] NCCL INFO ncclCommInitRank comm 0x563a62844c90 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0x4f7e9367046f0f0 - Init COMPLETE
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
           8             2     float     sum      -1    17.08    0.00    0.00      0    16.76    0.00    0.00      0
          16             4     float     sum      -1    16.72    0.00    0.00      0    16.66    0.00    0.00      0
          32             8     float     sum      -1    16.84    0.00    0.00      0    16.88    0.00    0.00      0
          64            16     float     sum      -1    17.04    0.00    0.00      0    16.83    0.00    0.00      0
         128            32     float     sum      -1    17.31    0.01    0.01      0    17.43    0.01    0.01      0
         256            64     float     sum      -1    17.72    0.01    0.01      0    17.44    0.01    0.01      0
         512           128     float     sum      -1    18.30    0.03    0.03      0    19.42    0.03    0.03      0
        1024           256     float     sum      -1    19.97    0.05    0.05      0    19.67    0.05    0.05      0
        2048           512     float     sum      -1    20.24    0.10    0.10      0    20.13    0.10    0.10      0
        4096          1024     float     sum      -1    22.76    0.18    0.18      0    22.61    0.18    0.18      0
        8192          2048     float     sum      -1    28.66    0.29    0.29      0    30.11    0.27    0.27      0
       16384          4096     float     sum      -1    42.29    0.39    0.39      0    44.71    0.37    0.37      0
       32768          8192     float     sum      -1    82.71    0.40    0.40      0    84.63    0.39    0.39      0
       65536         16384     float     sum      -1    183.1    0.36    0.36      0    196.2    0.33    0.33      0
      131072         32768     float     sum      -1    392.0    0.33    0.33      0    393.4    0.33    0.33      0
      262144         65536     float     sum      -1    786.1    0.33    0.33      0    807.0    0.32    0.32      0
      524288        131072     float     sum      -1   1666.7    0.31    0.31      0   1649.9    0.32    0.32      0
     1048576        262144     float     sum      -1   3332.3    0.31    0.31      0   3392.5    0.31    0.31      0
     2097152        524288     float     sum      -1    365.5    5.74    5.74      0    365.2    5.74    5.74      0
     4194304       1048576     float     sum      -1    686.3    6.11    6.11      0    687.8    6.10    6.10      0
     8388608       2097152     float     sum      -1   1332.9    6.29    6.29      0   1323.5    6.34    6.34      0
    16777216       4194304     float     sum      -1   2619.1    6.41    6.41      0   2640.6    6.35    6.35      0
    33554432       8388608     float     sum      -1   5218.2    6.43    6.43      0   5234.4    6.41    6.41      0
    67108864      16777216     float     sum      -1    10442    6.43    6.43      0    10466    6.41    6.41      0
   134217728      33554432     float     sum      -1    20889    6.43    6.43      0    20910    6.42    6.42      0
   268435456      67108864     float     sum      -1    41747    6.43    6.43      0    41808    6.42    6.42      0
   536870912     134217728     float     sum      -1    83359    6.44    6.44      0    83576    6.42    6.42      0
  1073741824     268435456     float     sum      -1   166733    6.44    6.44      0   167090    6.43    6.43      0
test2:4962:4962 [0] NCCL INFO comm 0x55629db45410 rank 1 nranks 2 cudaDev 0 busId 81000 - Destroy COMPLETE
test1:5425:5425 [0] NCCL INFO comm 0x563a62844c90 rank 0 nranks 2 cudaDev 0 busId 81000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 2.36313
#
```

Is there a way for bandwidth to come out better?


## 评论 (6)

### sjeaugey · 2025-03-07

Why are you setting:
```
NCCL_NET_GDR_LEVEL=SYS
NCCL_SHM_DISABLE=1
```

What is the performance you get if you unset those two variables?

### gim4moon · 2025-03-07

> Why are you setting:
> 
> ```
> NCCL_NET_GDR_LEVEL=SYS
> NCCL_SHM_DISABLE=1
> ```
> 
> What is the performance you get if you unset those two variables?

NCCL_SHM_DISABLE=1 <- Setting this variable doesn't make much difference compared to not setting it. Someone recommended it to me.

NCCL_NET_GDR_LEVEL=SYS <- If you don't set this variable, the bandwidth will only be a maximum of 1.1GB/s.

```
root@test1:/# mpirun --allow-run-as-root -np 2 -H 192.168.160.111:1,192.168.160.112:1 --bind-to socket -x NCCL_DEBUG=INFO -x LD_LIBRARY_PATH  /nccl-tests/build/all_reduce_perf -b 8 -e 1G -f 2 -g 1
# nThread 1 nGpus 1 minBytes 8 maxBytes 1073741824 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid   3521 on      test1 device  0 [0x81] NVIDIA A100-PCIE-40GB
#  Rank  1 Group  0 Pid   3985 on      test2 device  0 [0x81] NVIDIA A100-PCIE-40GB
test1:3521:3521 [0] NCCL INFO Bootstrap : Using eno1:192.168.160.111<0>
test1:3521:3521 [0] NCCL INFO cudaDriverVersion 12040
NCCL version 2.21.5+cuda12.4
test2:3985:3985 [0] NCCL INFO cudaDriverVersion 12040
test2:3985:3985 [0] NCCL INFO Bootstrap : Using eno1:192.168.160.112<0>
test1:3521:3535 [0] NCCL INFO Plugin Path : /hpcx-v2.18-gcc-mlnx_ofed-ubuntu22.04-cuda12-x86_64/nccl_rdma_sharp_plugin/lib/libnccl-net.so
test1:3521:3535 [0] NCCL INFO P2P plugin IBext_v8
test2:3985:3998 [0] NCCL INFO Plugin Path : /hpcx-v2.18-gcc-mlnx_ofed-ubuntu22.04-cuda12-x86_64/nccl_rdma_sharp_plugin/lib/libnccl-net.so
test2:3985:3998 [0] NCCL INFO P2P plugin IBext_v8
test1:3521:3535 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB/SHARP [RO]; OOB eno1:192.168.160.111<0>
test1:3521:3535 [0] NCCL INFO Using non-device net plugin version 0
test1:3521:3535 [0] NCCL INFO Using network IBext_v8
test2:3985:3998 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB/SHARP [RO]; OOB eno1:192.168.160.112<0>
test2:3985:3998 [0] NCCL INFO Using non-device net plugin version 0
test2:3985:3998 [0] NCCL INFO Using network IBext_v8
test1:3521:3535 [0] NCCL INFO DMA-BUF is available on GPU device 0
test1:3521:3535 [0] NCCL INFO ncclCommInitRank comm 0x55679c1b4e20 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0xba13681239d5afb7 - Init START
test2:3985:3998 [0] NCCL INFO ncclCommInitRank comm 0x55d9c8671e40 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0xba13681239d5afb7 - Init START
test1:3521:3535 [0] NCCL INFO comm 0x55679c1b4e20 rank 0 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
test1:3521:3535 [0] NCCL INFO Channel 00/02 :    0   1
test1:3521:3535 [0] NCCL INFO Channel 01/02 :    0   1
test1:3521:3535 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1
test1:3521:3535 [0] NCCL INFO P2P Chunksize set to 131072
test2:3985:3998 [0] NCCL INFO comm 0x55d9c8671e40 rank 1 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
test2:3985:3998 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1
test2:3985:3998 [0] NCCL INFO P2P Chunksize set to 131072
test2:3985:3998 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [receive] via NET/IBext_v8/0
test1:3521:3535 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [receive] via NET/IBext_v8/0
test2:3985:3998 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [receive] via NET/IBext_v8/0
test1:3521:3535 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [receive] via NET/IBext_v8/0
test2:3985:3998 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [send] via NET/IBext_v8/0
test1:3521:3535 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [send] via NET/IBext_v8/0
test2:3985:3998 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [send] via NET/IBext_v8/0
test1:3521:3535 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [send] via NET/IBext_v8/0
test1:3521:3535 [0] NCCL INFO Connected all rings
test1:3521:3535 [0] NCCL INFO Connected all trees
test1:3521:3535 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
test1:3521:3535 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
test2:3985:3998 [0] NCCL INFO Connected all rings
test2:3985:3998 [0] NCCL INFO Connected all trees
test2:3985:3998 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
test2:3985:3998 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
test1:3521:3535 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2, using internal tuner instead.
test1:3521:3535 [0] NCCL INFO ncclCommInitRank comm 0x55679c1b4e20 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0xba13681239d5afb7 - Init COMPLETE
```

![Image](https://github.com/user-attachments/assets/898c31e0-bd81-4650-be7c-83e120ae82c3)

### sjeaugey · 2025-03-07

Oh, I missed you were running with 2 GPUs on different nodes. Then indeed `NCCL_SHM_DISABLE=1` won't make any difference.

Regarding the 1.1GB/s performance without GDR, that is usually due to your CPU being configured with one Numa domain Per Socket (NPS=1) in the BIOS. You should set NPS to 4, hopefully performance will be much better, with default settings.

### gim4moon · 2025-03-08

> Oh, I missed you were running with 2 GPUs on different nodes. Then indeed `NCCL_SHM_DISABLE=1` won't make any difference.
> 
> Regarding the 1.1GB/s performance without GDR, that is usually due to your CPU being configured with one Numa domain Per Socket (NPS=1) in the BIOS. You should set NPS to 4, hopefully performance will be much better, with default settings.

Thank you. When I set NUMA Nodes Per Socket to 4 in Dell Bios Processor Setting as instructed and ran TEST, I got up to 9GB/s.

```
root@test1:/hpcx-v2.18-gcc-mlnx_ofed-ubuntu22.04-cuda12-x86_64# mpirun --allow-run-as-root -np 2 -H 192.168.160.111:1,192.168.160.112:1 --bind-to numa -x NCCL_DEBUG=INFO -x NCCL_NET_GDR_LEVEL=2 -x NCCL_SHM_DISABLE=1 -x LD_LIBRARY_PATH  /nccl-tests/build/all_reduce_perf -b 8 -e 1G -f 2 -g 1
# nThread 1 nGpus 1 minBytes 8 maxBytes 1073741824 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid   3595 on      test1 device  0 [0x81] NVIDIA A100-PCIE-40GB
#  Rank  1 Group  0 Pid   4017 on      test2 device  0 [0x81] NVIDIA A100-PCIE-40GB
test1:3595:3595 [0] NCCL INFO Bootstrap : Using eno1:192.168.160.111<0>
test1:3595:3595 [0] NCCL INFO cudaDriverVersion 12040
NCCL version 2.21.5+cuda12.4
test2:4017:4017 [0] NCCL INFO cudaDriverVersion 12040
test2:4017:4017 [0] NCCL INFO Bootstrap : Using eno1:192.168.160.112<0>
test1:3595:3609 [0] NCCL INFO Plugin Path : /hpcx-v2.18-gcc-mlnx_ofed-ubuntu22.04-cuda12-x86_64/nccl_rdma_sharp_plugin/lib/libnccl-net.so
test1:3595:3609 [0] NCCL INFO P2P plugin IBext_v8
test2:4017:4030 [0] NCCL INFO Plugin Path : /hpcx-v2.18-gcc-mlnx_ofed-ubuntu22.04-cuda12-x86_64/nccl_rdma_sharp_plugin/lib/libnccl-net.so
test2:4017:4030 [0] NCCL INFO P2P plugin IBext_v8
test2:4017:4030 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB/SHARP [RO]; OOB eno1:192.168.160.112<0>
test2:4017:4030 [0] NCCL INFO Using non-device net plugin version 0
test2:4017:4030 [0] NCCL INFO Using network IBext_v8
test1:3595:3609 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/IB/SHARP [RO]; OOB eno1:192.168.160.111<0>
test1:3595:3609 [0] NCCL INFO Using non-device net plugin version 0
test1:3595:3609 [0] NCCL INFO Using network IBext_v8
test1:3595:3609 [0] NCCL INFO DMA-BUF is available on GPU device 0
test1:3595:3609 [0] NCCL INFO ncclCommInitRank comm 0x55a347241ed0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0x6dbf75e027b52dc1 - Init START
test2:4017:4030 [0] NCCL INFO ncclCommInitRank comm 0x563a8a2c7400 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0x6dbf75e027b52dc1 - Init START
test1:3595:3609 [0] NCCL INFO comm 0x55a347241ed0 rank 0 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
test1:3595:3609 [0] NCCL INFO Channel 00/02 :    0   1
test1:3595:3609 [0] NCCL INFO Channel 01/02 :    0   1
test1:3595:3609 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1
test1:3595:3609 [0] NCCL INFO P2P Chunksize set to 131072
test2:4017:4030 [0] NCCL INFO comm 0x563a8a2c7400 rank 1 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
test2:4017:4030 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1
test2:4017:4030 [0] NCCL INFO P2P Chunksize set to 131072
test1:3595:3609 [0] NCCL INFO NCCL_SHM_DISABLE set by environment to 1.
test1:3595:3609 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to PXB
test2:4017:4030 [0] NCCL INFO NCCL_SHM_DISABLE set by environment to 1.
test2:4017:4030 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to PXB
test1:3595:3609 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [receive] via NET/IBext_v8/0
test1:3595:3609 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [receive] via NET/IBext_v8/0
test1:3595:3609 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [send] via NET/IBext_v8/0
test1:3595:3609 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [send] via NET/IBext_v8/0
test2:4017:4030 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[0] [receive] via NET/IBext_v8/0
test2:4017:4030 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[0] [receive] via NET/IBext_v8/0
test2:4017:4030 [0] NCCL INFO Channel 00/0 : 1[0] -> 0[0] [send] via NET/IBext_v8/0
test2:4017:4030 [0] NCCL INFO Channel 01/0 : 1[0] -> 0[0] [send] via NET/IBext_v8/0
test1:3595:3609 [0] NCCL INFO Connected all rings
test1:3595:3609 [0] NCCL INFO Connected all trees
test1:3595:3609 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
test1:3595:3609 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
test2:4017:4030 [0] NCCL INFO Connected all rings
test2:4017:4030 [0] NCCL INFO Connected all trees
test2:4017:4030 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
test2:4017:4030 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
test2:4017:4030 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2, using internal tuner instead.
test2:4017:4030 [0] NCCL INFO ncclCommInitRank comm 0x563a8a2c7400 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0x6dbf75e027b52dc1 - Init COMPLETE
test1:3595:3609 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2, using internal tuner instead.
test1:3595:3609 [0] NCCL INFO ncclCommInitRank comm 0x55a347241ed0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 81000 commId 0x6dbf75e027b52dc1 - Init COMPLETE
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
           8             2     float     sum      -1    17.59    0.00    0.00      0    17.03    0.00    0.00      0
          16             4     float     sum      -1    17.21    0.00    0.00      0    17.07    0.00    0.00      0
          32             8     float     sum      -1    17.38    0.00    0.00      0    17.38    0.00    0.00      0
          64            16     float     sum      -1    17.27    0.00    0.00      0    17.25    0.00    0.00      0
         128            32     float     sum      -1    17.94    0.01    0.01      0    27.34    0.00    0.00      0
         256            64     float     sum      -1    34.31    0.01    0.01      0    17.93    0.01    0.01      0
         512           128     float     sum      -1    18.31    0.03    0.03      0    18.31    0.03    0.03      0
        1024           256     float     sum      -1    18.88    0.05    0.05      0    18.99    0.05    0.05      0
        2048           512     float     sum      -1    19.66    0.10    0.10      0    20.27    0.10    0.10      0
        4096          1024     float     sum      -1    22.37    0.18    0.18      0    22.33    0.18    0.18      0
        8192          2048     float     sum      -1    25.26    0.32    0.32      0    24.93    0.33    0.33      0
       16384          4096     float     sum      -1    29.56    0.55    0.55      0    29.01    0.56    0.56      0
       32768          8192     float     sum      -1    34.17    0.96    0.96      0    35.66    0.92    0.92      0
       65536         16384     float     sum      -1    48.80    1.34    1.34      0    47.69    1.37    1.37      0
      131072         32768     float     sum      -1    76.13    1.72    1.72      0    78.10    1.68    1.68      0
      262144         65536     float     sum      -1    129.1    2.03    2.03      0    128.5    2.04    2.04      0
      524288        131072     float     sum      -1    230.9    2.27    2.27      0    229.1    2.29    2.29      0
     1048576        262144     float     sum      -1    165.1    6.35    6.35      0    164.5    6.37    6.37      0
     2097152        524288     float     sum      -1    280.4    7.48    7.48      0    349.6    6.00    6.00      0
     4194304       1048576     float     sum      -1    511.1    8.21    8.21      0    510.1    8.22    8.22      0
     8388608       2097152     float     sum      -1    989.6    8.48    8.48      0    995.3    8.43    8.43      0
    16777216       4194304     float     sum      -1   1969.1    8.52    8.52      0   1964.1    8.54    8.54      0
    33554432       8388608     float     sum      -1   3910.3    8.58    8.58      0   3891.0    8.62    8.62      0
    67108864      16777216     float     sum      -1   7722.8    8.69    8.69      0   7625.4    8.80    8.80      0
   134217728      33554432     float     sum      -1    15176    8.84    8.84      0    15070    8.91    8.91      0
   268435456      67108864     float     sum      -1    29841    9.00    9.00      0    29856    8.99    8.99      0
   536870912     134217728     float     sum      -1    59962    8.95    8.95      0    59868    8.97    8.97      0
  1073741824     268435456     float     sum      -1   122177    8.79    8.79      0   122222    8.79    8.79      0
test1:3595:3595 [0] NCCL INFO comm 0x55a347241ed0 rank 0 nranks 2 cudaDev 0 busId 81000 - Destroy COMPLETE
test2:4017:4017 [0] NCCL INFO comm 0x563a8a2c7400 rank 1 nranks 2 cudaDev 0 busId 81000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 3.60188
#
```

The topology is still SYS.

The performance has improved, but it doesn't seem to be a good figure. Shouldn't it be at least 20GB/s in a PCI Gen4 environment?

### sjeaugey · 2025-03-10

> Shouldn't it be at least 20GB/s in a PCI Gen4 environment?

Well, it depends on the speed of the CPU and the memory attached to it. It also depends on the path data has to take between the GPU and NIC. From the original nvidia-smi output, it would look like the NIC is attached to a different CPU socket than the GPUs are attached to?

### gim4moon · 2025-03-11

> > Shouldn't it be at least 20GB/s in a PCI Gen4 environment?
> 
> Well, it depends on the speed of the CPU and the memory attached to it. It also depends on the path data has to take between the GPU and NIC. From the original nvidia-smi output, it would look like the NIC is attached to a different CPU socket than the GPUs are attached to?

![Image](https://github.com/user-attachments/assets/34e85779-5c6b-4db2-b8c3-4f6e5a46bf50)
Both GPU 2EA HDRcand set CPU Affinity to 2.
