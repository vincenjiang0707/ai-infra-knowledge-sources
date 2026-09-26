# [Issue #211] Does _clone_args cause unintended plan() re-execution in FlashInfer baseline solutions benchmarks?

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/211
state: open | updated: 2026-03-11T14:56:49Z
labels: 

## 正文

# Problem

  In the https://github.com/flashinfer-ai/flashinfer-bench/issues/127, it was mentioned that:

  > Thanks Shiyi for raising the issue. The FlashInfer wrapper solutions in the dataset are outdated. When we benchmarked the attention kernels for https://bench.flashinfer.ai/, we cached planned wrappers across calls and only re-planned when metadata changed, which better represents the actual usage. We'll update the `flashinfer_wrapper` solutions to the new version. 

 _Originally posted by @zanderjiang in [#127](https://github.com/flashinfer-ai/flashinfer-bench/issues/127#issuecomment-3652871550)_

  I've been looking at the current implementation and I'd like to confirm whether the behavior matches this description.

# Observation

  The FlashInfer baseline wrapper (e.g., `flashinfer_wrapper_03f7b0` for `mla_paged_decode_h16_ckv512_kpe64_ps1`) determines whether to re-plan based on several fields, including data_ptr():
```
  needs_plan = (
      state.get("batch_size") != batch_size
      or state.get("len_indptr") != len_indptr
      or state.get("num_kv_indices") != num_kv_indices
      or state.get("sm_scale") != sm_scale
      or state.get("kv_indptr_ptr") != kv_indptr.data_ptr()
      or state.get("kv_indices_ptr") != kv_indices.data_ptr()
  )
```
  Meanwhile, https://github.com/flashinfer-ai/flashinfer-bench/blob/main/flashinfer_bench/bench/timing.py uses _clone_args as a setup function:
```
  def time_runnable(fn, args, warmup, iters, device):
      return do_bench(
          fn=lambda cloned_args: fn(*cloned_args),
          setup=lambda: _clone_args(args),
          ...
      )
```
  Since `_clone_args` clones all tensors before each timed iteration, the resulting `kv_indptr` and `kv_indices` will have different `data_ptr()` values every time. This means `needs_plan` evaluates to True on every iteration, and `plan()` is re-executed inside every timed call — even though the actual metadata (batch_size, shapes, sm_scale) hasn't changed.

  - The baseline's measured latency includes plan() overhead (tensor allocation + wrapper.plan(...)) on every iteration, not just when metadata changes.
  - Solutions that don't use data_ptr() as a cache key (e.g., Triton kernels caching by batch_size) are unaffected by _clone_args, and thus avoid this repeated overhead.
  - This may not reflect real inference behavior, where plan() typically runs once per batch shape change.

# Questions
Is this the intended behavior? Should plan() be included in the timed region for every iteration?

## 评论 (3)

### xslingcn · 2026-03-10

Thank you for the issue! I haven't been tracking the recent changes but seems that the `cloned_args` semantics was introduced in [this pr](https://github.com/flashinfer-ai/flashinfer-bench/pull/125/changes#diff-5da370893521461895d3756b1bffc9f64f3f6b2455c1a5ec2fc06d76127a042aR253), and our released solutions/evaluations/wrappers were based on earlier codebases, which does take same instance inputs, so the reported results should be accurate.

But for current timing runs this does seem to be an issue. cc @Ubospica can you take a look?

### A-PolarBear · 2026-03-10

Thank you for reaching out! 
Quick follow-up: Would it make sense to comment these out in the needs_plan check to achieve the expected behavior?
```
needs_plan = (
      state.get("batch_size") != batch_size
      or state.get("len_indptr") != len_indptr
      or state.get("num_kv_indices") != num_kv_indices
      or state.get("sm_scale") != sm_scale
      ### or state.get("kv_indptr_ptr") != kv_indptr.data_ptr()
      ### or state.get("kv_indices_ptr") != kv_indices.data_ptr()
  )
```
Additionally, I would like to confirm something regarding the benchmark setup. If we apply a "Triton Kernel Launch Overhead Bypass" trick for the Triton implementation—where the first call goes through the normal Triton path to compile the kernel, and we then extract the compiled CUDA function handle from Triton's internal cache to directly call `cuLaunchKernel` via `ctypes` for subsequent calls—would using this trick still be considered a fair comparison here?

### zanderjiang · 2026-03-11

Thank you for the issue, in #196 we removed the _clone_args logic when we shifted to cupti for timing. Updating to the latest version should fix the issue.
