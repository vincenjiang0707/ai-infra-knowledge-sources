# [Issue #2238] [Issue]: Performance and functional issues when using ncclPutSignal/ncclWaitSignal in Pipeline Parallelism

source: https://github.com/NVIDIA/nccl/issues/2238
state: open | updated: 2026-09-14T12:03:09Z
labels: 

## 正文


# Summary
We explored replacing ncclSend/ncclRecv in ZeroBubble-V Pipeline Parallelism with NCCL's one-sided RMA API. The goal was to eliminate the implicit sender-receiver synchronization in two-sided communication and reduce SM usage to achieve zero-SM P2P transfers.

On the PyTorch side, we used `torch.distributed._symmetric_memory.put_signal / wait_signal` (PyTorch 2.12) as the interface, which wrap `ncclPutSignal/ncclWaitSignal` internally.

We observed a ~2.5% performance improvement with model accuracy preserved. However, we encountered several functional and performance issues during integration, described below.

## Issue 1: CUDA_DEVICE_MAX_CONNECTIONS=1 serializes ncclPutSignal and compute kernels across streams

**Background**

We set `CUDA_DEVICE_MAX_CONNECTIONS=1` to improve compute-communication overlap. With NCCL's RMA API, we observed unexpected serialization: ncclPutSignal and compute kernels are launched on independent streams with no explicit dependencies between them, but compute kernels are blocked until ncclPutSignal completes.

**Root Cause Hypothesis**

We suspect this is caused by ncclPutSignal internally calling cuStreamBatchMemOp, which batches two operations: writing readySeq and waiting on doneSeq. These memory operations appear to block the GPU command processor until the Proxy thread signals completion, preventing kernels on other streams from being scheduled.

**Questions**

- Is this serialization behavior expected under CUDA_DEVICE_MAX_CONNECTIONS=1?

- Is cuStreamBatchMemOp the root cause of this cross-stream serialization?

- Is there a recommended workaround to preserve compute-communication overlap?

## Issue 2: Decoupling the two operations in cuStreamBatchMemOp

**Background**

In PP inter-stage communication, ncclPutSignal currently batches two operations into a single cuStreamBatchMemOp call:

- Write `readySeq` to notify the Proxy thread to start the data transfer.

- Wait on `doneSeq` to confirm the transfer is complete before the send buffer can be reused.

A more natural pattern for pipeline parallelism would be to decouple these two operations:

- Write readySeq immediately when send is called, so the Proxy thread can start the transfer promptly.

- Defer the doneSeq wait to handle.wait(), at the point where the send buffer actually needs to be reclaimed for reuse.

Under CUDA_DEVICE_MAX_CONNECTIONS=1, batching both operations together in a single cuStreamBatchMemOp call blocks subsequent compute kernels from execution until the Proxy thread signals doneSeq. By deferring the doneSeq wait out of the batch, we achieved better performance.

**Questions**

- What was the original design rationale for batching both operations together in a single cuStreamBatchMemOp call?

- Would it be safe or feasible to decouple them: write readySeq eagerly at send initiation and defer the doneSeq wait to handle.wait(), without breaking correctness guarantees?

## Issue 3: Fine-grained signal control between ranks

**Background**

We are attempting to implement a slot-based buffer management mechanism similar to DeepEP v2, where the receiver signals back to the sender to release each slot independently, allowing the sender to reuse it. This requires multiple independent signals between a pair of ranks.

Currently, sigIdx and ctx must both be 0, which appears to conflate all RMA operations between a pair of ranks into a single signal domain, making per-slot release signaling conflict with activation/gradient transfers.

**Our understanding of (peer, ctx, sigIdx) semantics**

- A (peer, ctx) pair defines a serialized, ordered channel: when a signal update completes, all prior ncclPutSignal/ncclSignal operations on the same (peer, ctx) are guaranteed to have completed as well.
- Within a (peer, ctx) channel, multiple sigIdx values allow independent signals to be tracked.
- Different (peer, ctx) channels are independent of each other with no cross-channel ordering guarantees.
  
**Questions**

- Is the semantic interpretation above correct?
- When is support for non-zero sigIdx / ctx planned?
- Is creating a new communicator group the recommended workaround for isolating signal domains in the interim?

## Issue 4: Limited observability for NCCL RMA operations

**Background**

When profiling, only the CPU-side launch latency of ncclPutSignal/ncclWaitSignal is visible. The actual data transfer duration is not captured, which makes it difficult to diagnose performance bottlenecks in RMA-based communication.

**Question**

- Is there a plan to enhance observability for NCCL RMA operations, such as exposing the actual data transfer duration in profiling tools?

## Issue 5: Symmetric memory creation count should be identical across group ranks

**Background**

When calling `torch.distributed._symmetric_memory.empty` + `rendezvous` to allocate a symmetric memory region within a group, all ranks in the group must have the same global symmetric memory allocation count at the time of the call. 

This count is not scoped to the current group, it tracks all symmetric memory regions ever created by each rank across all groups. If the counts differ between any two ranks in the group, the rendezvous call times out. For example, if rank 0 has previously created 1 region in total and rank 1 has created 2, the call will time out.

**Question**

- Is the count check strictly required for correctness, or can it be relaxed?

# Environment
- Hardware: 4 nodes × 8 × NVIDIA H20-3e, Hopper Architecture (sm_90, x86_64, 141 GiB)
- Interconnect: 8 × ConnectX-7 400 Gb/s RoCE, NV18 intra-node full-mesh NVLink, no NVLink cross-node
- GPU driver: 580.105.08
- CUDA: 12.8
- PyTorch: 2.12.0+cu128
- NCCL versions tested:  v2.30.7-1


# Reproduce Issue 1

We constructed a minimal reproducible example demonstrating the serialization of ncclPutSignal and compute kernels across streams described in Issue 1, and the issue reproduces reliably. When `CUDA_DEVICE_MAX_CONNECTIONS=1` is set, a ~300 µs bubble is observed between consecutive compute kernels, which we attribute to ncclPutSignal blocking kernel execution.

Since ncclPutSignal itself is not visible in profiling traces, we insert a D2D (device-to-device) copy operation before each ncclPutSignal call as a marker to identify its position in the timeline.

<img width="655" height="303" alt="Image" src="https://github.com/user-attachments/assets/e31f9496-0f67-4f14-a3ab-7ef4838f67aa" />

When `CUDA_DEVICE_MAX_CONNECTIONS` is unset, the bubble is largely eliminated and ncclPutSignal overlaps with compute kernels as expected.

<img width="655" height="333" alt="Image" src="https://github.com/user-attachments/assets/b26f1dcb-b83e-4bf0-a52a-cafedd5b0136" />

## Source code
```python
import os
import time
import torch
import torch.distributed as dist
import torch.distributed._symmetric_memory as symm_mem

# ============================================================================
# Configuration
# ============================================================================
GPUS_PER_NODE = 8            # Number of GPUs per node
NUM_NODES = 4                # Number of nodes
PP_SIZE = 4                  # Pipeline parallel size
NUM_ITERS = 100              # Total number of iterations
MATMUL_M = 1024              # Matrix dimension M
MATMUL_N = 1024              # Matrix dimension N
MATMUL_K = 6144              # Matrix dimension K
SYM_MEM_NUMEL = 1024 * 6144  # Symmetric memory buffer size (number of elements)

# Pre-allocated tensors for matmul (created once to avoid repeated allocation per iteration)
_matmul_a = None
_matmul_b = None

def create_pp_group(rank, world_size, device):
    local_rank = rank % GPUS_PER_NODE
    pp_ranks = [local_rank + i * GPUS_PER_NODE for i in range(NUM_NODES)]
    assert len(pp_ranks) == PP_SIZE, f"PP ranks count {len(pp_ranks)} != PP_SIZE {PP_SIZE}"

    pp_group = dist.new_group(ranks=pp_ranks, backend='nccl', device_id=device)

    # Position of the current rank within its PP group (0~3)
    pp_rank_in_group = pp_ranks.index(rank)

    dist.all_reduce(torch.ones(1, device=device), group=pp_group)
    return pp_group, pp_ranks, pp_rank_in_group

def init_symm_mem_for_pp(pp_group, pp_rank_in_group, device):
    """Initialize symmetric memory on the PP group (backend=NCCL)"""
    symm_mem.set_backend('NCCL')

    rma_stream = torch.cuda.Stream()

    next_peer = (pp_rank_in_group + 1) % PP_SIZE

    # --- Send direction: buffer for next_peer ---
    send_buf = symm_mem.empty(SYM_MEM_NUMEL, dtype=torch.bfloat16, device=device)
    symm_mem.rendezvous(send_buf, group=pp_group)

    # recv handle corresponds to the handle registered on next_peer's recv buffer.
    # put_signal(send_buf, recv_hdl_for_next, next_peer) sends data to the peer's recv buffer.
    recv_hdl_for_next = symm_mem.rendezvous(
        symm_mem.empty(SYM_MEM_NUMEL, dtype=torch.bfloat16, device=device), group=pp_group
    )

    return {
        'rma_stream': rma_stream,
        'next_peer': next_peer,
        'send_buf': send_buf,
        'recv_hdl_for_next': recv_hdl_for_next,
    }

def heavy_matmul(device):
    """Perform a large matrix multiplication"""
    global _matmul_a, _matmul_b
    c = torch.matmul(_matmul_a, _matmul_b)
    return c

def run_iteration(iter_idx, pp_rank_in_group, symm_state, device, src_tensor):
    rma_stream = symm_state['rma_stream']
    next_peer = symm_state['next_peer']
    send_buf = symm_state['send_buf']
    recv_hdl_for_next = symm_state['recv_hdl_for_next']

    current_stream = torch.cuda.current_stream()
    
    rma_stream.wait_stream(current_stream)
    # === Phase 1: put_signal to the next stage (dispatched on rma_stream) ===
    with torch.cuda.stream(rma_stream):
        send_buf.copy_(src_tensor)
        symm_mem.put_signal(send_buf, recv_hdl_for_next, next_peer)

    # === Phase 2: immediately launch matmul on the compute stream ===
    # put_signal runs on rma_stream; matmul runs on current_stream.
    # No explicit dependency between them — the GPU should execute them concurrently.
    c = heavy_matmul(device)

def main():
    # ------------------------------------------------------------------
    # 1. Initialize the distributed environment
    # ------------------------------------------------------------------
    local_rank = int(os.environ["LOCAL_RANK"])
    device = torch.device(f"cuda:{local_rank}")
    torch.cuda.set_device(device)

    print(f"[Rank {os.environ.get('RANK', '?')}] Setting CUDA device to {device}")
    
    dist.init_process_group("nccl", device_id=device)
    rank = dist.get_rank()
    world_size = dist.get_world_size()
    print(f"[Rank {rank}] Process group initialized. world_size={world_size}")
    dist.barrier()
    print(f"[Rank {rank}] Global barrier passed.")

    # ------------------------------------------------------------------
    # 2. Create PP groups
    # ------------------------------------------------------------------
    pp_group, pp_ranks, pp_rank_in_group = create_pp_group(rank, world_size, device)
    print(f"[Rank {rank}] PP group created: pp_ranks={pp_ranks}, "
          f"pp_rank_in_group={pp_rank_in_group}")
    dist.barrier()
    print(f"[Rank {rank}] PP group barrier passed.")

    # ------------------------------------------------------------------
    # 3. Initialize symmetric memory on the PP group
    # ------------------------------------------------------------------
    symm_state = init_symm_mem_for_pp(pp_group, pp_rank_in_group, device)
    print(f"[Rank {rank}] Symmetric memory initialized on PP group. "
          f"pp_ranks={pp_ranks}, pp_rank_in_group={pp_rank_in_group}, "
          f"next={symm_state['next_peer']}")
    dist.barrier()
    print(f"[Rank {rank}] Symm mem barrier passed. Starting training loop...")

    # ------------------------------------------------------------------
    # 4. Pre-allocate matmul tensors (created once) and run warmup
    # ------------------------------------------------------------------
    global _matmul_a, _matmul_b
    print(f"[Rank {rank}] Pre-allocating matmul tensors...")
    _matmul_a = torch.randn(MATMUL_M, MATMUL_K, dtype=torch.bfloat16, device=device)
    _matmul_b = torch.randn(MATMUL_K, MATMUL_N, dtype=torch.bfloat16, device=device)
    for _ in range(3):
        heavy_matmul(device)
    torch.distributed.barrier()
    print(f"[Rank {rank}] Warmup done. Starting {NUM_ITERS} iterations...")

    # Pre-prepared source tensor (same data copied each iteration, simulating D2D)
    src_tensor = torch.full((SYM_MEM_NUMEL,), fill_value=float(pp_rank_in_group), dtype=torch.bfloat16, device=device)

    # ------------------------------------------------------------------
    # 5. Training loop: put_signal overlapped with matmul
    # ------------------------------------------------------------------
    # NOTE: We omit the profiler setup here for brevity — please define your own
    # (e.g., torch.profiler.profile) and wrap the loop accordingly.
    t_start = time.time()
    with profiler: # define your own profiler before running
        for it in range(NUM_ITERS):
            for _ in range(20):
                run_iteration(it, pp_rank_in_group, symm_state, device, src_tensor)
            torch.distributed.barrier()
            profiler.step()

            if it % 10 == 0 and pp_rank_in_group == 0:
                elapsed = time.time() - t_start
                print(f"[Rank {rank}] iter {it}/{NUM_ITERS} elapsed={elapsed:.2f}s")

    t_total = time.time() - t_start
    if pp_rank_in_group == 0:
        print(f"[Rank {rank}] ===== DONE: {NUM_ITERS} iters in {t_total:.2f}s "
              f"({t_total/NUM_ITERS*1000:.1f} ms/iter) =====")
    dist.barrier()
    print(f"[Rank {rank}] All done. Profiler trace saved")

if __name__ == "__main__":
    main()
``` 

## 评论 (13)

### DAMI211 · 2026-06-17

We also observed that zero-SM AllGather (both intra-node and inter-node) suffers from the same serialization issue described in Issue 1 when `CUDA_DEVICE_MAX_CONNECTIONS=1` is set. The root cause may be that `ncclMemOpSync` also relies on `cuStreamBatchMemOp` internally.

When `CUDA_DEVICE_MAX_CONNECTIONS=1` is set, we observe significant bubbles between compute kernels. The shorter bubble corresponds to intra-node AllGather, and the longer one to inter-node AllGather.

<img width="513" height="164" alt="Image" src="https://github.com/user-attachments/assets/ffade4c7-4126-4d58-9a26-2830e59a9047" />

When `CUDA_DEVICE_MAX_CONNECTIONS` is unset, compute and communication resume overlapping as expected.

<img width="513" height="138" alt="Image" src="https://github.com/user-attachments/assets/10ef764f-f569-49fc-9fbb-6510c8f8a39d" />


### xiaofanl-nvidia · 2026-06-22

++ @zhenhaohe to review and relay some of the above issues to CUDA team. 

### zhenhaohe · 2026-06-23

Regarding Issue 3: Fine-grained signal control between ranks:

- Your understanding is correct
- Support of multiple sigIdx and context will be available in the next NCCL release
- Currently you need to create multiple communicators as workaround

### zhenhaohe · 2026-06-23

@kwen2501 for issue 5

### zhenhaohe · 2026-06-23

Regarding Issue 1, why do you say `CUDA_DEVICE_MAX_CONNECTIONS=1 to improve compute-communication overlap` ? 
https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/environment-variables.html#cuda-device-max-connections
From the doc, you might create a false dependency if the CUDA_DEVICE_MAX_CONNECTIONS is smaller than the number of streams.

### zhenhaohe · 2026-06-23

Regarding issue 2, the current putSignal has a local completion semantic, meaning that once it is done on stream, the buffer could be reused. So we have both the start and done signal enqueued to the stream. 

What do you mean exactly with handle.wait()? Are you suggesting new NCCL API, such as: putSignal_nonblocking which returns an handle, and a putSignal_completion that takes in the handle?

### DAMI211 · 2026-06-23

Thanks @zhenhaohe for the clarification :)

The reason we set `CUDA_DEVICE_MAX_CONNECTIONS=1` comes from the NVIDIA Megatron-LM training framework. For example, during the backward pass with tensor parallelism enabled, the TP communication group's AllReduce/ReduceScatter kernel (for dX) and the local dW GEMM kernel can run in parallel. However, with the default `CUDA_DEVICE_MAX_CONNECTIONS=8`, the CUDA scheduler may reorder kernels across work queues, breaking this intended overlap. Setting `CUDA_DEVICE_MAX_CONNECTIONS=1` forces kernels to be scheduled in launch order, which achieves better compute-communication overlap.

A related discussion on `CUDA_DEVICE_MAX_CONNECTIONS` can be found here: https://github.com/NVIDIA/Megatron-LM/issues/5105. This setting is no longer needed on Blackwell, but since we are on Hopper, `CUDA_DEVICE_MAX_CONNECTIONS=1` remains a requirement for us.

Given this constraint, is there a way to preserve compute-communication overlap between ncclPutSignal and compute kernels (as well as between zero-SM operations and compute kernels)?



### DAMI211 · 2026-06-23

> Regarding issue 2, the current putSignal has a local completion semantic, meaning that once it is done on stream, the buffer could be reused. So we have both the start and done signal enqueued to the stream.
> 
> What do you mean exactly with handle.wait()? Are you suggesting new NCCL API, such as: putSignal_nonblocking which returns an handle, and a putSignal_completion that takes in the handle?

Issue 2 is likely only relevant under `CUDA_DEVICE_MAX_CONNECTIONS=1`. Without it, decoupling the two operations is unnecessary since launching ncclPutSignal on a separate CUDA stream does not block subsequent compute kernels. 

In our case with `CUDA_DEVICE_MAX_CONNECTIONS=1`, ncclPutSignal blocks subsequent compute kernels until doneSeq is signaled, even though the send buffer is not needed for reuse until much later in our pipeline schedule.

We are indeed exploring splitting ncclPutSignal into `putSignal_nonblocking + putSignal_completion` as a local modification for our own use case, not as a new NCCL API suggestion. By deferring the doneSeq wait to the point where the buffer actually needs to be reused, we can reduce the blocking overhead.

Our question is: is this decoupling safe in principle, as long as doneSeq is waited before the buffer is reused?



### DAMI211 · 2026-06-23

> What do you mean exactly with handle.wait()? 

Handle is a concept from Megatron, backed by `ProcessGroupNCCL::WorkNCCL` class in PyTorch. When a collective is launched, an event is recorded on the communication stream, and calling handle.wait() makes the compute stream wait for it.

In our case, we wrap `torch.distributed._symmetric_memory.put_signal` in a similar class exposing a `wait()` method. If we decouple it into `putSignal_nonblocking + putSignal_completion`, we can defer putSignal_completion to wait(), so the compute stream is only blocked when the buffer actually needs to be reused.

### zhenhaohe · 2026-06-25

Thanks for the background. This is an interesting issue.

If you set CUDA_DEVICE_MAX_CONNECTIONS = 1 then you will have 1 compute channel and 1 copy engine channel. So similar operations on two different streams should serialize. And the stream memory operations are mapped to the compute channel. So this blocking behavior you see is expected.

And in terms of decoupling, it should be safe if do it properly. Feel free to open up an PR if you already have your putSignal_nonblocking + putSignal_completion ready and we could take a look as well.

### DAMI211 · 2026-06-26

```bash
> Thanks for the background. This is an interesting issue.
> 
> If you set CUDA_DEVICE_MAX_CONNECTIONS = 1 then you will have 1 compute channel and 1 copy engine channel. So similar operations on two different streams should serialize. And the stream memory operations are mapped to the compute channel. So this blocking behavior you see is expected.
> 
> And in terms of decoupling, it should be safe if do it properly. Feel free to open up an PR if you already have your putSignal_nonblocking + putSignal_completion ready and we could take a look as well.
```

Interestingly, under CUDA_DEVICE_MAX_CONNECTIONS = 1, we also noticed that kernel-to-kernel overlap is affected. Some pairs overlap better, some worse. Overall the improvements seem to outweigh the regressions, which is likely why we still see a net performance gain.

This serialization issue seems hard to avoid on Hopper and earlier architectures. I also considered whether setting CUDA_DEVICE_MAX_CONNECTIONS=2 could help by allocating one compute channel exclusively to NCCL RMA operations, but I couldn't find a way to make that work at that level of granularity.

Even without full overlap between compute kernels and putSignal_nonblocking, we found that using NCCL RMA for cross-stage P2P communication in Pipeline Parallelism still slightly outperforms our tuned DeepEP V2 P2P implementation. We believe NCCL RMA has significant potential here. That said, the comparison is a bit unfair. We pre-allocated enough symmetric memory buffers to avoid any send/recv buffer reuse concerns, at the cost of higher memory usage. Once multiple sigIdx and context are supported, we plan to reduce memory usage by reusing buffers.

Also worth mentioning: we are currently using a copy-based send approach (D2D copy followed by putSignal) rather than zero-copy send. The reason is that zero-copy send seems to require customizing PyTorch's CUDACachingAllocator so that compute results land directly in symmetric memory. We may explore that path later, but at least NCCL RMA gives us the possibility to implement truly zero-copy, zero-SM transfers.

For Issue 2, we will open a PR soon and continue the discussion there. Thanks again!

### xiaofanl-nvidia · 2026-08-10

@zhenhaohe @DAMI211 was the PR opened? Should we close this issue? 

### DAMI211 · 2026-09-14

Hi @xiaofanl-nvidia  and @zhenhaohe , we’re revisiting the PP optimizations now that multiple sigIdx values are supported, and since we now have access to Blackwell GPUs, we may not need any API changes after all. Feel free to close this issue for now, and we can follow up if anything else comes up.

Thanks all :)
