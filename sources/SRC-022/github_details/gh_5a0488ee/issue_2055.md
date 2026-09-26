# [Issue #2055] [Issue]: Extremely slow compile time (6+ hours) for some GPU families

source: https://github.com/ROCm/rccl/issues/2055
state: closed | updated: 2026-01-20T21:29:38Z
labels: status: triage

## 正文

### Problem Description

We've observed upwards of 6 hours spent compiling RCCL on 48+ core build machines for certain GPU families like `gfx1010;gfx1011;gfx1012` when building within TheRock, see more details at https://github.com/ROCm/TheRock/issues/2130

Here are some configure and build logs:
* configure: https://therock-artifacts.s3.amazonaws.com/19202117581-linux/logs/gfx101X-dgpu/rccl_configure.log
* build: https://therock-artifacts.s3.amazonaws.com/19202117581-linux/logs/gfx101X-dgpu/rccl_build.log

    ```
    384.8	[535/541] Building CXX object CMakeFiles/rccl.dir/hipify/gensrc/all_reduce_minmax_f8e5m2.cpp.o
    388.1	[536/541] Building CXX object CMakeFiles/rccl.dir/hipify/gensrc/all_reduce_premulsum_f8e4m3.cpp.o
    401.3	[537/541] Building CXX object CMakeFiles/rccl.dir/hipify/gensrc/all_reduce_premulsum_f8e5m2.cpp.o
    20033.9	[538/541] Linking CXX shared library librccl.so.1.0
    20033.9	Elapsed time (seconds): 19632.6
    20034.0	[539/541] Creating library symlink librccl.so.1 librccl.so
    20034.0	CMake Warning at /__w/TheRock/TheRock/comm-libs/rccl/cmake/scripts/extract_metadata.cmake:80 (message):
    20034.0	  [Error No such file or directory] roc-obj-ls failed.  stderr:
    20034.0	
    20034.0	
    20034.2	[540/541] Linking CXX executable rcclras
    20034.3	[541/541] Linking CXX executable test/rccl-UnitTests
    END	1762677871.7076726	20034.27623295784	0
    ```

Compilation is slow for other GPU families but that build in particular is an order of magnitude slower and is causing CI/CD pipelines to hit 10+ hour timeouts occasionally.

### Operating System

Linux

### CPU

Various (Azure cloud builders and some developer machines)

### GPU

N/A

### ROCm Version

7.9 (source builds in TheRock)

### ROCm Component

rccl

### Steps to Reproduce

Follow the logs and https://github.com/ROCm/TheRock?tab=readme-ov-file#building-from-source (other reproducers could be produced with some effort too)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

We can tune our ccache configurations and split how many targets we bundle into each GPU "family", but something is clearly off here if compilation for a single build target takes multiple hours.

## 评论 (2)

### huanrwan-amd · 2025-11-14

related issue: https://github.com/ROCm/TheRock/issues/2130

### huanrwan-amd · 2026-01-20

close this one as rccl has JIRA to track this issue.

