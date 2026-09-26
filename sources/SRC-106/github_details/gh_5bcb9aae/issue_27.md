# [Issue #27] [Issue]: event - incorrect GPU IDs

source: https://github.com/ROCm/amdsmi/issues/27
state: closed | updated: 2026-05-06T22:29:37Z
labels: 

## 正文

### Problem Description

Thanks @Ori-Messinger for pointing out this issue:
![image](https://github.com/ROCm/amdsmi/assets/19967783/5c415ba9-0bf8-470d-80f1-b7f3f67bd3c4)


### Operating System

Linux

### CPU

-

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.1.0

### ROCm Component

amdsmi

### Steps to Reproduce

Run the following in different terminals on one machine:
`amd-smi event`
`rocm-smi --showevents`
`rocm-smi --gpureset -d 0`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### dmitrii-galantsev · 2026-05-06

fixed in https://github.com/ROCm/amdsmi/commit/41488f0c1805b0b5d0566ab56e18a4654e6a5f45
