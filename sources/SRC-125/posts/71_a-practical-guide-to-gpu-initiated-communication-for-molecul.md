# a-practical-guide-to-gpu-initiated-communication-for-molecular-dynamics-at-scale

source: https://developer.nvidia.com/blog/a-practical-guide-to-gpu-initiated-communication-for-molecular-dynamics-at-scale/

Molecular dynamics (MD) simulations are among the most demanding workloads in computational science. Using them, researchers can observe atomic behavior in extraordinary detail, from protein folding to drug and materials discovery.

But they come at a steep cost. Simulations model hundreds of thousands to tens of millions of atoms, advancing femtoseconds per step across billions of steps. Because problem size is typically fixed, parallelization must spread work across all available resources simultaneously, a regime known as strong scaling.

[GROMACS](https://www.gromacs.org/) is one of the world’s most widely used MD packages. Modern hardware and [heterogeneous CPU-GPU parallelization](https://doi.org/10.1063/5.0018516) has pushed performance into the sub-millisecond regime, reaching 100–200 microseconds per time-step across multiple GPUs. Achieving strong scaling at this level demands extremely low kernel latency, but GPU-to-GPU communication remains a fundamental bottleneck as simulations scale across more GPUs.

Most large-scale HPC applications, including GROMACS, use the Message Passing Interface (MPI) for inter-process communication. However, MPI was designed for CPU-centric execution.

When GROMACS runs on GPUs, the communication workflow forces the GPU to pause while the CPU orchestrates data transfers before signaling the GPU to resume. In GROMACS’s halo exchange—the algorithm that shares boundary atom data between neighboring GPU domains—this handoff repeats across all three spatial dimensions, consuming more than 50% of total CPU wall time at peak iteration rates and capping scalability.

In this post, we examine strategies to eliminate this bottleneck by replacing CPU-orchestrated MPI with GPU-native communication using [NVSHMEM](https://developer.nvidia.com/nvshmem).

## Accelerating GROMACS using Device-initiated Remote Memory Access

The key to accelerating GROMACS is eliminating CPU-GPU handoffs with GPU-native communication. NVIDIA NVSHMEM is a library for implementing remote memory access based on the OpenSHMEM partitioned global address space model. NVSHMEM enables GPU kernels to initiate data transfers directly, removing the CPU from the critical path and enabling better overlap of computation and communication.

The GROMACS halo exchange uses a staged forwarding mechanism: data is relayed through intermediate ranks within each spatial dimension across one or more communication steps, or pulses. Each pulse begins with a pack kernel that gathers boundary atoms into a contiguous send buffer. This creates a chain of dependencies between communication phases (Z → Y → X) that the traditional implementation handles through coarse phase-level serialization. The reformulation replaces these coarse barriers with fine-grained per-pulse signals expressed directly in a fused kernel.

A natural starting point is the stream-triggered API (nvshmemx_put_signal_nbi_on_stream), which removes CPU-GPU synchronization barriers with minimal code restructuring. It has two limitations: communication can only begin at a kernel boundary, preventing pack/communication overlap within a pulse, and stream-governed sequencing means the dependent forwarding chain (Z → Y → X) cannot be fused.

We address both with fine-grained per-pulse dependencies in the [Replacing host-side communication](https://developer.nvidia.com/blog/?p=119056&preview=1&_ppp=2df0ef2355#replacing_host-side_communication_with_nvshmem) and [Enabling parallelism across pulses ](https://developer.nvidia.com/blog/?p=119056&preview=1&_ppp=2df0ef2355#enabling_parallelism_across_pulses_through_kernel_fusion)sections.

The following figure shows execution diagrams of a simulation timestep with two communication pulses, showing how kernel-initiated RMA, kernel fusion, and event-driven multi-queue execution overlap communication and computation.

*Figure 2. GROMACS NVSHMEM schedule for 2D DD. Overlapping CPU kernel launches and GPU compute streams remove halo exchange from the critical path*

## From MPI baseline to optimized GPU-native halo exchange

The existing MPI-based halo exchange relays data through neighboring ranks to minimize communication volume, but at the cost of sequential dependencies across the three phases (Z → Y → X), each containing one or more pulses. The following code shows the coordinate halo-exchange pack kernel and its host-side invocation from the GROMACS source code.

````cuda` `// GPU kernel: pack boundary atom coordinates into a contiguous send buffer ` `__global__ void packSendBufKernel(float3* dataPacked, // packed coordinate buffer ` ` ` `const float3* data, // full coordinate array ` ` ` `const int* map, // index map: which atoms to pack ` ` ` `const int mapSize) ` `{ ` ` ` `int threadIndex = blockIdx.x * blockDim.x + threadIdx.x; ` ` ` `if (threadIndex < mapSize) ` ` ` `{ ` ` ` `dataPacked[threadIndex] = data[map[threadIndex]]; ` ` ` `} ` `}` `// GPU kernel: unpack received halo forces, scatter back into the force array via index map ` `template<bool accumulate> ` `__global__ void unpackRecvBufKernel(float3* forces, // full force array ` ` ` `const float3* dataPacked, // received packed forces ` ` ` `const int* map, ` ` ` `const int mapSize) ` `{ ` ` ` `int threadIndex = blockIdx.x * blockDim.x + threadIdx.x; ` ` ` `if (threadIndex < mapSize) ` ` ` `{ ` ` ` `if (accumulate) ` ` ` `forces[map[threadIndex]] += dataPacked[threadIndex]; ` ` ` `else ` ` ` `forces[map[threadIndex]] = dataPacked[threadIndex]; ` ` ` `} ` `} ` ````` ````c` `// CPU host code: coordinate halo exchange (MPI path)` `for each dimension d in [Z, Y, X]:` ` ` `for each pulse p in dimension d:` ` ` `// 1. Launch GPU pack kernel on non-local stream` ` ` `packSendBufKernel<<<grid, block, 0, nonLocalStream>>>(` ` ` `sendBuf, coords, indexMap, mapSize);` ` ` `// 2. CPU blocks until GPU pack completes` ` ` `cudaStreamSynchronize(nonLocalStream); // *** BLOCKING ***` ` ` `// 3. CPU orchestrates MPI transfer` ` ` `MPI_Isend(sendBuf, sendSize, sendRank, ...);` ` ` `MPI_Irecv(coords + atomOffset, recvSize, recvRank, ...);` ` ` `MPI_Waitall(...); // *** BLOCKING ***` ` ` `// Received data lands directly` ` ` `// in the coordinate buffer at the correct offset and is consumed` ` ` `// by the non-local non-bonded force kernel as-is.` ````` |

While these kernels are simple, the bottleneck is the CPU-side control flow that wraps them. Every pulse requires the CPU to block on the GPU, start an MPI transfer, and signal the GPU to resume a serializing sequence for each pulse across all three dimensions.

The force halo exchange follows the same pattern but in the reverse direction (X → Y → Z). The rank that sent coordinates now receives the forces computed on those halo atoms, and forces require a scatter-unpack step through `unpackRecvBufKernel`

because they must accumulate into the correct positions in the full-force array.

Every pulse requires two blocking CPU–GPU synchronizations: one before the MPI invocation to guarantee the pack kernel has completed, and one enforced before the next pulse can consume forwarded data. With a 3D decomposition and one pulse per dimension, that is six blocking waits per time-step for coordinates and six more for forces—12 in total. Each adds latency to the critical path, impacting GROMACS iteration rates.

### Replacing host-side communication with NVSHMEM

Building on this idea, the first design folds packing, the remote put, and the completion-wait into a single kernel per communication pulse. The host still issues launches in pulse order, but it drops the CPU–GPU barriers that sat between pulses. Correct execution order is now guaranteed by the NVIDIA CUDA stream alone. The host invocation of the fused pack-put-wait kernel and its implementation are:

````c` `// CPU host code: one kernel launch per pulse, no CPU-GPU sync in between` `int pulseOffset = 0;` `for each dimension d in [Z, Y, X]:` ` ` `for each pulse p in dimension d:` ` ` `// Pack + send + wait are fused into a single GPU kernel` ` ` `packSendBufAndPutNvshmemKernel<<<grid, block, 0, nonLocalStream>>>(` ` ` `coords, dataPacked, indexMap, sendSize,` ` ` `sendRank, atomOffsetInSendRank,` ` ` `signalReceiverRank + pulseOffset, signalCounter, bar, recvSize);` ` ` `pulseOffset++;` ````` |

The entire pack–put–wait operation is fused into a single device-side launch. Adapted from the GROMACS implementation, the kernel is:

````cuda` `__global__ void packSendBufAndPutNvshmemKernel(` ` ` `float3* coords, float3* dataPacked, int* map,` ` ` `int sendSize, int sendRank, int atomOffsetInSendRank,` ` ` `uint64_t* signalReceiverRank, uint64_t signalCounter,` ` ` `cuda::barrier<cuda::thread_scope_device>* bar, int recvSize)` `{` ` ` `int tid = blockIdx.x * blockDim.x + threadIdx.x;` ` ` `if (sendSize > 0)` ` ` `{` ` ` `// Pack: grid-stride gather into contiguous send buffer` ` ` `for (int i = tid; i < sendSize; i += blockDim.x * gridDim.x)` ` ` `dataPacked[i] = coords[map[i]];` ` ` `// Device-scoped barrier: all CTAs must finish packing before put` ` ` `auto token = bar->arrive();` ` ` `if (blockIdx.x == 0)` ` ` `{` ` ` `bar->wait(std::move(token));` ` ` `// Put packed data into peer's coordinate array` ` ` `nvshmemx_float_put_signal_nbi_block(` ` ` `&coords[atomOffsetInSendRank], // peer destination` ` ` `dataPacked, // local source` ` ` `sendSize * 3, // float count` ` ` `signalReceiverRank, signalCounter,` ` ` `NVSHMEM_SIGNAL_SET, sendRank);` ` ` `}` ` ` `}` ` ` `// Wait for incoming data from recvRank before exiting` ` ` `if (tid == 0 && recvSize > 0)` ` ` `nvshmem_signal_wait_until(signalReceiverRank, NVSHMEM_CMP_EQ, signalCounter);` `}` ````` |

This implementation eliminates all CPU-GPU synchronization from the critical path. The CPU only performs kernel launches, which can overlap with GPU execution. All GPU threads (CTAs) arrive at a device-scoped barrier after packing, and block 0 waits on that barrier to ensure all threads have finished before issuing the `nvshmemx_float_put_signal_nbi_block`

call. That call transfers the packed data to the peer and sets `signalReceiverRank`

on the peer to confirm completion; the receiver waits on that signal before consuming the data.

However, note that this version still processes pulses sequentially (stream ordering enforces it), and each pulse still incurs a separate kernel launch.

## Optimizing for efficient transfers across NVIDIA NVLink-connected GPUs

In the design described, data always routes through the NVSHMEM transport (`nvshmemx_float_put_signal_nbi_block`

), which works for any interconnect, but when the peer is NVLink-connected, GPUs can load/store directly into each other’s memory. Instead of packing into a local buffer and issuing a put, pack directly into the peer’s coordinate array and eliminate the separate global memory round-trip.

`nvshmem_ptr(remotePtr, peerRank)`

returns a non-null device pointer when the peer is reachable via NVLink, and null otherwise. We query this once in the kernel and branch accordingly, as shown:

````cuda` `__global__ void packSendBufAndPutNvshmemKernel(` ` ` `float3* coords, float3* dataPacked, int* map,` ` ` `int sendSize, int sendRank, int atomOffsetInSendRank,` ` ` `uint64_t* signalReceiverRank, uint64_t signalCounter,` ` ` `cuda::barrier<cuda::thread_scope_device>* bar, int recvSize)` `{` ` ` `int tid = blockIdx.x * blockDim.x + threadIdx.x;` ` ` `if (sendSize > 0)` ` ` `{` ` ` `// Probe for NVLink: non-null means direct store is possible` ` ` `float3* remotePtr = (float3*)nvshmem_ptr(coords, sendRank);` ` ` `bool isNVLink = (remotePtr != nullptr);` ` ` `// NVLink: pack directly into peer's coordinate buffer` ` ` `// IB: pack into local staging buffer for later put` ` ` `float3* dest = isNVLink ? (remotePtr + atomOffsetInSendRank)` ` ` `: dataPacked;` ` ` `for (int i = tid; i < sendSize; i += blockDim.x * gridDim.x)` ` ` `dest[i] = coords[map[i]];` ` ` `auto token = bar->arrive();` ` ` `if (blockIdx.x == 0)` ` ` `{` ` ` `bar->wait(std::move(token));` ` ` `if (isNVLink)` ` ` `{` ` ` `// Data already in peer memory — just signal completion` ` ` `uint64_t* peerSignal = (uint64_t*)nvshmem_ptr(` ` ` `signalReceiverRank, sendRank);` ` ` `storeReleaseSysAsm(peerSignal, signalCounter);` ` ` `}` ` ` `else` ` ` `{` ` ` `// IB: combined data transfer + signal notification` ` ` `nvshmemx_float_put_signal_nbi_block(` ` ` `(float*)&coords[atomOffsetInSendRank],` ` ` `(float*)dataPacked,` ` ` `sendSize * 3,` ` ` `signalReceiverRank, signalCounter,` ` ` `NVSHMEM_SIGNAL_SET, sendRank);` ` ` `}` ` ` `}` ` ` `}` ` ` `if (tid == 0 && recvSize > 0)` ` ` `nvshmem_signal_wait_until(signalReceiverRank, NVSHMEM_CMP_EQ, signalCounter);` `}` ````` |

On the NVLink path, the packing loop writes directly into the exact location in the peer’s coordinate array. Once block 0 confirms all CTAs have finished packing using the device-scoped barrier, it signals the peer with a system-scope release store (`st.release.sys`

), which ensures all the preceding direct writes are visible to the peer before it reads the signal. No additional data put operation is needed because the data is already in place.

When `nvshmem_ptr`

returns null, the behavior matches the first design. Data is packed into a local staging buffer and handed off to `nvshmemx_float_put_signal_nbi_block`

, which the NVSHMEM transport delivers over InfiniBand, Slingshot, or other RDMA fabrics.

This optimization highlights an important asymmetry between the two paths. The NVLink path requires many CUDA cores (SMs) issuing stores concurrently to saturate the NVLink bandwidth, whereas the InfiniBand path only needs a single thread (CTA) to initiate a bulk transfer using the NVSHMEM transport. The remaining bottlenecks are per-pulse kernel launch overhead and rigid sequential ordering between pulses, even when some data has no cross-pulse dependencies.

## Enabling parallelism across pulses through kernel fusion

The key insight is that not all data in a pulse depends on prior pulses. Most atoms in a pulse can be packed and sent immediately; only the “forwarded” atoms that receive data from a previous pulse must wait. This is achieved by partitioning each pulse’s index map at `dependencyAtomOffset`

:

**Independent atoms (atomIndex <**Safe to pack and send as soon as the pulse runs`dependencyAtomOffset`

):**Dependent atoms (atomIndex ≥**Must wait for the relevant previous-pulse signal`dependencyAtomOffset`

):

With this partition, a single kernel processes all pulses concurrently. Dependent work waits only on the specific per-pulse signal it needs, not on an entire phase.

### Dependency-aware packing

The `packSubset`

device function selectively packs atoms by threshold—first for independent atoms, then a second time for dependent atoms after waiting on signals.

````cuda` `// Templated pack: selectively gather atoms based on threshold` `// packAll=true: pack everything (no dependency check needed)` `// packAll=false, packLessThan=true: pack only atomIndex < threshold (independent)` `// packAll=false, packLessThan=false: pack only atomIndex >= threshold (dependent)` `template<bool packAll, bool packLessThan>` `__device__ void packSubset(float3* dest,` ` ` `float3* data,` ` ` `const int* map,` ` ` `int sendSize,` ` ` `int gridStride,` ` ` `int threadIndex,` ` ` `int threshold,` ` ` `int& hasDependencyAtoms)` `{` ` ` `for (int idx = threadIndex; idx < sendSize; idx += gridStride)` ` ` `{` ` ` `int atomIndex = map[idx];` ` ` `float3 srcVal = data[atomIndex];` ` ` `if constexpr (packAll)` ` ` `{` ` ` `dest[idx] = srcVal;` ` ` `}` ` ` `else` ` ` `{` ` ` `bool packNow = packLessThan ? (atomIndex < threshold)` ` ` `: (atomIndex >= threshold);` ` ` `if (packNow)` ` ` `dest[idx] = srcVal;` ` ` `else if (packLessThan)` ` ` `hasDependencyAtoms++; // track deferred atoms in first pass` ` ` `}` ` ` `}` `}` ````` |

Pulses are numbered globally in Z→Y→X order. Each waits for all preceding pulse signals before packing its dependent atoms. With one pulse per dimension `[z0, y0, x0]`

: `z0`

has no dependencies; `y0`

waits for `z0`

; `x0`

waits for both. This is what the loop `for (int i = currPulse; i > 0; i--)`

in `packHaloCoords`

implements:

````cuda` `// Dependency-aware packing: pack independent data immediately,` `// wait for signals from prior pulses, then pack dependent data` `__device__ void packHaloCoords(float3* dest,` ` ` `int sendSize,` ` ` `float3* data,` ` ` `const int* map,` ` ` `int currPulse,` ` ` `uint64_t signalCounter,` ` ` `uint64_t* signalReceiverRankCurr,` ` ` `int dependencyAtomOffset)` `{` ` ` `int gridStride = blockDim.x * gridDim.x;` ` ` `int threadIndex = blockIdx.x * blockDim.x + threadIdx.x;` ` ` `if (currPulse > 0)` ` ` `{` ` ` `// Pass 1: pack atoms below dependency threshold (no waiting)` ` ` `int hasDependencyAtoms = 0;` ` ` `packSubset<false, true>(dest, data, map, sendSize, gridStride,` ` ` `threadIndex, dependencyAtomOffset,` ` ` `hasDependencyAtoms);` ` ` `// Thread 0 waits for all prior pulses to deliver their data` ` ` `if (threadIdx.x == 0)` ` ` `{` ` ` `for (int i = currPulse; i > 0; i--)` ` ` `while (loadRelaxedSys(signalReceiverRankCurr - i) != signalCounter)` ` ` `;` ` ` `}` ` ` `constexpr unsigned fullWarpMask = 0xFFFFFFFF;` ` ` `int need_to_wait = __any_sync(fullWarpMask, hasDependencyAtoms > 0);` ` ` `__syncthreads();` ` ` `// Pass 2: pack the deferred atoms (>= threshold)` ` ` `if (need_to_wait)` ` ` `{` ` ` `int unused = 0;` ` ` `packSubset<false, false>(dest, data, map, sendSize, gridStride,` ` ` `threadIndex, dependencyAtomOffset,` ` ` `unused);` ` ` `}` ` ` `}` ` ` `else` ` ` `{` ` ` `// Pulse 0: no dependencies, pack everything unconditionally` ` ` `int unused = 0;` ` ` `packSubset<true, true>(dest, data, map, sendSize, gridStride,` ` ` `threadIndex, 0, unused);` ` ` `}` ` ` `__syncthreads();` `}` ````` |

A practical note: `loadRelaxedSys`

uses PTX `ld.relaxed.sys.global.u64`

—system scope because the signal is written by a remote GPU, relaxed ordering because it’s a spin loop. The `__syncthreads()`

after the wait makes the guarded data visible to all threads. In production code, `cuda::atomic_ref<uint64_t, cuda::thread_scope_system>`

with `cuda::memory_order_relaxed`

from libcu++ provides equivalent semantics.

The [fused kernel](https://gitlab.com/gromacs/gromacs/-/blob/release-2026/src/gromacs/domdec/gpuhaloexchange_impl_gpu.cu?ref_type=heads#L581) assigns each pulse to a `blockIdx.y`

row, with all blocks in that row cooperating on one pulse via a grid-stride loop (indexed by `blockIdx.x`

). The pre-computed remote pointer selects the transport at runtime: non-null means NVLink direct stores, null falls back to the NVSHMEM put path (InfiniBand):

````cuda` `// One kernel launch replaces all per-pulse pack + send operations` `// Grid: (blocksPerPulse, totalNumPulses, 1) — one blockIdx.y per pulse` `__global__ void fusedPulsesPackAndSendKernel(` ` ` `float3* data, // full coordinate array` ` ` `HaloExchangeData* pulseData, // per-pulse metadata array` ` ` `uint64_t* signalReceiverRank,` ` ` `uint64_t signalCounter,` ` ` `uint32_t* gridSync, // per-pulse block-completion counters` ` ` `int totalNumPulses,` ` ` `int dependencyAtomOffset)` `{` ` ` `int currPulse = blockIdx.y;` ` ` `if (currPulse < totalNumPulses)` ` ` `{` ` ` `HaloExchangeData halo = pulseData[currPulse];` ` ` `// Precomputed by nvshmem_ptr; null => IB/RDMA path` ` ` `float3* remotePtr = halo.remoteCoordsPutPtr;` ` ` `bool isNVLink = (remotePtr != nullptr);` ` ` `// Choose destination: peer memory (NVLink) or local staging buffer (IB)` ` ` `float3* dest = isNVLink ? (remotePtr + halo.atomOffsetInPeer)` ` ` `: halo.d_sendBuf;` ` ` `if (halo.sendSize > 0)` ` ` `{` ` ` `// Two-pass dependency-aware packing` ` ` `packHaloCoords(dest, halo.sendSize, data, halo.indexMap,` ` ` `currPulse, signalCounter,` ` ` `signalReceiverRank + currPulse,` ` ` `dependencyAtomOffset);` ` ` `// Last-block sync and peer notification` ` ` `if (threadIdx.x == 0)` ` ` `signalPeerOnLastBlock(` ` ` `isNVLink,` ` ` `gridSync + currPulse, signalReceiverRank + currPulse,` ` ` `signalCounter, halo.sendRank, gridDim.x,` ` ` `dest, halo.recvPtr, halo.sendSize);` ` ` `}` ` ` `}` `}` ````` |

A subtle but performance-critical optimization is fusing receiver notification into the same kernel. Typical NVSHMEM patterns use a separate kernel or host-side call to signal the receiver. We avoid this with `signalPeerOnLastBlock`

, which uses a hierarchical block-completion counter to elect the last block as shown below.

````cuda` `// Custom PTX wrappers for precise memory ordering control` `__device__ uint32_t atomicIncReleaseGpu(uint32_t* addr, int32_t mod) {` ` ` `uint32_t old;` ` ` `asm("atom.inc.release.gpu.global.u32 %0,[%1],%2;"` ` ` `: "=r"(old) : "l"(addr), "r"(mod) : "memory");` ` ` `return old;` `}` `__device__ void storeReleaseSys(uint64_t* ptr, uint64_t val) {` ` ` `asm("st.release.sys.global.u64 [%0], %1;" : : "l"(ptr), "l"(val) : "memory");` `}` `__device__ void signalPeerOnLastBlock(` ` ` `bool isNVLink, // selects NVLink direct-store path vs. InfiniBand put` ` ` `uint32_t* gridSync, // per-pulse block-completion counter` ` ` `uint64_t* signalCurr, // peer's signal slot for this pulse` ` ` `uint64_t signalCounter, // value to store into the signal slot` ` ` `int sendRank, // peer rank to notify` ` ` `int numBlocks,` ` ` `const float* dataPacked, // staging buffer (InfiniBand path only)` ` ` `void* recvPtr, // peer's receive buffer (InfiniBand path only)` ` ` `int sendSize) // payload size in float3 elements (InfiniBand only)` `{` ` ` `// GPU-scope release atomic: flushes this block's writes to GPU scope` ` ` `// and returns the old counter value` ` ` `uint32_t old = atomicIncReleaseGpu(gridSync, numBlocks - 1);` ` ` `// Only the last arriving block proceeds` ` ` `if (old != numBlocks - 1)` ` ` `return;` ` ` `if (isNVLink)` ` ` `{` ` ` `// NVLink: data already written directly — just signal the peer` ` ` `// st.release.sys ensures all prior writes visible before signal` ` ` `uint64_t* peerSignal = (uint64_t*)nvshmem_ptr(signalCurr, sendRank);` ` ` `storeReleaseSys(peerSignal, signalCounter);` ` ` `}` ` ` `else` ` ` `{` ` ` `// InfiniBand: combined data transfer + notification` ` ` `nvshmem_float_put_signal_nbi(` ` ` `recvPtr, dataPacked, sendSize * 3,` ` ` `signalCurr, signalCounter, NVSHMEM_SIGNAL_SET, sendRank);` ` ` `}` `}` ````` |

`atomicIncReleaseGpu`

wraps PTX `atom.inc.release.gpu.global.u32`

, combining block-completion tracking with a GPU-scope release that flushes all preceding writes. Only the last arriving block pays the system-scope store, or NVSHMEM put; all others exit immediately.

## NVLink path: TMA-based direct stores

On the NVLink path, a further optimization offloads the data movement from SMs to the Tensor Memory Accelerator (TMA) async copy engine (NVIDIA Hopper and later), freeing SM resources for compute. The TMA variant works at per-warp granularity each warp independently issues its own TMA store:

- Each warp packs its independent atoms into shared memory
- If the warp’s chunk contains dependent atoms, the warp leader waits on prior-pulse signals before all lanes pack the remaining atoms—fully populating the shared memory buffer
- The warp leader issues a single TMA store (
`cuda::ptx::cp_async_bulk`

) of the complete buffer to the peer, and other warps proceed independently with no block-wide synchronization required

````cuda` `// NVLink TMA path: per-warp pipelining of pack + remote store` `int warpId = threadIdx.x / 32;` `int laneId = threadIdx.x % 32;` `int warpChunk = SMEM_BUFFER_LENGTH / numWarpsPerBlock;` `float3* mySmem = &sharedBuf[warpId * warpChunk];` `int chunkOffset = blockIdx.x * SMEM_BUFFER_LENGTH + warpId * warpChunk;` `bool isWarpLeader = warpElect(); // elect one thread per warp` `// Pass 1: pack independent atoms into shared memory` `for (int i = laneId; i < warpChunk; i += 32) {` ` ` `int atomIdx = indexMap[chunkOffset + i];` ` ` `if (atomIdx < dependencyAtomOffset)` ` ` `mySmem[i] = data[atomIdx];` `}` `// Pass 2 only when this warp's chunk contains dependent atoms` `if (hasDependencyAtoms) {` ` ` `// Warp leader: wait on prior pulse signals before packing dependent atoms` ` ` `if (isWarpLeader) {` ` ` `// ... wait on prior pulse signals at warp granularity ...` ` ` `}` ` ` `__syncwarp();` ` ` `for (int i = laneId; i < warpChunk; i += 32) {` ` ` `int atomIdx = indexMap[chunkOffset + i];` ` ` `if (atomIdx >= dependencyAtomOffset)` ` ` `mySmem[i] = data[atomIdx];` ` ` `}` `}` `// Warp leader issues TMA async store of the full contiguous buffer to peer` `if (isWarpLeader)` ` ` `cuda::ptx::cp_async_bulk(remoteDst + chunkOffset, mySmem,` ` ` `warpChunk * sizeof(float3));` `// Other warps continue independently — no syncthreads() between warps` ````` |

The TMA engine handles remote stores independently of the SM, freeing compute resources. Each warp issues its store as soon as it finishes packing; warps with only independent atoms skip the dependency wait entirely. Shared memory serves as a staging area satisfying TMA’s alignment requirements while ensuring a fully populated buffer before the TMA bulk copy.

### Force halo exchange: Reversing the dependency chain

During the force halo exchange, computed forces on boundary atoms are sent back to the ranks that originally owned those atoms. Here, the dependency chain is reversed. The last pulse’s forces become available first, and earlier pulses wait for later ones before forwarding accumulated forces. The fused kernel handles force communication and unpacking in a single kernel that processes data as it flows backwards through the pulse chain.

### SM occupancy and kernel scheduling

The overlap benefits also depend on a subtlety of GPU scheduling. The compute-intensive local non-bonded force kernel fills every SM with hundreds of thread blocks, and the scheduler can’t preempt running blocks, so the high-priority communication kernels can’t start until some local blocks finish and free their SMs. With MPI, the pack and unpack kernels launched for each pulse pay for this scheduling delay independently at every launch. The fused kernel pays it once: a single kernel handles all pulses, and dependency-aware partitioning lets it immediately pack and send independent data the moment it is scheduled, while dependent data is still in flight. Fewer kernel boundaries mean fewer re-scheduling events across the whole non-local stream, so kernel fusion improves overlap with local compute well beyond just reducing launch overhead.

## Strategies in a nutshell

The design rests on four ideas:

**Kernel fusion with dependency-aware partitioning**: One fused kernel replaces the per-pulse pack/send/wait cycle, processing all pulses in a single launch. Each pulse’s index map splits into independent atoms (sent immediately) and a dependent tail (waiting only on a fine-grained per-pulse signal), cutting six launches per timestep to one.**Reduced thread-block synchronization**: Notification is fused into the kernel using hierarchical release scopes. A lighter GPU-scope release atomic is performed by every block, while the system-scope cross-GPU release is issued only once per pulse by the final block.**Event-driven, host-free execution**: Cross-kernel dependencies are expressed as GPU-visible signals, so local and non-local pipelines launch back-to-back without`cudaStreamSynchronize`

.**Interconnect-aware transport**: NVLink peers receive direct stores plus a release signal, otherwise, the kernel falls back to`nvshmemx_float_put_signal_nbi_block`

over RDMA interconnects (InfiniBand, Slingshot).

## A leap in scaling performance

[Benchmarking](https://doi.org/10.1145/3731599.3767508) was performed on the NVIDIA Eos supercomputer, a cluster of 576 NVIDIA DGX H100 nodes connected by NVLink 4.0 intra-node and 400 Gb/s InfiniBand NDR inter-node, using water-ethanol mixtures ranging from 45,000 to 23M atoms to represent typical biomolecular workloads.

Intra-node delivered up to 1.5x better performance than GPU-aware MPI, with the largest gains on smaller, latency-bound systems. A 45,000-atom system on four GPUs gained a 46% improvement (1,649 vs. 1,126 ns/day). On NVIDIA GB200 NVL72 multi-node NVLink clusters, the benefit extends to 2x, and on standard InfiniBand clusters to 1.3x.

The one trade-off is that device-initiated communication consumes modest GPU resources, giving traditional MPI a narrow 1–3% edge on very large, compute-bound configurations at low node counts. Across the scaling regimes most relevant to production MD research, however, the new approach wins consistently.

The following figures show simulation performance using MPI and NVSHMEM for an intranode execution on four and 8 GPUs (Figure 3) and multinode execution with four GPUs per node (Figure 4) using achieved simulation length (ns/day) and iteration rate (ms/step) metrics.

## Open and portable solutions in the future

This shows a broader shift in how latency-sensitive HPC applications can approach inter-GPU communication. Applications that scale strongly into microsecond kernel times need a different model than CPU-centric MPI. GPU-initiated communication is a compelling answer. The techniques aren’t specific to molecular dynamics. Halo exchange patterns appear throughout computational science (CFD, astrophysics, lattice QCD), and the approach transfers directly to any application that relies on boundary data exchange between decomposed domains.

A natural next step is lifting these ideas into the broader HPC ecosystem. Distributed data abstractions such as Kokkos Remote Spaces and execution models like std::execution are beginning to encapsulate these patterns behind portable interfaces.

Wider adoption also requires standardization: the GPU-native extensions used here currently fall outside the core OpenSHMEM specification, and formal adoption of device-initiated communication, fine-grained signaling, and direct peer memory access is needed for uniform availability.

The goal is a future where innovations from specialized codes like GROMACS become standard building blocks for any application scaling across heterogeneous hardware. If you run GROMACS, try the GPU-initiated halo exchange in GROMACS 2026 and measure the strong-scaling gains on your own simulations.

To apply the same patterns elsewhere:

- Explore
[NVSHMEM](https://developer.nvidia.com/nvshmem)and look for CPU-orchestrated communication on your critical path. - Read the
[SC’25 workshop paper](https://dl.acm.org/doi/10.1145/3731599.3767508)with the full design and benchmarks.

## Start the discussion at forums.developer.nvidia.com
