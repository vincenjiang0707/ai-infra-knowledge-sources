# [Issue #547] How to tune Broadcast performance?

source: https://github.com/ROCm/rccl/issues/547
state: closed | updated: 2023-04-05T23:10:50Z
labels: 

## 正文

Hi!
I use Broadcast. I measured the **Broadcast** collective call and saw its performance with _HSA_FORCE_FINE_GRAIN_PCIE_=1 is **1.7 GB/sec** maximum. Broadcast **without** _HSA_FORCE_FINE_GRAIN_PCIE_ is > **14 GB/sec**. this is one order of magnitude!

- I work at GPU claster with 4 AI100 connected via PCIE (https://github.com/ROCmSoftwarePlatform/rccl/issues/538). 
- RCCL was built via `CXX=/opt/rocm/bin/hipcc cmake -DTRACE -DPROFILE 1 -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=<my path>`.

There is way to understand why the performance of Broadcast with **P2P** enabled (via _HSA_FORCE_FINE_GRAIN_PCIE_=1) is worse than HSA_FORCE_FINE_GRAIN_PCIE turned off?

Thanks!


## 评论 (15)

### vasslavich · 2022-05-12

It seems that the problem is that the P2P Send/Recv kernels running by Broadcast on each device copy the memory _from_ the root GPU _with source memory_ to themselves. That is _executor_ is not device of _source_ memory.
For comparison:

- `./TransferBench ./my.cfg 4G` with the configuration `1 4 (G0->G0->G1)` results up to 27GB/sec for PCIE-2
- `./TransferBench ./my.cfg 4G` with the configuration `1 4 (G0->G1->G1)` results to < 2.9GB/sec only

### gilbertlee-amd · 2022-05-12

Broadcast isn't built on P2P send/recv kernels, so I don't think TransferBench is representative of the performance difference.  
Performing copies using (local read + remote write) (G0->G0->G1) generally performs faster than (remote read + local write) (G0->G1->G1).  

Could you run broadcast again with and without HSA_FORCE_FINE_GRAIN_PCIE=1, and provide logs using NCCL_DEBUG=INFO along with NCCL_DEBUG_SUBSYS=all?

### vasslavich · 2022-05-13

@gilbertlee-amd , thank you for your attention!
I did Send/Recv and Broadcast tests and I've attached metrics (with the prefix **metrics_**) and logs (with the prefix **runlog_**).
**Send/Recv**:
- 2G x uint32
- 0->1, 2->3
- not inplace

**Broadcast**:
- 2G x uint32
- _root_ device _0_
- 0 -> {1,2,3}
- not inplace
- I estimate the performance of a sending for _root_ by the expression: 2G x sizeof(uint32) x 4 / _time of collectives_

It looks strange: 
- WriteSize metric for Broadcast is ~16Gb at GPU 0,1,2. 
- by the _rocprof_'s output in _*.csv_, the kernel _ncclKernel_SendRecv_RING_SIMPLE_Sum_int8_t_ are called in both cases - for Send/Recv and Broadcast

[metrics_broadcast_fine_grain_pcie_OFF.csv](https://github.com/ROCmSoftwarePlatform/rccl/files/8689237/metrics_broadcast_fine_grain_pcie_OFF.csv)
[metrics_broadcast_fine_grain_pcie_ON.csv](https://github.com/ROCmSoftwarePlatform/rccl/files/8689238/metrics_broadcast_fine_grain_pcie_ON.csv)
[metrics_sendrecv_fine_grain_pcie_OFF.csv](https://github.com/ROCmSoftwarePlatform/rccl/files/8689239/metrics_sendrecv_fine_grain_pcie_OFF.csv)
[metrics_sendrecv_fine_grain_pcie_ON.csv](https://github.com/ROCmSoftwarePlatform/rccl/files/8689240/metrics_sendrecv_fine_grain_pcie_ON.csv)
[runlog_broadcast_fine_grain_pcie_OFF.txt](https://github.com/ROCmSoftwarePlatform/rccl/files/8689241/runlog_broadcast_fine_grain_pcie_OFF.txt)
[runlog_broadcast_fine_grain_pcie_ON.txt](https://github.com/ROCmSoftwarePlatform/rccl/files/8689242/runlog_broadcast_fine_grain_pcie_ON.txt)
[runlog_sendrecv_fine_grain_pcie_OFF.txt](https://github.com/ROCmSoftwarePlatform/rccl/files/8689243/runlog_sendrecv_fine_grain_pcie_OFF.txt)
[runlog_sendrecv_fine_grain_pcie_ON.txt](https://github.com/ROCmSoftwarePlatform/rccl/files/8689244/runlog_sendrecv_fine_grain_pcie_ON.txt)


### vasslavich · 2022-05-20

Hello!
If copies using (_local read + remote write_) generally performs faster than (_remote read + local write_), _why_ not use this fact in collective operations? In MI100 there are 120 CU. _TransferBench_ shows that the saturation of the throughput in the copy-kernel is achieved at 4 CU. In other words, in case when P2P access is enabled, we can **simultaneously** perform 120/4 copies to remote GPUs. Or, are there any HW restrictions of the root GPU on the simultaneous use of transfers to many GPUs?

### gilbertlee-amd · 2022-05-20

Hi,

When HSA_FINE_GRAIN_PCIE is enabled, RCCL attempts to use peer to peer PCIe transfers, instead of staging via shared CPU memory buffers.  On certain configurations, this can improve performance however there are certain configurations where peer to peer PCIe transfers may actually cause performance degradation, for example, when all GPUs are connected to the root CPU PCIe port, in which case all those transfers may contend with one another.  It appears that this may be the case here.  Would you be able to share your topology.xml file? (Set via NCCL_TOPO_DUMP_FILE).

The primitives used by the collective operations within RCCL are all local read + remote write, as far as I know.  Generally data is read locally by a GPU, then written to a buffer on the remote GPU during the "send" operations.  Even during a "recv" operation, this is reading from the local buffer (that was written to by the remote GPU), prior to copying remotely to the next GPU.

Due to how group calls are implemented, only a single kernel is launched, which is why profiler will also show the same kernel name for broadcast / sends.  Further differentiation of the collective is handled within that kernel - branching off to the appropriate device functions.

Currently Broadcast in RCCL (and NCCL) only utilizes a ring to perform the broadcast.  The array is chunked and data is passed in parallel from each GPU to the next GPU in ring, stopping only at the "end" of the ring.  Each GPU only sends to a single "next" gpu (except the last GPU in the ring).

You are correct in that it should be possible to actually have the root simultaneously broadcast data to all other GPUs (at least for this configuration), although additional pre-allocated buffers would be required, which isn't something currently implemented.  The issue is that the number of buffers grows significantly with the number of GPUs on the node (N squared).  Also, I'm not sure if you would see much improvement as PCIe bandwidth available from the root GPU is still a limiting factor.
Perhaps this is something you could simulate with TransferBench with simultaneous transfers:

## Case 1: Ring style
4 (G0->G0->G1) (G1->G1->G2) (G2->G2->G3) (G3->G3->G0)
## Case 2: Tree style
4 (G0->G0->G0) (G0->G0->G1) (G0->G0->G2) (G0->G0->G3)

It doesn't quite account for the initial costs for "filling" the pipeline with data, however it's likely a good performance estimate.


### vasslavich · 2022-06-06

Hi! @gilbertlee-amd , thank you for your reply!
Please, refer to my attached topology file (via NCCL_TOPO_DUMP_FILE) with HSA_FORCE_FINE_GRAIN_PCIE=1.
[rccl_topology.xml.txt](https://github.com/ROCmSoftwarePlatform/rccl/files/8843712/rccl_topology.xml.txt)



### vasslavich · 2022-06-20

Hi! @gilbertlee-amd , can you hints me please how I can understands if _all GPUs are connected to the root CPU PCIe port_? **Root PCIe port** be a _Root complex_ like [this](https://en.wikipedia.org/wiki/Root_complex)?

As far as I understand, sysfs KFD topology is: 
- GPU0, GPU1 are on NUMA1 and GPU2, GPU3 are on NUMA3. 
- GPU0 <-> GPU1 PCIE
- NUMA1 <-> NUMA3 Hypertransport

I.e. in my case:
- the root port can be between GPU0-GPU1 and between GPU2-GPU3?

Thanks!



### gilbertlee-amd · 2022-06-22

Hi @vasslavich,

Sorry for the delay - I had been on holidays.

I only meant "all GPUs are connected to the root CPU PCIe port" as an example for how performance could be degraded.
Technically, I should probably had said if all GPUs had to go through PCI root complex in order to communicate with each other to be more clear.

In the topology file you provided, GPUs 0 and 1 are connected by a PCIe switch (43:00.0).  Theoretically, this should mean that when GPU 0 sends to GPU 1, the data only goes up to the PCIe switch then back down to GPU 1.  For GPU 0 to 2/3, the data needs to go all the up to the root complex, across HyperTransport then back down.   
Even in this situation, I wouldn't expect performance to drop down to only 1.7GB/s for a broadcast.

I spoke with some other team members, and they suggested looking into whether or not Access Control Service (ACS) is enabled.  If it is not disabled, all peer to peer traffic may end up having to go back up to the root complex.   You may be able to check status via lspci -vv.

Could you run TransferBench with 
4 4 (G0->G0->G0) (G0->G0->G1) (G0->G0->G2) (G0->G0->G3), both with HSA_FORCE_FINE_GRAIN_PCIE=0/1?
as well as "./TransferBench p2p"?

Also, are you running bare-metal or under virtualization?


### vasslavich · 2022-06-28

Hi, @gilbertlee-amd! Thank you for your feedback.

Yes, I run tests in docker container. I use the latest ROCm 5.1.3.

The output of TransferBench with HSA_FORCE_FINE_GRAIN_PCIE=0 and `4 4 (G0->G0->G0) (G0->G0->G1) (G0->G0->G2) (G0->G0->G3)` is

```
Run configuration (TransferBench v1.02)
=====================================================
BLOCK_BYTES          =          256 : Each CU gets a multiple of 256 bytes to copy
BYTE_OFFSET          =            0 : Using byte offset of 0
FILL_PATTERN         =      (unset) : Pseudo-random: (Element i = i modulo 383 + 31)
NUM_CPU_PER_TRANSFER =            4 : Using 4 CPU thread(s) per CPU-based-copy Transfer
NUM_ITERATIONS       =           10 : Running 10 timed iteration(s) per topology
NUM_WARMUPS          =            3 : Running 3 warmup iteration(s) per topology
OUTPUT_TO_CSV        =            0 : Output to console
SHARED_MEM_BYTES     =      (unset) : Using 32769 shared mem per threadblock
USE_HIP_CALL         =            0 : Using custom kerncd els for GPU-executed copies
USE_INTERACTIVE      =            0 : Running in non-interactive mode
USE_MEMSET           =            0 : Performing memcopy
USE_PCIE_INDEX       =            0 : Using HIP-based GPU indexing
USE_SINGLE_STREAM    =            0 : Using single stream per Transfer

Test 1: [1073741824 bytes]
 Transfer 00: G00 -> [GPU 00:004] -> G00 |     8.420 GB/s |  127.527 ms | LOCAL-LOCAL     
 Transfer 01: G00 -> [GPU 00:004] -> G01 |     8.413 GB/s |  127.626 ms | LOCAL-PCIE-2    
 Transfer 02: G00 -> [GPU 00:004] -> G02 |     8.406 GB/s |  127.742 ms | LOCAL-PCIE-2    
 Transfer 03: G00 -> [GPU 00:004] -> G03 |     8.416 GB/s |  127.587 ms | LOCAL-PCIE-2    
 Aggregate Bandwidth (CPU timed)         |    33.518 GB/s |  128.139 ms | Overhead: 0.397 ms
```

The output of TransferBench with HSA_FORCE_FINE_GRAIN_PCIE=1 and `4 4 (G0->G0->G0) (G0->G0->G1) (G0->G0->G2) (G0->G0->G3)`:
```
Run configuration (TransferBench v1.02)
=====================================================
BLOCK_BYTES          =          256 : Each CU gets a multiple of 256 bytes to copy
BYTE_OFFSET          =            0 : Using byte offset of 0
FILL_PATTERN         =      (unset) : Pseudo-random: (Element i = i modulo 383 + 31)
NUM_CPU_PER_TRANSFER =            4 : Using 4 CPU thread(s) per CPU-based-copy Transfer
NUM_ITERATIONS       =           10 : Running 10 timed iteration(s) per topology
NUM_WARMUPS          =            3 : Running 3 warmup iteration(s) per topology
OUTPUT_TO_CSV        =            0 : Output to console
SHARED_MEM_BYTES     =      (unset) : Using 32769 shared mem per threadblock
USE_HIP_CALL         =            0 : Using custom kernels for GPU-executed copies
USE_INTERACTIVE      =            0 : Running in non-interactive mode
USE_MEMSET           =            0 : Performing memcopy
USE_PCIE_INDEX       =            0 : Using HIP-based GPU indexing
USE_SINGLE_STREAM    =            0 : Using single stream per Transfer

Test 1: [1073741824 bytes]
 Transfer 00: G00 -> [GPU 00:004] -> G00 |     8.467 GB/s |  126.821 ms | LOCAL-LOCAL     
 Transfer 01: G00 -> [GPU 00:004] -> G01 |     8.410 GB/s |  127.675 ms | LOCAL-PCIE-2    
 Transfer 02: G00 -> [GPU 00:004] -> G02 |     8.407 GB/s |  127.715 ms | LOCAL-PCIE-2    
 Transfer 03: G00 -> [GPU 00:004] -> G03 |     8.427 GB/s |  127.424 ms | LOCAL-PCIE-2    
 Aggregate Bandwidth (CPU timed)         |    33.538 GB/s |  128.064 ms | Overhead: 0.350 ms
```

I did some additional tests with HSA_FORCE_FINE_GRAIN_PCIE=1. For broadcast I got

|   Devices        | Throughput, GB/s |
|  ---                 |   ---                       |
| 0 -> {0,2}        |     25.7                  |
| 0 -> {0,2,3}     |     12.8                  |
| 0 -> {0,1,2,3}  |     1.7                    |


and for P2P

|  Devices           |  Throughput, GB/s   |
| ---                    |    ---                         |
| 0->1, 2->3       |  16.5                        |
| 0->2, 1->3       |  13.1                        |
| 0->3, 1->2       |  13.2                        |

If we suggest that P2P traffic also goes through the root complex, then why it only affects the Broadcast?


### vasslavich · 2022-06-28

ACS is enabled for some of PCI bridges (an example of one via `lspci -vvv`):
```
40:01.1 PCI bridge: Advanced Micro Devices, Inc. [AMD] Starship/Matisse GPP Bridge (prog-if 00 [Normal decode])
....
	NUMA node: 1
....
	Capabilities: [2a0 v1] Access Control Services
		ACSCap:	SrcValid+ TransBlk+ ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans+
		ACSCtl:	SrcValid+ TransBlk- ReqRedir+ CmpltRedir+ UpstreamFwd+ EgressCtrl- DirectTrans-
....
```
and via `lspci -tv`:
```
 +-[0000:40]-+-00.0  Advanced Micro Devices, Inc. [AMD] Starship/Matisse Root Complex
 |           +-00.2  Advanced Micro Devices, Inc. [AMD] Starship/Matisse IOMMU
 |           +-01.0  Advanced Micro Devices, Inc. [AMD] Starship/Matisse PCIe Dummy Host Bridge
 |           +-01.1-[43-53]--+-00.0-[44-53]--+-00.0-[45]----00.0  Mellanox Technologies MT28908 Family [ConnectX-6]
 |           |               |               +-01.0-[46-4b]--+-00.0-[47-4b]--+-00.0-[48-4a]----00.0-[49-4a]----00.0-[4a]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 738c
 |           |               |               |               |               \-01.0-[4b]--
 |           |               |               |               \-00.1  PMC-Sierra Inc. Device 4000
 |           |               |               +-02.0-[4c-51]--+-00.0-[4d-51]--+-00.0-[4e-50]----00.0-[4f-50]----00.0-[50]----00.0  Advanced Micro Devices, Inc. [AMD/ATI] Device 738c
 |           |               |               |               |               \-01.0-[51]--
 |           |               |               |               \-00.1  PMC-Sierra Inc. Device 4000
 |           |               |               +-03.0-[52]----00.0  SK hynix Device 2839
 |           |               |               \-04.0-[53]----00.0  SK hynix Device 2839
 |           |               \-00.1  PMC-Sierra Inc. Device 4000
```

but I'm not sure how to check if that's the PCI bridge which GPUs are connected to. Could you suggest how to check this?

### gilbertlee-amd · 2022-06-28

ACS should likely be enabled for virtualized environments.  lstopo output to a image file another way to check which one the GPU is connected to.

I'm still not quite sure what could be causing the difference in performance for broadcast.  For the send,recv could you actually simulate the broadcast (0->1) (0->2) (0->3), From your test, I see the expected slowdown when it goes across the HyperTransport, however it still doesn't come close to the slow broadcast performance.

Do you see the same performance issue running on bare-metal?

I'll try to investigate what other changes HSA_FORCE_FINE_GRAIN_PCIE=1 could be having on RCCL.

### vasslavich · 2022-07-14

Hello, @gilbertlee-amd ! Thank you!
I'd been on holidays, as well. I ran the Broadcast benchmark on bare-metal. The performance issue still remains.

### gilbertlee-amd · 2022-09-08

Hi @vasslavich ,

Sorry, but I haven't heard back anything interesting from the team behind HSA_FORCE_FINE_GRAIN_PCIE=1.
In the meantime, could you try copying in TransferBench using fine-grained GPU memory?

Previously you had run:
4 4 (G0->G0->G0) (G0->G0->G1) (G0->G0->G2) (G0->G0->G3)
Could you also run:
4 4 (F0->G0->F0) (F0->G0->F1) (F0->G0->F2) (F0->G0->F3)

Thanks




### vasslavich · 2022-09-09

Hi @gilbertlee-amd !
Yes, I will do it on the next week, when the server will available again.
Thank you a lot for your attention!

### gilbertlee-amd · 2023-04-05

Closing for now.  Please re-open when more information is available
