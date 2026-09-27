# [Issue #520] [Bug]: ERROR [roofline] Cannot find a valid binary for your operating system

source: https://github.com/ROCm/rocprofiler-compute/issues/520
state: closed | updated: 2025-08-06T18:23:52Z
labels: bug, triage

## 正文

### Describe the bug

As per title.

I am running:
```
omniperf profile -n mfma_mine -- ./a.out
```

on a kernel of mine.

I use omniperf:
```
----------------------------------------
Omniperf version: 2.1.0 (release)
Git revision:     e497928
----------------------------------------
```

My best guess is that I would be better off running within `rocm/dev-ubuntu-22.04:6.3` docker image with the latest version of omniperf, but just to let you know.

### Linux Distribution

Ubuntu 24.04 LTS (Noble Numbat)

### ROCm Compute Profiler Version

2.1.0

### GPU

AMD MI250

### ROCm Version

6.2.4

### Cluster name (if applicable)

xcomx250-1

### Reproducer

1. Compile some kernel with `hipcc`
2. Run `omniperf profile -n mfma_mine -- ./a.out`
3. Get omniperf running, and at the end an error `ERROR [roofline] Cannot find a valid binary for your operating system`

### Expected behavior

No error.

### Relevant log output

_No response_

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/47

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
