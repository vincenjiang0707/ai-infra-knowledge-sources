# [Issue #625] [Bug]: KeyError

source: https://github.com/ROCm/rocprofiler-compute/issues/625
state: closed | updated: 2025-08-06T18:20:27Z
labels: bug, triage

## 正文

### Describe the bug

Repo process:
1) Go to the sample directory (rocprofiler-compute_source/sample)
2) Run the command:
`rocprof-compute profile -n test1 -k run_forward$async_dispatch_48_attention_4x10x4096x64xf8E4M3FNUZ_generic --no-roof -- ./occupancy`

3) Bear in mind that there is **no kernel named** "run_forward$async_dispatch_48_attention_4x10x4096x64xf8E4M3FNUZ_generic", this test might just exit early instead of running all 15 tests using 15 input files


When I try to profile my application using kernel filter like this:

In the end, timestamps.csv is almost empty (with Dispatch_ID,Kernel_Name)
The error message on screen is:
```
Traceback (most recent call last):
  File "/rocprofiler-compute_source/install/bin/rocprof-compute", line 156, in <module>
    main()
    ~~~~^^
  File "/rocprofiler-compute_source/install/bin/rocprof-compute", line 144, in main
    rocprof_compute.run_profiler()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/rocprofiler-compute_source/install/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
  File "/rocprofiler-compute_source/install/libexec/rocprofiler-compute/rocprof_compute_base.py", line 357, in run_profiler
    profiler.post_processing()
    ~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/rocprofiler-compute_source/install/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
  File "/rocprofiler-compute_source/install/libexec/rocprofiler-compute/rocprof_compute_profile/profiler_rocprof_v1.py", line 100, in post_processing
    self.join_prof()
    ~~~~~~~~~~~~~~^^
  File "/rocprofiler-compute_source/install/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
  File "/rocprofiler-compute_source/install/libexec/rocprofiler-compute/rocprof_compute_profile/profiler_base.py", line 121, in join_prof
    key = _df.groupby(["Kernel_Name", "Grid_Size"]).cumcount()
          ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/root/.pyenv/versions/3.13t-dev/lib/python3.13t/site-packages/pandas/core/frame.py", line 9183, in groupby
    return DataFrameGroupBy(
        obj=self,
    ...<7 lines>...
        dropna=dropna,
    )
  File "/root/.pyenv/versions/3.13t-dev/lib/python3.13t/site-packages/pandas/core/groupby/groupby.py", line 1329, in __init__
    grouper, exclusions, obj = get_grouper(
                               ~~~~~~~~~~~^
        obj,
        ^^^^
    ...<5 lines>...
        dropna=self.dropna,
        ^^^^^^^^^^^^^^^^^^^
    )
    ^
  File "/root/.pyenv/versions/3.13t-dev/lib/python3.13t/site-packages/pandas/core/groupby/grouper.py", line 1043, in get_grouper
    raise KeyError(gpr)
KeyError: 'Grid_Size'
```

### Linux Distribution

Ubuntu22.04

### ROCm Compute Profiler Version

git hash 40ad99eae1e1c3acd1323f47cccbf2966c807122

### GPU

AMD MI300X

### ROCm Version

ROCM6.3.4

### Cluster name (if applicable)

_No response_

### Reproducer

1. Run command:
`rocprof-compute profile -n test1 -k run_forward$async_dispatch_48_attention_4x10x4096x64xf8E4M3FNUZ_generic --no-roof -- ./occupancy`

### Expected behavior

Report no kernel named "run_forward$async_dispatch_48_attention_4x10x4096x64xf8E4M3FNUZ_generic"

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (3)

### dezhiAmd · 2025-03-22

dezhliao@amd.com 
SharkAI team for more details

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/38

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
