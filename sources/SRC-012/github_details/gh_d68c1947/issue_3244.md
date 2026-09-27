# [Issue #3244] [Bug]  ios Cannot find system lib with llama_q4f16_1_d44304359a2802d16aa168086928bcad

source: https://github.com/mlc-ai/mlc-llm/issues/3244
state: closed | updated: 2026-03-02T14:51:14Z
labels: bug

## 正文

## 🐛 Bug

```
libc++abi: terminating due to uncaught exception of type tvm::runtime::InternalError: Traceback (most recent call last):
  File "/Users/chenqg/myfiles/myprojects/ios/mlc-llm/cpp/serve/function_table.cc", line 114, in 
InternalError: Check failed: (fload_exec.defined()) is false: Cannot find system lib with llama_q4f16_1_d44304359a2802d16aa168086928bcad, please make sure you set model_lib field consistently with the compilation 
```

## To Reproduce

Steps to reproduce the behavior:

1.Run the ios APP once the build is successful, The code used for the build is the latest commit of the clone

<img width="514" alt="Image" src="https://github.com/user-attachments/assets/4cb3470d-c5ac-4134-aa23-5d8b393eaba5" />

2.Click to open the chat window for the corresponding model


## Expected behavior

The dialog window should open successfully

## Environment

 - Platform (e.g. WebGPU/Vulkan/IOS/Android/CUDA): IOS
 - Operating system (e.g. Ubuntu/Windows/MacOS/...): MacOS Version 15.5  XCode Version 16.1
 - Device (e.g. iPhone 12 Pro, PC+RTX 3090, ...) Mac （ Designed For ipad）
 - How you installed MLC-LLM (`conda`, source): conda
 - How you installed TVM-Unity (`pip`, source):
 - Python version (e.g. 3.10): 3.11
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable):
 - TVM Unity Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
 ```
python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"
BUILD_STATIC_RUNTIME: OFF
BUILD_DUMMY_LIBTVM: OFF
COMPILER_RT_PATH: 3rdparty/compiler-rt
CUDA_VERSION: NOT-FOUND
DLPACK_PATH: 3rdparty/dlpack/include
DMLC_PATH: 3rdparty/dmlc-core/include
GIT_COMMIT_HASH: 58405c27d8a92f5ceb01d8de02b6c72e78075a72
GIT_COMMIT_TIME: 2025-06-02 20:49:17 -0400
HIDE_PRIVATE_SYMBOLS: ON
INDEX_DEFAULT_I64: ON
INSTALL_DEV: OFF
LLVM_VERSION: 15.0.7
MLIR_VERSION: NOT-FOUND
PICOJSON_PATH: 3rdparty/picojson
RANG_PATH: 3rdparty/rang/include
ROCM_PATH: /opt/rocm
SUMMARIZE: OFF
TVM_CXX_COMPILER_PATH: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++
USE_ALTERNATIVE_LINKER: AUTO
USE_ARM_COMPUTE_LIB_GRAPH_EXECUTOR: OFF
USE_ARM_COMPUTE_LIB: OFF
USE_BLAS: none
USE_BNNS: OFF
USE_BYODT_POSIT: OFF
USE_COREML: OFF
USE_CPP_RPC: OFF
USE_CPP_RTVM: 
USE_CUBLAS: OFF
USE_CUDA: OFF
USE_NVTX: OFF
USE_NCCL: OFF
USE_MSCCL: OFF
USE_CUDNN: OFF
USE_CUSTOM_LOGGING: OFF
USE_CUTLASS: OFF
USE_FLASHINFER: 
USE_AMX: OFF
USE_DNNL: OFF
USE_FALLBACK_STL_MAP: OFF
USE_GTEST: AUTO
USE_HEXAGON: OFF
USE_HEXAGON_RPC: OFF
USE_HEXAGON_SDK: /path/to/sdk
USE_HEXAGON_GTEST: /path/to/hexagon/gtest
USE_HEXAGON_EXTERNAL_LIBS: OFF
USE_IOS_RPC: OFF
USE_KHRONOS_SPIRV: OFF
USE_LIBBACKTRACE: AUTO
USE_LIBTORCH: OFF
USE_LLVM: llvm-config --link-static
USE_MLIR: OFF
USE_METAL: ON
USE_MIOPEN: OFF
USE_MKL: OFF
USE_MRVL: OFF
USE_MSVC_MT: OFF
USE_NNPACK: OFF
USE_OPENCL: OFF
USE_OPENCL_ENABLE_HOST_PTR: OFF
USE_OPENCL_EXTN_QCOM: NOT-FOUND
USE_OPENCL_GTEST: /path/to/opencl/gtest
USE_OPENMP: OFF
USE_PAPI: OFF
USE_RANDOM: ON
TVM_DEBUG_WITH_ABI_CHANGE: OFF
TVM_LOG_BEFORE_THROW: OFF
USE_ROCBLAS: OFF
USE_HIPBLAS: OFF
USE_ROCM: OFF
USE_RCCL: OFF
USE_RPC: ON
USE_RTTI: ON
USE_RUST_EXT: OFF
USE_SORT: ON
USE_SPIRV_KHR_INTEGER_DOT_PRODUCT: OFF
USE_STACKVM_RUNTIME: OFF
USE_TENSORFLOW_PATH: none
USE_TENSORRT_CODEGEN: OFF
USE_TENSORRT_RUNTIME: OFF
USE_TFLITE: OFF
USE_THREADS: ON
USE_THRUST: OFF
USE_CURAND: OFF
USE_VULKAN: OFF
USE_CLML: OFF
TVM_CLML_VERSION: 
USE_CLML_GRAPH_EXECUTOR: OFF
USE_UMA: OFF
USE_MSC: OFF
USE_CCACHE: AUTO
USE_NVSHMEM: OFF
USE_NNAPI_CODEGEN: OFF
USE_NNAPI_RUNTIME: OFF
BACKTRACE_ON_SEGFAULT: OFF

```
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (3)

### grabbou · 2025-09-10

Have you found solution to this?

### grytrn · 2025-09-27

I also have this problem.

### grabbou · 2025-09-30

FWIW I fixed this issue by aligning the MLC library precompiled with source repository (make sure to check out right version)
