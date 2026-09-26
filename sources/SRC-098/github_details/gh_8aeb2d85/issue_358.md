# [Issue #358] A Bug in Gin GDAKI Put?

source: https://github.com/NVIDIA/nccl-tests/issues/358
state: closed | updated: 2025-11-03T15:30:58Z
labels: 

## 正文

I implemented a custom kernel using the GIN API to measure the performance of the `Put` operation:

```c++
template <typename T, typename Coop = ncclCoopWarp>
__global__ void nPing1PongLatKernel(ncclWindow_t sendwin, size_t sendoffset,
                                    ncclWindow_t recvwin, size_t recvoffset,
                                    size_t n, size_t count, int root,
                                    TimingResult *timing_result,
                                    struct ncclDevComm devComm) {
  
  ncclTeam world = ncclTeamWorld(devComm);

  int globalTid = threadIdx.x + blockIdx.x*blockDim.x;
  int globalNthreads = blockDim.x * gridDim.x;

  int globalWid = globalTid / 32;
  int globalNwarps = (globalNthreads+31) / 32;

  if (world.nRanks != 2) return ;

  int ginContext = 0;
  unsigned int signalIndex = 0;

  ncclGin gin { devComm, ginContext };
  uint64_t signalValue = gin.readSignal(signalIndex);
  ncclBarrierSession<ncclCoopCta> bar { ncclCoopCta(), ncclTeamTagWorld(), gin, blockIdx.x };
  bar.sync(ncclCoopCta(), cuda::memory_order_relaxed, ncclGinFenceLevel::Relaxed);

  const size_t size = count * sizeof(T);
  int rank = world.rank, peer = world.rank ^ 1;
  if (rank == root) {
    ncclCoopCta().sync();
    gin.waitSignal(ncclCoopCta(), signalIndex, signalValue + 1);
    signalValue = gin.readSignal(signalIndex);
    printf("rank %d, tid %d: recv signal %lu\n", rank, globalTid, signalValue);
    if (globalTid == 0) {
      timing_result->start_time = globaltimer();
    }
    int i;
    for (i = 0; i < n-1; i ++) {
      gin.put<ncclGin_None, ncclGin_None, Coop>(
        world, peer,
        recvwin, recvoffset + i * size,
        sendwin, sendoffset + i * size,
        size,
        ncclGin_None{},
        ncclGin_None{},
        Coop{}
      );
    }
    gin.put<ncclGin_SignalInc, ncclGin_None, Coop>(
      world, peer,
      recvwin, recvoffset + i * size,
      sendwin, sendoffset + i * size,
      size,
      ncclGin_SignalInc{signalIndex},
      ncclGin_None{},
      Coop{}
    );
    printf("rank %d, tid %d: send %lu data\n", rank, globalTid, n);
    gin.waitSignal(ncclCoopCta(), signalIndex, signalValue + 1);
    signalValue = gin.readSignal(signalIndex);
    printf("rank %d, tid %d: recv signal %lu\n", rank, globalTid, signalValue);
    ncclCoopCta().sync();
    if (globalTid == 0) {
      timing_result->end_time = globaltimer();
    }
  } else {
    gin.put<ncclGin_SignalInc, ncclGin_None, Coop>(
      world, peer,
      recvwin, recvoffset,
      sendwin, sendoffset,
      size,
      ncclGin_SignalInc{signalIndex},
      ncclGin_None{},
      Coop{}
    );
    printf("rank %d, tid %d: put 1 data\n", rank, globalTid);
    gin.waitSignal(ncclCoopCta(), signalIndex, signalValue + 1);
    signalValue = gin.readSignal(signalIndex);
    printf("rank %d, tid %d: recv signal %lu\n", rank, globalTid, signalValue);
    gin.put<ncclGin_SignalInc, ncclGin_None, Coop>(
      world, peer,
      recvwin, recvoffset + size,
      sendwin, sendoffset + size,
      size,
      ncclGin_SignalInc{signalIndex},
      ncclGin_None{},
      Coop{}
    );
    printf("rank %d, tid %d: put 1 data\n", rank, globalTid);
  }
  gin.flush(ncclCoopCta());
  bar.sync(ncclCoopCta(), cuda::memory_order_relaxed, ncclGinFenceLevel::Relaxed);
}
```

However, when I `set NCCL_GIN_TYPE=3` to use `GDAKI`, the kernel hangs during execution. In contrast, it runs correctly when `NCCL_GIN_TYPE=2` is set to use the `Proxy` mode.

The log output during the hang is as follows:

```bash
rank 0, tid 0: recv signal 1
rank 0, tid 1: recv signal 1
rank 0, tid 2: recv signal 1
rank 0, tid 3: recv signal 1
rank 0, tid 4: recv signal 1
rank 0, tid 5: recv signal 1
rank 0, tid 6: recv signal 1
rank 0, tid 7: recv signal 1
rank 0, tid 8: recv signal 1
rank 0, tid 9: recv signal 1
rank 0, tid 10: recv signal 1
rank 0, tid 11: recv signal 1
rank 0, tid 12: recv signal 1
rank 0, tid 13: recv signal 1
rank 0, tid 14: recv signal 1
rank 0, tid 15: recv signal 1
rank 0, tid 16: recv signal 1
rank 0, tid 17: recv signal 1
rank 0, tid 18: recv signal 1
rank 0, tid 19: recv signal 1
rank 0, tid 20: recv signal 1
rank 0, tid 21: recv signal 1
rank 0, tid 22: recv signal 1
rank 0, tid 23: recv signal 1
rank 0, tid 24: recv signal 1
rank 0, tid 25: recv signal 1
rank 0, tid 26: recv signal 1
rank 0, tid 27: recv signal 1
rank 0, tid 28: recv signal 1
rank 0, tid 29: recv signal 1
rank 0, tid 30: recv signal 1
rank 0, tid 31: recv signal 1
rank 0, tid 1: send 5 data
rank 0, tid 2: send 5 data
rank 0, tid 3: send 5 data
rank 0, tid 4: send 5 data
rank 0, tid 5: send 5 data
rank 0, tid 6: send 5 data
rank 0, tid 7: send 5 data
rank 0, tid 8: send 5 data
rank 0, tid 9: send 5 data
rank 0, tid 10: send 5 data
rank 0, tid 11: send 5 data
rank 0, tid 12: send 5 data
rank 0, tid 13: send 5 data
rank 0, tid 14: send 5 data
rank 0, tid 15: send 5 data
rank 0, tid 16: send 5 data
rank 0, tid 17: send 5 data
rank 0, tid 18: send 5 data
rank 0, tid 19: send 5 data
rank 0, tid 20: send 5 data
rank 0, tid 21: send 5 data
rank 0, tid 22: send 5 data
rank 0, tid 23: send 5 data
rank 0, tid 24: send 5 data
rank 0, tid 25: send 5 data
rank 0, tid 26: send 5 data
rank 0, tid 27: send 5 data
rank 0, tid 28: send 5 data
rank 0, tid 29: send 5 data
rank 0, tid 30: send 5 data
rank 0, tid 31: send 5 data
rank 1, tid 1: put 1 data
rank 1, tid 2: put 1 data
rank 1, tid 3: put 1 data
rank 1, tid 4: put 1 data
rank 1, tid 5: put 1 data
rank 1, tid 6: put 1 data
rank 1, tid 7: put 1 data
rank 1, tid 8: put 1 data
rank 1, tid 9: put 1 data
rank 1, tid 10: put 1 data
rank 1, tid 11: put 1 data
rank 1, tid 12: put 1 data
rank 1, tid 13: put 1 data
rank 1, tid 14: put 1 data
rank 1, tid 15: put 1 data
rank 1, tid 16: put 1 data
rank 1, tid 17: put 1 data
rank 1, tid 18: put 1 data
rank 1, tid 19: put 1 data
rank 1, tid 20: put 1 data
rank 1, tid 21: put 1 data
rank 1, tid 22: put 1 data
rank 1, tid 23: put 1 data
rank 1, tid 24: put 1 data
rank 1, tid 25: put 1 data
rank 1, tid 26: put 1 data
rank 1, tid 27: put 1 data
rank 1, tid 28: put 1 data
rank 1, tid 29: put 1 data
rank 1, tid 30: put 1 data
rank 1, tid 31: put 1 data
```

Notably, the log from `tid 0` is missing.

In addition, when I set `Coop` to `ncclCoopThread` and modify the kernel so that only `tid=0` issues the `Put` operation (consistent with the latest nccl-tests implementation of `ginAllToAll`), the kernel runs normally.

Below is the complete host-side kernel launch code. In short, the kernel is launched with `grid_dim=1` and `block_dim=32`:

```c++
/*************************************************************************
 * Copyright (c) 2025, NVIDIA CORPORATION. All rights reserved.
 *
 * See LICENSE.txt for license information
 ************************************************************************/

#include "cuda_runtime.h"
#include "nccl.h"
#include "nccl_device.h"
#include "utils.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>

/*
 * NCCL Device GIN API Profile Example
 */

// Device API kernel launch configuration
// CTA count must match lsaBarrierCount for proper barrier synchronization
#define NCCL_DEVICE_CTA_COUNT 1
#define NCCL_DEVICE_THREADS_PER_CTA 32

// ==========================================================================
// Device Kernel Implementation
// ==========================================================================
__device__ __forceinline__ unsigned long long int globaltimer() {
  unsigned long long int timer;
  asm volatile("mov.u64 %0, %%globaltimer;" : "=l"(timer));
  return timer;
}
struct TimingResult {
  unsigned long long int start_time;
  unsigned long long int end_time;
};

template <typename T, typename Coop = ncclCoopWarp>
__global__ void nPing1PongLatKernel(ncclWindow_t sendwin, size_t sendoffset,
                                    ncclWindow_t recvwin, size_t recvoffset,
                                    size_t n, size_t count, int root,
                                    TimingResult *timing_result,
                                    struct ncclDevComm devComm) {
  
  ncclTeam world = ncclTeamWorld(devComm);

  int globalTid = threadIdx.x + blockIdx.x*blockDim.x;
  int globalNthreads = blockDim.x * gridDim.x;

  int globalWid = globalTid / 32;
  int globalNwarps = (globalNthreads+31) / 32;

  if (world.nRanks != 2) return ;

  int ginContext = 0;
  unsigned int signalIndex = 0;

  ncclGin gin { devComm, ginContext };
  uint64_t signalValue = gin.readSignal(signalIndex);
  ncclBarrierSession<ncclCoopCta> bar { ncclCoopCta(), ncclTeamTagWorld(), gin, blockIdx.x };
  bar.sync(ncclCoopCta(), cuda::memory_order_relaxed, ncclGinFenceLevel::Relaxed);

  const size_t size = count * sizeof(T);
  int rank = world.rank, peer = world.rank ^ 1;
  if (rank == root) {
    ncclCoopCta().sync();
    gin.waitSignal(ncclCoopCta(), signalIndex, signalValue + 1);
    signalValue = gin.readSignal(signalIndex);
    printf("rank %d, tid %d: recv signal %lu\n", rank, globalTid, signalValue);
    if (globalTid == 0) {
      timing_result->start_time = globaltimer();
    }
    int i;
    for (i = 0; i < n-1; i ++) {
      gin.put<ncclGin_None, ncclGin_None, Coop>(
        world, peer,
        recvwin, recvoffset + i * size,
        sendwin, sendoffset + i * size,
        size,
        ncclGin_None{},
        ncclGin_None{},
        Coop{}
      );
    }
    gin.put<ncclGin_SignalInc, ncclGin_None, Coop>(
      world, peer,
      recvwin, recvoffset + i * size,
      sendwin, sendoffset + i * size,
      size,
      ncclGin_SignalInc{signalIndex},
      ncclGin_None{},
      Coop{}
    );
    printf("rank %d, tid %d: send %lu data\n", rank, globalTid, n);
    gin.waitSignal(ncclCoopCta(), signalIndex, signalValue + 1);
    signalValue = gin.readSignal(signalIndex);
    printf("rank %d, tid %d: recv signal %lu\n", rank, globalTid, signalValue);
    ncclCoopCta().sync();
    if (globalTid == 0) {
      timing_result->end_time = globaltimer();
    }
  } else {
    gin.put<ncclGin_SignalInc, ncclGin_None, Coop>(
      world, peer,
      recvwin, recvoffset,
      sendwin, sendoffset,
      size,
      ncclGin_SignalInc{signalIndex},
      ncclGin_None{},
      Coop{}
    );
    printf("rank %d, tid %d: put 1 data\n", rank, globalTid);
    gin.waitSignal(ncclCoopCta(), signalIndex, signalValue + 1);
    signalValue = gin.readSignal(signalIndex);
    printf("rank %d, tid %d: recv signal %lu\n", rank, globalTid, signalValue);
    gin.put<ncclGin_SignalInc, ncclGin_None, Coop>(
      world, peer,
      recvwin, recvoffset + size,
      sendwin, sendoffset + size,
      size,
      ncclGin_SignalInc{signalIndex},
      ncclGin_None{},
      Coop{}
    );
    printf("rank %d, tid %d: put 1 data\n", rank, globalTid);
  }
  gin.flush(ncclCoopCta());
  bar.sync(ncclCoopCta(), cuda::memory_order_relaxed, ncclGinFenceLevel::Relaxed);
}

TimingResult measurePingPongLatency(ncclComm_t comm, ncclDevComm devComm, 
                                   ncclWindow_t send_win, ncclWindow_t recv_win,
                                   size_t n, size_t count, int root, 
                                   cudaStream_t stream) {
  TimingResult* d_timing_result;
  CUDACHECK(cudaMalloc(&d_timing_result, sizeof(TimingResult)));
  
  nPing1PongLatKernel<float><<<NCCL_DEVICE_CTA_COUNT, NCCL_DEVICE_THREADS_PER_CTA, 0, stream>>>(
    send_win, 0, recv_win, 0, n, count, root, d_timing_result, devComm
  );
  
  CUDACHECK(cudaStreamSynchronize(stream));
  
  TimingResult h_timing_result;
  CUDACHECK(cudaMemcpy(&h_timing_result, d_timing_result, sizeof(TimingResult), cudaMemcpyDeviceToHost));
  
  CUDACHECK(cudaFree(d_timing_result));
  
  return h_timing_result;
}

// ==========================================================================
// Host-Side Setup and Device API Initialization
// ==========================================================================

// This function can be called inside an MPI rank or pthread thread. The
// initialization and broadcast are implemented in common/src/utils.cc for
// easier readability. For fully integrated examples using pthreads or MPI see
// examples. in 01_communicators.

void* test(int my_rank, int total_ranks, int local_device, int devices_per_rank, size_t n, size_t count) {
  ncclComm_t comm;
  ncclUniqueId nccl_unique_id;

  if (my_rank == 0) {
    printf("Starting Device API Test initialization\n");
  }


  // Standard NCCL communicator initialization (same as Host API)
  if (my_rank == 0) {
    NCCLCHECK(ncclGetUniqueId(&nccl_unique_id));
  }

  // Distribute unique ID in case of MPI.
  util_broadcast(0, my_rank, &nccl_unique_id);

  // Set device context for this rank
  CUDACHECK(cudaSetDevice(local_device));
  printf("  Rank %d using GPU device %d\n", my_rank, local_device);

  // ==========================================================================
  // STEP 2: Initialize NCCL Communicator and Allocate Memory
  // ==========================================================================

  // Initialize NCCL communicator (same as Host API)
  NCCLCHECK(ncclCommInitRank(&comm, total_ranks, nccl_unique_id, my_rank));
  printf("  Rank %d initialized NCCL communicator for %d total ranks\n", my_rank, total_ranks);

  // Allocate memory for AlltoAll operation
  // n and count are now passed as parameters from command line
  size_t size_bytes = n * count * sizeof(float);

  void* d_sendbuff;
  void* d_recvbuff;
  ncclWindow_t send_win;
  ncclWindow_t recv_win;

  // Device API requires allocation compatible with symmetric memory allocation
  // This ensures memory can be accessed directly by device kernels from all ranks
  NCCLCHECK(ncclMemAlloc(&d_sendbuff, size_bytes));
  NCCLCHECK(ncclMemAlloc(&d_recvbuff, size_bytes));

  // ==========================================================================
  // STEP 4: Register Memory Windows for Device-Side Access
  // ==========================================================================

  // Register symmetric windows for GIN access
  // Windows enable direct peer-to-peer access from device kernels
  NCCLCHECK(ncclCommWindowRegister(comm, d_sendbuff, size_bytes, &send_win, NCCL_WIN_DEFAULT));
  NCCLCHECK(ncclCommWindowRegister(comm, d_recvbuff, size_bytes, &recv_win, NCCL_WIN_DEFAULT));

  // ==========================================================================
  // STEP 5: Create Device Communicator and Configure LSA Barriers
  // ==========================================================================

  // Create stream for kernel execution
  cudaStream_t stream;
  CUDACHECK(cudaStreamCreate(&stream));

  // Create device communicator - this is the key Device API component
  // Requirements specify resources to allocate (e.g., one barrier per CTA)
  ncclDevComm devComm;
  ncclDevCommRequirements reqs;
  memset(&reqs, 0, sizeof(reqs));
  reqs.barrierCount = NCCL_DEVICE_CTA_COUNT;
  reqs.ginSignalCount = NCCL_DEVICE_CTA_COUNT;
  NCCLCHECK(ncclDevCommCreate(comm, &reqs, &devComm));
  printf("  Rank %d created device communicator with %d barriers and ginSignals\n", my_rank, NCCL_DEVICE_CTA_COUNT);

  // ==========================================================================
  // STEP 6: Launch Device Kernel for Ping-Pong Operation
  // ==========================================================================

  printf("  Rank %d launching ping-pong kernel...\n", my_rank);
  
  TimingResult timing_result = measurePingPongLatency(comm, devComm, send_win, recv_win, n, count, 0, stream);
  
  printf("  Rank %d completed nPing1PongLatKernel kernel execution\n", my_rank);
  
  if (my_rank == 0) {
    double latency_ns = (double)(timing_result.end_time - timing_result.start_time);
    printf("  Ping-Pong Latency: %.2f ns (%.2f us)\n", latency_ns, latency_ns / 1000.0);
    printf("  Start time: %llu, End time: %llu\n", timing_result.start_time, timing_result.end_time);
  }

  // ==========================================================================
  // STEP 7: Verify Results and Cleanup Resources
  // ==========================================================================

  if (my_rank == 0) {
    printf("Ping-Pong latency test completed successfully\n");
  }

  // Device API specific cleanup
  NCCLCHECK(ncclDevCommDestroy(comm, &devComm));
  NCCLCHECK(ncclCommWindowDeregister(comm, send_win));
  NCCLCHECK(ncclCommWindowDeregister(comm, recv_win));
  NCCLCHECK(ncclMemFree(d_sendbuff));
  NCCLCHECK(ncclMemFree(d_recvbuff));

  // Standard NCCL cleanup
  CUDACHECK(cudaStreamDestroy(stream));
  NCCLCHECK(ncclCommFinalize(comm));
  NCCLCHECK(ncclCommDestroy(comm));

  return NULL;
}

void* test_wrapper(int my_rank, int total_ranks, int local_device, int devices_per_rank) {
  extern size_t g_n, g_count;
  return test(my_rank, total_ranks, local_device, devices_per_rank, g_n, g_count);
}

size_t g_n = 100; 
size_t g_count = 1024; 

int main(int argc, char* argv[]) {
  if (argc >= 3) {
    g_n = (size_t)atoi(argv[1]);
    g_count = (size_t)atoi(argv[2]);
  } else if (argc == 2) {
    printf("Usage: %s <n> <count>\n", argv[0]);
    printf("Using default values: n=%zu, count=%zu\n", g_n, g_count);
  }
  
  printf("Running with n=%zu, count=%zu\n", g_n, g_count);
  
  // Run example using the provided utility framework
  return run_example(argc, argv, test_wrapper);
}
```

## 评论 (1)

### jywangx · 2025-11-03

Sorry, I just realized this issue was filed in the wrong repository.🫨
I’ll close it here and re-open it in the main NCCL repo.

Issue in NCCL repo here: https://github.com/NVIDIA/nccl/issues/1893
