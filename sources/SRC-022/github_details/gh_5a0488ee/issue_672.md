# [Issue #672] compilation issue

source: https://github.com/ROCm/rccl/issues/672
state: closed | updated: 2023-01-27T18:32:02Z
labels: 

## 正文

I'm getting several "symbol not found error"-s when compiling with rocm/5.2.0:

```
$ git clone https://github.com/ROCmSoftwarePlatform/rccl.git
$ cd rccl
$ mkdir build && cd build
$ cmake --version
cmake version 3.23.2

CMake suite maintained and supported by Kitware (kitware.com/cmake).

$ hipcc --version
HIP version: 5.2.21151-afdc89f8
AMD clang version 14.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.2.0 22204 50d6d5d5b608d2abd6af44314abc6ad20036af3b)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-5.2.0/llvm/bin

$ cmake '-DCMAKE_CXX_COMPILER=hipcc' \
      '-DROCM_PATH=/opt/rocm-5.2.0' \
      '-DCMAKE_HIP_ARCHITECTURES=gfx90a' \
      ..

rccl/build/src/include/alloc.h:196:1314:  errors generatederror:  when compiling for gfx90a.
use of undeclared identifier 'cudaThreadExchangeStreamCaptureMode'; did you mean 'hipThreadExchangeStreamCaptureMode'?
  CUDACHECK(cudaThreadExchangeStreamCaptureMode(&mode));

rccl/build/src/misc/strongstream.cpp:261:15: error: use of undeclared identifier 'cudaLaunchHostFunc'; did you mean 'hipLaunchHostFunc'?
    CUDACHECK(cudaLaunchHostFunc(ss->cudaStream, fn, arg));
```

Replacing `cudaThreadExchangeStreamCaptureMode` with `hipThreadExchangeStreamCaptureMode` and `cudaLaunchHostFunc` with `hipLaunchHostFunc` solved the issue, but only after deleting build and rerunning cmake (because cmake runs hipify step during generation).

## 评论 (3)

### gilbertlee-amd · 2023-01-17

Hi @frobnitzem,
Unfortunately, you may need to install ROCm 5.4 which should have the correct symbols in order to get around this current issue, or use an older version of RCCL, e.g. https://github.com/ROCmSoftwarePlatform/rccl/tree/release/rocm-rel-5.2.

### frobnitzem · 2023-01-27

Noted.  Since this package seems to be relatively quickly changing, it would be nice to put "Use a matching rocm version" in the Requirements section of the README.md.

### gilbertlee-amd · 2023-01-27

Thanks - will do.
