# [Issue #3111] [Bug] Compiling the MLC from source is failed (cuda_fp8.h)

source: https://github.com/mlc-ai/mlc-llm/issues/3111
state: closed | updated: 2026-03-01T20:43:32Z
labels: bug

## 正文

## 🐛 Bug

I execute the following scripts (from [https://llm.mlc.ai/docs/install/mlc_llm.html#option-2-build-from-source]()) to build the MLC-llm from the source code, but it fails.

## To Reproduce
```
# clone from GitHub
git clone --recursive https://github.com/mlc-ai/mlc-llm.git && cd mlc-llm/
# create build directory
mkdir -p build && cd build
# generate build configuration
python ../cmake/gen_cmake_config.py
# build mlc_llm libraries
cmake .. && cmake --build . --parallel $(nproc) && cd ..
```

<!-- If you have a code sample, error messages, stack traces, please provide it here as well -->
## Error:
```
./mlc-llm/3rdparty/tvm/3rdparty/flashinfer/src/generated/batch_paged_decode_head_128_logitshook_0_posenc_1_dtypeq_f16_dtypekv_f16_dtypeout_f16_idtype_i32.cu:1:
./mlc-llm/3rdparty/tvm/3rdparty/flashinfer/include/flashinfer/attention/../vec_dtypes.cuh:21:10: fatal error: cuda_fp8.h: No such file or directory
   21 | #include <cuda_fp8.h>
      |          ^~~~~~~~~~~~
compilation terminated.
gmake[2]: *** [tvm/3rdparty/flashinfer/CMakeFiles/decode_kernels.dir/build.make:181: tvm/3rdparty/flashinfer/CMakeFiles/decode_kernels.dir/src/generated/batch_paged_decode_head_128_logitshook_0_posenc_1_dtypeq_f16_dtypekv_f16_dtypeout_f16_idtype_i32.cu.o] Error 1
gmake[2]: *** Waiting for unfinished jobs....

./mlc-llm/3rdparty/tvm/3rdparty/flashinfer/src/generated/single_decode_head_128_logitshook_1_posenc_1_dtypeq_f16_dtypekv_f16_dtypeout_f16.cu:1:
/home/wwt/mlc-llm/3rdparty/tvm/3rdparty/flashinfer/include/flashinfer/attention/../vec_dtypes.cuh:21:10: fatal error: cuda_fp8.h: No such file or directory
   21 | #include <cuda_fp8.h>
      |          ^~~~~~~~~~~~
compilation terminated.
```

## Expected behavior
<!-- A clear and concise description of what you expected to happen. -->
I hope to receive help from kind-hearted people.

## Environment
 - Platform (e.g. CUDA):
 - Operating system (e.g. Ubuntu):
 - How you installed MLC-LLM (`conda`, source):
 - Python version (3.11):
 - GPU driver version (565.57.01):
 - CUDA version (cuda_11.5.r11.5):


## 评论 (4)

### MasterJH5574 · 2025-01-28

Hi @wwt02 thank you for asking. May I ask for the content of `build/config.cmake`? Also, I noted that you're using CUDA 11.5, which is no longer supported by MLC. We suggest you upgrade your CUDA version to > 12.

### wwt02 · 2025-02-04

Hello, the following image shows the content of the build/config.cmake file on my machine.

![Image](https://github.com/user-attachments/assets/09d6aa07-56fa-4731-897f-8a2e0fb138e7)



### MasterJH5574 · 2025-02-11

Hi @wwt02 thank you. Indeed we will need CUDA version at least 12.

### wwt02 · 2025-02-20

Okay, thank you.
