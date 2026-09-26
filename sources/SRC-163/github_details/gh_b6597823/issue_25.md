# [Issue #25] Swift transformers cmak build 一直循序

source: https://github.com/LLMServe/DistServe/issues/25
state: closed | updated: 2025-03-09T17:52:04Z
labels: 

## 正文

-- Found Torch: /opt/conda/lib/python3.10/site-packages/torch/lib/libtorch.so
-- USE_CXX11_ABI=False
-- The C compiler identification is GNU 11.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found Python: /opt/conda/bin/python3.10 (found version "3.10.14") found components: Interpreter
CMake Warning (dev) at /opt/conda/lib/python3.10/site-packages/cmake/data/share/cmake-3.29/Modules/FetchContent.cmake:1352 (message):
  The DOWNLOAD_EXTRACT_TIMESTAMP option was not given and policy CMP0135 is
  not set.  The policy's OLD behavior will be used.  When using a URL
  download, the timestamps of extracted files should preferably be that of
  the time of extraction, otherwise code that depends on the extracted
  contents might not be rebuilt if the URL changes.  The OLD behavior
  preserves the timestamps from the archive instead, but this is usually not
  what you want.  Update your project to the NEW behavior or specify the
  DOWNLOAD_EXTRACT_TIMESTAMP option with a value of true to avoid this
  robustness issue.
Call Stack (most recent call first):
  CMakeLists.txt:139 (FetchContent_Declare)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Deprecation Warning at build/_deps/json-src/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Using the multi-header code from /data/lc/DistServe/SwiftTransformer/build/_deps/json-src/include/
-- Configuring done (9.9s)
You have changed variables that require your cache to be deleted.
Configure will be re-run and you may have to reset some variables.
The following variables have changed:
CMAKE_CUDA_COMPILER= /etc/alternatives/cuda/bin/nvcc

-- The CXX compiler identification is GNU 11.4.0
-- The CUDA compiler identification is NVIDIA 12.1.105
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting CUDA compiler ABI info
-- Detecting CUDA compiler ABI info - done
-- Check for working CUDA compiler: /etc/alternatives/cuda/bin/nvcc - skipped
-- Detecting CUDA compile features
-- Detecting CUDA compile features - done
-- Found CUDAToolkit: /etc/alternatives/cuda/targets/x86_64-linux/include (found suitable version "12.1.105", minimum required is "11.4")
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
No build type selected, defaulting to RELEASE mode
Use -DBUILD_MODE=DEBUG or -DBUILD_MODE=RELEASE to specify build type
Building in release mode
Building with MPI and NCCL
-- Found NCCL: /usr/include
-- Determining NCCL version from /usr/include/nccl.h...
-- Looking for NCCL_VERSION_CODE
-- Looking for NCCL_VERSION_CODE - not found
-- Found NCCL (include: /usr/include, library: /usr/lib/x86_64-linux-gnu/libnccl.so)
-- Found MPI_CXX: /user/local/openmpi/lib/libmpi.so (found version "3.1")
-- Found MPI: TRUE (found version "3.1")
-- Found CUDA: /usr/local/cuda (found version "12.1")
-- Found CUDAToolkit: /etc/alternatives/cuda/include (found version "12.1.105")
-- Caffe2: CUDA detected: 12.1
-- Caffe2: CUDA nvcc is: /usr/local/cuda/bin/nvcc
-- Caffe2: CUDA toolkit directory: /usr/local/cuda
-- Caffe2: Header version is: 12.1
-- /usr/local/cuda-12.1/targets/x86_64-linux/lib/libnvrtc.so shorthash is b51b459d
-- Found CUDNN: /usr/lib/x86_64-linux-gnu/libcudnn.so
-- USE_CUSPARSELT is set to 0. Compiling without cuSPARSELt support
-- Autodetected CUDA architecture(s):  8.0 8.0 8.0 8.0 8.0 8.0 8.0 8.0
-- Added CUDA NVCC flags for: -gencode;arch=compute_80,code=sm_80
CMake Warning at /opt/conda/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message):
  static library kineto_LIBRARY-NOTFOUND not found.
Call Stack (most recent call first):
  /opt/conda/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:127 (append_torchlib_if_found)
  CMakeLists.txt:100 (find_package)


-- Found Torch: /opt/conda/lib/python3.10/site-packages/torch/lib/libtorch.so
-- USE_CXX11_ABI=False
-- The C compiler identification is GNU 11.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found Python: /opt/conda/bin/python3.10 (found version "3.10.14") found components: Interpreter
CMake Warning (dev) at /opt/conda/lib/python3.10/site-packages/cmake/data/share/cmake-3.29/Modules/FetchContent.cmake:1352 (message):
  The DOWNLOAD_EXTRACT_TIMESTAMP option was not given and policy CMP0135 is
  not set.  The policy's OLD behavior will be used.  When using a URL
  download, the timestamps of extracted files should preferably be that of
  the time of extraction, otherwise code that depends on the extracted
  contents might not be rebuilt if the URL changes.  The OLD behavior
  preserves the timestamps from the archive instead, but this is usually not
  what you want.  Update your project to the NEW behavior or specify the
  DOWNLOAD_EXTRACT_TIMESTAMP option with a value of true to avoid this
  robustness issue.
Call Stack (most recent call first):
  CMakeLists.txt:139 (FetchContent_Declare)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Deprecation Warning at build/_deps/json-src/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Using the multi-header code from /data/lc/DistServe/SwiftTransformer/build/_deps/json-src/include/
-- Configuring done (10.0s)
You have changed variables that require your cache to be deleted.
Configure will be re-run and you may have to reset some variables.
The following variables have changed:
CMAKE_CUDA_COMPILER= /etc/alternatives/cuda/bin/nvcc

-- The CXX compiler identification is GNU 11.4.0
-- The CUDA compiler identification is NVIDIA 12.1.105
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting CUDA compiler ABI info
-- Detecting CUDA compiler ABI info - done
-- Check for working CUDA compiler: /etc/alternatives/cuda/bin/nvcc - skipped
-- Detecting CUDA compile features
-- Detecting CUDA compile features - done
-- Found CUDAToolkit: /etc/alternatives/cuda/targets/x86_64-linux/include (found suitable version "12.1.105", minimum required is "11.4")
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
No build type selected, defaulting to RELEASE mode
Use -DBUILD_MODE=DEBUG or -DBUILD_MODE=RELEASE to specify build type
Building in release mode
Building with MPI and NCCL
-- Found NCCL: /usr/include
-- Determining NCCL version from /usr/include/nccl.h...
-- Looking for NCCL_VERSION_CODE
-- Looking for NCCL_VERSION_CODE - not found
-- Found NCCL (include: /usr/include, library: /usr/lib/x86_64-linux-gnu/libnccl.so)
-- Found MPI_CXX: /user/local/openmpi/lib/libmpi.so (found version "3.1")
-- Found MPI: TRUE (found version "3.1")


## 评论 (3)

### lcvcl · 2024-07-16

一直重复显示上述信息，停不下来

### lcvcl · 2024-07-16

该问题是因为CMAKE_CUDA_COMPILER= /etc/alternatives/cuda/bin/nvcc
参数由软链接变成了真正的地址，所以会导致一直重新build

### LordEdison · 2025-03-09

请问后来怎么解决的呀？谢谢！
