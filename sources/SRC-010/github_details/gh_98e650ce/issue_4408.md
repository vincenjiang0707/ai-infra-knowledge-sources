# [Issue #4408] [Bug] Qwen3.5 Turbomind missing V100 support

source: https://github.com/InternLM/lmdeploy/issues/4408
state: closed | updated: 2026-03-19T15:29:13Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [x] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug
```
[TM][FATAL] kernels/attention/decoding.cu(34): Check failed: kernel No decoding kernel found: decode_d256_f16_gs4
```
### Reproduction

Run Qwen3.5 model.

### Environment

```Shell
sys.platform: linux
Python: 3.10.12 (main, Mar  3 2026, 11:56:32) [GCC 11.4.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0,1,2,3: Tesla V100-SXM2-32GB
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
LMDeploy: 0.12.1+
transformers: 5.3.0
fastapi: 0.135.1
pydantic: 2.12.5
triton: 3.6.0
NVIDIA Topology: 
        GPU0    GPU1    GPU2    GPU3    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      NV2     NV2     NV1     20-39,60-79     1               N/A
GPU1    NV2      X      NV1     NV2     20-39,60-79     1               N/A
GPU2    NV2     NV1      X      NV1     20-39,60-79     1               N/A
GPU3    NV1     NV2     NV1      X      20-39,60-79     1               N/A

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

### mizuikki · 2026-03-13

I tested the decoding_sm70_256.diff patch, but I'm only achieving 30 tokens/s on my dual V100 setup.
// src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu
```
diff --git a/src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu b/src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu
index 5442ffac..6cb44778 100644
--- a/src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu
+++ b/src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu
@@ -14,30 +14,42 @@ namespace turbomind::attention {
 constexpr int kHeadDim = 256;
 constexpr int kCTA_S   = 64;
 constexpr int kWARP_S  = 16;
-constexpr int kStages  = 3;
+
+// Use fewer pipeline stages for the non-quantized d256 SM70 decode kernels.
+// Root cause: with CTA_S=64 and head_dim=256, the original 3-stage fp16 KV-cache path needs
+// 3 * 64 * 256 * sizeof(half) + 3 * 64 * 2 * sizeof(half) = 99,072 bytes of dynamic shared
+// memory because `SharedStorage` keeps staged K/V tiles together with the KV parameter scratch.
+// Tesla V100 / SM70 exposes only 98,304 bytes via `cudaDevAttrMaxSharedMemoryPerBlockOptin`,
+// so Registry::Add() rejects these kernels and GQA decode falls through to
+// "No decoding kernel found: decode_d256_f16_gs8".
+// Solution: keep the 3-stage pipeline for quantized KV-cache kernels, but register a 2-stage
+// fp16 KV-cache variant that fits within the SM70 opt-in shared-memory limit.
+// Affected by: NVIDIA Volta / SM70 devices such as Tesla V100
+constexpr int kF16Stages = 2;
+constexpr int kKVStages  = 3;
 
 // kH = Qh%3==0 ? 3 : (Qh%2==0 ? 2 : 1)
 // kH=1 covers Qh ∈ {1,5,7}, kH=2 covers {2,4,8}, kH=3 covers {3,6,9}
-template<class T, class Tkv, int kH>
+template<class T, class Tkv, int kH, int Stages>
 using KT =
     AttentionUniversal<arch::Sm70,
-                       Mainloop<arch::Sm70, Impl<MMA_SIMT, T, Tkv, kH, 1, kCTA_S, kH, 1, kWARP_S, kHeadDim, kStages>>,
+                       Mainloop<arch::Sm70, Impl<MMA_SIMT, T, Tkv, kH, 1, kCTA_S, kH, 1, kWARP_S, kHeadDim, Stages>>,
                        GetBlockIterFactory<T, Tkv, kCTA_S, kHeadDim>,
                        DecodingCtaMap>;
 
 namespace {
 Registrar reg([](Collector& c) {
-    c.add<KT<half, half, 1>>();
-    c.add<KT<half, half, 2>>();
-    c.add<KT<half, half, 3>>();
+    c.add<KT<half, half, 1, kF16Stages>>();
+    c.add<KT<half, half, 2, kF16Stages>>();
+    c.add<KT<half, half, 3, kF16Stages>>();
 
-    c.add<KT<half, uint8_t, 1>>();
-    c.add<KT<half, uint8_t, 2>>();
-    c.add<KT<half, uint8_t, 3>>();
+    c.add<KT<half, uint8_t, 1, kKVStages>>();
+    c.add<KT<half, uint8_t, 2, kKVStages>>();
+    c.add<KT<half, uint8_t, 3, kKVStages>>();
 
-    c.add<KT<half, uint4_t, 1>>();
-    c.add<KT<half, uint4_t, 2>>();
-    c.add<KT<half, uint4_t, 3>>();
+    c.add<KT<half, uint4_t, 1, kKVStages>>();
+    c.add<KT<half, uint4_t, 2, kKVStages>>();
+    c.add<KT<half, uint4_t, 3, kKVStages>>();
 });
 }
```

### tuilakhanh · 2026-03-13

> I tested the decoding_sm70_256.diff patch, but I'm only achieving 30 tokens/s on my dual V100 setup. // src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu
> 
> ```
> diff --git a/src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu b/src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu
> index 5442ffac..6cb44778 100644
> --- a/src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu
> +++ b/src/turbomind/kernels/attention/kernel/decoding_sm70_256.cu
> @@ -14,30 +14,42 @@ namespace turbomind::attention {
>  constexpr int kHeadDim = 256;
>  constexpr int kCTA_S   = 64;
>  constexpr int kWARP_S  = 16;
> -constexpr int kStages  = 3;
> +
> +// Use fewer pipeline stages for the non-quantized d256 SM70 decode kernels.
> +// Root cause: with CTA_S=64 and head_dim=256, the original 3-stage fp16 KV-cache path needs
> +// 3 * 64 * 256 * sizeof(half) + 3 * 64 * 2 * sizeof(half) = 99,072 bytes of dynamic shared
> +// memory because `SharedStorage` keeps staged K/V tiles together with the KV parameter scratch.
> +// Tesla V100 / SM70 exposes only 98,304 bytes via `cudaDevAttrMaxSharedMemoryPerBlockOptin`,
> +// so Registry::Add() rejects these kernels and GQA decode falls through to
> +// "No decoding kernel found: decode_d256_f16_gs8".
> +// Solution: keep the 3-stage pipeline for quantized KV-cache kernels, but register a 2-stage
> +// fp16 KV-cache variant that fits within the SM70 opt-in shared-memory limit.
> +// Affected by: NVIDIA Volta / SM70 devices such as Tesla V100
> +constexpr int kF16Stages = 2;
> +constexpr int kKVStages  = 3;
>  
>  // kH = Qh%3==0 ? 3 : (Qh%2==0 ? 2 : 1)
>  // kH=1 covers Qh ∈ {1,5,7}, kH=2 covers {2,4,8}, kH=3 covers {3,6,9}
> -template<class T, class Tkv, int kH>
> +template<class T, class Tkv, int kH, int Stages>
>  using KT =
>      AttentionUniversal<arch::Sm70,
> -                       Mainloop<arch::Sm70, Impl<MMA_SIMT, T, Tkv, kH, 1, kCTA_S, kH, 1, kWARP_S, kHeadDim, kStages>>,
> +                       Mainloop<arch::Sm70, Impl<MMA_SIMT, T, Tkv, kH, 1, kCTA_S, kH, 1, kWARP_S, kHeadDim, Stages>>,
>                         GetBlockIterFactory<T, Tkv, kCTA_S, kHeadDim>,
>                         DecodingCtaMap>;
>  
>  namespace {
>  Registrar reg([](Collector& c) {
> -    c.add<KT<half, half, 1>>();
> -    c.add<KT<half, half, 2>>();
> -    c.add<KT<half, half, 3>>();
> +    c.add<KT<half, half, 1, kF16Stages>>();
> +    c.add<KT<half, half, 2, kF16Stages>>();
> +    c.add<KT<half, half, 3, kF16Stages>>();
>  
> -    c.add<KT<half, uint8_t, 1>>();
> -    c.add<KT<half, uint8_t, 2>>();
> -    c.add<KT<half, uint8_t, 3>>();
> +    c.add<KT<half, uint8_t, 1, kKVStages>>();
> +    c.add<KT<half, uint8_t, 2, kKVStages>>();
> +    c.add<KT<half, uint8_t, 3, kKVStages>>();
>  
> -    c.add<KT<half, uint4_t, 1>>();
> -    c.add<KT<half, uint4_t, 2>>();
> -    c.add<KT<half, uint4_t, 3>>();
> +    c.add<KT<half, uint4_t, 1, kKVStages>>();
> +    c.add<KT<half, uint4_t, 2, kKVStages>>();
> +    c.add<KT<half, uint4_t, 3, kKVStages>>();
>  });
>  }
> ```

I tried a PR before rebasing from main, and it worked with the V100, but only for AWQ models. I previously tested a 35B model on a V100 and managed to get around 40 tokens/s.

### carcoonzyk · 2026-03-13

Is there a way to cancel the loading of the visual capabilities of multimodal models in lmdeploy turbomind? I need this to load qwen3.5 in resource-constrained environments.

### huliangbing2000 · 2026-03-14

最新版lmdeploy能支持v100跑qwen3.5-35b-a3b?

### lvhan028 · 2026-03-18

May refer to #4420 

### tuilakhanh · 2026-03-19

Fixed with https://github.com/InternLM/lmdeploy/pull/4420
