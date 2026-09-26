# [Issue #1162] [Issue]:  no member named 'memoryType' in 'hipPointerAttribute_t'

source: https://github.com/ROCm/rccl/issues/1162
state: closed | updated: 2024-05-02T11:15:28Z
labels: 

## 正文

### Problem Description

Hello,

Im trying to compile the rccl-6.1.0 and I receive this error. I configure with this line:
cmake \
    -Wno-dev \
    -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc \
    -D CMAKE_INSTALL_PREFIX=/opt/rocm \
    -D BUILD_TESTS=OFF \
    -D HIP_CLANG_INCLUDE_PATH=/opt/rocm/llvm/include \



[ 48%] Building CXX object CMakeFiles/rccl.dir/hipify/src/graph/xml.cc.o
[ 48%] Building CXX object CMakeFiles/rccl.dir/hipify/src/group.cc.o
[ 49%] Building CXX object CMakeFiles/rccl.dir/hipify/src/init.cc.o
[ 49%] Building CXX object CMakeFiles/rccl.dir/hipify/src/misc/archinfo.cc.o
[ 49%] Building CXX object CMakeFiles/rccl.dir/hipify/src/misc/argcheck.cc.o
[183/453] Building CXX object CMakeFiles/rccl.dir/hipify/src/misc/argcheck.cc.o
FAILED: CMakeFiles/rccl.dir/hipify/src/misc/argcheck.cc.o 
/opt/rocm/bin/hipcc -DCOMPILE_MSCCL_KERNEL -DENABLE_COLLTRACE -DHIP_EVENT_DISABLE_FENCE -DHIP_UNCACHED_MEMORY -DNVTX_NO_IMPL -DUSE_INDIRECT_FUNCTION_CALL -DUSE_PROF_API=1 -DUSE_ROCM_SMI64CONFIG -D__HIP_PLATFORM_AMD__=1 -Drccl_EXPORTS -I/mnt/arhiv/rocm/rocm-build/build/rccl/include -I/mnt/arhiv/rocm/rocm-build/build/rccl/hipify/src -I/mnt/arhiv/rocm/rocm-build/build/rccl/hipify/src/include -I/mnt/arhiv/rocm/rocm-build/build/rccl/hipify/src/collectives -I/mnt/arhiv/rocm/rocm-build/build/rccl/hipify/src/collectives/device -O3 -DNDEBUG -std=c++14 -fPIC -parallel-jobs=12 -Wno-format-nonliteral -fgpu-rdc -fvisibility=hidden -mllvm --amdgpu-kernarg-preload-count=16 -x hip --offload-arch=gfx803 --offload-arch=gfx900:xnack- --offload-arch=gfx906:xnack- --offload-arch=gfx908:xnack- --offload-arch=gfx90a:xnack- --offload-arch=gfx90a:xnack+ --offload-arch=gfx940 --offload-arch=gfx941 --offload-arch=gfx942 --offload-arch=gfx1030 --offload-arch=gfx1100 --offload-arch=gfx1101 --offload-arch=gfx1102 -MD -MT CMakeFiles/rccl.dir/hipify/src/misc/argcheck.cc.o -MF CMakeFiles/rccl.dir/hipify/src/misc/argcheck.cc.o.d -o CMakeFiles/rccl.dir/hipify/src/misc/argcheck.cc.o -c /mnt/arhiv/rocm/rocm-build/build/rccl/hipify/src/misc/argcheck.cc
/mnt/arhiv/rocm/rocm-build/build/rccl/hipify/src/misc/argcheck.cc:18:12: error: no member named 'memoryType' in 'hipPointerAttribute_t'
   18 |   if (attr.memoryType == hipMemoryTypeDevice && attr.device != comm->cudaDev) {
      |       ~~~~ ^
1 error generated when compiling for gfx906.

gmake[2]: *** [CMakeFiles/rccl.dir/build.make:1092: CMakeFiles/rccl.dir/hipify/src/misc/argcheck.cc.o] Error 1
gmake[1]: *** [CMakeFiles/Makefile2:110: CMakeFiles/rccl.dir/all] Error 2
gmake: *** [Makefile:156: all] Error 2


### Operating System

Slackware 15.0

### CPU

AMD Ryzen 7 3800X 8-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.1.0

### ROCm Component

rccl

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_

## 评论 (1)

### RandUser123sa · 2024-05-02

Found the problem, the file /opt/rocm/.info/version contain bad version i.e. 60100-66 should be 6.1.0 according to CMakeLists.txt:141 regex 
