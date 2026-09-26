# [Issue #3606] [BUG] NVCC 13.3 cudafe++ explodes host code for structured bindings of CuTe TMA tuples

source: https://github.com/NVIDIA/cutlass/issues/3606
state: open | updated: 2026-09-10T05:13:51Z
labels: CUTLASS C++

## 正文

### Which component has the problem?

CUTLASS C++

### Bug Report

**Describe the bug**

With CUDA NVCC 13.3.73, using a structured binding to unpack a tuple of CuTe TMA copy objects and then using the binding names in kernel template arguments causes `cudafe++` to generate an unexpectedly large host-side `.cudafe1.cpp` file.

The same source compiles successfully with NVCC 13.0.88. With NVCC 13.3.73, replacing the structured binding with an ordinary tuple variable plus `std::get<N>` also compiles successfully.

This reproduces with current CUTLASS `main` at `147295a3d4b75f3aeff247c25b8927cea9a7006a` (version header reports 4.8.0), so it does not appear to be fixed by a newer CuTe header revision. The evidence points to a CUDA 13.3 `cudafe++` regression, but I am reporting it here because the reproducer uses public CuTe TMA types.

**Steps/Code to reproduce bug**

```cuda
#include <tuple>
#include <cute/tensor.hpp>

using namespace cute;

template <class Tensor>
auto make_three_tmas(Tensor tensor) {
  using T = bfloat16_t;
  using KAtom = GMMA::Layout_K_SW128_Atom<T>;
  using MNAtom = GMMA::Layout_MN_SW128_Atom<T>;
  using QLayout = decltype(tile_to_shape(KAtom{}, make_shape(_128{}, _192{})));
  using KVLayout = decltype(tile_to_shape(KAtom{}, make_shape(_128{}, _192{}, _2{})));
  using YLayout = decltype(tile_to_shape(MNAtom{}, make_shape(_64{}, _128{})));

  auto q = make_tma_copy(SM90_TMA_LOAD{}, tensor, QLayout{});
  auto kv = make_tma_copy(SM90_TMA_LOAD{}, tensor, take<0, 2>(KVLayout{}));
  auto y = make_tma_copy(SM90_TMA_STORE{}, tensor, YLayout{});
  return std::make_tuple(q, kv, y);
}

template <class Q, class KV, class Y>
__global__ void probe(Q, KV, Y) {}

void reproduce(void* ptr, int rows, int cols, int heads, int ld) {
  using T = bfloat16_t;
  auto tensor = make_tensor(make_gmem_ptr(static_cast<T*>(ptr)),
                            make_shape(rows, cols, heads),
                            make_stride(ld, _1{}, cols));
#ifdef WORKAROUND
  auto tmas = make_three_tmas(tensor);
  auto q = std::get<0>(tmas);
  auto kv = std::get<1>(tmas);
  auto y = std::get<2>(tmas);
#else
  auto [q, kv, y] = make_three_tmas(tensor);
#endif
  auto kernel = probe<decltype(q), decltype(kv), decltype(y)>;
  kernel<<<1, 1>>>(q, kv, y);
}
```

Compile from a CUTLASS checkout:

```bash
nvcc -std=c++20 -O3 \
  -gencode arch=compute_90a,code=sm_90a \
  --expt-relaxed-constexpr \
  -DCUTE_SM90_EXTENDED_MMA_SHAPES_ENABLED \
  -Iinclude --keep --keep-dir keep \
  -c repro.cu -o repro.o
```

The workaround build adds `-DWORKAROUND`.

Measured results with the public reproducer:

| NVCC | Source form | Result | Generated `repro.cudafe1.cpp` |
| --- | --- | --- | ---: |
| 13.0.88 | structured binding | succeeds | 13,135,532 bytes |
| 13.3.73 | structured binding | stopped after exceeding a 64 MiB safety limit | >64 MiB |
| 13.3.73 | `std::get` workaround | succeeds | 13,446,890 bytes |

The 13.3 failing process was intentionally terminated once its generated host file exceeded 64 MiB to avoid unbounded disk usage. In the original larger translation unit, it produced a roughly 29 GB `.cudafe1.cpp` file before subsequent host compiler parse errors.

**Expected behavior**

NVCC 13.3 should compile the structured-binding form as NVCC 13.0 does, without expanding the bound CuTe types repeatedly into a huge generated host source file.

**Environment details**

- Environment location: bare metal
- OS: TencentOS Server 4, Linux x86_64
- Host compiler: GCC 12.3.1
- Failing compiler: CUDA NVCC 13.3.73
- Working comparison compiler: CUDA NVCC 13.0.88
- CUTLASS: current `main`, commit `147295a3d4b75f3aeff247c25b8927cea9a7006a`, version 4.8.0
- C++ standard: C++20
- Target: `sm_90a`

**Additional context**

The original failure was first observed with GCC 14.3, but it also reproduces with GCC 12.3.1. Keeping the tuple object named and extracting its elements with `std::get<N>` avoids the CUDA 13.3 front-end expansion while preserving the types and generated kernel behavior.

If this is best tracked directly by the CUDA compiler team, guidance or internal routing to the appropriate NVCC owners would be appreciated.


## 评论 (2)

### RobotGF · 2026-09-10

Update: I retested the public reproducer with **CUDA Toolkit 13.4 Update 1**, released on 2026-09-09. Its NVCC component reports:

```
Cuda compilation tools, release 13.4, V13.4.59
Build cuda_13.4.r13.4/compiler.38657139_0
```

Using the same CUTLASS `main` commit (`147295a3d4b75f3aeff247c25b8927cea9a7006a`) and GCC 12.3.1:

| NVCC | Source form | Result | Generated `repro.cudafe1.cpp` |
| --- | --- | --- | ---: |
| 13.4.59 | structured binding | stopped after exceeding the 64 MiB safety limit in 22.24 s | >64 MiB |
| 13.4.59 | `std::get` workaround | succeeds in 36.65 s | 13,232,759 bytes |

So the `cudafe++` expansion regression is still present in CUDA 13.4 Update 1; the workaround remains effective.


### RobotGF · 2026-09-10

Further isolation points to the tuple-like structured-binding type printer in `cudafe++`, rather than CUTLASS/CuTe semantics or the host compiler.

I passed the exact same public repro preprocessed input (`repro.cpp4.ii`) directly to each `cudafe++` binary:

| `cudafe++` | EDG front end | Result | Generated host C++ |
| --- | --- | --- | ---: |
| 13.0.88 | 6.7 | succeeds | 13,135,720 bytes |
| 13.1.115 | 6.7 | succeeds | 13,136,458 bytes |
| 13.2.86 | 6.7 | succeeds | 13,133,760 bytes |
| 13.3.33 | 6.8 | stopped at safety limit | >64 MiB |
| 13.3.73 | 6.8 | stopped at safety limit | >64 MiB |
| 13.4.59 | 6.8 | stopped at safety limit | >64 MiB |

The first observed regression is therefore the initial CUDA 13.3 compiler build. The EDG 6.7 to 6.8 change correlates with its introduction, although this alone does not establish whether the defect is in EDG itself or NVIDIA's CUDA-specific integration.

Generated-code comparison on the identical input is particularly revealing:

* 13.2.86 emits a 2,415-byte kernel-instantiation line containing concrete `cute::TiledCopy<...>` types. The entire file contains 151 occurrences of `tuple_element`.
* 13.3.33 emits an incomplete 56,050,392-byte kernel-instantiation line beginning with `std::tuple_element<0, std::tuple<...>>`. That partial file already contains 660,490 occurrences of `tuple_element`.

Additional syntax tests with NVCC 13.4.59 and the current CUTLASS `main`:

| Form | Result |
| --- | --- |
| `std::tuple` + structured binding + `decltype(binding)` | fails / expands |
| `cute::tuple` + structured binding + `decltype(binding)` | fails / expands |
| Plain aggregate return + structured binding + `decltype(binding)` | succeeds |
| `std::apply` with deduced lambda parameters | succeeds |
| Helper function that deduces the kernel template arguments from values | succeeds |

This matches the C++ structured-binding rules: tuple-like decomposition gives each binding a referenced type based on `tuple_element<I, E>::type`, while aggregate decomposition uses the declared member type. In 13.3+, `cudafe++` appears to preserve and recursively print the former type expression instead of canonicalizing it before serializing the explicit CUDA kernel template-id.

A compiler-friendly workaround that preserves the original call-site syntax is therefore to return a plain aggregate rather than a tuple:

```cpp
template<class Q, class KV, class Y>
struct TmaBundle { Q q; KV kv; Y y; };

auto [q, kv, y] = make_tma_bundle(...);
auto kernel = probe<decltype(q), decltype(kv), decltype(y)>;
```

I also tested this form in the larger source: NVCC 13.3.73 host generation succeeds and returns to the normal ~13 MiB output size; a full NVCC 13.4.59 compile succeeds as well.

