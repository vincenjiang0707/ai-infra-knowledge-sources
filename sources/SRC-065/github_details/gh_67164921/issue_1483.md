# [Issue #1483] Illegal memory access for large enough shapes on 4D tensors GEMM

source: https://github.com/triton-lang/triton/issues/1483
state: open | updated: 2026-09-01T18:09:37Z
labels: help wanted

## 正文

Hi, I doubt this is a duplicate of https://github.com/openai/triton/issues/1058 because I am not overflowing on the program ids (largest PID should be `cdiv(8192, 16) * cdiv(8192, 32) = 131072` in my case).

I extended https://github.com/openai/triton/blob/main/python/triton/ops/matmul.py to support 4D tensors, e.g. of shapes (2, 8, 1024, 1024) and (2, 8, 1024, 512).

For large enough values in dimension 1 (while keeping all other dims equal),  a `CUDA error: an illegal memory access was encountered` is raised:

```
✅ Triton and Torch match
[M,N,K=8192, bs=1, n_head=30] triton TFLOPS: 190.21, ms: 173.412354
[M,N,K=8192, bs=1, n_head=30] cublas TFLOPS: 130.25, ms: 253.250565
[M,N,K=8192, bs=1, n_head=32] triton TFLOPS: 181.86, ms: 193.468414
[M,N,K=8192, bs=1, n_head=32] cublas TFLOPS: 127.34, ms: 276.293640
Traceback (most recent call last):
  File "/home/felix/test_triton/batched_gemm.py", line 227, in <module>
    benchmark(val, val, val, bs, n_head, provider)
  File "/home/felix/test_triton/batched_gemm.py", line 214, in benchmark
    ms, min_ms, max_ms = triton.testing.do_bench(lambda: matmul(a, b))
  File "/home/felix/triton/python/triton/testing.py", line 44, in do_bench
    torch.cuda.synchronize()
  File "/home/felix/miniconda3/envs/fx/lib/python3.9/site-packages/torch/cuda/__init__.py", line 688, in synchronize
    return torch._C._cuda_synchronize()
RuntimeError: CUDA error: an illegal memory access was encountered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.
```

Is it an issue in my implementation or expected at first glance? I have no issues on smaller shapes. This is on A100-SXM4-80GB on triton `main`.

---

Here is my kernel. You can see that the only change is grabbing a `pid_batch` and `pid_dim1`, and changing the offset to account the many GEMMs as we have 4D tensors.

```python
import torch

import triton
import triton.language as tl

from matmul_perf_model import early_config_prune, estimate_matmul_time


def init_to_zero(name):
    return lambda nargs: nargs[name].zero_()


def get_configs_io_bound():
    configs = []
    for num_stages in [2, 3, 4, 5, 6]:
        for block_m in [16, 32]:
            for block_k in [32, 64]:
                for block_n in [32, 64, 128, 256]:
                    num_warps = 2 if block_n <= 64 else 4
                    configs.append(
                        triton.Config({'BLOCK_M': block_m, 'BLOCK_N': block_n, 'BLOCK_K': block_k, 'SPLIT_K': 1},
                                      num_stages=num_stages, num_warps=num_warps))
                    # split_k
                    for split_k in [2, 4, 8, 16]:
                        configs.append(triton.Config({'BLOCK_M': block_m, 'BLOCK_N': block_n, 'BLOCK_K': block_k, 'SPLIT_K': split_k},
                                                     num_stages=num_stages, num_warps=num_warps, pre_hook=init_to_zero('C')))
    return configs


@triton.autotune(
    configs=[
        # basic configs for compute-bound matmuls
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 256, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=3, num_warps=8),
        triton.Config({'BLOCK_M': 256, 'BLOCK_N': 128, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=3, num_warps=8),
        triton.Config({'BLOCK_M': 256, 'BLOCK_N': 64, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 64, 'BLOCK_N': 256, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 128, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 64, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 64, 'BLOCK_N': 128, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 32, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 64, 'BLOCK_N': 32, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=5, num_warps=2),
        # good for int8
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 256, 'BLOCK_K': 128, 'SPLIT_K': 1}, num_stages=3, num_warps=8),
        triton.Config({'BLOCK_M': 256, 'BLOCK_N': 128, 'BLOCK_K': 128, 'SPLIT_K': 1}, num_stages=3, num_warps=8),
        triton.Config({'BLOCK_M': 256, 'BLOCK_N': 64, 'BLOCK_K': 128, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 64, 'BLOCK_N': 256, 'BLOCK_K': 128, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 128, 'BLOCK_K': 128, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 64, 'BLOCK_K': 64, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 64, 'BLOCK_N': 128, 'BLOCK_K': 64, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 32, 'BLOCK_K': 64, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 64, 'BLOCK_N': 32, 'BLOCK_K': 64, 'SPLIT_K': 1}, num_stages=5, num_warps=2),
    ] + get_configs_io_bound(),
    key=['M', 'N', 'K'],
    prune_configs_by={
        'early_config_prune': early_config_prune,
        'perf_model': estimate_matmul_time,
        'top_k': 10
    },
)
@triton.heuristics({
    'EVEN_K': lambda args: args['K'] % (args['BLOCK_K'] * args['SPLIT_K']) == 0,
})
@triton.jit
def matmul_kernel(
    # Pointers to matrices
    A,
    B,
    C,
    # Matrix dimensions
    M,
    N,
    K,
    # The stride variables represent how much to increase the ptr by when moving by 1
    # element in a particular dimension. E.g. stride_am is how much to increase a_ptr
    # by to get the element one row down (A has M rows)
    dim1,
    stride_batch_a,
    stride_batch_b,
    stride_batch_c,
    stride_dim1_a,
    stride_dim1_b,
    stride_dim1_c,
    stride_am,
    stride_ak,
    stride_bk,
    stride_bn,
    stride_cm,
    stride_cn,
    # Meta-parameters
    BLOCK_M: tl.constexpr,
    BLOCK_N: tl.constexpr,
    BLOCK_K: tl.constexpr,
    GROUP_M: tl.constexpr,
    SPLIT_K: tl.constexpr,
    EVEN_K: tl.constexpr,
):
    # matrix multiplication
    pid = tl.program_id(0)
    pid_z = tl.program_id(1)
    pid_first_dims = tl.program_id(axis=2)
    # pid_dim1 = tl.program_id(axis=3)

    grid_m = (M + BLOCK_M - 1) // BLOCK_M
    grid_n = (N + BLOCK_N - 1) // BLOCK_N
    # re-order program ID for better L2 performance
    width = GROUP_M * grid_n
    group_id = pid // width
    group_size = min(grid_m - group_id * GROUP_M, GROUP_M)
    pid_m = group_id * GROUP_M + (pid % group_size)
    pid_n = (pid % width) // (group_size)
    # do matrix multiplication
    rm = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    rn = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    ram = tl.max_contiguous(tl.multiple_of(rm % M, BLOCK_M), BLOCK_M)
    rbn = tl.max_contiguous(tl.multiple_of(rn % N, BLOCK_N), BLOCK_N)
    rk = pid_z * BLOCK_K + tl.arange(0, BLOCK_K)

    # pointer to the i-th matrix

    pid_batch = pid_first_dims // dim1 # (pid_first_dims + dim1 - 1) // dim1
    pid_dim1 = pid_first_dims % dim1

    a_ith_ptr = pid_batch * stride_batch_a + pid_dim1 * stride_dim1_a
    b_ith_ptr = pid_batch * stride_batch_b + pid_dim1 * stride_dim1_b
    c_ith_ptr = pid_batch * stride_batch_c + pid_dim1 * stride_dim1_c

    # pointers
    A = A + a_ith_ptr + (ram[:, None] * stride_am + rk[None, :] * stride_ak)
    B = B + b_ith_ptr + (rk[:, None] * stride_bk + rbn[None, :] * stride_bn)
    acc = tl.zeros((BLOCK_M, BLOCK_N), dtype=tl.float32)
    for k in range(K, 0, -BLOCK_K * SPLIT_K):
        if EVEN_K:
            a = tl.load(A)
            b = tl.load(B)
        else:
            a = tl.load(A, mask=rk[None, :] < k, other=0.)
            b = tl.load(B, mask=rk[:, None] < k, other=0.)
        acc += tl.dot(a, b)
        A += BLOCK_K * SPLIT_K * stride_ak
        B += BLOCK_K * SPLIT_K * stride_bk
    acc = acc.to(C.dtype.element_ty)
    # rematerialize rm and rn to save registers
    rm = pid_m * BLOCK_M + tl.arange(0, BLOCK_M)
    rn = pid_n * BLOCK_N + tl.arange(0, BLOCK_N)
    C = C + c_ith_ptr + (rm[:, None] * stride_cm + rn[None, :] * stride_cn)
    mask = (rm < M)[:, None] & (rn < N)[None, :]
    # handles write-back with reduction-splitting
    if SPLIT_K == 1:
        tl.store(C, acc, mask=mask)
    else:
        tl.atomic_add(C, acc, mask=mask)

def matmul(a, b):
    # checks constraints
    assert a.shape[-1] == b.shape[-2], "incompatible dimensions"
    assert a.is_contiguous(), "matrix A must be contiguous"
    assert b.is_contiguous(), "matrix B must be contiguous"

    assert len(a.shape) == 4, "4D kernel"
    assert len(b.shape) == 4, "4D kernel"
    batch_size_a, dim1_a, M, K = a.shape
    batch_size_b, dim1_b, K, N = b.shape
    assert (
        K % 32 == 0
    ), "We don't check memory-out-of-bounds with K so K must be divisible by BLOCK_K"
    # allocates output

    assert batch_size_a == batch_size_b, "only same batch size supported"
    assert dim1_a == dim1_b, "only same dim 1 is supported"

    c = torch.empty((batch_size_a, dim1_a, M, N), device=a.device, dtype=a.dtype)
    # 1D launch kernel where each block gets its own program.
    grid = lambda META: (
        triton.cdiv(M, META['BLOCK_M']) * triton.cdiv(N, META['BLOCK_N']),
        META['SPLIT_K'],
        batch_size_a * dim1_a,
        #dim1_a,
    )
    matmul_kernel[grid](
        a, b, c,
        M, N, K,
        dim1_a,
        a.stride(0), b.stride(0), c.stride(0),
        a.stride(1), b.stride(1), c.stride(1),
        a.stride(2), a.stride(3),
        b.stride(2), b.stride(3),
        c.stride(2), c.stride(3),
        GROUP_M=8
    )
    return c

#a = torch.rand((1, 16, 2048, 2048), dtype=torch.float16, device='cuda')
#b = torch.rand((1, 16, 2048, 2048), dtype=torch.float16, device='cuda')
a = torch.rand((2, 4, 1024, 1024), dtype=torch.float16, device='cuda')
b = torch.rand((2, 4, 1024, 1024), dtype=torch.float16, device='cuda')
triton_output = matmul(a, b)
torch_output = torch.matmul(a, b)

if torch.allclose(triton_output, torch_output):
    print("✅ Triton and Torch match")
else:
    print("❌ Triton and Torch differ")
    print(f"    Maxdiff: {torch.abs(torch_output - triton_output).max()}")
    num_diff = torch.sum(torch.abs(torch_output - triton_output) > 1e-5)
    total_items = torch.numel(torch_output)
    print(f"    Num diff: {num_diff} ({num_diff / total_items * 100:.2f} %)")

def benchmark(M, N, K, bs, n_head, provider):
    a = torch.randn((bs, n_head, M, K), device='cuda', dtype=torch.float16)
    b = torch.randn((bs, n_head, K, N), device='cuda', dtype=torch.float16)
    if provider == 'cublas':
        ms, min_ms, max_ms = triton.testing.do_bench(lambda: torch.matmul(a, b))
    if provider == 'triton':
        ms, min_ms, max_ms = triton.testing.do_bench(lambda: matmul(a, b))

    perf = lambda ms: bs * n_head * 2 * M * N * K * 1e-12 / (ms * 1e-3)
    print(f"[M,N,K={val}, bs={bs}, n_head={n_head}] {provider} TFLOPS: {perf(ms):.2f}, ms: {ms:.6f}")

#for bs in [1, 4, 8]:
#    for n_head in [16, 32, 48]:
#        for val in [2048, 4096, 8192]:

for bs in [1]:
    for n_head in [30, 32, 34, 36]:
        for val in [8192]:
            for provider in ["triton", "cublas"]:
                benchmark(val, val, val, bs, n_head, provider)
```

Thank you!

## 评论 (4)

### Profesor09 · 2023-04-09

import torch

import triton
import triton.language as tl

from matmul_perf_model import early_config_prune


def init_to_zero(nargs):
    return nargs.zero_()


def get_configs_io_bound():
    for num_stages in range(2, 7):
        for block_m in [16, 32]:
            for block_k in [32, 64]:
                for block_n in [32, 64, 128, 256]:
                    num_warps = 2 if block_n <= 64 else 4
                    yield triton.Config({'BLOCK_M': block_m, 'BLOCK_N': block_n, 'BLOCK_K': block_k, 'SPLIT_K': 1},
                                        num_stages=num_stages, num_warps=num_warps)
                    # split_k
                    for split_k in [2, 4, 8, 16]:
                        yield triton.Config({'BLOCK_M': block_m, 'BLOCK_N': block_n, 'BLOCK_K': block_k, 'SPLIT_K': split_k},
                                             num_stages=num_stages, num_warps=num_warps, pre_hook=init_to_zero)


@triton.autotune(
    configs=[
        # basic configs for compute-bound matmuls
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 256, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=3, num_warps=8),
        triton.Config({'BLOCK_M': 256, 'BLOCK_N': 128, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=3, num_warps=8),
        triton.Config({'BLOCK_M': 256, 'BLOCK_N': 64, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 64, 'BLOCK_N': 256, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK_N': 128, 'BLOCK_K': 32, 'SPLIT_K': 1}, num_stages=4, num_warps=4),
        triton.Config({'BLOCK_M': 128, 'BLOCK


### LeonxLJX · 2026-09-01

I'd like to take this one (`Illegal memory access for large enough shapes on 4D tensors `). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)

### LeonxLJX · 2026-09-01

I'd like to take this one (`Illegal memory access for large enough shapes on 4D tensors `). I'll dig into the root cause and follow up with a PR shortly. (claiming via @LeonxLJX)

### LeonxLJX · 2026-09-01

I'd like to take this one (`Illegal memory access for large enough shapes on 4D tensors `). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)
