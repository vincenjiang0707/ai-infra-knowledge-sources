# [Issue #548] [Req]: Update documentation in `develop` branch

source: https://github.com/ROCm/rocprofiler-compute/issues/548
state: closed | updated: 2025-08-06T18:23:39Z
labels: enhancement, triage

## 正文

### Is your feature request related to a problem?

While testing some of the latest functionality, I don't see the newest options are mentioned in the documentation. If I take inventory, I see the following new rocprof-compute options:

## New MPI related options

- https://github.com/ROCm/rocprofiler-compute/blob/da1bd045abbe7a01c606b70cdb55c14795d2d5f2/src/argparser.py#L133-L134
- https://github.com/ROCm/rocprofiler-compute/blob/da1bd045abbe7a01c606b70cdb55c14795d2d5f2/src/argparser.py#L255-L256

## New rocprofv3 related options

- https://github.com/ROCm/rocprofiler-compute/blob/da1bd045abbe7a01c606b70cdb55c14795d2d5f2/src/argparser.py#L142-L143
- https://github.com/ROCm/rocprofiler-compute/blob/da1bd045abbe7a01c606b70cdb55c14795d2d5f2/src/argparser.py#L150-L151
- https://github.com/ROCm/rocprofiler-compute/blob/da1bd045abbe7a01c606b70cdb55c14795d2d5f2/src/argparser.py#L265-L266
- https://github.com/ROCm/rocprofiler-compute/blob/da1bd045abbe7a01c606b70cdb55c14795d2d5f2/src/argparser.py#L574-L575
- https://github.com/ROCm/rocprofiler-compute/blob/da1bd045abbe7a01c606b70cdb55c14795d2d5f2/src/argparser.py#L596-L597
- https://github.com/ROCm/rocprofiler-compute/blob/da1bd045abbe7a01c606b70cdb55c14795d2d5f2/src/argparser.py#L601-L602

No reference of these option or how to use in the `develop` branch docs

### Describe the solution you'd like

In my mind these should all be mentioned in the docs profiling section [docs/how-to/profile/mode.rst](https://github.com/ROCm/rocprofiler-compute/blob/develop/docs/how-to/profile/mode.rst). In addition, there should be a brief write up on "What is spatial multiplexing".

### Describe any alternatives you've considered

_No response_

### Additional context

_No response_

## 评论 (2)

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/46

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
