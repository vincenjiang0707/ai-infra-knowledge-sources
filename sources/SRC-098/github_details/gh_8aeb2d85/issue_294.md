# [Issue #294] Getting Avg bus bandwidth = 0 when running all_reduce_perf in nccl-tests

source: https://github.com/NVIDIA/nccl-tests/issues/294
state: open | updated: 2025-03-15T05:29:58Z
labels: question, triaged

## 正文

I am trying to run nccl test between two H100s and it gives Avg bus bandwidth = 0. 

nccl-test script
```
#!/bin/bash

. /opt/hpcx/hpcx-init.sh
hpcx_load

mpirun -np 16 -N 8 -hostfile hostfile --bind-to none -mca btl tcp,self -mca coll_hcoll_enable 0 -x PATH -x LD_LIBRARY_PATH -x NCCL_DEBUG=INFO /home/ubuntu/nccl-tests/build/all_reduce_perf -b 128M -e 2048M -f 2 -t 1 -g 1 -c 1 -n 10
```

And here's my `/etc/nccl.conf`
```
NCCL_IB_DISABLE=0
NCCL_SOCKET_NTHREADS=4
NCCL_NSOCKS_PERTHREAD=8
NCCL_TOPO_FILE=/etc/crusoe/nccl_topo/h100-80gb-sxm-ib-cloud-hypervisor.xml
NCCL_IB_MERGE_VFS=0
NCCL_ALGO=NVLSTree
NCCL_IB_HCA=^mlx5_0:1
```

And the results
```
   134217728      33554432     float     sum      -1    631.9  212.41    0.00      0     0.51  263017.30    0.00      0
   134217728      33554432     float     sum      -1    419.3  320.07    0.00      0     0.31  428400.03    0.00      0
   536870912     134217728     float     sum      -1   2202.2  243.79    0.00      0     0.31  1747057.96    0.00      0
   536870912     134217728     float     sum      -1    842.5  637.23    0.00      0     0.30  1777718.25    0.00      0
   268435456      67108864     float     sum      -1   1007.4  266.46    0.00      0     0.31  857621.27    0.00      0
   268435456      67108864     float     sum      -1    822.4  326.41    0.00      0     0.30  888564.90    0.00      0
   134217728      33554432     float     sum      -1    604.0  222.21    0.00      0     0.45  297996.73    0.00      0
   134217728      33554432     float     sum      -1    698.2  192.24    0.00      0     0.32  422201.09    0.00      0
   268435456      67108864     float     sum      -1   1615.8  166.13    0.00      0     0.32  851095.29    0.00      0
   268435456      67108864     float     sum      -1    611.3  439.13    0.00      0     0.46  580275.52    0.00      0
   536870912     134217728     float     sum      -1   1288.7  416.59    0.00      0     0.32  1690399.60    0.00      0
   268435456      67108864     float     sum      -1    707.7  379.30    0.00      0     0.31  856253.45    0.00      0
   536870912     134217728     float     sum      -1   1791.4  299.70    0.00      0     0.34  1584157.31    0.00      0
   268435456      67108864     float     sum      -1    522.5  513.75    0.00      0     0.38  713354.92    0.00      0
  1073741824     268435456     float     sum      -1   5253.3  204.39    0.00      0     0.31  3512403.74    0.00      0
  1073741824     268435456     float     sum      -1   3922.0  273.77    0.00      0     0.32  3316064.93    0.00      0
   536870912     134217728     float     sum      -1   1233.9  435.11    0.00      0     0.30  1773021.51    0.00      0
   536870912     134217728     float     sum      -1    896.9  598.56    0.00      0     0.33  1611257.24    0.00      0
   536870912     134217728     float     sum      -1   1559.8  344.18    0.00      0     0.31  1731283.17    0.00      0
   536870912     134217728     float     sum      -1   1802.1  297.91    0.00      0     0.31  1727939.85    0.00      0
  1073741824     268435456     float     sum      -1   2932.7  366.13    0.00      0     0.31  3448111.19    0.00      0
  1073741824     268435456     float     sum      -1   3015.3  356.09    0.00      0     0.31  3489573.69    0.00      0
  1073741824     268435456     float     sum      -1   3632.4  295.60    0.00      0     0.34  3153426.80    0.00      0
  2147483648     536870912     float     sum      -1   8645.7  248.39    0.00      0     0.31  7017920.42    0.00      0
h100-test-rg-1:19570:19570 [0] NCCL INFO comm 0x55ba38f2abd0 rank 0 nranks 1 cudaDev 0 busId 200010 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 0
```

Can I get some help if the settings in my nccl.conf or mpirun command or correctly applied? Thanks!

## 评论 (9)

### AddyLaddy · 2025-03-14

It looks like you didn't compile the nccl-tests binaries with `MPI=1` 

### rgee18 · 2025-03-14

Compiled the nccl-tests binaries on both H100s
```
make MPI=1
make -C src build BUILDDIR=/home/ubuntu/nccl-tests/build
make[1]: Entering directory '/home/ubuntu/nccl-tests/src'
Compiling  timer.cc                            > /home/ubuntu/nccl-tests/build/timer.o
Compiling /home/ubuntu/nccl-tests/build/verifiable/verifiable.o
Compiling  all_reduce.cu                       > /home/ubuntu/nccl-tests/build/all_reduce.o
Compiling  common.cu                           > /home/ubuntu/nccl-tests/build/common.o
Linking  /home/ubuntu/nccl-tests/build/all_reduce.o > /home/ubuntu/nccl-tests/build/all_reduce_perf
Compiling  all_gather.cu                       > /home/ubuntu/nccl-tests/build/all_gather.o
Linking  /home/ubuntu/nccl-tests/build/all_gather.o > /home/ubuntu/nccl-tests/build/all_gather_perf
Compiling  broadcast.cu                        > /home/ubuntu/nccl-tests/build/broadcast.o
Linking  /home/ubuntu/nccl-tests/build/broadcast.o > /home/ubuntu/nccl-tests/build/broadcast_perf
Compiling  reduce_scatter.cu                   > /home/ubuntu/nccl-tests/build/reduce_scatter.o
Linking  /home/ubuntu/nccl-tests/build/reduce_scatter.o > /home/ubuntu/nccl-tests/build/reduce_scatter_perf
Compiling  reduce.cu                           > /home/ubuntu/nccl-tests/build/reduce.o
Linking  /home/ubuntu/nccl-tests/build/reduce.o > /home/ubuntu/nccl-tests/build/reduce_perf
Compiling  alltoall.cu                         > /home/ubuntu/nccl-tests/build/alltoall.o
Linking  /home/ubuntu/nccl-tests/build/alltoall.o > /home/ubuntu/nccl-tests/build/alltoall_perf
Compiling  scatter.cu                          > /home/ubuntu/nccl-tests/build/scatter.o
Linking  /home/ubuntu/nccl-tests/build/scatter.o > /home/ubuntu/nccl-tests/build/scatter_perf
Compiling  gather.cu                           > /home/ubuntu/nccl-tests/build/gather.o
Linking  /home/ubuntu/nccl-tests/build/gather.o > /home/ubuntu/nccl-tests/build/gather_perf
Compiling  sendrecv.cu                         > /home/ubuntu/nccl-tests/build/sendrecv.o
Linking  /home/ubuntu/nccl-tests/build/sendrecv.o > /home/ubuntu/nccl-tests/build/sendrecv_perf
Compiling  hypercube.cu                        > /home/ubuntu/nccl-tests/build/hypercube.o
Linking  /home/ubuntu/nccl-tests/build/hypercube.o > /home/ubuntu/nccl-tests/build/hypercube_perf
make[1]: Leaving directory '/home/ubuntu/nccl-tests/src'
```
```
   134217728      33554432     float     sum      -1    738.7  181.69  340.67      0    739.9  181.40  340.12      0
   268435456      67108864     float     sum      -1   1278.7  209.93  393.62      0   1259.7  213.10  399.57      0
   536870912     134217728     float     sum      -1   2467.0  217.62  408.04      0   2481.0  216.39  405.73      0
  1073741824     268435456     float     sum      -1   4568.9  235.01  440.65      0   4527.2  237.18  444.71      0
  2147483648     536870912     float     sum      -1   9063.6  236.93  444.25      0   9089.4  236.26  442.99      0
h100-test-rg-1:31789:31789 [0] NCCL INFO comm 0x556b35426090 rank 0 nranks 16 cudaDev 0 busId 200010 - Destroy COMPLETE
h100-test-rg-2:32768:32768 [4] NCCL INFO comm 0x55694311e2f0 rank 12 nranks 16 cudaDev 4 busId 300010 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 406.034
```
Thank you!

### rgee18 · 2025-03-14

So then it seems like `make` after a cloning of the repository wouldn't work? And that I would need to run `make MPI=1`?

### AddyLaddy · 2025-03-14

You would need to do a `make clean` before the `make MPI=1` if you previously compiled without `MPI=1`
The binary names generated are the same. 

### AddyLaddy · 2025-03-14

BTW: We normally suggest not overloading the NCCL default algorithm selection with say `NCCL_ALGO=NVLSTree` unless you're benchmarking on just 2 nodes (`NCCL_ALGO=Ring`) or doing some specific performance investigations.

### rgee18 · 2025-03-14

Understood on the `make clean` part.

Yeah the test would be just for two nodes. Is your recommendation on two nodes to use `NCCL_ALGO=Ring`? 

### rgee18 · 2025-03-14

I'm now getting this error
```
# nThread 1 nGpus 1 minBytes 134217728 maxBytes 2147483648 step: 2(factor) warmup iters: 5 iters: 10 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 895544 on     h100-2 device  0 [0002:00:01] NVIDIA H100 80GB HBM3
#  Rank  1 Group  0 Pid 895545 on     h100-2 device  1 [0002:00:02] NVIDIA H100 80GB HBM3
#  Rank  2 Group  0 Pid 895546 on     h100-2 device  2 [0002:00:03] NVIDIA H100 80GB HBM3
#  Rank  3 Group  0 Pid 895547 on     h100-2 device  3 [0002:00:04] NVIDIA H100 80GB HBM3
#  Rank  4 Group  0 Pid 895548 on     h100-2 device  4 [0003:00:01] NVIDIA H100 80GB HBM3
#  Rank  5 Group  0 Pid 895549 on     h100-2 device  5 [0003:00:02] NVIDIA H100 80GB HBM3
#  Rank  6 Group  0 Pid 895550 on     h100-2 device  6 [0003:00:03] NVIDIA H100 80GB HBM3
#  Rank  7 Group  0 Pid 895552 on     h100-2 device  7 [0003:00:04] NVIDIA H100 80GB HBM3
#  Rank  8 Group  0 Pid 739786 on     h100-4 device  0 [0002:00:01] NVIDIA H100 80GB HBM3
#  Rank  9 Group  0 Pid 739787 on     h100-4 device  1 [0002:00:02] NVIDIA H100 80GB HBM3
#  Rank 10 Group  0 Pid 739788 on     h100-4 device  2 [0002:00:03] NVIDIA H100 80GB HBM3
#  Rank 11 Group  0 Pid 739789 on     h100-4 device  3 [0002:00:04] NVIDIA H100 80GB HBM3
#  Rank 12 Group  0 Pid 739790 on     h100-4 device  4 [0003:00:01] NVIDIA H100 80GB HBM3
#  Rank 13 Group  0 Pid 739791 on     h100-4 device  5 [0003:00:02] NVIDIA H100 80GB HBM3
#  Rank 14 Group  0 Pid 739792 on     h100-4 device  6 [0003:00:03] NVIDIA H100 80GB HBM3
#  Rank 15 Group  0 Pid 739794 on     h100-4 device  7 [0003:00:04] NVIDIA H100 80GB HBM3
h100-2:895544:895544 [0] NCCL INFO Bootstrap : Using ens7:172.27.37.143<0>
h100-4:739788:739788 [2] NCCL INFO cudaDriverVersion 12020
h100-4:739792:739792 [6] NCCL INFO cudaDriverVersion 12020
h100-4:739794:739794 [7] NCCL INFO cudaDriverVersion 12020
h100-4:739790:739790 [4] NCCL INFO cudaDriverVersion 12020
h100-4:739786:739786 [0] NCCL INFO cudaDriverVersion 12020
h100-4:739787:739787 [1] NCCL INFO cudaDriverVersion 12020
h100-4:739789:739789 [3] NCCL INFO cudaDriverVersion 12020
h100-4:739791:739791 [5] NCCL INFO cudaDriverVersion 12020
h100-2:895544:895544 [0] NCCL INFO cudaDriverVersion 12020
NCCL version 2.18.3+cuda12.2
h100-2:895547:895547 [3] NCCL INFO cudaDriverVersion 12020
h100-2:895547:895547 [3] NCCL INFO Bootstrap : Using ens7:172.27.37.143<0>
h100-2:895548:895548 [4] NCCL INFO cudaDriverVersion 12020
h100-2:895548:895548 [4] NCCL INFO Bootstrap : Using ens7:172.27.37.143<0>
h100-2:895552:895552 [7] NCCL INFO cudaDriverVersion 12020
h100-2:895552:895552 [7] NCCL INFO Bootstrap : Using ens7:172.27.37.143<0>
h100-2:895550:895550 [6] NCCL INFO cudaDriverVersion 12020
h100-2:895550:895550 [6] NCCL INFO Bootstrap : Using ens7:172.27.37.143<0>
h100-2:895546:895546 [2] NCCL INFO cudaDriverVersion 12020
h100-2:895546:895546 [2] NCCL INFO Bootstrap : Using ens7:172.27.37.143<0>
h100-2:895545:895545 [1] NCCL INFO cudaDriverVersion 12020
h100-2:895549:895549 [5] NCCL INFO cudaDriverVersion 12020
h100-2:895549:895549 [5] NCCL INFO Bootstrap : Using ens7:172.27.37.143<0>
h100-2:895545:895545 [1] NCCL INFO Bootstrap : Using ens7:172.27.37.143<0>
h100-4:739788:739788 [2] NCCL INFO Bootstrap : Using ens7:172.27.32.104<0>
h100-4:739792:739792 [6] NCCL INFO Bootstrap : Using ens7:172.27.32.104<0>
h100-4:739792:739876 [6] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-4:739792:739876 [6] NCCL INFO P2P plugin IBext_v6
h100-4:739788:739877 [2] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-4:739788:739877 [2] NCCL INFO P2P plugin IBext_v6
h100-4:739790:739790 [4] NCCL INFO Bootstrap : Using ens7:172.27.32.104<0>
h100-4:739790:739878 [4] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-4:739790:739878 [4] NCCL INFO P2P plugin IBext_v6
h100-4:739794:739794 [7] NCCL INFO Bootstrap : Using ens7:172.27.32.104<0>
h100-4:739794:739879 [7] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-4:739794:739879 [7] NCCL INFO P2P plugin IBext_v6
h100-4:739790:739878 [4] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-4:739792:739876 [6] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-4:739788:739877 [2] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-4:739794:739879 [7] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-4:739786:739786 [0] NCCL INFO Bootstrap : Using ens7:172.27.32.104<0>
h100-4:739786:739887 [0] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-4:739786:739887 [0] NCCL INFO P2P plugin IBext_v6
h100-4:739789:739789 [3] NCCL INFO Bootstrap : Using ens7:172.27.32.104<0>
h100-4:739786:739887 [0] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-4:739789:739898 [3] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-4:739789:739898 [3] NCCL INFO P2P plugin IBext_v6
h100-4:739791:739791 [5] NCCL INFO Bootstrap : Using ens7:172.27.32.104<0>
h100-4:739789:739898 [3] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-4:739791:739911 [5] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-4:739791:739911 [5] NCCL INFO P2P plugin IBext_v6
h100-4:739787:739787 [1] NCCL INFO Bootstrap : Using ens7:172.27.32.104<0>
h100-4:739787:739914 [1] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-4:739787:739914 [1] NCCL INFO P2P plugin IBext_v6
h100-4:739791:739911 [5] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-4:739790:739878 [4] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.32.104<0>
h100-4:739790:739878 [4] NCCL INFO Using network IBext_v6
h100-4:739792:739876 [6] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.32.104<0>
h100-4:739792:739876 [6] NCCL INFO Using network IBext_v6
h100-4:739788:739877 [2] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.32.104<0>
h100-4:739788:739877 [2] NCCL INFO Using network IBext_v6
h100-4:739787:739914 [1] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.

h100-4:739790:739878 [4] misc/socket.cc:397 NCCL WARN Net : connecting to address  with family 33621 is neither AF_INET(2) nor AF_INET6(10)
h100-4:739790:739878 [4] NCCL INFO bootstrap.cc:256 -> 3
h100-4:739790:739878 [4] NCCL INFO init.cc:516 -> 3
h100-4:739790:739878 [4] NCCL INFO init.cc:1089 -> 3
h100-4:739790:739878 [4] NCCL INFO group.cc:64 -> 3 [Async thread]

h100-4:739792:739876 [6] misc/socket.cc:397 NCCL WARN Net : connecting to address  with family 33621 is neither AF_INET(2) nor AF_INET6(10)
h100-4:739792:739876 [6] NCCL INFO bootstrap.cc:256 -> 3
h100-4:739792:739876 [6] NCCL INFO init.cc:516 -> 3
h100-4:739792:739876 [6] NCCL INFO init.cc:1089 -> 3
h100-4:739792:739876 [6] NCCL INFO group.cc:64 -> 3 [Async thread]

h100-4:739788:739877 [2] misc/socket.cc:397 NCCL WARN Net : connecting to address  with family 33621 is neither AF_INET(2) nor AF_INET6(10)
h100-4:739788:739877 [2] NCCL INFO bootstrap.cc:256 -> 3
h100-4:739788:739877 [2] NCCL INFO init.cc:516 -> 3
h100-4:739788:739877 [2] NCCL INFO init.cc:1089 -> 3
h100-4:739788:739877 [2] NCCL INFO group.cc:64 -> 3 [Async thread]
h100-4:739790:739790 [4] NCCL INFO group.cc:421 -> 3
h100-4:739790:739790 [4] NCCL INFO group.cc:106 -> 3
h100-4: Test NCCL failure common.cu:1057 'internal error / '
 .. h100-4 pid 739790: Test failure common.cu:893
h100-4:739788:739788 [2] NCCL INFO group.cc:421 -> 3
h100-4:739788:739788 [2] NCCL INFO group.cc:106 -> 3
h100-4: Test NCCL failure common.cu:1057 'internal error / '
 .. h100-4 pid 739788: Test failure common.cu:893
h100-4:739792:739792 [6] NCCL INFO group.cc:421 -> 3
h100-4:739792:739792 [6] NCCL INFO group.cc:106 -> 3
h100-4: Test NCCL failure common.cu:1057 'internal error / '
 .. h100-4 pid 739792: Test failure common.cu:893
h100-4:739794:739879 [7] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.32.104<0>
h100-4:739794:739879 [7] NCCL INFO Using network IBext_v6

h100-4:739794:739879 [7] misc/socket.cc:397 NCCL WARN Net : connecting to address  with family 33621 is neither AF_INET(2) nor AF_INET6(10)
h100-4:739794:739879 [7] NCCL INFO bootstrap.cc:256 -> 3
h100-4:739794:739879 [7] NCCL INFO init.cc:516 -> 3
h100-4:739794:739879 [7] NCCL INFO init.cc:1089 -> 3
h100-4:739794:739879 [7] NCCL INFO group.cc:64 -> 3 [Async thread]
h100-4:739794:739794 [7] NCCL INFO group.cc:421 -> 3
h100-4:739794:739794 [7] NCCL INFO group.cc:106 -> 3
h100-4: Test NCCL failure common.cu:1057 'internal error / '
 .. h100-4 pid 739794: Test failure common.cu:893
h100-4:739786:739887 [0] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.32.104<0>
h100-4:739786:739887 [0] NCCL INFO Using network IBext_v6

h100-4:739786:739887 [0] misc/socket.cc:397 NCCL WARN Net : connecting to address  with family 33621 is neither AF_INET(2) nor AF_INET6(10)
h100-4:739786:739887 [0] NCCL INFO bootstrap.cc:256 -> 3
h100-4:739786:739887 [0] NCCL INFO init.cc:516 -> 3
h100-4:739786:739887 [0] NCCL INFO init.cc:1089 -> 3
h100-4:739786:739887 [0] NCCL INFO group.cc:64 -> 3 [Async thread]
h100-4:739786:739786 [0] NCCL INFO group.cc:421 -> 3
h100-4:739786:739786 [0] NCCL INFO group.cc:106 -> 3
h100-4: Test NCCL failure common.cu:1057 'internal error / '
 .. h100-4 pid 739786: Test failure common.cu:893
h100-4:739789:739898 [3] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.32.104<0>
h100-4:739789:739898 [3] NCCL INFO Using network IBext_v6

h100-4:739789:739898 [3] misc/socket.cc:397 NCCL WARN Net : connecting to address  with family 33621 is neither AF_INET(2) nor AF_INET6(10)
h100-4:739789:739898 [3] NCCL INFO bootstrap.cc:256 -> 3
h100-4:739789:739898 [3] NCCL INFO init.cc:516 -> 3
h100-4:739789:739898 [3] NCCL INFO init.cc:1089 -> 3
h100-4:739789:739898 [3] NCCL INFO group.cc:64 -> 3 [Async thread]
h100-4:739789:739789 [3] NCCL INFO group.cc:421 -> 3
h100-4:739789:739789 [3] NCCL INFO group.cc:106 -> 3
h100-4: Test NCCL failure common.cu:1057 'internal error / '
 .. h100-4 pid 739789: Test failure common.cu:893
h100-4:739791:739911 [5] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.32.104<0>
h100-4:739791:739911 [5] NCCL INFO Using network IBext_v6

h100-4:739791:739911 [5] misc/socket.cc:397 NCCL WARN Net : connecting to address  with family 33621 is neither AF_INET(2) nor AF_INET6(10)
h100-4:739791:739911 [5] NCCL INFO bootstrap.cc:256 -> 3
h100-4:739791:739911 [5] NCCL INFO init.cc:516 -> 3
h100-4:739791:739911 [5] NCCL INFO init.cc:1089 -> 3
h100-4:739791:739911 [5] NCCL INFO group.cc:64 -> 3 [Async thread]
h100-4:739791:739791 [5] NCCL INFO group.cc:421 -> 3
h100-4:739791:739791 [5] NCCL INFO group.cc:106 -> 3
h100-4: Test NCCL failure common.cu:1057 'internal error / '
 .. h100-4 pid 739791: Test failure common.cu:893
h100-4:739787:739914 [1] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.32.104<0>
h100-4:739787:739914 [1] NCCL INFO Using network IBext_v6

h100-4:739787:739914 [1] misc/socket.cc:397 NCCL WARN Net : connecting to address  with family 33621 is neither AF_INET(2) nor AF_INET6(10)
h100-4:739787:739914 [1] NCCL INFO bootstrap.cc:256 -> 3
h100-4:739787:739914 [1] NCCL INFO init.cc:516 -> 3
h100-4:739787:739914 [1] NCCL INFO init.cc:1089 -> 3
h100-4:739787:739914 [1] NCCL INFO group.cc:64 -> 3 [Async thread]
h100-4:739787:739787 [1] NCCL INFO group.cc:421 -> 3
h100-4:739787:739787 [1] NCCL INFO group.cc:106 -> 3
h100-4: Test NCCL failure common.cu:1057 'internal error / '
 .. h100-4 pid 739787: Test failure common.cu:893
h100-2:895544:895648 [0] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-2:895544:895648 [0] NCCL INFO P2P plugin IBext_v6
h100-2:895544:895648 [0] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-2:895544:895648 [0] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.37.143<0>
h100-2:895544:895648 [0] NCCL INFO Using network IBext_v6
h100-2:895552:895651 [7] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-2:895552:895651 [7] NCCL INFO P2P plugin IBext_v6
h100-2:895552:895651 [7] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-2:895552:895651 [7] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.37.143<0>
h100-2:895552:895651 [7] NCCL INFO Using network IBext_v6
h100-2:895550:895652 [6] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-2:895550:895652 [6] NCCL INFO P2P plugin IBext_v6
h100-2:895550:895652 [6] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-2:895548:895650 [4] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-2:895548:895650 [4] NCCL INFO P2P plugin IBext_v6
h100-2:895548:895650 [4] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-2:895550:895652 [6] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.37.143<0>
h100-2:895550:895652 [6] NCCL INFO Using network IBext_v6
h100-2:895546:895653 [2] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-2:895546:895653 [2] NCCL INFO P2P plugin IBext_v6
h100-2:895548:895650 [4] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.37.143<0>
h100-2:895548:895650 [4] NCCL INFO Using network IBext_v6
h100-2:895549:895654 [5] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-2:895549:895654 [5] NCCL INFO P2P plugin IBext_v6
h100-2:895546:895653 [2] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-2:895545:895655 [1] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-2:895545:895655 [1] NCCL INFO P2P plugin IBext_v6
h100-2:895549:895654 [5] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-2:895545:895655 [1] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-2:895546:895653 [2] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.37.143<0>
h100-2:895546:895653 [2] NCCL INFO Using network IBext_v6
h100-2:895549:895654 [5] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.37.143<0>
h100-2:895549:895654 [5] NCCL INFO Using network IBext_v6
h100-2:895547:895649 [3] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
h100-2:895547:895649 [3] NCCL INFO P2P plugin IBext_v6
h100-2:895545:895655 [1] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.37.143<0>
h100-2:895545:895655 [1] NCCL INFO Using network IBext_v6
h100-2:895547:895649 [3] NCCL INFO NCCL_IB_MERGE_VFS set by environment to 0.
h100-2:895547:895649 [3] NCCL INFO NET/IB : Using [0]mlx5_1:1/IB/SHARP [1]mlx5_2:1/IB/SHARP [2]mlx5_3:1/IB/SHARP [3]mlx5_4:1/IB/SHARP [4]mlx5_5:1/IB/SHARP [5]mlx5_6:1/IB/SHARP [6]mlx5_7:1/IB/SHARP [7]mlx5_8:1/IB/SHARP [RO]; OOB ens7:172.27.37.143<0>
h100-2:895547:895649 [3] NCCL INFO Using network IBext_v6
--------------------------------------------------------------------------
Primary job  terminated normally, but 1 process returned
a non-zero exit code. Per user-direction, the job has been aborted.
--------------------------------------------------------------------------
--------------------------------------------------------------------------
mpirun detected that one or more processes exited with non-zero status, thus causing
the job to be terminated. The first process to do so was:

  Process name: [[12167,1],10]
  Exit code:    3
```
From my understanding, I haven't set `NCCL_SOCKET_IFNAME` anywhere from my other instances

### sjeaugey · 2025-03-14

Did you ensure you synchronized the binaries between the two nodes? It looks like different ranks running mismatched code.

### rgee18 · 2025-03-14

The process is the same for both nodes and binaries between the two nodes match. Anything specific you want me to check?
