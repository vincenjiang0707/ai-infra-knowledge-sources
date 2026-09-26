# [Issue #1781] Problems with using NVLink across Kubernetes Pods on a same node

source: https://github.com/NVIDIA/nccl/issues/1781
state: open | updated: 2026-08-13T01:01:50Z
labels: 

## 正文

When deploying a LLM inference system on a Kubernetes cluster using the PD disaggregation framework (e.g., Dynamo). The efficiency of this transport between Prefill Pod and Decode Pod impacts the throughput of the inference system. Therefore, **I want that NVlink can be utilized in data transport between different pods located on the same node.** 

However, I found that **even when scheduling both Pods onto the same node, NVLink couldn't be utilized for data transport between Pods, and only RDMA or TCP was available**. Consequently, I conducted some experiments with NCCL:

- Environment
   - Nccl version: 2.27.5
   - Driver Version: 535.161.07
   - CUDA Version: 12.8
   - Node info: 8 * H20 with nvlink full connectivity
  
I conducted NCCL tests using MPIJob, where Rank0 and Rank1 are run in two separate Pods on a a same node, each allocated with one GPU resource.
```
mpirun \
  --allow-run-as-root -x CUDA_VISIBLE_DEVICES=0,1 -x NCCL_DEBUG=TRACE -x PATH -np 1 --host 10.131.x.x /opt/nccl-tests/build/all_reduce_perf -b 8 -e 2G -f 2 -g 1 -t 1 -a 2 -n 50 : \
  --allow-run-as-root -x CUDA_VISIBLE_DEVICES=2,3 -x NCCL_DEBUG=TRACE -x PATH -np 1 --host 10.131.x.x /opt/nccl-tests/build/all_reduce_perf -b 8 -e 2G -f 2 -g 1 -t 1 -a 2 -n 50
```

Get the following output：
```
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO ncclCommInitRank comm 0x5626a6a1a1a0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 8000 commId 0xe4b8e65544d3f326 - Init START
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO ncclCommInitRank comm 0x5588c7079580 rank 1 nranks 2 cudaDev 0 nvmlDev 2 busId a2000 commId 0xe4b8e65544d3f326 - Init START
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO RAS client listening socket at ::1<28028>
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO RAS client listening socket at ::1<28028>
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO Bootstrap timings total 0.001420 (create 0.000022, send 0.000367, recv 0.000465, ring 0.000138, delay 0.000000)
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO Bootstrap timings total 0.154328 (create 0.000019, send 0.000072, recv 0.153307, ring 0.000140, delay 0.000000)
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO Setting affinity for GPU 2 to 01,00000000,00000000,00000001
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO Setting affinity for GPU 0 to 01,00000000,00000000,00000001
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO comm 0x5588c7079580 rank 1 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] 0/-1/-1->1->-1
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO P2P Chunksize set to 131072
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO comm 0x5626a6a1a1a0 rank 0 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO Channel 00/02 : 0 1
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO Channel 01/02 : 0 1
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO P2P Chunksize set to 131072
nccl-tests-gdr-2-worker-1:225:234 [0] NCCL INFO [Proxy Service] Device 0 CPU core 0
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO Check P2P Type intraNodeP2pSupport 0 directMode 0
nccl-tests-gdr-2-worker-0:298:308 [0] NCCL INFO [Proxy Service] Device 0 CPU core 0
nccl-tests-gdr-2-worker-0:298:309 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 0
nccl-tests-gdr-2-worker-1:225:235 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 0
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO CC Off, workFifoBytes 1048576
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO TUNER/Plugin: Using tuner plugin NCCLNET-TUNER
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO TUNER/Plugin: Using tuner plugin NCCLNET-TUNER
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO ncclCommInitRank comm 0x5588c7079580 rank 1 nranks 2 cudaDev 0 nvmlDev 2 busId a2000 commId 0xe4b8e65544d3f326 - Init COMPLETE
nccl-tests-gdr-2-worker-1:225:232 [0] NCCL INFO Init timings - ncclCommInitRank: rank 1 nranks 2 total 0.47 (kernels 0.14, alloc 0.26, bootstrap 0.00, allgathers 0.00, topo 0.06, graphs 0.00, connections 0.00, rest 0.00)
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO ncclCommInitRank comm 0x5626a6a1a1a0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 8000 commId 0xe4b8e65544d3f326 - Init COMPLETE
nccl-tests-gdr-2-worker-0:298:306 [0] NCCL INFO Init timings - ncclCommInitRank: rank 0 nranks 2 total 0.61 (kernels 0.14, alloc 0.26, bootstrap 0.15, allgathers 0.00, topo 0.06, graphs 0.00, connections 0.00, rest 0.00)
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
nccl-tests-gdr-2-worker-0:298:311 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 0
nccl-tests-gdr-2-worker-1:225:236 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[2] [receive] via NET/Socket/0
nccl-tests-gdr-2-worker-1:225:236 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[2] [receive] via NET/Socket/0
nccl-tests-gdr-2-worker-1:225:236 [0] NCCL INFO Channel 00/0 : 1[2] -> 0[0] [send] via NET/Socket/0
nccl-tests-gdr-2-worker-1:225:236 [0] NCCL INFO Channel 01/0 : 1[2] -> 0[0] [send] via NET/Socket/0
nccl-tests-gdr-2-worker-1:225:237 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 96
nccl-tests-gdr-2-worker-0:298:310 [0] NCCL INFO Channel 00/0 : 1[2] -> 0[0] [receive] via NET/Socket/0
nccl-tests-gdr-2-worker-0:298:310 [0] NCCL INFO Channel 01/0 : 1[2] -> 0[0] [receive] via NET/Socket/0
nccl-tests-gdr-2-worker-0:298:310 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[2] [send] via NET/Socket/0
nccl-tests-gdr-2-worker-0:298:310 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[2] [send] via NET/Socket/0
```

**Data transport between ranks across Pods on the same node can only utilize Net/Socket/0.** 


After some code review, I discovered that NCCL uses the [canConnect](https://github.com/NVIDIA/nccl/blob/master/src/transport.cc#L14-L42) method from the transport to sequentially determine whether to use `P2P,` `SHM`, or `NET` for transmission.  

In the implement of `p2pTransport`, it requires checking the **HostHash**, **SHM device**, and **GPU topology** to determine if two ranks can perform P2P connections. [link to ncclTopoCheckP2p](https://github.com/NVIDIA/nccl/blob/master/src/graph/paths.cc#L269)

NCCL also provides an ENV option `NCCL_HOSTID` to override the HostHash. [link to getHostHash](https://github.com/NVIDIA/nccl/blob/master/src/misc/utils.cc#L78)

 Based on these findings, I modified the nccl-test script as following to ensure that the `HostHash` of ranks within the two Pods is identical.

```
mpirun \
  --allow-run-as-root -x NCCL_HOSTID=0.0.0.0 -x CUDA_VISIBLE_DEVICES=0,1 -x NCCL_DEBUG=TRACE -x PATH -np 1 --host 10.131.x.x /opt/nccl-tests/build/all_reduce_perf -b 8 -e 2G -f 2 -g 1 -t 1 -a 2 -n 50 : \
  --allow-run-as-root -x NCCL_HOSTID=0.0.0.0 -x CUDA_VISIBLE_DEVICES=2,3 -x NCCL_DEBUG=TRACE -x PATH -np 1 --host 10.131.x.x /opt/nccl-tests/build/all_reduce_perf -b 8 -e 2G -f 2 -g 1 -t 1 -a 2 -n 50
```

Then I reran the NCCL test and found that the communication link between the ranks resulted in the following output.

```
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO ncclCommInitRank comm 0x562262701920 rank 1 nranks 2 cudaDev 0 nvmlDev 2 busId a2000 commId 0x9eddd89fcffb8f13 - Init START
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO ncclCommInitRank comm 0x562934d19e90 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 8000 commId 0x9eddd89fcffb8f13 - Init START
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO NCCL_HOSTID set by environment to 10.10.10.10
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO NCCL_HOSTID set by environment to 10.10.10.10
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO RAS client listening socket at ::1<28028>
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO RAS client listening socket at ::1<28028>
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Bootstrap timings total 0.007173 (create 0.000023, send 0.000126, recv 0.006511, ring 0.000053, delay 0.000000)
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO Bootstrap timings total 0.082206 (create 0.000030, send 0.000259, recv 0.081437, ring 0.000055, delay 0.000001)
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO Setting affinity for GPU 2 to 0,96
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Setting affinity for GPU 0 to 0,96
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO comm 0x562262701920 rank 1 nRanks 2 nNodes 1 localRanks 2 localRank 1 MNNVL 0
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0 [2] -1/-1/-1->1->0 [3] -1/-1/-1->1->0 [4] -1/-1/-1->1->0 [5] -1/-1/-1->1->0 [6] 0/-1/-1->1->-1 [7] 0/-1/-1->1->-1 [8] 0/-1/-1->1->-1 [9] 0/-1/-1->1->-1 [10] 0/-1/-1->1->-1 [11] 0/-1/-1->1->-1 [12] -1/-1/-1->1->0 [13] -1/-1/-1->1->0 [14] -1/-1/-1->1->0 [15] -1/-1/-1->1->0 [16] -1/-1/-1->1->0 [17] -1/-1/-1->1->0 [18] 0/-1/-1->1->-1 [19] 0/-1/-1->1->-1 [20] 0/-1/-1->1->-1 [21] 0/-1/-1->1->-1 [22] 0/-1/-1->1->-1 [23] 0/-1/-1->1->-1
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO P2P Chunksize set to 524288
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO comm 0x562934d19e90 rank 0 nRanks 2 nNodes 1 localRanks 2 localRank 0 MNNVL 0
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 00/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 01/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 02/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 03/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 04/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 05/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 06/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 07/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 08/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 09/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 10/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 11/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 12/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 13/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 14/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 15/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 16/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 17/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 18/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 19/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 20/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 21/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 22/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Channel 23/24 : 0 1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1 [2] 1/-1/-1->0->-1 [3] 1/-1/-1->0->-1 [4] 1/-1/-1->0->-1 [5] 1/-1/-1->0->-1 [6] -1/-1/-1->0->1 [7] -1/-1/-1->0->1 [8] -1/-1/-1->0->1 [9] -1/-1/-1->0->1 [10] -1/-1/-1->0->1 [11] -1/-1/-1->0->1 [12] 1/-1/-1->0->-1 [13] 1/-1/-1->0->-1 [14] 1/-1/-1->0->-1 [15] 1/-1/-1->0->-1 [16] 1/-1/-1->0->-1 [17] 1/-1/-1->0->-1 [18] -1/-1/-1->0->1 [19] -1/-1/-1->0->1 [20] -1/-1/-1->0->1 [21] -1/-1/-1->0->1 [22] -1/-1/-1->0->1 [23] -1/-1/-1->0->1
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO P2P Chunksize set to 524288
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Check P2P Type isAllDirectP2p 1 directMode 0
nccl-tests-gdr-2-worker-1:1960519:1960659 [0] NCCL INFO [Proxy Service] Device 0 CPU core 96
nccl-tests-gdr-2-worker-0:1960518:1960661 [0] NCCL INFO [Proxy Service] Device 0 CPU core 0
nccl-tests-gdr-2-worker-1:1960519:1960660 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 96
nccl-tests-gdr-2-worker-0:1960518:1960662 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 0
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO 24 coll channels, 24 collnet channels, 0 nvls channels, 32 p2p channels, 32 p2p channels per peer
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO 24 coll channels, 24 collnet channels, 0 nvls channels, 32 p2p channels, 32 p2p channels per peer
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO CC Off, workFifoBytes 1048576
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO TUNER/Plugin: Using tuner plugin NCCLNET-TUNER
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO ncclCommInitRank comm 0x562934d19e90 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 8000 commId 0x9eddd89fcffb8f13 - Init COMPLETE
nccl-tests-gdr-2-worker-1:1960519:1960630 [0] NCCL INFO Init timings - ncclCommInitRank: rank 0 nranks 2 total 0.91 (kernels 0.20, alloc 0.55, bootstrap 0.01, allgathers 0.00, topo 0.13, graphs 0.00, connections 0.01, rest 0.01)
#
#                                                              out-of-place                       in-place
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO TUNER/Plugin: Using tuner plugin NCCLNET-TUNER
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO ncclCommInitRank comm 0x562262701920 rank 1 nranks 2 cudaDev 0 nvmlDev 2 busId a2000 commId 0x9eddd89fcffb8f13 - Init COMPLETE
nccl-tests-gdr-2-worker-0:1960518:1960631 [0] NCCL INFO Init timings - ncclCommInitRank: rank 1 nranks 2 total 0.89 (kernels 0.21, alloc 0.45, bootstrap 0.08, allgathers 0.00, topo 0.13, graphs 0.00, connections 0.01, rest 0.01)
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 00/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 01/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 02/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 03/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 04/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 05/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 06/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 02/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 07/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 03/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 08/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 04/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 09/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 05/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 10/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 06/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 11/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 07/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 12/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 13/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 08/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 14/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 09/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 15/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 10/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 11/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 16/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 12/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 17/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 13/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 18/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 19/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 14/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 20/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 15/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 21/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 16/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 22/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 17/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-0:1960518:1960664 [0] NCCL INFO Channel 23/0 : 1[2] -> 0[0] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[2] via P2P/CUMEM
nccl-tests-gdr-2-worker-1:1960519:1960663 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[2] via P2P/CUMEM
```
**Data transport between ranks in different Pods on the same node used `P2P/CUMEM` instead of `P2P/direct pointer`.**

The monitoring data of the GPU also indicates that there is no traffic through NVLink.

<img width="1610" height="614" alt="Image" src="https://github.com/user-attachments/assets/4d8a496c-7800-4664-8925-a76e781d08d5" />

Upon further investigation of the code, I found that during the [P2PSendSetup](https://github.com/NVIDIA/nccl/blob/master/src/transport/p2p.cc#L382-L402)/[P2PRecvSetup](https://github.com/NVIDIA/nccl/blob/master/src/transport/p2p.cc#L450-L465) , NCCL also checks the `PidHash` [link to P2P_SAME_PID define](https://github.com/NVIDIA/nccl/blob/master/src/transport/p2p.cc#L311) and `HostHash` of the two ranks. Previously, to pass the `p2pTransport.canConnect` verification, we set the environment variable `NCCL_HOSTID` to keep the `HostHash` of the two ranks consistent, but the PIDs for the ranks in different Pods are certainly different. Due to this limitation, data transport between Pods cannot use the `P2P/direct point`, but instead falls back to `P2P/CUMEM` or `P2P/IPC`.

For the further verification, I hardcoded the logic here to remove the consistency check of ranks' PID and retested and got following result:

```
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO ncclCommInitRank comm 0x5640d64f3f00 rank 1 nranks 2 cudaDev 0 nvmlDev 2 busId a2000 commId 0x8c5c91a36567f54a - Init START
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO ncclCommInitRank comm 0x558cd55c7760 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 8000 commId 0x8c5c91a36567f54a - Init START
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO NCCL_HOSTID set by environment to 10.10.10.10
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO NCCL_HOSTID set by environment to 10.10.10.10
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO RAS client listening socket at ::1<28028>
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO RAS client listening socket at ::1<28028>
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO UDS: Creating socket /tmp/nccl-socket-0-840b4f60b1dfa869
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO UDS: Creating socket /tmp/nccl-socket-1-ef1f1062e0c09dd6
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Bootstrap timings total 0.005420 (create 0.000020, send 0.004386, recv 0.000328, ring 0.000311, delay 0.000000)
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO NCCL_CUMEM_ENABLE set by environment to 0.
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Bootstrap timings total 0.025106 (create 0.000028, send 0.000149, recv 0.024173, ring 0.000033, delay 0.000000)
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO NCCL_CUMEM_ENABLE set by environment to 0.
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to NVL
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO NCCL_P2P_LEVEL set by environment to NVL
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Setting affinity for GPU 2 to 0,96
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Setting affinity for GPU 0 to 0,96
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO comm 0x5640d64f3f00 rank 1 nRanks 2 nNodes 1 localRanks 2 localRank 1 MNNVL 0
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO comm 0x558cd55c7760 rank 0 nRanks 2 nNodes 1 localRanks 2 localRank 0 MNNVL 0
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0 [2] -1/-1/-1->1->0 [3] -1/-1/-1->1->0 [4] -1/-1/-1->1->0 [5] -1/-1/-1->1->0 [6] 0/-1/-1->1->-1 [7] 0/-1/-1->1->-1 [8] 0/-1/-1->1->-1 [9] 0/-1/-1->1->-1 [10] 0/-1/-1->1->-1 [11] 0/-1/-1->1->-1 [12] -1/-1/-1->1->0 [13] -1/-1/-1->1->0 [14] -1/-1/-1->1->0 [15] -1/-1/-1->1->0 [16] -1/-1/-1->1->0 [17] -1/-1/-1->1->0 [18] 0/-1/-1->1->-1 [19] 0/-1/-1->1->-1 [20] 0/-1/-1->1->-1 [21] 0/-1/-1->1->-1 [22] 0/-1/-1->1->-1 [23] 0/-1/-1->1->-1
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO P2P Chunksize set to 524288
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 00/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 01/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 02/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 03/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 04/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 05/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 06/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 07/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 08/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 09/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 10/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 11/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 12/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 13/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 14/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 15/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 16/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 17/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 18/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 19/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 20/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 21/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 22/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 23/24 : 0 1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1 [2] 1/-1/-1->0->-1 [3] 1/-1/-1->0->-1 [4] 1/-1/-1->0->-1 [5] 1/-1/-1->0->-1 [6] -1/-1/-1->0->1 [7] -1/-1/-1->0->1 [8] -1/-1/-1->0->1 [9] -1/-1/-1->0->1 [10] -1/-1/-1->0->1 [11] -1/-1/-1->0->1 [12] 1/-1/-1->0->-1 [13] 1/-1/-1->0->-1 [14] 1/-1/-1->0->-1 [15] 1/-1/-1->0->-1 [16] 1/-1/-1->0->-1 [17] 1/-1/-1->0->-1 [18] -1/-1/-1->0->1 [19] -1/-1/-1->0->1 [20] -1/-1/-1->0->1 [21] -1/-1/-1->0->1 [22] -1/-1/-1->0->1 [23] -1/-1/-1->0->1
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO P2P Chunksize set to 524288
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Check P2P Type isAllDirectP2p 1 directMode 0
nccl-tests-gdr-1-worker-1:990668:990800 [0] NCCL INFO [Proxy Service] Device 0 CPU core 96
nccl-tests-gdr-1-worker-0:990669:990798 [0] NCCL INFO [Proxy Service] Device 0 CPU core 96
nccl-tests-gdr-1-worker-0:990669:990799 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 96
nccl-tests-gdr-1-worker-1:990668:990801 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 96
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 00/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 01/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 02/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 03/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 04/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 05/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 06/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 07/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 08/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 09/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 10/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 11/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 12/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 13/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 14/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 15/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 16/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 17/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 18/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 19/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 20/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 21/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 22/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-0:990669:990750 [0] NCCL INFO Channel 23/0 : 0[0] -> 1[2] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 00/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 01/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 02/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 03/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 04/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 05/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 06/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 07/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 08/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 09/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 10/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 11/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 12/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 13/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 14/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 15/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 16/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 17/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 18/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 19/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 20/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 21/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 22/0 : 1[2] -> 0[0] via P2P/direct pointer
nccl-tests-gdr-1-worker-1:990668:990751 [0] NCCL INFO Channel 23/0 : 1[2] -> 0[0] via P2P/direct pointer
```

**data transport between Pods on a same node finally utilized NVLink, which is confirmed through the GPU's NVLink monitoring data.**

<img width="1594" height="608" alt="Image" src="https://github.com/user-attachments/assets/4d560598-7e0e-49a4-bfdf-8377e28b1aa8" />

There are two questions:
- What are the differences between `P2P/DirectPoint, P2P/CUMEM, P2P/IPC` in P2P communication?
- Why do we require the `PidHash` to be the same for utilizing P2P/DirectPoint transport? Is this validation still applicable in the context of Kubernetes Pods? Could we provide an environment variable similar to `NVIDIA_HOSTID` to support overriding this requirement in Kubernetes Pod scenarios?



## 评论 (13)

### Wahid612 · 2025-07-17

Hi @Syspretor,
Have you tried injecting your topology to NCCL when running with Kubernetes? 

### Wahid612 · 2025-07-17

Please disregard my previous comment; after checking, here are some tentative answers.

> What are the differences between P2P/DirectPoint, P2P/CUMEM, P2P/IPC in P2P communication?

P2P/direct pointer refers to using the pointer between GPUs within the same process, P2P/IPC involves inter-process memory mapping via cudaIpc* functions, and P2P/CUMEM uses cuMem* functions for inter-process memory mapping; 
however, as far as I know, none of these methods allow NVLink communication between containers.

> Why do we require the PidHash to be the same for utilizing P2P/DirectPoint transport?

The two GPU communicator objects must be part of the same process for the pointer to be valid for the other rank, as this is simply how CUDA works.

> Is this validation still applicable in the context of Kubernetes Pods?

Yes, that still apply.

> Could we provide an environment variable similar to NVIDIA_HOSTID to support overriding this requirement in Kubernetes 

Pod scenarios?
That still would not work.





### cheyang · 2025-07-21

@Wahid612 Thank you for your response. Based on my understanding of [https://github.com/NVIDIA/nccl/pull/248#issuecomment-524081130](https://github.com/NVIDIA/nccl/pull/248#issuecomment-524081130), cross-container P2P support requires three conditions to be met:  
1. Processes share the same `boot_id` (indicating same host), or override via `NCCL_HOSTID`  
2. `/dev/shm` has identical `MAJOR:MINOR` device numbers (confirming shared IPC namespace)  
3. `cuDeviceCanAccessPeer()` verifies NVLink capability  

This functionality appears to have been implemented in NCCL 2.5.6, but we're observing it's no longer working consistently in recent versions. Could you help me understand:  
- Is this an intentional design change?  
- Or might this be an unexpected regression?  

The change is from [https://github.com/NVIDIA/nccl/blame/master/src/transport/p2p.cc#L311](https://github.com/NVIDIA/nccl/blame/master/src/transport/p2p.cc#L311)  which is introduced in 2024.

Specifically for Kubernetes Pod scenarios where we can enable shared IPC and PID namespaces, would it be possible to restore/maintain this cross-container P2P functionality? We believe this would be valuable for containerized HPC workloads.

### sjeaugey · 2025-07-21

I think there is an important aspect to consider: for this to work, you need each container to see all GPUs. IIRC it won't work if you only map a subset of GPUs in each container.

@cheyang in your experiments did each container see all GPUs?


### cheyang · 2025-07-21

> I think there is an important aspect to consider: for this to work, you need each container to see all GPUs. IIRC it won't work if you only map a subset of GPUs in each container.
> 
> [@cheyang](https://github.com/cheyang) in your experiments did each container see all GPUs?

Yes. In our experiment, each container can see all GPUs. 

### sjeaugey · 2025-07-21

Thanks for confirming. Can you try with NCCL_CUMEM_ENABLE=0 and see if it changes anything?

It could be that when we added CUMEM inter-process memory mappings, that use case got broken, but I don't know whether the legacy IPC path still works or was broken as well.

### Syspretor · 2025-07-23

> Thanks for confirming. Can you try with NCCL_CUMEM_ENABLE=0 and see if it changes anything?
> 
> It could be that when we added CUMEM inter-process memory mappings, that use case got broken, but I don't know whether the legacy IPC path still works or was broken as well.

@sjeaugey In our experiment, by setting the `NVIDIA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7` environment variable for the both two containers to allow each container to see all GPUs, we confirmed this using `nvidia topo -m` in two separate containers. We also verified that there is NVLINK connectivity between all GPU devices.

I also tried setting the environment variable `NCCL_CUMEM_ENABLE=0` in the NCCL test, and after configuring this, the transport method changed from **P2P/CUMEM** to **P2P/IPC**, as indicated by the logic in this code. 
https://github.com/NVIDIA/nccl/blob/master/src/transport/p2p.cc#L382-L402

When using P2P/IPC for transport, monitoring the GPU NVLink revealed that NVLink was also not being utilized.




### sjeaugey · 2025-07-23

Could it be that your setup is actually not checking the conditions?

Could you print the hostHash and pidHash of the different ranks and see why they differ?

### Syspretor · 2025-07-28

> Could it be that your setup is actually not checking the conditions?
> 
> Could you print the hostHash and pidHash of the different ranks and see why they differ?

@sjeaugey I attempted to add some logs within this conditional logic to confirm whether this condition was actually reached. As illustrated in the diagram below, the NCCL test topology I ran has rank 0 and rank 1 in one Pod's container, and rank 2 and rank 3 in another Pod's container.

<img width="786" height="578" alt="Image" src="https://github.com/user-attachments/assets/d6ef56d3-2e91-47c8-9ce2-1a48737cc37e" />

Through the logs, it was evident that when rank 1 attempted to transfer data to rank 2 across containers, it used **P2P/IPC** (due to the environment variable `NCCL_CUMEM_ENABLE=0` I set). Rank 1 and rank 2 had the same hostHash (because I set the same environment variables `NCCL_HOSTID=0`), **but different PidHashes**. In contrast, when rank 2 and rank 3 transferred data within the same container, **both the hostHash and PidHash were identical**, thus utilizing the P2P/GPU Direct transport method.

<img width="1758" height="708" alt="Image" src="https://github.com/user-attachments/assets/014261eb-f287-4d5b-912c-7989cace3ab6" />

Therefore, I can conclude that the PidHash of ranks in different containers is indeed different, and this discrepancy determines whether P2P/GPU Direct can be used for transport across containers.

### sjeaugey · 2025-07-28

@Syspretor my bad, I got confused. pidHashes being different is not a problem. It just means those are different processes hence we need to use inter-process mapping.

So if we don't use P2P it's either that host hashes differ or CUDA doesn't allow us to enable P2P between the two GPUs.

### Syspretor · 2025-07-29

> [@Syspretor](https://github.com/Syspretor) my bad, I got confused. pidHashes being different is not a problem. It just means those are different processes hence we need to use inter-process mapping.
> 
> So if we don't use P2P it's either that host hashes differ or CUDA doesn't allow us to enable P2P between the two GPUs.

@sjeaugey Maybe I think that PidHash affects the behavior of P2P. After **removing the PidHash check logic in the NCCL code through hardcoding**, the transport between ranks within the two Pods was able to use P2P, or NVLink. Therefore, in this scenario, CUDA already allows us to enable P2P between the two GPUs, but the PidHash check prevented this from happening.

If you need to reproduce the issue, I can provide a method using Docker to reproduce it, along with how I resolved it after hardcoding.

### sjeaugey · 2025-07-29

Removing the pidHash check will only lead to crashes or data corruption. You can't share data between processes by sharing a pointer, like you would do it within the same process.

### nataliekung · 2026-08-13

Independent data point from an RL fine-tuning setup (verl + FSDP + vLLM, GRPO) on 2x H200 on a single physical node, which lines up with @sjeaugey's "each container must see all GPUs" point.

**Config A - pod-per-rank (1 GPU visible per pod):** 2 training ranks, each in a separate Kubernetes pod scheduled onto the **same** node, each pod requesting **1 GPU** (so each container sees only its own GPU). The cross-rank NCCL debug log shows the P2P/NVLink path is not taken:
- `isAllDirectP2p 0`
- channels are established `via NET` using the AWS Libfabric provider (EFA), i.e. the network transport, not P2P/NVLink.

**Config B - single pod exposing both GPUs:** the same 2 ranks colocated in **one** pod that exposes **both** GPUs (single process/namespace, both GPUs visible). Measured with `nvidia-smi nvlink -gt d`: GPU0/GPU1 Link0 Tx and Rx each increment ~260 MiB over ~6 s of training -> NVLink actually carries traffic.

So in our measurements the deciding factor is exactly the GPU-visibility condition discussed above: with only 1 GPU visible per container, NCCL never takes the NVLink P2P path (it falls back to NET) even when both pods are on the same node; giving a single process/namespace visibility of all the GPUs restores NVLink.

Practical takeaway for containerized colocated/RL workloads: if two ranks must communicate over NVLink, place them in one pod that sees all the relevant GPUs rather than one-GPU-per-pod. One-GPU-per-pod on the same node will silently fall back to the network transport.

Versions: NCCL bundled with PyTorch 2.8 / CUDA 12.8, vLLM 0.11.0.

