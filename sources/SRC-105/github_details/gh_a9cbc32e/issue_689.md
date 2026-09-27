# [Issue #689] KeyError: `Grid_Size' when no kernel are launched

source: https://github.com/ROCm/rocprofiler-compute/issues/689
state: closed | updated: 2025-05-06T17:26:34Z
labels: Under Investigation

## 正文

```
rocprof-compute profile -n dummy_mi250x --roof-only --device 0 --mem-level HBM -- sleep 1
```

I get 
```
Empty DataFrame
Columns: [Dispatch_ID, Kernel_Name]
Index: []
Traceback (most recent call last):
  File "/rocprofiler-compute/bin/rocprof-compute", line 156, in <module>
    main()
  File "/rocprofiler-compute/bin/rocprof-compute", line 144, in main
    rocprof_compute.run_profiler()
  File "/rocprofiler-compute/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/rocprofiler-compute/libexec/rocprofiler-compute/rocprof_compute_base.py", line 286, in run_profiler
    profiler.post_processing()
  File "/rocprofiler-compute/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/rocprofiler-compute/libexec/rocprofiler-compute/rocprof_compute_profile/profiler_rocprof_v1.py", line 100, in post_processing
    self.join_prof()
  File "/rocprofiler-compute/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/rocprofiler-compute/libexec/rocprofiler-compute/rocprof_compute_profile/profiler_base.py", line 116, in join_prof
    key = _df.groupby(["Kernel_Name", "Grid_Size"]).cumcount()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/rocprofiler-compute/python-libs/pandas/core/frame.py", line 9183, in groupby
    return DataFrameGroupBy(
           ^^^^^^^^^^^^^^^^^
  File "/rocprofiler-compute/python-libs/pandas/core/groupby/groupby.py", line 1329, in __init__
    grouper, exclusions, obj = get_grouper(
                               ^^^^^^^^^^^^
  File "/rocprofiler-compute/python-libs/pandas/core/groupby/grouper.py", line 1043, in get_grouper
    raise KeyError(gpr)
KeyError: 'Grid_Size'
```

I understand that profiling sleep is a bit of a stretch, but clearly, this is bad experience, I would expect an empty roofline.

This seems linked to https://github.com/ROCm/rocprofiler-compute/issues/294

## 评论 (2)

### ppanchad-amd · 2025-04-30

Hi @etiennemlb. Internal ticket has been created to investigate this issue. Thanks!

### ppanchad-amd · 2025-05-06

@etiennemlb PR (https://github.com/ROCm/rocprofiler-compute/pull/694) has been submitted to fix this issue. Closing ticket. Thanks!
