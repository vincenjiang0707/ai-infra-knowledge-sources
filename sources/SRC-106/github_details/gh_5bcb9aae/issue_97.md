# [Issue #97] [Issue]: amd-smi reports different "size" value for XCD memory size different from the docs on MI300A at TPX and CPX

source: https://github.com/ROCm/amdsmi/issues/97
state: open | updated: 2025-06-30T16:29:59Z
labels: Under Investigation

## 正文

### Problem Description

Hello
I hope this finds you well.

On `MI300A` in `TPX` and `CPX` modes, when running `amd-smi` command it correctly identifies the number of GPUs and everything is fine.

The problem comes to the `size` column (attribute) that is used to represent the memory size for each XCD (GPU).

[AMD documentation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/latest/gpu-partitioning/mi300a/overview.html) show that in `TPX` mode each XCD (GPU) gets `32GB` but the `amd-smi` command shows `42.66GB`
The same for `CPX` mode, the docs mention `16GB` for each XCD, but the `amd-smi` tool show `21.33GB`

In the case of `SPX` mode, everything matches as it is.

Any idea/help what could be the reason for these differences and why?

Appreciate your precious time.

### Operating System

Linux RHE

### CPU

N/A

### GPU

MI300A

### ROCm Version

6.2.4

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### ppanchad-amd · 2025-06-26

Hi @amroakmal. Internal ticket has been created to assist with your issue. Thanks!

### schung-amd · 2025-06-26

Hi @amroakmal, this sounds like a known issue with various metrics reported by rocm-smi and amd-smi on partitioned GPUs; see https://github.com/ROCm/ROCm/issues/4750 for example. You can verify that this is a display issue by checking the output of `rocminfo` or the driver interfaces at `/sys/class/kfd/kfd/topology/nodes/<device id>/mem_banks/0/properties` which should show the correct amount of VRAM per partition. We're working on a fix for this, which hopefully will be in ROCm 7.0.

### amroakmal · 2025-06-30

@ppanchad-amd @schung-amd : 
Thank you so much for this, will verify and get back to you if there was any problem. Appreciate your precious help.
