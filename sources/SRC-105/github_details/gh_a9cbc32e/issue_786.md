# [Issue #786] [Bug]: vanilla GUI does not display correctly (IndexError("single positional indexer is out-of-bounds"))

source: https://github.com/ROCm/rocprofiler-compute/issues/786
state: closed | updated: 2025-07-23T07:57:35Z
labels: bug, triage

## 正文

### Describe the bug

Hi,

I am using 61a9381edfd781cdbef83aa8837d77531bbb661f on CDNA4, using https://github.com/ROCm/rocprofiler-sdk/commit/e7616c3aad9ed99dbc2d1fcf97b1dbdc7399905f.

I am running `CUDA_VISIBLE_DEVICES=0 ROCPROF=rocprofiler-sdk ROCPROFCOMPUTE_LOGLEVEL=debug /repos/rocprofiler-compute/install3/3.1.0/bin/rocprof-compute analyze -p workloads/my_kernel/MI355/ --gui`

Here is backtrace when selecting the specific kernel in the GUI:

```
  ERROR Exception on /_dash-update-component [POST]
Traceback (most recent call last):
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/dash/dash.py", line 1484, in dispatch
    response_data = ctx.run(partial_func)
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/dash/_callback.py", line 698, in add_context
    raise err
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/dash/_callback.py", line 689, in add_context
    output_value = _invoke_callback(func, *func_args, **func_kwargs)  # type: ignore[reportArgumentType]
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/dash/_callback.py", line 58, in _invoke_callback
    return func(*args, **kwargs)  # %% callback invoked %%
  File "/repos/rocprofiler-compute/install3/3.1.0/libexec/rocprofiler-compute/rocprof_compute_analyze/analysis_webui.py", line 226, in generate_from_filter
    content = determine_chart_type(
  File "/repos/rocprofiler-compute/install3/3.1.0/libexec/rocprofiler-compute/utils/logger.py", line 48, in wrap_function
    result = function(*args, **kwargs)
  File "/repos/rocprofiler-compute/install3/3.1.0/libexec/rocprofiler-compute/rocprof_compute_analyze/analysis_webui.py", line 373, in determine_chart_type
    d_figs = build_bar_chart(display_df, table_config, barchart_elements, norm_filt)
  File "/repos/rocprofiler-compute/install3/3.1.0/libexec/rocprofiler-compute/utils/gui.py", line 218, in build_bar_chart
    display_df[display_df["Metric"] == "HBM Bandwidth"]["Avg"].iloc[0]
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/pandas/core/indexing.py", line 1103, in __getitem__
    return self._getitem_axis(maybe_callable, axis=axis)
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/pandas/core/indexing.py", line 1656, in _getitem_axis
    self._validate_integer(key, axis)
  File "/opt/conda/envs/py_3.10/lib/python3.10/site-packages/pandas/core/indexing.py", line 1589, in _validate_integer
    raise IndexError("single positional indexer is out-of-bounds")
IndexError: single positional indexer is out-of-bounds
```

and then I still get `To dive deeper, use the top drop down menus to isolate particular kernel(s) or dispatch(s). You will then see the web page update with additional low-level metrics specific to the filter you've applied.` in the GUI.

Is this a known issue?

In my case it appear that `display_df[display_df['Metric'] == 'HBM Bandwidth']` is an `Empty DataFrame` at https://github.com/ROCm/rocprofiler-compute/blob/61a9381edfd781cdbef83aa8837d77531bbb661f/src/utils/gui.py#L217-L219

The dataframe rather contains:
```
------- display_df                                   Metric         Avg  Unit
Metric_ID
17.1.0                       Utilization     96.9881   Pct
17.1.1                         Bandwidth    34.43659   Pct
17.1.2                          Hit Rate   93.775099   Pct
17.1.3                 L2-Fabric Read BW  798.694667  Gb/s
17.1.4     L2-Fabric Write and Atomic BW   44.280983  Gb/s
display_df['Metric'] Metric_ID
17.1.0                      Utilization
17.1.1                        Bandwidth
17.1.2                         Hit Rate
17.1.3                L2-Fabric Read BW
17.1.4    L2-Fabric Write and Atomic BW
```

### Linux Distribution

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### ROCm Compute Profiler Version

rocprofiler-compute version: 3.2.0 (release)

### GPU

AMD MI355

### ROCm Version

/opt/rocm-6.5.0/bin/rocprof

### Cluster name (if applicable)

_No response_

### Reproducer

I can share if needed.

### Expected behavior

_No response_

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (2)

### xuchen-amd · 2025-07-04

Hi @fxmarty-amd, just syncing comments from #787 for visibility.

The reason for
> display_df[display_df['Metric'] == 'HBM Bandwidth'] is an Empty DataFrame

is because `HBM Bandwidth` is calculated with [`"hbmBandwidth": "($max_mclk / 1000 * 32 * $num_hbm_channels)"`](https://github.com/ROCm/rocprofiler-compute/blob/61a9381edfd781cdbef83aa8837d77531bbb661f/src/utils/parser.py#L89). With this, please check if you are seeing the warning message:
"WARNING max_mclk is not available in sysinfo.csv, please provide the correct value using --specs-correction".

With a `max_mclk` value, you should see `HBM Bandwidth` correctly calculated and displayed:
<img width="467" alt="image" src="https://github.com/user-attachments/assets/f5e4cbe0-d6d1-45f9-af5c-604129fb03e1" />

Usage for `--specs-correction` is at: [argparser.py#L678](https://github.com/ROCm/rocprofiler-compute/blob/61a9381edfd781cdbef83aa8837d77531bbb661f/src/argparser.py#L678)

### fxmarty-amd · 2025-07-23

Fixed by https://github.com/ROCm/rocprofiler-compute/pull/825
