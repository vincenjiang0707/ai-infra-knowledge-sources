# [Issue #8239] [RFE] Masked version of batched matmul_ogs kernel

source: https://github.com/triton-lang/triton/issues/8239
state: open | updated: 2026-09-19T04:59:44Z
labels: 

## 正文

Hello Developers. IIUC, the matmul_ogs kernel supports batched matrix multiplication. However, it assumes that all the entries in the batches are valid. I have a use case where only a few arbitrary entries in each batch is actually valid. Computing the matmul over all the entries leaves significant performance on the table.

Are there any plans to support a Masked version of the batched matmul_ogs kernel where only some entries in each batch are valid ? 

reference: https://github.com/deepseek-ai/DeepGEMM/tree/main#grouped-gemms-masked-layout 

Thanks 🙌 

## 评论 (2)

### 0z5a · 2026-09-18

Hi @varun-sundar-rabindranath , I'd like to take a look at this.

I'm planning to first clarify the masking contract (arbitrary valid entries vs. per-batch valid lengths), then prototype it on top of the existing batched matmul path so that invalid tiles are actually skipped rather than only masked at load/store time.

I can also add correctness + performance coverage, including sparse/imbalanced cases, and validate it on NVIDIA L20.

### 0z5a · 2026-09-19

The main-based version is now in #11873 (Draft), replacing release-branch #11865. It adds device-side valid leading-row counts to non-persistent batched `matmul`; fully padded M tiles skip computation.

| Test | Baseline/reference | Result |
|---|---|---|
| Prefix counts × split-K 1/2 | Unmodified main rejects the new keyword; dense output is the numerical oracle | 6/6 passed, exact valid-row matches |
| Full → empty → partial → full CUDA Graph replay | Dense reference | 1/1 passed |
| Invalid count metadata | Expected rejection | 3/3 passed |

10 L20 tests passed using Triton 3.8.0 and the changed main Python code. Persistent kernels and arbitrary element masks are outside this version. No main-port speedup is claimed; the older 3.6.x timings do not apply.

