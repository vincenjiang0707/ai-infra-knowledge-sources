# [Issue #250] Is CUDA 11 required for compilation and installation? I am using CUDA 12.8.

source: https://github.com/NVIDIA/DCGM/issues/250
state: open | updated: 2025-08-20T05:21:34Z
labels: 

## 正文

-- Found Boost: /usr/lib/x86_64-linux-gnu/cmake/Boost-1.74.0/BoostConfig.cmake (found version "1.74.0") found components: filesystem stacktrace_basic system 
CUDA11_INCLUDE_DIR-NOTFOUND
libcublas11-NOTFOUND
libcudart11-NOTFOUND
libculibos11-NOTFOUND
libcublaslt11-NOTFOUND
libcuda11-NOTFOUND
CMake Error at cmake/FindCuda.cmake:82 (message):
  Could NOT find Cuda 11
Call Stack (most recent call first):
  cmake/FindCuda.cmake:98 (load_cuda)
  CMakeLists.txt:37 (find_package)

## 评论 (1)

### nikkon-dev · 2025-08-20

We only support building in the dcgmbuild container environment that has all required components, including CUDA 11/12.
