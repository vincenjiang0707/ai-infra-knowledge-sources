# [Issue #24] [Issue]: ./amd-smi event can't be stopped/killed

source: https://github.com/ROCm/amdsmi/issues/24
state: closed | updated: 2024-09-20T14:54:40Z
labels: 

## 正文

### Problem Description

When running ./amd-smi event it doesn't stop when you hit "q + ENTER" or "Ctrl + c" however ./rocm-smi --showevents does.

### Operating System

Ubuntu 22.04

### CPU

EYPC 7251

### GPU

AMD Radeon RX 7900 XT

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

## 评论 (2)

### dmitrii-galantsev · 2024-05-02

Yup was able to repro

### harkgill-amd · 2024-09-20

Hi @Ori-Messinger, the following patch has been merged to resolve the failure to exit amd-smi event, https://github.com/ROCm/amdsmi/commit/d263b53797db492f9d6305e334fa7b9788dc5cc9. 

Could you please build amd-smi from the `amd-staging` branch and confirm if the patch addresses the issue on your end?
