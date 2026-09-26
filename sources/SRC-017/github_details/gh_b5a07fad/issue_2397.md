# [Issue #2397] [Issue]: ncclCommShrink leads to IB transport errors and hang when excluded ranks exit without calling shrink, and also affects the allreduce operations after the shrink.

source: https://github.com/NVIDIA/nccl/issues/2397
state: closed | updated: 2026-09-17T11:53:36Z
labels: 

## 正文

### How is this issue impacting you?

Application hang

### Share Your Debug Logs

[2026-09-09 10:46:33] ubuntu2:319733:319761 [1] transport/net_ib/[p2p.cc:783](https://p2p.cc:783/) NCCL WARN NET/IB: ncclIbTest: Got CQE with error (devIndex=0, req=0x7fccfc04e028, comm=0x7fccfc04e000 (recv), wr_id=0, qp_num=26257)

[2026-09-09 10:46:33] ubuntu2:319733:319761 [1] transport/net_ib/[p2p.cc:648](https://p2p.cc:648/) NCCL WARN NET/IB: Got completion from peer 10.153.235.13<40554> with status=IBV_WC_RETRY_EXC_ERR(12) opcode=IBV_WC_RECV_RDMA_WITH_IMM(129) vendor_err=129 localGid ::ffff:1.1.2.2 remoteGids::ffff:1.1.1.4 hca mlx5_1

[2026-09-09 10:46:34] ubuntu4:250415:250528 [1] transport/net_ib/[p2p.cc:783](https://p2p.cc:783/) NCCL WARN NET/IB: ncclIbTest: Got CQE with error (devIndex=0, req=0x7fa5a800e028, comm=0x7fa5a800e000 (send), wr_id=0, qp_num=21535)

[2026-09-09 10:46:34] ubuntu4:250415:250528 [1] transport/net_ib/[p2p.cc:648](https://p2p.cc:648/) NCCL WARN NET/IB: Got completion from peer 10.153.235.11<52743> with status=IBV_WC_RETRY_EXC_ERR(12) opcode=IBV_WC_RDMA_WRITE(1) vendor_err=129 localGid ::ffff:1.1.1.4 remoteGids::ffff:1.1.2.2 hca mlx5_0

[2026-09-09 10:46:34] ubuntu4:250414:250527 [0] transport/net_ib/[p2p.cc:783](https://p2p.cc:783/) NCCL WARN NET/IB: ncclIbTest: Got CQE with error (devIndex=0, req=0x7fd6cc00e028, comm=0x7fd6cc00e000 (recv), wr_id=0, qp_num=21536)

[2026-09-09 10:46:34] ubuntu4:250414:250527 [0] transport/net_ib/[p2p.cc:648](https://p2p.cc:648/) NCCL WARN NET/IB: Got completion from peer 10.153.235.11<38830> with status=IBV_WC_RETRY_EXC_ERR(12) opcode=IBV_WC_RDMA_WRITE(1) vendor_err=129 localGid ::ffff:1.1.1.4 remoteGids::ffff:1.1.2.2 hca mlx5_0

### Steps to Reproduce the Issue

**Key observations**:
- All ranks successfully complete the first 10 AllReduce iterations on the full communicator
- Excluded rank (rank 0) exits without calling ncclCommShrink
- Remaining ranks report shrink success (`Init COMPLETE`)
- IB errors appear during AllReduce on the shrunk communicator
- Multiple ranks report errors simultaneously, then the job hangs permanently

---

### Steps to Reproduce the Issue

**Minimal Steps**:

1. Compile the provided test program `two_host_4gpu.c`:
```bash
mpicxx -o two_host_4gpu two_host_4gpu.c -I${NCCL_HOME}/include -L${NCCL_HOME}/lib -lnccl -lcudart
Run on 2 nodes (2 GPUs per node):

bash
mpirun -np 4 -host node1:2,node2:2 \
  -x LD_LIBRARY_PATH=/path/to/nccl/build/lib:$LD_LIBRARY_PATH \
  -x NCCL_DEBUG=INFO \
  ./two_host_4gpu --exclude=0
Observe the failure:

First 10 AllReduce iterations succeed (full communicator)

Rank 0 is excluded and exits (does NOT call ncclCommShrink)

Ranks 1, 2, 3 call ncclCommShrink to create a size=3 communicator

IB errors appear during AllReduce on the new communicator, followed by hang

Environment Details:

OS: Ubuntu 20.04.6 LTS

CUDA version: 13.0 (cudaDriverVersion 13030)

NCCL version: 2.30.4+cuda13.3 (git HEAD 1933fdd-dirty)

MPI implementation: OpenMPI 4.1.9a1

Network: RoCE (mlx5_0, mlx5_1)

GPU: 2 GPUs per node

Intermittency:

Reproducible 100% of the time

Errors always occur during AllReduce after shrink

Previous Success:

Not tested with older NCCL versions for shrink functionality

Works correctly in single-node environment (no IB errors)

Issue only appears in multi-node IB/RoCE scenarios

### NCCL Version

2.30.4 + cuda13.3

### Your platform details

GPU & Network：
<system version="1">
  <cpu host_hash="0xceea43a840550885" numaid="0" affinity="0000,000fffff,ff000000,0fffffff" arch="x86_64" vendor="GenuineIntel" familyid="6" modelid="106">
    <pci busid="0000:16:00.0" class="0x020000" vendor="0x15b3" device="0x101d" subsystem_vendor="0x15b3" subsystem_device="0x0016" link_speed="16.0 GT/s PCIe" link_width="8">
      <nic>
        <net name="mlx5_0" dev="0" latency="0" speed="100000" port="1" guid="0x78ad550003d3ebe8" maxconn="131072" gdr="0" net="1" gin="1"/>
        <net name="mlx5_1" dev="1" latency="0" speed="100000" port="2" guid="0x78ad550003d3ebe8" maxconn="131072" gdr="0" net="1" gin="1"/>
      </nic>
    </pci>
    <pci busid="0000:69:00.0" class="0x030200" vendor="0x10de" device="0x20b5" subsystem_vendor="0x10de" subsystem_device="0x1533" link_speed="16.0 GT/s PCIe" link_width="16">
      <gpu dev="0" sm="80" rank="0" gdr="1"/>
    </pci>
  </cpu>
  <cpu host_hash="0xceea43a840550885" numaid="1" affinity="ffff,fff00000,00ffffff,f0000000" arch="x86_64" vendor="GenuineIntel" familyid="6" modelid="106">
    <pci busid="0000:b1:00.0" class="0x030200" vendor="0x10de" device="0x20b5" subsystem_vendor="0x10de" subsystem_device="0x1533" link_speed="16.0 GT/s PCIe" link_width="16">
      <gpu dev="1" sm="80" rank="1" gdr="1"/>
    </pci>
  </cpu>
</system>

topology_10.153.235.13.xml

<system version="1">
  <cpu host_hash="0xfb6aa62d48a84bd4" numaid="0" affinity="0000,000fffff,ff000000,0fffffff" arch="x86_64" vendor="GenuineIntel" familyid="6" modelid="106">
    <pci busid="0000:16:00.0" class="0x020000" vendor="0x15b3" device="0x101d" subsystem_vendor="0x15b3" subsystem_device="0x0016" link_speed="16.0 GT/s PCIe" link_width="16">
      <nic>
        <net name="mlx5_0" dev="0" latency="0" speed="100000" port="1" guid="0x40ac550003d3ebe8" maxconn="131072" gdr="0" net="1" gin="1"/>
        <net name="mlx5_1" dev="1" latency="0" speed="100000" port="2" guid="0x40ac550003d3ebe8" maxconn="131072" gdr="0" net="1" gin="1"/>
      </nic>
    </pci>
    <pci busid="0000:69:00.0" class="0x030200" vendor="0x10de" device="0x20b5" subsystem_vendor="0x10de" subsystem_device="0x1533" link_speed="16.0 GT/s PCIe" link_width="16">
      <gpu dev="0" sm="80" rank="0" gdr="1"/>
    </pci>
  </cpu>
  <cpu host_hash="0xfb6aa62d48a84bd4" numaid="1" affinity="ffff,fff00000,00ffffff,f0000000" arch="x86_64" vendor="GenuineIntel" familyid="6" modelid="106">
    <pci busid="0000:b1:00.0" class="0x030200" vendor="0x10de" device="0x20b5" subsystem_vendor="0x10de" subsystem_device="0x1533" link_speed="16.0 GT/s PCIe" link_width="16">
      <gpu dev="1" sm="80" rank="1" gdr="1"/>
    </pci>
  </cpu>
</system>**



### Error Message & Behavior

__actual is previos Debug Logs, and  is hang;_

this is expected: 

/nccl_bak/nccl/docs/examples/01_communicators/test$ /usr/mpi/gcc/openmpi-4.1.9a1/bin/mpirun   -x LD_LIBRARY_PATH=/home/pengbobo/nccl_bak/nccl/build/lib:$LD_LIBRARY_PATH   -x NCCL_DEBUG=INFO   -np 4 -host 10.153.235.11:2,10.153.235.13:2   ./two_host_4gpu --exclude=0,1
[1] Global rank 1, local rank 1, using GPU 1
[3] Global rank 3, local rank 1, using GPU 1
[0] Global rank 0, local rank 0, using GPU 0
ubuntu2:321049:321049 [0] NCCL INFO ncclOsDlopen(libnccl-env.so) failed: libnccl-env.so: cannot open shared object file: No such file or directory
ubuntu2:321049:321049 [0] NCCL INFO ENV/Plugin: Could not find: libnccl-env.so
ubuntu2:321049:321049 [0] NCCL INFO Bootstrap: Using ens16f1:10.153.235.11<0>
ubuntu2:321049:321049 [0] NCCL INFO cudaDriverVersion 13030
ubuntu2:321050:321050 [1] NCCL INFO ncclOsDlopen(libnccl-env.so) failed: libnccl-env.so: cannot open shared object file: No such file or directory
ubuntu2:321050:321050 [1] NCCL INFO ENV/Plugin: Could not find: libnccl-env.so
ubuntu2:321050:321050 [1] NCCL INFO cudaDriverVersion 13030
ubuntu4:251908:251908 [1] NCCL INFO ncclOsDlopen(libnccl-env.so) failed: libnccl-env.so: cannot open shared object file: No such file or directory
ubuntu4:251908:251908 [1] NCCL INFO ENV/Plugin: Could not find: libnccl-env.so
ubuntu4:251908:251908 [1] NCCL INFO cudaDriverVersion 13030
ubuntu2:321049:321049 [0] NCCL INFO NCCL version 2.30.4+cuda13.3
ubuntu2:321049:321049 [0] NCCL INFO NCCL git version HEAD 1933fdd-dirty
ubuntu2:321050:321050 [1] NCCL INFO Bootstrap: Using ens16f1:10.153.235.11<0>
ubuntu2:321050:321050 [1] NCCL INFO NCCL version 2.30.4+cuda13.3
ubuntu2:321050:321050 [1] NCCL INFO NCCL git version HEAD 1933fdd-dirty
ubuntu4:251908:251908 [1] NCCL INFO Bootstrap: Using ens16f1:10.153.235.13<0>
ubuntu4:251908:251908 [1] NCCL INFO NCCL version 2.30.4+cuda13.3
ubuntu4:251908:251908 [1] NCCL INFO NCCL git version HEAD 1933fdd-dirty
[2] Global rank 2, local rank 0, using GPU 0
ubuntu4:251907:251907 [0] NCCL INFO ncclOsDlopen(libnccl-env.so) failed: libnccl-env.so: cannot open shared object file: No such file or directory
ubuntu4:251907:251907 [0] NCCL INFO ENV/Plugin: Could not find: libnccl-env.so
ubuntu4:251907:251907 [0] NCCL INFO cudaDriverVersion 13030
ubuntu4:251907:251907 [0] NCCL INFO Bootstrap: Using ens16f1:10.153.235.13<0>
ubuntu4:251907:251907 [0] NCCL INFO NCCL version 2.30.4+cuda13.3
ubuntu4:251907:251907 [0] NCCL INFO NCCL git version HEAD 1933fdd-dirty
ubuntu2:321050:321050 [1] NCCL INFO ncclOsDlopen(libnccl-net.so) failed: libnccl-net.so: cannot open shared object file: No such file or directory
ubuntu2:321050:321050 [1] NCCL INFO NET/Plugin: Could not find: libnccl-net.so
ubuntu2:321050:321050 [1] NCCL INFO NCCL_IB_HCA set to mlx5_0,mlx5_1
ubuntu4:251908:251908 [1] NCCL INFO ncclOsDlopen(libnccl-net.so) failed: libnccl-net.so: cannot open shared object file: No such file or directory
ubuntu4:251908:251908 [1] NCCL INFO NET/Plugin: Could not find: libnccl-net.so
ubuntu4:251908:251908 [1] NCCL INFO NCCL_IB_HCA set to mlx5_0,mlx5_1
ubuntu2:321050:321050 [1] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [1]mlx5_1:1/RoCE [RO]; OOB ens16f1:10.153.235.11<0>
ubuntu2:321050:321050 [1] NCCL INFO Initialized NET plugin IB
ubuntu2:321050:321050 [1] NCCL INFO Assigned NET plugin IB to comm
ubuntu2:321050:321050 [1] NCCL INFO ncclOsDlopen(libnccl-gin.so) failed: libnccl-gin.so: cannot open shared object file: No such file or directory
ubuntu2:321050:321050 [1] NCCL INFO GIN/Plugin: Could not find: libnccl-gin.so
ubuntu2:321050:321050 [1] NCCL INFO Assigned GIN plugin GIN_IB_GDAKI to comm
ubuntu2:321050:321050 [1] NCCL INFO Assigned RMA plugin GIN_IB_PROXY to comm
ubuntu2:321050:321050 [1] NCCL INFO Using network IB
ubuntu2:321050:321050 [1] NCCL INFO Loaded NVML from libnvidia-ml.so.1
ubuntu4:251908:251908 [1] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [1]mlx5_1:1/RoCE [RO]; OOB ens16f1:10.153.235.13<0>
ubuntu4:251908:251908 [1] NCCL INFO Initialized NET plugin IB
ubuntu4:251908:251908 [1] NCCL INFO Assigned NET plugin IB to comm
ubuntu4:251908:251908 [1] NCCL INFO ncclOsDlopen(libnccl-gin.so) failed: libnccl-gin.so: cannot open shared object file: No such file or directory
ubuntu4:251908:251908 [1] NCCL INFO GIN/Plugin: Could not find: libnccl-gin.so
ubuntu4:251908:251908 [1] NCCL INFO Assigned GIN plugin GIN_IB_GDAKI to comm
ubuntu4:251908:251908 [1] NCCL INFO Assigned RMA plugin GIN_IB_PROXY to comm
ubuntu4:251908:251908 [1] NCCL INFO Using network IB
ubuntu4:251908:251908 [1] NCCL INFO Loaded NVML from libnvidia-ml.so.1
ubuntu2:321050:321050 [1] NCCL INFO [Rank 1] ncclCommInitRank comm 0x5563e3b79140 rank 1 nranks 4 cudaDev 1 nvmlDev 1 busId b1000 commId 0xef3a13f82ff54f6a - Init START
ubuntu4:251908:251908 [1] NCCL INFO [Rank 3] ncclCommInitRank comm 0x560a4f522ae0 rank 3 nranks 4 cudaDev 1 nvmlDev 1 busId b1000 commId 0xef3a13f82ff54f6a - Init START
ubuntu2:321049:321049 [0] NCCL INFO ncclOsDlopen(libnccl-net.so) failed: libnccl-net.so: cannot open shared object file: No such file or directory
ubuntu2:321049:321049 [0] NCCL INFO NET/Plugin: Could not find: libnccl-net.so
ubuntu2:321049:321049 [0] NCCL INFO NCCL_IB_HCA set to mlx5_0,mlx5_1
ubuntu2:321049:321049 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [1]mlx5_1:1/RoCE [RO]; OOB ens16f1:10.153.235.11<0>
ubuntu2:321049:321049 [0] NCCL INFO Initialized NET plugin IB
ubuntu2:321049:321049 [0] NCCL INFO Assigned NET plugin IB to comm
ubuntu2:321049:321049 [0] NCCL INFO ncclOsDlopen(libnccl-gin.so) failed: libnccl-gin.so: cannot open shared object file: No such file or directory
ubuntu2:321049:321049 [0] NCCL INFO GIN/Plugin: Could not find: libnccl-gin.so
ubuntu2:321049:321049 [0] NCCL INFO Assigned GIN plugin GIN_IB_GDAKI to comm
ubuntu2:321049:321049 [0] NCCL INFO Assigned RMA plugin GIN_IB_PROXY to comm
ubuntu2:321049:321049 [0] NCCL INFO Using network IB
ubuntu2:321049:321049 [0] NCCL INFO Loaded NVML from libnvidia-ml.so.1
ubuntu4:251907:251907 [0] NCCL INFO ncclOsDlopen(libnccl-net.so) failed: libnccl-net.so: cannot open shared object file: No such file or directory
ubuntu4:251907:251907 [0] NCCL INFO NET/Plugin: Could not find: libnccl-net.so
ubuntu4:251907:251907 [0] NCCL INFO NCCL_IB_HCA set to mlx5_0,mlx5_1
ubuntu4:251907:251907 [0] NCCL INFO NET/IB : Using [0]mlx5_0:1/RoCE [1]mlx5_1:1/RoCE [RO]; OOB ens16f1:10.153.235.13<0>
ubuntu4:251907:251907 [0] NCCL INFO Initialized NET plugin IB
ubuntu4:251907:251907 [0] NCCL INFO Assigned NET plugin IB to comm
ubuntu4:251907:251907 [0] NCCL INFO ncclOsDlopen(libnccl-gin.so) failed: libnccl-gin.so: cannot open shared object file: No such file or directory
ubuntu4:251907:251907 [0] NCCL INFO GIN/Plugin: Could not find: libnccl-gin.so
ubuntu4:251907:251907 [0] NCCL INFO Assigned GIN plugin GIN_IB_GDAKI to comm
ubuntu4:251907:251907 [0] NCCL INFO Assigned RMA plugin GIN_IB_PROXY to comm
ubuntu4:251907:251907 [0] NCCL INFO Using network IB
ubuntu4:251907:251907 [0] NCCL INFO Loaded NVML from libnvidia-ml.so.1
ubuntu2:321049:321049 [0] NCCL INFO [Rank 0] ncclCommInitRank comm 0x5612d31d6590 rank 0 nranks 4 cudaDev 0 nvmlDev 0 busId 69000 commId 0xef3a13f82ff54f6a - Init START

[2026-09-09 11:29:56] ubuntu2:321049:321049 [0] ras/client_support.cc:181 NCCL WARN Call to bind failed: Address already in use
ubuntu2:321049:321049 [0] NCCL INFO RAS failed to establish a client listening socket at localhost:28028
ubuntu4:251907:251907 [0] NCCL INFO [Rank 2] ncclCommInitRank comm 0x56461d4d4c10 rank 2 nranks 4 cudaDev 0 nvmlDev 0 busId 69000 commId 0xef3a13f82ff54f6a - Init START

[2026-09-09 11:29:56] ubuntu4:251908:251908 [1] ras/client_support.cc:181 NCCL WARN Call to bind failed: Address already in use
ubuntu4:251908:251908 [1] NCCL INFO RAS failed to establish a client listening socket at localhost:28028

[2026-09-09 11:29:56] ubuntu2:321050:321050 [1] ras/client_support.cc:181 NCCL WARN Call to bind failed: Address already in use
ubuntu2:321050:321050 [1] NCCL INFO RAS failed to establish a client listening socket at localhost:28028

[2026-09-09 11:29:56] ubuntu4:251907:251907 [0] ras/client_support.cc:181 NCCL WARN Call to bind failed: Address already in use
ubuntu4:251907:251907 [0] NCCL INFO RAS failed to establish a client listening socket at localhost:28028
ubuntu2:321050:321050 [1] NCCL INFO Bootstrap timings total 0.433246 (create 0.000034, send 0.000141, recv 0.429239, ring 0.003284, delay 0.000001)
ubuntu4:251908:251908 [1] NCCL INFO Bootstrap timings total 0.409289 (create 0.000038, send 0.000203, recv 0.378810, ring 0.003745, delay 0.000001)
ubuntu4:251907:251907 [0] NCCL INFO Bootstrap timings total 0.004841 (create 0.000036, send 0.000148, recv 0.000358, ring 0.003246, delay 0.000001)
ubuntu2:321049:321049 [0] NCCL INFO Bootstrap timings total 0.040396 (create 0.000031, send 0.000134, recv 0.009563, ring 0.029746, delay 0.000002)
ubuntu4:251908:251908 [1] NCCL INFO ncclTopoGetCpuAffinity: Affinity for GPU 1 is 28,84. (GPU affinity = 28-55,84-111 ; CPU affinity = 28,84).
ubuntu4:251908:251908 [1] NCCL INFO NVLS multicast support is not available on dev 1
ubuntu4:251907:251907 [0] NCCL INFO ncclTopoGetCpuAffinity: Affinity for GPU 0 is 0,56. (GPU affinity = 0-27,56-83 ; CPU affinity = 0,56).
ubuntu4:251907:251907 [0] NCCL INFO NVLS multicast support is not available on dev 0
ubuntu4:251908:251908 [1] NCCL INFO Rank 3: 3 Net devices
ubuntu4:251908:251908 [1] NCCL INFO Rank 3: 0 CollNet devices
ubuntu4:251907:251907 [0] NCCL INFO Rank 2: 3 Net devices
ubuntu4:251907:251907 [0] NCCL INFO Rank 2: 0 CollNet devices
ubuntu2:321049:321049 [0] NCCL INFO ncclTopoGetCpuAffinity: Affinity for GPU 0 is 0,56. (GPU affinity = 0-27,56-83 ; CPU affinity = 0,56).
ubuntu2:321049:321049 [0] NCCL INFO NVLS multicast support is not available on dev 0
ubuntu2:321050:321050 [1] NCCL INFO ncclTopoGetCpuAffinity: Affinity for GPU 1 is 28,84. (GPU affinity = 28-55,84-111 ; CPU affinity = 28,84).
ubuntu2:321050:321050 [1] NCCL INFO NVLS multicast support is not available on dev 1
ubuntu2:321049:321049 [0] NCCL INFO Rank 0: 3 Net devices
ubuntu2:321049:321049 [0] NCCL INFO Rank 0: 0 CollNet devices
ubuntu2:321050:321050 [1] NCCL INFO Rank 1: 3 Net devices
ubuntu2:321050:321050 [1] NCCL INFO Rank 1: 0 CollNet devices
ubuntu2:321050:321050 [1] NCCL INFO comm 0x5563e3b79140 rank 1 nRanks 4 nNodes 2 localRanks 2 localRank 1 MNNVL 0
ubuntu2:321050:321050 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0
ubuntu2:321050:321050 [1] NCCL INFO P2P Chunksize set to 131072
ubuntu2:321050:321050 [1] NCCL INFO Tuning P2P operations with maxP2pPeers = 4
ubuntu4:251908:251908 [1] NCCL INFO comm 0x560a4f522ae0 rank 3 nRanks 4 nNodes 2 localRanks 2 localRank 1 MNNVL 0
ubuntu2:321050:321050 [1] NCCL INFO ncclOsDlopen(libnccl-profiler.so) failed: libnccl-profiler.so: cannot open shared object file: No such file or directory
ubuntu2:321050:321050 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so
ubuntu2:321050:321050 [1] NCCL INFO Check P2P Type isAllDirectP2p 0 directMode 0 isAllCudaP2p 1
ubuntu4:251908:251908 [1] NCCL INFO Trees [0] -1/-1/-1->3->2 [1] -1/-1/-1->3->2
ubuntu4:251908:251908 [1] NCCL INFO P2P Chunksize set to 131072
ubuntu4:251908:251908 [1] NCCL INFO Tuning P2P operations with maxP2pPeers = 4
ubuntu2:321049:321049 [0] NCCL INFO Local Net device counts across ranks: min 3 max 3
ubuntu2:321049:321049 [0] NCCL INFO Local CollNet device counts across ranks: min 0 max 0
ubuntu2:321049:321049 [0] NCCL INFO comm 0x5612d31d6590 rank 0 nRanks 4 nNodes 2 localRanks 2 localRank 0 MNNVL 0
ubuntu2:321049:321049 [0] NCCL INFO Channel 00/02 : 0 1 2 3
ubuntu2:321049:321049 [0] NCCL INFO Channel 01/02 : 0 1 2 3
ubuntu2:321049:321049 [0] NCCL INFO Trees [0] 1/2/-1->0->-1 [1] 1/-1/-1->0->2
ubuntu2:321049:321049 [0] NCCL INFO P2P Chunksize set to 131072
ubuntu2:321049:321049 [0] NCCL INFO Tuning P2P operations with maxP2pPeers = 4
ubuntu4:251908:251908 [1] NCCL INFO ncclOsDlopen(libnccl-profiler.so) failed: libnccl-profiler.so: cannot open shared object file: No such file or directory
ubuntu4:251908:251908 [1] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so
ubuntu2:321049:321049 [0] NCCL INFO ncclOsDlopen(libnccl-profiler.so) failed: libnccl-profiler.so: cannot open shared object file: No such file or directory
ubuntu2:321049:321049 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so
ubuntu2:321049:321049 [0] NCCL INFO Check P2P Type isAllDirectP2p 0 directMode 0 isAllCudaP2p 1
ubuntu4:251908:251908 [1] NCCL INFO Check P2P Type isAllDirectP2p 0 directMode 0 isAllCudaP2p 1
ubuntu4:251907:251907 [0] NCCL INFO comm 0x56461d4d4c10 rank 2 nRanks 4 nNodes 2 localRanks 2 localRank 0 MNNVL 0
ubuntu4:251907:251907 [0] NCCL INFO Trees [0] 3/-1/-1->2->0 [1] 3/0/-1->2->-1
ubuntu4:251907:251907 [0] NCCL INFO P2P Chunksize set to 131072
ubuntu4:251907:251907 [0] NCCL INFO Tuning P2P operations with maxP2pPeers = 4
ubuntu4:251907:251907 [0] NCCL INFO ncclOsDlopen(libnccl-profiler.so) failed: libnccl-profiler.so: cannot open shared object file: No such file or directory
ubuntu4:251907:251907 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so
ubuntu4:251907:251907 [0] NCCL INFO Check P2P Type isAllDirectP2p 0 directMode 0 isAllCudaP2p 1
ubuntu4:251908:251948 [0] NCCL INFO [Proxy Service UDS] Device 1 CPU core 28
ubuntu4:251908:251947 [0] NCCL INFO [Proxy Service] Device 1 CPU core 28
ubuntu2:321050:321136 [0] NCCL INFO [Proxy Service UDS] Device 1 CPU core 28
ubuntu2:321049:321137 [0] NCCL INFO [Proxy Service] Device 0 CPU core 0
ubuntu2:321049:321138 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 56
ubuntu2:321050:321135 [0] NCCL INFO [Proxy Service] Device 1 CPU core 28
ubuntu2:321050:321050 [1] NCCL INFO ncclOsDlopen(libnccl-tuner.so) failed: libnccl-tuner.so: cannot open shared object file: No such file or directory
ubuntu2:321050:321050 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
ubuntu2:321050:321050 [1] NCCL INFO threadThresholds 8/8/64 | 32/8/64 | 512 | 512
ubuntu2:321050:321050 [1] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 1 p2p channels per peer
ubuntu2:321050:321050 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 1, globalGinSupport 0, globalNicFused 1 cuMemGdrSupport 1
ubuntu2:321049:321049 [0] NCCL INFO ncclOsDlopen(libnccl-tuner.so) failed: libnccl-tuner.so: cannot open shared object file: No such file or directory
ubuntu2:321049:321049 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
ubuntu2:321049:321049 [0] NCCL INFO threadThresholds 8/8/64 | 32/8/64 | 512 | 512
ubuntu2:321049:321049 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 1 p2p channels per peer
ubuntu2:321049:321049 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 1, globalGinSupport 0, globalNicFused 1 cuMemGdrSupport 1
ubuntu2:321049:321049 [0] NCCL INFO CC Off, workFifoBytes 1048576
ubuntu4:251907:251949 [0] NCCL INFO [Proxy Service] Device 0 CPU core 56
ubuntu4:251907:251950 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 56
ubuntu2:321050:321050 [1] NCCL INFO ncclCommInitRank comm 0x5563e3b79140 rank 1 nranks 4 cudaDev 1 nvmlDev 1 busId b1000 commId 0xef3a13f82ff54f6a - Init COMPLETE
ubuntu2:321049:321049 [0] NCCL INFO ncclCommInitRank comm 0x5612d31d6590 rank 0 nranks 4 cudaDev 0 nvmlDev 0 busId 69000 commId 0xef3a13f82ff54f6a - Init COMPLETE
ubuntu2:321049:321049 [0] NCCL INFO Init timings - ncclCommInitRank: rank 0 nranks 4 total 1.32 (kernels 1.17, alloc 0.07, bootstrap 0.04, allgathers 0.00, topo 0.02, graphs 0.00, connections 0.01, rest 0.00)
[0] Full communicator initialized. world size=4
[0] Running 10 AllReduce before shrink...
ubuntu2:321050:321050 [1] NCCL INFO Init timings - ncclCommInitRank: rank 1 nranks 4 total 1.32 (kernels 0.78, alloc 0.06, bootstrap 0.43, allgathers 0.00, topo 0.02, graphs 0.00, connections 0.01, rest 0.00)
[1] Full communicator initialized. world size=4
[1] Running 10 AllReduce before shrink...
ubuntu4:251908:251908 [1] NCCL INFO ncclOsDlopen(libnccl-tuner.so) failed: libnccl-tuner.so: cannot open shared object file: No such file or directory
ubuntu4:251908:251908 [1] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
ubuntu4:251908:251908 [1] NCCL INFO NCCL_ALGO set by environment to
ubuntu4:251908:251908 [1] NCCL INFO threadThresholds 8/8/64 | 32/8/64 | 512 | 512
ubuntu4:251908:251908 [1] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 1 p2p channels per peer
ubuntu4:251908:251908 [1] NCCL INFO Symmetric memory is not supported. cuMemEnable 1, globalGinSupport 0, globalNicFused 1 cuMemGdrSupport 1
ubuntu4:251907:251907 [0] NCCL INFO ncclOsDlopen(libnccl-tuner.so) failed: libnccl-tuner.so: cannot open shared object file: No such file or directory
ubuntu4:251907:251907 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
ubuntu4:251907:251907 [0] NCCL INFO NCCL_ALGO set by environment to
ubuntu4:251907:251907 [0] NCCL INFO threadThresholds 8/8/64 | 32/8/64 | 512 | 512
ubuntu4:251907:251907 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 1 p2p channels per peer
ubuntu4:251907:251907 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 1, globalGinSupport 0, globalNicFused 1 cuMemGdrSupport 1
ubuntu4:251908:251908 [1] NCCL INFO ncclCommInitRank comm 0x560a4f522ae0 rank 3 nranks 4 cudaDev 1 nvmlDev 1 busId b1000 commId 0xef3a13f82ff54f6a - Init COMPLETE
ubuntu4:251907:251907 [0] NCCL INFO ncclCommInitRank comm 0x56461d4d4c10 rank 2 nranks 4 cudaDev 0 nvmlDev 0 busId 69000 commId 0xef3a13f82ff54f6a - Init COMPLETE
ubuntu4:251907:251907 [0] NCCL INFO Init timings - ncclCommInitRank: rank 2 nranks 4 total 1.30 (kernels 1.17, alloc 0.07, bootstrap 0.00, allgathers 0.00, topo 0.02, graphs 0.00, connections 0.02, rest 0.00)
[2] Full communicator initialized. world size=4
[2] Running 10 AllReduce before shrink...
ubuntu4:251908:251908 [1] NCCL INFO Init timings - ncclCommInitRank: rank 3 nranks 4 total 1.33 (kernels 0.79, alloc 0.08, bootstrap 0.41, allgathers 0.00, topo 0.02, graphs 0.00, connections 0.02, rest 0.00)
[3] Full communicator initialized. world size=4
[3] Running 10 AllReduce before shrink...
ubuntu2:321049:321139 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 56
ubuntu2:321049:321049 [0] NCCL INFO Channel 00/0 : 3[1] -> 0[0] [receive] via NET/IB/2
ubuntu4:251907:251952 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 0
ubuntu2:321049:321049 [0] NCCL INFO Channel 01/0 : 3[1] -> 0[0] [receive] via NET/IB/2
ubuntu2:321049:321049 [0] NCCL INFO Channel 00 : 0[0] -> 1[1] via SHM/direct/direct
ubuntu2:321050:321141 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 28
ubuntu2:321050:321050 [1] NCCL INFO Channel 00/0 : 1[1] -> 2[0] [send] via NET/IB/2
ubuntu4:251908:251953 [0] NCCL INFO [Proxy Progress] Device 1 CPU core 28
ubuntu4:251907:251907 [0] NCCL INFO Channel 00/0 : 1[1] -> 2[0] [receive] via NET/IB/2
ubuntu4:251908:251908 [1] NCCL INFO Channel 00/0 : 3[1] -> 0[0] [send] via NET/IB/2
ubuntu2:321049:321049 [0] NCCL INFO Channel 01 : 0[0] -> 1[1] via SHM/direct/direct
ubuntu2:321050:321050 [1] NCCL INFO Channel 01/0 : 1[1] -> 2[0] [send] via NET/IB/2
ubuntu4:251907:251907 [0] NCCL INFO Channel 01/0 : 1[1] -> 2[0] [receive] via NET/IB/2
ubuntu4:251908:251908 [1] NCCL INFO Channel 01/0 : 3[1] -> 0[0] [send] via NET/IB/2
ubuntu4:251907:251907 [0] NCCL INFO Channel 00 : 2[0] -> 3[1] via SHM/direct/direct
ubuntu4:251907:251907 [0] NCCL INFO Channel 01 : 2[0] -> 3[1] via SHM/direct/direct
ubuntu2:321050:321135 [1] NCCL INFO NCCL_IB_GID_INDEX set by environment to 3.
ubuntu2:321050:321135 [1] NCCL INFO NCCL_IB_TC set by environment to 162.
ubuntu4:251907:251949 [0] NCCL INFO NCCL_IB_GID_INDEX set by environment to 3.
ubuntu4:251908:251947 [1] NCCL INFO NCCL_IB_GID_INDEX set by environment to 3.
ubuntu4:251908:251947 [1] NCCL INFO NCCL_IB_TC set by environment to 162.
ubuntu2:321049:321137 [0] NCCL INFO NCCL_IB_GID_INDEX set by environment to 3.
ubuntu2:321050:321050 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 0
ubuntu2:321049:321049 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 0
ubuntu4:251908:251908 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 0
ubuntu4:251907:251907 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 0
[1] AllReduce iteration 0 completed.
[0] AllReduce iteration 0 completed.
[3] AllReduce iteration 0 completed.
[2] AllReduce iteration 0 completed.
[1] AllReduce iteration 1 completed.
[0] AllReduce iteration 1 completed.
[3] AllReduce iteration 1 completed.
[2] AllReduce iteration 1 completed.
[1] AllReduce iteration 2 completed.
[0] AllReduce iteration 2 completed.
[2] AllReduce iteration 2 completed.
[3] AllReduce iteration 2 completed.
[2] AllReduce iteration 3 completed.
[3] AllReduce iteration 3 completed.
[0] AllReduce iteration 3 completed.
[1] AllReduce iteration 3 completed.
[2] AllReduce iteration 4 completed.
[3] AllReduce iteration 4 completed.
[0] AllReduce iteration 4 completed.
[1] AllReduce iteration 4 completed.
[1] AllReduce iteration 5 completed.
[0] AllReduce iteration 5 completed.
[2] AllReduce iteration 5 completed.
[3] AllReduce iteration 5 completed.
[2] AllReduce iteration 6 completed.
[3] AllReduce iteration 6 completed.
[0] AllReduce iteration 6 completed.
[1] AllReduce iteration 6 completed.
[2] AllReduce iteration 7 completed.
[3] AllReduce iteration 7 completed.
[0] AllReduce iteration 7 completed.
[1] AllReduce iteration 7 completed.
[1] AllReduce iteration 8 completed.
[2] AllReduce iteration 8 completed.
[3] AllReduce iteration 8 completed.
[0] AllReduce iteration 8 completed.
[1] AllReduce iteration 9 completed.
[1] I am excluded, destroying full communicator and exiting.
[0] AllReduce iteration 9 completed.
[0] I am excluded, destroying full communicator and exiting.
[3] AllReduce iteration 9 completed.
[3] Calling ncclCommShrink to exclude ranks: 0 1
ubuntu4:251908:251908 [1] NCCL INFO Initialized NET plugin IB
ubuntu4:251908:251908 [1] NCCL INFO Assigned NET plugin IB to comm
ubuntu4:251908:251908 [1] NCCL INFO Assigned GIN plugin GIN_IB_GDAKI to comm
ubuntu4:251908:251908 [1] NCCL INFO Assigned RMA plugin GIN_IB_PROXY to comm
ubuntu4:251908:251908 [1] NCCL INFO Using network IB
ubuntu4:251908:251908 [1] NCCL INFO ncclCommShrink comm 0x560a53c8c740 rank 1 nranks 2 cudaDev 1 nvmlDev 1 busId b1000 parent 0x560a4f522ae0 childCount 0 color 0 key 3- Init START
[2] AllReduce iteration 9 completed.
[2] Calling ncclCommShrink to exclude ranks: 0 1
ubuntu4:251907:251907 [0] NCCL INFO Initialized NET plugin IB
ubuntu4:251907:251907 [0] NCCL INFO Assigned NET plugin IB to comm
ubuntu4:251907:251907 [0] NCCL INFO Assigned GIN plugin GIN_IB_GDAKI to comm
ubuntu4:251907:251907 [0] NCCL INFO Assigned RMA plugin GIN_IB_PROXY to comm
ubuntu4:251907:251907 [0] NCCL INFO Using network IB
ubuntu4:251907:251907 [0] NCCL INFO ncclCommShrink comm 0x564621c3e210 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 69000 parent 0x56461d4d4c10 childCount 0 color 0 key 2- Init START
ubuntu4:251908:251908 [1] NCCL INFO ncclTopoGetCpuAffinity: Affinity for GPU 1 is 28,84. (GPU affinity = 28-55,84-111 ; CPU affinity = 28,84).
ubuntu4:251908:251908 [1] NCCL INFO NVLS multicast support is not available on dev 1
ubuntu4:251908:251908 [1] NCCL INFO Rank 1: 3 Net devices
ubuntu4:251908:251908 [1] NCCL INFO Rank 1: 0 CollNet devices
ubuntu4:251907:251907 [0] NCCL INFO ncclTopoGetCpuAffinity: Affinity for GPU 0 is 0,56. (GPU affinity = 0-27,56-83 ; CPU affinity = 0,56).
ubuntu4:251907:251907 [0] NCCL INFO NVLS multicast support is not available on dev 0
ubuntu4:251907:251907 [0] NCCL INFO Rank 0: 3 Net devices
ubuntu4:251907:251907 [0] NCCL INFO Rank 0: 0 CollNet devices
ubuntu4:251907:251907 [0] NCCL INFO Local Net device counts across ranks: min 3 max 3
ubuntu4:251907:251907 [0] NCCL INFO Local CollNet device counts across ranks: min 0 max 0
ubuntu4:251907:251907 [0] NCCL INFO comm 0x564621c3e210 rank 0 nRanks 2 nNodes 1 localRanks 2 localRank 0 MNNVL 0
ubuntu4:251908:251908 [1] NCCL INFO comm 0x560a53c8c740 rank 1 nRanks 2 nNodes 1 localRanks 2 localRank 1 MNNVL 0
ubuntu4:251908:251908 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0
ubuntu4:251908:251908 [1] NCCL INFO P2P Chunksize set to 131072
ubuntu4:251908:251908 [1] NCCL INFO Check P2P Type isAllDirectP2p 0 directMode 0 isAllCudaP2p 1
ubuntu4:251907:251907 [0] NCCL INFO Channel 00/02 : 0 1
ubuntu4:251907:251907 [0] NCCL INFO Channel 01/02 : 0 1
ubuntu4:251907:251907 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1
ubuntu4:251907:251907 [0] NCCL INFO P2P Chunksize set to 131072
ubuntu4:251907:251907 [0] NCCL INFO Check P2P Type isAllDirectP2p 0 directMode 0 isAllCudaP2p 1
ubuntu4:251908:251955 [0] NCCL INFO [Proxy Service] Device 1 CPU core 28
ubuntu4:251908:251956 [0] NCCL INFO [Proxy Service UDS] Device 1 CPU core 28
ubuntu4:251907:251954 [0] NCCL INFO [Proxy Service] Device 0 CPU core 56
ubuntu4:251907:251957 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 56
ubuntu4:251907:251907 [0] NCCL INFO NCCL_ALGO set by environment to
ubuntu4:251907:251907 [0] NCCL INFO Enabled NCCL Func/Proto/Algo Matrix:
     Function |       LL     LL128    Simple   |          Tree           Ring  CollNetDirect   CollNetChain           NVLS       NVLSTree            PAT
    Broadcast |        1         2         1   |             1              1              1              1              1              1              1
       Reduce |        1         2         1   |             1              1              1              1              1              1              1
    AllGather |        1         2         1   |             1              1              1              1              1              1              1
ReduceScatter |        1         2         1   |             1              1              1              1              1              1              1
    AllReduce |        1         2         1   |             1              1              1              1              1              1              1

ubuntu4:251908:251908 [1] NCCL INFO NCCL_ALGO set by environment to
ubuntu4:251908:251908 [1] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
ubuntu4:251908:251908 [1] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
ubuntu4:251907:251907 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
ubuntu4:251907:251907 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
ubuntu4:251907:251907 [0] NCCL INFO CC Off, workFifoBytes 1048576
ubuntu4:251908:251908 [1] NCCL INFO ncclCommShrink comm 0x560a53c8c740 rank 1 nranks 2 cudaDev 1 nvmlDev 1 busId b1000 parent 0x560a4f522ae0 childCount 0 color 0 key 3 - Init COMPLETE
ubuntu4:251907:251907 [0] NCCL INFO ncclCommShrink comm 0x564621c3e210 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 69000 parent 0x56461d4d4c10 childCount 0 color 0 key 2 - Init COMPLETE
ubuntu4:251907:251907 [0] NCCL INFO Init timings - ncclCommShrink: rank 0 nranks 2 total 0.06 (kernels 0.00, alloc 0.00, bootstrap 0.00, allgathers 0.00, topo 0.04, graphs 0.00, connections 0.02, rest 0.00)
[2] Shrink success: new rank=0, new size=2
[2] Running 10 AllReduce after shrink...
ubuntu4:251908:251908 [1] NCCL INFO Init timings - ncclCommShrink: rank 1 nranks 2 total 0.07 (kernels 0.00, alloc 0.00, bootstrap 0.01, allgathers 0.01, topo 0.03, graphs 0.00, connections 0.02, rest 0.00)
[3] Shrink success: new rank=1, new size=2
[3] Running 10 AllReduce after shrink...
ubuntu4:251907:251907 [0] NCCL INFO Symmetric VA size=80GB
ubuntu4:251908:251908 [1] NCCL INFO Symmetric VA size=80GB
ubuntu4:251907:251907 [0] NCCL INFO Channel 00 : 0[0] -> 1[1] via SHM/direct/direct
ubuntu4:251907:251907 [0] NCCL INFO Channel 01 : 0[0] -> 1[1] via SHM/direct/direct
ubuntu4:251908:251908 [1] NCCL INFO Channel 00 : 1[1] -> 0[0] via SHM/direct/direct
ubuntu4:251908:251908 [1] NCCL INFO Channel 01 : 1[1] -> 0[0] via SHM/direct/direct
ubuntu4:251908:251908 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
ubuntu4:251907:251907 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
[3] AllReduce iteration 0 completed.
[2] AllReduce iteration 0 completed.
[2] AllReduce iteration 1 completed.
[3] AllReduce iteration 1 completed.
[2] AllReduce iteration 2 completed.
[3] AllReduce iteration 2 completed.
[2] AllReduce iteration 3 completed.
[3] AllReduce iteration 3 completed.
[3] AllReduce iteration 4 completed.
[2] AllReduce iteration 4 completed.
[2] AllReduce iteration 5 completed.
[3] AllReduce iteration 5 completed.
[3] AllReduce iteration 6 completed.
[2] AllReduce iteration 6 completed.
[3] AllReduce iteration 7 completed.
[2] AllReduce iteration 7 completed.
[3] AllReduce iteration 8 completed.
[2] AllReduce iteration 8 completed.
[3] AllReduce iteration 9 completed.
[2] AllReduce iteration 9 completed.
[0] Excluded rank done.
[2] Done.
[1] Excluded rank done.
[3] Done.
pengbobo@ubuntu2:~/nccl_bak/nccl/docs/examples/01_communicators/test$_

## 评论 (6)

### rbenayed · 2026-09-10

@perpyoke can you share the `two_host_4gpu.c` reproducer as well?

### perpyoke · 2026-09-11

actually，we already find the quetion. After the shrink, on host0 where rank0 was shrunk, the topology scan incorrectly detected two physical NICs, while host1's topology remained unchanged. This caused the channel selection to pick the wrong cross-NIC net path, which in turn led to the IB failure. But I see that makeVnic has already been fixed in 2.31
this is my test program.
#include "cuda_runtime.h"
#include "nccl.h"
#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>

#ifndef NCCL_SHRINK_ABORT
#define NCCL_SHRINK_ABORT 0
#endif

#define NCCLCHECK_RANK(cmd, rank)                                            \
  do {                                                                       \
    ncclResult_t res = cmd;                                                  \
    if (res != ncclSuccess) {                                                \
      fprintf(stderr, "[%d] NCCL FATAL %s:%d err=%s\n", rank, __FILE__, __LINE__, \
              ncclGetErrorString(res));                                      \
      MPI_Abort(MPI_COMM_WORLD, 1);                                          \
    }                                                                        \
  } while (0)

#define CUDACHECK_RANK(cmd, rank)                                            \
  do {                                                                       \
    cudaError_t err = cmd;                                                   \
    if (err != cudaSuccess) {                                                \
      fprintf(stderr, "[%d] CUDA FATAL %s:%d err=%s\n", rank, __FILE__, __LINE__, \
              cudaGetErrorString(err));                                      \
      MPI_Abort(MPI_COMM_WORLD, 1);                                          \
    }                                                                        \
  } while (0)

#define NCCLCHECK(cmd) NCCLCHECK_RANK(cmd, globalRank)
#define CUDACHECK(cmd) CUDACHECK_RANK(cmd, globalRank)

#define NUM_ITERATIONS 10
#define DATA_SIZE 1024

void run_allreduce_loop(ncclComm_t comm, int rank, int n_iters) {
    if (comm == NULL) {
        fprintf(stderr, "[%d] Error: run_allreduce_loop called with NULL communicator\n", rank);
        return;
    }
    float* devBuf = NULL;
    cudaStream_t stream;
    CUDACHECK_RANK(cudaMalloc(&devBuf, DATA_SIZE * sizeof(float)), rank);
    CUDACHECK_RANK(cudaStreamCreate(&stream), rank);

    for (int i = 0; i < n_iters; ++i) {
        CUDACHECK_RANK(cudaMemsetAsync(devBuf, 0, DATA_SIZE * sizeof(float), stream), rank);
        NCCLCHECK_RANK(ncclAllReduce(devBuf, devBuf, DATA_SIZE, ncclFloat, ncclSum, comm, stream), rank);
        CUDACHECK_RANK(cudaStreamSynchronize(stream), rank);
        printf("[%d] AllReduce iteration %d completed.\n", rank, i);
        fflush(stdout);
    }

    CUDACHECK_RANK(cudaFree(devBuf), rank);
    CUDACHECK_RANK(cudaStreamDestroy(stream), rank);
}

// Parse "--exclude=0,1,3"; return count and rank array
int parse_exclude_ranks(int argc, char* argv[], int** ranks_out) {
    for (int i = 1; i < argc; ++i) {
        if (strncmp(argv[i], "--exclude=", 10) == 0) {
            const char* val = argv[i] + 10;
            char* str = strdup(val);
            if (!str) return -1;
            int count = 1;
            char* p = str;
            while (*p) if (*p++ == ',') count++;
            int* ranks = (int*)malloc(count * sizeof(int));
            int idx = 0;
            char* token = strtok(str, ",");
            while (token && idx < count) {
                ranks[idx++] = atoi(token);
                token = strtok(NULL, ",");
            }
            free(str);
            *ranks_out = ranks;
            return idx;
        }
    }
    return 0;
}

// Check if a rank is in the exclude list
int is_excluded(int rank, int* excludeRanks, int excludeCnt) {
    for (int i = 0; i < excludeCnt; ++i) {
        if (excludeRanks[i] == rank) return 1;
    }
    return 0;
}

int main(int argc, char* argv[]) {
    MPI_Init(&argc, &argv);

    int globalRank, worldSize;
    MPI_Comm_rank(MPI_COMM_WORLD, &globalRank);
    MPI_Comm_size(MPI_COMM_WORLD, &worldSize);

    // Parse exclude argument
    int* excludeRanks = NULL;
    int excludeCnt = parse_exclude_ranks(argc, argv, &excludeRanks);
    if (excludeCnt < 0) {
        fprintf(stderr, "[%d] Error parsing --exclude argument.\n", globalRank);
        MPI_Abort(MPI_COMM_WORLD, 1);
    }
    if (excludeCnt == 0) {
        fprintf(stderr, "[%d] Warning: No --exclude specified. Will not shrink.\n", globalRank);
    }

    // Validate exclude list
    for (int i = 0; i < excludeCnt; ++i) {
        if (excludeRanks[i] < 0 || excludeRanks[i] >= worldSize) {
            fprintf(stderr, "[%d] Invalid exclude rank %d\n", globalRank, excludeRanks[i]);
            MPI_Abort(MPI_COMM_WORLD, 1);
        }
    }

    // Get local rank and bind GPU
    MPI_Comm local_comm;
    MPI_Comm_split_type(MPI_COMM_WORLD, MPI_COMM_TYPE_SHARED, 0, MPI_INFO_NULL, &local_comm);
    int local_rank;
    MPI_Comm_rank(local_comm, &local_rank);
    CUDACHECK(cudaSetDevice(local_rank));
    MPI_Comm_free(&local_comm);

    printf("[%d] Global rank %d, local rank %d, using GPU %d\n", globalRank, globalRank, local_rank, local_rank);
    fflush(stdout);

    ncclUniqueId uid;
    ncclComm_t fullComm;

    // 1. Sync UID
    if (globalRank == 0) {
        NCCLCHECK(ncclGetUniqueId(&uid));
    }
    MPI_Bcast(&uid, sizeof(ncclUniqueId), MPI_BYTE, 0, MPI_COMM_WORLD);

    // 2. Init full communicator
    NCCLCHECK(ncclCommInitRank(&fullComm, worldSize, uid, globalRank));
    printf("[%d] Full communicator initialized. world size=%d\n", globalRank, worldSize);
    fflush(stdout);

    // 3. Pre-shrink AllReduce
    printf("[%d] Running %d AllReduce before shrink...\n", globalRank, NUM_ITERATIONS);
    fflush(stdout);
    run_allreduce_loop(fullComm, globalRank, NUM_ITERATIONS);

    // 4. Check if this rank is excluded
    if (excludeCnt > 0 && is_excluded(globalRank, excludeRanks, excludeCnt)) {
        // Excluded rank: skip ncclCommShrink, destroy comm and exit
        printf("[%d] I am excluded, destroying full communicator and exiting.\n", globalRank);
        fflush(stdout);
        NCCLCHECK(ncclCommDestroy(fullComm));
        if (excludeRanks) free(excludeRanks);
        MPI_Finalize();
        printf("[%d] Excluded rank done.\n", globalRank);
        fflush(stdout);
        return 0;
    }

    // 5. Kept ranks: perform shrink
    ncclComm_t shrunkComm = NULL;
    if (excludeCnt > 0) {
        printf("[%d] Calling ncclCommShrink to exclude ranks: ", globalRank);
        for (int i = 0; i < excludeCnt; ++i) printf("%d ", excludeRanks[i]);
        printf("\n");
        fflush(stdout);
        ncclConfig_t* cfg = NULL;
        NCCLCHECK(ncclCommShrink(fullComm, excludeRanks, excludeCnt,
                                 &shrunkComm, cfg, NCCL_SHRINK_ABORT));
    } else {
        // No exclusions, skip shrink
        printf("[%d] No exclude ranks, skipping shrink.\n", globalRank);
        shrunkComm = fullComm;  // handle uniformly below
    }

    // 6. Post-shrink handling (only kept ranks reach here)
    if (shrunkComm != NULL && shrunkComm != fullComm) {
        int newRank, newSize;
        NCCLCHECK(ncclCommUserRank(shrunkComm, &newRank));
        NCCLCHECK(ncclCommCount(shrunkComm, &newSize));
        printf("[%d] Shrink success: new rank=%d, new size=%d\n", globalRank, newRank, newSize);
        fflush(stdout);

        printf("[%d] Running %d AllReduce after shrink...\n", globalRank, NUM_ITERATIONS);
        fflush(stdout);
        run_allreduce_loop(shrunkComm, globalRank, NUM_ITERATIONS);

        NCCLCHECK(ncclCommDestroy(shrunkComm));
        NCCLCHECK(ncclCommDestroy(fullComm));
    } else if (shrunkComm == fullComm) {
        // Shrink not performed
        printf("[%d] No shrink performed, running AllReduce on full communicator...\n", globalRank);
        run_allreduce_loop(fullComm, globalRank, NUM_ITERATIONS);
        NCCLCHECK(ncclCommDestroy(fullComm));
    }

    if (excludeRanks) free(excludeRanks);
    MPI_Finalize();
    printf("[%d] Done.\n", globalRank);
    fflush(stdout);
    return 0;
}

### rbenayed · 2026-09-11

@perpyoke, Thanks for the additional details. Could you confirm whether the mlx5_0 and mlx5_1 rails are isolated, or whether cross-rail RoCE communication is supported? This would help explain the retry errors on the path selected after shrink.

### perpyoke · 2026-09-14

 yes, is't isolate.  cross-rail RoCE communication is supporte.

### rbenayed · 2026-09-17

Confirmed that this bug was caused by physical NICs leaking into the topology when new communicators reused cached virtual NICs. This is fixed in NCCL 2.30.7. I think we can close this issue. Thanks for the reproducer and investigation!

### stephenmsachs · 2026-09-17

Closing per last comment. Thanks again for investigating.
