# [Issue #100] Roofline for INT32?

source: https://github.com/ROCm/rocprofiler-compute/issues/100
state: closed | updated: 2025-08-06T18:41:13Z
labels: question, Roofline

## 正文

I used the Flask-based GUI to view roofline data for a kernel that is heavy on INT32 VALU arithmetic instructions, but has no FP16, FP32, FP64, or INT8 instructions. Because of this the plot marker for this kernel does not show up on the displayed Roofline plots. This can be disorienting, leaving the user to wonder why the kernel does not show up on the plots (but may only become clear when looking at the instruction mix further down).  Is there any possibility or plan to extend the roofline plots to demonstrate performance of kernels heavy on INT32 arithmetic?
Testing info:
* ROCm v5.4.3
* OmniPerf v1.0.6
* Hardware: Single GCD of MI250x

## 评论 (4)

### coleramos425 · 2023-03-20

Thanks for reaching out @mrowan137. The reasoning behind our two Empirical Roofline plots is 

1. (FP32/FP64) for HPC applications
2. (FP16/INT8) for ML application

My understanding is that these data types encapsulate a majority of the arithmetic for these two crowds. To justify adding this to our model, could you tell me a little more about your application and what group this would fit in?

### mrowan137 · 2023-03-20

Hi @coleramos425 , the data I collected are from an application called ALE3D which we are supporting at LLNL as part of ELCAP bring-up.  This would fall in the HPC category.

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/85

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
