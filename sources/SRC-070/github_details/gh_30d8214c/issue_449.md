# [Issue #449] [Bug] non-deterministic results in sm90 tf32_hc_prenorm_gemm

source: https://github.com/deepseek-ai/DeepGEMM/issues/449
state: open | updated: 2026-09-23T14:58:39Z
labels: 

## 正文

### Description

  On SM90 GPUs, tf32_hc_prenorm_gemm can produce incorrect and non-deterministic GEMM outputs when processing multiple K blocks.
  Repeated calls with identical inputs can return different results.

  ### Root cause

  The kernel uses asynchronous WGMMA instructions with register-source A operands. Previously, the next iteration loaded its A fragment
  before waiting for the preceding iteration's WGMMA to complete. This could overwrite A registers while they were still being read by
  the in-flight WGMMA.

  ### Fix

  Proposed fix: https://github.com/deepseek-ai/DeepGEMM/pull/448

  The fix moves `warpgroup_wait<0>()` immediately after `warpgroup_commit_batch()`, ensuring that each iteration's WGMMA completes
  before its A registers are reused.

  The PR also adds a regression test covering split-K, PDL enabled/disabled, and default/side streams. It checks outputs against FP32
  references and verifies repeatability across identical launches.

  ### Validation

  With the fix applied, both the existing hyperconnection tests and all 24 configurations of the new regression test passed on an SM90
  GPU.

### TODO
   fix will introduce some performance regression which suppose to be mitigated in upcoming PRs。

## 评论 (2)

### LiRunGuo · 2026-09-22

I measured this on an H200 (SM90, driver 580.159.03, PyTorch 2.11.0+cu130) with DeepGEMM `main` (78b6900), in case it helps the review of #448.

**Reproduction.** I ran the 24 shapes from `test_hc_prenorm_gemm` (`m` in 13 / 137 / 4096 / 8192, `n = 24`, `k` in 7168 / 7680 / 28672, with and without 16 splits), with 50 back-to-back launches per shape. I did this with both NVCC 12.9.86 and 13.0.48. `main` gave 0 bitwise mismatches in every case, and the regression test added in #448 also passes on `main` with both compilers (24 / 24).

I also checked the SASS of `main` from both compilers with a small script. It looks for writes to the A registers of an in-flight `HGMMA` group before the `WARPGROUP.DEPBAR` that waits for it, and found none: ptxas puts the A fragments of consecutive stages in different registers. So the source-level race is real, but these two ptxas versions do not turn it into a hazard for these instantiations. That may explain why it is hard to reproduce, and it could still show up with other compiler versions.

**Performance of #448.** Median of 3 `bench_kineto` runs, NVCC 12.9, in µs:

| m, k, splits | `main` | #448 | double-buffered A |
|---|---|---|---|
| 137, 28672, none | 106.5 | 120.8 (+13%) | 111.4 (+5%) |
| 4096, 7680, none | 32.9 | 36.2 (+10%) | 33.8 (+3%) |
| 4096, 7680, 16 | 45.5 | 38.0 (−16%) | 47.6 (+5%) |
| 8192, 28672, none | 123.5 | 131.8 (+7%) | 125.2 (+1%) |

The geometric mean over all 24 shapes versus `main` is +2.8% for #448 and +2.2% for the double-buffered variant (NVCC 13.0: +4.6% and +2.9%). #448 costs 8–13% on most shapes without splits, but it is about 16% faster on the `k = 7680`, 16-split shapes.

The double-buffered variant keeps two A register buffers selected by stage parity, and waits with one WGMMA group in flight (`warpgroup_wait<1>`) before a buffer is reused. It fixes the race by construction and recovers most of the loss on the shapes without splits, but it does not get #448's gain on the 16-split shapes. So it is not clearly better overall. The patch is on [LiRunGuo/DeepGEMM@sm90-hc-prenorm-double-buffered-a](https://github.com/LiRunGuo/DeepGEMM/commit/a77409b816cc3be35e762a9ba67784570a06cd92) if it is useful.


### leevan · 2026-09-23

@LiRunGuo cool, maybe you can try with a H20. regarding the performance, I do have another version of double buffer which improves the performance.
