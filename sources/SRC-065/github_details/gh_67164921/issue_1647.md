# [Issue #1647] Calculate tl.dot, the output is the matrix of col major, but the result is wrong

source: https://github.com/triton-lang/triton/issues/1647
state: open | updated: 2026-09-01T18:09:36Z
labels: help wanted

## 正文

My test code is following:

```
def test_dot(M_, N_, K_, num_warps_): 

      @triton.autotune(
             configs=[triton.Config({'BLOCK_M': M_, 'BLOCK_N': N_, 'BLOCK_K': K_}, num_stages=1, num_warps=num_warps_)],
             key=[]
       )
      @triton.jit
       def matmul_kernel(
             a_ptr, b_ptr, c_ptr, M, N, K,
             BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr
       ):
            offs_am = tl.arange(0, BLOCK_M)
            offs_bn = tl.arange(0, BLOCK_N)
            offs_k = tl.arange(0, BLOCK_K)

            a_ptrs = a_ptr + (offs_am[:, None] * K + offs_k[None, :])
            b_ptrs = b_ptr + (offs_k[:, None] * N + offs_bn[None, :])
 
            a = tl.load(a_ptrs)
            b = tl.load(b_ptrs)

            c = tl.dot(a, b, allow_tf32 = False)
            
            c_ptrs = c_ptr + 1 * offs_am[:, None] + M * offs_bn[None, :]
            tl.store(c_ptrs, c)

     def  matmul(a, b):
            c = torch.empty((M_, N_), device = a.device, dtype = a.dtype)
            c = torch.as_strided(c, (M_, N_), c.stride()[::-1])
            grid = lambda META: (
                  triton.cdiv(M_, M_) * triton.cdiv(N_, N_),
            )
            matmul_kernel[grid](
                     a, b, c,
                     M_, N_, K_,
            )
           return c

    torch.manual_seed(0)
    a = torch.randn(M_, K_, dtype = torch.float).cuda()
    b = torch.randn(K_, N_, dtype = torch.float).cuda()
    triton_output = matmul(a, b).cpu()
    torch_output = torch.matmul(a, b).cpu()
    assert triton.testing.allclose(triton_output, torch_output), (triton_output, torch_output)
```

But when M!=N, the triton output will be different with torch_output. If `c_ptrs = c_ptr + N * offs_am[:, None] + 1 * offs_bn[None, :]`, which means the output of tl.dot is row major, the results are equal.

I checked the generated ttgir, to confirm that the output of tl.dot is col major or the order is {0 ,1}:
<img width="1824" alt="4F73D3C0-008C-4c0f-95BE-F392C05351CB" src="https://github.com/openai/triton/assets/29512097/62c5e1b8-eb2a-4439-b041-7fab19c599dc">


## 评论 (6)

### Jokeren · 2023-05-10

> But when M!=N, the triton output will be different with torch_output. 

It's very unlikely now, but we could check. Please provide the full script.

### yushinliu · 2023-05-11

Full script is like below:

```
import torch
import numpy as np

import triton
import triton.language as tl
import pytest

@pytest.mark.parametrize("M_, N_, K_, num_warps_",
[(32, 16, 16, 1)])
def test_dot(M_, N_, K_, num_warps_): 

      @triton.autotune(
             configs=[triton.Config({'BLOCK_M': M_, 'BLOCK_N': N_, 'BLOCK_K': K_}, num_stages=1, num_warps=num_warps_)],
             key=[]
       )
      @triton.jit
       def matmul_kernel(
             a_ptr, b_ptr, c_ptr, M, N, K,
             BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr, BLOCK_K: tl.constexpr
       ):
            offs_am = tl.arange(0, BLOCK_M)
            offs_bn = tl.arange(0, BLOCK_N)
            offs_k = tl.arange(0, BLOCK_K)

            a_ptrs = a_ptr + (offs_am[:, None] * K + offs_k[None, :])
            b_ptrs = b_ptr + (offs_k[:, None] * N + offs_bn[None, :])
 
            a = tl.load(a_ptrs)
            b = tl.load(b_ptrs)

            c = tl.dot(a, b, allow_tf32 = False)
            
            c_ptrs = c_ptr + 1 * offs_am[:, None] + M * offs_bn[None, :]
            tl.store(c_ptrs, c)

     def  matmul(a, b):
            c = torch.empty((M_, N_), device = a.device, dtype = a.dtype)
            c = torch.as_strided(c, (M_, N_), c.stride()[::-1])
            grid = lambda META: (
                  triton.cdiv(M_, M_) * triton.cdiv(N_, N_),
            )
            matmul_kernel[grid](
                     a, b, c,
                     M_, N_, K_,
            )
           return c

    torch.manual_seed(0)
    a = torch.randn(M_, K_, dtype = torch.float).cuda()
    b = torch.randn(K_, N_, dtype = torch.float).cuda()
    triton_output = matmul(a, b).cpu()
    torch_output = torch.matmul(a, b).cpu()
    assert triton.testing.allclose(triton_output, torch_output), (triton_output, torch_output)
````

and you can use pytest to execute.

### ptillet · 2023-05-11

To be fair I don't think we have unit tests for it 😬 I'll take a look tomorrow.

### weixingzhang · 2023-05-31

I realized it is probably a bug in test script instead of in triton when I was checking generated IR. The stride for C was incorrect. The test will pass with the code change below.

    c = torch.empty((N_, M_), device = a.device, dtype = a.dtype)

### LeonxLJX · 2026-09-01

I'd like to take this one (`Calculate tl.dot, the output is the matrix of col major, but`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)

### LeonxLJX · 2026-09-01

I'd like to take this one (`Calculate tl.dot, the output is the matrix of col major, but`). I'll look into the root cause and follow up with a PR. (claiming via @LeonxLJX)
