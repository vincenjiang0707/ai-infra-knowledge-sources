# [Issue #777] [Bug]: KeyError: 'Transaction' from GUI

source: https://github.com/ROCm/rocprofiler-compute/issues/777
state: closed | updated: 2025-07-23T07:57:56Z
labels: bug, triage

## 正文

### Describe the bug

My Installation:

```
# Example docker image
docker.io/rocm/vllm-dev:20250114
# Install latest version. It seems to have GUI bug "KeyError: 'Transaction'" but cli is fine
mkdir -p /app; cd /app
git clone https://github.com/ROCm/rocprofiler-compute 
git clone https://github.com/ROCm/rocprofiler-sdk 
cd rocprofiler-compute
git checkout amd-staging; git pull   
rm -rf /usr/lib/python3/dist-packages/blinker* # blinker  was installed using distutils in the image which block the pip dependency
python3 -m pip install -r requirements.txt -r requirements-test.txt
# Make it global
export PATH=/app/rocprofiler-compute/src/:$PATH
rocprof-compute --version # Check rocprof-compute is ready

cd /app/rocprofiler-sdk/ 
rm -rf build install  
apt-get update; apt-get install -y libdw-dev           
cmake -B build -D CMAKE_INSTALL_PREFIX=install -D CMAKE_PREFIX_PATH=/opt/rocm -D CMAKE_HIP_COMPILER=/usr/bin/amdclang++ -D ROCPROFILER_BUILD_TESTS=OFF -D ROCPROFILER_BUILD_SAMPLES=OFF .
cmake --build build --target all --parallel 8
ls build/bin/rocprofv3
export ROCPROF=/app/rocprofiler-sdk/build/bin/rocprofv3 
```

Profile and analyze on linux machine
```
cd  /app/rocprofiler-compute/sample
hipcc -o vcopy vcopy.cpp
export HIP_VISIBLE_DEVICES=0
rocprof-compute profile -n vcopy_data   -- ./vcopy -n 1048576 -b 256
rocprof-compute analyze -p workloads/vcopy_data/MI300X_A1/ --gui
```

Open Chrome for GUI 
```
ssh -L 8050:localhost:8050 jacchang@IP
```

![Image](https://github.com/user-attachments/assets/5e76906d-eeae-4af7-a798-9edd8e2aca0e)

After I selected the kernel vecCopy, the orange rectangle still declared that I should choose the kernel or dispatch ID for showing further profiling info.
I checked the linux log and there was error which showed "Transaction" wasn't the key in the pandas storage.
```
Traceback (most recent call last):
  File "/usr/local/lib/python3.12/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
         ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/dash/dash.py", line 1484, in dispatch
    response_data = ctx.run(partial_func)
                    ^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/dash/_callback.py", line 698, in add_context
    raise err
  File "/usr/local/lib/python3.12/dist-packages/dash/_callback.py", line 689, in add_context
    output_value = _invoke_callback(func, *func_args, **func_kwargs)  # type: ignore[reportArgumentType]
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/dash/_callback.py", line 58, in _invoke_callback
    return func(*args, **kwargs)  # %% callback invoked %%
           ^^^^^^^^^^^^^^^^^^^^^
  File "/app/rocprofiler-compute/src/rocprof_compute_analyze/analysis_webui.py", line 226, in generate_from_filter
    content = determine_chart_type(
              ^^^^^^^^^^^^^^^^^^^^^
  File "/app/rocprofiler-compute/src/utils/logger.py", line 48, in wrap_function
    result = function(*args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/rocprofiler-compute/src/rocprof_compute_analyze/analysis_webui.py", line 373, in determine_chart_type
    d_figs = build_bar_chart(display_df, table_config, barchart_elements, norm_filt)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/rocprofiler-compute/src/utils/gui.py", line 155, in build_bar_chart
    nested_bar = multi_bar_chart(table_config["id"], display_df)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/app/rocprofiler-compute/src/utils/gui.py", line 60, in multi_bar_chart
    nested_bar[row["Transaction"]][row["Type"]] = row["Avg"]
               ~~~^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/pandas/core/series.py", line 1121, in __getitem__
    return self._get_value(key)
           ^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/pandas/core/series.py", line 1237, in _get_value
    loc = self.index.get_loc(label)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/dist-packages/pandas/core/indexes/base.py", line 3812, in get_loc
    raise KeyError(key) from err
KeyError: 'Transaction'

```
CLI analyze, FYI
```rocprof-compute analyze -p workloads/vcopy_data/MI300X_A1/ -b 2 3 4 5 -k 0    ```
![Image](https://github.com/user-attachments/assets/1e53fa7e-d97f-431b-babb-07b78babe658)


### Linux Distribution

Ubuntu 22.04.5 LTS (Jammy Jellyfish)

### ROCm Compute Profiler Version

3.2.0

### GPU

MI300X

### ROCm Version

ROCm 6.3.0

### Cluster name (if applicable)

_No response_

### Reproducer

Please see the description of how I install the tool and do profiling.

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

### fxmarty-amd · 2025-07-03

same issue after fixing https://github.com/ROCm/rocprofiler-compute/issues/786

we have no `Transaction` here:
```
------- display_df                                Metric            Avg      Min       Max               Unit
Metric_ID
17.4.0        Stalled on Latency FIFO     222.561086      0.0    2895.0  Cycles per kernel
17.4.1     Stalled on Write Data FIFO            0.0      0.0       0.0  Cycles per kernel
17.4.2     Input Buffer Stalled on L2  104657.977376  62318.0  185239.0  Cycles per kernel
nested_bar {'Read': {}, 'Write': {}}
row Metric    Stalled on Latency FIFO
Avg                           222
Min                           0.0
Max                        2895.0
Unit            Cycles per kernel
```

The CLI does not have read/write here so I am confused:

![Image](https://github.com/user-attachments/assets/ca1685e2-bc82-4a00-85e7-4fd152b3f76f)

### fxmarty-amd · 2025-07-23

Fixed by https://github.com/ROCm/rocprofiler-compute/pull/825
