# [Issue #3435] [Bug] iOS MLCChat is not working properly. ERR: Undefined symbol: _TVMFFIXXX

source: https://github.com/mlc-ai/mlc-llm/issues/3435
state: closed | updated: 2026-03-02T07:35:48Z
labels: bug

## 正文

## 🐛 Bug
Running the MLCChat project resulted in the following errors:

Undefined symbol: _TVMFFIEnvModRegisterSystemLibSymbol

Undefined symbol: _TVMFFIErrorSetRaisedFromCStr

Undefined symbol: _TVMFFIFunctionCall

Linker command failed with exit code 1 (use -v to see invocation)

<img width="764" height="400" alt="Image" src="https://github.com/user-attachments/assets/a76099de-f63f-4ac6-a32b-00a1d213cc6a" />

## To Reproduce

Steps to reproduce the behavior:

1. mlc-llm (v0.19.0 and main)
2. python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu
3. MLC_JIT_POLICY=REDO mlc_llm package
4. open MLCChat.xcodeproj

XCode Error: 
```shell
Undefined symbol: _TVMFFIEnvModRegisterSystemLibSymbol

Undefined symbol: _TVMFFIErrorSetRaisedFromCStr

Undefined symbol: _TVMFFIFunctionCall

Linker command failed with exit code 1 (use -v to see invocation)

```

pip list:
> conda "llvmdev>=15" "cmake=3.26.4" git python=3.11
```shell
mlc-ai-nightly-cpu  0.20.dev748
mlc-llm-nightly-cpu 0.20.dev126
```



## Expected behavior

<!-- A clear and concise description of what you expected to happen. -->

## Environment

 - Platform IOS: 26.3
 - Operating system MacOS: Apple M4 Pro 26.1 (25B78)
 - Device iPhone 17 Pro
 - How you installed MLC-LLM (`conda`, source): conda
 - How you installed TVM (`pip`, source): pip
 - Python version (e.g. 3.10): 3.11
 - GPU driver version (if applicable):
 - CUDA/cuDNN version (if applicable):
 - TVM Hash Tag (`python -c "import tvm; print('\n'.join(f'{k}: {v}' for k, v in tvm.support.libinfo().items()))"`, applicable if you compile models):
```shell
BUILD_STATIC_RUNTIME: OFF
BUILD_DUMMY_LIBTVM: OFF
COMPILER_RT_PATH: 3rdparty/compiler-rt
CUDA_VERSION: NOT-FOUND
DMLC_PATH: 3rdparty/dmlc-core/include
GIT_COMMIT_HASH: b3d4fe9fa8860804ee166549ad1898276273eb93
GIT_COMMIT_TIME: 2026-02-09 12:27:03 -0500
HIDE_PRIVATE_SYMBOLS: ON
INDEX_DEFAULT_I64: ON
INSTALL_DEV: OFF
LLVM_VERSION: 19.1.7
MLIR_VERSION: NOT-FOUND
PICOJSON_PATH: 3rdparty/picojson
RANG_PATH: 3rdparty/rang/include
ROCM_PATH: /opt/rocm
SUMMARIZE: OFF
TVM_CXX_COMPILER_PATH: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/clang++
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
TVM_BUILD_PYTHON_MODULE: ON
USE_RTTI: ON
USE_RUST_EXT: OFF
USE_SORT: ON
USE_SPIRV_KHR_INTEGER_DOT_PRODUCT: OFF
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

### MasterJH5574 · 2026-03-01

Thank you @hocgin for reporting.  We are going through some refactors right now. I'll verify the iOS and Android build flow when the refactor is done, and report back.

### MasterJH5574 · 2026-03-01

Hi @hocgin, the refactor is completed.  Could you please

* checkout the latest main branch
* rerun `python -m pip install --pre -U -f https://mlc.ai/wheels mlc-llm-nightly-cpu mlc-ai-nightly-cpu`
* also make sure you upgrade tvm-ffi to the latest: `python -m pip install apache-tvm-ffi --upgrade`

and try build in Xcode again?

Please let us know if the issue persists.

### hocgin · 2026-03-02

@MasterJH5574 Hi, thanks for the guidance!

I followed your steps — checked out the latest main, reinstalled the nightly packages, and upgraded apache-tvm-ffi. After rebuilding in Xcode, the issue is now resolved.

Really appreciate your help and the quick refactor 🙏
