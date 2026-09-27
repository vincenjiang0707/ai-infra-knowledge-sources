# [Issue #176] Better metric dependency resolution and reuse

source: https://github.com/ROCm/rocprofiler-compute/issues/176
state: closed | updated: 2025-08-06T18:38:57Z
labels: Omniperf Revamp

## 正文

**Describe the suggestion**

Better metric dependency resolution and reuse

**Justification**

Enable re-use of intermediate computations and metrics to avoid code-duplication / copy-paste errors.
For example when looking at the [PoP for VALU FLOPs](https://github.com/AMDResearch/omniperf/blob/ed31b8a988b0fde6a5e11bc949417c82c6db1abc/src/omniperf_analyze/configs/gfx90a/0200_system-speed-of-light.yaml#L23), we:

1. Compute the FLOPs
2. Compute the Peak
3. Recompute the FLOPs and the Peak to find the % of Peak

Other examples would be things like continually recomputing duration, GRBM_GUI_ACTIVE * $numCU, etc., etc.

If we had a more flexible evaluator, we could also theoretically let a user ask for _just_ a specific metric, or group of metrics (and break the "ask for SQ on profile", "ask for section x.y on analyze" chain)

**Implementation**

Less clear what the best way to do this short of a full AST with dependency resolution would be.
In the short term, we could move more values to the list of builtin vars: https://github.com/AMDResearch/omniperf/blob/ed31b8a988b0fde6a5e11bc949417c82c6db1abc/src/omniperf_analyze/utils/parser.py#L77

**Additional Notes**

May not be as important if we can pre-compile metrics

_Originally posted by @arghdos in https://github.com/AMDResearch/omniperf/discussions/153#discussioncomment-6577261_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/75

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
