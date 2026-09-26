# [Issue #290] Single-node and multi-node performance of H100 nodes.

source: https://github.com/NVIDIA/nccl-tests/issues/290
state: open | updated: 2025-03-04T09:13:02Z
labels: 

## 正文

Hello @AddyLaddy, 

Your assistance and advice would be greatly appreciated here. We are running multi-node training and have observed some performance degradation. Could you please review our envs and identify any potential abnormalities during multi node setup? Our GPU fabric is based on InfiniBand.

I am currently using Slurm to run the test. Are there any other environment variables I need to include? I also don't get the difference between UCX_NET_DEVICES and NCCL_IB_HCA. Could you please explain it? Thanks in advance for your help.

```
export NCCL_SOCKET_IFNAME=eth0 
export UCX_NET_DEVICES=mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_7:1,mlx5_8:1
```

Single node:
```
# nThread 1 nGpus 8 minBytes 134217728 maxBytes 4294967296 step: 2(factor) warmup iters: 5 iters: 2 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 295203 on    node005 device  0 [0x18] NVIDIA H100 80GB HBM3
#  Rank  1 Group  0 Pid 295203 on    node005 device  1 [0x6d] NVIDIA H100 80GB HBM3
#  Rank  2 Group  0 Pid 295203 on    node005 device  2 [0x97] NVIDIA H100 80GB HBM3
#  Rank  3 Group  0 Pid 295203 on    node005 device  3 [0xc0] NVIDIA H100 80GB HBM3
#  Rank  4 Group  0 Pid 295203 on    node005 device  4 [0x19] NVIDIA H100 80GB HBM3
#  Rank  5 Group  0 Pid 295203 on    node005 device  5 [0x6c] NVIDIA H100 80GB HBM3
#  Rank  6 Group  0 Pid 295203 on    node005 device  6 [0x96] NVIDIA H100 80GB HBM3
#  Rank  7 Group  0 Pid 295203 on    node005 device  7 [0xc1] NVIDIA H100 80GB HBM3
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
   134217728      33554432     float     sum      -1    613.3  218.85  382.99      0    614.3  218.48  382.34      0
   268435456      67108864     float     sum      -1   1139.2  235.63  412.35      0   1134.8  236.56  413.97      0
   536870912     134217728     float     sum      -1   2175.8  246.75  431.81      0   2181.4  246.11  430.69      0
  1073741824     268435456     float     sum      -1   4038.8  265.85  465.25      0   4043.6  265.54  464.70      0
  2147483648     536870912     float     sum      -1   8020.3  267.76  468.57      0   8002.1  268.36  469.64      0
  4294967296    1073741824     float     sum      -1    15870  270.63  473.60      0    15773  272.30  476.53      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 439.369
#
```

using two H100 nodes: 

```
 0: # nThread 1 nGpus 1 minBytes 8388608 maxBytes 8589934592 step: 2(factor) warmup iters: 5 iters: 200 agg iters: 1 validation: 0 graph: 0
 0: #
 0: # Using devices
 0: #  Rank  0 Group  0 Pid 291005 on    node005 device  0 [0x18] NVIDIA H100 80GB HBM3
 0: #  Rank  1 Group  0 Pid 291006 on    node005 device  1 [0x6d] NVIDIA H100 80GB HBM3
 0: #  Rank  2 Group  0 Pid 291002 on    node005 device  2 [0x97] NVIDIA H100 80GB HBM3
 0: #  Rank  3 Group  0 Pid 291004 on    node005 device  3 [0xc0] NVIDIA H100 80GB HBM3
 0: #  Rank  4 Group  0 Pid 291003 on    node005 device  4 [0x19] NVIDIA H100 80GB HBM3
 0: #  Rank  5 Group  0 Pid 291001 on    node005 device  5 [0x6c] NVIDIA H100 80GB HBM3
 0: #  Rank  6 Group  0 Pid 291008 on    node005 device  6 [0x96] NVIDIA H100 80GB HBM3
 0: #  Rank  7 Group  0 Pid 291007 on    node005 device  7 [0xc1] NVIDIA H100 80GB HBM3
 0: #  Rank  8 Group  0 Pid 541703 on    node007 device  0 [0x18] NVIDIA H100 80GB HBM3
 0: #  Rank  9 Group  0 Pid 541708 on    node007 device  1 [0x6d] NVIDIA H100 80GB HBM3
 0: #  Rank 10 Group  0 Pid 541707 on    node007 device  2 [0x97] NVIDIA H100 80GB HBM3
 0: #  Rank 11 Group  0 Pid 541702 on    node007 device  3 [0xc0] NVIDIA H100 80GB HBM3
 0: #  Rank 12 Group  0 Pid 541706 on    node007 device  4 [0x19] NVIDIA H100 80GB HBM3
 0: #  Rank 13 Group  0 Pid 541704 on    node007 device  5 [0x6c] NVIDIA H100 80GB HBM3
 0: #  Rank 14 Group  0 Pid 541709 on    node007 device  6 [0x96] NVIDIA H100 80GB HBM3
 0: #  Rank 15 Group  0 Pid 541705 on    node007 device  7 [0xc1] NVIDIA H100 80GB HBM3
 0: #
 0: #                                                              out-of-place                       in-place
 0: #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
 0: #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
 0:      8388608       2097152     float     sum      -1    215.3   38.96   73.04    N/A    180.0   46.60   87.38    N/A
 0:     16777216       4194304     float     sum      -1    262.9   63.81  119.65    N/A    261.9   64.05  120.10    N/A
 0:     33554432       8388608     float     sum      -1    439.3   76.38  143.21    N/A    437.8   76.64  143.69    N/A
 0:     67108864      16777216     float     sum      -1    918.4   73.07  137.01    N/A    856.0   78.39  146.99    N/A
 0:    134217728      33554432     float     sum      -1   1575.6   85.19  159.72    N/A   1566.6   85.68  160.64    N/A
 0:    268435456      67108864     float     sum      -1   3027.9   88.65  166.22    N/A   2998.2   89.53  167.87    N/A
 0:    536870912     134217728     float     sum      -1   6983.7   76.88  144.14    N/A   7003.1   76.66  143.74    N/A
 0:   1073741824     268435456     float     sum      -1    13435   79.92  149.85    N/A    13430   79.95  149.91    N/A
 0:   2147483648     536870912     float     sum      -1    26301   81.65  153.09    N/A    26293   81.68  153.14    N/A
 0:   4294967296    1073741824     float     sum      -1    52043   82.53  154.74    N/A    51992   82.61  154.89    N/A
 0:   8589934592    2147483648     float     sum      -1   103530   82.97  155.57    N/A   103538   82.96  155.56    N/A
 0: # Out of bounds values : 0 OK
 0: # Avg bus bandwidth    : 142.735
 0: #
 0:
```


## 评论 (3)

### AddyLaddy · 2025-03-03

Only MPI/SLURM use UCX support, so the UCX_NET_DEVICES env var is purely for those.
NCCL uses NCCL_IB_HCA devices to select the specific HCAs to use for collective communication, but in general it finds the correct ones.

The single node run above will be using NVLink and NVLink SHARP to accelerate AllReduce and 476GB/s looks to be in the expected range for H100.

Running on two nodes (over IB/RoCE) is more complex and we suggest passing NCCL_ALGO=RING when benchmarking just two nodes to examine the HCA/Network performance.

What speed are your NICs ? For NDR @ 400Gbps you should see 46-48GB/s per NIC.

You should examine the NCCL_DEBUG=INFO logs to see more details on which NICs NCCL is selecting and how many channels etc it is using.

### shahizat · 2025-03-04

Thank you, @AddyLaddy , for the informative response. Yes, we are using NDR with NVIDIA Quantum-2 400Gbps InfiniBand network switches and ConnectX-7 Mellanox NICs on the server side. Could you please explain where I should expect to see 46-48 GB/s per NIC, specifically in terms of out-of-place or in-place operations?

I will provide more details later. 

### shahizat · 2025-03-04

@AddyLaddy I used these environment variables and received these results. Can you confirm if these values are correct?

```
export NCCL_ALGO=RING
export NCCL_IB_AR_THRESHOLD=0 
export NCCL_IB_PCI_RELAXED_ORDERING=1
export NCCL_IB_SPLIT_DATA_ON_QPS=0 
export NCCL_IB_QPS_PER_CONNECTION=2 
export CUDA_DEVICE_ORDER=PCI_BUS_ID
export NCCL_IB_HCA=mlx5_0:1,mlx5_2:1,mlx5_3:1,mlx5_4:1,mlx5_5:1,mlx5_7:1,mlx5_8:1,mlx5_9:1
export NCCL_SOCKET_IFNAME=eth0
export NCCL_IGNORE_CPU_AFFINITY=1
```

```
 0: # Using devices
 0: #  Rank  0 Group  0 Pid 367195 on    node005 device  0 [0x18] NVIDIA H100 80GB HBM3
 0: #  Rank  1 Group  0 Pid 367196 on    node005 device  1 [0x6d] NVIDIA H100 80GB HBM3
 0: #  Rank  2 Group  0 Pid 367193 on    node005 device  2 [0x97] NVIDIA H100 80GB HBM3
 0: #  Rank  3 Group  0 Pid 367197 on    node005 device  3 [0xc0] NVIDIA H100 80GB HBM3
 0: #  Rank  4 Group  0 Pid 367194 on    node005 device  4 [0x19] NVIDIA H100 80GB HBM3
 0: #  Rank  5 Group  0 Pid 367200 on    node005 device  5 [0x6c] NVIDIA H100 80GB HBM3
 0: #  Rank  6 Group  0 Pid 367198 on    node005 device  6 [0x96] NVIDIA H100 80GB HBM3
 0: #  Rank  7 Group  0 Pid 367199 on    node005 device  7 [0xc1] NVIDIA H100 80GB HBM3
 0: #  Rank  8 Group  0 Pid 617100 on    node007 device  0 [0x18] NVIDIA H100 80GB HBM3
 0: #  Rank  9 Group  0 Pid 617096 on    node007 device  1 [0x6d] NVIDIA H100 80GB HBM3
 0: #  Rank 10 Group  0 Pid 617099 on    node007 device  2 [0x97] NVIDIA H100 80GB HBM3
 0: #  Rank 11 Group  0 Pid 617101 on    node007 device  3 [0xc0] NVIDIA H100 80GB HBM3
 0: #  Rank 12 Group  0 Pid 617102 on    node007 device  4 [0x19] NVIDIA H100 80GB HBM3
 0: #  Rank 13 Group  0 Pid 617097 on    node007 device  5 [0x6c] NVIDIA H100 80GB HBM3
 0: #  Rank 14 Group  0 Pid 617098 on    node007 device  6 [0x96] NVIDIA H100 80GB HBM3
 0: #  Rank 15 Group  0 Pid 617103 on    node007 device  7 [0xc1] NVIDIA H100 80GB HBM3
 0: #
 0: #                                                              out-of-place                       in-place
 0: #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
 0: #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
 0:      8388608       2097152     float     sum      -1    407.5   20.59   38.60    N/A    405.5   20.69   38.79    N/A
 0:     16777216       4194304     float     sum      -1    495.4   33.87   63.50    N/A    461.0   36.39   68.24    N/A
 0:     33554432       8388608     float     sum      -1    666.0   50.38   94.47    N/A    665.8   50.40   94.50    N/A
 0:     67108864      16777216     float     sum      -1   1232.4   54.45  102.10    N/A   1230.4   54.54  102.27    N/A
 0:    134217728      33554432     float     sum      -1   2519.5   53.27   99.88    N/A   2491.1   53.88  101.02    N/A
 0:    268435456      67108864     float     sum      -1   5268.0   50.96   95.54    N/A   5249.3   51.14   95.88    N/A
 0:    536870912     134217728     float     sum      -1    11557   46.45   87.10    N/A    11561   46.44   87.07    N/A
 0:   1073741824     268435456     float     sum      -1    22920   46.85   87.84    N/A    22918   46.85   87.85    N/A
 0:   2147483648     536870912     float     sum      -1    45157   47.56   89.17    N/A    45150   47.56   89.18    N/A
 0:   4294967296    1073741824     float     sum      -1    89577   47.95   89.90    N/A    90035   47.70   89.44    N/A
 0:   8589934592    2147483648     float     sum      -1   179148   47.95   89.90    N/A   180166   47.68   89.40    N/A
 0: # Out of bounds values : 0 OK
 0: # Avg bus bandwidth    : 85.5294
```

