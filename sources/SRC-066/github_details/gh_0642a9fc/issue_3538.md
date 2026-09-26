# [Issue #3538] GemmWithKReduction parallel split-K: workspace initialization is skipped, partials land in the user output buffer

source: https://github.com/NVIDIA/cutlass/issues/3538
state: open | updated: 2026-09-01T16:52:19Z
labels: CUTLASS C++

## 正文

### Description

Since CUTLASS 3.2, `GemmUniversalBase::initialize()` only calls into `Params::init_workspace` when the mode is plain GEMM:

```cpp
// include/cutlass/gemm/device/gemm_universal_base.h:415-420
// Assign and prepare workspace memory
if (args.mode == GemmUniversalMode::kGemm) {
  return params_.init_workspace(workspace, stream);
}
return Status::kSuccess;
```

`GemmWithKReduction` overrides `Params::init_workspace` to do its work exactly in the other mode:

```cpp
// include/cutlass/gemm/kernel/gemm_with_k_reduction.h (init_workspace)
if (this->mode == GemmUniversalMode::kGemmSplitKParallel) {
  ptr_D = workspace;
  ptr_gemm_k_reduction = static_cast<uint8_t *>(workspace)
           + sizeof(ElementC) * size_t(this->batch_stride_D) * size_t(this->grid_tiled_shape.k());
  return Status::kSuccess;
}
```

The override can therefore never run: in `kGemmSplitKParallel` mode the base class skips the call entirely. Consequences for `device::GemmWithKReduction` with `--parallel-split-k` (example 23):

1. The mainloop writes unreduced per-slice partial products through `ptr_D`, which still points at the user's D buffer; with a grid whose K extent exceeds the user D allocation this writes out of bounds.
2. The separate reduction launch reads `ptr_gemm_k_reduction` from a never-initialized workspace.

`get_workspace_size` does reserve the right size in that mode, so the buffer exists and `initialize()` returns success; only the redirect is skipped.

Verified statically by reading both functions; additionally exercised on hardware via a probe subclass of the protected base (example 23 flow with `--parallel-split-k`): after a successful `initialize()`, `params_.ptr_D` still equals the user pointer while the reported workspace size is nonzero.

### Suggested fix

Widen the gate in `gemm_universal_base.h` so the virtual `init_workspace` runs for every mode (the kernels' own overrides already no-op where nothing is needed), or special-case `kGemmSplitKParallel` alongside `kGemm`.


## 评论 (1)

### AyaanFaisal21 · 2026-09-01

Confirmed on an A10 with example 23 (m=1024 n=1024 k=8192, 8 slices): parallel split-k miscompares and compute-sanitizer shows OOB 16-byte writes past D; serial and plain pass. Nice find.

Some history: the gate came in with the 3.2 squash commit (4575443); before that, initialize() called init_workspace unconditionally (v2.11, v3.1), and the python cppgen backend still does. So rather than widening the gate, I'd revert it and move the mode check onto the memset in ParamsBase (only serial split-k needs the semaphore zeroing). Same fix, keeps 3.2's memset skip for the parallel path. Verified: all three modes pass after, sanitizer clean.

There's an attached PR with more details, open to feedback
