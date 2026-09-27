# [Issue #3208] Failed mlc build from source with CUTLASS enabled

source: https://github.com/mlc-ai/mlc-llm/issues/3208
state: closed | updated: 2026-03-02T14:52:38Z
labels: bug

## 正文

## 🐛 Bug

tried to build mlc from source, following the exact steps reported on the docs. I am working on an NVIDIA jetson agx orin 64gb. When i try to build mlc with cutlass enabled and a custom tvm path (also built from source) i get errors.

## To Reproduce

Steps to reproduce the behavior:

1. download tvm from source following docs
2. echo the following to cmake config
3. echo "set(CMAKE_BUILD_TYPE RelWithDebInfo)" >> config.cmake
```
echo "set(USE_LLVM \"llvm-config --ignore-libllvm --link-static\")" >> config.cmake
echo "set(HIDE_PRIVATE_SYMBOLS ON)" >> config.cmake
echo 'set(CMAKE_C_COMPILER_LAUNCHER ccache)' >> config.cmake
echo 'set(CMAKE_CXX_COMPILER_LAUNCHER ccache)' >> config.cmake
echo "set(USE_CUDA ON)" >> config.cmake on 
echo "set(USE_METAL OFF)" >> config.cmake
echo "set(USE_VULKAN OFF)" >> config.cmake
echo "set(USE_OPENCL OFF)" >> config.cmake
echo "set(USE_CUBLAS ON)" >> config.cmake on
echo "set(USE_CUDNN ON)" >> config.cmake on 
echo "set(USE_CUTLASS ON)" >> config.cmake on 
set(USE_FLASHINFER OFF)
```

3. build tvm:   cmake .. && cmake --build . --parallel $(nproc)

ization_and_destruction_0(int, int)’:
/home/truffle/abd_work/tvm/src/target/tag.cc:462:1: note: variable tracking size limit exceeded with ‘-fvar-tracking-assignments’, retrying without
  462 | }  // namespace tvm
      | ^
[ 98%] Building CXX object CMakeFiles/tvm_objs.dir/src/relax/backend/contrib/cutlass/codegen.cc.o
[ 98%] Linking CUDA shared library libflash_attn.so
[ 98%] Built target flash_attn
[ 98%] Built target tvm_objs
gmake[1]: *** [CMakeFiles/Makefile2:557: 3rdparty/cutlass_fpA_intB_gemm/cutlass_kernels/CMakeFiles/fpA_intB_gemm.dir/all] Error 2
gmake: *** [Makefile:136: all] Error 2

this is the error i get ^
it works with cutlass off



## Environment

 - Platform (CUDA):
 - Operating system (eUbuntu):
 - Device (Jetsonn AGX ORIN)
 - How you installed MLC-LLM ( source):
 - How you installed TVM-Unity (source):
 - Python version (e.g. 3.10): Python 3.11.12
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable): 12.6
 - TVM Unity Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`,
```yaml
 applicable if you compile models):
in applicable since the build wasnt successfull
but this is what i get when i try with CUTLASS OFF
USE_NVTX: OFF
USE_GTEST: AUTO
SUMMARIZE: OFF
TVM_DEBUG_WITH_ABI_CHANGE: OFF
USE_IOS_RPC: OFF
USE_MSC: OFF
CUDA_VERSION: 12.6
USE_LIBBACKTRACE: AUTO
DLPACK_PATH: 3rdparty/dlpack/include
USE_TENSORRT_CODEGEN: OFF
USE_OPENCL_EXTN_QCOM: NOT-FOUND
USE_THRUST: OFF
BUILD_DUMMY_LIBTVM: OFF
USE_CUDNN: ON
USE_TENSORRT_RUNTIME: OFF
USE_ARM_COMPUTE_LIB_GRAPH_EXECUTOR: OFF
USE_CCACHE: AUTO
USE_ARM_COMPUTE_LIB: OFF
USE_CPP_RTVM: OFF
USE_OPENCL_GTEST: /path/to/opencl/gtest
TVM_LOG_BEFORE_THROW: OFF
USE_MKL: OFF
MLIR_VERSION: NOT-FOUND
USE_CLML: OFF
USE_STACKVM_RUNTIME: OFF
ROCM_PATH: /opt/rocm
USE_DNNL: OFF
USE_MSCCL: OFF
USE_NNAPI_RUNTIME: OFF
USE_MLIR: OFF
USE_RCCL: OFF
USE_LLVM: llvm-config --ignore-libllvm --link-static
USE_THREADS: ON
USE_MSVC_MT: OFF
BACKTRACE_ON_SEGFAULT: OFF
USE_ROCBLAS: OFF
USE_NCCL: OFF
GIT_COMMIT_HASH: 6bd55f0c90c74d667afe9b2aba887a33a90ae84d
USE_VULKAN: OFF
USE_RUST_EXT: OFF
USE_CUTLASS: OFF
USE_CPP_RPC: OFF
USE_HEXAGON: OFF
USE_CUSTOM_LOGGING: OFF
USE_UMA: OFF
USE_FALLBACK_STL_MAP: OFF
USE_SORT: ON
USE_RTTI: ON
```
GIT_COMMIT_TIME: 2025-04-14 18:52:30 +0900
```yaml
USE_HIPBLAS: OFF
USE_HEXAGON_SDK: /path/to/sdk
USE_BLAS: none
USE_LIBTORCH: OFF
USE_RANDOM: ON
USE_CUDA: ON
USE_COREML: OFF
USE_AMX: OFF
BUILD_STATIC_RUNTIME: OFF
USE_KHRONOS_SPIRV: OFF
USE_CLML_GRAPH_EXECUTOR: OFF
USE_TFLITE: OFF
USE_HEXAGON_GTEST: /path/to/hexagon/gtest
PICOJSON_PATH: 3rdparty/picojson
USE_OPENCL_ENABLE_HOST_PTR: OFF
INSTALL_DEV: OFF
USE_NNPACK: OFF
LLVM_VERSION: 20.1.2
USE_MRVL: OFF
USE_OPENCL: OFF
COMPILER_RT_PATH: 3rdparty/compiler-rt
USE_NNAPI_CODEGEN: OFF
RANG_PATH: 3rdparty/rang/include
USE_SPIRV_KHR_INTEGER_DOT_PRODUCT: OFF
USE_OPENMP: none
USE_BNNS: OFF
USE_FLASHINFER: OFF
USE_CUBLAS: ON
USE_METAL: OFF
USE_HEXAGON_EXTERNAL_LIBS: OFF
USE_ALTERNATIVE_LINKER: AUTO
USE_BYODT_POSIT: OFF
USE_NVSHMEM: OFF
USE_HEXAGON_RPC: OFF
DMLC_PATH: 3rdparty/dmlc-core/include
INDEX_DEFAULT_I64: ON
USE_RPC: ON
USE_TENSORFLOW_PATH: none
TVM_CLML_VERSION: 
USE_MIOPEN: OFF
USE_ROCM: OFF
USE_PAPI: OFF
USE_CURAND: OFF
TVM_CXX_COMPILER_PATH: /usr/bin/c++
HIDE_PRIVATE_SYMBOLS: ON
```
 - Any other relevant information:

## Additional context

<!-- Add any other context about the problem here. -->


## 评论 (1)

### johnnynunez · 2025-04-25

also with flashinfer
tvm(relax) is old...
