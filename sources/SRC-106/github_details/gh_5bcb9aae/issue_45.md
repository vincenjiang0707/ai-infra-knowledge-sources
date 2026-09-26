# [Issue #45] [Issue]: `amdsmi -h` requires kernel module to be loaded

source: https://github.com/ROCm/amdsmi/issues/45
state: closed | updated: 2024-09-24T13:53:51Z
labels: 

## 正文

### Problem Description

When a user runs `amdsmi -h`, it fails if the `amdgpu` kernel module is not loaded. For normal cases, we wish the help information can be printed even if there is no kernel module.

### Operating System

Debian

### CPU

AMD Ryzen 9 5950X 16-Core Processor

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### harkgill-amd · 2024-09-24

Hi @xuantengh, having the `amdgpu` and `amd_hsmp` driver modules loaded is a hard requirement for the initialization of amdsmi to pass. At the moment, there are no plans to enable simpler commands to run without initialization. However, this is something we may consider if there is increased demand in the future.

A small change has also been made to the error message to make it clear which commands need to be run if the driver modules are missing https://github.com/ROCm/amdsmi/commit/3660724a08fc0bd66a22184c29e6a9a93863234c.
