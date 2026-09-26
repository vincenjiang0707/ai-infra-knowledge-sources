# [Issue #163] Allow dumping of computed metrics per-kernel for further analysis

source: https://github.com/ROCm/rocprofiler-compute/issues/163
state: closed | updated: 2025-08-06T18:40:30Z
labels: enhancement

## 正文

**Is your feature request related to a problem? Please describe.**

This is a proposed extension of the current `--save-dfs` mechanism.
Essentially, today when using --save-dfs, Omniperf will compute the metrics, apply the min/max/avg, etc. aggregations, and then save that to a file.

In some cases, (e.g., plotting, further data analysis, etc.) it's more useful to be able to get each of the metrics _per_ kernel launch, for instance, so that one could suck in the data-frame and do a kNN (or whatever) to look for correlations of kernel runtime w/ metrics "outliers", or to plot the metrics over multiple invocations, etc.

**Describe the solution you'd like**

Provide a mode to allow computation of the metrics on each dispatch, and save that result to a file.
This should allow filtering of dispatches, and blocks, as normal, i.e., it only skips the min/max/avg computation steps.

**Describe alternatives you've considered**

One _can_ walk through each dispatch and use `--dispatch <X>` to filter the dataframe to just that dispatch, and dump like 8000 different data-frams, but that is... quite slow, particularly with the current metric parsing overheads.

**Additional context**

None


## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/83

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
