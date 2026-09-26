# [Issue #202] CU_TENSOR_MAP_SWIZZLE_128B_ATOM_32B causes CUDA versions below 12.8 to fail to compile.

source: https://github.com/deepseek-ai/DeepGEMM/issues/202
state: closed | updated: 2025-10-01T12:29:31Z
labels: 

## 正文

According to [CUDA 12.6.1 document](https://docs.nvidia.com/cuda/archive/12.6.1/cuda-driver-api/group__CUDA__TENSOR__MEMORY.html) and [CUDA 12.8.0 document](https://docs.nvidia.com/cuda/archive/12.8.0/cuda-driver-api/group__CUDA__TENSOR__MEMORY.html), enum `CU_TENSOR_MAP_SWIZZLE_128B_ATOM_32B` appears to have been added in 12.8. 

Changes in #198 make CUDA versions < 12.8 to fail to compile.

https://github.com/deepseek-ai/DeepGEMM/blob/594953acce41793ae00a1233eb516044d604bcb6/csrc/jit_kernels/impls/runtime_utils.hpp#L70-L76

## 评论 (1)

### LyricZhao · 2025-10-01

Fixed in https://github.com/deepseek-ai/DeepGEMM/commit/07b82fb8cd035330b8849ebc42ef9d6df2dfdde4. Thanks!
