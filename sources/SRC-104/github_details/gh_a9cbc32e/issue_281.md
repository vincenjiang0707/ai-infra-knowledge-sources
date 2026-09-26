# [Issue #281] Request roofline-only data files

source: https://github.com/ROCm/rocprofiler-compute/issues/281
state: closed | updated: 2025-08-06T18:33:41Z
labels: enhancement, Profiling, Roofline

## 正文

**Is your feature request related to a problem? Please describe.**
A common issue in generating roofline plots is labeling. Kokkos and RAJA codes tend to have large naming schemes tied to their kernels, which is not treated especially well with omniperf's plotter (for obvious reasons). E.g.:

[kernelName_legend.pdf](https://github.com/AMDResearch/omniperf/files/14436412/kernelName_legend.pdf)

**Describe the solution you'd like**
As a workaround, it would be nice to be able to get the raw data used to generate the roofline plot so that users can customize the plotting process. We can see from the data directory that we have the `pmc_perf.csv` and `roofline.csv` data files, but it is unclear how a build the roofline plot given the raw data/counters in these files.

If possible, can a csv file be generated for each roofline plot that gets generated with kernel names, AI/GFLOPs data, and roofline data so that a user can rebuild the plots separately from omniperf.



## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/65

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
