# [Issue #196] Add custom kernel name shortening interface

source: https://github.com/ROCm/rocprofiler-compute/issues/196
state: closed | updated: 2025-08-06T18:35:10Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
Users that profile Kokkos and Raja-based applications would like to be able to "nickname" functions for easier display.

Specifically, we've gotten feedback from code teams at Sandia National Labs that this would increase the usability of Omniperf for them. 

**Describe the solution you'd like**
Allow users to provide a file that contains exact kernel names to match, and shortened strings to replace them with.

**Describe alternatives you've considered**
Pointing to an alternate .csv file could work, but seems pretty fragile/potentially frustrating.
Manually editing the existing dispatch to kernel name mapping doesn't work for all cases: roofline generation will still show the long kernel names on the kernel legend.



## 评论 (4)

### srinathv · 2023-11-02

I like this suggestion.  I would like to understand if somthing like this already exists. 

### IanBogle · 2023-12-13

I encountered a team using roctx-rename and ROCP_RENAME_KERNEL to rename kernels in traces using roctx-region. This could serve as a workaround, except it only changes the .json output, not the .csv output. Using the same environment variable with omniperf did not result in shortened kernel names due to the .json/.csv issue, but also omniperf's rocprof call doesn't seem to use roctx-trace.  

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/68

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
