# [Issue #9] [Issue]: api_buffered_tracing throws exceptions

source: https://github.com/ROCm/rocprofiler-sdk/issues/9
state: closed | updated: 2024-07-29T21:13:56Z
labels: 

## 正文

### Problem Description

Trying to build and run the api_buffered_tracing example, I get the following logs:

E20240725 12:34:03.379593 140562161231616 buffer.cpp:204] buffer callback threw an exception: vector::_M_range_check: __n (which is 1) >= this->size() (which is 0)

Removing the references to `client_name_info` in `tool_tracing_callback` fixes this.

### Operating System

sles15sp5

### CPU

AMD EPYC

### GPU

AMD Instinct MI250X

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

### jrmadsen · 2024-07-29

rocprofiler-sdk is not fully compatible with ROCm 6.1 so I am going to close this. Please report back if this issue still exists once ROCm 6.2 is available.
