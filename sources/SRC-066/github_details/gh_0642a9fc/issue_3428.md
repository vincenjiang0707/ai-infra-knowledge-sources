# [Issue #3428] [BUG] Broken atomicCAS RMW loop in SubbyteReference::set() for straddling elements

source: https://github.com/NVIDIA/cutlass/issues/3428
state: closed | updated: 2026-09-01T20:08:39Z
labels: bug, ? - Needs Triage, CUTLASS C++

## 正文

### Which component has the problem?

CUTLASS C++

### Bug Report

### Describe the bug

The multi-storage-unit (straddling) path of `SubbyteReference::set()` in `include/cutlass/subbyte_reference.h` contains a broken atomic compare-and-swap read-modify-write loop.

Specifically, after a successful `atomicCAS` the retry condition compares the updated value against the value returned by `atomicCAS` instead of comparing the originally assumed value against the returned value. As a result, the loop may:

- Spin indefinitely after a successful CAS.
- Produce torn or incorrect writes under contention.

This affects concurrent updates to adjacent sub-byte elements whose bit ranges span two `StorageUnit`s (`high_storage_unit_idx_ != low_storage_unit_idx_`).

### Steps to reproduce

Any concurrent write that enters the multi-storage-unit branch of `SubbyteReference::set()`.

Minimal device-side sketch (packed `int4b_t` values stored in a `uint8_t` array):

```cpp
using Element = cutlass::int4b_t;
using StorageVec = cutlass::Array<uint8_t, N>;  // N sufficiently large

SubbyteReference<Element, StorageVec> ref0(ptr, offset);
SubbyteReference<Element, StorageVec> ref1(ptr, offset + 1);  // Adjacent element crossing a StorageUnit boundary

// Executed concurrently from different threads:
ref0.set(value0);
ref1.set(value1);
```

The affected code currently follows this pattern:

```cpp
do {
  original_low_bits = ((*ptr_)[low_storage_unit_idx_]);
  update_low_bits = (original_low_bits & kLowUpdateMask) | low_new_bits;
  original_low_bits = atomicCAS(
      &((*ptr_)[low_storage_unit_idx_]),
      original_low_bits,
      update_low_bits);
} while (update_low_bits != original_low_bits);
```

The identical issue exists in the corresponding high-half CAS loop.

### Expected behavior

The CAS loop should follow the standard read-modify-write retry pattern already used elsewhere in the same file (including the single-storage-unit path and the previously fixed `ConstSubbyteReference` implementation):

```cpp
Storage original = *ptr;
Storage assumed;

do {
  assumed = original;
  Storage updated = (assumed & mask) | new_bits;
  original = atomicCAS(ptr, assumed, updated);
} while (original != assumed);
```

A successful CAS should exit the loop immediately while a failed CAS caused by a concurrent modification should simply retry.

### Environment

- **Environment:** Bare metal
- **CUDA architectures:** Any architecture taking the `__CUDA_ARCH__` path
- **Observed on:** Recent `main` branch and 4.5.x–4.6.x releases

### Additional context

- The single-storage-unit implementation already uses the correct CAS retry pattern.
- The `ConstSubbyteReference` implementation was previously fixed to use the same correct algorithm (referenced in the 4.5.x changelog).

However, both CAS retry loops in this path still use the incorrect termination condition.

- Because the bug only manifests when multiple threads concurrently update packed sub-byte elements that span a `StorageUnit` boundary, it is difficult to reproduce with conventional unit tests and is more likely to surface in real packed-tensor workloads involving multiple threads or CTAs.

## 评论 (4)

### github-actions[bot] · 2026-08-31

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### nouraellm · 2026-08-31

@hwu36 given the comments in #3440 should I keep this open? 

### hwu36 · 2026-08-31

@jackkosaian , is the fix in?

### jackkosaian · 2026-09-01

Yes: https://github.com/NVIDIA/cutlass/blame/dc45f979ae336a235da1676b311f35efeb30149a/include/cutlass/subbyte_reference.h#L819
