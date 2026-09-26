# [Issue #195] do_bench: per-iteration torch.cuda.synchronize() inflates runtimes for fast kernels

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/195
state: closed | updated: 2026-02-27T20:17:19Z
labels: 

## 正文

## Summary

`do_bench()` in `flashinfer_bench/bench/timing.py` calls `torch.cuda.synchronize()` **inside** the benchmark loop (lines 199, 203), once per iteration. For microsecond-scale kernels, this creates a GPU idle bubble between iterations (red bracket in slide below, link at the bottom) and drastically inflates measured runtimes.

<img width="80%" alt="Image" src="https://github.com/user-attachments/assets/e88236b3-fc4d-4716-9ce5-dd7d6821adb0" />

## The problem

```python
# Benchmark (lines 186-206)
for i in range(rep):
    ...
    _clear_cache(cache)
    if setup is not None:
        setup_result = setup()
        torch.cuda.synchronize()      # <-- sync before EVERY iteration
        start_events[i].record()
        fn(setup_result)
    else:
        torch.cuda.synchronize()      # <-- sync before EVERY iteration
        start_events[i].record()
        fn()
    end_events[i].record()
```

The per-iteration `synchronize()` forces the CPU to wait for all prior GPU work (including `_clear_cache`) to complete before scheduling the start event. For fast kernels, the GPU then sits idle waiting for the CPU to schedule the kernel. The kernel runtime includes this GPU idle gap.

## Impact

For the GDN decode kernel (~4 us on RTX 3090 as per NCU), `do_bench` reports ~51 us, a **~12x overestimate**. Removing the per-iteration `synchronize()` brings measurements to ~4.3 us, which is much more consistent with both NCU and NVBench runtimes.

## Suggested fix

Remove the two `torch.cuda.synchronize()` calls inside the loop (lines 199 and 203). The sync on line 184 (after warmup) and line 209 (after the loop) are correct and sufficient.

```diff
         if setup is not None:
             setup_result = setup()
-            torch.cuda.synchronize()
             start_events[i].record()
             fn(setup_result)
         else:
-            torch.cuda.synchronize()
             start_events[i].record()
             fn()
```

## Precedent

Both Triton's `do_bench` and FlashInfer's own `bench_gpu_time_with_cuda_event` already implement the correct pattern:

- **Triton** ([`triton-lang/triton/python/triton/testing.py`](https://github.com/triton-lang/triton/blob/main/python/triton/testing.py), lines 174-186): no `synchronize()` inside the benchmark loop.
- **FlashInfer main repo** ([`flashinfer/testing/utils.py`](https://github.com/flashinfer-ai/flashinfer/blob/main/flashinfer/testing/utils.py), line 902): explicitly comments *"Synchronize once outside of the loop to avoid synchronization overhead"*.
- **PyTorch** ([pytorch/pytorch#133053](https://github.com/pytorch/pytorch/issues/133053)): open issue titled "Stop calling `torch.cuda.synchronize()` in `triton/testing.py` `do_bench`", filed by Edward Yang.
- **NVBench** solves the same problem with a "blocking kernel" that eliminates CPU/GPU sync points entirely ([GPUMode talk at 13:58](https://www.youtube.com/watch?v=CtrqBmYtSEk&t=838)).

## Reproducibility

Any kernel under ~50 us will show inflated runtimes. The effect scales with the ratio of sync overhead to kernel duration: negligible for millisecond kernels, but dominant for microsecond kernels.

## 评论 (3)

### yzh119 · 2026-02-22

@Ubospica @zanderjiang  can you please update to use https://github.com/flashinfer-ai/flashinfer/blob/78a0091728754b28f2e01819f9eb263940ceb735/flashinfer/testing/utils.py#L1508-L1524 (and use cupti for precise benchmarking) instead of keeping an outdated benchmarking function in flashinfer-bench codebase?

### zanderjiang · 2026-02-22

@yzh119 @Ubospica Updated via #196 

### Ubospica · 2026-02-27

This should be fixed by the cupti api. Feel free to reopen it if there are still problems!
