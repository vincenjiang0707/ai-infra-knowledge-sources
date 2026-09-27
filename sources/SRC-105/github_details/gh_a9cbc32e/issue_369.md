# [Issue #369] Option to show per-XCD memory metrics

source: https://github.com/ROCm/rocprofiler-compute/issues/369
state: closed | updated: 2025-08-06T18:28:29Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
I am trying to optimize an application and would like better visibility into how to get good reuse.

**Describe the solution you'd like**
I would like the option for the memory map to show memory metrics hierarchically (for example, per-XCD) as the memory is disaggregated across the hierarchy (as mentioned here : https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-3-white-paper.pdf) 

**Describe alternatives you've considered**
I've considered using the profiler and microbenchmarks to get XCD-level information and hacking together my own data analysis infrastructure.

Thanks!


## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/58

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
