# [Issue #3534] maximum_active_blocks wrappers pass int into CudaHostAdapter* and no longer compile

source: https://github.com/NVIDIA/cutlass/issues/3534
state: open | updated: 2026-09-14T13:53:24Z
labels: CUTLASS C++

## 正文

### Description

Since 3.4, `GemmUniversalBase::maximum_active_blocks` takes a `CudaHostAdapter*`:

```cpp
// include/cutlass/gemm/device/gemm_universal_base.h:350
static int maximum_active_blocks(CudaHostAdapter *cuda_adapter = nullptr)
```

but the 2.x-style device wrappers still declare the pre-3.4 signature `(int smem_capacity = -1)` and forward the int into that pointer parameter, which does not convert:

```cpp
static int maximum_active_blocks(int smem_capacity = -1) {
  return UnderlyingOperator::maximum_active_blocks(smem_capacity);   // int -> CudaHostAdapter*: error
}
```

Calling any of these wrappers fails to compile:

```
error: argument of type "int" is incompatible with parameter of type "cutlass::CudaHostAdapter *"
```

Affected call sites (all forwarding `smem_capacity`):

- `gemm/device/gemm_universal.h:393-394`
- `gemm/device/gemm_universal_adapter.h:738-739` (2.x alias path)
- `gemm/device/rank_k.h:462`
- `gemm/device/rank_2k.h:499`
- `gemm/device/symm.h:554`
- `gemm/device/gemm_universal_with_broadcast.h:337`
- `gemm/device/gemm_universal_streamk_with_broadcast.h:337`
- `gemm/device/gemm_universal_with_absmax.h:355`
- `gemm/device/gemm_with_k_reduction.h:366`
- `gemm/device/gemm_layernorm_mainloop_fusion.h:336-337`

The 3.x adapter (`gemm_universal_adapter.h:270`) already updated its own declaration correctly (`maximum_active_blocks(int /* smem_capacity */ = -1)` ignoring the value), so only these forwarders were missed. Nothing in-tree calls them anymore (the profiler moved to the new API), which is why CI does not see it.

Reproduction: compile a TU that calls e.g.

```cpp
#include "cutlass/gemm/device/gemm.h"
using Gemm = cutlass::gemm::device::Gemm<float, cutlass::layout::ColumnMajor,
                                         float, cutlass::layout::ColumnMajor,
                                         float, cutlass::layout::RowMajor>;
int n = Gemm::maximum_active_blocks();
```

with nvcc or g++ against the current headers; it errors at the forwarded argument.

### Suggested fix

Drop the unused parameter in the ten wrappers to match the base signature (`maximum_active_blocks()` with no arguments), mirroring what `gemm_universal_adapter.h:270` already does.


## 评论 (2)

### VaggelisGian · 2026-08-25

Scope refinement while preparing a fix: of the ten listed forwarders, seven resolve through primaries that inherit `GemmUniversalBase` (gemm_universal, gemm_universal_adapter's 2.x path, the two with-broadcast wrappers, absmax, k-reduction, layernorm-fusion) and are pure signature fixes. The rank_k / rank_2k / symm column-major-output forwarders are a different case: their primary specializations never provided `maximum_active_blocks` anywhere (they do not derive `GemmUniversalBase`), so those three name a nonexistent member and need an API decision (add the query to the primaries, or remove the dead forwarders) rather than a signature drop.

### chrisXYZhang · 2026-09-14

Dear maintainer. Is there anyone working on this one? otherwise, I would like to work on this one. Thanks
