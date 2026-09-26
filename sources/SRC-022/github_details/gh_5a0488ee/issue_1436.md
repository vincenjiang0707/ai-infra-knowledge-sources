# [Issue #1436] [Issue]: Despite adding a new INFO log or modifying an existing INFO in the source code, recompiling and setting export NCCL_DEBUG=INFO, the expected log outputs do not appear

source: https://github.com/ROCm/rccl/issues/1436
state: closed | updated: 2025-05-12T15:46:03Z
labels: 

## 正文

### Problem Description

When I create a new log using INFO in the source code, then compile it using ./install.sh, and test it with ./all_reduce_perf, while setting the environment variable as export NCCL_DEBUG=INFO, I cannot see the log output that I added. Moreover, I tried modifying the string in the existing INFO log at line 57 of bootstrap.cc (e.g., INFO(NCCL_INIT, "Bootstrap: Using")), recompiled as described above and executed the test again, but the INFO output still did not change. I also tried deleting the build directory, modifying the source code, and recompiling, but it still doesn't work.

### Operating System

ubuntu-24.04

### CPU

Intel(R) Core(TM) i7-14700k

### GPU

2x AMD Radeon RX GPU 7900XT

### ROCm Version

ROCm 6.2.3

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### nileshnegi · 2024-11-27

how are you building RCCL-Tests?
can you check if `ldd ./all_reduce_perf` links to the correct RCCL (that you built) instead of a pre-built RCCL like under `/opt/rocm/lib/librccl.so`?

alternatively, you can re-try by setting `LD_LIBRARY_PATH=<path-to-your-RCCL>/build/release NCCL_DEBUG=INFO ./all_reduce_perf`

### nileshnegi · 2024-12-17

any updates @Kyrienn?

### ppanchad-amd · 2025-05-12

Hi @Kyrienn. Closing ticket due to lack of response.  Please feel free to re-open ticket if you are still seeing this issue. Thanks!
