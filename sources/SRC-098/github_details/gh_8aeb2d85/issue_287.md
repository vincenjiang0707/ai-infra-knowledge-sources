# [Issue #287] NCCL all_reduce_perf errors with 5090s

source: https://github.com/NVIDIA/nccl-tests/issues/287
state: closed | updated: 2025-03-15T05:36:16Z
labels: bug, fixed

## 正文

all_reduce_perf test errors when using dual 5090 GPUs. Works fine with one 5090.

Using nvidia driver 570.86.16

1x 5090;

```
user@GENOA-06:~/nccl-tests$ ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 1
# nThread 1 nGpus 1 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid   5092 on   GENOA-06 device  0 [0x21] NVIDIA GeForce RTX 5090
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
           8             2     float     sum      -1     5.63    0.00    0.00      0     0.20    0.04    0.00      0
          16             4     float     sum      -1     5.60    0.00    0.00      0     0.19    0.08    0.00      0
          32             8     float     sum      -1     5.30    0.01    0.00      0     0.18    0.17    0.00      0
          64            16     float     sum      -1     5.37    0.01    0.00      0     0.15    0.44    0.00      0
         128            32     float     sum      -1     4.61    0.03    0.00      0     0.15    0.86    0.00      0
         256            64     float     sum      -1     4.62    0.06    0.00      0     0.15    1.75    0.00      0
         512           128     float     sum      -1     4.59    0.11    0.00      0     0.15    3.46    0.00      0
        1024           256     float     sum      -1     4.60    0.22    0.00      0     0.14    7.09    0.00      0
        2048           512     float     sum      -1     6.21    0.33    0.00      0     0.15   14.03    0.00      0
        4096          1024     float     sum      -1     4.61    0.89    0.00      0     0.14   28.35    0.00      0
        8192          2048     float     sum      -1     4.57    1.79    0.00      0     0.15   56.30    0.00      0
       16384          4096     float     sum      -1     4.62    3.54    0.00      0     0.15  112.22    0.00      0
       32768          8192     float     sum      -1     4.57    7.18    0.00      0     0.15  219.18    0.00      0
       65536         16384     float     sum      -1     2.93   22.37    0.00      0     0.07  910.22    0.00      0
      131072         32768     float     sum      -1     2.91   45.07    0.00      0     0.07  1807.89    0.00      0
      262144         65536     float     sum      -1     2.95   88.98    0.00      0     0.09  2995.93    0.00      0
      524288        131072     float     sum      -1     3.10  169.24    0.00      0     0.08  6853.44    0.00      0
     1048576        262144     float     sum      -1     3.53  296.68    0.00      0     0.07  14563.56    0.00      0
     2097152        524288     float     sum      -1     3.64  576.23    0.00      0     0.07  28926.23    0.00      0
     4194304       1048576     float     sum      -1     5.30  791.69    0.00      0     0.09  48489.06    0.00      0
     8388608       2097152     float     sum      -1     9.83  853.29    0.00      0     0.08  109655.01    0.00      0
    16777216       4194304     float     sum      -1    19.44  863.04    0.00      0     0.07  226719.14    0.00      0
    33554432       8388608     float     sum      -1    41.36  811.21    0.00      0     0.07  453438.27    0.00      0
    67108864      16777216     float     sum      -1    85.69  783.15    0.00      0     0.08  818400.78    0.00      0
   134217728      33554432     float     sum      -1    175.6  764.34    0.00      0     0.08  1777718.25    0.00      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 0 
#
```

2x 5090s;

```
user@GENOA-06:~/nccl-tests$ NCCL_P2P_DISABLE=1 ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2
# nThread 1 nGpus 2 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid   5068 on   GENOA-06 device  0 [0x21] NVIDIA GeForce RTX 5090
#  Rank  1 Group  0 Pid   5068 on   GENOA-06 device  1 [0x61] NVIDIA GeForce RTX 5090
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
GENOA-06: Test NCCL failure common.cu:392 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. GENOA-06 pid 5068: Test failure common.cu:590
 .. GENOA-06 pid 5068: Test failure all_reduce.cu:90
 .. GENOA-06 pid 5068: Test failure common.cu:623
 .. GENOA-06 pid 5068: Test failure common.cu:1078
 .. GENOA-06 pid 5068: Test failure common.cu:891
```

2x 5090s with NCCL_DEBUG=INFO

```
user@GENOA-06:~/nccl-tests$ NCCL_DEBUG=INFO ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 2
# nThread 1 nGpus 2 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid   4766 on   GENOA-06 device  0 [0x21] NVIDIA GeForce RTX 5090
#  Rank  1 Group  0 Pid   4766 on   GENOA-06 device  1 [0x61] NVIDIA GeForce RTX 5090
GENOA-06:4766:4766 [0] NCCL INFO Bootstrap: Using enp227s0f0:192.168.1.250<0>
GENOA-06:4766:4766 [0] NCCL INFO cudaDriverVersion 12080
GENOA-06:4766:4766 [0] NCCL INFO NCCL version 2.25.1+cuda12.8
GENOA-06:4766:4780 [0] NCCL INFO ncclMaxSharedMem 82240 exceeds device/fn maxSharedMem 79856
GENOA-06:4766:4781 [1] NCCL INFO ncclMaxSharedMem 82240 exceeds device/fn maxSharedMem 79856
GENOA-06:4766:4780 [0] NCCL INFO NET/Plugin: Could not find: libnccl-net.so. Using internal network plugin.
GENOA-06:4766:4780 [0] NCCL INFO Failed to open libibverbs.so[.1]
GENOA-06:4766:4780 [0] NCCL INFO NET/Socket : Using [0]enp227s0f0:192.168.1.250<0> [1]enxfe1dc2e063ea:fe80::52b1:b1f3:51c0:ecca%enxfe1dc2e063ea<0>
GENOA-06:4766:4780 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so.
GENOA-06:4766:4780 [0] NCCL INFO Using network Socket
GENOA-06:4766:4781 [1] NCCL INFO Using network Socket
GENOA-06:4766:4781 [1] NCCL INFO ncclCommInitAll comm 0x639f4c7a4290 rank 1 nranks 2 cudaDev 1 nvmlDev 1 busId 61000 commId 0x726fb0d348b9154b - Init START
GENOA-06:4766:4780 [0] NCCL INFO ncclCommInitAll comm 0x639f4c724ac0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 21000 commId 0x726fb0d348b9154b - Init START
GENOA-06:4766:4781 [1] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
GENOA-06:4766:4781 [1] NCCL INFO Bootstrap timings total 0.001151 (create 0.000048, send 0.000163, recv 0.000423, ring 0.000026, delay 0.000000)
GENOA-06:4766:4780 [0] NCCL INFO Bootstrap timings total 0.001101 (create 0.000034, send 0.000134, recv 0.000570, ring 0.000023, delay 0.000000)
GENOA-06:4766:4781 [1] NCCL INFO Setting affinity for GPU 1 to 0fff,c0000000,00000000,00000000,0fffc000

GENOA-06:4766:4781 [1] graph/search.cc:1135 NCCL WARN Could not find a path for pattern 4, falling back to simple order

GENOA-06:4766:4781 [1] graph/search.cc:1135 NCCL WARN Could not find a path for pattern 1, falling back to simple order
GENOA-06:4766:4780 [0] NCCL INFO Setting affinity for GPU 0 to 03fff000,00000000,00000000,000003ff,f0000000

GENOA-06:4766:4780 [0] graph/search.cc:1135 NCCL WARN Could not find a path for pattern 4, falling back to simple order

GENOA-06:4766:4780 [0] graph/search.cc:1135 NCCL WARN Could not find a path for pattern 1, falling back to simple order
GENOA-06:4766:4780 [0] NCCL INFO comm 0x639f4c724ac0 rank 0 nRanks 2 nNodes 1 localRanks 2 localRank 0 MNNVL 0
GENOA-06:4766:4781 [1] NCCL INFO comm 0x639f4c7a4290 rank 1 nRanks 2 nNodes 1 localRanks 2 localRank 1 MNNVL 0
GENOA-06:4766:4780 [0] NCCL INFO Channel 00/02 : 0 1
GENOA-06:4766:4780 [0] NCCL INFO Channel 01/02 : 0 1
GENOA-06:4766:4781 [1] NCCL INFO Trees [0] -1/-1/-1->1->0 [1] -1/-1/-1->1->0
GENOA-06:4766:4781 [1] NCCL INFO P2P Chunksize set to 131072
GENOA-06:4766:4780 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] 1/-1/-1->0->-1
GENOA-06:4766:4780 [0] NCCL INFO P2P Chunksize set to 131072
GENOA-06:4766:4780 [0] NCCL INFO Check P2P Type intraNodeP2pSupport 0 directMode 1
GENOA-06:4766:4785 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 29
GENOA-06:4766:4783 [0] NCCL INFO [Proxy Service] Device 0 CPU core 149
GENOA-06:4766:4784 [1] NCCL INFO [Proxy Service] Device 1 CPU core 22
GENOA-06:4766:4786 [1] NCCL INFO [Proxy Service UDS] Device 1 CPU core 127
GENOA-06:4766:4780 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
GENOA-06:4766:4780 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
GENOA-06:4766:4781 [1] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
GENOA-06:4766:4781 [1] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 2 p2p channels per peer
GENOA-06:4766:4780 [0] NCCL INFO CC Off, workFifoBytes 1048576
GENOA-06:4766:4780 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so libnccl-net.so. Using internal tuner plugin.
GENOA-06:4766:4780 [0] NCCL INFO ncclCommInitAll comm 0x639f4c724ac0 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 21000 commId 0x726fb0d348b9154b - Init COMPLETE
GENOA-06:4766:4780 [0] NCCL INFO Init timings - ncclCommInitAll: rank 0 nranks 2 total 0.29 (kernels 0.26, alloc 0.02, bootstrap 0.00, allgathers 0.00, topo 0.01, graphs 0.00, connections 0.00, rest 0.00)
GENOA-06:4766:4781 [1] NCCL INFO ncclCommInitAll comm 0x639f4c7a4290 rank 1 nranks 2 cudaDev 1 nvmlDev 1 busId 61000 commId 0x726fb0d348b9154b - Init COMPLETE
GENOA-06:4766:4781 [1] NCCL INFO Init timings - ncclCommInitAll: rank 1 nranks 2 total 0.29 (kernels 0.26, alloc 0.02, bootstrap 0.00, allgathers 0.00, topo 0.01, graphs 0.00, connections 0.00, rest 0.00)
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
GENOA-06:4766:4787 [1] NCCL INFO Channel 00 : 1[1] -> 0[0] via SHM/direct/direct
GENOA-06:4766:4788 [0] NCCL INFO Channel 00 : 0[0] -> 1[1] via SHM/direct/direct
GENOA-06:4766:4787 [1] NCCL INFO Channel 01 : 1[1] -> 0[0] via SHM/direct/direct
GENOA-06:4766:4788 [0] NCCL INFO Channel 01 : 0[0] -> 1[1] via SHM/direct/direct
GENOA-06:4766:4787 [1] NCCL INFO Connected all rings, use ring PXN 0 GDR 1
GENOA-06:4766:4788 [0] NCCL INFO Connected all rings, use ring PXN 0 GDR 1

GENOA-06:4766:4766 [1] enqueue.cc:1500 NCCL WARN Cuda failure 1 'invalid argument'
GENOA-06:4766:4766 [1] NCCL INFO group.cc:242 -> 1
GENOA-06:4766:4766 [1] NCCL INFO group.cc:470 -> 1
GENOA-06:4766:4766 [1] NCCL INFO group.cc:573 -> 1
GENOA-06:4766:4766 [1] NCCL INFO group.cc:106 -> 1
GENOA-06: Test NCCL failure common.cu:392 'unhandled cuda error (run with NCCL_DEBUG=INFO for details) / '
 .. GENOA-06 pid 4766: Test failure common.cu:590
 .. GENOA-06 pid 4766: Test failure all_reduce.cu:90
 .. GENOA-06 pid 4766: Test failure common.cu:623
 .. GENOA-06 pid 4766: Test failure common.cu:1078
 .. GENOA-06 pid 4766: Test failure common.cu:891
```

I've also tried adding "NCCL_P2P_DISABLE=1" with the same results.



## 评论 (20)

### kiskra-nvidia · 2025-02-20

It looks to me like there is no P2P connectivity between the 2 GPUs. There should be... So, in a way, `NCCL_P2P_DISABLE=1` probably doesn't do anything because P2P is already disabled... Have you followed the steps outlined in https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting.html#gpu-direct? In particular, I recommend first running https://github.com/NVIDIA/cuda-samples/tree/master/Samples/5_Domain_Specific/p2pBandwidthLatencyTest.

### sjeaugey · 2025-02-20

GeForce cards do not support P2P.

The CUDA failure seems to happen when we launch the kernel.

I see this line in the log:
```
GENOA-06:4766:4780 [0] NCCL INFO ncclMaxSharedMem 82240 exceeds device/fn maxSharedMem 79856
```

Perhaps that's the reason for the launch error?

@RCS1 could you try to remove this line (line 488 of src/include/device.h):
https://github.com/NVIDIA/nccl/blob/master/src/include/device.h#L488
and see if it fixes the issue?

### RCS1 · 2025-02-20

Hi sjeaugey,

Thanks for your reply.

I'm unsure where that file would be located? That doesn't seem to be a directory I have.

### RCS1 · 2025-02-20

Results of p2pBandwidthLatencyTest

```
user@GENOA-05:~/cuda-samples/Samples/5_Domain_Specific/p2pBandwidthLatencyTest$ ./p2pBandwidthLatencyTest
[P2P (Peer-to-Peer) GPU Bandwidth Latency Test]
Device: 0, NVIDIA Graphics Device, pciBusID: 21, pciDeviceID: 0, pciDomainID:0
Device: 1, NVIDIA Graphics Device, pciBusID: 61, pciDeviceID: 0, pciDomainID:0
Device=0 CANNOT Access Peer Device=1
Device=1 CANNOT Access Peer Device=0

***NOTE: In case a device doesn't have P2P access to other one, it falls back to normal memcopy procedure.
So you can see lesser Bandwidth (GB/s) and unstable Latency (us) in those cases.

P2P Connectivity Matrix
     D\D     0     1
     0	     1     0
     1	     0     1
Unidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0      1 
     0 1516.99  38.24 
     1  38.92 1537.94 
Unidirectional P2P=Enabled Bandwidth (P2P Writes) Matrix (GB/s)
   D\D     0      1 
     0 1509.66  38.20 
     1  38.66 1536.43 
Bidirectional P2P=Disabled Bandwidth Matrix (GB/s)
   D\D     0      1 
     0 1528.05  43.03 
     1  42.78 1540.10 
Bidirectional P2P=Enabled Bandwidth Matrix (GB/s)
   D\D     0      1 
     0 1525.06  43.19 
     1  42.78 1539.36 
P2P=Disabled Latency Matrix (us)
   GPU     0      1 
     0   2.10  12.83 
     1  12.75   2.08 

   CPU     0      1 
     0   2.11   5.91 
     1   5.86   2.04 
P2P=Enabled Latency (P2P Writes) Matrix (us)
   GPU     0      1 
     0   2.09  12.76 
     1  12.87   2.08 

   CPU     0      1 
     0   2.13   5.67 
     1   5.64   2.20 

NOTE: The CUDA Samples are not meant for performance measurements. Results may vary when GPU Boost is enabled.
```

### RCS1 · 2025-02-20

Also to note;

Nvidia 570 (closed) drivers do not recognize 5090s (unsure as to why) so I am currently using 570-open

Could this be causing issues?


### AddyLaddy · 2025-02-20

The ncclMaxSharedMem message is likely the issue here. That should have been a WARN/exit and I've fixed it in the next release. On these systems you'll just have to reduce the amount of Shared Memory NCCL requests with this change:

```
diff --git a/src/include/device.h b/src/include/device.h
index f4dfcf219..0763a579a 100644
--- a/src/include/device.h
+++ b/src/include/device.h
@@ -474,7 +474,7 @@ __host__ __device__ constexpr int ncclCalcUnroll(int bytePerPack, int insns, int
 
 __host__ __device__ constexpr int ncclCollUnroll(int cudaArch = NCCL_CUDA_ARCH) {
   // Our collective unroll should move to the same bytes&insns model as NVLS.
-  return cudaArch >= 800 ? 8 : 4;
+  return cudaArch >= 800 ? (cudaArch == 1200 ? 6 : 8) : 4;
 }
 
 __host__ __device__ constexpr int ncclNvlsUnrollBytes(int cudaArch = NCCL_CUDA_ARCH) { return 4*16; }
```
 

### RCS1 · 2025-02-20

Is there a way I can adjust the test command to get around this and see performance? Thank you!

### AddyLaddy · 2025-02-20

> Is there a way I can adjust the test command to get around this and see performance? Thank you!

No, you need to modify the NCCL library in order for the CUDA kernels to work on these GPU SKUs. It will be fixed in NCCL 2.26.x

### sjeaugey · 2025-02-21

@RCS1 I was suggesting that you checkout the NCCL source code, delete line 488 of `src/include/device.h`, then recompile NCCL and use that newly-built NCCL. You can refer to the README for instruction on how to build NCCL. It's pretty straightforward.

Now maybe my change wouldn't work, and the patch above would work better.

### yangxin120704 · 2025-03-06

> > Is there a way I can adjust the test command to get around this and see performance? Thank you!
> 
> No, you need to modify the NCCL library in order for the CUDA kernels to work on these GPU SKUs. It will be fixed in NCCL 2.26.x

root@node:~/nccl-tests/build#_ NCCL_DEBUG=INFO ./alltoall_perf 

#nThread 1 nGpus 1 minBytes 33554432 maxBytes 33554432 step: 1048576(bytes) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
#Using devices
#Rank  0 Group  0 Pid  12225 on node device  0 [0000:16:00] NVIDIA GeForce RTX 5090
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
#out-of-place                       in-place          
#size count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#(B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
node: Test CUDA failure common.cu:297 'an illegal memory access was encountered'
 .. node pid 12225: Test failure common.cu:407
 .. node pid 12225: Test failure common.cu:594
 .. node pid 12225: Test failure alltoall.cu:97
 .. node pid 12225: Test failure common.cu:625
 .. node pid 12225: Test failure common.cu:1123
 .. node pid 12225: Test failure common.cu:893


when i change +  return cudaArch >= 800 ? (cudaArch == 1200 ? 6 : 8) : 4; i can run all_reduce_perf，bug alltoall has error

### sjeaugey · 2025-03-07

Is that last run on a single GPU? Didn't that work before?

### yangxin120704 · 2025-03-07

> Is that last run on a single GPU? Didn't that work before?

The 4090 works fine, but the 5090 fails to run on both single-GPU and multi-GPU setups—it never worked properly before either.

### RCS1 · 2025-03-10

all_reduce_perf works with 1x 5090, fails with multiple

alltoall_perf fails with 1x 5090 and multiple

### shahizat · 2025-03-12

Hello @AddyLaddy . could you please provide an estimated release date for the next version of NCCL? We are experiencing memory leaks during shared memory usage, which is preventing us from running inference on LLM models using two 5090 GPUs. 

### kiskra-nvidia · 2025-03-12

We are hoping for "really soon" (sorry, that's as specific as I'm willing to be without committing to a particular date).

However, I don't remember any recent reports or fixes regarding shared memory leaks -- would you mind providing any details you might have?

### kiskra-nvidia · 2025-03-13

@RCS1 NCCL 2.26.2 has been released -- could you let us know if it works better on 5090s for you?

### RCS1 · 2025-03-14

Can confirm all_reduce_perf now works. Thank you.

```
user@GENOA-01:~/nccl-tests$ sudo ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 4
# nThread 1 nGpus 4 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 2168673 on   GENOA-01 device  0 [0x01] NVIDIA GeForce RTX 5090
#  Rank  1 Group  0 Pid 2168673 on   GENOA-01 device  1 [0x21] NVIDIA GeForce RTX 5090
#  Rank  2 Group  0 Pid 2168673 on   GENOA-01 device  2 [0x41] NVIDIA GeForce RTX 5090
#  Rank  3 Group  0 Pid 2168673 on   GENOA-01 device  3 [0x61] NVIDIA GeForce RTX 5090
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
           8             2     float     sum      -1    15.60    0.00    0.00      0    15.22    0.00    0.00      0
          16             4     float     sum      -1    15.32    0.00    0.00      0    15.38    0.00    0.00      0
          32             8     float     sum      -1    15.52    0.00    0.00      0    15.67    0.00    0.00      0
          64            16     float     sum      -1    15.44    0.00    0.01      0    15.59    0.00    0.01      0
         128            32     float     sum      -1    15.46    0.01    0.01      0    15.46    0.01    0.01      0
         256            64     float     sum      -1    15.82    0.02    0.02      0    15.41    0.02    0.02      0
         512           128     float     sum      -1    15.81    0.03    0.05      0    15.83    0.03    0.05      0
        1024           256     float     sum      -1    15.88    0.06    0.10      0    15.70    0.07    0.10      0
        2048           512     float     sum      -1    26.16    0.08    0.12      0    26.26    0.08    0.12      0
        4096          1024     float     sum      -1    27.21    0.15    0.23      0    26.73    0.15    0.23      0
        8192          2048     float     sum      -1    27.45    0.30    0.45      0    27.42    0.30    0.45      0
       16384          4096     float     sum      -1    31.06    0.53    0.79      0    30.83    0.53    0.80      0
       32768          8192     float     sum      -1    31.64    1.04    1.55      0    31.57    1.04    1.56      0
       65536         16384     float     sum      -1    32.58    2.01    3.02      0    32.07    2.04    3.07      0
      131072         32768     float     sum      -1    35.19    3.72    5.59      0    34.79    3.77    5.65      0
      262144         65536     float     sum      -1    45.84    5.72    8.58      0    45.96    5.70    8.56      0
      524288        131072     float     sum      -1    70.24    7.46   11.20      0    69.50    7.54   11.32      0
     1048576        262144     float     sum      -1    93.45   11.22   16.83      0    93.21   11.25   16.87      0
     2097152        524288     float     sum      -1    152.9   13.72   20.57      0    152.6   13.75   20.62      0
     4194304       1048576     float     sum      -1    261.4   16.04   24.07      0    260.3   16.12   24.17      0
     8388608       2097152     float     sum      -1    490.3   17.11   25.67      0    489.8   17.13   25.69      0
    16777216       4194304     float     sum      -1    935.7   17.93   26.90      0    934.5   17.95   26.93      0
    33554432       8388608     float     sum      -1   1860.0   18.04   27.06      0   1866.0   17.98   26.97      0
    67108864      16777216     float     sum      -1   3708.9   18.09   27.14      0   3705.1   18.11   27.17      0
   134217728      33554432     float     sum      -1   7384.4   18.18   27.26      0   7380.5   18.19   27.28      0
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 9.09703 
#
```

### yangxin120704 · 2025-03-14

> Can confirm all_reduce_perf now works. Thank you.
> 
> ```
> user@GENOA-01:~/nccl-tests$ sudo ./build/all_reduce_perf -b 8 -e 128M -f 2 -g 4
> # nThread 1 nGpus 4 minBytes 8 maxBytes 134217728 step: 2(factor) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
> #
> # Using devices
> #  Rank  0 Group  0 Pid 2168673 on   GENOA-01 device  0 [0x01] NVIDIA GeForce RTX 5090
> #  Rank  1 Group  0 Pid 2168673 on   GENOA-01 device  1 [0x21] NVIDIA GeForce RTX 5090
> #  Rank  2 Group  0 Pid 2168673 on   GENOA-01 device  2 [0x41] NVIDIA GeForce RTX 5090
> #  Rank  3 Group  0 Pid 2168673 on   GENOA-01 device  3 [0x61] NVIDIA GeForce RTX 5090
> #
> #                                                              out-of-place                       in-place          
> #       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
> #        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
>            8             2     float     sum      -1    15.60    0.00    0.00      0    15.22    0.00    0.00      0
>           16             4     float     sum      -1    15.32    0.00    0.00      0    15.38    0.00    0.00      0
>           32             8     float     sum      -1    15.52    0.00    0.00      0    15.67    0.00    0.00      0
>           64            16     float     sum      -1    15.44    0.00    0.01      0    15.59    0.00    0.01      0
>          128            32     float     sum      -1    15.46    0.01    0.01      0    15.46    0.01    0.01      0
>          256            64     float     sum      -1    15.82    0.02    0.02      0    15.41    0.02    0.02      0
>          512           128     float     sum      -1    15.81    0.03    0.05      0    15.83    0.03    0.05      0
>         1024           256     float     sum      -1    15.88    0.06    0.10      0    15.70    0.07    0.10      0
>         2048           512     float     sum      -1    26.16    0.08    0.12      0    26.26    0.08    0.12      0
>         4096          1024     float     sum      -1    27.21    0.15    0.23      0    26.73    0.15    0.23      0
>         8192          2048     float     sum      -1    27.45    0.30    0.45      0    27.42    0.30    0.45      0
>        16384          4096     float     sum      -1    31.06    0.53    0.79      0    30.83    0.53    0.80      0
>        32768          8192     float     sum      -1    31.64    1.04    1.55      0    31.57    1.04    1.56      0
>        65536         16384     float     sum      -1    32.58    2.01    3.02      0    32.07    2.04    3.07      0
>       131072         32768     float     sum      -1    35.19    3.72    5.59      0    34.79    3.77    5.65      0
>       262144         65536     float     sum      -1    45.84    5.72    8.58      0    45.96    5.70    8.56      0
>       524288        131072     float     sum      -1    70.24    7.46   11.20      0    69.50    7.54   11.32      0
>      1048576        262144     float     sum      -1    93.45   11.22   16.83      0    93.21   11.25   16.87      0
>      2097152        524288     float     sum      -1    152.9   13.72   20.57      0    152.6   13.75   20.62      0
>      4194304       1048576     float     sum      -1    261.4   16.04   24.07      0    260.3   16.12   24.17      0
>      8388608       2097152     float     sum      -1    490.3   17.11   25.67      0    489.8   17.13   25.69      0
>     16777216       4194304     float     sum      -1    935.7   17.93   26.90      0    934.5   17.95   26.93      0
>     33554432       8388608     float     sum      -1   1860.0   18.04   27.06      0   1866.0   17.98   26.97      0
>     67108864      16777216     float     sum      -1   3708.9   18.09   27.14      0   3705.1   18.11   27.17      0
>    134217728      33554432     float     sum      -1   7384.4   18.18   27.26      0   7380.5   18.19   27.28      0
> # Out of bounds values : 0 OK
> # Avg bus bandwidth    : 9.09703 
> #
> ```

can you try alltoall_perf work fine?

### RCS1 · 2025-03-14

Seems like it works.

```
user@GENOA-01:~/nccl-tests$ sudo ./build/./alltoall_perf
[sudo] password for m2: 
# nThread 1 nGpus 1 minBytes 33554432 maxBytes 33554432 step: 1048576(bytes) warmup iters: 5 iters: 20 agg iters: 1 validation: 1 graph: 0
#
# Using devices
#  Rank  0 Group  0 Pid 2181762 on   GENOA-01 device  0 [0x01] NVIDIA GeForce RTX 5090
#
#                                                              out-of-place                       in-place          
#       size         count      type   redop    root     time   algbw   busbw #wrong     time   algbw   busbw #wrong
#        (B)    (elements)                               (us)  (GB/s)  (GB/s)            (us)  (GB/s)  (GB/s)       
    33554432       8388608     float    none      -1    19.56  1715.44    0.00      0     0.78  43046.10    0.00    N/A
# Out of bounds values : 0 OK
# Avg bus bandwidth    : 0 
#
```

### kiskra-nvidia · 2025-03-15

Thank you for confirming; closing.
