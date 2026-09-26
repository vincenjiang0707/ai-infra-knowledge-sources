# [Issue #62] [Issue]: Static asserts (incorrectly) reporting ABI breaks when building rocprofiler-sdk from source

source: https://github.com/ROCm/rocprofiler-sdk/issues/62
state: closed | updated: 2025-07-08T10:50:40Z
labels: Under Investigation

## 正文

### Problem Description

As described in the discussion [here](https://github.com/ROCm/rocprofiler-sdk/issues/51#issuecomment-2850427914), attempting to build rocprofiler-sdk from source (with an external libdw, should that be relevant) runs into static asserts that claim the set of functions introduced in ROCm 6.3.0 are ABI breakers in rocprofiler-sdk. This is obviously not the case, but the asserts nevertheless are firing for some reason.

### Operating System

Rocky Linux 8.9

### CPU

AMD EPYC 7702 64-Core Processor

### GPU

AMD Instinct MI210

### ROCm Version

ROCm 6.3.0-195

### ROCm Component

_No response_

### Steps to Reproduce

My `build.sh` for amdclang is as follows; the compiler lines may be dropped or edited for GCC, of course.
```
#!/bin/bash

cmake                                         \
      -B rocprofiler-sdk-build                \
      -D ROCPROFILER_BUILD_TESTS=ON           \
      -D ROCPROFILER_BUILD_SAMPLES=ON         \
      -D CMAKE_INSTALL_PREFIX=/data/horse/ws/wwilliam/rocprofv3-build/sw/rocprofiler-sdk       \
      -D libdw_INCLUDE_DIR=/data/horse/ws/wwilliam-rocprofv3-build/sw/elfutils/include \
      -D libdw_LIBRARY=/data/horse/ws/wwilliam-rocprofv3-build/sw/elfutils/lib/libdw.so \
      -D drm_LIBRARY=/opt/amdgpu/lib64/libdrm.so \
      -D drm_amdgpu_LIBRARY=/opt/amdgpu/lib64/libdrm_amdgpu.so \
      -D CMAKE_BUILD_CONFIG=RelWithDebInfo \
      -D CMAKE_C_COMPILER=amdclang \
      -D CMAKE_CXX_COMPILER=amdclang++ \
       rocprofiler-sdk-source

cmake --build rocprofiler-sdk-build --target all --parallel 8
```


There is only one ROCm install on the system, in `/opt/rocm-6.3.0-195`, also symlinked to `/opt/rocm`.

GCC 8.5 output below:
```
[ 24%] Building CXX object source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/hip/abi.cpp.o
cd /data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-build/source/lib/rocprofiler-sdk && /usr/bin/c++ -DAMD_INTERNAL_BUILD=1 -DGLOG_USE_GLOG_EXPORT -DROCPROFILER_HAS_GHC_LIB_FILESYSTEM=1 -DROCPROFILER_SDK_USE_SYSTEM_RCCL=0 -DROCPROFILER_SDK_USE_SYSTEM_ROCDECODE=0 -DROCPROFILER_SDK_USE_SYSTEM_ROCJPEG=0 -DUSE_PROF_API=1 -DYAML_CPP_STATIC_DEFINE -D__HIP_PLATFORM_AMD__=1 -Drocprofiler_EXPORTS=1 -I/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-build/source/include -I/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/include -I/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source -I/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/external/yaml-cpp/include -I/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/external/ptl/source -I/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-build/external/ptl/source -isystem /opt/rocm-6.3.0-195/include -isystem /data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/external/filesystem/include -isystem /data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-build/external/glog -isystem /data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/external/glog/src -isystem /data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/external/fmt/include -isystem /data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/external/elfio -isystem /opt/amdgpu/include/libdrm -isystem /opt/amdgpu/include -isystem /data/horse/ws/wwilliam-rocprofv3-build/sw/elfutils/include -O3 -DNDEBUG -std=c++17 -fPIC -fvisibility=hidden -fvisibility-inlines-hidden -W -Wall -Wno-unknown-pragmas -Wno-error=extra -Wno-unused-variable -Wno-error=unused-but-set-variable -Wno-error=unused-but-set-parameter -Wno-error=shadow -faligned-new -fstack-protector-strong -Wstack-protector -pthread -MD -MT source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/hip/abi.cpp.o -MF CMakeFiles/rocprofiler-sdk-object-library.dir/hip/abi.cpp.o.d -o CMakeFiles/rocprofiler-sdk-object-library.dir/hip/abi.cpp.o -c /data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp
In file included from /data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:26:
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/common/abi.hpp:68:36: error: static assertion failed: ABI break for ::HipDispatchTable.hipSetValidDevices_fn. Only add new function pointers to end of struct and do not rearrange them
             offsetof(TABLE, ENTRY) == ::rocprofiler::common::abi::compute_table_offset(NUM),       \
                                    ^
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:513:1: note: in expansion of macro ‘ROCP_SDK_ENFORCE_ABI’
 ROCP_SDK_ENFORCE_ABI(::HipDispatchTable, hipSetValidDevices_fn, 445);
 ^~~~~~~~~~~~~~~~~~~~
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/common/abi.hpp:68:36: error: static assertion failed: ABI break for ::HipDispatchTable.hipMemcpyAtoD_fn. Only add new function pointers to end of struct and do not rearrange them
             offsetof(TABLE, ENTRY) == ::rocprofiler::common::abi::compute_table_offset(NUM),       \
                                    ^
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:514:1: note: in expansion of macro ‘ROCP_SDK_ENFORCE_ABI’
 ROCP_SDK_ENFORCE_ABI(::HipDispatchTable, hipMemcpyAtoD_fn, 446);
 ^~~~~~~~~~~~~~~~~~~~
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/common/abi.hpp:68:36: error: static assertion failed: ABI break for ::HipDispatchTable.hipMemcpyDtoA_fn. Only add new function pointers to end of struct and do not rearrange them
             offsetof(TABLE, ENTRY) == ::rocprofiler::common::abi::compute_table_offset(NUM),       \
                                    ^
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:515:1: note: in expansion of macro ‘ROCP_SDK_ENFORCE_ABI’
 ROCP_SDK_ENFORCE_ABI(::HipDispatchTable, hipMemcpyDtoA_fn, 447);
 ^~~~~~~~~~~~~~~~~~~~
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/common/abi.hpp:68:36: error: static assertion failed: ABI break for ::HipDispatchTable.hipMemcpyAtoA_fn. Only add new function pointers to end of struct and do not rearrange them
             offsetof(TABLE, ENTRY) == ::rocprofiler::common::abi::compute_table_offset(NUM),       \
                                    ^
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:516:1: note: in expansion of macro ‘ROCP_SDK_ENFORCE_ABI’
 ROCP_SDK_ENFORCE_ABI(::HipDispatchTable, hipMemcpyAtoA_fn, 448);
 ^~~~~~~~~~~~~~~~~~~~
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/common/abi.hpp:68:36: error: static assertion failed: ABI break for ::HipDispatchTable.hipMemcpyAtoHAsync_fn. Only add new function pointers to end of struct and do not rearrange them
             offsetof(TABLE, ENTRY) == ::rocprofiler::common::abi::compute_table_offset(NUM),       \
                                    ^
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:517:1: note: in expansion of macro ‘ROCP_SDK_ENFORCE_ABI’
 ROCP_SDK_ENFORCE_ABI(::HipDispatchTable, hipMemcpyAtoHAsync_fn, 449);
 ^~~~~~~~~~~~~~~~~~~~
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/common/abi.hpp:68:36: error: static assertion failed: ABI break for ::HipDispatchTable.hipMemcpyHtoAAsync_fn. Only add new function pointers to end of struct and do not rearrange them
             offsetof(TABLE, ENTRY) == ::rocprofiler::common::abi::compute_table_offset(NUM),       \
                                    ^
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:518:1: note: in expansion of macro ‘ROCP_SDK_ENFORCE_ABI’
 ROCP_SDK_ENFORCE_ABI(::HipDispatchTable, hipMemcpyHtoAAsync_fn, 450);
 ^~~~~~~~~~~~~~~~~~~~
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/common/abi.hpp:68:36: error: static assertion failed: ABI break for ::HipDispatchTable.hipMemcpy2DArrayToArray_fn. Only add new function pointers to end of struct and do not rearrange them
             offsetof(TABLE, ENTRY) == ::rocprofiler::common::abi::compute_table_offset(NUM),       \
                                    ^
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:519:1: note: in expansion of macro ‘ROCP_SDK_ENFORCE_ABI’
 ROCP_SDK_ENFORCE_ABI(::HipDispatchTable, hipMemcpy2DArrayToArray_fn, 451);
 ^~~~~~~~~~~~~~~~~~~~
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/common/abi.hpp:62:27: error: static assertion failed: size of the API table struct has changed. Update the STEP_VERSION number (or in rare cases, the MAJOR_VERSION number)
             sizeof(TABLE) == ::rocprofiler::common::abi::compute_table_offset(NUM),                \
             ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-source/source/lib/rocprofiler-sdk/hip/abi.cpp:560:1: note: in expansion of macro ‘ROCP_SDK_ENFORCE_ABI_VERSIONING’
 ROCP_SDK_ENFORCE_ABI_VERSIONING(::HipDispatchTable, 452)
 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
make[2]: *** [source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/build.make:482: source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/hip/abi.cpp.o] Error 1
make[2]: Leaving directory '/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-build'
make[1]: *** [CMakeFiles/Makefile2:4646: source/lib/rocprofiler-sdk/CMakeFiles/rocprofiler-sdk-object-library.dir/all] Error 2
make[1]: Leaving directory '/data/horse/ws/wwilliam-rocprofv3-build/rocprofiler-sdk-build'
make: *** [Makefile:166: all] Error 2
```
`/usr/bin/c++` is g++ 8.5, which seemed like a possible cause to me, so I tried with `amdclang` and `amdclang++`; that does change the style of the static assert error output but not the result--the same set of functions are reported as ABI breaks somehow.



### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (3)

### ppanchad-amd · 2025-05-09

Hi @wrwilliams. Internal ticket has been created to investigate this issue. Thanks!

### huanrwan-amd · 2025-07-07

@wrwilliams as seem in https://github.com/ROCm/rocprofiler-sdk/issues/51, can we close this one as well?
> > [@wrwilliams](https://github.com/wrwilliams) please try the latest amd-staging branch. This should have been fixed in [3580478](https://github.com/ROCm/rocprofiler-sdk/commit/3580478426c3da4319bbf793cabf6f3878540bfa)
> 
> Have gotten clean builds from source against 6.4.x, marking this one fixed.

### wrwilliams · 2025-07-08

> [@wrwilliams](https://github.com/wrwilliams) as seem in [#51](https://github.com/ROCm/rocprofiler-sdk/issues/51), can we close this one as well?
> 
> > > [@wrwilliams](https://github.com/wrwilliams) please try the latest amd-staging branch. This should have been fixed in [3580478](https://github.com/ROCm/rocprofiler-sdk/commit/3580478426c3da4319bbf793cabf6f3878540bfa)
> > 
> > 
> > Have gotten clean builds from source against 6.4.x, marking this one fixed.

Sure, I think it's a WONTFIX given that folks should not be staying on 6.3 in any event.
