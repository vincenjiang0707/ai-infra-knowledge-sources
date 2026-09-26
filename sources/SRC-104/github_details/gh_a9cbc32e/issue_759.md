# [Issue #759] [Bug]: profiler crashes when profiling with torch multi processing

source: https://github.com/ROCm/rocprofiler-compute/issues/759
state: closed | updated: 2025-08-06T18:19:26Z
labels: bug, triage

## 正文

### Describe the bug

I tried to profile a script that contains a main method like this
```
if __name__ == '__main__':
    num_processes = 8
    torch.multiprocessing.spawn(test_loop, args=(num_processes, ), nprocs=num_processes)
```

command
```
/opt/rocm/bin/rocprof-compute  profile -n perf_data  -- python3 ./test.py
```

Error:
The profiler crashes after one iteration saying "An instance of rocprof is already running"


Workaround(or single rank hack) for now
```
# Launch following on RANK 0
/opt/rocm/bin/rocprof-compute  profile -n perf_data  -- python3 ./test.py

# Keep closing and relaunching following on the reamining launch for every iteration of /opt/rocm/bin/rocprof-compute
python3 ./test.py
```

### Linux Distribution

Ubuntu 22.04

### ROCm Compute Profiler Version

3.0.0

### GPU

MI300X

### ROCm Version

_No response_

### Cluster name (if applicable)

_No response_

### Reproducer

a script that contains a main method like this
```
if __name__ == '__main__':
    num_processes = 8
    torch.multiprocessing.spawn(test_loop, args=(num_processes, ), nprocs=num_processes)
```

command
```
/opt/rocm/bin/rocprof-compute  profile -n perf_data  -- python3 ./test.py
```

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

### systems-assistant[bot] · 2025-08-06

This issue has been migrated to: https://github.com/ROCm/rocm-systems/issues/33

### amd-hsivasun · 2025-08-06

Imported to ROCm/rocm-systems
