# [Issue #215] No healthy persistent workers available` after workload shape mismatch

source: https://github.com/flashinfer-ai/flashinfer-bench/issues/215
state: open | updated: 2026-03-17T18:15:10Z
labels: 

## 正文

When running:

```bash
flashinfer-bench run --local /path/to/flashinfer-trace
```

the workload for `gdn_decode_qk4_v8_d128_k_last` first triggers an input shape validation error:

```text
'a' expected [4, 1, 8], got [4, 8]
'a' expected [8, 1, 8], got [8, 8]
```

then the persistent runner repeatedly restarts/removes workers, eventually removing all GPU workers, and all subsequent definitions/workloads fail with:

```text
No healthy persistent workers available
```


1. In the `gdn_decode_qk4_v8_d128_k_last` stage, baseline/reference construction fails with:
   - `'a' expected [B, 1, 8], got [B, 8]`
2. The runner treats this exception as a worker failure and triggers restart/retry.
3. Each device is removed after reaching the retry limit.
4. Once the worker pool is empty, all subsequent workloads fail with:
   - `No healthy persistent workers available`

The log shows a repeated pattern:

- `Persistent worker cuda:X failed while running reference ...`
- `Removing device cuda:X after 3 failed attempts`
- `Failed to run workload ...: No healthy persistent workers available`





## 评论 (1)

### Ubospica · 2026-03-17

Thanks for raising the problem! We will fix it soon.
