# [Issue #2274] [BUG] MLA example is broken for split-kv and larger Q

source: https://github.com/NVIDIA/cutlass/issues/2274
state: open | updated: 2026-09-13T03:17:17Z
labels: bug, ? - Needs Triage, inactive-30d, inactive-90d

## 正文

**Describe the bug**
Currently example initializes Q to quite small values (mean -1, stddev 1). If I initialize Q to a bit bigger values (e.g. stddev 100), split-kv stops working. Larger Qs are typical for LLMs.
Looks like is some overflow in LSE compute.

**Steps/Code to reproduce bug**
Apply the following patch https://gist.github.com/divchenko/10f1991a7a197b706b5c46aaca1a9bd2  to
commit f535c33634b640a4c0bee131f2f6e9f81877a18c (HEAD, tag: v3.9.1)
Then run w/o split-kv

```
./77_blackwell_mla_2sm_fp16 --verify --split_kv=1
###### B 64 MLA H 128 D_rope 64 D_latent 512 Q 1 K 256 Gen None Split 1 Gen None #SM 148
 [OK]  128x128 fp16 persistent          : 156.768 TFLOPS/s 1.26077 TB/s
 [OK]  128x128 fp16 individual          : 162.176 TFLOPS/s 1.30426 TB/s

```

But when split-kv is enabled, it fails:
```

./77_blackwell_mla_2sm_fp16 --verify --split_kv=2
###### B 64 MLA H 128 D_rope 64 D_latent 512 Q 1 K 256 Gen None Split 2 Gen None #SM 148
failed O: max diff 6.26562 mean 1.15391
failed LSE: max diff inf mean inf
Reference check failed
[FAIL] 128x128 fp16 persistent          : 70.6905 TFLOPS/s 0.568513 TB/s
failed O: max diff 6.26562 mean 1.15391
failed LSE: max diff inf mean inf
Reference check failed
[FAIL] 128x128 fp16 individual          : 65.94 TFLOPS/s 0.530308 TB/s

```

**Expected behavior**
Verification should pass for larger Q

**Environment details (please complete the following information):**
B200
NVIDIA-SMI 570.124.06             Driver Version: 570.124.06     CUDA Version: 12.8

**Additional context**



## 评论 (3)

### github-actions[bot] · 2025-05-31

This issue has been labeled `inactive-30d` due to no recent activity in the past 30 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed. This issue will be labeled `inactive-90d` if there is no activity in the next 60 days.

### github-actions[bot] · 2025-08-29

This issue has been labeled `inactive-90d` due to no recent activity in the past 90 days. Please close this issue if no further response or action is needed. Otherwise, please respond with a comment indicating any updates or changes to the original issue and/or confirm this issue still needs to be addressed.

### XFDG · 2026-09-13

I reran this report on an NVIDIA B200 using current main (147295a3d4b75f3aeff247c25b8927cea9a7006a), CUDA 13.1, and the built-in large-Q mode (--init-style-q=l, Gaussian stddev 100). Both --split_kv=1 and --split_kv=2 pass verification for the persistent and individual kernels; the split=2 LSE remains finite. This issue appears resolved on current main.
