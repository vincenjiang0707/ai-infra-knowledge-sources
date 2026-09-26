# [Issue #39] [Issue]: There are not api to get compute units and FP32 or FP64 units in amdsmi

source: https://github.com/ROCm/amdsmi/issues/39
state: closed | updated: 2024-10-28T22:07:31Z
labels: Under Investigation

## 正文

### Problem Description

I need a api to get compute units and FP32 and FP64 units in amdsmi,
I need this api to get compute performance, like nvidia's  nvmlDeviceGetNumGpuCores to get sm cores in nvml library.

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

Hi @lizhenneng. Internal ticket has been created to assist with your issue. Thanks!

### darren-amd · 2024-10-28

Hi @lizhenneng,

Are you looking to query the number of Streaming Multiprocessors (SM's) which are equivalent to CU's for AMD, or the number of CUDA cores? The Nvidia function `nvmlDeviceGetNumGpuCores` appears to query the number of CUDA cores: [Docs](https://docs.nvidia.com/deploy/nvml-api/group__nvmlDeviceQueries.html#group__nvmlDeviceQueries_1gbe689df58db3c072cb0e890b13612abc), whereas you seem to want to get the number of SM's?

### dmitrii-galantsev · 2024-10-28

@lizhenneng That's right, there is no way to get that info from amdsmi.
You have to rely on RDC + rocprofiler.
https://github.com/ROCm/rdc/blob/345ac64a439d82dd817b0b0980b59dd948024b8a/common/rdc_field.data#L137

