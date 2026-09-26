# [Issue #18] [Issue]: string returned by amdsmi_status_code_to_string() contains RSMI_STATUS_*

source: https://github.com/ROCm/amdsmi/issues/18
state: closed | updated: 2025-02-13T20:44:58Z
labels: Under Investigation

## 正文

### Problem Description

Not a big issue, but the string returned by amdsmi_status_code_to_string() contains the RSMI_STATUS_* code. For example:

```
amdsmi_status_code_to_string(AMDSMI_STATUS_SUCCESS, &err)
-> "RSMI_STATUS_SUCCESS: The function has been executed successfully."

amdsmi_status_code_to_string(AMDSMI_STATUS_INVAL, &err)
-> "RSMI_STATUS_INVALID_ARGS: The provided arguments do not meet the preconditions required for calling this function."
```

### Operating System

Ubuntu 22.04

### CPU

AMD EPYC 7763

### GPU

AMD Instinct MI250

### ROCm Version

ROCm 6.0.0

### ROCm Component

amdsmi

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (2)

### harkgill-amd · 2024-09-17

Hi @maxweiss, an internal ticket has been created to fix this. Thanks for pointing this out!

### harkgill-amd · 2025-02-13

Hi @maxweiss, this has been addressed in https://github.com/ROCm/amdsmi/commit/c1cd2b46ef9292c500d0f1fae363d5be893a5f05. The `amdsmi_status_code_to_string` output will now specify `AMDSMI_STATUS_` rather than `RSMI_STATUS_`. 

You can find the latest implementation here https://github.com/ROCm/amdsmi/blob/amd-staging/src/amd_smi/amd_smi.cc#L184-L338.
