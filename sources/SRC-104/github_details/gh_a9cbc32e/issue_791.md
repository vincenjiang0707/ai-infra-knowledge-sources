# [Issue #791] [Bug]: CLI `analyze` results for `Dispatch List` include data with `NaN` only, resulting in errors in `rocprofiler-compute analyze`

source: https://github.com/ROCm/rocprofiler-compute/issues/791
state: closed | updated: 2025-08-06T18:18:51Z
labels: bug, triage, Under Investigation

## 正文

### Describe the bug

Hi,

@yogi81 profiled vllm using rocprof-compute with a filter `--kernel fused_moe_kernel`, which was found through a more top level pytorch profiler.

As rocprof-compute needs to run multiple times to collect metrics (I assume as different performance counters are recorded in different runs for them to be more accurate?), the user needs to restart vllm multiple times through `vllm serve` manually + do requests, and kill it manually as this is an infinite server. Eventually, this works and `rocprofiler-compute profile` successfully finishes.

The collected trace is available at: https://github.com/yogi81/rocmprofiler.

Calling `rocprofiler-compute analyze` on this data, we get:

```
Traceback (most recent call last):
  File "/usr/bin/rocprofiler-compute", line 156, in <module>
    main()
  File "/usr/bin/rocprofiler-compute", line 148, in main
    rocprof_compute.run_analysis()
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/rocprof_compute_base.py", line 355, in run_analysis
    analyzer.run_analysis()
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/utils.py", line 53, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/rocprof_compute_analyze/analysis_cli.py", line 90, in run_analysis
    tty.show_all(
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/tty.py", line 114, in show_all
    adjusted_name = base_df["Kernel_Name"].apply(
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/pandas/core/series.py", line 4924, in apply
    ).apply()
      ^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/pandas/core/apply.py", line 1427, in apply
    return self.apply_standard()
           ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/pandas/core/apply.py", line 1507, in apply_standard
    mapped = obj._map_values(
             ^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/pandas/core/base.py", line 921, in _map_values
    return algorithms.map_array(arr, mapper, na_action=na_action, convert=convert)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/pandas/core/algorithms.py", line 1743, in map_array
    return lib.map_infer(values, mapper, convert=convert)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "lib.pyx", line 2972, in pandas._libs.lib.map_infer
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/tty.py", line 115, in <lambda>
    lambda x: string_multiple_lines(x, 80, 4)
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/rocm-6.4.1/libexec/rocprofiler-compute/utils/tty.py", line 47, in string_multiple_lines
    while idx < len(source) and len(lines) < max_rows:
                ^^^^^^^^^^^
TypeError: object of type 'float' has no len()
```

It appears that the data for `Dispatch List` contains some data with `Kernel_Name` being `nan`, later resulting in this issue.

https://github.com/ROCm/rocprofiler-compute/blob/61a9381edfd781cdbef83aa8837d77531bbb661f/src/utils/tty.py#L134-L140

https://github.com/ROCm/rocprofiler-compute/blob/61a9381edfd781cdbef83aa8837d77531bbb661f/src/utils/tty.py#L37-L43

I assume these are kernels that were not filtered with `--name`? See:

```
type, table_config raw_csv_table {'id': 2, 'title': 'Dispatch List', 'source': 'pmc_dispatch_info.csv'}
table_config[id] 2
base_df       Dispatch_ID          Kernel_Name  GPU_ID
0           612.0  fused_moe_kernel.kd     1.0
1           615.0  fused_moe_kernel.kd     1.0
2           636.0  fused_moe_kernel.kd     1.0
3           639.0  fused_moe_kernel.kd     1.0
4           831.0  fused_moe_kernel.kd     1.0
...           ...                  ...     ...
6467          NaN                  NaN     NaN
6468          NaN                  NaN     NaN
6469          NaN                  NaN     NaN
6470          NaN                  NaN     NaN
6471          NaN                  NaN     NaN
```

Is this a known issue? Why do we have data with NaN? Should they just be filtered out, or is it a deeper issue? cc @coleramos425 

Thank you.

cc @yogi81

### Linux Distribution

22.04.5 LTS (Jammy Jellyfish)

### ROCm Compute Profiler Version

3.1.0 (release) / f29f1341

### GPU

MI300X

### ROCm Version

rocm-6.4.1

### Cluster name (if applicable)

_No response_

### Reproducer

Can share if needed later.

### Expected behavior

_No response_

### Relevant log output

```shell

```

### Screenshots

_No response_

### Additional Context

_No response_

## 评论 (10)

### eddieliao · 2025-07-21

I was curious if there was ever an update on this? I am running into a similar issue when profiling with `rocprof-compute` on MIGraphX and MLIR kernels. In my case, I do not see any NaNs, but instead `pmc_dispatch_info.csv` ends with a row of empty values:
```
...
601.0,mlir_convolution,0.0
602.0,mlir_convolution,0.0
603.0,mlir_convolution,0.0
604.0,mlir_convolution,0.0
605.0,mlir_convolution,0.0
606.0,mlir_convolution,0.0
607.0,mlir_convolution,0.0
608.0,mlir_convolution,0.0
,,
```
Running analyze gives me the same error as reported above: `TypeError: object of type 'float' has no len()`.

### fxmarty-amd · 2025-07-22

@eddieliao Unfortunately I was not able to debug further this issue, maybe somebody from rocprofiler-compute team could have a look. I just reproduced it from the trace collected by @yogi81.

### fxmarty-amd · 2025-07-22

@eddieliao if you are able to share a full reproduction it might help. In my case I only got a workloads compute trace dump, not full repro.

### eddieliao · 2025-07-22

> [@eddieliao](https://github.com/eddieliao) if you are able to share a full reproduction it might help. In my case I only got a workloads compute trace dump, not full repro.

Here's a simple workflow that reproduced the issue for me. I am building MIGraphX from source although it can be installed through the package manager to obtain the migraphx-driver as well.

1. Install rocprof-compute using apt following the instructions here: https://rocm.docs.amd.com/projects/rocprofiler-compute/en/latest/install/core-install.html#install-via-package-manager
2. Run the following command: `ROCPROF=rocprofv3 rocprof-compute profile -n repro_workload -- ./build/bin/driver run --test`
3. The corresponding trace throws the error mentioned above when using analyze: `rocprof-compute analyze -p /workloads/repro_workload/MI300X_A1/ -b 2`

I am on a Ubuntu 22.04 container running ROCm 6.4.2.

### fxmarty-amd · 2025-07-23

cc @vedithal-amd 

### ppanchad-amd · 2025-07-23

Hi @fxmarty-amd. I have triaged this issue to @taylding-amd who will be assisting with the investigation. Thanks!

### taylding-amd · 2025-08-06

Hi @gxmarty-amd, I’m not very familiar with vllm. Could you please provide detailed reproduction steps, or try running the latest version of our code within the Docker environment and let me know if the issue still occurs? I tested a similar MIGraphX bug but was unable to reproduce the issue, which suggests it may have already been resolved in the latest code.
Here's the [instruction](https://github.com/ROCm/rocprofiler-compute?tab=readme-ov-file#testing) about how to use the docker.

Thank you!

### fxmarty-amd · 2025-08-06

Thank you @taylding-amd! Let me try to reproduce with latest version.

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/32

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
