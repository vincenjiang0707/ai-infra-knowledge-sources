# [Issue #103] Integrate kernel-level power usage data

source: https://github.com/ScalingIntelligence/KernelBench/issues/103
state: open | updated: 2026-01-01T06:47:21Z
labels: 

## 正文

Coincidentally, I worked on a very similar project one years ago, where I built a version of KernelBench focused on linear algebra kernels [(Link) ](https://github.com/tanish111/Power-Extraction/tree/master/Codes/Linear-Algebra/template) written in raw CUDA. As part of that effort, I also developed a tool called [PowerAPI](https://github.com/tanish111/Power-Extraction/tree/master/PowerAPI) that measures power consumption using NVIDIA NVML. Its design style and purpose are very closely aligned with the design of KernelBench.

If the community is interested, I would be happy to:
Extend PowerAPI to provide Python bindings
Integrate it directly into KernelBench as an optional module for per-kernel power measurement

This could help users benchmark kernels not only on execution time, but also energy cost per operation, enabling more sustainable and realistic comparisons.

Please let me know if a PR in this direction would be welcomed.

## 评论 (2)

### tanish111 · 2025-12-04

@simonguozirui and other authors of [KernelBench](https://scalingintelligence.stanford.edu/blogs/kernelbench/) would really appreciate hearing your thoughts on this.

### tanish111 · 2025-12-31

> [@simonguozirui](https://github.com/simonguozirui) and other authors of [KernelBench](https://scalingintelligence.stanford.edu/blogs/kernelbench/) would really appreciate hearing your thoughts on this.
@simonguozirui @pythonomar22 I have implemented this Should I raise a PR? 
