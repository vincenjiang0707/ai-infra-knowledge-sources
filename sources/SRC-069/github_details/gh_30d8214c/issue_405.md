# [Issue #405] CUDA Illegal Instruction in test_k_grouped_gemm_contiguous

source: https://github.com/deepseek-ai/DeepGEMM/issues/405
state: open | updated: 2026-09-13T03:24:57Z
labels: 

## 正文

I encountered a CUDA kernel error while running the `test_k_grouped_gemm_contiguous` test with the matrix dimensions explicitly set to:

* `M = 768`
* `N = 1536`

The test fails with the following error:

```text
torch.AcceleratorError: CUDA error: an illegal instruction was encountered
```

The error appears to originate from a CUDA kernel execution. Since CUDA errors can be reported asynchronously, the reported stack trace may not point to the actual source of the failure.

For debugging, I also considered using:

```bash
CUDA_LAUNCH_BLOCKING=1
```

and enabling device-side assertions with `TORCH_USE_CUDA_DSA`.

### Question

Is the `M=768, N=1536` shape combination currently supported by the grouped GEMM implementation?

If this shape is expected to be supported, could there be a kernel configuration or shape-related issue causing the illegal instruction?

### Environment

* Test: `test_k_grouped_gemm_contiguous`
* M: `768`
* N: `1536`
* Error: `CUDA error: an illegal instruction was encountered`


## 评论 (2)

### PavelPaha · 2026-08-25

Hi @henny-bee, this has already been fixed on the current main branch by:
https://github.com/deepseek-ai/DeepGEMM/commit/1f6f3f378920ccb5cc036ef43eb3f5972e921713

### XFDG · 2026-09-13

Hi, I verified this on the current main branch (`66081d4c`) on an NVIDIA B200 (SM100) with CUDA 13.1.

Using 8 small K groups with the reported `M=768, N=1536` shape, 50/50 synchronized `k_grouped_fp8_gemm_tn_contiguous` launches completed without an illegal instruction. The output stayed finite and bitwise deterministic across all launches. This confirms that the tensor-map race fix in `1f6f3f378920ccb5cc036ef43eb3f5972e921713` covers this failure on current main.
