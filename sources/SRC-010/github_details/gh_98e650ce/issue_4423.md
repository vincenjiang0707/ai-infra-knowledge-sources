# [Issue #4423] [Bug] V100 nvlink运行Qwen3.5速度异常

source: https://github.com/InternLM/lmdeploy/issues/4423
state: closed | updated: 2026-05-01T02:21:54Z
labels: awaiting response, Stale

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

使用8卡V100 sxm2 nvlink运行Qwen3.5 122B awq 4bit量化只有约22 token/s 
使用4卡，2卡运行更小尺寸的模型情况类似，速度大幅低于预期

### Reproduction

lmdeploy serve api_server /root/ssd_cache/Qwen/QuantTrio/Qwen3.5-122B-A10B-AWQ   --tp 8   --cache-max-entry-count 0.75   --max-batch-size 64 --quant-policy 8   --enable
-prefix-caching   --server-port 6006 

### Environment

```Shell
root@autodl-container-96e947997b-61f74d95:~/lmdeploy# lmdeploy check_env
sys.platform: linux
Python: 3.12.3 | packaged by Anaconda, Inc. | (main, May  6 2024, 19:46:43) [GCC 11.2.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0,1,2,3,4,5,6,7: Tesla PG503-216
CUDA_HOME: /usr/local/cuda
NVCC: Cuda compilation tools, release 12.8, V12.8.93
GCC: gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
PyTorch: 2.8.0+cu128
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
    - Built with CuDNN 90.8
  - Magma 2.6.1
  - Build settings: BLAS_INFO=mkl, BUILD_TYPE=Release, COMMIT_SHA=a1cb3cc05d46d198467bebbb6e8fba50a325d4e7, CUDA_VERSION=12.8, CUDNN_VERSION=9.8.0, CXX_COMPILER=/opt/rh/gcc-toolset-13/root/usr/bin/c++, CXX_FLAGS= -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOROCTRACER -DLIBKINETO_NOXPUPTI=ON -DUSE_FBGEMM -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -DC10_NODEPRECATED -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=range-loop-construct -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-unknown-pragmas -Wno-unused-parameter -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=old-style-cast -faligned-new -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-dangling-reference -Wno-error=dangling-reference -Wno-stringop-overflow, LAPACK_INFO=mkl, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, TORCH_VERSION=2.8.0, USE_CUDA=ON, USE_CUDNN=ON, USE_CUSPARSELT=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_GLOO=ON, USE_MKL=ON, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=1, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF, USE_XCCL=OFF, USE_XPU=OFF, 

TorchVision: 0.23.0+cu128
LMDeploy: 0.12.2+
transformers: 5.3.0
fastapi: 0.135.1
pydantic: 2.12.5
triton: 3.4.0
NVIDIA Topology: 
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      NV1     NV1     NV2     NV2     SYS     SYS     SYS     0-19,40-59      0               N/A
GPU1    NV1      X      NV2     NV1     SYS     NV2     SYS     SYS     0-19,40-59      0               N/A
GPU2    NV1     NV2      X      NV2     SYS     SYS     NV1     SYS     0-19,40-59      0               N/A
GPU3    NV2     NV1     NV2      X      SYS     SYS     SYS     NV1     0-19,40-59      0               N/A
GPU4    NV2     SYS     SYS     SYS      X      NV1     NV1     NV2     20-39,60-79     1               N/A
GPU5    SYS     NV2     SYS     SYS     NV1      X      NV2     NV1     20-39,60-79     1               N/A
GPU6    SYS     SYS     NV1     SYS     NV1     NV2      X      NV2     20-39,60-79     1               N/A
GPU7    SYS     SYS     SYS     NV1     NV2     NV1     NV2      X      20-39,60-79     1               N/A

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

```

## 评论 (6)

### xywjlidi · 2026-03-18

发现相同的问题，按照qwen3的测试结果，目前0.12.2版本v100运行qwen3.5的decode速度大概只有预期的30%。

### Slava715 · 2026-03-18

The same problem on 5090 and v0.12.2, when running QuantTrio/Qwen3.5-35B-A3B-AWQ, the generation speed is 4 times lower compared to running via vllm.

### JiwaniZakir · 2026-04-03

The core issue is almost that V100 (sm_70) lacks native INT4 tensor core support, which AWQ 4-bit weight quantization kernels depend on — these are optimized for sm_75 (Turing) at minimum and sm_80+ (Ampere) for peak throughput. On V100, the quantized weights likely get dequantized back to FP16 before GEMM, negating most of the compute benefit of AWQ and introducing extra memory traffic. Additionally, `--quant-policy 8` enables INT8 KV cache quantization, which also has no hardware acceleration on sm_70, compounding the overhead. Running the model in pure FP16 without `--quant-policy 8` may actually yield better throughput on V100, and you can verify kernel dispatch behavior by checking the `w4a16` kernel selection path in `lmdeploy/turbomind/kernels/` for sm_70 fallback behavior.

### lvhan028 · 2026-04-18

You may want to give v0.12.3 a try. It includes optimizations for Qwen3.5 on Volta architecture, which should address the performance issues you're seeing with V100. Let us know if it helps!

### github-actions[bot] · 2026-04-26

This issue is marked as stale because it has been marked as invalid or awaiting response for 7 days without any further response. It will be closed in 5 days if the stale label is not removed or if there is no further response.

### github-actions[bot] · 2026-05-01

This issue is closed because it has been stale for 5 days. Please open a new issue if you have similar issues or you have any new updates now.
