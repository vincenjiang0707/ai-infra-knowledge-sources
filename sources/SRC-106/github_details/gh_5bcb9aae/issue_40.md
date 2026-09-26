# [Issue #40] [Issue]: amdsmi_status_code_to_string not support AMDSMI_STATUS_DRIVER_NOT_LOADED

source: https://github.com/ROCm/amdsmi/issues/40
state: closed | updated: 2024-11-06T16:36:00Z
labels: Under Investigation

## 正文

### Problem Description

// Define a map of rsmi status codes to amdsmi status codes
const std::map<rsmi_status_t, amdsmi_status_t> rsmi_status_map = {
    {RSMI_STATUS_SUCCESS, AMDSMI_STATUS_SUCCESS},
    {RSMI_STATUS_INVALID_ARGS, AMDSMI_STATUS_INVAL},
    {RSMI_STATUS_NOT_SUPPORTED, AMDSMI_STATUS_NOT_SUPPORTED},
    {RSMI_STATUS_FILE_ERROR, AMDSMI_STATUS_FILE_ERROR},
    {RSMI_STATUS_PERMISSION, AMDSMI_STATUS_NO_PERM},
    {RSMI_STATUS_OUT_OF_RESOURCES, AMDSMI_STATUS_OUT_OF_RESOURCES},
    {RSMI_STATUS_INTERNAL_EXCEPTION, AMDSMI_STATUS_INTERNAL_EXCEPTION},
    {RSMI_STATUS_INPUT_OUT_OF_BOUNDS, AMDSMI_STATUS_INPUT_OUT_OF_BOUNDS},
    {RSMI_STATUS_INIT_ERROR, AMDSMI_STATUS_NOT_INIT},
    {RSMI_INITIALIZATION_ERROR, AMDSMI_STATUS_NOT_INIT},
    {RSMI_STATUS_NOT_YET_IMPLEMENTED, AMDSMI_STATUS_NOT_YET_IMPLEMENTED},
    {RSMI_STATUS_NOT_FOUND, AMDSMI_STATUS_NOT_FOUND},
    {RSMI_STATUS_INSUFFICIENT_SIZE, AMDSMI_STATUS_INSUFFICIENT_SIZE},
    {RSMI_STATUS_INTERRUPT, AMDSMI_STATUS_INTERRUPT},
    {RSMI_STATUS_UNEXPECTED_SIZE, AMDSMI_STATUS_UNEXPECTED_SIZE},
    {RSMI_STATUS_NO_DATA, AMDSMI_STATUS_NO_DATA},
    {RSMI_STATUS_UNEXPECTED_DATA, AMDSMI_STATUS_UNEXPECTED_DATA},
    {RSMI_STATUS_BUSY, AMDSMI_STATUS_BUSY},
    {RSMI_STATUS_REFCOUNT_OVERFLOW, AMDSMI_STATUS_REFCOUNT_OVERFLOW},
    {RSMI_STATUS_SETTING_UNAVAILABLE, AMDSMI_STATUS_SETTING_UNAVAILABLE},
    {RSMI_STATUS_AMDGPU_RESTART_ERR, AMDSMI_STATUS_AMDGPU_RESTART_ERR},
    {RSMI_STATUS_UNKNOWN_ERROR, AMDSMI_STATUS_UNKNOWN_ERROR},
};
This map have not AMDSMI_STATUS_DRIVER_NOT_LOADED.

### Operating System

Ubuntu 22.04.3 LTS

### CPU

Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz

### GPU

AMD Radeon RX 7900 XTX

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

## 评论 (3)

### ppanchad-amd · 2024-10-28

Hi @lizhenneng. Internal ticket has been created to investigate your issue. Thanks!

### jamesxu2 · 2024-10-29

Hi @lizhenneng, the AMDSMI_STATUS_DRIVER_NOT_LOADED is not in the rsmi_status_map because it is not translatable from ROCm SMI (rsmi). There is no equivalent rsmi_status_t. 

The AMDSMI_STATUS_DRIVER_NOT_LOADED code was added in [this commit](https://github.com/ROCm/amdsmi/commit/f86f62b3f7d93b0be3424031dc99025d1242207c). You can look at this function for a usage example:
https://github.com/ROCm/amdsmi/blob/0ceca28f4139dced5e9b5739a3f393780d7add48/src/amd_smi/amd_smi_system.cc#L182-L192

Please provide me with more details on what exactly you're trying to do with AMDSMI_STATUS_DRIVER_NOT_LOADED, or if you are observing an error involving that status code.

### jamesxu2 · 2024-11-06

Closing due to inactivity. Please reopen it @lizhenneng if you come back to this issue at some point.
