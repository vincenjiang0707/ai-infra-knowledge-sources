# [Issue #311] CollNet randomly hangs or fallbacks to P2P

source: https://github.com/NVIDIA/nccl-tests/issues/311
state: open | updated: 2025-05-27T07:02:36Z
labels: more info needed

## 正文

Hi, 

When running `all_reduce_perf` with 4 nodes x 2 A100-SMX4 per node, i.e. 8 GPUs in total, `collnet` either hangs or fallbacks to P2P. 

### System infomation 
- CPU: 2x AMD EPYC 7543 (NPS4) 
- GPU: 8x A100-SMX4 (Driver: 550.54.14) 
- Interconnect: MT4123 (Melanox ConnectX-6)  
- GPU:NIC = 2:1 (2x A100 sharing one NIC) 
<details>
<summary>Topology</summary>

```
         GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    NIC0    NIC1    NIC2    NIC3    NIC4    NIC5    NIC6    NIC7NIC8    NIC9    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      NV12    NV12    NV12    NV12    NV12    NV12    NV12    PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYSSYS      SYS     24-31,88-95     3               N/A
GPU1    NV12     X      NV12    NV12    NV12    NV12    NV12    NV12    PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYSSYS      SYS     24-31,88-95     3               N/A
GPU2    NV12    NV12     X      NV12    NV12    NV12    NV12    NV12    SYS     SYS     PXB     PXB     SYS     SYS     SYS     SYSSYS      SYS     8-15,72-79      1               N/A
GPU3    NV12    NV12    NV12     X      NV12    NV12    NV12    NV12    SYS     SYS     PXB     PXB     SYS     SYS     SYS     SYSSYS      SYS     8-15,72-79      1               N/A
GPU4    NV12    NV12    NV12    NV12     X      NV12    NV12    NV12    SYS     SYS     SYS     SYS     PXB     PXB     SYS     SYSSYS      SYS     56-63,120-127   7               N/A
GPU5    NV12    NV12    NV12    NV12    NV12     X      NV12    NV12    SYS     SYS     SYS     SYS     PXB     PXB     SYS     SYSSYS      SYS     56-63,120-127   7               N/A
GPU6    NV12    NV12    NV12    NV12    NV12    NV12     X      NV12    SYS     SYS     SYS     SYS     SYS     SYS     PXB     PXBSYS      SYS     40-47,104-111   5               N/A
GPU7    NV12    NV12    NV12    NV12    NV12    NV12    NV12     X      SYS     SYS     SYS     SYS     SYS     SYS     PXB     PXBSYS      SYS     40-47,104-111   5               N/A
NIC0    PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYS      X      PIX     SYS     SYS     SYS     SYS     SYS     SYSSYS      SYS
NIC1    PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYS     PIX      X      SYS     SYS     SYS     SYS     SYS     SYSSYS      SYS
NIC2    SYS     SYS     PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYS      X      PIX     SYS     SYS     SYS     SYSSYS      SYS
NIC3    SYS     SYS     PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYS     PIX      X      SYS     SYS     SYS     SYSSYS      SYS
NIC4    SYS     SYS     SYS     SYS     PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYS      X      PIX     SYS     SYSSYS      SYS
NIC5    SYS     SYS     SYS     SYS     PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYS     PIX      X      SYS     SYSSYS      SYS
NIC6    SYS     SYS     SYS     SYS     SYS     SYS     PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYS      X      PIXSYS      SYS
NIC7    SYS     SYS     SYS     SYS     SYS     SYS     PXB     PXB     SYS     SYS     SYS     SYS     SYS     SYS     PIX      X SYS      SYS
NIC8    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS X       PIX
NIC9    SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYS     SYSPIX       X

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
  NIC4: mlx5_4
  NIC5: mlx5_5
  NIC6: mlx5_6
  NIC7: mlx5_7
  NIC8: mlx5_8
  NIC9: mlx5_9
```
</details>

<details> 
<summary> sharp_hello test result </summary>

```
[gpu34:0:40581 - context.c:665][2025-05-26 15:58:56] INFO job (ID: 10883548833119725849) resource request quota: ( osts:0 user_data_per_ost:0 max_groups:0 max_qps:1 max_group_channels:1, num_trees:1)
[gpu34:0:40581 - context.c:867][2025-05-26 15:58:56] INFO sharp_job_id:41   resv_key: tree_type:LLT tree_idx:0  treeID:18 caps:0x5 quota:(osts:167 user_data_per_ost:1024 max_groups:167 max_qps:1 max_group_channels:1)
[gpu34:0:40581 - comm.c:413][2025-05-26 15:58:56] INFO [group#:0] job_id:41 group id:0 tree idx:0 tree_type:LLT rail_idx:0 group size:1 quota: (osts:8 user_data_per_ost:1024) mgid: (subnet prefix:0x0 interface id:0x0) mlid:0
Test Passed.
```
</details> 

### Softwares 
- OpenMPI: v4.1.7 
- CUDA: v12.3 
- NCCL: v2.23.4
- SHARP: v3.5.0 (from Mellanox OFED) 
- nccl-rdma-sharp-plugin: https://github.com/Mellanox/nccl-rdma-sharp-plugins/commit/b2e92a4b87e23705d2004ab174b7d0293bfb6d48
- nccl-tests: https://github.com/NVIDIA/nccl-tests/commit/e041d901e6d3dabb67a22905cba77d9ba2689898 

### Job Script
```
module load gcc/12.2.0 cuda/12.3 cudampi/openmpi-4.1.7
module load nccl/2.23.4

export HPCX_SHARP_DIR=/opt/mellanox/sharp

export LD_LIBRARY_PATH=\
/scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs:\
$LD_LIBRARY_PATH

mpirun                        \
    -np 8                     \
    -mca btl ^openib          \
    -x NCCL_DEBUG=info        \
    -x NCCL_COLLNET_ENABLE=1  \
    -x SHARP_COLL_LOG_LEVEL=3 \
    ./build/nccl-tests/build/all_reduce_perf \
    -b 16 -e 4G -f 4 -g 1 
```
Followling NVIDIA documentation, I have: 
- Point `HPCX_SHARP_DIR` to SHARP installation bundled with Mellanox OFED. 
- Make sure that `libnccl-net.so` can be found from `LD_LIBRARY_PATH` 
- Enable collnet with `NCCL_COLLNET_ENABLE=1` 
 
### CollNet hangs 
<details> 
<summary> With NCCL_DEBUG=info </summary>

```
# nThread 1 nGpus 1 minBytes 16 maxBytes 4294967296 step: 4(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid  23654 on      gpu34 device  0 [0000:07:00] NVIDIA A100-SXM4-80GB
#  Rank  1 Group  0 Pid  23655 on      gpu34 device  1 [0000:0b:00] NVIDIA A100-SXM4-80GB
#  Rank  2 Group  0 Pid  15433 on      gpu36 device  0 [0000:88:00] NVIDIA A100-SXM4-80GB
#  Rank  3 Group  0 Pid  15434 on      gpu36 device  1 [0000:cb:00] NVIDIA A100-SXM4-80GB
#  Rank  4 Group  0 Pid   2899 on      gpu40 device  0 [0000:4c:00] NVIDIA A100-SXM4-80GB
#  Rank  5 Group  0 Pid   2900 on      gpu40 device  1 [0000:88:00] NVIDIA A100-SXM4-80GB
#  Rank  6 Group  0 Pid  63046 on      gpu41 device  0 [0000:07:00] NVIDIA A100-SXM4-80GB
#  Rank  7 Group  0 Pid  63047 on      gpu41 device  1 [0000:88:00] NVIDIA A100-SXM4-80GB
gpu34:23654:23654 [0] NCCL INFO Bootstrap : Using ib0:10.159.0.34<0>
gpu36:15434:15434 [1] NCCL INFO cudaDriverVersion 12040
gpu34:23654:23654 [0] NCCL INFO cudaDriverVersion 12040
gpu34:23655:23655 [1] NCCL INFO cudaDriverVersion 12040
gpu36:15433:15433 [0] NCCL INFO cudaDriverVersion 12040
gpu40:2899:2899 [0] NCCL INFO cudaDriverVersion 12040
gpu40:2900:2900 [1] NCCL INFO cudaDriverVersion 12040
gpu41:63047:63047 [1] NCCL INFO cudaDriverVersion 12040
gpu41:63046:63046 [0] NCCL INFO cudaDriverVersion 12040
gpu34:23654:23654 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu34:23655:23655 [1] NCCL INFO Bootstrap : Using ib0:10.159.0.34<0>
gpu34:23655:23655 [1] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu36:15434:15434 [1] NCCL INFO Bootstrap : Using ib0:10.159.0.36<0>
gpu36:15433:15433 [0] NCCL INFO Bootstrap : Using ib0:10.159.0.36<0>
gpu36:15433:15433 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu36:15434:15434 [1] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu40:2899:2899 [0] NCCL INFO Bootstrap : Using ib0:10.159.0.40<0>
gpu40:2899:2899 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu40:2900:2900 [1] NCCL INFO Bootstrap : Using ib0:10.159.0.40<0>
gpu40:2900:2900 [1] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu41:63047:63047 [1] NCCL INFO Bootstrap : Using ib0:10.159.0.41<0>
gpu41:63046:63046 [0] NCCL INFO Bootstrap : Using ib0:10.159.0.41<0>
gpu41:63046:63046 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu41:63047:63047 [1] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu34:23654:23684 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu34:23654:23684 [0] NCCL INFO P2P plugin v8 IBext_v8
gpu34:23655:23685 [1] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu34:23655:23685 [1] NCCL INFO P2P plugin v8 IBext_v8
gpu40:2899:2929 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu40:2899:2929 [0] NCCL INFO P2P plugin v8 IBext_v8
gpu40:2900:2930 [1] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu40:2900:2930 [1] NCCL INFO P2P plugin v8 IBext_v8
gpu41:63046:63077 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu41:63046:63077 [0] NCCL INFO P2P plugin v8 IBext_v8
gpu36:15434:15500 [1] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu36:15434:15500 [1] NCCL INFO P2P plugin v8 IBext_v8
gpu36:15433:15499 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu36:15433:15499 [0] NCCL INFO P2P plugin v8 IBext_v8
gpu41:63047:63078 [1] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu41:63047:63078 [1] NCCL INFO P2P plugin v8 IBext_v8
gpu40:2900:2930 [1] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.40<0>
gpu40:2899:2929 [0] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.40<0>
gpu40:2900:2930 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu40:2899:2929 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu40:2899:2929 [0] NCCL INFO Using network IBext_v8
gpu40:2900:2930 [1] NCCL INFO Using network IBext_v8
gpu34:23654:23684 [0] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.34<0>
gpu34:23655:23685 [1] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.34<0>
gpu34:23654:23684 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu34:23654:23684 [0] NCCL INFO Using network IBext_v8
gpu34:23655:23685 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu34:23655:23685 [1] NCCL INFO Using network IBext_v8
gpu36:15434:15500 [1] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.36<0>
gpu41:63046:63077 [0] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.41<0>
gpu36:15433:15499 [0] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.36<0>
gpu41:63046:63077 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu41:63046:63077 [0] NCCL INFO Using network IBext_v8
gpu36:15434:15500 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu41:63047:63078 [1] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.41<0>
gpu36:15434:15500 [1] NCCL INFO Using network IBext_v8
gpu41:63047:63078 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu41:63047:63078 [1] NCCL INFO Using network IBext_v8
gpu36:15433:15499 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu36:15433:15499 [0] NCCL INFO Using network IBext_v8
gpu40:2899:2929 [0] NCCL INFO ncclCommInitRank comm 0x5289720 rank 4 nranks 8 cudaDev 0 nvmlDev 0 busId 4c000 commId 0x45701cda3f259923 - Init START
gpu40:2900:2930 [1] NCCL INFO ncclCommInitRank comm 0x617db00 rank 5 nranks 8 cudaDev 1 nvmlDev 1 busId 88000 commId 0x45701cda3f259923 - Init START
gpu34:23654:23684 [0] NCCL INFO ncclCommInitRank comm 0x5aae1d0 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 7000 commId 0x45701cda3f259923 - Init START
gpu34:23655:23685 [1] NCCL INFO ncclCommInitRank comm 0x60005e0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId b000 commId 0x45701cda3f259923 - Init START
gpu41:63046:63077 [0] NCCL INFO ncclCommInitRank comm 0x55b2020 rank 6 nranks 8 cudaDev 0 nvmlDev 0 busId 7000 commId 0x45701cda3f259923 - Init START
gpu36:15434:15500 [1] NCCL INFO ncclCommInitRank comm 0x5464220 rank 3 nranks 8 cudaDev 1 nvmlDev 1 busId cb000 commId 0x45701cda3f259923 - Init START
gpu36:15433:15499 [0] NCCL INFO ncclCommInitRank comm 0x6426550 rank 2 nranks 8 cudaDev 0 nvmlDev 0 busId 88000 commId 0x45701cda3f259923 - Init START
gpu41:63047:63078 [1] NCCL INFO ncclCommInitRank comm 0x6a02830 rank 7 nranks 8 cudaDev 1 nvmlDev 1 busId 88000 commId 0x45701cda3f259923 - Init START
gpu34:23654:23684 [0] NCCL INFO Bootstrap timings total 0.015323 (create 0.000016, send 0.008211, recv 0.005053, ring 0.000517, delay 0.000000)
gpu40:2900:2930 [1] NCCL INFO Bootstrap timings total 0.016299 (create 0.000062, send 0.000124, recv 0.014486, ring 0.001366, delay 0.000001)
gpu41:63047:63078 [1] NCCL INFO Bootstrap timings total 0.001078 (create 0.000091, send 0.000140, recv 0.000208, ring 0.000394, delay 0.000001)
gpu41:63046:63077 [0] NCCL INFO Bootstrap timings total 0.009451 (create 0.000092, send 0.000196, recv 0.008524, ring 0.000352, delay 0.000001)
gpu34:23655:23685 [1] NCCL INFO Bootstrap timings total 0.011128 (create 0.000032, send 0.000081, recv 0.008798, ring 0.002030, delay 0.000001)
gpu40:2899:2929 [0] NCCL INFO Bootstrap timings total 0.018614 (create 0.000038, send 0.000246, recv 0.002004, ring 0.002037, delay 0.000001)
gpu36:15434:15500 [1] NCCL INFO Bootstrap timings total 0.007906 (create 0.000036, send 0.000281, recv 0.005323, ring 0.002012, delay 0.000001)
gpu36:15433:15499 [0] NCCL INFO Bootstrap timings total 0.007691 (create 0.000041, send 0.000166, recv 0.005303, ring 0.002005, delay 0.000001)
gpu36:15433:15499 [0] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu36:15434:15500 [1] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu41:63046:63077 [0] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu41:63047:63078 [1] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu40:2899:2929 [0] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu40:2900:2930 [1] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu34:23654:23684 [0] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu34:23655:23685 [1] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu34:23654:23684 [0] NCCL INFO comm 0x5aae1d0 rank 0 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0
gpu34:23654:23684 [0] NCCL INFO Channel 00/03 : 0 1 2 3 4 5 6 7
gpu34:23654:23684 [0] NCCL INFO Channel 01/03 : 0 1 2 3 4 5 6 7
gpu34:23654:23684 [0] NCCL INFO Channel 02/03 : 0 1 2 3 4 5 6 7
gpu34:23654:23684 [0] NCCL INFO Trees [0] 1/4/-1->0->-1 [1] 1/-1/-1->0->2 [2] 1/4/-1->0->-1
gpu34:23654:23684 [0] NCCL INFO P2P Chunksize set to 131072
gpu41:63047:63078 [1] NCCL INFO comm 0x6a02830 rank 7 nRanks 8 nNodes 4 localRanks 2 localRank 1 MNNVL 0
gpu40:2900:2930 [1] NCCL INFO comm 0x617db00 rank 5 nRanks 8 nNodes 4 localRanks 2 localRank 1 MNNVL 0
gpu36:15434:15500 [1] NCCL INFO comm 0x5464220 rank 3 nRanks 8 nNodes 4 localRanks 2 localRank 1 MNNVL 0
gpu41:63046:63077 [0] NCCL INFO comm 0x55b2020 rank 6 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0
gpu41:63046:63077 [0] NCCL INFO Trees [0] 7/-1/-1->6->4 [1] 7/2/-1->6->-1 [2] 7/-1/-1->6->4
gpu41:63046:63077 [0] NCCL INFO P2P Chunksize set to 131072
gpu40:2899:2929 [0] NCCL INFO comm 0x5289720 rank 4 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0
gpu40:2899:2929 [0] NCCL INFO Trees [0] 5/6/-1->4->0 [1] 5/-1/-1->4->3 [2] 5/6/-1->4->0
gpu40:2899:2929 [0] NCCL INFO P2P Chunksize set to 131072
gpu36:15433:15499 [0] NCCL INFO comm 0x6426550 rank 2 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0
gpu36:15433:15499 [0] NCCL INFO Trees [0] 3/-1/-1->2->5 [1] 3/0/-1->2->6 [2] 3/-1/-1->2->5
gpu36:15433:15499 [0] NCCL INFO P2P Chunksize set to 131072
gpu40:2900:2930 [1] NCCL INFO Trees [0] 2/-1/-1->5->4 [1] -1/-1/-1->5->4 [2] 2/-1/-1->5->4
gpu36:15434:15500 [1] NCCL INFO Trees [0] -1/-1/-1->3->2 [1] 4/-1/-1->3->2 [2] -1/-1/-1->3->2
gpu41:63047:63078 [1] NCCL INFO Trees [0] -1/-1/-1->7->6 [1] -1/-1/-1->7->6 [2] -1/-1/-1->7->6
gpu40:2900:2930 [1] NCCL INFO P2P Chunksize set to 131072
gpu36:15434:15500 [1] NCCL INFO P2P Chunksize set to 131072
gpu41:63047:63078 [1] NCCL INFO P2P Chunksize set to 131072
gpu34:23655:23685 [1] NCCL INFO comm 0x60005e0 rank 1 nRanks 8 nNodes 4 localRanks 2 localRank 1 MNNVL 0
gpu34:23655:23685 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0 [2] -1/-1/-1->1->0
gpu34:23655:23685 [1] NCCL INFO P2P Chunksize set to 131072
gpu34:23654:23703 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 8
gpu34:23654:23702 [0] NCCL INFO [Proxy Service] Device 0 CPU core 8
gpu36:15433:15519 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 16
gpu40:2900:2950 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 36
gpu36:15433:15517 [0] NCCL INFO [Proxy Service] Device 0 CPU core 16
gpu40:2900:2949 [1] NCCL INFO [Proxy Service] Device 1 CPU core 36
gpu41:63046:63098 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 8
gpu41:63046:63096 [0] NCCL INFO [Proxy Service] Device 0 CPU core 8
gpu36:15434:15520 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 48
gpu36:15434:15518 [1] NCCL INFO [Proxy Service] Device 1 CPU core 48
gpu41:63047:63099 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 40
gpu40:2899:2948 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 20
gpu40:2899:2947 [0] NCCL INFO [Proxy Service] Device 0 CPU core 20
gpu34:23655:23705 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 40
gpu41:63047:63097 [1] NCCL INFO [Proxy Service] Device 1 CPU core 40
gpu34:23655:23704 [1] NCCL INFO [Proxy Service] Device 1 CPU core 40
gpu34:23654:23684 [0] NCCL INFO CollNet 00/0 : 0 [receive] via COLLNET/SHARP/1/GDRDMA
gpu41:63046:63077 [0] NCCL INFO CollNet 00/0 : 6 [receive] via COLLNET/SHARP/1/GDRDMA
gpu36:15433:15499 [0] NCCL INFO CollNet 00/0 : 2 [receive] via COLLNET/SHARP/5/GDRDMA
gpu40:2899:2929 [0] NCCL INFO CollNet 00/0 : 4 [receive] via COLLNET/SHARP/0/GDRDMA
gpu34:23654:23706 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 8
gpu36:15433:15521 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 16
gpu41:63046:63100 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 8
gpu40:2899:2951 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 20
[gpu34:0:23654 - context.c:665][2025-05-26 15:20:21] INFO job (ID: 10883559310443912581) resource request quota: ( osts:0 user_data_per_ost:0 max_groups:0 max_qps:1 max_group_channels:1, num_trees:1)
[gpu34:0:23654 - context.c:867][2025-05-26 15:20:21] INFO sharp_job_id:36   resv_key: tree_type:LLT tree_idx:0  treeID:15 caps:0x5 quota:(osts:25 user_data_per_ost:1024 max_groups:25 max_qps:1 max_group_channels:1)
[gpu34:0:23654 - context.c:874][2025-05-26 15:20:21] INFO sharp_job_id:36   tree_type:SAT tree_idx:1  treeID:47 caps:0x15

gpu36:15433:15517 [0] sharp_plugin.c:382 NCCL WARN SHARP int8,uint8,bfloat16 Datatypes not supported
gpu36:15433:15517 [0] NCCL INFO SHARP rank 1/4 initialized on mlx5_4:1

gpu40:2899:2947 [0] sharp_plugin.c:382 NCCL WARN SHARP int8,uint8,bfloat16 Datatypes not supported
gpu40:2899:2947 [0] NCCL INFO SHARP rank 2/4 initialized on mlx5_2:1

gpu41:63046:63096 [0] sharp_plugin.c:382 NCCL WARN SHARP int8,uint8,bfloat16 Datatypes not supported
gpu41:63046:63096 [0] NCCL INFO SHARP rank 3/4 initialized on mlx5_0:1

gpu34:23654:23702 [0] sharp_plugin.c:382 NCCL WARN SHARP int8,uint8,bfloat16 Datatypes not supported
gpu34:23654:23702 [0] NCCL INFO SHARP rank 0/4 initialized on mlx5_0:1
```
</details> 

Here, allreduce was tested on 4 nodes-gpu34,gpu36,gpu40,gpu41-with only 2 GPU per nodes. 
I understand that it is far from ideal condition in which all 8x A100 GPUs form rings or chains. 
But we have a node-sharing environment, and it is not clear whether collnet demands exclusive access to all GPUs within the node. 
This log file shows that: 
- `libnccl-net.so` was succesfully loaded 
     ```
    gpu34:23654:23684 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
    ```
-  collnet was initialized 
    ```
    gpu34:23654:23684 [0] NCCL INFO CollNet 00/0 : 0 [receive] via COLLNET/SHARP/1/GDRDMA
    gpu41:63046:63077 [0] NCCL INFO CollNet 00/0 : 6 [receive] via COLLNET/SHARP/1/GDRDMA
    gpu36:15433:15499 [0] NCCL INFO CollNet 00/0 : 2 [receive] via COLLNET/SHARP/5/GDRDMA
    gpu40:2899:2929 [0] NCCL INFO CollNet 00/0 : 4 [receive] via COLLNET/SHARP/0/GDRDMA
    ``` 
- SHARP was initialized
    ```
    [gpu34:0:23654 - context.c:665][2025-05-26 15:20:21] INFO job (ID: 10883559310443912581) resource request quota: ( osts:0 user_data_per_ost:0 max_groups:0 max_qps:1 max_group_channels:1, num_trees:1)
    [gpu34:0:23654 - context.c:867][2025-05-26 15:20:21] INFO sharp_job_id:36   resv_key: tree_type:LLT tree_idx:0  treeID:15 caps:0x5 quota:(osts:25 user_data_per_ost:1024 max_groups:25 max_qps:1 max_group_channels:1)
    [gpu34:0:23654 - context.c:874][2025-05-26 15:20:21] INFO sharp_job_id:36   tree_type:SAT tree_idx:1  treeID:47 caps:0x15
    ```
- No output was produced beyong debug message. 

### CollNet fallbacks to P2P 
<details> 
<summary> With NCCL_DEBUG=info </summary>

```
# nThread 1 nGpus 1 minBytes 16 maxBytes 4294967296 step: 4(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid  34088 on      gpu34 device  0 [0000:07:00] NVIDIA A100-SXM4-80GB
#  Rank  1 Group  0 Pid  34089 on      gpu34 device  1 [0000:0b:00] NVIDIA A100-SXM4-80GB
#  Rank  2 Group  0 Pid  20775 on      gpu36 device  0 [0000:88:00] NVIDIA A100-SXM4-80GB
#  Rank  3 Group  0 Pid  20776 on      gpu36 device  1 [0000:cb:00] NVIDIA A100-SXM4-80GB
#  Rank  4 Group  0 Pid   9455 on      gpu40 device  0 [0000:4c:00] NVIDIA A100-SXM4-80GB
#  Rank  5 Group  0 Pid   9456 on      gpu40 device  1 [0000:88:00] NVIDIA A100-SXM4-80GB
#  Rank  6 Group  0 Pid   3928 on      gpu41 device  0 [0000:07:00] NVIDIA A100-SXM4-80GB
#  Rank  7 Group  0 Pid   3929 on      gpu41 device  1 [0000:88:00] NVIDIA A100-SXM4-80GB
gpu34:34088:34088 [0] NCCL INFO Bootstrap : Using ib0:10.159.0.34<0>
gpu40:9455:9455 [0] NCCL INFO cudaDriverVersion 12040
gpu40:9456:9456 [1] NCCL INFO cudaDriverVersion 12040
gpu34:34088:34088 [0] NCCL INFO cudaDriverVersion 12040
gpu41:3929:3929 [1] NCCL INFO cudaDriverVersion 12040
gpu41:3928:3928 [0] NCCL INFO cudaDriverVersion 12040
gpu34:34089:34089 [1] NCCL INFO cudaDriverVersion 12040
gpu36:20776:20776 [1] NCCL INFO cudaDriverVersion 12040
gpu36:20775:20775 [0] NCCL INFO cudaDriverVersion 12040
gpu34:34088:34088 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu34:34089:34089 [1] NCCL INFO Bootstrap : Using ib0:10.159.0.34<0>
gpu34:34089:34089 [1] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu40:9455:9455 [0] NCCL INFO Bootstrap : Using ib0:10.159.0.40<0>
gpu40:9455:9455 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu36:20776:20776 [1] NCCL INFO Bootstrap : Using ib0:10.159.0.36<0>
gpu40:9456:9456 [1] NCCL INFO Bootstrap : Using ib0:10.159.0.40<0>
gpu36:20775:20775 [0] NCCL INFO Bootstrap : Using ib0:10.159.0.36<0>
gpu36:20775:20775 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu36:20776:20776 [1] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu40:9456:9456 [1] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu41:3929:3929 [1] NCCL INFO Bootstrap : Using ib0:10.159.0.41<0>
gpu41:3928:3928 [0] NCCL INFO Bootstrap : Using ib0:10.159.0.41<0>
gpu41:3928:3928 [0] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu41:3929:3929 [1] NCCL INFO NCCL version 2.23.4+cuda12.4
gpu34:34088:34116 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu34:34088:34116 [0] NCCL INFO P2P plugin v8 IBext_v8
gpu34:34089:34117 [1] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu34:34089:34117 [1] NCCL INFO P2P plugin v8 IBext_v8
gpu40:9455:9487 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu40:9455:9487 [0] NCCL INFO P2P plugin v8 IBext_v8
gpu41:3928:3962 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu41:3928:3962 [0] NCCL INFO P2P plugin v8 IBext_v8
gpu41:3929:3961 [1] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu41:3929:3961 [1] NCCL INFO P2P plugin v8 IBext_v8
gpu40:9456:9488 [1] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu40:9456:9488 [1] NCCL INFO P2P plugin v8 IBext_v8
gpu36:20776:20808 [1] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu36:20776:20808 [1] NCCL INFO P2P plugin v8 IBext_v8
gpu36:20775:20807 [0] NCCL INFO Plugin Path : /scratch/optpar01/work/2025/10-sharp/build/nccl-rdma-sharp-plugins/src/.libs/libnccl-net.so
gpu36:20775:20807 [0] NCCL INFO P2P plugin v8 IBext_v8
gpu40:9455:9487 [0] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.40<0>
gpu40:9455:9487 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu40:9455:9487 [0] NCCL INFO Using network IBext_v8
gpu40:9456:9488 [1] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.40<0>
gpu40:9456:9488 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu41:3929:3961 [1] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.41<0>
gpu40:9456:9488 [1] NCCL INFO Using network IBext_v8
gpu41:3928:3962 [0] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.41<0>
gpu41:3929:3961 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu41:3928:3962 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu41:3928:3962 [0] NCCL INFO Using network IBext_v8
gpu41:3929:3961 [1] NCCL INFO Using network IBext_v8
gpu34:34088:34116 [0] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.34<0>
gpu34:34089:34117 [1] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.34<0>
gpu34:34088:34116 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu34:34088:34116 [0] NCCL INFO Using network IBext_v8
gpu34:34089:34117 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu34:34089:34117 [1] NCCL INFO Using network IBext_v8
gpu36:20776:20808 [1] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.36<0>
gpu36:20775:20807 [0] NCCL INFO NET/IB : Using [0]mlx5_2:1/IB/SHARP [1]mlx5_0:1/IB/SHARP [2]mlx5_6:1/IB/SHARP [3]mlx5_8:1/IB/SHARP [4]mlx5_9:1/IB/SHARP [5]mlx5_4:1/IB/SHARP [RO]; OOB ib0:10.159.0.36<0>
gpu36:20776:20808 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu36:20775:20807 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
gpu36:20775:20807 [0] NCCL INFO Using network IBext_v8
gpu36:20776:20808 [1] NCCL INFO Using network IBext_v8
gpu34:34088:34116 [0] NCCL INFO ncclCommInitRank comm 0x5468150 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 7000 commId 0x70fba02a8d314739 - Init START
gpu41:3928:3962 [0] NCCL INFO ncclCommInitRank comm 0x59f8cc0 rank 6 nranks 8 cudaDev 0 nvmlDev 0 busId 7000 commId 0x70fba02a8d314739 - Init START
gpu41:3929:3961 [1] NCCL INFO ncclCommInitRank comm 0x6699950 rank 7 nranks 8 cudaDev 1 nvmlDev 1 busId 88000 commId 0x70fba02a8d314739 - Init START
gpu36:20775:20807 [0] NCCL INFO ncclCommInitRank comm 0x542f3f0 rank 2 nranks 8 cudaDev 0 nvmlDev 0 busId 88000 commId 0x70fba02a8d314739 - Init START
gpu36:20776:20808 [1] NCCL INFO ncclCommInitRank comm 0x636b080 rank 3 nranks 8 cudaDev 1 nvmlDev 1 busId cb000 commId 0x70fba02a8d314739 - Init START
gpu34:34089:34117 [1] NCCL INFO ncclCommInitRank comm 0x69853c0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId b000 commId 0x70fba02a8d314739 - Init START
gpu40:9455:9487 [0] NCCL INFO ncclCommInitRank comm 0x63e6140 rank 4 nranks 8 cudaDev 0 nvmlDev 0 busId 4c000 commId 0x70fba02a8d314739 - Init START
gpu40:9456:9488 [1] NCCL INFO ncclCommInitRank comm 0x5f56040 rank 5 nranks 8 cudaDev 1 nvmlDev 1 busId 88000 commId 0x70fba02a8d314739 - Init START
gpu34:34089:34117 [1] NCCL INFO Bootstrap timings total 0.002997 (create 0.000032, send 0.000099, recv 0.000086, ring 0.002617, delay 0.000001)
gpu34:34088:34116 [0] NCCL INFO Bootstrap timings total 0.020601 (create 0.000024, send 0.008984, recv 0.008794, ring 0.002692, delay 0.000001)
gpu36:20775:20807 [0] NCCL INFO Bootstrap timings total 0.012039 (create 0.000577, send 0.000281, recv 0.003220, ring 0.002537, delay 0.000001)
gpu41:3929:3961 [1] NCCL INFO Bootstrap timings total 0.014155 (create 0.000128, send 0.000216, recv 0.002542, ring 0.010980, delay 0.000001)
gpu40:9455:9487 [0] NCCL INFO Bootstrap timings total 0.001344 (create 0.000387, send 0.000216, recv 0.000283, ring 0.000289, delay 0.000001)
gpu41:3928:3962 [0] NCCL INFO Bootstrap timings total 0.014514 (create 0.000474, send 0.000232, recv 0.002655, ring 0.000366, delay 0.000001)
gpu40:9456:9488 [1] NCCL INFO Bootstrap timings total 0.000972 (create 0.000040, send 0.000171, recv 0.000137, ring 0.000289, delay 0.000001)
gpu36:20776:20808 [1] NCCL INFO Bootstrap timings total 0.008580 (create 0.000070, send 0.000143, recv 0.007734, ring 0.000307, delay 0.000001)
gpu34:34088:34116 [0] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu34:34089:34117 [1] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu36:20775:20807 [0] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu36:20776:20808 [1] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu41:3929:3961 [1] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu41:3928:3962 [0] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu40:9455:9487 [0] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu40:9456:9488 [1] NCCL INFO NCCL_COLLNET_ENABLE set by environment to 1.
gpu34:34089:34117 [1] NCCL INFO comm 0x69853c0 rank 1 nRanks 8 nNodes 4 localRanks 2 localRank 1 MNNVL 0
gpu34:34088:34116 [0] NCCL INFO comm 0x5468150 rank 0 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0
gpu41:3929:3961 [1] NCCL INFO comm 0x6699950 rank 7 nRanks 8 nNodes 4 localRanks 2 localRank 1 MNNVL 0
gpu36:20776:20808 [1] NCCL INFO comm 0x636b080 rank 3 nRanks 8 nNodes 4 localRanks 2 localRank 1 MNNVL 0
gpu34:34088:34116 [0] NCCL INFO Channel 00/03 : 0 1 2 3 4 5 6 7
gpu36:20775:20807 [0] NCCL INFO comm 0x542f3f0 rank 2 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0
gpu36:20775:20807 [0] NCCL INFO Trees [0] 3/-1/-1->2->5 [1] 3/0/-1->2->6 [2] 3/-1/-1->2->5
gpu34:34088:34116 [0] NCCL INFO Channel 01/03 : 0 1 2 3 4 5 6 7
gpu34:34088:34116 [0] NCCL INFO Channel 02/03 : 0 1 2 3 4 5 6 7
gpu34:34088:34116 [0] NCCL INFO Trees [0] 1/4/-1->0->-1 [1] 1/-1/-1->0->2 [2] 1/4/-1->0->-1
gpu40:9455:9487 [0] NCCL INFO comm 0x63e6140 rank 4 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0
gpu36:20775:20807 [0] NCCL INFO P2P Chunksize set to 131072
gpu41:3928:3962 [0] NCCL INFO comm 0x59f8cc0 rank 6 nRanks 8 nNodes 4 localRanks 2 localRank 0 MNNVL 0
gpu34:34088:34116 [0] NCCL INFO P2P Chunksize set to 131072
gpu40:9456:9488 [1] NCCL INFO comm 0x5f56040 rank 5 nRanks 8 nNodes 4 localRanks 2 localRank 1 MNNVL 0
gpu36:20776:20808 [1] NCCL INFO Trees [0] -1/-1/-1->3->2 [1] 4/-1/-1->3->2 [2] -1/-1/-1->3->2
gpu41:3929:3961 [1] NCCL INFO Trees [0] -1/-1/-1->7->6 [1] -1/-1/-1->7->6 [2] -1/-1/-1->7->6
gpu40:9455:9487 [0] NCCL INFO Trees [0] 5/6/-1->4->0 [1] 5/-1/-1->4->3 [2] 5/6/-1->4->0
gpu40:9455:9487 [0] NCCL INFO P2P Chunksize set to 131072
gpu36:20776:20808 [1] NCCL INFO P2P Chunksize set to 131072
gpu41:3928:3962 [0] NCCL INFO Trees [0] 7/-1/-1->6->4 [1] 7/2/-1->6->-1 [2] 7/-1/-1->6->4
gpu41:3928:3962 [0] NCCL INFO P2P Chunksize set to 131072
gpu40:9456:9488 [1] NCCL INFO Trees [0] 2/-1/-1->5->4 [1] -1/-1/-1->5->4 [2] 2/-1/-1->5->4
gpu41:3929:3961 [1] NCCL INFO P2P Chunksize set to 131072
gpu40:9456:9488 [1] NCCL INFO P2P Chunksize set to 131072
gpu34:34089:34117 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0 [2] -1/-1/-1->1->0
gpu34:34089:34117 [1] NCCL INFO P2P Chunksize set to 131072
gpu40:9455:9506 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 20
gpu36:20775:20826 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 16
gpu36:20775:20825 [0] NCCL INFO [Proxy Service] Device 0 CPU core 16
gpu40:9455:9505 [0] NCCL INFO [Proxy Service] Device 0 CPU core 20
gpu41:3928:3983 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 8
gpu34:34088:34137 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 8
gpu34:34088:34135 [0] NCCL INFO [Proxy Service] Device 0 CPU core 8
gpu41:3928:3982 [0] NCCL INFO [Proxy Service] Device 0 CPU core 8
gpu40:9456:9508 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 36
gpu34:34089:34136 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 40
gpu34:34089:34134 [1] NCCL INFO [Proxy Service] Device 1 CPU core 40
gpu41:3929:3981 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 40
gpu41:3929:3980 [1] NCCL INFO [Proxy Service] Device 1 CPU core 40
gpu36:20776:20828 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 48
gpu40:9456:9507 [1] NCCL INFO [Proxy Service] Device 1 CPU core 36
gpu36:20776:20827 [1] NCCL INFO [Proxy Service] Device 1 CPU core 48
gpu40:9455:9487 [0] NCCL INFO CollNet 00/0 : 4 [receive] via COLLNET/SHARP/0/GDRDMA
gpu34:34088:34116 [0] NCCL INFO CollNet 00/0 : 0 [receive] via COLLNET/SHARP/1/GDRDMA
gpu36:20775:20807 [0] NCCL INFO CollNet 00/0 : 2 [receive] via COLLNET/SHARP/5/GDRDMA
gpu41:3928:3962 [0] NCCL INFO CollNet 00/0 : 6 [receive] via COLLNET/SHARP/1/GDRDMA
gpu40:9455:9509 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 20
gpu36:20775:20829 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 16
gpu34:34088:34138 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 8
gpu41:3928:3984 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 8
[gpu34:0:34088 - context.c:665][2025-05-26 15:39:24] INFO job (ID: 10883558421705822370) resource request quota: ( osts:0 user_data_per_ost:0 max_groups:0 max_qps:1 max_group_channels:1, num_trees:1)
[gpu34][May 26 15:39:24 887618][GENERAL][34135][warn ] - Begin job id: 10883558421705822370 failed with status: No resource
[gpu34:0:34088 unique id 10883558421705822370][2025-05-26 15:39:24] ERROR Job error in sharp_get_job_data_len.

[gpu34:0:34088 - context.c:696][2025-05-26 15:39:24] ERROR sharp_get_job_data_len failed: Job error(-35)
[gpu34:0:34088 - context.c:705][2025-05-26 15:39:24] ERROR SHArP Job init error: No resource

gpu36:20775:20825 [0] sharp_plugin.c:365 NCCL WARN NET/IB : SHARP coll init error: Cannot create SHARP job(-11)

gpu36:20775:20807 [0] NCCL INFO transport.cc:356 -> 2

gpu36:20775:20807 [0] transport.cc:384 NCCL WARN Cannot initialize CollNet, using point-to-point network instead
gpu36:20775:20807 [0] NCCL INFO transport/coll_net.cc:1358 -> 2
gpu36:20775:20807 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu36:20775:20807 [0] NCCL INFO 3 coll channels, 3 collnet channels, 0 nvls channels, 4 p2p channels, 1 p2p channels per peer
gpu36:20776:20808 [1] NCCL INFO transport/coll_net.cc:1358 -> 2
gpu36:20776:20808 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu36:20776:20808 [1] NCCL INFO 3 coll channels, 3 collnet channels, 0 nvls channels, 4 p2p channels, 1 p2p channels per peer

gpu40:9455:9505 [0] sharp_plugin.c:365 NCCL WARN NET/IB : SHARP coll init error: Cannot create SHARP job(-11)

gpu40:9455:9487 [0] NCCL INFO transport.cc:356 -> 2

gpu40:9455:9487 [0] transport.cc:384 NCCL WARN Cannot initialize CollNet, using point-to-point network instead
gpu40:9455:9487 [0] NCCL INFO transport/coll_net.cc:1358 -> 2
gpu40:9455:9487 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu40:9455:9487 [0] NCCL INFO 3 coll channels, 3 collnet channels, 0 nvls channels, 4 p2p channels, 1 p2p channels per peer
gpu40:9456:9488 [1] NCCL INFO transport/coll_net.cc:1358 -> 2
gpu40:9456:9488 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512

gpu41:3928:3982 [0] sharp_plugin.c:365 NCCL WARN NET/IB : SHARP coll init error: Cannot create SHARP job(-11)

gpu40:9456:9488 [1] NCCL INFO 3 coll channels, 3 collnet channels, 0 nvls channels, 4 p2p channels, 1 p2p channels per peer
gpu41:3928:3962 [0] NCCL INFO transport.cc:356 -> 2

gpu34:34088:34135 [0] sharp_plugin.c:365 NCCL WARN NET/IB : SHARP coll init error: Cannot create SHARP job(-11)


gpu41:3928:3962 [0] transport.cc:384 NCCL WARN Cannot initialize CollNet, using point-to-point network instead
gpu41:3928:3962 [0] NCCL INFO transport/coll_net.cc:1358 -> 2
gpu34:34088:34116 [0] NCCL INFO transport.cc:356 -> 2
gpu41:3928:3962 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu41:3928:3962 [0] NCCL INFO 3 coll channels, 3 collnet channels, 0 nvls channels, 4 p2p channels, 1 p2p channels per peer
gpu41:3929:3961 [1] NCCL INFO transport/coll_net.cc:1358 -> 2
gpu41:3929:3961 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu41:3929:3961 [1] NCCL INFO 3 coll channels, 3 collnet channels, 0 nvls channels, 4 p2p channels, 1 p2p channels per peer

gpu34:34088:34116 [0] transport.cc:384 NCCL WARN Cannot initialize CollNet, using point-to-point network instead
gpu34:34088:34116 [0] NCCL INFO transport/coll_net.cc:1358 -> 2
gpu34:34089:34117 [1] NCCL INFO transport/coll_net.cc:1358 -> 2
gpu34:34089:34117 [1] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu34:34089:34117 [1] NCCL INFO 3 coll channels, 3 collnet channels, 0 nvls channels, 4 p2p channels, 1 p2p channels per peer
gpu34:34088:34116 [0] NCCL INFO threadThresholds 8/8/64 | 64/8/64 | 512 | 512
gpu34:34088:34116 [0] NCCL INFO 3 coll channels, 3 collnet channels, 0 nvls channels, 4 p2p channels, 1 p2p channels per peer
gpu36:20775:20807 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
gpu36:20775:20807 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
gpu36:20775:20807 [0] NCCL INFO ncclCommInitRank comm 0x542f3f0 rank 2 nranks 8 cudaDev 0 nvmlDev 0 busId 88000 commId 0x70fba02a8d314739 - Init COMPLETE
gpu36:20775:20807 [0] NCCL INFO Init timings - ncclCommInitRank: rank 2 nranks 8 total 0.75 (kernels 0.09, alloc 0.08, bootstrap 0.01, allgathers 0.01, topo 0.07, graphs 0.00, connections 0.48, rest 0.00)
gpu36:20776:20808 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
gpu36:20776:20808 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
gpu36:20776:20808 [1] NCCL INFO ncclCommInitRank comm 0x636b080 rank 3 nranks 8 cudaDev 1 nvmlDev 1 busId cb000 commId 0x70fba02a8d314739 - Init COMPLETE
gpu36:20776:20808 [1] NCCL INFO Init timings - ncclCommInitRank: rank 3 nranks 8 total 0.75 (kernels 0.09, alloc 0.08, bootstrap 0.01, allgathers 0.01, topo 0.07, graphs 0.00, connections 0.48, rest 0.00)
gpu34:34088:34116 [0] NCCL INFO CC Off, Multi-GPU CC Off, workFifoBytes 1048576
gpu41:3928:3962 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
gpu41:3928:3962 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
gpu41:3928:3962 [0] NCCL INFO ncclCommInitRank comm 0x59f8cc0 rank 6 nranks 8 cudaDev 0 nvmlDev 0 busId 7000 commId 0x70fba02a8d314739 - Init COMPLETE
gpu41:3928:3962 [0] NCCL INFO Init timings - ncclCommInitRank: rank 6 nranks 8 total 0.75 (kernels 0.08, alloc 0.09, bootstrap 0.01, allgathers 0.01, topo 0.08, graphs 0.00, connections 0.48, rest 0.00)
gpu41:3929:3961 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
gpu41:3929:3961 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
gpu41:3929:3961 [1] NCCL INFO ncclCommInitRank comm 0x6699950 rank 7 nranks 8 cudaDev 1 nvmlDev 1 busId 88000 commId 0x70fba02a8d314739 - Init COMPLETE
gpu41:3929:3961 [1] NCCL INFO Init timings - ncclCommInitRank: rank 7 nranks 8 total 0.75 (kernels 0.08, alloc 0.08, bootstrap 0.01, allgathers 0.01, topo 0.07, graphs 0.00, connections 0.48, rest 0.00)
gpu34:34088:34116 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
gpu34:34088:34116 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
gpu34:34088:34116 [0] NCCL INFO ncclCommInitRank comm 0x5468150 rank 0 nranks 8 cudaDev 0 nvmlDev 0 busId 7000 commId 0x70fba02a8d314739 - Init COMPLETE
gpu34:34088:34116 [0] NCCL INFO Init timings - ncclCommInitRank: rank 0 nranks 8 total 0.75 (kernels 0.08, alloc 0.08, bootstrap 0.02, allgathers 0.01, topo 0.07, graphs 0.00, connections 0.48, rest 0.00)
gpu34:34089:34117 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
gpu34:34089:34117 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
gpu34:34089:34117 [1] NCCL INFO ncclCommInitRank comm 0x69853c0 rank 1 nranks 8 cudaDev 1 nvmlDev 1 busId b000 commId 0x70fba02a8d314739 - Init COMPLETE
gpu34:34089:34117 [1] NCCL INFO Init timings - ncclCommInitRank: rank 1 nranks 8 total 0.75 (kernels 0.08, alloc 0.10, bootstrap 0.00, allgathers 0.01, topo 0.07, graphs 0.00, connections 0.48, rest 0.00)
gpu40:9455:9487 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
gpu40:9455:9487 [0] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
gpu40:9455:9487 [0] NCCL INFO ncclCommInitRank comm 0x63e6140 rank 4 nranks 8 cudaDev 0 nvmlDev 0 busId 4c000 commId 0x70fba02a8d314739 - Init COMPLETE
gpu40:9455:9487 [0] NCCL INFO Init timings - ncclCommInitRank: rank 4 nranks 8 total 0.87 (kernels 0.08, alloc 0.10, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.00, connections 0.61, rest 0.00)
gpu40:9456:9488 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v3 symbol.
gpu40:9456:9488 [1] NCCL INFO TUNER/Plugin: Failed to find ncclTunerPlugin_v2 symbol, using internal tuner instead.
gpu40:9456:9488 [1] NCCL INFO ncclCommInitRank comm 0x5f56040 rank 5 nranks 8 cudaDev 1 nvmlDev 1 busId 88000 commId 0x70fba02a8d314739 - Init COMPLETE
gpu40:9456:9488 [1] NCCL INFO Init timings - ncclCommInitRank: rank 5 nranks 8 total 0.87 (kernels 0.08, alloc 0.10, bootstrap 0.00, allgathers 0.00, topo 0.08, graphs 0.00, connections 0.61, rest 0.00)
gpu34:34088:34142 [0] NCCL INFO Channel 00/0 : 7[1] -> 0[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9578 [0] NCCL INFO Channel 00/0 : 3[1] -> 4[0] [receive] via NET/IBext_v8/0/GDRDMA
gpu36:20775:20832 [0] NCCL INFO Channel 00/0 : 1[1] -> 2[0] [receive] via NET/IBext_v8/5/GDRDMA
gpu40:9455:9578 [0] NCCL INFO Channel 01/0 : 3[1] -> 4[0] [receive] via NET/IBext_v8/0/GDRDMA
gpu36:20775:20832 [0] NCCL INFO Channel 01/0 : 1[1] -> 2[0] [receive] via NET/IBext_v8/5/GDRDMA
gpu34:34088:34142 [0] NCCL INFO Channel 01/0 : 7[1] -> 0[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9578 [0] NCCL INFO Channel 02/0 : 3[1] -> 4[0] [receive] via NET/IBext_v8/0/GDRDMA
gpu41:3928:3989 [0] NCCL INFO Channel 00/0 : 5[1] -> 6[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9578 [0] NCCL INFO Channel 00/0 : 4[0] -> 5[1] via P2P/CUMEM/read
gpu36:20775:20832 [0] NCCL INFO Channel 02/0 : 1[1] -> 2[0] [receive] via NET/IBext_v8/5/GDRDMA
gpu36:20775:20832 [0] NCCL INFO Channel 00/0 : 2[0] -> 3[1] via P2P/CUMEM/read
gpu41:3928:3989 [0] NCCL INFO Channel 01/0 : 5[1] -> 6[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu41:3928:3989 [0] NCCL INFO Channel 02/0 : 5[1] -> 6[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu34:34088:34142 [0] NCCL INFO Channel 02/0 : 7[1] -> 0[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu34:34088:34142 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[1] via P2P/CUMEM/read
gpu41:3928:3989 [0] NCCL INFO Channel 00/0 : 6[0] -> 7[1] via P2P/CUMEM/read
gpu36:20775:20832 [0] NCCL INFO Channel 01/0 : 2[0] -> 3[1] via P2P/CUMEM/read
gpu40:9455:9578 [0] NCCL INFO Channel 01/0 : 4[0] -> 5[1] via P2P/CUMEM/read
gpu34:34088:34142 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[1] via P2P/CUMEM/read
gpu41:3928:3989 [0] NCCL INFO Channel 01/0 : 6[0] -> 7[1] via P2P/CUMEM/read
gpu36:20775:20832 [0] NCCL INFO Channel 02/0 : 2[0] -> 3[1] via P2P/CUMEM/read
gpu40:9455:9578 [0] NCCL INFO Channel 02/0 : 4[0] -> 5[1] via P2P/CUMEM/read
gpu34:34088:34142 [0] NCCL INFO Channel 02/0 : 0[0] -> 1[1] via P2P/CUMEM/read
gpu41:3928:3989 [0] NCCL INFO Channel 02/0 : 6[0] -> 7[1] via P2P/CUMEM/read
gpu36:20776:20833 [1] NCCL INFO Channel 00/0 : 3[1] -> 4[0] [send] via NET/IBext_v8/5(2)/GDRDMA
gpu41:3929:3988 [1] NCCL INFO Channel 00/0 : 7[1] -> 0[0] [send] via NET/IBext_v8/1(6)/GDRDMA
gpu36:20776:20833 [1] NCCL INFO Channel 01/0 : 3[1] -> 4[0] [send] via NET/IBext_v8/5(2)/GDRDMA
gpu36:20776:20833 [1] NCCL INFO Channel 02/0 : 3[1] -> 4[0] [send] via NET/IBext_v8/5(2)/GDRDMA
gpu40:9456:9579 [1] NCCL INFO Channel 00/0 : 5[1] -> 6[0] [send] via NET/IBext_v8/0(4)/GDRDMA
gpu41:3929:3988 [1] NCCL INFO Channel 01/0 : 7[1] -> 0[0] [send] via NET/IBext_v8/1(6)/GDRDMA
gpu40:9456:9579 [1] NCCL INFO Channel 01/0 : 5[1] -> 6[0] [send] via NET/IBext_v8/0(4)/GDRDMA
gpu40:9456:9579 [1] NCCL INFO Channel 02/0 : 5[1] -> 6[0] [send] via NET/IBext_v8/0(4)/GDRDMA
gpu41:3929:3988 [1] NCCL INFO Channel 02/0 : 7[1] -> 0[0] [send] via NET/IBext_v8/1(6)/GDRDMA
gpu34:34089:34143 [1] NCCL INFO Channel 00/0 : 1[1] -> 2[0] [send] via NET/IBext_v8/1/GDRDMA
gpu34:34089:34143 [1] NCCL INFO Channel 01/0 : 1[1] -> 2[0] [send] via NET/IBext_v8/1/GDRDMA
gpu34:34089:34143 [1] NCCL INFO Channel 02/0 : 1[1] -> 2[0] [send] via NET/IBext_v8/1/GDRDMA
gpu34:34089:34144 [1] NCCL INFO [Proxy Progress] Device 1 CPU core 40
gpu34:34089:34143 [1] NCCL INFO Connected all rings
gpu34:34088:34142 [0] NCCL INFO Connected all rings
gpu36:20775:20832 [0] NCCL INFO Connected all rings
gpu36:20776:20833 [1] NCCL INFO Connected all rings
gpu41:3929:3988 [1] NCCL INFO Connected all rings
gpu40:9455:9578 [0] NCCL INFO Connected all rings
gpu40:9456:9579 [1] NCCL INFO Connected all rings
gpu41:3928:3989 [0] NCCL INFO Connected all rings
gpu34:34089:34147 [1] NCCL INFO Channel 00/0 : 1[1] -> 0[0] via P2P/CUMEM/read
gpu41:3929:3991 [1] NCCL INFO Channel 00/0 : 7[1] -> 6[0] via P2P/CUMEM/read
gpu34:34088:34148 [0] NCCL INFO Channel 01/0 : 0[0] -> 2[0] [send] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9584 [0] NCCL INFO Channel 00/0 : 4[0] -> 6[0] [send] via NET/IBext_v8/0/GDRDMA
gpu36:20775:20838 [0] NCCL INFO Channel 01/0 : 0[0] -> 2[0] [receive] via NET/IBext_v8/5/GDRDMA
gpu41:3928:3992 [0] NCCL INFO Channel 00/0 : 4[0] -> 6[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9584 [0] NCCL INFO Channel 02/0 : 4[0] -> 6[0] [send] via NET/IBext_v8/0/GDRDMA
gpu41:3928:3992 [0] NCCL INFO Channel 02/0 : 4[0] -> 6[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu34:34088:34148 [0] NCCL INFO Channel 00/0 : 4[0] -> 0[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu36:20775:20838 [0] NCCL INFO Channel 00/0 : 2[0] -> 5[1] [send] via NET/IBext_v8/5/GDRDMA
gpu40:9455:9584 [0] NCCL INFO Channel 00/0 : 0[0] -> 4[0] [receive] via NET/IBext_v8/0/GDRDMA
gpu41:3928:3992 [0] NCCL INFO Channel 01/0 : 2[0] -> 6[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu36:20775:20838 [0] NCCL INFO Channel 02/0 : 2[0] -> 5[1] [send] via NET/IBext_v8/5/GDRDMA
gpu41:3928:3992 [0] NCCL INFO Channel 01/0 : 6[0] -> 2[0] [send] via NET/IBext_v8/1/GDRDMA
gpu34:34088:34148 [0] NCCL INFO Channel 02/0 : 4[0] -> 0[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9584 [0] NCCL INFO Channel 02/0 : 0[0] -> 4[0] [receive] via NET/IBext_v8/0/GDRDMA
gpu40:9455:9584 [0] NCCL INFO Channel 00/0 : 4[0] -> 0[0] [send] via NET/IBext_v8/0/GDRDMA
gpu34:34088:34148 [0] NCCL INFO Channel 00/0 : 0[0] -> 4[0] [send] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9584 [0] NCCL INFO Channel 02/0 : 4[0] -> 0[0] [send] via NET/IBext_v8/0/GDRDMA
gpu41:3929:3991 [1] NCCL INFO Channel 01/0 : 7[1] -> 6[0] via P2P/CUMEM/read
gpu34:34089:34147 [1] NCCL INFO Channel 01/0 : 1[1] -> 0[0] via P2P/CUMEM/read
gpu34:34088:34148 [0] NCCL INFO Channel 02/0 : 0[0] -> 4[0] [send] via NET/IBext_v8/1/GDRDMA
gpu34:34088:34148 [0] NCCL INFO Channel 01/0 : 2[0] -> 0[0] [receive] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9584 [0] NCCL INFO Channel 00/0 : 6[0] -> 4[0] [receive] via NET/IBext_v8/0/GDRDMA
gpu41:3929:3991 [1] NCCL INFO Channel 02/0 : 7[1] -> 6[0] via P2P/CUMEM/read
gpu40:9455:9584 [0] NCCL INFO Channel 02/0 : 6[0] -> 4[0] [receive] via NET/IBext_v8/0/GDRDMA
gpu34:34089:34147 [1] NCCL INFO Channel 02/0 : 1[1] -> 0[0] via P2P/CUMEM/read
gpu36:20776:20837 [1] NCCL INFO Channel 01/0 : 4[0] -> 3[1] [receive] via NET/IBext_v8/5/GDRDMA
gpu36:20776:20837 [1] NCCL INFO Channel 00/0 : 3[1] -> 2[0] via P2P/CUMEM/read
gpu36:20776:20837 [1] NCCL INFO Channel 01/0 : 3[1] -> 2[0] via P2P/CUMEM/read
gpu36:20776:20837 [1] NCCL INFO Channel 02/0 : 3[1] -> 2[0] via P2P/CUMEM/read
gpu40:9456:9585 [1] NCCL INFO Channel 00/0 : 2[0] -> 5[1] [receive] via NET/IBext_v8/0/GDRDMA
gpu40:9456:9585 [1] NCCL INFO Channel 02/0 : 2[0] -> 5[1] [receive] via NET/IBext_v8/0/GDRDMA
gpu40:9456:9585 [1] NCCL INFO Channel 00/0 : 5[1] -> 2[0] [send] via NET/IBext_v8/0(4)/GDRDMA
gpu40:9456:9585 [1] NCCL INFO Channel 02/0 : 5[1] -> 2[0] [send] via NET/IBext_v8/0(4)/GDRDMA
gpu36:20776:20839 [1] NCCL INFO [Proxy Progress] Device 1 CPU core 48
gpu40:9456:9586 [1] NCCL INFO [Proxy Progress] Device 1 CPU core 36
gpu36:20775:20838 [0] NCCL INFO Channel 01/0 : 6[0] -> 2[0] [receive] via NET/IBext_v8/5/GDRDMA
gpu36:20775:20838 [0] NCCL INFO Channel 01/0 : 2[0] -> 6[0] [send] via NET/IBext_v8/5/GDRDMA
gpu36:20775:20838 [0] NCCL INFO Channel 00/0 : 5[1] -> 2[0] [receive] via NET/IBext_v8/5/GDRDMA
gpu36:20775:20838 [0] NCCL INFO Channel 02/0 : 5[1] -> 2[0] [receive] via NET/IBext_v8/5/GDRDMA
gpu40:9456:9585 [1] NCCL INFO Channel 00/0 : 5[1] -> 4[0] via P2P/CUMEM/read
gpu36:20775:20838 [0] NCCL INFO Channel 01/0 : 2[0] -> 0[0] [send] via NET/IBext_v8/5/GDRDMA
gpu40:9456:9585 [1] NCCL INFO Channel 01/0 : 5[1] -> 4[0] via P2P/CUMEM/read
gpu40:9456:9585 [1] NCCL INFO Channel 02/0 : 5[1] -> 4[0] via P2P/CUMEM/read
gpu41:3928:3992 [0] NCCL INFO Channel 00/0 : 6[0] -> 4[0] [send] via NET/IBext_v8/1/GDRDMA
gpu41:3928:3992 [0] NCCL INFO Channel 02/0 : 6[0] -> 4[0] [send] via NET/IBext_v8/1/GDRDMA
gpu40:9455:9584 [0] NCCL INFO Channel 01/0 : 4[0] -> 3[1] [send] via NET/IBext_v8/0/GDRDMA
gpu40:9456:9585 [1] NCCL INFO Connected all trees
gpu36:20775:20838 [0] NCCL INFO Connected all trees
gpu41:3928:3992 [0] NCCL INFO Connected all trees
gpu40:9455:9584 [0] NCCL INFO Connected all trees
gpu36:20776:20837 [1] NCCL INFO Connected all trees
gpu41:3929:3991 [1] NCCL INFO Connected all trees
gpu34:34088:34148 [0] NCCL INFO Connected all trees
gpu34:34089:34147 [1] NCCL INFO Connected all trees
          16             4     float     sum      -1    151.3    0.00    0.00      0    68.64    0.00    0.00      0
          64            16     float     sum      -1    79.14    0.00    0.00      0    73.99    0.00    0.00      0
         256            64     float     sum      -1    80.50    0.00    0.01      0    79.37    0.00    0.01      0
        1024           256     float     sum      -1    81.29    0.01    0.02      0    45.97    0.02    0.04      0
        4096          1024     float     sum      -1    84.22    0.05    0.09      0    46.31    0.09    0.15      0
       16384          4096     float     sum      -1    61.28    0.27    0.47      0    124.1    0.13    0.23      0
       65536         16384     float     sum      -1    150.2    0.44    0.76      0    274.9    0.24    0.42      0
      262144         65536     float     sum      -1    167.6    1.56    2.74      0    154.1    1.70    2.98      0
     1048576        262144     float     sum      -1   1473.4    0.71    1.25      0   1471.6    0.71    1.25      0
     4194304       1048576     float     sum      -1    402.7   10.42   18.23      0    423.4    9.91   17.34      0
    16777216       4194304     float     sum      -1   1378.9   12.17   21.29      0   1271.1   13.20   23.10      0
    67108864      16777216     float     sum      -1   5421.8   12.38   21.66      0   5835.6   11.50   20.12      0
   268435456      67108864     float     sum      -1    22144   12.12   21.21      0    22470   11.95   20.91      0
  1073741824     268435456     float     sum      -1    87174   12.32   21.56      0    86596   12.40   21.70      0
  4294967296    1073741824     float     sum      -1   346304   12.40   21.70      0   347314   12.37   21.64      0
gpu36:20776:20776 [1] NCCL INFO comm 0x636b080 rank 3 nranks 8 cudaDev 1 busId cb000 - Destroy COMPLETE
gpu34:34088:34088 [0] NCCL INFO comm 0x5468150 rank 0 nranks 8 cudaDev 0 busId 7000 - Destroy COMPLETE
gpu41:3928:3928 [0] NCCL INFO comm 0x59f8cc0 rank 6 nranks 8 cudaDev 0 busId 7000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 8.69534
#
gpu34:34089:34089 [1] NCCL INFO comm 0x69853c0 rank 1 nranks 8 cudaDev 1 busId b000 - Destroy COMPLETE
gpu41:3929:3929 [1] NCCL INFO comm 0x6699950 rank 7 nranks 8 cudaDev 1 busId 88000 - Destroy COMPLETE
gpu40:9456:9456 [1] NCCL INFO comm 0x5f56040 rank 5 nranks 8 cudaDev 1 busId 88000 - Destroy COMPLETE
gpu36:20775:20775 [0] NCCL INFO comm 0x542f3f0 rank 2 nranks 8 cudaDev 0 busId 88000 - Destroy COMPLETE
gpu40:9455:9455 [0] NCCL INFO comm 0x63e6140 rank 4 nranks 8 cudaDev 0 busId 4c000 - Destroy COMPLETE
```

</details>

If I rerun the test again, sometimes it will proceed  with collnet being disabled: 
```
[gpu34:0:34088 - context.c:665][2025-05-26 15:39:24] INFO job (ID: 10883558421705822370) resource request quota: ( osts:0 user_data_per_ost:0 max_groups:0 max_qps:1 max_group_channels:1, num_trees:1)
[gpu34][May 26 15:39:24 887618][GENERAL][34135][warn ] - Begin job id: 10883558421705822370 failed with status: No resource
[gpu34:0:34088 unique id 10883558421705822370][2025-05-26 15:39:24] ERROR Job error in sharp_get_job_data_len.

[gpu34:0:34088 - context.c:696][2025-05-26 15:39:24] ERROR sharp_get_job_data_len failed: Job error(-35)
[gpu34:0:34088 - context.c:705][2025-05-26 15:39:24] ERROR SHArP Job init error: No resource
...
gpu34:34088:34116 [0] transport.cc:384 NCCL WARN Cannot initialize CollNet, using point-to-point network instead
```

Due to node-sharing nature of the cluster, the MPI processes are bound to different NIC, i.e. 
```
gpu36:20550:20599 [0] NCCL INFO SHARP rank 1/4 initialized on mlx5_4:1
gpu40:9230:9279 [0] NCCL INFO SHARP rank 2/4 initialized on mlx5_2:1
gpu41:3697:3747 [0] NCCL INFO SHARP rank 3/4 initialized on mlx5_0:1
gpu34:33807:33855 [0] NCCL INFO SHARP rank 0/4 initialized on mlx5_0:1
```
Could the above binding prevent CollNet to proceed ? 

I have strive to provide as much information as possible. 
I appreciate it if you can provide some insights to diagnose the issue. 

Thanks. 

## 评论 (1)

### kiskra-nvidia · 2025-05-27

Does Collnet ever succeed in your case?

It sounds like you are using a self-compiled plugin. Have you tried using the version included in the HPCX releases?
