# [Issue #90] [Issue]: Display of VRAM% in amd-smi CLI is not correct

source: https://github.com/ROCm/amdsmi/issues/90
state: closed | updated: 2026-05-06T22:28:25Z
labels: bug

## 正文

### Problem Description

When ~half of the memory is used, it displays
```
 VRAM%
0.48 %
```
which should be 48%


### Operating System

NAME="Ubuntu" VERSION="22.04.5 LTS (Jammy Jellyfish)"

### CPU

model name      : AMD Ryzen Threadripper PRO 7985WX 64-Cores

### GPU

gfx950

### ROCm Version

6.5.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### Ceye4n · 2025-11-25

was fixed in 41488f0c1805b0b5d0566ab56e18a4654e6a5f45, can be closed

I had the same issue, saw this, found it correct in the source code and solved it on my end by updating
