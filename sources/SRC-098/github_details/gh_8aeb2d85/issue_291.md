# [Issue #291] NCCL alltoall_perf errors with 5090

source: https://github.com/NVIDIA/nccl-tests/issues/291
state: closed | updated: 2025-03-19T02:29:27Z
labels: bug, duplicate, fixed

## 正文

#287 
when i change nccl code with device.h "return cudaArch >= 800 ? (cudaArch == 1200 ? 6 : 8) : 4;" i can run all_reduce_perf，bug alltoall_perf has error
```
root@node:~/nccl-tests/build#_ NCCL_DEBUG=INFO ./alltoall_perf
#nThread 1 nGpus 1 minBytes 33554432 maxBytes 33554432 step: 1048576(bytes) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#Using devices
#Rank 0 Group 0 Pid 12225 on node device 0 [0000:16:00] NVIDIA GeForce RTX 5090
node:12225:12225 [0] NCCL INFO Bootstrap: Using ens49f1np1:192.168.30.122<0>
node:12225:12225 [0] NCCL INFO cudaDriverVersion 12080
node:12225:12225 [0] NCCL INFO NCCL version 2.25.1+cuda12.4
node:12225:12255 [0] NCCL INFO NET/Plugin: Could not find: libnccl-net.so. Using internal network plugin.
node:12225:12255 [0] NCCL INFO Failed to open libibverbs.so[.1]
node:12225:12255 [0] NCCL INFO NET/Socket : Using [0]ens49f1np1:192.168.30.122<0>
node:12225:12255 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
node:12225:12255 [0] NCCL INFO Using network Socket
node:12225:12255 [0] NCCL INFO ncclCommInitAll comm 0x55cc27005c20 rank 0 nranks 1 cudaDev 0 nvmlDev 0 busId 16000 commId 0x1c3170e2c1182784 - Init START
node:12225:12255 [0] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
node:12225:12255 [0] NCCL INFO Bootstrap timings total 0.000633 (create 0.000024, send 0.000092, recv 0.000286, ring 0.000001, delay 0.000000)
node:12225:12255 [0] NCCL INFO Setting affinity for GPU 0 to ffff,ffffffff,00000000,0000ffff,ffffffff
node:12225:12255 [0] NCCL INFO comm 0x55cc27005c20 rank 0 nRanks 1 nNodes 1 localRanks 1 localRank 0 MNNVL 0
node:12225:12255 [0] NCCL INFO Channel 00/64 : 0
node:12225:12255 [0] NCCL INFO Channel 01/64 : 0
node:12225:12255 [0] NCCL INFO Channel 02/64 : 0
node:12225:12255 [0] NCCL INFO Channel 03/64 : 0
node:12225:12255 [0] NCCL INFO Channel 04/64 : 0
node:12225:12255 [0] NCCL INFO Channel 05/64 : 0
node:12225:12255 [0] NCCL INFO Channel 06/64 : 0
node:12225:12255 [0] NCCL INFO Channel 07/64 : 0
node:12225:12255 [0] NCCL INFO Channel 08/64 : 0
node:12225:12255 [0] NCCL INFO Channel 09/64 : 0
node:12225:12255 [0] NCCL INFO Channel 10/64 : 0
node:12225:12255 [0] NCCL INFO Channel 11/64 : 0
node:12225:12255 [0] NCCL INFO Channel 12/64 : 0
node:12225:12255 [0] NCCL INFO Channel 13/64 : 0
node:12225:12255 [0] NCCL INFO Channel 14/64 : 0
node:12225:12255 [0] NCCL INFO Channel 15/64 : 0
node:12225:12255 [0] NCCL INFO Channel 16/64 : 0
node:12225:12255 [0] NCCL INFO Channel 17/64 : 0
node:12225:12255 [0] NCCL INFO Channel 18/64 : 0
node:12225:12255 [0] NCCL INFO Channel 19/64 : 0
node:12225:12255 [0] NCCL INFO Channel 20/64 : 0
node:12225:12255 [0] NCCL INFO Channel 21/64 : 0
node:12225:12255 [0] NCCL INFO Channel 22/64 : 0
node:12225:12255 [0] NCCL INFO Channel 23/64 : 0
node:12225:12255 [0] NCCL INFO Channel 24/64 : 0
node:12225:12255 [0] NCCL INFO Channel 25/64 : 0
node:12225:12255 [0] NCCL INFO Channel 26/64 : 0
node:12225:12255 [0] NCCL INFO Channel 27/64 : 0
node:12225:12255 [0] NCCL INFO Channel 28/64 : 0
node:12225:12255 [0] NCCL INFO Channel 29/64 : 0
node:12225:12255 [0] NCCL INFO Channel 30/64 : 0
node:12225:12255 [0] NCCL INFO Channel 31/64 : 0
node:12225:12255 [0] NCCL INFO Channel 32/64 : 0
node:12225:12255 [0] NCCL INFO Channel 33/64 : 0
node:12225:12255 [0] NCCL INFO Channel 34/64 : 0
node:12225:12255 [0] NCCL INFO Channel 35/64 : 0
node:12225:12255 [0] NCCL INFO Channel 36/64 : 0
node:12225:12255 [0] NCCL INFO Channel 37/64 : 0
node:12225:12255 [0] NCCL INFO Channel 38/64 : 0
node:12225:12255 [0] NCCL INFO Channel 39/64 : 0
node:12225:12255 [0] NCCL INFO Channel 40/64 : 0
node:12225:12255 [0] NCCL INFO Channel 41/64 : 0
node:12225:12255 [0] NCCL INFO Channel 42/64 : 0
node:12225:12255 [0] NCCL INFO Channel 43/64 : 0
node:12225:12255 [0] NCCL INFO Channel 44/64 : 0
node:12225:12255 [0] NCCL INFO Channel 45/64 : 0
node:12225:12255 [0] NCCL INFO Channel 46/64 : 0
node:12225:12255 [0] NCCL INFO Channel 47/64 : 0
node:12225:12255 [0] NCCL INFO Channel 48/64 : 0
node:12225:12255 [0] NCCL INFO Channel 49/64 : 0
node:12225:12255 [0] NCCL INFO Channel 50/64 : 0
node:12225:12255 [0] NCCL INFO Channel 51/64 : 0
node:12225:12255 [0] NCCL INFO Channel 52/64 : 0
node:12225:12255 [0] NCCL INFO Channel 53/64 : 0
node:12225:12255 [0] NCCL INFO Channel 54/64 : 0
node:12225:12255 [0] NCCL INFO Channel 55/64 : 0
node:12225:12255 [0] NCCL INFO Channel 56/64 : 0
node:12225:12255 [0] NCCL INFO Channel 57/64 : 0
node:12225:12255 [0] NCCL INFO Channel 58/64 : 0
node:12225:12255 [0] NCCL INFO Channel 59/64 : 0
node:12225:12255 [0] NCCL INFO Channel 60/64 : 0
node:12225:12255 [0] NCCL INFO Channel 61/64 : 0
node:12225:12255 [0] NCCL INFO Channel 62/64 : 0
node:12225:12255 [0] NCCL INFO Channel 63/64 : 0
node:12225:12255 [0] NCCL INFO Trees [0] -1/-1/-1->0->-1 [1] -1/-1/-1->0->-1 [2] -1/-1/-1->0->-1 [3] -1/-1/-1->0->-1 [4] -1/-1/-1->0->-1 [5] -1/-1/-1->0->-1 [6] -1/-1/-1->0->-1 [7] -1/-1/-1->0->-1 [8] -1/-1/-1->0->-1 [9] -1/-1/-1->0->-1 [10] -1/-1/-1->0->-1 [11] -1/-1/-1->0->-1 [12] -1/-1/-1->0->-1 [13] -1/-1/-1->0->-1 [14] -1/-1/-1->0->-1 [15] -1/-1/-1->0->-1 [16] -1/-1/-1->0->-1 [17] -1/-1/-1->0->-1 [18] -1/-1/-1->0->-1 [19] -1/-1/-1->0->-1 [20] -1/-1/-1->0->-1 [21] -1/-1/-1->0->-1 [22] -1/-1/-1->0->-1 [23] -1/-1/-1->0->-1 [24] -1/-1/-1->0->-1 [25] -1/-1/-1->0->-1 [26] -1/-1/-1->0->-1 [27] -1/-1/-1->0->-1 [28] -1/-1/-1->0->-1 [29] -1/-1/-1->0->-1 [30] -1/-1/-1->0->-1 [31] -1/-1/-1->0->-1 [32] -1/-1/-1->0->-1 [33] -1/-1/-1->0->-1 [34] -1/-1/-1->0->-1 [35] -1/-1/-1->0->-1 [36] -1/-1/-1->0->-1 [37] -1/-1/-1->0->-1 [38] -1/-1/-1->0->-1 [39] -1/-1/-1->0->-1 [40] -1/-1/-1->0->-1 [41] -1/-1/-1->0->-1 [42] -1/-1/-1->0->-1 [43] -1/-1/-1->0->-1 [44] -1/-1/-1->0->-1 [45] -1/-1/-1->0->-1 [46] -1/-1/-1->0->-1 [4
node:12225:12255 [0] NCCL INFO P2P Chunksize set to 524288
node:12225:12255 [0] NCCL INFO Check P2P Type intraNodeP2pSupport 0 directMode 0
node:12225:12259 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 2
node:12225:12258 [0] NCCL INFO [Proxy Service] Device 0 CPU core 1
node:12225:12255 [0] NCCL INFO 64 coll channels, 64 collnet channels, 0 nvls channels, 64 p2p channels, 64 p2p channels per peer
node:12225:12255 [0] NCCL INFO CC Off, workFifoBytes 1048576
node:12225:12255 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so libnccl-net.so. Using internal tuner plugin.
node:12225:12255 [0] NCCL INFO ncclCommInitAll comm 0x55cc27005c20 rank 0 nranks 1 cudaDev 0 nvmlDev 0 busId 16000 commId 0x1c3170e2c1182784 - Init COMPLETE
node:12225:12255 [0] NCCL INFO Init timings - ncclCommInitAll: rank 0 nranks 1 total 35.59 (kernels 35.48, alloc 0.08, bootstrap 0.00, allgathers 0.00, topo 0.00, graphs 0.00, connections 0.02, rest 0.00)
#out-of-place in-place
#size count type redop root time algbw busbw #wrong time algbw busbw #wrong
#(B) (elements) (us) (GB/s) (GB/s) (us) (GB/s) (GB/s)
node: Test CUDA failure common.cu:297 'an illegal memory access was encountered'
.. node pid 12225: Test failure common.cu:407
.. node pid 12225: Test failure common.cu:594
.. node pid 12225: Test failure alltoall.cu:97
.. node pid 12225: Test failure common.cu:625
.. node pid 12225: Test failure common.cu:1123
.. node pid 12225: Test failure common.cu:893
```

## 评论 (3)

### kiskra-nvidia · 2025-03-13

NCCL 2.26.2 has been released -- could you let us know if it works better on 5090s for you?

### yangxin120704 · 2025-03-19

> NCCL 2.26.2 has been released -- could you let us know if it works better on 5090s for you?

yes, it work fine now

### kiskra-nvidia · 2025-03-19

Thanks for confirming -- closing this bug.
