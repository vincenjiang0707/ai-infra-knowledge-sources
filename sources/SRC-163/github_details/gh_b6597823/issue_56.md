# [Issue #56] When using the cmake - B build command, the following message appears in a continuous loop

source: https://github.com/LLMServe/DistServe/issues/56
state: open | updated: 2025-02-09T10:06:55Z
labels: 

## 正文

-- The CXX compiler identification is GNU 12.3.0
-- The CUDA compiler identification is NVIDIA 12.0.140
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting CUDA compiler ABI info
-- Detecting CUDA compiler ABI info - done
-- Check for working CUDA compiler: /usr/bin/nvcc - skipped
-- Detecting CUDA compile features
-- Detecting CUDA compile features - done
-- Found CUDAToolkit: /usr/include (found suitable version "12.0.140", minimum required is "11.4")
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
-- Looking for NCCL_VERSION_CODE - found
-- NCCL version: 2.18.3

-- Found NCCL (include: /usr/include, library: /usr/lib/x86_64-linux-gnu/libnccl.so)
-- Found MPI_CXX: /usr/lib/x86_64-linux-gnu/openmpi/lib/libmpi_cxx.so (found version "3.1")
-- Found MPI: TRUE (found version "3.1")
-- Found CUDA: /home/lq/anaconda3/envs/distserve (found version "12.1")
-- Found CUDAToolkit: /usr/include (found version "12.0.140")
-- Caffe2: CUDA detected: 12.0
-- Caffe2: CUDA nvcc is: /home/lq/anaconda3/envs/distserve/bin/nvcc
-- Caffe2: CUDA toolkit directory: /home/lq/anaconda3/envs/distserve
-- Caffe2: Header version is: 12.1
-- /usr/lib/x86_64-linux-gnu/stubs/libnvrtc.so shorthash is 68d1f4ba
-- Found CUDNN: /home/lq/anaconda3/envs/distserve/lib/libcudnn.so
-- USE_CUSPARSELT is set to 0. Compiling without cuSPARSELt support
-- Autodetected CUDA architecture(s):  7.0 7.0 7.0 7.0 7.0 7.0 7.0 7.0
-- Added CUDA NVCC flags for: -gencode;arch=compute_70,code=sm_70
CMake Warning at /home/lq/anaconda3/envs/distserve/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message):
  static library kineto_LIBRARY-NOTFOUND not found.
Call Stack (most recent call first):
  /home/lq/anaconda3/envs/distserve/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:127 (append_torchlib_if_found)
  CMakeLists.txt:100 (find_package)


-- Found Torch: /home/lq/anaconda3/envs/distserve/lib/python3.10/site-packages/torch/lib/libtorch.so
-- USE_CXX11_ABI=False
-- The C compiler identification is GNU 12.3.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found Python: /home/lq/anaconda3/envs/distserve/bin/python3 (found version "3.10.14") found components: Interpreter
CMake Warning (dev) at /usr/share/cmake-3.28/Modules/FetchContent.cmake:1331 (message):
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


-- Using the multi-header code from /home/lq/DistServe/SwiftTransformer/build/_deps/json-src/include/
-- Configuring done (14.1s)
You have changed variables that require your cache to be deleted.
Configure will be re-run and you may have to reset some variables.
The following variables have changed:
CMAKE_CUDA_COMPILER= /usr/bin/nvcc


The program's continuous loop never ends, but it also does not report any errors

## 评论 (5)

### interestingLSY · 2025-02-07

Can you try to remove [these two lines](https://github.com/LLMServe/SwiftTransformer/commit/8b194e5622a6b48c1539586d4f8e32e6204ab150), `rm -r build`, and then execute `cmake -B build` again?



### 67lc · 2025-02-08

Thanks for your answer, I have solved the problem.

### 67lc · 2025-02-09

Hello,I have 4 V100 GPU on my node with NVlink.When tensor_parrllel_size=1,it is right.Now,I change the offiline.py like  follow.
`disagg_parallel_config=DisaggParallelConfig(
        context=ParallelConfig(
            tensor_parallel_size=2,
            pipeline_parallel_size=1
        ),
        decoding=ParallelConfig(
            tensor_parallel_size=2,
            pipeline_parallel_size=1
        )
    ),
`
there is my error:
(ParaWorker pid=1272483) Node03:1272483:1272483 [0] misc/strongstream.cc:60 NCCL WARN Cuda failure 'CUDA driver is a stub library'
(ParaWorker pid=1272483) [ERROR] NCCL error /home/lq/DistServe/SwiftTransformer/src/csrc/util/nccl_utils.cc:59 'ncclAllReduce(sendbuff, recvbuff, count, datatype, op, comm, stream)' : unhandled cuda error (run with NCCL_DEBUG=INFO for details)
(ParaWorker pid=1272491)
(raylet) A worker died or was killed while executing a task by an unexpected system error. To troubleshoot the problem, check the logs for the dead worker. RayTask ID: ffffffffffffffffd2509eb2880ca536eb1c342a07000000 Worker ID: 5308d46bf02d72c478c15c99c5681e50983213728e7cfc1edab73b1b Node ID: b60482efafa3d4a9528ff576e2897821501a6a4b4569e570b892dc72 Worker IP address: 10.0.0.103 Worker port: 10029 Worker PID: 1272491 Worker exit type: SYSTEM_ERROR Worker exit detail: Worker unexpectedly exits with a connection error code 2. End of file. There are some potential root causes. (1) The process is killed by SIGKILL by OOM killer due to high memory usage. (2) ray stop --force is called. (3) The worker is crashed unexpectedly due to SIGSEGV or other unexpected errors.
INFO 17:23:56 (context) 1 waiting, 0 finished but unaccepted, 4 blocks occupied by on-the-fly requests`
How can i do for it?

### interestingLSY · 2025-02-09

I think the `NCCL WARN Cuda failure 'CUDA driver is a stub library'` is really suspecious, which may indicate that your environment has some problem. I'm not really sure what the problem is, and you may try to Google yourself?

### 67lc · 2025-02-09

OK,thank you.
