# [Issue #2057] [Issue]: Single-node 2-GPU ncclSend/ncclRecv fails with internal error when P2P and SHM are disabled: NET/Socket receives AF_UNIX address

source: https://github.com/NVIDIA/nccl/issues/2057
state: open | updated: 2026-09-11T07:05:34Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

_No response_

### Steps to Reproduce the Issue

## Environment

- NCCL version: `2.29.2+cuda12.8`
- NCCL git version: `master be4d833-dirty`
- CUDA driver version: `12080`
- OS: `Ubuntu`
- GPUs: `2 GPUs on a single node`
- Network backend: `Socket`
- Run mode: `2 ranks launched separately on the same node`

---

## 1. Summary

I hit an internal NCCL error in a single-node 2-GPU `ncclSend/ncclRecv` test when both P2P and SHM are disabled.

NCCL appears to fall back to `NET/Socket` as expected, but the `NET/Socket` path then receives an address with family `1` (`AF_UNIX`), and `ncclSocketInit` rejects it because it only supports `AF_INET` / `AF_INET6`:

```text
misc/socket.cc:537 NCCL WARN ncclSocketInit: connecting to address  with family 1 is neither AF_INET(2) nor AF_INET6(10)
```

This eventually results in:

```text
internal error - please report this issue to the NCCL developers
```

This looks like a local/shared-node address is being passed into the `NET/Socket` transport path in this configuration.


## 2. Source code reproducer

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <nccl.h>
#include <cuda_runtime.h>

#define CHECK_CUDA(cmd) do { cudaError_t e = (cmd); if (e != cudaSuccess) { \
    fprintf(stderr,"CUDA error %s:%d: %s\n", __FILE__, __LINE__, cudaGetErrorString(e)); \
    exit(EXIT_FAILURE);} \
} while(0)

#define CHECK_NCCL(cmd) do { ncclResult_t r = (cmd); if (r != ncclSuccess) { \
    fprintf(stderr,"NCCL error %s:%d: %s\n", __FILE__, __LINE__, ncclGetErrorString(r));  \
    exit(EXIT_FAILURE);} \
} while(0)

int main(int argc, char* argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <rank>\n", argv[0]);
        return EXIT_FAILURE;
    }
    int rank = atoi(argv[1]);
    int nranks = 2; // 2 gpu

    CHECK_CUDA(cudaSetDevice(rank));

    ncclUniqueId id;
    CHECK_NCCL(ncclGetUniqueId(&id));
    ncclComm_t comm;
    if (rank == 0) printf("Initializing NCCL across %d nodes...\n", nranks);
    CHECK_NCCL(ncclCommInitRank(&comm, nranks, id, rank));

    size_t total_size_bytes = 1ULL * 1024 * 1024 * 1024;
    size_t element_count = total_size_bytes / sizeof(float);
    float *d_sendbuff = nullptr;
    float *d_recvbuff = nullptr;
    CHECK_CUDA(cudaMalloc(&d_sendbuff, total_size_bytes));
    CHECK_CUDA(cudaMalloc(&d_recvbuff, total_size_bytes));

    cudaStream_t stream;
    CHECK_CUDA(cudaStreamCreate(&stream));
    printf("Starting send/recv...\n");

    // (Rank 0 <-> Rank 1)
    // CHECK_NCCL(ncclGroupStart()); // NOTE: without nccl group
    if (rank == 0) {
        CHECK_NCCL(ncclSend(d_sendbuff, element_count, ncclFloat, 1, comm, stream));
        CHECK_NCCL(ncclRecv(d_recvbuff, element_count, ncclFloat, 1, comm, stream));
    } else {
        CHECK_NCCL(ncclSend(d_sendbuff, element_count, ncclFloat, 0, comm, stream));
        CHECK_NCCL(ncclRecv(d_recvbuff, element_count, ncclFloat, 0, comm, stream));
    }
    // CHECK_NCCL(ncclGroupEnd());
    CHECK_CUDA(cudaStreamSynchronize(stream));
    printf("Done send/recv\n");

    CHECK_CUDA(cudaFree(d_sendbuff));
    CHECK_CUDA(cudaFree(d_recvbuff));
    CHECK_CUDA(cudaStreamDestroy(stream));
    CHECK_NCCL(ncclCommDestroy(comm));
    return 0;
}
```


## 3. How I run it

I launch 2 ranks on the same node, each with the same `NCCL_COMM_ID`.

Example command for rank 0:

```bash
NCCL_P2P_DISABLE=1 \
NCCL_SHM_DISABLE=1 \
NCCL_COMM_ID=172.17.16.64:23456 \
NCCL_DEBUG=INFO \
./a.out 0
```

Rank 1 is launched similarly with:

```bash
NCCL_P2P_DISABLE=1 \
NCCL_SHM_DISABLE=1 \
NCCL_COMM_ID=172.17.16.64:23456 \
NCCL_DEBUG=INFO \
./a.out 1
```



## 4. Full log

```text
ubuntu@VM-16-64-ubuntu:~$ NCCL_P2P_DISABLE=1 NCCL_SHM_DISABLE=1 NCCL_COMM_ID=172.17.16.64:23456 NCCL_DEBUG=INFO ./a.out 0
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO ENV/Plugin: Could not find: libnccl-env.so
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Bootstrap: Using eth0:172.17.16.64<0>
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NCCL_COMM_ID set by environment to 172.17.16.64:23456
Initializing NCCL across 2 nodes...
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO cudaDriverVersion 12080
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NCCL version 2.29.2+cuda12.8
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NCCL git version master be4d833-dirty
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NCCL_COMM_ID set by environment to 172.17.16.64:23456
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NET/Plugin: Could not find: libnccl-net.so
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NCCL_COMM_ID set by environment to 172.17.16.64:23456
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NET/IB : No device found.
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NET/IB : Using [RO]; OOB eth0:172.17.16.64<0>
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Failed to initialize NET plugin IB
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NCCL_COMM_ID set by environment to 172.17.16.64:23456
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NET/Socket : Using [0]eth0:172.17.16.64<0>
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Initialized NET plugin Socket
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Assigned NET plugin Socket to comm
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Using network Socket
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO [Rank 0] ncclCommInitRank comm 0x55eb22a04a50 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 80 commId 0x2ef13c5ed0553a05 - Init START
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO RAS client listening socket at 127.0.0.1<28028>
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Bootstrap timings total 1.927735 (create 0.000034, send 0.000107, recv 1.927205, ring 0.000036, delay 0.000000)
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NCCL_P2P_DISABLE set by environment to 1
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO NCCL_SHM_DISABLE set by environment to 1.
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO ncclTopoGetCpuAffinity: Affinity for GPU 0 is empty, ignoring. (GPU affinity =  ; CPU affinity = 0-19).
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO comm 0x55eb22a04a50 rank 0 nRanks 2 nNodes 2 localRanks 1 localRank 0 MNNVL 0
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Channel 00/02 : 0 1
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Channel 01/02 : 0 1
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Trees [0] 1/-1/-1->0->-1 [1] -1/-1/-1->0->1
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO P2P Chunksize set to 131072
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO PROFILER/Plugin: Could not find: libnccl-profiler.so
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Check P2P Type isAllDirectP2p 1 directMode 0 isAllCudaP2p 1
VM-16-64-ubuntu:28471:28499 [0] NCCL INFO [Proxy Service] Device 0 CPU core 19
VM-16-64-ubuntu:28471:28502 [0] NCCL INFO [Proxy Service UDS] Device 0 CPU core 0
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO TUNER/Plugin: Could not find: libnccl-tuner.so
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO threadThresholds 8/8/64 | 16/8/64 | 512 | 512
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO 2 coll channels, 2 collnet channels, 0 nvls channels, 2 p2p channels, 1 p2p channels per peer
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Symmetric memory is not supported. cuMemEnable 1, ginSupport 0, globalNicFused 1
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO CC Off, workFifoBytes 1048576
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO ncclCommInitRank comm 0x55eb22a04a50 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 80 commId 0x2ef13c5ed0553a05 - Init COMPLETE
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Init timings - ncclCommInitRank: rank 0 nranks 2 total 2.13 (kernels 0.17, alloc 0.02, bootstrap 1.93, allgathers 0.00, topo 0.01, graphs 0.00, connections 0.00, rest 0.00)
Starting send/recv...
VM-16-64-ubuntu:28471:28503 [0] NCCL INFO [Proxy Progress] Device 0 CPU core 12
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO Channel 01/1 : 0[0] -> 1[1] [send] via NET/Socket/0/Shared

[2026-03-18 11:13:09] VM-16-64-ubuntu:28471:28499 [0] misc/socket.cc:537 NCCL WARN ncclSocketInit: connecting to address  with family 1 is neither AF_INET(2) nor AF_INET6(10)
VM-16-64-ubuntu:28471:28499 [0] NCCL INFO transport/net_socket.cc:399 -> 3
VM-16-64-ubuntu:28471:28499 [0] NCCL INFO transport/net.cc:860 -> 3
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO transport.cc:212 -> 3
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO group.cc:142 -> 3
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO group.cc:78 -> 3 [Async thread]
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO group.cc:575 -> 3
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO group.cc:781 -> 3
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO enqueue.cc:3014 -> 3
NCCL error a.cu:46: internal error - please report this issue to the NCCL developers
VM-16-64-ubuntu:28471:28471 [0] NCCL INFO ENV/Plugin: Closing env plugin ncclEnvDefault
```

## 5. Expected behavior

I would expect one of the following:

1. NCCL successfully uses `NET/Socket` in this configuration and passes a valid IPv4/IPv6 socket address to the socket transport, or
2. If single-node `P2P_DISABLE=1` + `SHM_DISABLE=1` is not a supported configuration for this path, NCCL should return a clear user-facing error instead of an internal error.


I realize this may not be a common production configuration, but since NCCL reaches the `NET/Socket` path and then fails with `internal error`, I think it would still be useful either to fix the fallback path or return a more explicit unsupported-configuration error.

### NCCL Version

2.29.2+cuda12.8

### Your platform details

_No response_

### Error Message & Behavior

_No response_

## 评论 (2)

### teojgo · 2026-03-18

@liangxs, with the above ordering of operations:

```
    if (rank == 0) {
        CHECK_NCCL(ncclSend(d_sendbuff, element_count, ncclFloat, 1, comm, stream));
        CHECK_NCCL(ncclRecv(d_recvbuff, element_count, ncclFloat, 1, comm, stream));
    } else {
        CHECK_NCCL(ncclSend(d_sendbuff, element_count, ncclFloat, 0, comm, stream));
        CHECK_NCCL(ncclRecv(d_recvbuff, element_count, ncclFloat, 0, comm, stream));
    }
```

NCCL fails because both ranks are performing a Send before the Recv. To make this work, you need to uncomment the `ncclGroupStart()`, `ncclGroupEnd()` or revert the order of operations in one of the ranks, e.g:

```
    if (rank == 0) {
        CHECK_NCCL(ncclSend(d_sendbuff, element_count, ncclFloat, 1, comm, stream));
        CHECK_NCCL(ncclRecv(d_recvbuff, element_count, ncclFloat, 1, comm, stream));
    } else {
        CHECK_NCCL(ncclRecv(d_recvbuff, element_count, ncclFloat, 0, comm, stream));
        CHECK_NCCL(ncclSend(d_sendbuff, element_count, ncclFloat, 0, comm, stream));
    }
```


### ToLiveAndLove · 2026-09-11

I can reproduce the reported `AF_UNIX` / invalid address-family error on both NCCL 2.29.2 and current master, but only with the ungrouped call sequence from the reproducer:

```cpp
ncclSend(...);
ncclRecv(...);
```

When both ranks issue the first `ncclSend`, it immediately ends its implicit group and starts P2P preconnect before either matching receive has been posted. With NET/Socket, rank 0 then reports address family 1 and rank 1 reports family 0; both calls return `ncclInternalError`.

The following controls all pass and transfer the expected values:

- wrap the send and receive in `ncclGroupStart()` / `ncclGroupEnd()`;
- use an ordered ungrouped exchange (rank 0 send/recv, rank 1 recv/send);
- MPI-distributed unique ID and `NCCL_COMM_ID` bootstrap;
- same and different `NCCL_HOSTID` values;
- `NCCL_NET_SHARED_COMMS=1` and `0`.

NCCL's point-to-point documentation states that calls which need to progress concurrently must be grouped, and its sendrecv example groups `ncclSend` and `ncclRecv`:

https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/p2p.html

Changing the reproducer to:

```cpp
ncclGroupStart();
ncclSend(...);
ncclRecv(...);
ncclGroupEnd();
```

resolves the failure on both tested NCCL versions. This therefore appears to be an invalid P2P ordering in the reproducer rather than a NET/Socket fallback defect.
