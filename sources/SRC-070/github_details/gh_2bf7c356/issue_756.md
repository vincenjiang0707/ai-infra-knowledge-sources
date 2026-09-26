# [Issue #756] [HybridEP] Blocking-mode permute/unpermute kernels read a per-call pinned host tensor that the caller's allocator can recycle before the kernels run (intermittent `illegal memory access`)

source: https://github.com/deepseek-ai/DeepEP/issues/756
state: closed | updated: 2026-09-21T08:52:20Z
labels: 

## 正文

## Summary

In blocking mode (`non_blocking=False`, i.e. no `num_permuted_tokens` supplied), `metadata_preprocessing` stores the dispatched-token count in a **4-byte CPU pinned tensor** that is allocated per call, and the permute / unpermute kernels then **dereference that host pointer on the device** — in the forward pass and again in both backward passes (`combine_with_unpermute` in the dispatch backward, `dispatch_with_permute` in the combine backward). HybridEP never ties that tensor's lifetime to the stream (`record_stream` / `CachingHostAllocator_recordEvent` are not used anywhere under `csrc/hybrid_ep`). PyTorch's pinned-memory allocator is not stream-ordered, so as soon as the caller drops the handle — which autograd does right after the backward kernels are *enqueued* — the block goes back to the host free list and is handed to the next small pinned allocation. A kernel still queued behind the host then reads a count written by an unrelated tensor and indexes far outside `row_id_map` / the shared NVLink buffer. The result is an intermittent `CUDA error: an illegal memory access was encountered`, reported at the next host synchronization, i.e. at the start of the following training iteration.

The non-blocking path is not affected: there the count lives in a device tensor (`executor.cu:103-105`).

Reproduced with both `1b8f467` and `d28bd67` (identical code for the files involved; the diff between them only touches includes in `internode_doca.cuh`).

## Environment

- HybridEP `hybrid-ep` branch at `d28bd67` and `1b8f467` (`deep_ep 1.2.1+…`), single NVLink domain per EP group, `use_shared_buffer` default
- NGC PyTorch 26.04 container (PyTorch 2.12.0a0, CUDA 13.2, driver 595), GB300 NVL72
- Caller: Megatron-LM MoE flex dispatcher with `moe_flex_dispatcher_backend=hybridep`, blocking mode (no `moe_expert_rank_capacity_factor`, so `num_permuted_tokens=None`), `moe_hybridep_num_sms=32`, `NUM_OF_TOKENS_PER_CHUNK_{DISPATCH_API,COMBINE_API,PREPROCESSING_API}=128`
- EP group of 64 GPUs (16 nodes x 4), 896 experts / 14 local experts, top-16, hidden 7168 (bf16), **32768 tokens per rank per call** (512K packed sequence, CP16, TP4 with sequence parallelism), routing force-balanced so every call has identical counts
- Training loop: 32 micro-batches per iteration, about 74 s per iteration

## Symptom

Iterations 1 and 2 complete normally. At the very beginning of iteration 3 (sometimes 4-6), one or two processes fail with `CUDA error: an illegal memory access was encountered`, surfacing at the first host sync of the new iteration (a `.item()` in the first layer); the NCCL watchdog reports the same sticky error. The failing processes are always the **node-local rank 0** of their node — in our setup exactly the processes that run the data loader, i.e. the ones that allocate pinned staging buffers at the start of every iteration. The other 62-63 processes never fault.

## Bisect (all on the same 512K configuration)

| Change | Result |
| --- | --- |
| baseline, HybridEP blocking mode | crashes at iteration 3-6 |
| `CUDA_LAUNCH_BLOCKING=1` | 6/6 iterations pass |
| Megatron all-to-all dispatcher instead of HybridEP | 20/20 iterations pass |
| two 256K documents per 512K buffer (same token counts, shorter attention) | 8/8 pass |
| chunked optimizer-state offload disabled | crashes |
| top-k 16 → 8 | crashes |
| `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:False` | crashes |
| `moe_hybridep_pad_variable_tokens=True` | crashes at iteration 6 (extra per-layer syncs narrow the window) |
| **caller keeps the handle's pinned tensors alive** (see mitigation below), HybridEP otherwise unchanged | **8/8 and 20/20 iterations pass** |

So: not a deterministic index/overflow problem, not the device allocator, not the optimizer; a host-side lifetime race on the HybridEP path that disappears when the host cannot run ahead of the GPU.

## Root cause (code at `d28bd67`)

1. The count is a per-call pinned host tensor in blocking mode (`csrc/hybrid_ep/executor/executor.cu:103-109`):

```cpp
  if (non_blocking) {
    handle.num_dispatched_tokens_tensor =
        torch::empty({1}, torch::dtype(torch::kInt32).device(torch::kCUDA));
  } else {
    handle.num_dispatched_tokens_tensor =
        torch::empty({1}, torch::dtype(torch::kInt32).pinned_memory(true));
  }
```

   `padded_tokens_per_expert` gets the same treatment (`executor.cu:168-175`). The scan kernel writes the count into it (`executor.cu:140`), and the host reads it after an unchecked `cudaStreamSynchronize` (`executor.cu:182-191`) — that part is fine.

2. The same pinned tensor is then passed to device kernels by raw host pointer, not only to the host. `hybrid_ep.cu:196/303/383` copy `handle.num_dispatched_tokens_tensor` into the launch args of dispatch, combine and the permute helpers; `csrc/hybrid_ep/extension/permute.cu` hands `data_ptr<int>()` to the kernels (`permute.cu:288`, `:429`, `:548`) and the kernels dereference it:

```cpp
// permute_preprocessing_kernel, permute.cu:52
int num_dispatched_tokens = *num_dispatched_tokens_ptr;
// permute_kernel, permute.cu:326
int num_dispatched_tokens = *num_dispatched_tokens_ptr + pad_multiple;
// unpermute_kernel, permute.cu:459
int num_dispatched_tokens = *num_dispatched_tokens_ptr;
```

   Reading pinned host memory from a kernel is legal, but only while the block is alive.

3. Nothing extends the block's lifetime to the kernels. Every HybridEP launch runs on `at::cuda::getCurrentCUDAStream()` (`hybrid_ep.cu:199/257/312/389`, `executor.cu:45/86`) and there is no `record_stream`, `CachingHostAllocator_recordEvent`, event or side stream anywhere under `csrc/hybrid_ep`. PyTorch's `CachingHostAllocator` frees a block straight into its free list unless a stream was recorded for it (PyTorch's own copy kernels do record); the freed 4-byte block is the first candidate for the next small pinned request.

4. The handle (and with it the pinned tensor) is released by the caller as soon as the backward is enqueued: in Megatron's `HybridEPDispatch.backward` / `HybridEPCombine.backward` the handle lives in the autograd context, which is dropped right after `combine_with_unpermute` / `dispatch_with_permute` return — but those calls only *enqueue* the unpermute / permute kernels. With the host running ahead of the GPU, the block is recycled and rewritten (on our ranks by the data loader pinning the next batch) before the kernels execute. The kernels then compute row indices from a foreign value, hence the fault.

Why it depends on sequence length: it is a race, not a size limit. Longer sequences make each iteration's attention much longer, so the GPU lags further behind the host at the iteration boundary and the window between "handle dropped" and "backward kernel actually runs" widens. Why only node-local rank 0: those processes are the only ones that immediately reuse the freed pinned block for something else (data-loader staging); on the other ranks the block is recycled but still holds the old, and in this force-balanced run still correct, value.

## Suggested fix

Any of these closes the hole; (1) is the cleanest and matches what the non-blocking path already does:

1. Never hand a host pointer to the kernels. In blocking mode, keep the pinned tensor for the host read, but after the `cudaStreamSynchronize` in `metadata_preprocessing` copy the count into a device int32 (a plain device tensor is stream-ordered by the caching allocator) and pass that to `permute_preprocessing_kernel`, `permute_kernel` and `unpermute_kernel`. Equivalently: always allocate the device tensor for the kernels and add the pinned copy only for the host read.
2. Keep the host pointer but register the stream: call `at::cuda::CachingHostAllocator_recordEvent(ptr, ctx, stream)` on the pinned tensor after every kernel launch that reads it (forward and both backward paths), so the allocator does not recycle the block until those kernels complete.
3. Robustness, independent of the race: check the return codes of `cudaStreamSynchronize` (`executor.cu:183`) and of `cudaFuncSetAttribute` / `cudaLaunchCooperativeKernel` in `permute.cu` (`:296-299`); today a failure there is silent and only shows up later as a corrupted count.

`padded_tokens_per_expert` (pinned int64) is only read on the host after the sync, so it is not affected, but the same "device copy for kernels, pinned copy for the host" pattern would keep both consistent.

## Caller-side mitigation we validated

While the fix lands in HybridEP we keep the handle's pinned tensors alive on the Megatron side (module-level `collections.deque(maxlen=1024)`, appended right after `dispatch_with_permute` returns in the dispatch autograd forward):

```python
_HYBRIDEP_RETIRED_PINNED_TENSORS = collections.deque(maxlen=1024)

def _retain_hybridep_pinned_tensors(handle):
    for item in handle:
        if torch.is_tensor(item) and item.device.type == "cpu" and item.is_pinned():
            _HYBRIDEP_RETIRED_PINNED_TENSORS.append(item)
```

Every later blocking dispatch synchronizes the stream, so by the time an entry is evicted the kernels that could read it have completed. With only this change (HybridEP untouched) the 512K configuration runs 8/8 and 20/20 iterations at the same throughput as before the crash (about 73 s per iteration, 64 GPUs). It is a mitigation, not a fix: the ownership problem stays in HybridEP.

## Reproduction notes

Any Megatron-LM MoE run that uses the flex dispatcher with `moe_flex_dispatcher_backend=hybridep` in blocking mode, long enough sequences to keep the GPU well behind the host (we needed 32768 tokens per rank per call; 16384 did not trigger it), and pinned-memory churn on the host (a data loader with pinned staging buffers is enough). The failure shows up within the first few iterations. A quick sanity check of the diagnosis is to poison the pinned block (write a large value into it right after the handle is dropped) — the fault then becomes deterministic. Happy to open a PR for option (1) if the approach is acceptable.

## 评论 (2)

### yuzhongw-nvidia · 2026-09-21

Hi @Autumn1998 , could you please help take a look at this? Thanks!

### yuzhongw-nvidia · 2026-09-21

Update after retesting with the current `hybrid-ep` head (`10d4dd7`, 2026-09-11):

**The mechanism described above is gone since `17cfb81` (#625, "Optimization of the standalone permute path").** Starting with that commit the permute/unpermute kernels no longer take a pointer to `handle.num_dispatched_tokens_tensor`: in blocking mode the count is read on the host after the `cudaStreamSynchronize` in `metadata_preprocessing` and passed to the kernels by value (`PermuteArgs::num_permuted_token`), and the kernels only read device tensors (`dense_chunk_layout`, `dense_to_expert_map`, `tokens_per_expert`); `UnpermuteArgs` carries no count pointer at all. `grep num_dispatched_tokens_ptr csrc/hybrid_ep/extension/permute.cu` returns nothing on `10d4dd7`. Our container had `d28bd67`, i.e. the commit right before that change.

Empirical confirmation on the same setup as the report (GB300 NVL72, 64 ranks, 32768 tokens per rank per call, blocking mode, no caller-side mitigation), same day:

| DeepEP hybrid-ep | Result |
| --- | --- |
| `d28bd67` | `illegal memory access` at the start of iteration 3 on a node-local-rank-0 process, as reported |
| `10d4dd7` (rebuilt in the same container with the same build flags) | 20/20 iterations, no errors, ~72 s/iteration |

What remains is only the robustness note: in blocking mode `num_dispatched_tokens_tensor` (and `padded_tokens_per_expert`) are still per-call pinned host tensors with no stream tracking. Their only device access is now the scan kernel's write, which completes before the synchronize, so I do not see a way for the race to recur with the current kernels. From our side this can be closed, or kept open only as a note about the untracked pinned allocations if you prefer to move the count to a device tensor as in the non-blocking path.
