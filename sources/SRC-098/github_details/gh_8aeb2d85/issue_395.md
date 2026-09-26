# [Issue #395] "comm_ops.cu", line 25: error: cannot open source file "curand.h"

source: https://github.com/NVIDIA/nccl-tests/issues/395
state: open | updated: 2026-09-10T15:52:58Z
labels: 

## 正文

Compiling nccl-tests fails by default with the NVIDIA HPC SDK.

The HPC SDK does not include curand.h as part of the core cuda install. It is instead part of math_libs:

```
gpu-0001:~ # find /opt/nvidia/hpc_sdk/Linux_x86_64/ -type f -name 'curand.h'
/opt/nvidia/hpc_sdk/Linux_x86_64/26.3/math_libs/12.9/targets/x86_64-linux/include/curand.h
/opt/nvidia/hpc_sdk/Linux_x86_64/26.3/math_libs/13.1/targets/x86_64-linux/include/curand.h
```

Setting `CUDA_HOME` does not pull in math_libs and building fails.
Additionally, the nccl-tests make cfg doesn't support most standard environment variables like CXXFLAGS/NVCUFLAGS. The only workaround I found was:
```
export NVCC_PREPEND_FLAGS="-I/opt/nvidia/hpc_sdk/Linux_x86_64/26.3/math_libs/13.1/include"
```

In my opinion, this should be much cleaner. Either skip building the new benchmarks, or support arguments to nccl-tests to make it work smoother.

## 评论 (3)

### sjeaugey · 2026-09-10

Let me check .. I 'm surprised we even use curand. Seems like an include which wasn't cleaned up.

### codambro · 2026-09-10

Added as part of the new comm_ops_perf:
https://github.com/NVIDIA/nccl-tests/commit/7b31df28ee0bf8d156d9e8555ec128f747b8759c

### codambro · 2026-09-10

As far as I can tell though, it isn't actually used
