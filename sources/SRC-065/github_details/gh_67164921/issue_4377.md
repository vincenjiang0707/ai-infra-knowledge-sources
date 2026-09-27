# [Issue #4377] How to make compiler execute Instruction reordering properly to avoid register spilling

source: https://github.com/triton-lang/triton/issues/4377
state: closed | updated: 2026-09-25T15:49:37Z
labels: 

## 正文

I implemented a element-wise op.

```python
@triton.jit
def silu_grad(dy, x):
    dtype = x.dtype
    dy = dy.to(tl.float32)
    x = x.to(tl.float32)
    s_acc = fast_dividef(1.0, 1.0 + fast_expf(-x))
    return (dy * s_acc * (1.0 + x * (1.0 - s_acc))).to(dtype)

ds = silu_grad(dp, qk) # BLOCK_M x BLOCK_N
```

For triton tensor x [128 ⨉ 128], the Intermediate variable x, s_acc, and  (1.0 + x * (1.0 - s_acc)) will occupy the register. 
Because the 128 ⨉ 128 element calculations are divided into 4 warps (for example) and the silu_grad calculations are sequentially expanded into PTX and SASS, the lack of instruction reordering causes these "x, s_acc, and  (1.0 + x * (1.0 - s_acc))" occupying the register and leas to register spilling.

<img width="1052" alt="image" src="https://github.com/user-attachments/assets/ef86106a-3fc1-4ea9-9020-016eb6f15c3d">


## 评论 (6)

### Jokeren · 2024-07-24

@manman-ren @htyu Have you encountered similar problems? 

### manman-ren · 2024-07-24

I wonder where the unrolling happens, at ttgir level, or at llvm level. Do you have the ttgir for this kernel?

### haojiwei · 2024-07-24

> I wonder where the unrolling happens, at ttgir level, or at llvm level. Do you have the ttgir for this kernel?

There are two calls

```
      %157 = triton_gpu.convert_layout %153 : (tensor<64x64xbf16, #shared>) -> tensor<64x64xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>>
      %158 = triton_gpu.convert_layout %155 : (tensor<64x256xbf16, #shared>) -> tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>>
      %159 = tt.dot %157, %158, %arg38 {allowTF32 = true, maxNumImpreciseAcc = 0 : i32} : tensor<64x64xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>> * tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>> -> tensor<64x256xf32, #mma>
      %160 = triton_gpu.convert_layout %55 : (tensor<64x256xbf16, #shared>) -> tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>>
      %161 = triton_gpu.convert_layout %156 : (tensor<256x64xbf16, #shared1>) -> tensor<256x64xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>>
      %162 = tt.dot %160, %161, %cst {allowTF32 = false, maxNumImpreciseAcc = 0 : i32} : tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>> * tensor<256x64xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>> -> tensor<64x64xf32, #mma>
      %163 = arith.truncf %162 : tensor<64x64xf32, #mma> to tensor<64x64xbf16, #mma>
      %164 = arith.extf %163 : tensor<64x64xbf16, #mma> to tensor<64x64xf32, #mma>
      %165 = tt.extern_elementwise %cst_0, %150 {libname = "libdevice", libpath = "/home/username/.local/lib/python3.10/site-packages/triton/language/../third_party/cuda/lib/libdevice.10.bc", pure = true, symbol = "__nv_fast_fdividef"} : (tensor<64x64xf32, #mma>, tensor<64x64xf32, #mma>) -> tensor<64x64xf32, #mma>
      %166 = arith.mulf %164, %165 : tensor<64x64xf32, #mma>
      %167 = arith.subf %cst_0, %165 : tensor<64x64xf32, #mma>
      %168 = arith.mulf %147, %167 : tensor<64x64xf32, #mma>
      %169 = arith.addf %168, %cst_0 : tensor<64x64xf32, #mma>
      %170 = arith.mulf %166, %169 : tensor<64x64xf32, #mma>
      %171 = arith.truncf %170 : tensor<64x64xf32, #mma> to tensor<64x64xbf16, #mma>
      %172 = triton_gpu.convert_layout %171 : (tensor<64x64xbf16, #mma>) -> tensor<64x64xbf16, #shared>
      %173 = triton_gpu.convert_layout %172 : (tensor<64x64xbf16, #shared>) -> tensor<64x64xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>>
      %174 = triton_gpu.convert_layout %142 : (tensor<64x256xbf16, #shared>) -> tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>>
      %175 = tt.dot %173, %174, %arg39 {allowTF32 = true, maxNumImpreciseAcc = 0 : i32} : tensor<64x64xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>> * tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>> -> tensor<64x256xf32, #mma>
```

```
      %149 = triton_gpu.convert_layout %111 : (tensor<64x256xbf16, #shared>) -> tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>>
      %150 = triton_gpu.convert_layout %144 : (tensor<256x64xbf16, #shared1>) -> tensor<256x64xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>>
      %151 = tt.dot %149, %150, %cst {allowTF32 = false, maxNumImpreciseAcc = 0 : i32} : tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>> * tensor<256x64xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>> -> tensor<64x64xf32, #mma>
      %152 = arith.truncf %151 : tensor<64x64xf32, #mma> to tensor<64x64xbf16, #mma>
      %153 = arith.extf %152 : tensor<64x64xbf16, #mma> to tensor<64x64xf32, #mma>
      %154 = arith.extf %148 : tensor<64x64xbf16, #mma> to tensor<64x64xf32, #mma>
      %155 = arith.subf %cst, %154 : tensor<64x64xf32, #mma>
      %156 = tt.extern_elementwise %155 {libname = "libdevice", libpath = "/home/username/.local/lib/python3.10/site-packages/triton/language/../third_party/cuda/lib/libdevice.10.bc", pure = true, symbol = "__nv_fast_expf"} : (tensor<64x64xf32, #mma>) -> tensor<64x64xf32, #mma>
      %157 = arith.addf %156, %cst_0 : tensor<64x64xf32, #mma>
      %158 = tt.extern_elementwise %cst_0, %157 {libname = "libdevice", libpath = "/home/username/.local/lib/python3.10/site-packages/triton/language/../third_party/cuda/lib/libdevice.10.bc", pure = true, symbol = "__nv_fast_fdividef"} : (tensor<64x64xf32, #mma>, tensor<64x64xf32, #mma>) -> tensor<64x64xf32, #mma>
      %159 = arith.mulf %153, %158 : tensor<64x64xf32, #mma>
      %160 = arith.subf %cst_0, %158 : tensor<64x64xf32, #mma>
      %161 = arith.mulf %154, %160 : tensor<64x64xf32, #mma>
      %162 = arith.addf %161, %cst_0 : tensor<64x64xf32, #mma>
      %163 = arith.mulf %159, %162 : tensor<64x64xf32, #mma>
      %164 = arith.truncf %163 : tensor<64x64xf32, #mma> to tensor<64x64xbf16, #mma>
      %165 = triton_gpu.convert_layout %164 : (tensor<64x64xbf16, #mma>) -> tensor<64x64xbf16, #shared>
      %166 = triton_gpu.convert_layout %165 : (tensor<64x64xbf16, #shared>) -> tensor<64x64xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>>
      %167 = triton_gpu.convert_layout %142 : (tensor<64x256xbf16, #shared>) -> tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>>
      %168 = tt.dot %166, %167, %arg38 {allowTF32 = true, maxNumImpreciseAcc = 0 : i32} : tensor<64x64xbf16, #triton_gpu.dot_op<{opIdx = 0, parent = #mma, kWidth = 2}>> * tensor<64x256xbf16, #triton_gpu.dot_op<{opIdx = 1, parent = #mma, kWidth = 2}>> -> tensor<64x256xf32, #mma>
```


### manman-ren · 2024-07-25

%163 = arith.mulf %159, %162 : tensor<64x64xf32, #mma>
will become a list of mul.f32 when lowering from ttgir.
Is that what you refer as excessive instruction unrolling?

### haojiwei · 2024-07-28

> %163 = arith.mulf %159, %162 : tensor<64x64xf32, #mma> will become a list of mul.f32 when lowering from ttgir. Is that what you refer as excessive instruction unrolling?


@manman-ren @Jokeren  Hello, I made an example. There is an element-wise operator that requires a few registers (two or three registers) to hold the intermediate result after the matrix multiplication calculation. 

```python
import torch
import triton
import triton.language as tl

try:
    from triton.language.extra.cuda.libdevice import fast_dividef, fast_expf
except ImportError:
    from triton.language.math import fast_dividef, fast_expf


@triton.jit
def element_op(dy, x):
    dtype = x.dtype
    dy = dy.to(tl.float32)
    x = x.to(tl.float32)
    s_acc = fast_dividef(1.0, 1.0 + fast_expf(-x))
    return (dy * s_acc * (1.0 + x * (1.0 - s_acc))).to(dtype)


@triton.jit
def fused_kernel(
    A, B, C, D, 
    M, N, K, 
    stride_ab, stride_am, stride_ak, 
    stride_bb, stride_bk, stride_bn, 
    stride_cb, stride_cm, stride_cn,
    stride_db, stride_dm, stride_dn,
    BLOCK_M: tl.constexpr, 
    BLOCK_N: tl.constexpr, 
    BLOCK_K: tl.constexpr,
    WITH_ELEMENT_OP: tl.constexpr,
):
    offset_b = tl.program_id(1)
    start_m = tl.program_id(0)

    offset_m = start_m * BLOCK_M + tl.arange(0, BLOCK_M)
    offset_n = tl.arange(0, BLOCK_N)
    offset_k = tl.arange(0, BLOCK_K)

    A_ptrs = A + offset_b * stride_ab + offset_m[:, None] * stride_am + offset_k[None, :] * stride_ak
    B_ptrs = B + offset_b * stride_bb + offset_k[:, None] * stride_bk + offset_n[None, :] * stride_bn
    C_ptrs = C + offset_b * stride_cb + offset_m[:, None] * stride_cm + offset_n[None, :] * stride_cn
    D_ptrs = D + offset_b * stride_db + offset_m[:, None] * stride_dm + offset_n[None, :] * stride_dn

    a = tl.load(A_ptrs, mask=offset_m[:, None] < M, other=0.0)

    for start_N in range(0, BLOCK_N, BLOCK_N):
        b = tl.load(B_ptrs, mask=offset_n[None, :] < N, other=0.0)
        c = tl.load(C_ptrs, mask=offset_n[None, :] < N, other=0.0)
        q = tl.dot(a, b).to(a.dtype)

        if WITH_ELEMENT_OP:
            q = element_op(q, c)
        
        tl.store(D_ptrs, q, mask=offset_n[None, :] < N)

        B_ptrs += BLOCK_N * stride_bn
        C_ptrs += BLOCK_N * stride_cn
        D_ptrs += BLOCK_N * stride_dn


if __name__ == "__main__":
    device = torch.device("cuda")
    BS, M, N, K = 1, 1024, 1024, 128
    dtype = torch.float16
    A = torch.randn(BS, M, K, dtype=dtype, device=device)
    B = torch.randn(BS, K, N, dtype=dtype, device=device)
    C = torch.randn(BS, M, N, dtype=dtype, device=device)
    D = torch.randn(BS, M, N, dtype=dtype, device=device)

    BLOCK_M = 128
    BLOCK_N = 128
    BLOCK_K = K
    grid = lambda META: (
        triton.cdiv(M, META["BLOCK_M"]), BS
    )

    with_element_op = fused_kernel[grid](
        A, B, C, D,
        M, N, K,
        A.stride(0), A.stride(1), A.stride(2),
        B.stride(0), B.stride(1), B.stride(2),
        C.stride(0), C.stride(1), C.stride(2),
        D.stride(0), D.stride(1), D.stride(2),
        BLOCK_M=BLOCK_M,
        BLOCK_N=BLOCK_N,
        BLOCK_K=BLOCK_K,
        WITH_ELEMENT_OP=True,
        num_stages=3,
        num_warps=4,
    )
    print(f"{with_element_op.n_spills=}")

    without_element_op = fused_kernel[grid](
        A, B, C, D,
        M, N, K,
        A.stride(0), A.stride(1), A.stride(2),
        B.stride(0), B.stride(1), B.stride(2),
        C.stride(0), C.stride(1), C.stride(2),
        D.stride(0), D.stride(1), D.stride(2),
        BLOCK_M=BLOCK_M,
        BLOCK_N=BLOCK_N,
        BLOCK_K=BLOCK_K,
        WITH_ELEMENT_OP=False,
        num_stages=3,
        num_warps=4,
    )
    print(f"{without_element_op.n_spills=}")
```

output:

```
with_element_op.n_spills=14
without_element_op.n_spills=0
```

On the A100 GPU, the element_op compiled by triton has a high degree of instruction parallelism, but leads to register spilling. 

I wonder how to avoid calculating the Intermediate variable `s_acc` and other implicit intermediate variable in registers corresponding to the x [128 ⨉ 128] all at once. The ideal situation is to compute partial block (for example [16 ⨉ 16]) of the intermediate variables and the result of `element_op` returned value in registers until the whole block [128 ⨉ 128]  is computed iteratively.

### ThomasRaoux · 2026-09-25

sched4reg option now allows reducing pressure at the scheduler level
