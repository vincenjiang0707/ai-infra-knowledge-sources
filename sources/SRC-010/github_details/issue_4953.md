# [Issue #4953] [Bug]  Slower decode speed in v0.17  when compared to v0.14

source: https://github.com/InternLM/lmdeploy/issues/4953
state: open | updated: 2026-09-22T06:25:50Z
labels: 

## 正文

### Checklist

- [x] 1. I have searched related issues but cannot get the expected help.
- [x] 2. The bug has not been fixed in the latest version.
- [ ] 3. Please note that if the bug-related issue you submitted lacks corresponding environment info and a minimal reproducible demo, it will be challenging for us to reproduce and resolve the issue, reducing the likelihood of receiving feedback.

### Describe the bug

We have tested  Qwen3.8-27B model with v0.14 and also in  v0.17. Keeping the input, code and all the configs unchanged, we tested the decode speed in v0.14 and in v0.17 in 2 different environments with corresponding deps

Some basic configs are as follows:

```javascript
{
    "gpu_memory_utilization": 0.9,
    "max_model_len": 32768,
    "max_prefill_token_num": 0,  
    "enable_prefix_caching": true,  
    "profile_prefill": false,
    "dtype": "bfloat16",  
    "quant_policy": 0,
    "engine": "turbomind"
}
``` 



Logs from V0.17:
```javascript
{
      "n_items": 1,
      "wall_s": 89.438,
      "prefill_s": null,
      "decode_s": null,
      "input_tokens": 858,
      "output_tokens": 4096,
      "output_tokens_mean": 4096.0,
      "output_tokens_min": 4096,
      "output_tokens_max": 4096,
      "max_new_tokens": 4096,
      "truncated": 1,
      "tps": 45.8,
      "tps_per_seq": 45.8,
      "decode_tps": null,
      "per_item": [
        {
          "wall_s": null,
          "input_tokens": 858,
          "output_tokens": 4096,
          "tps": null,
          "truncated": 1
        }
      ]
    },
    "inference_time_s": 89.67
  }
``` 


Logs from v0.14:
```javascript
 {
      "n_items": 1,
      "wall_s": 65.819,
      "prefill_s": null,
      "decode_s": null,
      "input_tokens": 858,
      "output_tokens": 4096,
      "output_tokens_mean": 4096.0,
      "output_tokens_min": 4096,
      "output_tokens_max": 4096,
      "max_new_tokens": 4096,
      "truncated": 1,
      "tps": 62.2,
      "tps_per_seq": 62.2,
      "decode_tps": null,
      "per_item": [
        {
          "wall_s": null,
          "input_tokens": 858,
          "output_tokens": 4096,
          "tps": null,
          "truncated": 1
        }
      ]
    },
    "inference_time_s": 66.03
  }``` 


This was tested in H200 Single GPU. We haven't used server mode for the above testing. Let me know if we are missing any configs


### Reproduction

Run as library

### Environment

```Shell
**For v0.17:**


sys.platform: linux
Python: 3.12.14 | packaged by Anaconda, Inc. | (main, Aug 27 2026, 14:46:43) [GCC 14.3.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0: NVIDIA H200
CUDA_HOME: /usr/local/cuda
NVCC: Cuda compilation tools, release 12.6, V12.6.77
GCC: gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
PyTorch: 2.12.1+cu130
PyTorch compiling details: PyTorch built with:
  - GCC 13.3
  - C++ Version: 202002
  - Intel(R) oneAPI Math Kernel Library Version 2024.2-Product Build 20240605 for Intel(R) 64 architecture applications
  - Intel(R) MKL-DNN v3.11.2 (Git Hash 03c022d3ffdcee958cfacbe720048e725fdf644c)
  - OpenMP 201511 (a.k.a. OpenMP 4.5)
  - LAPACK is enabled (usually provided by MKL)
  - NNPACK is enabled
  - CPU capability usage: AVX512
  - CUDA Runtime 13.0
  - NVCC architecture flags: -gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80;-gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_90,code=sm_90;-gencode;arch=compute_100,code=sm_100;-gencode;arch=compute_120,code=sm_120
  - CuDNN 92.0  (built against CUDA 13.2)
  - Magma 2.6.1
  - Build settings: BLAS_INFO=mkl, BUILD_TYPE=Release, COMMIT_SHA=7269437d655783a26cba32aa88195b741ff496aa, CUDA_FLAGS= -DLIBCUDACXX_ENABLE_SIMPLIFIED_COMPLEX_OPERATIONS -Xfatbin -compress-all -DONNX_NAMESPACE=onnx_torch -gencode arch=compute_75,code=sm_75 -gencode arch=compute_80,code=sm_80 -gencode arch=compute_86,code=sm_86 -gencode arch=compute_90,code=sm_90 -gencode arch=compute_100,code=sm_100 -gencode arch=compute_120,code=sm_120 -Xcudafe --diag_suppress=cc_clobber_ignored,--diag_suppress=field_without_dll_interface,--diag_suppress=base_class_has_different_dll_interface,--diag_suppress=dll_interface_conflict_none_assumed,--diag_suppress=dll_interface_conflict_dllexport_assumed,--diag_suppress=bad_friend_decl --expt-relaxed-constexpr --expt-extended-lambda -Xfatbin -compress-all --threads 2 -compress-mode=size -Wno-deprecated-gpu-targets --expt-extended-lambda -DCUB_WRAPPED_NAMESPACE=at_cuda_detail -DDISABLE_CUSPARSE_DEPRECATED -DCUDA_HAS_FP16=1 -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -DC10_NODEPRECATED, CUDA_VERSION=13.0, CUDNN_VERSION=9.20.0, CXX_COMPILER=/opt/rh/gcc-toolset-13/root/usr/bin/c++, CXX_FLAGS= -fvisibility-inlines-hidden -DUSE_PTHREADPOOL -DNDEBUG -DUSE_KINETO -DLIBKINETO_NOROCTRACER -DLIBKINETO_NOXPUPTI=ON -DUSE_FBGEMM -DUSE_MSLK -DUSE_PYTORCH_QNNPACK -DUSE_XNNPACK -DSYMBOLICATE_MOBILE_DEBUG_HANDLE -O2 -fPIC -DC10_NODEPRECATED -Wall -Wextra -Werror=return-type -Werror=non-virtual-dtor -Werror=range-loop-construct -Werror=bool-operation -Wnarrowing -Wno-missing-field-initializers -Wno-unknown-pragmas -Wno-unused-parameter -Wno-strict-overflow -Wno-strict-aliasing -Wno-stringop-overflow -Wsuggest-override -Wno-psabi -Wno-error=old-style-cast -faligned-new -Wno-maybe-uninitialized -fno-math-errno -fno-trapping-math -Werror=format -Wno-dangling-reference -Wno-error=dangling-reference -Wno-stringop-overflow, LAPACK_INFO=mkl, PERF_WITH_AVX=1, PERF_WITH_AVX2=1, TORCH_VERSION=2.12.1, USE_CUDA=ON, USE_CUDNN=ON, USE_CUSPARSELT=1, USE_GFLAGS=OFF, USE_GLOG=OFF, USE_GLOO=ON, USE_MKL=ON, USE_MKLDNN=ON, USE_MPI=OFF, USE_NCCL=1, USE_NNPACK=ON, USE_OPENMP=ON, USE_ROCM=OFF, USE_ROCM_KERNEL_ASSERT=OFF, USE_XCCL=OFF, USE_XPU=OFF, 

TorchVision: 0.27.1+cu130
LMDeploy: 0.17.0+a84fb59
transformers: 5.16.1
fastapi: 0.141.1
pydantic: 2.13.5
triton: 3.7.1
NVIDIA Topology: 
	^[[4mGPU0	NIC0	NIC1	NIC2	NIC3	CPU Affinity	NUMA Affinity	GPU NUMA ID^[[0m
GPU0	 X 	SYS	SYS	NODE	NODE	169,171,173	1		N/A
NIC0	SYS	 X 	PIX	SYS	SYS				
NIC1	SYS	PIX	 X 	SYS	SYS				
NIC2	NODE	SYS	SYS	 X 	PIX				
NIC3	NODE	SYS	SYS	PIX	 X 				

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_1
  NIC1: mlx5_2
  NIC2: mlx5_7
  NIC3: mlx5_8

---------------------------------------------------
**For v0.14**

sys.platform: linux
Python: 3.11.16 (main, Aug 27 2026, 14:44:21) [GCC 14.3.0]
CUDA available: True
MUSA available: False
numpy_random_seed: 2147483648
GPU 0: NVIDIA H200
CUDA_HOME: /usr/local/cuda
NVCC: Cuda compilation tools, release 12.6, V12.6.77
GCC: gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
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
LMDeploy: 0.14.0+a84fb59
transformers: 5.14.1
fastapi: 0.141.1
pydantic: 2.13.5
triton: 3.6.0
NVIDIA Topology: 
	^[[4mGPU0	NIC0	NIC1	NIC2	NIC3	CPU Affinity	NUMA Affinity	GPU NUMA ID^[[0m
GPU0	 X 	SYS	SYS	NODE	NODE	169,171,173	1		N/A
NIC0	SYS	 X 	PIX	SYS	SYS				
NIC1	SYS	PIX	 X 	SYS	SYS				
NIC2	NODE	SYS	SYS	 X 	PIX				
NIC3	NODE	SYS	SYS	PIX	 X 				

Legend:

  X    = Self
  SYS  = Connection traversing PCIe as well as the SMP interconnect between NUMA nodes (e.g., QPI/UPI)
  NODE = Connection traversing PCIe as well as the interconnect between PCIe Host Bridges within a NUMA node
  PHB  = Connection traversing PCIe as well as a PCIe Host Bridge (typically the CPU)
  PXB  = Connection traversing multiple PCIe bridges (without traversing the PCIe Host Bridge)
  PIX  = Connection traversing at most a single PCIe bridge
  NV#  = Connection traversing a bonded set of # NVLinks

NIC Legend:

  NIC0: mlx5_1
  NIC1: mlx5_2
  NIC2: mlx5_7
  NIC3: mlx5_8
```

### Error traceback

```Shell

```

## 评论 (4)

### lvhan028 · 2026-09-10

Hi, @Viji2029 
Thanks for your report. We'll reproduce it as soon as possible. 
I noticed that "max_prefill_token_num" was set 0. Could you use the default value instead?

### Viji2029 · 2026-09-22

Hi Team,
           We have tested the merged PR and observed an improvement in decode speed.It is at 61 tps now .

 However , if we test it on a quantized checkpoint (compressed-tensors, pack-quantized W4A16, group_size=128), it fails with the following error:

`RuntimeError: in_proj_all: <lmdeploy.turbomind._turbomind.Family object at 0x7554b6849e70> requires K >= 128, K % 64 == 0, N >= 1, and N % 64 == 0; got K=5120 N=16480`

The failure is specific to the quantized weight path.


### lvhan028 · 2026-09-22

Hi, @Viji2029 could you share the model url so that we can reproduce it at our side.

### Viji2029 · 2026-09-22

Hi, 
       It is a custom test model (Qwen 3.8-27B) that was quantized using compressed-tensors library.

