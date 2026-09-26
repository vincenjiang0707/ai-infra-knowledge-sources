# [Issue #172] Pre-compile metrics at build time.

source: https://github.com/ROCm/rocprofiler-compute/issues/172
state: closed | updated: 2025-08-06T18:39:42Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**
Pre-compile metrics at build time.

**Justification**
Metric compilation leads to a huge overhead in the analyze step (both on the CLI and standalone GUI).  Further, the metrics themselves typically are unchanging for a given version after install (e.g., it's an experts-only thing to do).  Therefore, we would greatly benefit from the ability to 'compile' the metrics are build/install time, such that they we can swap many, many calls to `eval` for loading a pre-compiled python module (say).

**Implementation**
I'm sure Fei has better ideas than me here, but one option would be to simply parse the metric and generate a corresponding python function to evaluate it (e.g., everything inside of the 'AVG', 'MAX', 'MIN', etc.).  This can then be applied row-wise to a data-frame using `apply`.  If needed, we could put all counter values into e.g., a `row['<counter name>']` or some other uniform name for the row that can be passed to the function.

**Additional Notes**

Also, we should drop the separate metrics for 'AVG' v 'MIN' v 'MAX', etc., and  just rely on pandas functions for these to cut down on unnecessary function calls / evals.

cc: @feizheng10

_Originally posted by @arghdos in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6509573_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/78

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
