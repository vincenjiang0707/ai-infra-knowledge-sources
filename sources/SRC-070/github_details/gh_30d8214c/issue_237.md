# [Issue #237] [Bug] k_grouped_fp8_gemm_nt_contiguous crashes with n = 768 on H100

source: https://github.com/deepseek-ai/DeepGEMM/issues/237
state: open | updated: 2025-12-05T16:02:41Z
labels: 

## 正文



First of all, thank you for the amazing work on DeepGEMM — it's been extremely helpful.
While integrating DeepGEMM into a backward pass implementation, I encountered a reproducible crash when running the **k-grouped FP8 GEMM** with **N = 768**.

---

## **❗ Error**

Running DeepGEMM with the following shape causes a CUDA illegal instruction error:

```
RuntimeError: CUDA driver error (csrc/apis/../jit_kernels/impls/sm90_fp8_gemm_1d1d.hpp:65): 715 
(CUDA_ERROR_ILLEGAL_INSTRUCTION, an illegal instruction was encountered)
```

---

## **🔁 Reproduction**

The issue reproduces consistently by adding the following shape into
`enumerate_k_grouped_contiguous`:

```python
(128, 2048, 768, 4096)
```

This triggers the following call path:

* `k_grouped_fp8_gemm_nt_contiguous`
* → FP8 kernel selection
* → SM90 kernel dispatch
* → crash with CUDA illegal instruction

Notably, the same configuration works correctly when **N = 1536**, so the issue appears to be specific to `N = 768`.

---

## **🧩 Expected Behavior**

The kernel should run successfully for `(groups=128, M=2048, N=768, K=4096)` without causing an illegal instruction.

---

## **🧪 Environment (if helpful)**

* GPU: H100 (SM90)
* CUDA Toolkit: CUDA 12.9 Driver Version: 535.161.08
* PyTorch version: 2.8.0

---

## **🙏 Additional Notes**

If you need further logs or want me to test a patch, I’m happy to help.

Thanks again for the excellent work on DeepGEMM!


## 评论 (3)

### LyricZhao · 2025-12-05

cc @zheanxu, please take care of it when you are free.

### zheanxu · 2025-12-05

Thank you for reporting this issue.

After investigation, we found that this bug occurs when `m` and `n` are relatively small. In the SM90 K Grouped GEMM implementation, the tensor map for `group[i+1]` is prefetched while processing `group[i]`.

However, when the number of blocks in `group[i]` is small (specifically, when `ceil_div(m, block_m) * ceil_div(n, block_n)` is less than `the number of SMs`), the next group to be processed is not necessarily `group[i+1]`. In this scenario, using the incorrect tensor map leads to an illegal instruction error.

We will fix this shortly. Thanks again!

### xinqiu · 2025-12-05

#238 I made a few simple modifications to get it working properly first
