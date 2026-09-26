# [Issue #47] [Issue]: amd_hsmp.h local copy of kernel header

source: https://github.com/ROCm/amdsmi/issues/47
state: closed | updated: 2024-09-17T19:17:54Z
labels: 

## 正文

### Problem Description

amd_hsmp.h is fetched as part of the build process from the upstream kernel here
 https://github.com/ROCm/amdsmi/blob/amd-staging/CMakeLists.txt#L125 it should come from the system's kernel header.  A mismatch could crash the app or the kernel.

### Operating System

Fedora Rawhide

### CPU

x86_64

### GPU

AMD Radeon Pro W7900

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### harkgill-amd · 2024-09-17

Closing this issue as related PR has been merged.
