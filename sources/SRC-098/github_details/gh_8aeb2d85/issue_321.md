# [Issue #321] The performance of AlltoAll is not good.

source: https://github.com/NVIDIA/nccl-tests/issues/321
state: closed | updated: 2025-06-14T03:28:02Z
labels: question, more info needed

## 正文

1、In a virtual machine (VM) environment, H20
2、Virtual Machine (VM) Topology Optimization for Performance

```
nvidia-smi topo -m
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    NIC0    NIC1    NIC2    NIC3    NIC4    NIC5    NIC6    NIC7    CPU Affinity    NUMA Affinity     GPU NUMA ID
GPU0     X      NV18    NV18    NV18    NV18    NV18    NV18    NV18    SYS     SYS     SYS     SYS     NODE    NODE    NODE    PIX     0-63    0        N/A
GPU1    NV18     X      NV18    NV18    NV18    NV18    NV18    NV18    SYS     SYS     SYS     SYS     NODE    NODE    PIX     NODE    0-63    0        N/A
GPU2    NV18    NV18     X      NV18    NV18    NV18    NV18    NV18    SYS     SYS     SYS     SYS     NODE    PIX     NODE    NODE    0-63    0        N/A
GPU3    NV18    NV18    NV18     X      NV18    NV18    NV18    NV18    SYS     SYS     SYS     SYS     PIX     NODE    NODE    NODE    0-63    0        N/A
GPU4    NV18    NV18    NV18    NV18     X      NV18    NV18    NV18    NODE    NODE    NODE    PIX     SYS     SYS     SYS     SYS     64-127  1        N/A
GPU5    NV18    NV18    NV18    NV18    NV18     X      NV18    NV18    NODE    NODE    PIX     NODE    SYS     SYS     SYS     SYS     64-127  1        N/A
GPU6    NV18    NV18    NV18    NV18    NV18    NV18     X      NV18    NODE    PIX     NODE    NODE    SYS     SYS     SYS     SYS     64-127  1        N/A
GPU7    NV18    NV18    NV18    NV18    NV18    NV18    NV18     X      PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     64-127  1        N/A
NIC0    SYS     SYS     SYS     SYS     NODE    NODE    NODE    PIX      X      NODE    NODE    NODE    SYS     SYS     SYS     SYS
NIC1    SYS     SYS     SYS     SYS     NODE    NODE    PIX     NODE    NODE     X      NODE    NODE    SYS     SYS     SYS     SYS
NIC2    SYS     SYS     SYS     SYS     NODE    PIX     NODE    NODE    NODE    NODE     X      NODE    SYS     SYS     SYS     SYS
NIC3    SYS     SYS     SYS     SYS     PIX     NODE    NODE    NODE    NODE    NODE    NODE     X      SYS     SYS     SYS     SYS
NIC4    NODE    NODE    NODE    PIX     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS      X      NODE    NODE    NODE
NIC5    NODE    NODE    PIX     NODE    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     NODE     X      NODE    NODE
NIC6    NODE    PIX     NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     NODE    NODE     X      NODE
NIC7    PIX     NODE    NODE    NODE    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     NODE    NODE    NODE     X 
```

3、Here are the commands to execute for optimizing VM topology, categorized by task:

```
mpirun   -np 4   -H 30.159.184.2:2,30.159.184.22:2   -v   --allow-run-as-root   --bind-to none   --map-by slot   --mca btl_tcp_if_include bond0   --mca oob_tcp_if_include bond0   -x NCCL_SOCKET_IFNAME=bond0   -x UCX_NET_DEVICES=bond0   -x NCCL_IB_DISABLE=0   -x NCCL_IB_GID_INDEX=3   -x NCCL_IB_CUDA_SUPPORT=1   -x NCCL_DEBUG=INFO   -x NCCL_IB_HCA=mlx5_bond_6,mlx5_bond_7   -x NCCL_COLLNET_ENABLE=0   -x SHARP_COLL_ENABLE_SAT=0   -x NCCL_NET_GDR_LEVEL=2   -x NCCL_IB_QPS_PER_CONNECTION=4   -x NCCL_IB_TC=160   -x NCCL_PXN_DISABLE=0   --mca btl ^openib   -mca plm_rsh_args "-p 22"   -x CUDA_VISIBLE_DEVICES=1,0 -x NCCL_IB_TIMEOUT=21 -x NCCL_NET_GDR_LEVEL=1   -x NCCL_P2P_LEVEL=NVL  -x LD_LIBRARY_PATH="/data/data/hpcx/ompi/lib:/usr/lib64:/usr/local/cuda-12.2/lib64"   /data/data/nccl-tests-master/build/alltoall_perf   -b 1M -e 16G -f 2 -g 1 -n 200
[1749818353.155524] [vm-host40:34002:0]     ucp_context.c:1951 UCX  WARN  UCP API version is incompatible: required >= 1.15, actual 1.14.0 (loaded from /usr/lib64/libucp.so.0)
[1749818353.158196] [vm-host40:34001:0]     ucp_context.c:1951 UCX  WARN  UCP API version is incompatible: required >= 1.15, actual 1.14.0 (loaded from /usr/lib64/libucp.so.0)
[1749818352.121323] [vm-host38:33958:0]     ucp_context.c:1951 UCX  WARN  UCP API version is incompatible: required >= 1.15, actual 1.14.0 (loaded from /usr/lib64/libucp.so.0)
[1749818352.121551] [vm-host38:33957:0]     ucp_context.c:1951 UCX  WARN  UCP API version is incompatible: required >= 1.15, actual 1.14.0 (loaded from /usr/lib64/libucp.so.0)
[1749818353.311861] [vm-host40:34002:0]     ucp_context.c:1951 UCX  WARN  UCP API version is incompatible: required >= 1.15, actual 1.14.0 (loaded from /usr/lib64/libucp.so.0)
[1749818353.312015] [vm-host40:34001:0]     ucp_context.c:1951 UCX  WARN  UCP API version is incompatible: required >= 1.15, actual 1.14.0 (loaded from /usr/lib64/libucp.so.0)
[1749818352.275396] [vm-host38:33957:0]     ucp_context.c:1951 UCX  WARN  UCP API version is incompatible: required >= 1.15, actual 1.14.0 (loaded from /usr/lib64/libucp.so.0)
[1749818352.275452] [vm-host38:33958:0]     ucp_context.c:1951 UCX  WARN  UCP API version is incompatible: required >= 1.15, actual 1.14.0 (loaded from /usr/lib64/libucp.so.0)
[LOG_CAT_SBGP] libnuma.so: cannot open shared object file: No such file or directory
[LOG_CAT_SBGP] Failed to dlopen libnuma.so. Fallback to GROUP_BY_SOCKET manual.
[LOG_CAT_SBGP] libnuma.so: cannot open shared object file: No such file or directory
[LOG_CAT_SBGP] Failed to dlopen libnuma.so. Fallback to GROUP_BY_SOCKET manual.
[LOG_CAT_SBGP] libnuma.so: cannot open shared object file: No such file or directory
[LOG_CAT_SBGP] Failed to dlopen libnuma.so. Fallback to GROUP_BY_SOCKET manual.
[LOG_CAT_SBGP] libnuma.so: cannot open shared object file: No such file or directory
[LOG_CAT_SBGP] Failed to dlopen libnuma.so. Fallback to GROUP_BY_SOCKET manual.
# nThread 1 nGpus 1 minBytes 1048576 maxBytes 17179869184 step: 2(factor) warmup iters: 5 iters: 200 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid  34001 on  vm-host40 device  0 [0x33] NVIDIA H20-3e
#  Rank  1 Group  0 Pid  34002 on  vm-host40 device  1 [0x23] NVIDIA H20-3e
#  Rank  2 Group  0 Pid  33957 on  vm-host38 device  0 [0x33] NVIDIA H20-3e
#  Rank  3 Group  0 Pid  33958 on  vm-host38 device  1 [0x23] NVIDIA H20-3e
vm-host40:34001:34001 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to bond0
vm-host40:34001:34001 [0] NCCL INFO Bootstrap: Using bond0:30.159.184.22<0>
vm-host40:34001:34001 [0] NCCL INFO cudaDriverVersion 12020
vm-host40:34001:34001 [0] NCCL INFO NCCL version 2.26.5+cuda12.2
vm-host40:34002:34002 [1] NCCL INFO cudaDriverVersion 12020
vm-host40:34002:34002 [1] NCCL INFO NCCL_SOCKET_IFNAME set by environment to bond0
vm-host40:34002:34002 [1] NCCL INFO Bootstrap: Using bond0:30.159.184.22<0>
vm-host40:34002:34002 [1] NCCL INFO NCCL version 2.26.5+cuda12.2
vm-host38:33958:33958 [1] NCCL INFO cudaDriverVersion 12020
vm-host38:33958:33958 [1] NCCL INFO NCCL_SOCKET_IFNAME set by environment to bond0
vm-host38:33958:33958 [1] NCCL INFO Bootstrap: Using bond0:30.159.184.2<0>
vm-host38:33958:33958 [1] NCCL INFO NCCL version 2.26.5+cuda12.2
vm-host38:33957:33957 [0] NCCL INFO cudaDriverVersion 12020
vm-host38:33957:33957 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to bond0
vm-host38:33957:33957 [0] NCCL INFO Bootstrap: Using bond0:30.159.184.2<0>
vm-host38:33957:33957 [0] NCCL INFO NCCL version 2.26.5+cuda12.2
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v10 symbol.
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v9 symbol.
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v8 symbol.
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v7 symbol.
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Loaded net plugin NCCL RDMA Plugin v6 (v6)
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
vm-host40:34002:34044 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
vm-host40:34002:34044 [1] NCCL INFO Plugin Path : /usr/local/lib/libnccl-net.so
vm-host40:34002:34044 [1] NCCL INFO Plugin version : 1.2@Tencent Cloud
vm-host40:34002:34044 [1] NCCL INFO P2P plugin IBext
vm-host40:34002:34044 [1] NCCL INFO NCCL_SOCKET_IFNAME set by environment to bond0
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v10 symbol.
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v9 symbol.
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v8 symbol.
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v7 symbol.
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Loaded net plugin NCCL RDMA Plugin v6 (v6)
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
vm-host40:34001:34043 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
vm-host40:34001:34043 [0] NCCL INFO Plugin Path : /usr/local/lib/libnccl-net.so
vm-host40:34001:34043 [0] NCCL INFO Plugin version : 1.2@Tencent Cloud
vm-host40:34001:34043 [0] NCCL INFO P2P plugin IBext
vm-host40:34001:34043 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to bond0
vm-host40:34002:34044 [1] NCCL INFO NET/IB : Using [0]mlx5_bond_6:1/RoCE [1]mlx5_bond_7:1/RoCE [RO]; OOB bond0:30.159.184.22<0>
vm-host40:34002:34044 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
vm-host40:34002:34044 [1] NCCL INFO Using network NCCL RDMA Plugin v6
vm-host40:34001:34043 [0] NCCL INFO NET/IB : Using [0]mlx5_bond_6:1/RoCE [1]mlx5_bond_7:1/RoCE [RO]; OOB bond0:30.159.184.22<0>
vm-host40:34001:34043 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
vm-host40:34001:34043 [0] NCCL INFO Using network NCCL RDMA Plugin v6
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v10 symbol.
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v9 symbol.
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v8 symbol.
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v7 symbol.
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Loaded net plugin NCCL RDMA Plugin v6 (v6)
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
vm-host38:33958:33999 [1] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
vm-host38:33958:33999 [1] NCCL INFO Plugin Path : /usr/local/lib/libnccl-net.so
vm-host38:33958:33999 [1] NCCL INFO Plugin version : 1.2@Tencent Cloud
vm-host38:33958:33999 [1] NCCL INFO P2P plugin IBext
vm-host38:33958:33999 [1] NCCL INFO NCCL_SOCKET_IFNAME set by environment to bond0
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v10 symbol.
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v9 symbol.
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v8 symbol.
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v7 symbol.
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Loaded net plugin NCCL RDMA Plugin v6 (v6)
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v10 symbol.
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v9 symbol.
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v8 symbol.
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
vm-host38:33957:34000 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v6 symbol.
vm-host38:33957:34000 [0] NCCL INFO Plugin Path : /usr/local/lib/libnccl-net.so
vm-host38:33957:34000 [0] NCCL INFO Plugin version : 1.2@Tencent Cloud
vm-host38:33957:34000 [0] NCCL INFO P2P plugin IBext
vm-host38:33957:34000 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to bond0
vm-host38:33958:33999 [1] NCCL INFO NET/IB : Using [0]mlx5_bond_6:1/RoCE [1]mlx5_bond_7:1/RoCE [RO]; OOB bond0:30.159.184.2<0>
vm-host38:33958:33999 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
vm-host38:33958:33999 [1] NCCL INFO Using network NCCL RDMA Plugin v6
vm-host38:33957:34000 [0] NCCL INFO NET/IB : Using [0]mlx5_bond_6:1/RoCE [1]mlx5_bond_7:1/RoCE [RO]; OOB bond0:30.159.184.2<0>
vm-host38:33957:34000 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so. 
vm-host38:33957:34000 [0] NCCL INFO Using network NCCL RDMA Plugin v6
vm-host40:34002:34044 [1] NCCL INFO ncclCommInitRank comm 0x2725f60 rank 1 nranks 4 cudaDev 1 nvmlDev 0 busId 23000 commId 0x5bfdf821d2742f21 - Init START
vm-host40:34001:34043 [0] NCCL INFO ncclCommInitRank comm 0x3a73f80 rank 0 nranks 4 cudaDev 0 nvmlDev 1 busId 33000 commId 0x5bfdf821d2742f21 - Init START
vm-host38:33958:33999 [1] NCCL INFO ncclCommInitRank comm 0x1faf350 rank 3 nranks 4 cudaDev 1 nvmlDev 0 busId 23000 commId 0x5bfdf821d2742f21 - Init START
vm-host40:34001:34043 [0] NCCL INFO RAS client listening socket at ::1<28028>
vm-host38:33957:34000 [0] NCCL INFO ncclCommInitRank comm 0x1fa2830 rank 2 nranks 4 cudaDev 0 nvmlDev 1 busId 33000 commId 0x5bfdf821d2742f21 - Init START
vm-host40:34002:34044 [1] NCCL INFO RAS client listening socket at ::1<28028>
vm-host38:33957:34000 [0] NCCL INFO RAS client listening socket at ::1<28028>
vm-host38:33958:33999 [1] NCCL INFO RAS client listening socket at ::1<28028>
vm-host40:34002:34044 [1] NCCL INFO Bootstrap timings total 0.068348 (create 0.000123, send 0.000175, recv 0.065782, ring 0.000797, delay 0.000000)
vm-host40:34001:34043 [0] NCCL INFO Bootstrap timings total 0.050942 (create 0.000125, send 0.000172, recv 0.000752, ring 0.029410, delay 0.000000)
vm-host38:33957:34000 [0] NCCL INFO Bootstrap timings total 0.003585 (create 0.000108, send 0.000761, recv 0.000914, ring 0.000302, delay 0.000000)
vm-host38:33958:33999 [1] NCCL INFO Bootstrap timings total 0.051432 (create 0.000147, send 0.000938, recv 0.001048, ring 0.000190, delay 0.000000)
vm-host38:33958:33999 [1] NCCL INFO NCCL_P2P_LEVEL set by environment to NVL
vm-host38:33958:33999 [1] NCCL INFO NCCL_PXN_DISABLE set by environment to 0.
vm-host38:33958:33999 [1] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to PIX
vm-host38:33958:33999 [1] NCCL INFO Setting affinity for GPU 0 to ffffffff,ffffffff
vm-host38:33957:34000 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to NVL
vm-host38:33957:34000 [0] NCCL INFO NCCL_PXN_DISABLE set by environment to 0.
vm-host38:33957:34000 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to PIX
vm-host38:33957:34000 [0] NCCL INFO Setting affinity for GPU 1 to ffffffff,ffffffff
vm-host40:34002:34044 [1] NCCL INFO NCCL_P2P_LEVEL set by environment to NVL
vm-host40:34002:34044 [1] NCCL INFO NCCL_PXN_DISABLE set by environment to 0.
vm-host40:34002:34044 [1] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to PIX
vm-host40:34002:34044 [1] NCCL INFO Setting affinity for GPU 0 to ffffffff,ffffffff
vm-host40:34001:34043 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to NVL
vm-host40:34001:34043 [0] NCCL INFO NCCL_PXN_DISABLE set by environment to 0.
vm-host40:34001:34043 [0] NCCL INFO NCCL_NET_GDR_LEVEL set by environment to PIX
vm-host40:34001:34043 [0] NCCL INFO Setting affinity for GPU 1 to ffffffff,ffffffff
vm-host40:34002:34044 [1] NCCL INFO comm 0x2725f60 rank 1 nRanks 4 nNodes 2 localRanks 2 localRank 1 MNNVL 0
vm-host40:34001:34043 [0] NCCL INFO comm 0x3a73f80 rank 0 nRanks 4 nNodes 2 localRanks 2 localRank 0 MNNVL 0
vm-host40:34001:34043 [0] NCCL INFO Channel 00/04 : 0 3 2 1
vm-host40:34001:34043 [0] NCCL INFO Channel 01/04 : 0 1 2 3
vm-host40:34001:34043 [0] NCCL INFO Channel 02/04 : 0 3 2 1
vm-host40:34001:34043 [0] NCCL INFO Channel 03/04 : 0 1 2 3
vm-host38:33958:33999 [1] NCCL INFO comm 0x1faf350 rank 3 nRanks 4 nNodes 2 localRanks 2 localRank 1 MNNVL 0
vm-host40:34002:34044 [1] NCCL INFO Trees [0] 0/3/-1->1->-1 [1] -1/-1/-1->1->0 [2] 0/-1/-1->1->3 [3] -1/-1/-1->1->0
vm-host40:34002:34044 [1] NCCL INFO P2P Chunksize set to 131072
vm-host40:34001:34043 [0] NCCL INFO Trees [0] -1/-1/-1->0->1 [1] 1/2/-1->0->-1 [2] -1/-1/-1->0->1 [3] 1/-1/-1->0->2
vm-host40:34001:34043 [0] NCCL INFO P2P Chunksize set to 131072
vm-host40:34001:34043 [0] NCCL INFO Check P2P Type intraNodeP2pSupport 1 directMode 0
vm-host38:33957:34000 [0] NCCL INFO comm 0x1fa2830 rank 2 nRanks 4 nNodes 2 localRanks 2 localRank 0 MNNVL 0
vm-host38:33958:33999 [1] NCCL INFO Trees [0] 2/-1/-1->3->1 [1] -1/-1/-1->3->2 [2] 2/1/-1->3->-1 [3] -1/-1/-1->3->2
vm-host38:33958:33999 [1] NCCL INFO P2P Chunksize set to 131072
vm-host38:33957:34000 [0] NCCL INFO Trees [0] -1/-1/-1->2->3 [1] 3/-1/-1->2->0 [2] -1/-1/-1->2->3 [3] 3/0/-1->2->-1
vm-host38:33957:34000 [0] NCCL INFO P2P Chunksize set to 131072
vm-host40:34001:34053 [0] NCCL INFO [Proxy Service] Device 0 CPU core 3
vm-host38:33958:34012 [1] NCCL INFO [Proxy Service] Device 1 CPU core 5
vm-host38:33957:34013 [0] NCCL INFO [Proxy Service] Device 0 CPU core 9
vm-host38:33958:34014 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 11
vm-host38:33957:34015 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 13
vm-host40:34001:34054 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 5
vm-host40:34002:34055 [1] NCCL INFO [Proxy Service] Device 1 CPU core 7
vm-host40:34002:34056 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 9
vm-host38:33958:33999 [1] NCCL INFO threadThresholds 8/8/64 | 32/8/64 | 512 | 512
vm-host38:33958:33999 [1] NCCL INFO 4 coll channels, 4 collnet channels, 0 nvls channels, 4 p2p channels, 2 p2p channels per peer
vm-host38:33957:34000 [0] NCCL INFO threadThresholds 8/8/64 | 32/8/64 | 512 | 512
vm-host38:33957:34000 [0] NCCL INFO 4 coll channels, 4 collnet channels, 0 nvls channels, 4 p2p channels, 2 p2p channels per peer
vm-host40:34001:34043 [0] NCCL INFO threadThresholds 8/8/64 | 32/8/64 | 512 | 512
vm-host40:34001:34043 [0] NCCL INFO 4 coll channels, 4 collnet channels, 0 nvls channels, 4 p2p channels, 2 p2p channels per peer
vm-host40:34001:34043 [0] NCCL INFO CC Off, workFifoBytes 1048576
vm-host38:33958:33999 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so. Using internal tuner plugin.
vm-host38:33958:33999 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
vm-host38:33958:33999 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
vm-host38:33958:33999 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
vm-host38:33958:33999 [1] NCCL INFO ncclCommInitRank comm 0x1faf350 rank 3 nranks 4 cudaDev 1 nvmlDev 0 busId 23000 commId 0x5bfdf821d2742f21 - Init COMPLETE
vm-host38:33958:33999 [1] NCCL INFO Init timings - ncclCommInitRank: rank 3 nranks 4 total 1.07 (kernels 0.44, alloc 0.43, bootstrap 0.05, allgathers 0.01, topo 0.14, graphs 0.00, connections 0.00, rest 0.00)
vm-host38:33957:34000 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so. Using internal tuner plugin.
vm-host38:33957:34000 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
vm-host38:33957:34000 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
vm-host38:33957:34000 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
vm-host38:33957:34000 [0] NCCL INFO ncclCommInitRank comm 0x1fa2830 rank 2 nranks 4 cudaDev 0 nvmlDev 1 busId 33000 commId 0x5bfdf821d2742f21 - Init COMPLETE
vm-host38:33957:34000 [0] NCCL INFO Init timings - ncclCommInitRank: rank 2 nranks 4 total 1.07 (kernels 0.46, alloc 0.44, bootstrap 0.00, allgathers 0.02, topo 0.14, graphs 0.00, connections 0.00, rest 0.00)
vm-host40:34002:34044 [1] NCCL INFO threadThresholds 8/8/64 | 32/8/64 | 512 | 512
vm-host40:34002:34044 [1] NCCL INFO 4 coll channels, 4 collnet channels, 0 nvls channels, 4 p2p channels, 2 p2p channels per peer
vm-host40:34001:34043 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so. Using internal tuner plugin.
vm-host40:34001:34043 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
vm-host40:34001:34043 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
vm-host40:34001:34043 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
vm-host40:34002:34044 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so. Using internal tuner plugin.
vm-host40:34002:34044 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v4 symbol.
vm-host40:34002:34044 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
vm-host40:34002:34044 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
vm-host40:34002:34044 [1] NCCL INFO ncclCommInitRank comm 0x2725f60 rank 1 nranks 4 cudaDev 1 nvmlDev 0 busId 23000 commId 0x5bfdf821d2742f21 - Init COMPLETE
vm-host40:34002:34044 [1] NCCL INFO Init timings - ncclCommInitRank: rank 1 nranks 4 total 1.10 (kernels 0.40, alloc 0.46, bootstrap 0.07, allgathers 0.02, topo 0.15, graphs 0.00, connections 0.00, rest 0.00)
vm-host40:34001:34043 [0] NCCL INFO ncclCommInitRank comm 0x3a73f80 rank 0 nranks 4 cudaDev 0 nvmlDev 1 busId 33000 commId 0x5bfdf821d2742f21 - Init COMPLETE
vm-host40:34001:34043 [0] NCCL INFO Init timings - ncclCommInitRank: rank 0 nranks 4 total 1.10 (kernels 0.40, alloc 0.48, bootstrap 0.05, allgathers 0.01, topo 0.15, graphs 0.00, connections 0.00, rest 0.00)
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
vm-host38:33957:34019 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 7
vm-host38:33957:34018 [0] NCCL INFO Channel 01/1 : 1[0] -> 2[1] [receive] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host38:33958:34017 [1] NCCL INFO Channel 01/1 : 3[0] -> 0[1] [send] via NET/NCCL RDMA Plugin v6/0(2)/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 03/1 : 1[0] -> 2[1] [receive] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 00/1 : 2[1] -> 3[0] via P2P/CUMEM
vm-host38:33958:34017 [1] NCCL INFO Channel 03/1 : 3[0] -> 0[1] [send] via NET/NCCL RDMA Plugin v6/0(2)/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 02/1 : 2[1] -> 3[0] via P2P/CUMEM
vm-host40:34001:34059 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 61
vm-host40:34001:34058 [0] NCCL INFO Channel 01/1 : 3[0] -> 0[1] [receive] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host40:34001:34058 [0] NCCL INFO Channel 03/1 : 3[0] -> 0[1] [receive] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host40:34002:34057 [1] NCCL INFO Channel 01/1 : 1[0] -> 2[1] [send] via NET/NCCL RDMA Plugin v6/0(0)/GDRDMA/Shared
vm-host40:34001:34058 [0] NCCL INFO Channel 00/1 : 0[1] -> 1[0] via P2P/CUMEM
vm-host40:34001:34058 [0] NCCL INFO Channel 02/1 : 0[1] -> 1[0] via P2P/CUMEM
vm-host40:34002:34057 [1] NCCL INFO Channel 03/1 : 1[0] -> 2[1] [send] via NET/NCCL RDMA Plugin v6/0(0)/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 01/1 : 0[1] -> 2[1] [receive] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host40:34001:34058 [0] NCCL INFO Channel 01/1 : 2[1] -> 0[1] [receive] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 03/1 : 0[1] -> 2[1] [receive] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host40:34001:34058 [0] NCCL INFO Channel 03/1 : 2[1] -> 0[1] [receive] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host40:34001:34058 [0] NCCL INFO Channel 01/1 : 0[1] -> 2[1] [send] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host40:34001:34058 [0] NCCL INFO Channel 03/1 : 0[1] -> 2[1] [send] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 01/1 : 2[1] -> 0[1] [send] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 03/1 : 2[1] -> 0[1] [send] via NET/NCCL RDMA Plugin v6/0/GDRDMA/Shared
vm-host38:33958:34020 [1] NCCL INFO [Proxy Progress] Device 1 CPU core 9
vm-host38:33958:34017 [1] NCCL INFO Channel 01/1 : 1[0] -> 3[0] [receive] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 01/1 : 2[1] -> 1[0] [send] via NET/NCCL RDMA Plugin v6/1(3)/GDRDMA/Shared
vm-host38:33958:34017 [1] NCCL INFO Channel 03/1 : 1[0] -> 3[0] [receive] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host38:33957:34018 [0] NCCL INFO Channel 03/1 : 2[1] -> 1[0] [send] via NET/NCCL RDMA Plugin v6/1(3)/GDRDMA/Shared
vm-host38:33958:34017 [1] NCCL INFO Channel 01/1 : 3[0] -> 1[0] [send] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host38:33958:34017 [1] NCCL INFO Channel 03/1 : 3[0] -> 1[0] [send] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host40:34002:34061 [1] NCCL INFO [Proxy Progress] Device 1 CPU core 7
vm-host40:34002:34057 [1] NCCL INFO Channel 01/1 : 3[0] -> 1[0] [receive] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host40:34001:34058 [0] NCCL INFO Channel 01/1 : 0[1] -> 3[0] [send] via NET/NCCL RDMA Plugin v6/1(1)/GDRDMA/Shared
vm-host40:34002:34057 [1] NCCL INFO Channel 03/1 : 3[0] -> 1[0] [receive] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host40:34001:34058 [0] NCCL INFO Channel 03/1 : 0[1] -> 3[0] [send] via NET/NCCL RDMA Plugin v6/1(1)/GDRDMA/Shared
vm-host40:34002:34057 [1] NCCL INFO Channel 01/1 : 1[0] -> 3[0] [send] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host40:34002:34057 [1] NCCL INFO Channel 03/1 : 1[0] -> 3[0] [send] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host38:33958:34017 [1] NCCL INFO Channel 01/1 : 0[1] -> 3[0] [receive] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host40:34002:34057 [1] NCCL INFO Channel 01/1 : 2[1] -> 1[0] [receive] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host40:34002:34057 [1] NCCL INFO Channel 03/1 : 2[1] -> 1[0] [receive] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host40:34002:34057 [1] NCCL INFO Channel 00/1 : 1[0] -> 0[1] via P2P/CUMEM
vm-host38:33958:34017 [1] NCCL INFO Channel 03/1 : 0[1] -> 3[0] [receive] via NET/NCCL RDMA Plugin v6/1/GDRDMA/Shared
vm-host40:34002:34057 [1] NCCL INFO Channel 02/1 : 1[0] -> 0[1] via P2P/CUMEM
vm-host38:33958:34017 [1] NCCL INFO Channel 00/1 : 3[0] -> 2[1] via P2P/CUMEM
vm-host38:33958:34017 [1] NCCL INFO Channel 02/1 : 3[0] -> 2[1] via P2P/CUMEM
vm-host40:34001:34053 [0] NCCL INFO NCCL_IB_QPS_PER_CONNECTION set by environment to 4.
vm-host40:34001:34053 [0] NCCL INFO NCCL_IB_GID_INDEX set by environment to 3.
vm-host38:33957:34013 [0] NCCL INFO NCCL_IB_GID_INDEX set by environment to 3.
vm-host38:33957:34013 [0] NCCL INFO NCCL_IB_QPS_PER_CONNECTION set by environment to 4.
vm-host38:33957:34013 [0] NCCL INFO NCCL_IB_TC set by environment to 160.
vm-host38:33957:34013 [0] NCCL INFO NCCL_IB_TIMEOUT set by environment to 21.
vm-host40:34002:34055 [1] NCCL INFO NCCL_IB_QPS_PER_CONNECTION set by environment to 4.
vm-host40:34002:34055 [1] NCCL INFO NCCL_IB_GID_INDEX set by environment to 3.
vm-host38:33958:34012 [1] NCCL INFO NCCL_IB_QPS_PER_CONNECTION set by environment to 4.
vm-host38:33958:34012 [1] NCCL INFO NCCL_IB_GID_INDEX set by environment to 3.
vm-host38:33958:34012 [1] NCCL INFO NCCL_IB_TC set by environment to 160.
vm-host40:34001:34053 [0] NCCL INFO NCCL_IB_TC set by environment to 160.
vm-host40:34002:34055 [1] NCCL INFO NCCL_IB_TC set by environment to 160.
vm-host40:34001:34053 [0] NCCL INFO NCCL_IB_TIMEOUT set by environment to 21.
vm-host40:34002:34055 [1] NCCL INFO NCCL_IB_TIMEOUT set by environment to 21.
vm-host38:33958:34012 [1] NCCL INFO NCCL_IB_TIMEOUT set by environment to 21.
     1048576         65536     float    none      -1    52.94   19.81   14.85      0    53.47   19.61   14.71    N/A
     2097152        131072     float    none      -1    72.12   29.08   21.81      0    80.45   26.07   19.55    N/A
     4194304        262144     float    none      -1    95.86   43.75   32.82      0    94.87   44.21   33.16    N/A
     8388608        524288     float    none      -1    156.4   53.63   40.22      0    155.6   53.90   40.43    N/A
    16777216       1048576     float    none      -1    288.0   58.25   43.69      0    288.0   58.26   43.69    N/A
    33554432       2097152     float    none      -1    538.8   62.28   46.71      0    537.1   62.47   46.85    N/A
    67108864       4194304     float    none      -1   1038.5   64.62   48.46      0   1039.0   64.59   48.44    N/A
   134217728       8388608     float    none      -1   2040.8   65.77   49.32      0   2037.6   65.87   49.40    N/A
   268435456      16777216     float    none      -1   4041.6   66.42   49.81      0   4034.6   66.53   49.90    N/A
   536870912      33554432     float    none      -1   8034.6   66.82   50.11      0   8030.2   66.86   50.14    N/A
  1073741824      67108864     float    none      -1    16035   66.96   50.22      0    16110   66.65   49.99    N/A
  2147483648     134217728     float    none      -1    34234   62.73   47.05      0    33309   64.47   48.35    N/A
  4294967296     268435456     float    none      -1    64101   67.00   50.25      0    63946   67.17   50.37    N/A
```


## 评论 (3)

### kiskra-nvidia · 2025-06-13

> vm-host40:34001:34043 [0] NCCL INFO Plugin Path : /usr/local/lib/libnccl-net.so
> vm-host40:34001:34043 [0] NCCL INFO Plugin version : 1.2@Tencent Cloud

Note that we have no experience with this plugin. What is the underlying network? What is your performance expectation in this case? With send/recv traffic (which is what alltoall uses) you may want to try increasing `NCCL_NCHANNELS_PER_NET_PEER` to 2 or 4 and see if that helps...

### AddyLaddy · 2025-06-13

The SOL for A2A is effectively the line rate of an individual NIC (assuming each GPU has a dedicated NIC). But when combining NVL and IB/RoCE the number reported can be hard to calculate, and can exceed the NIC line rate at smaller scales.





### PaggyZhang · 2025-06-14

This plugin is compiled based on nccl-sharp.Thanks,NCCL_NCHANNELS_PER_NET_PEER is key.
