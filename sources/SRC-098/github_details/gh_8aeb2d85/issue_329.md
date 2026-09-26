# [Issue #329] Running nccl-tests on two docker on same host - uses same rank 0

source: https://github.com/NVIDIA/nccl-tests/issues/329
state: open | updated: 2025-07-01T13:18:00Z
labels: 

## 正文

I am trying to run two docker on same host ( single GPU and Mellanox RNIC)  
I created a macvlan network , so any docker when created creates a interface with 20.20.20.x ip address and all docker can commnunicate
with each other.
Commands used.

1.`docker network create -d macvlan --subnet=20.20.20.0/24 -o parent=enp175s0f0np0 network1`

2.`docker run --ipc=host --ulimit memlock=-1 --ulimit stack=67108864 --gpus all -it  --cap-add=IPC_LOCK --net=network1 --device=/dev/infiniband --device=/dev/infiniband/rdma_cm -v $(pwd)/nvidia-tools:/nvidia-tools --rm  docker.io/deepops/nccl-tests:2312
`

when i tried to run nccl-tests using openmpi on these two nodes i see that both side gets rank 0 only 

`mpirun --allow-run-as-root   -hostfile hosts.txt --tune tune.txt /usr/local/bin//all_reduce_perf -b 4M -e 4M -f 2 -g 1 -n 10 -w 2`

**hosts.txt**
20.20.20.2 slot=1
20.20.20.3 slot=1

**tune.txt**
-x NCCL_IB_DISABLE=0
-x NCCL_SOCKET_IFNAME=eth0
-x NCCL_IB_HCA=roce0
-x NCCL_IB_GID_INDEX=3
-x NCCL_DEBUG=TRACE
-x NCCL_DEBUG_SUBSYS=INIT,GRAPH,ENV,TUNING

RUN LOG

```
root@6a9ab017bb44:/nvidia-tools# mpirun --allow-run-as-root  -rank-by core   -hostfile hosts.txt --tune tune1.txt /usr/local/bin//all_reduce_perf -b 4M -e 4M -f 2 -g 1
 -n 10 -w 2
Warning: Permanently added '20.20.20.3' (ED25519) to the list of known hosts.
--------------------------------------------------------------------------
Process 799 Unable to locate the variable file "/nvidia-tools/tune1.txt" in the following search path:
   /nvidia-tools:/opt/hpcx/ompi/share/openmpi/amca-param-sets:/nvidia-tools
--------------------------------------------------------------------------
# nThread 1 nGpus 1 minBytes 4194304 maxBytes 4194304 step: 2(factor) warmup iters: 2 iters: 10 agg iters: 1 validation: 1 graph: 0
#
# Using devices
# nThread 1 nGpus 1 minBytes 4194304 maxBytes 4194304 step: 2(factor) warmup iters: 2 iters: 10 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid    454 on 6a9ab017bb44 device  0 [0xd8] NVIDIA T600
6a9ab017bb44:454:454 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to eth0
6a9ab017bb44:454:454 [0] NCCL INFO Bootstrap : Using eth0:20.20.20.2<0>
#  Rank  0 Group  0 Pid    808 on a4df80236412 device  0 [0xd8] NVIDIA T600
6a9ab017bb44:454:454 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v7 symbol.
6a9ab017bb44:454:454 [0] NCCL INFO NET/Plugin: Loaded net plugin NCCL RDMA Plugin v6 (v6)
6a9ab017bb44:454:454 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
6a9ab017bb44:454:454 [0] NCCL INFO NET/Plugin: Loaded coll plugin SHARP (v6)
a4df80236412:808:808 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to eth0
a4df80236412:808:808 [0] NCCL INFO Bootstrap : Using eth0:20.20.20.3<0>
a4df80236412:808:808 [0] NCCL INFO NET/Plugin: Failed to find ncclNetPlugin_v7 symbol.
a4df80236412:808:808 [0] NCCL INFO NET/Plugin: Loaded net plugin NCCL RDMA Plugin v6 (v6)
a4df80236412:808:808 [0] NCCL INFO NET/Plugin: Failed to find ncclCollNetPlugin_v7 symbol.
a4df80236412:808:808 [0] NCCL INFO NET/Plugin: Loaded coll plugin SHARP (v6)
6a9ab017bb44:454:454 [0] NCCL INFO cudaDriverVersion 12030
NCCL version 2.19.3+cuda12.3
a4df80236412:808:808 [0] NCCL INFO cudaDriverVersion 12020
NCCL version 2.19.3+cuda12.3
6a9ab017bb44:454:461 [0] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
6a9ab017bb44:454:461 [0] NCCL INFO P2P plugin IBext
6a9ab017bb44:454:461 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to eth0
6a9ab017bb44:454:461 [0] NCCL INFO NET/IB : Using [0]roce0:1/RoCE [RO]; OOB eth0:20.20.20.2<0>
6a9ab017bb44:454:461 [0] NCCL INFO Using non-device net plugin version 0
6a9ab017bb44:454:461 [0] NCCL INFO Using network IBext
a4df80236412:808:815 [0] NCCL INFO Plugin Path : /opt/hpcx/nccl_rdma_sharp_plugin/lib/libnccl-net.so
a4df80236412:808:815 [0] NCCL INFO P2P plugin IBext
a4df80236412:808:815 [0] NCCL INFO NCCL_SOCKET_IFNAME set by environment to eth0
a4df80236412:808:815 [0] NCCL INFO NET/IB : Using [0]roce0:1/RoCE [RO]; OOB eth0:20.20.20.3<0>
a4df80236412:808:815 [0] NCCL INFO Using non-device net plugin version 0
a4df80236412:808:815 [0] NCCL INFO Using network IBext
6a9ab017bb44:454:461 [0] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
6a9ab017bb44:454:461 [0] NCCL INFO comm 0x557b4c553c80 rank 0 nranks 1 cudaDev 0 nvmlDev 0 busId d8000 commId 0x428d7c9b55223c50 - Init START
6a9ab017bb44:454:461 [0] NCCL INFO NCCL_TOPO_DUMP_FILE set by environment to /tmp/topo.xml
6a9ab017bb44:454:461 [0] NCCL INFO === System : maxBw 5000.0 totalBw 0.0 ===
6a9ab017bb44:454:461 [0] NCCL INFO CPU/1 (1/1/2)
6a9ab017bb44:454:461 [0] NCCL INFO + PCI[12.0] - NIC/AF000
6a9ab017bb44:454:461 [0] NCCL INFO + PCI[12.0] - GPU/D8000 (0)
6a9ab017bb44:454:461 [0] NCCL INFO ==========================================
6a9ab017bb44:454:461 [0] NCCL INFO GPU/D8000 :GPU/D8000 (0/5000.000000/LOC) CPU/1 (1/12.000000/PHB)
6a9ab017bb44:454:461 [0] NCCL INFO Pattern 4, crossNic 0, nChannels 16, bw 40.000000/40.000000, type LOC/PIX, sameChannels 1
6a9ab017bb44:454:461 [0] NCCL INFO  0 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  1 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  2 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  3 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  4 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  5 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  6 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  7 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  8 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  9 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 10 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 11 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 12 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 13 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 14 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 15 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO Pattern 3, crossNic 0, nChannels 16, bw 40.000000/40.000000, type LOC/PIX, sameChannels 1
6a9ab017bb44:454:461 [0] NCCL INFO  0 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  1 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  2 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  3 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  4 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  5 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  6 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  7 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  8 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO  9 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 10 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 11 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 12 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 13 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 14 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO 15 : GPU/0
6a9ab017bb44:454:461 [0] NCCL INFO Tree 0 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 16 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 1 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 17 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 2 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 18 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 3 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 19 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 4 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 20 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 5 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 21 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 6 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 22 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 7 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 23 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 8 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 24 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 9 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 25 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 10 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 26 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 11 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 27 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 12 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 28 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 13 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 29 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 14 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 30 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 15 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Tree 31 : -1 -> 0 -> -1/-1/-1
6a9ab017bb44:454:461 [0] NCCL INFO Channel 00/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 01/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 02/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 03/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 04/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 05/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 06/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 07/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 08/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 09/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 10/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 11/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 12/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 13/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 14/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 15/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 16/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 17/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 18/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 19/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 20/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 21/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 22/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 23/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 24/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 25/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 26/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 27/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 28/32 :    0
a4df80236412:808:815 [0] NCCL INFO NCCL_DMABUF_ENABLE set by environment to 1.
6a9ab017bb44:454:461 [0] NCCL INFO Channel 29/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 30/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Channel 31/32 :    0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 00 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 01 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 02 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 03 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 04 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 05 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 06 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 07 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 08 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 09 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 10 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 11 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 12 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 13 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 14 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 15 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 16 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 17 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 18 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 19 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 20 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 21 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 22 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 23 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 24 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 25 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 26 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 27 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 28 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 29 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 30 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Ring 31 : 0 -> 0 -> 0
6a9ab017bb44:454:461 [0] NCCL INFO Trees [0] -1/-1/-1->0->-1 [1] -1/-1/-1->0->-1 [2] -1/-1/-1->0->-1 [3] -1/-1/-1->0->-1 [4] -1/-1/-1->0->-1 [5] -1/-1/-1->0->-1 [6] -1/-1/-1->0->-1 [7] -1/-1/-1->0->-1 [8] -1/-1/-1->0->-1 [9] -1/-1/-1->0->-1 [10] -1/-1/-1->0->-1 [11] -1/-1/-1->0->-1 [12] -1/-1/-1->0->-1 [13] -1/-1/-1->0->-1 [14] -1/-1/-1->0->-1 [15] -1/-1/-1->0->-1 [16] -1/-1/-1->0->-1 [17] -1/-1/-1->0->-1 [18] -1/-1/-1->0->-1 [19] -1/-1/-1->0->-1 [20] -1/-1/-1->0->-1 [21] -1/-1/-1->0->-1 [22] -1/-1/-1->0->-1 [23] -1/-1/-1->0->-1 [24] -1/-1/-1->0->-1 [25] -1/-1/-1->0->-1 [26] -1/-1/-1->0->-1 [27] -1/-1/-1->0->-1 [28] -1/-1/-1->0->-1 [29] -1/-1/-1->0->-1 [30] -1/-1/-1->0->-1 [31] -1/-1/-1->0->-1
6a9ab017bb44:454:461 [0] NCCL INFO P2P Chunksize set to 131072
6a9ab017bb44:454:461 [0] NCCL INFO Connected all rings
6a9ab017bb44:454:461 [0] NCCL INFO Connected all trees
6a9ab017bb44:454:461 [0] NCCL INFO 32 coll channels, 0 nvls channels, 32 p2p channels, 32 p2p channels per peer
a4df80236412:808:815 [0] NCCL INFO comm 0x559370ea1e30 rank 0 nranks 1 cudaDev 0 nvmlDev 0 busId d8000 commId 0x401fd347a370a800 - Init START
a4df80236412:808:815 [0] NCCL INFO NCCL_TOPO_DUMP_FILE set by environment to /tmp/topo.xml
a4df80236412:808:815 [0] NCCL INFO === System : maxBw 5000.0 totalBw 0.0 ===
a4df80236412:808:815 [0] NCCL INFO CPU/1 (1/1/2)
a4df80236412:808:815 [0] NCCL INFO + PCI[12.0] - NIC/AF000
a4df80236412:808:815 [0] NCCL INFO + PCI[12.0] - GPU/D8000 (0)
a4df80236412:808:815 [0] NCCL INFO ==========================================
a4df80236412:808:815 [0] NCCL INFO GPU/D8000 :GPU/D8000 (0/5000.000000/LOC) CPU/1 (1/12.000000/PHB)
a4df80236412:808:815 [0] NCCL INFO Setting affinity for GPU 0 to 02
a4df80236412:808:815 [0] NCCL INFO Pattern 4, crossNic 0, nChannels 16, bw 40.000000/40.000000, type LOC/PIX, sameChannels 1
a4df80236412:808:815 [0] NCCL INFO  0 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  1 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  2 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  3 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  4 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  5 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  6 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  7 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  8 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  9 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 10 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 11 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 12 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 13 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 14 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 15 : GPU/0
a4df80236412:808:815 [0] NCCL INFO Pattern 3, crossNic 0, nChannels 16, bw 40.000000/40.000000, type LOC/PIX, sameChannels 1
a4df80236412:808:815 [0] NCCL INFO  0 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  1 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  2 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  3 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  4 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  5 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  6 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  7 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  8 : GPU/0
a4df80236412:808:815 [0] NCCL INFO  9 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 10 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 11 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 12 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 13 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 14 : GPU/0
a4df80236412:808:815 [0] NCCL INFO 15 : GPU/0
a4df80236412:808:815 [0] NCCL INFO Tree 0 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 16 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 1 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 17 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 2 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 18 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 3 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 19 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 4 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 20 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 5 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 21 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 6 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 22 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 7 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 23 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 8 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 24 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 9 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 25 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 10 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 26 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 11 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 27 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 12 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 28 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 13 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 29 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 14 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 30 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 15 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Tree 31 : -1 -> 0 -> -1/-1/-1
a4df80236412:808:815 [0] NCCL INFO Channel 00/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 01/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 02/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 03/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 04/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 05/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 06/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 07/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 08/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 09/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 10/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 11/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 12/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 13/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 14/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 15/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 16/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 17/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 18/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 19/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 20/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 21/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 22/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 23/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 24/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 25/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 26/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 27/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 28/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 29/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 30/32 :    0
a4df80236412:808:815 [0] NCCL INFO Channel 31/32 :    0
a4df80236412:808:815 [0] NCCL INFO Ring 00 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 01 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 02 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 03 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 04 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 05 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 06 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 07 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 08 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 09 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 10 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 11 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 12 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 13 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 14 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 15 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 16 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 17 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 18 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 19 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 20 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 21 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 22 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 23 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 24 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 25 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 26 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 27 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 28 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 29 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 30 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Ring 31 : 0 -> 0 -> 0
a4df80236412:808:815 [0] NCCL INFO Trees [0] -1/-1/-1->0->-1 [1] -1/-1/-1->0->-1 [2] -1/-1/-1->0->-1 [3] -1/-1/-1->0->-1 [4] -1/-1/-1->0->-1 [5] -1/-1/-1->0->-1 [6] -1/-1/-1->0->-1 [7] -1/-1/-1->0->-1 [8] -1/-1/-1->0->-1 [9] -1/-1/-1->0->-1 [10] -1/-1/-1->0->-1 [11] -1/-1/-1->0->-1 [12] -1/-1/-1->0->-1 [13] -1/-1/-1->0->-1 [14] -1/-1/-1->0->-1 [15] -1/-1/-1->0->-1 [16] -1/-1/-1->0->-1 [17] -1/-1/-1->0->-1 [18] -1/-1/-1->0->-1 [19] -1/-1/-1->0->-1 [20] -1/-1/-1->0->-1 [21] -1/-1/-1->0->-1 [22] -1/-1/-1->0->-1 [23] -1/-1/-1->0->-1 [24] -1/-1/-1->0->-1 [25] -1/-1/-1->0->-1 [26] -1/-1/-1->0->-1 [27] -1/-1/-1->0->-1 [28] -1/-1/-1->0->-1 [29] -1/-1/-1->0->-1 [30] -1/-1/-1->0->-1 [31] -1/-1/-1->0->-1
a4df80236412:808:815 [0] NCCL INFO P2P Chunksize set to 131072
a4df80236412:808:815 [0] NCCL INFO Connected all rings
a4df80236412:808:815 [0] NCCL INFO Connected all trees
a4df80236412:808:815 [0] NCCL INFO 32 coll channels, 0 nvls channels, 32 p2p channels, 32 p2p channels per peer
6a9ab017bb44:454:461 [0] NCCL INFO Tuner: plugin load '(null)' returned error (11 : (null)), using default tuner instead.
6a9ab017bb44:454:461 [0] NCCL INFO comm 0x557b4c553c80 rank 0 nranks 1 cudaDev 0 nvmlDev 0 busId d8000 commId 0x428d7c9b55223c50 - Init COMPLETE
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
a4df80236412:808:815 [0] NCCL INFO Tuner: plugin load '(null)' returned error (11 : (null)), using default tuner instead.
a4df80236412:808:815 [0] NCCL INFO comm 0x559370ea1e30 rank 0 nranks 1 cudaDev 0 nvmlDev 0 busId d8000 commId 0x401fd347a370a800 - Init COMPLETE
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
     4194304       1048576     float     sum      -1    84.15   49.85    0.00      0     0.28  15033.35    0.00      0
     4194304       1048576     float     sum      -1    238.6   17.58    0.00      0     0.28  14974.31    0.00      0
6a9ab017bb44:454:454 [0] NCCL INFO comm 0x557b4c553c80 rank 0 nranks 1 cudaDev 0 busId d8000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 0
#

a4df80236412:808:808 [0] NCCL INFO comm 0x559370ea1e30 rank 0 nranks 1 cudaDev 0 busId d8000 - Destroy COMPLETE
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 0
```

**Things done/Verified**
1. GPU Can time share within multiple docker on same host.
2.tested perftest (client /server ) on each docker they are able to communicate

**Question**
1.is it feasible to run nccl-tests with different ranks inside dockers on same host.
2.Whats needs to be done?

## 评论 (1)

### alokprasad-mrvl · 2025-07-01

Dumping Topo on both docker yields same output , can this be the reason having same rank

```
<system version="1">
  <cpu numaid="1" affinity="aaaa,aaaaaaaa" arch="x86_64" vendor="GenuineIntel" familyid="6" modelid="85">
    <pci busid="0000:af:00.0" class="0x020000" vendor="0x15b3" device="0x1019" subsystem_vendor="0x15b3" subsystem_device="0x0008" link_speed="8.0 GT/s PCIe" link_width="16">
      <nic>
        <net name="roce0" dev="0" speed="100000" port="1" latency="0.000000" guid="0xe6fb480003f6ceb8" maxconn="262144" gdr="0"/>
      </nic>
    </pci>
    <pci busid="0000:d8:00.0" class="0x030000" vendor="0x10de" device="0x1fb1" subsystem_vendor="0x10de" subsystem_device="0x1488" link_speed="8.0 GT/s PCIe" link_width="16">
      <gpu dev="0" sm="75" rank="0" gdr="1"/>
    </pci>
  </cpu>
</system>
```
