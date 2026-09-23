# [Issue #4957] [Bug] 0.16.0和0.17.0版本lmdeploy加载InternVL3-78B模型W4A16量化版时内存要比0.15.0以及之前的版本要多150GB内存

source: https://github.com/InternLM/lmdeploy/issues/4957
state: closed | updated: 2026-09-17T10:15:56Z
labels: awaiting response

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

CUDA_VISIBLE_DEVICES=0,1,2,3 lmdeploy serve api_server /data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored --model-name InternVL3-78B-W4A16 --trust-remote-code --tp 4 --server-port 17891 --session-len 16384 --dtype float16 --cache-max-entry-count 0.85 --cache-block-seq-len 64 --max-batch-size 32 --vision-max-batch-size 8 --quant-policy 8 --enable-prefix-caching --max-prefill-token-num 16384 --log-level WARNING
我使用上述命令在一个4卡v100 32G显存+256GB主机内存的服务器上部署InternVL3-78B模型W4A16量化版，我测试了lmdeploy的0.13.0、0.15.0、0.16.0和0.17.0这四个版本，发现0.13.0和0.15.0这两个版本的lmdeploy加载完模型成功启动后，lmdeploy约占主机内存1.7%，使用0.16.0和0.17.0这两个版本的lmdeploy加载玩模型成功启动后，lmdeploy约占主机内存60.2%，想知道怎么才能减少主机的占用，下降至10%以内。

下面时使用0.16.0版本lmdeploy加载InternVL3-78B模型W4A16量化版的日志：
(py3.10_for_llm-run-with-lmdeploy_0.16.0) zenking@admin123:/data/qianyong/llm-internvl$ CUDA_VISIBLE_DEVICES=0,1,2,3 lmdeploy serve api_server /data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored --model-name InternVL3-78B-W4A16 --trust-remote-code --tp 4 --server-port 17891 --session-len 18432 --dtype float16 --cache-max-entry-count 0.85 --cache-block-seq-len 64 --max-batch-size 32 --vision-max-batch-size 8 --quant-policy 8 --enable-prefix-caching --max-prefill-token-num 16384 --log-level WARNING
[transformers] The tokenizer you are loading from '/data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
[transformers] The tokenizer you are loading from '/data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
[transformers] The tokenizer you are loading from '/data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
[transformers] You are using a model of type `internvl_chat` to instantiate a model of type ``. This may be expected if you are loading a checkpoint that shares a subset of the architecture (e.g., loading a `sam2_video` checkpoint into `Sam2Model`), but is otherwise not supported and can yield errors. Please verify that the checkpoint is compatible with the model you are instantiating.
[transformers] The tokenizer you are loading from '/data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
[transformers] You are using a model of type `internvl_chat` to instantiate a model of type ``. This may be expected if you are loading a checkpoint that shares a subset of the architecture (e.g., loading a `sam2_video` checkpoint into `Sam2Model`), but is otherwise not supported and can yield errors. Please verify that the checkpoint is compatible with the model you are instantiating.
[transformers] The tokenizer you are loading from '/data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
[TM][WARN][0912.11:43:21.506350][turbomind.cc:123] `max_context_token_num` is not set, default to 18432.
[transformers] The tokenizer you are loading from '/data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored' with an incorrect regex pattern: https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503/discussions/84#69121093e8b480e709447d5e. This will lead to incorrect tokenization. You should set the `fix_mistral_regex=True` flag when loading this tokenizer to fix this issue.
[TM][WARN][0912.11:44:07.043272][nccl.cu:81] Window registration may cause memory leaks in NCCL 2.27, use NCCL 2.28+ or disable the feature by setting NCCL_WIN_ENABLE=0.
[TM][WARN][0912.11:45:20.543139][slab.h:135] slab_size 33554432, object_size 2703360, object_count 12, ratio 0.9667969
[TM][WARN][0912.11:45:22.614722][slab.h:135] slab_size 33554432, object_size 2703360, object_count 12, ratio 0.9667969
[TM][WARN][0912.11:45:22.613705][slab.h:135] slab_size 33554432, object_size 2703360, object_count 12, ratio 0.9667969
[TM][WARN][0912.11:45:22.614680][slab.h:135] slab_size 33554432, object_size 2703360, object_count 12, ratio 0.9667969
HINT:    Please open http://0.0.0.0:17891 in a browser for detailed api usage!!!
HINT:    Please open http://0.0.0.0:17891 in a browser for detailed api usage!!!
HINT:    Please open http://0.0.0.0:17891 in a browser for detailed api usage!!!
INFO:     Started server process [303578]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:17891 (Press CTRL+C to quit)


### Reproduction

(py3.10_for_llm-run-with-lmdeploy_0.16.0) zenking@admin123:/data/qianyong/llm-internvl$ CUDA_VISIBLE_DEVICES=0,1,2,3 lmdeploy serve api_server /data/feature/models/InternVL3-78B-W4A16-by-LLMC_vision_ignored --model-name InternVL3-78B-W4A16 --trust-remote-code --tp 4 --server-port 17891 --session-len 18432 --dtype float16 --cache-max-entry-count 0.85 --cache-block-seq-len 64 --max-batch-size 32 --vision-max-batch-size 8 --quant-policy 8 --enable-prefix-caching --max-prefill-token-num 16384 --log-level WARNING

### Environment

```Shell
(py3.10_for_llm-run-with-lmdeploy_0.16.0) zenking@admin123:/data/qianyong/llm-internvl$ lmdeploy check_env
sys.platform: linux
Python: 3.10.21 (main, Aug 27 2026, 14:42:07) [GCC 14.3.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0,1,2,3,4,5,6,7: Tesla V100-SXM2-32GB
CUDA_HOME: /usr
NVCC: Cuda compilation tools, release 12.0, V12.0.140
GCC: gcc (Ubuntu 13.3.0-6ubuntu2~24.04.1) 13.3.0
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
LMDeploy: 0.16.0+21e134d
transformers: 5.17.0
fastapi: 0.141.1
pydantic: 2.13.5
triton: 3.6.0
NVIDIA Topology:
        GPU0    GPU1    GPU2    GPU3    GPU4    GPU5    GPU6    GPU7    CPU Affinity    NUMA Affinity   GPU NUMA ID
GPU0     X      NV1     NV2     NV1     SYS     SYS     SYS     NV2     0-17,36-53      0               N/A
GPU1    NV1      X      NV1     NV2     SYS     SYS     NV2     SYS     0-17,36-53      0               N/A
GPU2    NV2     NV1      X      NV2     SYS     NV1     SYS     SYS     0-17,36-53      0               N/A
GPU3    NV1     NV2     NV2      X      NV1     SYS     SYS     SYS     0-17,36-53      0               N/A
GPU4    SYS     SYS     SYS     NV1      X      NV2     NV2     NV1     18-35,54-71     1               N/A
GPU5    SYS     SYS     NV1     SYS     NV2      X      NV1     NV2     18-35,54-71     1               N/A
GPU6    SYS     NV2     SYS     SYS     NV2     NV1      X      NV1     18-35,54-71     1               N/A
GPU7    NV2     SYS     SYS     SYS     NV1     NV2     NV1      X      18-35,54-71     1               N/A

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

## 评论 (5)

### 18610361898 · 2026-09-12

下面时执行lmdeploy命令加载模型前的内存使用情况：
(base) zenking@admin123:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           251Gi        10Gi       158Gi       3.5Mi        85Gi       241Gi
Swap:          8.0Gi       2.3Gi       5.7Gi
下面时执行lmdeploy命令加载模型后的内存使用情况：
(base) zenking@admin123:~$ free -h
               total        used        free      shared  buff/cache   available
Mem:           251Gi       166Gi       1.3Gi       149Gi       235Gi        84Gi
Swap:          8.0Gi       2.3Gi       5.7Gi

### 18610361898 · 2026-09-12

<img width="1044" height="1730" alt="Image" src="https://github.com/user-attachments/assets/e09d6e84-b2a2-47b9-8e8f-5fe1f8dd58fd" />0.17.0版本lmdeploy是在红线所在的时间点疯狂分配主机端内存达150GB

### lvhan028 · 2026-09-14

根据日志提示，怀疑是用了 nccl 2.27 的原因，麻烦升级下 nccl 的版本试试。
```shell
pip install nvidia-nccl-cu12 -U
```

### irexyc · 2026-09-14

It looks like the memory usage is due to the relatively large input buffer. https://github.com/InternLM/lmdeploy/blob/main/src/turbomind/models/internvit/internvit.cc#L99-L101

You can temporarily  reduce number of `--max-prefill-token-num` and add `--async 0`  and I'll think about whether there's a better way to handle it.

### 18610361898 · 2026-09-14

经过定位调试分析是internvit.cc文件预分配内存导致的，改成按需分配后问题解决了，详细补丁如下：
diff --git a/src/turbomind/models/internvit/internvit.cc b/src/turbomind/models/internvit/internvit.cc
index 434097a4..cc637906 100644
--- a/src/turbomind/models/internvit/internvit.cc
+++ b/src/turbomind/models/internvit/internvit.cc
@@ -75,9 +75,10 @@ struct InternVit::Impl {
         const auto& cfg = weights.config();
         for (int i = 0; i < phases; ++i) {
             auto& d           = data_.emplace_back();
-            d.batch_input     = {{engine.max_forward_token_num, cfg.in_channels, cfg.image_height, cfg.image_width},
-                             cfg.data_type,
-                             kCPUpinned};
+            // d.batch_input     = {{engine.max_forward_token_num, cfg.in_channels, cfg.image_height, cfg.image_width},
+            //                  cfg.data_type,
+            //                  kCPUpinned};
+            d.batch_input     = {};
             d.attn_cu_seqlens = Tensor_<int>{{engine.max_forward_token_num + 1}, kDEVICE};
             d.attn_finished   = Tensor_<bool>{{engine.max_forward_token_num}, kDEVICE};
         }
@@ -260,7 +261,7 @@ struct InternVit::Impl {
 
         if (d.batch_size > 0) {
             // batch input
-            if (d.batch_size > d.batch_input.shape(0)) {
+            if (!d.batch_input || d.batch_size > d.batch_input.shape(0)) {
                 core::ContextGuard ctx{Allocator{kCPUpinned}};
                 Layout             layout{d.batch_size, cfg.in_channels, cfg.image_height, cfg.image_width};
                 d.batch_input = {layout, cfg.data_type, kCPUpinned};

