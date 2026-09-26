# [Issue #187] [Issue]: amdsmi_vram_info_t::vram_max_bandwidth is broken

source: https://github.com/ROCm/amdsmi/issues/187
state: closed | updated: 2026-04-13T18:17:59Z
labels: status: triage

## 正文

### Problem Description

`amdsmi_vram_info_t::vram_max_bandwidth` is broken and returns `18446744073709551615`.

### Operating System

Ubuntu 24.04.4 LTS, kernel 6.17.0-19-generic

### CPU

Intel Core i7-13700K

### GPU

AMD Radeon RX 7700 XT

### ROCm Version

ROCm 7.2.7

### ROCm Component

amdsmi

### Steps to Reproduce

https://github.com/ProjectPhysX/hw-smi

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### darren-amd · 2026-04-13

Hi @ProjectPhysX,

Thanks for reporting this, this appears to be the same request as in https://github.com/ROCm/rocm-systems/issues/5036 so going to close this as a duplicate.
