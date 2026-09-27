# [Issue #559] [Bug]: Rocprofv2 should be accepted for gfx908

source: https://github.com/ROCm/rocprofiler-compute/issues/559
state: closed | updated: 2025-07-02T15:26:14Z
labels: bug, triage, Under Investigation

## 正文

### Describe the bug

rocprofv2 is supported on gfx908 see:
https://github.com/ROCm/rocprofiler/blob/amd-staging/README.md

However rocprofv2 is masked away on gfx908 by:
https://github.com/ROCm/rocprofiler-compute/blob/bceddb094316a304334f0940c962eee85f011ef3/src/rocprof_compute_soc/soc_gfx908.py#L45

Eiting this line to read 'self.set_compatible_profilers(["rocprofv1", "rocprofv2", "rocscope", "rocprofv3"])'
allows:
`ROCPROF=rocprofv2 install/3.0.0/bin/rocprof-compute profile -V -V -n occupancy -k vgprbound --kernel-names vgprbound rocprofiler-compute/sample/occupancy` to complete with out problems, and all metrics actually supported by gfx908 (see issue https://github.com/ROCm/rocprofiler-compute/issues/558) work fine.

Further rocprofv1 appears to be currently broken see https://github.com/ROCm/rocprofiler-compute/issues/521


### Linux Distribution

any

### ROCm Compute Profiler Version

git @ 3396ba39064afe5946a9ccf37fb9130ad0bc0cfd

### GPU

MI100

### ROCm Version

6.3.2

### Cluster name (if applicable)

_No response_

### Reproducer

ROCPROF=rocprofv2 rocprof-compute profile -V -V -n occupancy -k vgprbound --kernel-names vgprbound rocprofiler-compute/sample/occupancy


### Expected behavior

rocprofv2 should be allowed on gfx908, it works fine.

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (1)

### ppanchad-amd · 2025-07-02

This is by design. rocprof v1 and v2 are deprecated. Closing ticket.
