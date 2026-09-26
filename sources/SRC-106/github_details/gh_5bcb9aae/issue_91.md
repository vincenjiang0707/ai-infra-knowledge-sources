# [Issue #91] [Issue]: --compute-partition and --memory-partition options in amd-smi are invalid in ROCm 6.4.1

source: https://github.com/ROCm/amdsmi/issues/91
state: closed | updated: 2025-06-18T18:27:04Z
labels: Under Investigation

## 正文

### Problem Description

Title: `--compute-partition` and `--memory-partition` options in `amd-smi` are invalid in ROCm 6.4.1

I tried the following commands as described in the official AMD ROCm documentation on compute and memory modes:
https://rocm.blogs.amd.com/software-tools-optimization/compute-memory-modes/README.html

```bash
amd-smi set --gpu 7 --compute-partition CPX
amd-smi set --gpu 7 --memory-partition NPS4
```

However, neither of them works:
```bash
Parameter '--compute-partition cpx' is invalid. Run '--help' for more info. Error code: -2
Parameter '--memory-partition nps4' is invalid. Run '--help' for more info. Error code: -2
```

My version info is 
```bash
AMDSMI Tool: 25.4.2+aca1101 | AMDSMI Library version: 25.4.0 | ROCm version: 6.4.1 | amdgpu version: 6.12.12 | amd_hsmp version: N/A
```

### Operating System

Ubuntu 22.04 LTS

### CPU

Intel(R) Xeon(R) Platinum 8480C

### GPU

8x AMD MI300X

### ROCm Version

ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

```bash
amd-smi set --gpu x --compute-partition CPX
amd-smi set --gpu x --memory-partition NPS4
```
Replace x with any real id

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (4)

### ppanchad-amd · 2025-05-27

Hi @Hamerlate. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-06-12

Hi @Hamerlate,

I haven't been able to reproduce this issue on my end with the same versions of amd-smi and ROCm. Could you please try running with `sudo`, such as `sudo amd-smi set --gpu 7 --compute-partition CPX`. If that doesn't work, could you please provide the output of `sudo amd-smi set --help` and `rocminfo`, thanks!

### Hamerlate · 2025-06-12

Thanks for your reply! Now I think the issue arises because my machine in Azure is running in a virtualized environment, which doesn't support partitioning...

![Image](https://github.com/user-attachments/assets/2eb66b86-f0f9-4593-adf4-d313443865b4)

### darren-amd · 2025-06-13

Hi @Hamerlate,

Yes, unfortunately partitions are currently not supported on virtualized environments. 
