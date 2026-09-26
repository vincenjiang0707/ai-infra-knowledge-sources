# [Issue #88] [Feature]: Ability to build rocprofiler-sdk for a single target architecture

source: https://github.com/ROCm/rocprofiler-sdk/issues/88
state: closed | updated: 2025-07-28T19:12:34Z
labels: 

## 正文

### Suggestion Description

Hi,

I am running

```bash
cmake --build rocprofiler-sdk-build --target all --parallel 8
```

to build rocprofiler-sdk.

I get errors as:

```
[ 51%] Linking CXX executable ../../../../bin/openmp-target
  CC       lib_otf2_la-OTF2_AttributeValue.lo
/opt/rocm-6.5.0/lib/llvm/bin/llvm-link: No such file or directory: '/opt/rocm-6.5.0/lib/llvm/lib/../runtimes/runtimes-bins/offload/libomptarget-amdgpu-gfx906.bc'
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
gmake[2]: *** [tests/bin/openmp/target/CMakeFiles/openmp-target.dir/build.make:101: bin/openmp-target] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:7953: tests/bin/openmp/target/CMakeFiles/openmp-target.dir/all] Error 2
gmake[1]: *** Waiting for unfinished jobs....
[ 51%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/kernel_dispatch/kernel_dispatch.cpp.o
[ 51%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/kernel_dispatch/profiling_time.cpp.o
[ 51%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/kernel_dispatch/tracing.cpp.o
[ 51%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/kfd/abi.cpp.o
[ 51%] Linking CXX executable ../../../bin/hip-in-libraries
[ 51%] Built target hip-in-libraries
[ 52%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/kfd/kfd.cpp.o
[ 52%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/rccl/abi.cpp.o
[ 52%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/rccl/rccl.cpp.o
[ 52%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/rocdecode/abi.cpp.o
  CC       lib_otf2_la-OTF2_AttributeList.lo
[ 53%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/rocdecode/rocdecode.cpp.o
[ 53%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/rocjpeg/abi.cpp.o
[ 53%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/rocjpeg/rocjpeg.cpp.o
[ 53%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/ompt/ompt.cpp.o
  CC       lib_otf2_la-OTF2_IdMap.lo
/opt/rocm-6.5.0/lib/llvm/bin/llvm-link: No such file or directory: '/opt/rocm-6.5.0/lib/llvm/lib/../runtimes/runtimes-bins/offload/libomptarget-amdgpu-gfx906.bc'
clang++: error: linker command failed with exit code 1 (use -v to see invocation)
gmake[2]: *** [samples/openmp_target/CMakeFiles/openmp-target-sample.dir/build.make:101: bin/openmp-target-sample] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:9365: samples/openmp_target/CMakeFiles/openmp-target-sample.dir/all] Error 2
```

as I removed these large files in `/opt/rocm/lib/llvm/lib` not related to my target architecture gfx950. I am keeping my ROCm install light.

Why do the steps `Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/ompt/ompt.cpp.o` and `Linking CXX executable ../../../../bin/openmp-target` require `/opt/rocm/lib/llvm/lib/libomptarget-amdgpu-gfx*.bc` files of architectures my hardware is not using (here gfx906)?

Is there a way to build rocprofiler-sdk for a single architecture?

Thank you

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_

## 评论 (1)

### jrmadsen · 2025-07-28

The cmake configuration variable is `OPENMP_GPU_TARGETS`, e.g. `cmake -DOPENMP_GPU_TARGETS=gfx90a …`
