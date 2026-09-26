# [Issue #1267] Compute time in the reduction operation

source: https://github.com/ROCm/rccl/issues/1267
state: closed | updated: 2024-07-24T06:23:13Z
labels: 

## 正文

### Problem Description

Hi, We are in need to time the compute of the reduction operation, Is there any environment variable or any process to get the time of the compute in the allreduce collective



### Operating System

Ubuntu

### CPU

EPYC77603

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

## 评论 (2)

### gilbertlee-amd · 2024-07-23

No - no such environment variable exists.  
Aside from NPKit, which I suggested previously, you could get the overall time for the AllReduce by wrapping it between two hipEvents, calling hipEventSynchronize, then getting the elapsed time using hipEventElapsedTime.


### tks2004 · 2024-07-24

> No - no such environment variable exists. Aside from NPKit, which I suggested previously, you could get the overall time for the AllReduce by wrapping it between two hipEvents, calling hipEventSynchronize, then getting the elapsed time using hipEventElapsedTime.

Ok. Thanks
