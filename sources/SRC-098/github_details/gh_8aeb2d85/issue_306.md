# [Issue #306] NCCL_TESTS_SPLIT feature test encounter unexpected split

source: https://github.com/NVIDIA/nccl-tests/issues/306
state: closed | updated: 2025-04-29T05:41:03Z
labels: 

## 正文

### description
I have 2 node H20\*8+CX7*8(400G) hpc, when test `NCCL_TESTS_SPLIT`, I found whatevet "MOD 8" or  "DIV 8", it allways run one operation per node, purely intra-node. Is there something wrong with my config?

### cmd:
```
/usr/mpi/gcc/openmpi-4.1.7rc1/bin/mpirun --host <IP>:1,<IP>:1 <other param> -x NCCL_TESTS_SPLIT="MOD 8" /home/ruijie/enlb_test/nccl-tests/build/all_reduce_perf -b 1M -e 2G -f 2 -g 1
/usr/mpi/gcc/openmpi-4.1.7rc1/bin/mpirun --host <IP>:1,<IP>:1 <other param> -x NCCL_TESTS_SPLIT="DIV 8" /home/ruijie/enlb_test/nccl-tests/build/all_reduce_perf -b 1M -e 2G -f 2 -g 1
```

### result:
- MOD 8
```
# nThread 1 nGpus 8 minBytes 1048576 maxBytes 2147483648 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
# nThread 1 nGpus 8 minBytes 1048576 maxBytes 2147483648 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 1528921 on      node3 device  0 [0000:0f:00] NVIDIA H20
#  Rank  1 Group  0 Pid 1528921 on      node3 device  1 [0000:10:00] NVIDIA H20
#  Rank  2 Group  0 Pid 1528921 on      node3 device  2 [0000:41:00] NVIDIA H20
#  Rank  3 Group  0 Pid 1528921 on      node3 device  3 [0000:44:00] NVIDIA H20
#  Rank  4 Group  0 Pid 1528921 on      node3 device  4 [0000:90:00] NVIDIA H20
#  Rank  5 Group  0 Pid 1528921 on      node3 device  5 [0000:91:00] NVIDIA H20
#  Rank  6 Group  0 Pid 1528921 on      node3 device  6 [0000:b8:00] NVIDIA H20
#  Rank  7 Group  0 Pid 1528921 on      node3 device  7 [0000:bb:00] NVIDIA H20
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
     1048576        262144     float     sum      -1    35.66   29.40   51.46      0    34.90   30.04   52.58      0
     2097152        524288     float     sum      -1    38.34   54.70   95.73      0    38.11   55.03   96.31      0
     4194304       1048576     float     sum      -1    52.73   79.54  139.20      0    52.62   79.71  139.49      0
     8388608       2097152     float     sum      -1    79.28  105.81  185.17      0    79.18  105.94  185.40      0
    16777216       4194304     float     sum      -1    117.9  142.26  248.96      0    116.1  144.49  252.85      0
    33554432       8388608     float     sum      -1    215.4  155.78  272.61      0    214.8  156.24  273.41      0
    67108864      16777216     float     sum      -1    362.9  184.91  323.59      0    363.4  184.65  323.14      0
   134217728      33554432     float     sum      -1    702.6  191.02  334.29      0    702.6  191.03  334.31      0
   268435456      67108864     float     sum      -1   1367.0  196.37  343.65      0   1367.2  196.34  343.60      0
   536870912     134217728     float     sum      -1   2672.4  200.89  351.56      0   2670.1  201.07  351.87      0
  1073741824     268435456     float     sum      -1   5252.0  204.44  357.78      0   5260.7  204.11  357.19      0
#  Rank  0 Group  0 Pid 2171626 on      node2 device  0 [0000:0f:00] NVIDIA H20
#  Rank  1 Group  0 Pid 2171626 on      node2 device  1 [0000:10:00] NVIDIA H20
#  Rank  2 Group  0 Pid 2171626 on      node2 device  2 [0000:41:00] NVIDIA H20
#  Rank  3 Group  0 Pid 2171626 on      node2 device  3 [0000:44:00] NVIDIA H20
#  Rank  4 Group  0 Pid 2171626 on      node2 device  4 [0000:90:00] NVIDIA H20
#  Rank  5 Group  0 Pid 2171626 on      node2 device  5 [0000:91:00] NVIDIA H20
#  Rank  6 Group  0 Pid 2171626 on      node2 device  6 [0000:b8:00] NVIDIA H20
#  Rank  7 Group  0 Pid 2171626 on      node2 device  7 [0000:bb:00] NVIDIA H20
  2147483648     536870912     float     sum      -1    10407  206.34  361.10      0    10400  206.49  361.36      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 255.692
#

#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
     1048576        262144     float     sum      -1    40892    0.03    0.04      0    39244    0.03    0.05      0
     2097152        524288     float     sum      -1    26917    0.08    0.14      0    34184    0.06    0.11      0
     4194304       1048576     float     sum      -1    35009    0.12    0.21      0    30583    0.14    0.24      0
     8388608       2097152     float     sum      -1    33787    0.25    0.43      0    33797    0.25    0.43      0
    16777216       4194304     float     sum      -1    21297    0.79    1.38      0    43169    0.39    0.68      0
    33554432       8388608     float     sum      -1    48806    0.69    1.20      0    52234    0.64    1.12      0
    67108864      16777216     float     sum      -1    53960    1.24    2.18      0    62263    1.08    1.89      0
   134217728      33554432     float     sum      -1    72465    1.85    3.24      0    63746    2.11    3.68      0
   268435456      67108864     float     sum      -1    75707    3.55    6.21      0    68998    3.89    6.81      0
   536870912     134217728     float     sum      -1    84629    6.34   11.10      0   155294    3.46    6.05      0
  1073741824     268435456     float     sum      -1   200381    5.36    9.38      0   139164    7.72   13.50      0
  2147483648     536870912     float     sum      -1   169292   12.69   22.20      0   145148   14.80   25.89      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 4.92348
#


```
- DIV 8
```
# nThread 1 nGpus 8 minBytes 1048576 maxBytes 2147483648 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
# nThread 1 nGpus 8 minBytes 1048576 maxBytes 2147483648 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 1530412 on      node3 device  0 [0000:0f:00] NVIDIA H20
#  Rank  1 Group  0 Pid 1530412 on      node3 device  1 [0000:10:00] NVIDIA H20
#  Rank  2 Group  0 Pid 1530412 on      node3 device  2 [0000:41:00] NVIDIA H20
#  Rank  3 Group  0 Pid 1530412 on      node3 device  3 [0000:44:00] NVIDIA H20
#  Rank  4 Group  0 Pid 1530412 on      node3 device  4 [0000:90:00] NVIDIA H20
#  Rank  5 Group  0 Pid 1530412 on      node3 device  5 [0000:91:00] NVIDIA H20
#  Rank  6 Group  0 Pid 1530412 on      node3 device  6 [0000:b8:00] NVIDIA H20
#  Rank  7 Group  0 Pid 1530412 on      node3 device  7 [0000:bb:00] NVIDIA H20
#  Rank  0 Group  0 Pid 2236260 on      node2 device  0 [0000:0f:00] NVIDIA H20
#  Rank  1 Group  0 Pid 2236260 on      node2 device  1 [0000:10:00] NVIDIA H20
#  Rank  2 Group  0 Pid 2236260 on      node2 device  2 [0000:41:00] NVIDIA H20
#  Rank  3 Group  0 Pid 2236260 on      node2 device  3 [0000:44:00] NVIDIA H20
#  Rank  4 Group  0 Pid 2236260 on      node2 device  4 [0000:90:00] NVIDIA H20
#  Rank  5 Group  0 Pid 2236260 on      node2 device  5 [0000:91:00] NVIDIA H20
#  Rank  6 Group  0 Pid 2236260 on      node2 device  6 [0000:b8:00] NVIDIA H20
#  Rank  7 Group  0 Pid 2236260 on      node2 device  7 [0000:bb:00] NVIDIA H20
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
     1048576        262144     float     sum      -1    34.65   30.26   52.96      0    34.35   30.52   53.41      0
     2097152        524288     float     sum      -1    37.96   55.24   96.67      0    38.07   55.09   96.40      0
     4194304       1048576     float     sum      -1    53.43   78.50  137.38      0    52.81   79.43  139.00      0
     8388608       2097152     float     sum      -1    79.41  105.64  184.87      0    78.46  106.91  187.09      0
    16777216       4194304     float     sum      -1    117.7  142.60  249.54      0    116.3  144.28  252.49      0
    33554432       8388608     float     sum      -1    215.4  155.81  272.66      0    215.1  156.02  273.03      0
    67108864      16777216     float     sum      -1    363.1  184.80  323.41      0    362.8  184.95  323.67      0
   134217728      33554432     float     sum      -1    704.1  190.64  333.61      0    702.1  191.17  334.55      0
   268435456      67108864     float     sum      -1   1365.4  196.60  344.06      0   1367.1  196.35  343.61      0
   536870912     134217728     float     sum      -1   2662.4  201.65  352.89      0   2672.4  200.89  351.56      0
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
  1073741824     268435456     float     sum      -1   5254.1  204.36  357.64      0   5251.4  204.47  357.82      0
  2147483648     536870912     float     sum      -1    10387  206.74  361.80      0    10391  206.67  361.67      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 255.909
#

     1048576        262144     float     sum      -1    34.29   30.58   53.52      0    34.41   30.47   53.33      0
     2097152        524288     float     sum      -1    38.12   55.01   96.27      0    38.04   55.13   96.48      0
     4194304       1048576     float     sum      -1    53.58   78.29  137.00      0    53.29   78.71  137.74      0
     8388608       2097152     float     sum      -1    79.40  105.65  184.90      0    78.29  107.15  187.51      0
    16777216       4194304     float     sum      -1    117.9  142.30  249.03      0    116.3  144.24  252.42      0
    33554432       8388608     float     sum      -1    214.4  156.51  273.90      0    215.5  155.68  272.43      0
    67108864      16777216     float     sum      -1    364.9  183.90  321.82      0    364.0  184.35  322.60      0
   134217728      33554432     float     sum      -1    701.5  191.32  334.81      0    702.5  191.07  334.37      0
   268435456      67108864     float     sum      -1   1368.7  196.12  343.21      0   1366.9  196.39  343.68      0
   536870912     134217728     float     sum      -1   2669.3  201.13  351.97      0   2679.1  200.39  350.69      0
  1073741824     268435456     float     sum      -1   5249.1  204.56  357.98      0   5251.3  204.47  357.82      0
  2147483648     536870912     float     sum      -1    10373  207.02  362.29      0    10388  206.72  361.76      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 255.731
#
```

## 评论 (2)

### AddyLaddy · 2025-04-29

Did you compile nccl-tests using `MPI=1` ?


### GeofferyGeng · 2025-04-29

> Did you compile nccl-tests using `MPI=1` ?

@AddyLaddy Thanks for your help! I added MPI_HOME but forgot to add MPI=1. :-)
