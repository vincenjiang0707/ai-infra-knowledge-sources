# [Issue #700] [Bug]: Incorrect MFMA Peak FLOPs Calculations for BF16 and F16 in `gfx941/0200_system-speed-of-light.yaml

source: https://github.com/ROCm/rocprofiler-compute/issues/700
state: closed | updated: 2025-06-27T19:31:56Z
labels: bug, triage

## 正文

### Describe the bug

While validating peak throughput calculations on MI300X, I noticed that the MFMA metrics for `BF16` and `F16` in [gfx941/0200_system-speed-of-light.yaml](https://github.com/ROCm/rocprofiler-compute/blob/amd-mainline/src/rocprof_compute_soc/analysis_configs/gfx941/0200_system-speed-of-light.yaml#L52) assume **4096 FLOPs per cycle per CU**:

```yaml
peak: ((($max_sclk * $cu_per_gpu) * 4096) / 1000)
```

This is incorrect. According to the [CDNA3 whitepaper](https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-3-white-paper.pdf), Table 1, the correct peak throughput for BF16 and F16 MFMA is **2048 FLOPs per cycle per CU**. The corrected expression should be:

```yaml
peak: ((($max_sclk * $cu_per_gpu) * 2048) / 1000)
```

Other MFMA-related metrics such as `F8`, `F32`, `F64`, and `I8` appear to follow a similar pattern and may also require review. Let me know how you'd prefer to track those.
Thanks.

### Linux Distribution

NA

### ROCm Compute Profiler Version

NA

### GPU

AMD MI300X

### ROCm Version

_No response_

### Cluster name (if applicable)

_No response_

### Reproducer

Shared the code snippet from src

### Expected behavior

_No response_

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (3)

### feizheng10 · 2025-05-09

Thanks for pointing out!  Will have a quick look then back to you.

### Hamerlate · 2025-05-23

By the way, similar bugs for gfx942

### harkgill-amd · 2025-06-27

Hi @ajassani , this is addressed in https://github.com/ROCm/rocprofiler-compute/commit/ab6665d3173fb6cc86f26ba38bb830602e311bdb. If you do find any other issues with the metrics calculations, please open a new issue and we'll investigate it further from there. Thanks!
