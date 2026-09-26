# [Issue #11] [Issue]: different/inconsistent python interfaces 

source: https://github.com/ROCm/amdsmi/issues/11
state: closed | updated: 2024-09-13T15:47:02Z
labels: 

## 正文

### Problem Description

The python interface functions are different depending on rocm version, is there a reason they're not updated for all rocm versions ?
rocm5.7: `devices_handles = amdsmi.amdsmi_get_processor_handles()`
rocm5.6: `devices_handles = amdsmi.amdsmi_get_device_handles()`

my problem is that I have to do things like this to support each version of rocm 😅
https://github.com/huggingface/optimum-benchmark/blob/main/optimum_benchmark/launchers/isolation_utils.py#L65-L111

### Operating System

Ubuntu 22.04

### CPU

AMD Epyc

### GPU

AMD Instinct MI250

### ROCm Version

ROCm 5.7.0, ROCm 5.6.0

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (2)

### marifamd · 2024-03-05

Hi @IlyasMoutawwakil thank you for reaching out. You are correct, we did change this because amd-smi will be able to handle all amd processors (GPUs & CPUs) in the future. 

amd-smi is still a realtively new project and I'm excited to see developers use the python library that we developed. FYI we are aware of the bugs in the amdsmi_get_gpu_process_list & amdsmi_get_gpu_process_info functions as we are redesigning it. 

### harkgill-amd · 2024-09-13

Hi @IlyasMoutawwakil, thank you again for reaching out with your concerns. Following up on @marifamd's reply, it looks like the function has not changed from `amdsmi_get_processor_handles()` since ROCm 5.7. As a result, I will close out this issue.
