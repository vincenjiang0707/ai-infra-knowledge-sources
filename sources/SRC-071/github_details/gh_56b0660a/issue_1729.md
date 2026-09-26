# [Issue #1729] [Feature Request] Improve layout when small fragments cause excessive thread replication

source: https://github.com/tile-ai/tilelang/issues/1729
state: closed | updated: 2026-08-21T06:47:04Z
labels: enhancement

## 正文

### Required prerequisites

- [x] I have searched the [Issue Tracker](https://github.com/tile-ai/tilelang/issues) that this hasn't already been reported. (comment there if it has.)

### Motivation

TileLang code:
```python
import tilelang
import tilelang.language as T


@tilelang.jit
def get_qwq():
    @T.prim_func
    def main(
        A: T.Tensor[(2, 2560), T.float32],
        B: T.Tensor[(2, 2560), T.float32],
        C: T.Tensor[(2, ), T.float32]
    ):
        with T.Kernel(1, threads=256):
            tx = T.get_thread_binding(0)

            C_local = T.alloc_fragment((2, ), T.float32)
            T.copy(C, C_local)

            for i, j in T.Parallel(2, 2560):
                if C_local[i] >= 0:
                    B[i, j] = A[i, j]

    return main


kernel = get_qwq()
print(kernel.get_kernel_source())
```

generated code:
```cuda
#include <tl_templates/cuda/gemm.h>
#include <tl_templates/cuda/copy.h>
#include <tl_templates/cuda/reduce.h>
#include <tl_templates/cuda/ldsm.h>
#include <tl_templates/cuda/threadblock_swizzle.h>
#include <tl_templates/cuda/debug.h>
#ifdef ENABLE_BF16
#include <tl_templates/cuda/cuda_bf16_fallbacks.cuh>
#endif

extern "C" __global__ void main_kernel(const float* __restrict__ A, float* __restrict__ B, const float* __restrict__ C);
extern "C" __global__ void __launch_bounds__(256, 1) main_kernel(const float* __restrict__ A, float* __restrict__ B, const float* __restrict__ C) {
  float C_local[1];
  C_local[0] = C[(((int)threadIdx.x) & 1)];
  if ((((int)threadIdx.x) >> 1) == 0) {
    #pragma unroll
    for (int i = 0; i < 640; ++i) {
      float4 v_ = *(float4*)(A + (((((int)threadIdx.x) & 1) * 2560) + (i * 4)));
      tl::store_global_128_conditional((&(B[(((((int)threadIdx.x) & 1) * 2560) + (i * 4))])), (*(uint4 *)(&(v_))), (0x0p+0f/*0.000000e+00*/ <= C_local[0]));
    }
  }
}
```

In the generated kernel, only threads 0 and 1 perform the global memory read/write, leaving most threads idle. This indicates a suboptimal layout and thread mapping, and there should be room to improve the layout.

### Solution

_No response_

### Alternatives

_No response_

### Additional context

_No response_

## 评论 (7)

### tzj-fxz · 2026-01-26

We can use `alloc_local` instead of `alloc_fragment` in this scenario.

### LJC00118 · 2026-01-26

Hi @tzj-fxz,

Thanks for the suggestion. While `alloc_local` works for this case, I think the real issue is layout inference.

This looks like a missed opportunity in layout inference: threads 0-127 handle row 0, threads 128-255 handle row 1. This gives 100% thread utilization with contiguous access.

`alloc_local` fixes this specific case, but for complex kernels, we need better automatic layout inference. The compiler should explore more layout and consider thread utilization + memory access patterns.

### tzj-fxz · 2026-01-31

@LJC00118 Your suggested layout is right in this case because there are no other operations of fragment `C_local` in `T.Parallel` loop.

In other cases of the read access of `C_local` (like changing `B[i, j] = A[i, j]` to `B[i, j] += C_local[i]`), the layout inferred by TileLang guarantees that no data races or duplicated writes in the dst buffer. The layout "threads 0-127 handle row 0, threads 128-255 handle row 1" may cause messy writes to `B[i, j]` because threads with even indices hold `C_local[0]` and threads with odd indices hold `C_local[1]`. In more scenarios where the layouts of fragment buffers are strictly determined by `T.gemm`, it is difficult to assume which thread holds which data.

In your case, it is suggested to manually use primitive `T.annotate_layout` to make sure your layout is correct and performant. No need to use `T.alloc_local` for this also causes ambiguity in `T.Parallel` loop. :)

### tzj-fxz · 2026-02-02

@LJC00118  By this PR https://github.com/tile-ai/tilelang/pull/1772, we can manually annotate a fully-replicated layout for `C_local` to leverage all threads' resources.

### LJC00118 · 2026-02-03

@tzj-fxz Thanks for the PR — it’s a helpful and practical workaround.

That said, I think it addresses the symptom rather than the root cause. The core issue here is not whether we use fully replicate, but whether layout inference chooses the right replicate.

In the ideal layout, 128 threads handle one row, and each thread only needs to hold one element of C. This corresponds to `replicate = 128`, rather than fully replicating across all threads. This layout is both correct and efficient, and it can already be expressed and verified via `annotate_layout`.

For example:
```python
import tilelang
import tilelang.language as T


def forward_layout_fn(i, j):
    forward_thread = i * 128 + (j // 4) % 128
    forward_local = j % 4 + j // 512 * 4
    return forward_thread, forward_local


@tilelang.jit
def get_qwq():
    @T.prim_func
    def main(
        A: T.Tensor[(2, 2560), T.float32],
        B: T.Tensor[(2, 2560), T.float32],
        C: T.Tensor[(2, ), T.float32]
    ):
        with T.Kernel(1, threads=256):
            tx = T.get_thread_binding(0)

            C_local = T.alloc_fragment((2, ), T.float32)
            T.copy(C, C_local)

            for i, j in T.Parallel(2, 2560, loop_layout=T.Fragment((2, 2560), forward_fn=forward_layout_fn)):
                if C_local[i] >= 0:
                    B[i, j] = A[i, j]

    return main


kernel = get_qwq()
print(kernel.get_kernel_source())
```
If we change the shape from `(2, 2560)` to `(32, 160)`, the required `replicate` can be reduced to 8, still without fully replicate.

So the real issue is likely that **layout inference picks an inappropriate replicate value**, and perhaps layout inference itself could be refactored or further optimized.


### LeiWang1999 · 2026-02-09

layout inference relies on a heuristic-based policy. Introducing a specific policy for this case might regress the performance of other operators. We may need to explore an ISL-based layout solving strategy in the future.

### LeiWang1999 · 2026-08-21

now we introduced io-aware cost model (opt-in) which can infer the expected layout for this code, to enable it:

```python
@tilelang.jit(
pass_configs={
tilelang.PassConfigKey.TL_LAYOUT_COST_MODEL: "io-aware"
}
)
```
