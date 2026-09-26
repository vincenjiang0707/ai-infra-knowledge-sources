# [Issue #248] When I disable the GPU option, why do I still report the following CUDA-related error?

source: https://github.com/triton-inference-server/perf_analyzer/issues/248
state: closed | updated: 2025-01-31T22:29:10Z
labels: 

## 正文

The error information is as follows:
```
/home/stage/root/spack-stage-perf-analyzer-main-a3iackh7pcgy7vfebrk5thpng5r6qmih/spack-src/src/cuda_runtime_library_manager.h:28:10: fatal error: cuda_runtim
             e_api.h: No such file or directory
     7829     #include <cuda_runtime_api.h>
     7830              ^~~~~~~~~~~~~~~~~~~~
     7831    compilation terminated.
  >> 7832    make[5]: *** [CMakeFiles/perf_analyzer.dir/build.make:147: CMakeFiles/perf_analyzer.dir/load_manager.cc.o] Error 1
```
Run the following command to reproduce the problem:

```
mkdir build && cd build
cmake -DTRITON_ENABLE_GPU=OFF ..
make -j64
```

## 评论 (3)

### the-david-oy · 2025-01-22

CC: @matthewkotila @nicolasnoble for visibility

### matthewkotila · 2025-01-22

Working on a fix currently :)

### matthewkotila · 2025-01-31

@simon28li fixed (#254) 🙏
