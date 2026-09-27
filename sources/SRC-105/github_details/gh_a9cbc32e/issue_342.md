# [Issue #342] Add an interface to specify a metric configuration file to filter omniperf output

source: https://github.com/ROCm/rocprofiler-compute/issues/342
state: closed | updated: 2025-08-06T18:29:52Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**
It can be cumbersome to type all the block fields you'd like to see in the omniperf output.
It is also somewhat difficult to tell which field numbers correspond to which metrics.
**Describe the solution you'd like**
An interface that allows passing a file specifying the blocks to display in omniperf analyze.
This can increase the readability of omniperf analyze invocations as sets of metrics can be grouped in user-named files, and if metric numbers change in subsequent omniperf versions, users only need to change the configuration file once and they should be up-to-date.

**Describe alternatives you've considered**
Saving omniperf invocations in scripts could be very similar, but I think users would like the ability to use configuration files for analyze output.


## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/61

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
