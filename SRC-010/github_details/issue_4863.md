# [Issue #4863] [Bug] turbomind can not support fp8 in SM75

source: https://github.com/InternLM/lmdeploy/issues/4863
state: closed | updated: 2026-08-20T02:55:37Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

use lmdeploy to run qwen3.6-35b-a3b-fp8 failed

### Reproduction

lmdeploy serve api_server /root/hf_model/Qwen/Qwen3.6-35B-A3B-FP8 --model-format fp8 --model-name Qwen/Qwen3.6-35B-A3B-FP8 --backend turbomind --server-port 8000 --reasoning-parser default --tool-call-parser qwen3coder --enable-prefix-caching --eager-mode --rope-scaling-factor 0.4 --session-len 512000 --log-level REQUEST --max-batch-size 8 --tp 4 --cache-max-entry-count 0.75 --quant-policy 8

### Environment

```Shell
sys.platform: linux
Python: 3.12.13 (main, Mar  4 2026, 09:23:07) [GCC 11.4.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0,1,2,3: NVIDIA GeForce RTX 2080 Ti
CUDA_HOME: /usr/local/cuda
NVCC: Cuda compilation tools, release 12.8, V12.8.93
GCC: x86_64-linux-gnu-gcc (Ubuntu 11.4.0-1ubuntu1~22.04.3) 11.4.0
PyTorch: 2.10.0+cu128
PyTorch compiling details: PyTorch built with:
  - GCC 13.3
  - C++ Version: 201703
  - Intel(R) oneAPI Math Kernel Library Version 2024.2-Product Build 20240605 for Intel(R) 64 architecture applications
  - Intel(R) MKL-DNN v3.7.1 (Git Hash 8d263e693366ef8db40acc569cc7d8edf644556d)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - LAPACK is enabled (usually provided by MKL)
  - NNPACK is enabled
  - CPU capability usage: AVX512
  - CUDA Runtime 12.8
  - NVCC architecture flags: -gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80;-gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_90,code=sm_90;-gencode;arch=compute_100,code=sm_100;-gencode;arch=compute_120,code=sm_120
  - CuDNN 91.0.2  (built against CUDA 12.9)
  - Magma 2.6.1
  - Build settings: BLAS_INFO=mkl, BUILD_TYPE=Release, COMMIT_SHA=449b1768410104d3ed79d3bcfe4ba1d65c7f22c0, CUDA_VERSION=12.8, CUDNN_VERSION=9.10.2, CXX_COMPILER=/opt/rh/gcc-toolset-13/root/usr/bin/c++, CXX_FLAGS= -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOROCTRACER -DLIBKINETO_NOXPUPTI=ON -DUSE_FBGEMM -DUSE_FBGEMM_GENAI -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -DC10_NODEPRECATED -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=range-loop-construct -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-unknown-pragmas -Wno-unused-parameter -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=old-style-cast -faligned-new -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-dangling-reference -Wno-error=dangling-reference -Wno-stringop-overflow, LAPACK_INFO=mkl, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, TORCH_VERSION=2.10.0, USE_CUDA=ON, USE_CUDNN=ON, USE_CUSPARSELT=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_GLOO=ON, USE_MKL=ON, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=1, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF, USE_XCCL=OFF, USE_XPU=OFF, 

TorchVision: 0.25.0+cu128
LMDeploy: 0.15.0+
transformers: 5.14.1
fastapi: 0.141.1
pydantic: 2.13.4
triton: 3.6.0
NVIDIA Topology: 
	GPU0	GPU1	GPU2	GPU3	CPU Affinity	NUMA Affinity	GPU NUMA ID
GPU0	 X 	PIX	PIX	PIX	0-19,40-59	0		N/A
GPU1	PIX	 X 	PIX	PIX	0-19,40-59	0		N/A
GPU2	PIX	PIX	 X 	PIX	0-19,40-59	0		N/A
GPU3	PIX	PIX	PIX	 X 	0-19,40-59	0		N/A

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks
```

### Error traceback

```Shell
No valid kernel found for the problem
[TM][FATAL][0814.22:31:20.267204][gemm.cu:327] No feasible kernel found for the problem: sm75_f16_e4m3b128_f16_ttt_fff_8x2048x1024_1
*** stacktrace of thread 0x7f43b1fff640 ***
  [ 0] TM_LOG_FATAL @ gemm.cu:327
  [ 1] LlamaLinear::Impl::Forward() @ LlamaLinear.cu:122
  [ 2] linear_.Forward @ GatedDeltaNetLayer.cc:514
  [ 3] GatedDeltaNetLayer::Forward() @ GatedDeltaNetLayer.cc:355
  [ 4] layer_0 @ unified_decoder.cc:244
  [ 5] UnifiedDecoder::Forward() @ unified_decoder.cc:166
  [ 6] LanguageModel::Impl::Forward() @ language_model.cc:405
  [ 7] ModelExecutor::Impl::Run() @ model_executor.cc:70
  [ 8] ModelExecutor::Impl::InternalThreadEntry() @ model_executor.cc:37
No valid kernel found for the problem
[TM][FATAL][0814.22:31:20.306509][gemm.cu:327] No feasible kernel found for the problem: sm75_f16_e4m3b128_f16_ttt_fff_8x2048x1024_1
No valid kernel found for the problem
No valid kernel found for the problem
*** stacktrace of thread 0x7f43cd0b2640 ***
  [ 0] TM_LOG_FATAL @ gemm.cu:327
  [ 1] LlamaLinear::Impl::Forward() @ LlamaLinear.cu:122
  [ 2] linear_.Forward @ GatedDeltaNetLayer.cc:514
  [ 3] GatedDeltaNetLayer::Forward() @ GatedDeltaNetLayer.cc:355
  [ 4] layer_0 @ unified_decoder.cc:244
  [ 5] UnifiedDecoder::Forward() @ unified_decoder.cc:166
  [ 6] LanguageModel::Impl::Forward() @ language_model.cc:405
  [ 7] ModelExecutor::Impl::Run() @ model_executor.cc:70
  [ 8] ModelExecutor::Impl::InternalThreadEntry() @ model_executor.cc:37
[TM][FATAL][0814.22:31:20.306633][gemm.cu:327] No feasible kernel found for the problem: sm75_f16_e4m3b128_f16_ttt_fff_8x2048x1024_1
[TM][FATAL][0814.22:31:20.306727][gemm.cu:327] No feasible kernel found for the problem: sm75_f16_e4m3b128_f16_ttt_fff_8x2048x1024_1
*** stacktrace of thread 0x7f43cc8b1640 ***
  [ 0] TM_LOG_FATAL @ gemm.cu:327
  [ 1] LlamaLinear::Impl::Forward() @ LlamaLinear.cu:122
  [ 2] linear_.Forward @ GatedDeltaNetLayer.cc:514
  [ 3] GatedDeltaNetLayer::Forward() @ GatedDeltaNetLayer.cc:355
  [ 4] layer_0 @ unified_decoder.cc:244
  [ 5] UnifiedDecoder::Forward() @ unified_decoder.cc:166
  [ 6] LanguageModel::Impl::Forward() @ language_model.cc:405
  [ 7] ModelExecutor::Impl::Run() @ model_executor.cc:70
  [ 8] ModelExecutor::Impl::InternalThreadEntry() @ model_executor.cc:37
*** stacktrace of thread 0x7f43b17fe640 ***
  [ 0] TM_LOG_FATAL @ gemm.cu:327
  [ 1] LlamaLinear::Impl::Forward() @ LlamaLinear.cu:122
  [ 2] linear_.Forward @ GatedDeltaNetLayer.cc:514
  [ 3] GatedDeltaNetLayer::Forward() @ GatedDeltaNetLayer.cc:355
  [ 4] layer_0 @ unified_decoder.cc:244
  [ 5] UnifiedDecoder::Forward() @ unified_decoder.cc:166
  [ 6] LanguageModel::Impl::Forward() @ language_model.cc:405
  [ 7] ModelExecutor::Impl::Run() @ model_executor.cc:70
  [ 8] ModelExecutor::Impl::InternalThreadEntry() @ model_executor.cc:37
/root/startlmdeploy.sh: line 8:     7 Aborted                 (core dumped)
```

## 评论 (2)

### AmirF194 · 2026-08-16

Traced the crash: it comes from turbomind's GEMM kernel selection having no hardware-capability gate for fp8. `src/turbomind/kernels/gemm/gemm.cu:341` throws `No feasible kernel found` only after conversion has already gone ahead and kernel dispatch is attempted, with no earlier check that fp8 tensor-core support needs sm>=9.0 (an RTX 2080 Ti is sm_75/Turing, which doesn't have it).

The pytorch backend already has this exact check: `lmdeploy/pytorch/check_env/cuda.py:19-22`, added alongside its own fp8 support in #3631, rejects `model_format=fp8` on `sm<9.0` with a clear message before touching CUDA at all. Turbomind's fp8 path (`lmdeploy/turbomind/converter.py`, added in #4557/#4602) never got an equivalent check.

So there are two separate things here: SM75 genuinely can't run fp8 today (no kernels for it), which is what #4865 (same reporter) is asking for as a feature; and turbomind failing late with a cryptic C++ error instead of the early, readable rejection the pytorch backend already gives, which looks cheap to close by porting that same check into the turbomind path.


### bltcn · 2026-08-17

In vLLM, support has already been added for running FP8-quantized models on SM75. Essentially, FP8 is just another quantization mode. If AWQ can be supported, there is no reason FP8 cannot be used. The only difference is that SM90 can support FP8 natively, while SM75 supports it in a way similar to AWQ quantization.
