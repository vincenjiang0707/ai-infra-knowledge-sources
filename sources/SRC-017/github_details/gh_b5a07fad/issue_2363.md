# [Issue #2363] [Issue]: Single-rank communicator initializes a large NET shared P2P buffer

source: https://github.com/NVIDIA/nccl/issues/2363
state: open | updated: 2026-08-23T20:30:52Z
labels: 

## 正文

### Impact

A single-rank NCCL communicator initializes a large NET shared P2P GPU buffer even though it has no remote peer. In a model serving process where communicators are initialized lazily, the first collective on such a group can fail at request time when GPU memory is already heavily utilized.

This caused an application crash in our workload:

```text
ncclUnhandledCudaError
Failed to CUDA calloc 536870912 bytes
```

### Environment

- NCCL 2.28.9
- PyTorch 2.11.0 + CUDA 13.0
- 8x NVIDIA B300, single node / all-NVLink topology
- Containerized deployment
- No `NCCL_BUFFSIZE`, `NCCL_P2P_NVL_CHUNKSIZE`, or `NCCL_CUMEM_ENABLE` override in the natural observation

### Minimal reproducer

Run with `NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,GRAPH,COLL,ALLOC torchrun --standalone --nproc-per-node=8 repro.py`:

```python
import os

import torch
import torch.distributed as dist

dist.init_process_group("nccl")
rank = dist.get_rank()
world_size = dist.get_world_size()
local_rank = int(os.environ["LOCAL_RANK"])
torch.cuda.set_device(local_rank)

# All ranks create all groups in the same order. Each process then uses its
# own singleton NCCL group.
groups = [dist.new_group([r], backend="nccl") for r in range(world_size)]

x = torch.zeros(1, device=f"cuda:{local_rank}")
dist.all_reduce(x, group=groups[rank])
torch.cuda.synchronize()
```

On the affected topology, the first collective on the singleton group logs:

```text
ncclCommInitRankConfig ... rank 0 nranks 1 ... Init START
P2P Chunksize set to 524288
transport/net.cc:656 Cuda Alloc Size 536870912
64 coll channels, 64 collnet channels, 0 nvls channels,
64 p2p channels, 64 p2p channels per peer
ncclCommInitRankConfig ... rank 0 nranks 1 ... Init COMPLETE
AllReduce ... count 1 ... [nranks=1]
```

The allocation happens before the count-one all-reduce. With sufficient free memory it succeeds; with less than 512 MiB allocatable memory it fails during communicator initialization.

### Source-level size calculation

In NCCL 2.28.9, the allocation comes from `sharedNetBuffersInit()` in `src/transport/net.cc`:

```cpp
#define NCCL_SHARED_STEPS 16
state->size = nChannels * NCCL_SHARED_STEPS * proxyState->p2pChunkSize;
...
ncclCudaCalloc(&state->cudaBuff, state->size);
```

For the observed topology:

```text
64 channels * 16 shared steps * 524288 bytes = 536870912 bytes
```

The call is reached through the unconditional local NET proxy shared initialization in communicator setup:

```text
ncclProxyMsgSharedInit -> proxySharedInit -> sharedNetBuffersInit
```

Ring/tree connection setup already has `nRanks > 1` guards, but the NET proxy shared initialization is still performed for `nranks=1`.

### Expected behavior

A communicator whose fixed size is one cannot communicate with a remote rank; all of its collectives have local identity semantics. Could NCCL skip NET/P2P proxy shared-buffer initialization for `nranks <= 1`, or otherwise provide a low-memory singleton fast path?

The exact allocation size is topology-dependent. The issue is the unnecessary transport initialization for a communicator that can only execute single-rank operations, not specifically the 512 MiB value.

## 评论 (2)

### wanna-01 · 2026-08-21

Additional source evidence and scope clarification:

- `ncclTransportP2pConnect()` already skips connectors when `peer == comm->rank`.
- The P2P enqueue path detects a self-send and sets `nProxyOps = 0`; an in-place matching self send/recv is skipped entirely.
- Therefore a singleton communicator has no remote NET/P2P data path that can consume the preallocated shared pool.

The ring/tree `nRanks > 1` guards are supporting evidence, not a claim that the same guard can be copied mechanically. The narrow optimization request is to skip the singleton communicator's NET shared-buffer/preconnect allocation. It is not to disable the entire proxy subsystem. Split communicators with shared resources, cleanup/refcount handling, RMA, plugins, and matching self send/recv should remain covered by NCCL's regression tests when choosing the exact guard placement.

### xiaofanl-nvidia · 2026-08-23

Thanks for the report and PR. I will need to assign some resources to optimize NCCL's resource consumption overhead in general. 
We'll review your PR and take it in if it's aligned with how we plan to tackle this general issue. 
