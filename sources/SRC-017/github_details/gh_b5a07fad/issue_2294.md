# [Issue #2294] [RFE]: Discuss per-peer P2P buffer merge to reduce NCCL communicator init time

source: https://github.com/NVIDIA/nccl/issues/2294
state: open | updated: 2026-08-28T03:20:42Z
labels: enhancement

## 正文

### Please provide the below details to ensure we understand your needs


## Motivation

I would like to discuss whether NCCL P2P transport can reduce communicator
initialization overhead by merging per-channel P2P shareable buffers for the
same peer and direction.

The buffer discussed here is the P2P shareable GPU buffer allocated by
`ncclP2pAllocateShareableBuffer` and exported/imported through IPC during
`ncclTransportP2pSetup`.

Today, P2P transport allocates one shareable buffer per channel per peer. Each
allocation may trigger a separate IPC export/import path. At a high level, this 
makes communicator initialization scale with `nChannels * nPeers` for these 
per-channel P2P resources. For one peer and one direction, the relevant IPC 
work scales with `nChannels`.

On systems with many channels, this becomes a noticeable part of communicator
initialization time, especially on the non-cuMem IPC path.

## Proposed direction

The idea is to merge all per-channel buffers for the same peer and direction
into a single contiguous allocation, then slice that allocation by channel:

- **Allocation side**: allocate one buffer with
  `totalSize = perChannelSize * nChannels` for the peer/direction, then compute
  each channel slice with `offset = perChannelSize * channelIndex`.
- **Import side**: import the base allocation once, cache the base pointer, and
  let subsequent channels use `base + offset` instead of reopening the same
  peer/direction allocation per channel.
- **Free side**: keep reference counting so the merged allocation is released
  only after all channel slices using it have been released.

This would reduce IPC export/import/close work from `O(nChannels)` to `O(1)`
for each peer/direction, while preserving per-channel buffer layout through
explicit offsets.

This design direction does not modify NVLS. It only applies a similar
"one larger allocation plus per-channel slicing" layout to P2P transport.

## Prototype status

I have a local prototype for this idea, but I am opening this as an issue first
to check whether the NCCL maintainers consider this direction acceptable before
turning it into a PR.

The prototype is intended to be limited to P2P transport. It does not add or
change any public API.

Important correctness constraints for a production change would include:

- preserving the existing send/recv direction separation;
- preserving existing IPC reference-count semantics, including cases where one
  exported P2P buffer can be imported by more than one peer;
- handling partial setup failure and cleanup without leaking the merged buffer;
- keeping the cuMem and non-cuMem paths behaviorally equivalent except for the
  allocation/import granularity.

## Benchmark methodology

Benchmark script: `bench_nccl_init.py`

The script is a self-contained Python benchmark using PyTorch only for process
management, CUDA tensors, and gloo bootstrap. It directly calls NCCL APIs through
ctypes.

For each round, each process does the following:

1. rank 0 creates an `ncclUniqueId` and broadcasts it to all ranks through gloo;
2. each rank calls `ncclCommInitRank` to create one or more NCCL communicators;
3. the script measures the elapsed time for the serial communicator creation
   phase;
4. it runs a small functional AllReduce warmup on each communicator;
5. it benchmarks AllReduce on a 32 MiB float32 tensor;
6. it aborts the communicators and starts the next round.

The reported init time is therefore the elapsed time for serial communicator
creation in the script, including the per-communicator unique ID generation and
gloo broadcast, followed by `ncclCommInitRank`. The same benchmark path is used
for both baseline and prototype runs, so the comparison is still useful for the
relative baseline/prototype result, but it should not be interpreted as a pure isolated
measurement of only the internal `ncclCommInitRank` implementation.

The AllReduce measurement uses 5 warmup iterations and 20 measured iterations
per communicator, with an 8M-element float32 tensor.

The main command shape was:

```bash
NCCL_CUMEM_ENABLE=<0 or 1> \
NCCL_MIN_NCHANNELS=4 \
NCCL_SOCKET_IFNAME=lo \
NCCL_DEBUG=INFO \
python bench_nccl_init.py --world-size 8 --rounds 10 --num-comms <1|2|3>
```

`NCCL_SOCKET_IFNAME=lo` is used only to make the single-node bootstrap interface
stable. The measured data path is still P2P/IPC.

## Environment

- GPU: 8x NVIDIA H20 (Hopper, cc 9.0, 96GB HBM3)
- Topology: NVLink fully connected mesh, 18 links per pair (NV18), ~478 GB/s per pair
- CPU: Intel Xeon, 96 cores, 1 socket
- Memory: 503 GB
- OS: Ubuntu 24.04.1 LTS, kernel 5.10.134
- CUDA: 12.8 (V12.8.93)
- Driver: 550.54.15
- PyTorch: 2.7.0a0+7c8ec84dab.nv25.03
- NCCL baseline: 2.27.3
- Local experiment: NCCL 2.27.3 with a prototype per-peer P2P buffer merge change
- NCCL env: `NCCL_MIN_NCHANNELS=4`, `NCCL_SOCKET_IFNAME=lo`, `NCCL_DEBUG=INFO`
- Channels: 24, confirmed from NCCL INFO logs
- NVLS: available on the system, but not used for the measured data path on H20
- Benchmark: `bench_nccl_init.py --world-size 8 --rounds 10 --num-comms <1|2|3>`

## Results with `NCCL_CUMEM_ENABLE=0`

### Communicator creation time, rank 0 median

| Communicators per round | Baseline | Local prototype | Change |
|:---:|---:|---:|---:|
| 1 | 1893.40 ms | 991.48 ms | **-47.6%** |
| 2 | 3660.51 ms | 1897.33 ms | **-48.2%** |
| 3 | 5464.44 ms | 2791.52 ms | **-48.9%** |

Per-communicator time, approximated as median divided by the number of
communicators, is reduced from about 1893 ms to about 950 ms.

### AllReduce latency and bandwidth

| Communicators per round | Baseline AR | Prototype AR | Baseline BW | Prototype BW |
|:---:|---:|---:|---:|---:|
| 1 | 0.200 ms | 0.200 ms | 167.37 GB/s | 167.42 GB/s |
| 2 | 0.201 ms | 0.202 ms | 167.35 GB/s | 166.07 GB/s |
| 3 | 0.201 ms | 0.202 ms | 166.69 GB/s | 166.55 GB/s |

AllReduce latency and bandwidth are within measurement noise in this test.

### Cross-rank consistency for 3 communicators per round

| Rank | Baseline init_avg | Prototype init_avg | Change |
|---:|---:|---:|---:|
| 0 | 5607.00 ms | 2920.99 ms | -47.9% |
| 1 | 5622.19 ms | 2935.76 ms | -47.8% |
| 2 | 5622.19 ms | 2935.76 ms | -47.8% |
| 3 | 5622.19 ms | 2935.76 ms | -47.8% |
| 4 | 5622.20 ms | 2935.74 ms | -47.8% |
| 5 | 5622.20 ms | 2935.77 ms | -47.8% |
| 6 | 5622.19 ms | 2935.75 ms | -47.8% |
| 7 | 5622.19 ms | 2935.77 ms | -47.8% |

The reduction is consistent across all ranks in this run.

## Results with `NCCL_CUMEM_ENABLE=1`

In the same test environment, the cuMem path already has much lower communicator
creation time than the non-cuMem path. The prototype is neutral within
measurement noise for this path.

### Communicator creation time, rank 0 median

| Communicators per round | Baseline | Local prototype | Change |
|:---:|---:|---:|---:|
| 1 | 840.20 ms | 845.87 ms | +0.7% |
| 2 | 1605.18 ms | 1594.43 ms | -0.7% |
| 3 | 2361.10 ms | 2351.04 ms | -0.4% |

Per-communicator time, approximated as median divided by the number of
communicators, is essentially unchanged at about 840 ms.

### AllReduce latency and bandwidth

| Communicators per round | Baseline AR | Prototype AR | Baseline BW | Prototype BW |
|:---:|---:|---:|---:|---:|
| 1 | 0.201 ms | 0.201 ms | 166.81 GB/s | 166.90 GB/s |
| 2 | 0.200 ms | 0.200 ms | 167.67 GB/s | 167.80 GB/s |
| 3 | 0.201 ms | 0.201 ms | 167.23 GB/s | 167.03 GB/s |

No AllReduce regression was observed in this test.

## Summary

| Path | Baseline per-communicator time | Prototype per-communicator time | Change |
|:---|---:|---:|---:|
| `NCCL_CUMEM_ENABLE=0` | ~1830-1890 ms | ~950 ms | **~48% lower** |
| `NCCL_CUMEM_ENABLE=1` | ~840 ms | ~840 ms | neutral |

The largest benefit appears on the non-cuMem path, where repeated per-channel
IPC open/close work is relatively expensive. In this environment, the cuMem path
is already faster and the prototype does not materially change it.

## Next step

I would like to confirm whether this per-peer/per-direction merged P2P buffer
layout is an acceptable direction for NCCL. If so, I can prepare a PR with the
prototype and include additional NCCL INFO logs, cleanup-path validation, and
any extra tests requested by maintainers.

Any feedback or suggestions would be greatly appreciated.


## 评论 (5)

### xiaofanl-nvidia · 2026-07-19

A couple of comments from me - 
1. The result shows most benefit with CUMEM disabled, and no benefit with CUMEM enabled, any idea why? 
This could be concerning (for this RFE) because we generally consider the CUMEM disabled path as legacy and it might be up for removal one day, so we may not spend a lot of efforts optimizing it. Is there any use case where you must disable CUMEM? 
2. Does this RFE also have any benefit for saving memory overhead? 
3. The init time benchmark bench_nccl_init.py is a great idea. However, we have an internal version of this similar to nccl-tests. We are currently considering open-sourcing that. 

++ @sjeaugey @justus-nv to take a look as well in case there is overlap with recent discussions on memory overhead saving. 

 

### sjeaugey · 2026-07-20

We've been investigating using a per-channel, shared buffer for P2P operations like we have for NET operations (even fusing the two), at least for NVLS and alltoall operations which require all-to-all connections, which uses a lot of memory.

I believe this is doable and it would reduce the memory usage by a lot. It may also incur some extra latency for the simple protocol, although it's not clear how much. I think that approach would have a much higher overall impact while also reducing the number of segments we import/export from O(nranks) to O(1).

### xiaoguoer · 2026-07-20

Thanks for the comments, @xiaofanl-nvidia . 

We do not have a requirement to disable CUMEM. In our use case, we cannot change the customer's runtime/data-path configuration just to optimize communicator initialization. We have observed some environments where CUMEM is disabled, and in production, NCCL_CUMEM_ENABLE may already be fixed by platform policy, compatibility validation, or existing deployment settings, so we need to work with either mode.

My understanding is that the visible benefit mainly comes from removing legacy CUDA IPC open/close amplification. With CUMEM disabled, each per-channel P2P buffer goes through cudaIpcGetMemHandle, cudaIpcOpenMemHandle, and later cudaIpcCloseMemHandle. The merge reduces those operations from per-channel to once per peer/direction.

With CUMEM enabled, the path uses cuMemImportFromShareableHandle plus VMM reserve/map/access operations. My understanding is that access setup is the most expensive part among those VMM operations, and its cost is related to the memory footprint being mapped/accessed. Since the per-peer merge does not reduce the total logical buffer size or memory footprint, the total time is not expected to change much in this path.

For memory overhead, I would frame this as an initialization/control-plane optimization first. The prototype keeps the same per-channel logical buffer slices and only changes the allocation/import granularity, so the immediate benefit is lower initialization overhead. That said, if the community sees value in reducing the memory overhead as well, we would be happy to explore that direction — for example, by rethinking how the merged buffers are partitioned or shared across channels.


### xiaofanl-nvidia · 2026-08-10

@xiaoguoer - Thanks for the extra info. I have an understanding of the expected benefits for this RFE now. 
As I mentioned, we don't want to put in a lot of complexity to optimize CUMEM-disabled path at this point, because many other features in NCCL depends on CUMEM functionality. 

However, if this is a simple/trivial change that can make the CUMEM-disabled path better without adding too much maintenance burden on NCCL, we can consider upstreaming it. If you'd like to raise a PR, we're happy to consider it! 

In the next couple of releases, we will optimize memory overhead so that you could need general improvements in overhead and perhaps init time as well. 

### xiaoguoer · 2026-08-28

@xiaofanl-nvidia Thanks for the reply!

Understood. I'll keep the PR strictly simple and low-maintenance: no new
public API or tunables, changes limited to P2P connection setup/teardown
(one larger allocation + per-channel slicing via offsets), existing IPC
semantics preserved.
