# [Issue #61] [Issue]: SQ_LEVEL_WAVES with SQ_ACCUM_PREV_HIRES reports all zeros only on rocprofv3

source: https://github.com/ROCm/rocprofiler-sdk/issues/61
state: closed | updated: 2025-06-02T23:43:21Z
labels: Under Investigation

## 正文

### Problem Description

The following input file works for rocprofv1 but not rocprofv3. I just see all 0s for SQ_ACCUM_PREV_HIRES

```
pmc: SQ_BUSY_CU_CYCLES GRBM_GUI_ACTIVE SQ_LEVEL_WAVES  SQ_ACCUM_PREV_HIRES

gpu:
range:
kernel:
```

### Operating System

Rocky Linux 9.4 (Blue Onyx)

### CPU

AMD EPYC 7V13 64-Core Processor

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.3.0

### ROCm Component

rocprofiler

### Steps to Reproduce

`rocprofv3 -i SQ_LEVEL_WAVES.txt -d Wavefront_1 --` [pytorch FSDP example](https://github.com/AMD-AIG-AIMA/pytorch-training-benchmark)

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

I'm running with apptainer

## 评论 (3)

### ppanchad-amd · 2025-05-07

Hi @mjkpolo. Internal ticket has been created to investigate this issue. Thanks!

### darren-amd · 2025-05-20

Hi @mjkpolo,

The `SQ_ACCUM_PREV_HIRES` counter must be used with the accumulate() function introduced in rocprofv3. This is a similar case for `SQ_LEVEL_WAVES`. Please see [Accumulate Function](https://rocm.docs.amd.com/projects/rocprofiler-sdk/en/amd-mainline/api-reference/counter_collection_services.html#accumulate-function) for more information, thanks!

### mjkpolo · 2025-06-02

Thanks!
