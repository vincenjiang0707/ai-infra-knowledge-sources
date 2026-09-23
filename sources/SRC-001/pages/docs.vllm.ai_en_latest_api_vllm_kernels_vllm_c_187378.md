source: https://docs.vllm.ai/en/latest/api/vllm/kernels/vllm_c/
lastmod: 2026-09-23

#

`vllm.kernels.vllm_c`

[¶](https://docs.vllm.ai#vllm.kernels.vllm_c)

Attributes:

-
–[CUDA_ALIKE](https://docs.vllm.ai#vllm.kernels.vllm_c.CUDA_ALIKE)Most kernels in this file are supported on all CUDA-alike platforms.

-
–[IS_ROCM](https://docs.vllm.ai#vllm.kernels.vllm_c.IS_ROCM)ROCm needs shape normalization before calling some vLLM C kernels.

-
–[rms_add_no_var_size](https://docs.vllm.ai#vllm.kernels.vllm_c.rms_add_no_var_size)vLLM Kernel does not support variance_size parameter and requires

-
–[rms_no_var_size](https://docs.vllm.ai#vllm.kernels.vllm_c.rms_no_var_size)vLLM kernel requires no variance_size override and matching input/weight dtype.


##

`CUDA_ALIKE = current_platform.is_cuda_alike()`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.vllm_c.CUDA_ALIKE)

Most kernels in this file are supported on all CUDA-alike platforms.

##

`IS_ROCM = current_platform.is_rocm()`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.vllm_c.IS_ROCM)

ROCm needs shape normalization before calling some vLLM C kernels.

##

`rms_add_no_var_size = lambda x, x_residual, weight, epsilon, variance_size=None: variance_size is None and (weight is None or weight.dtype == x.dtype)`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.vllm_c.rms_add_no_var_size)

vLLM Kernel does not support variance_size parameter and requires matching input/weight dtype.

##

`rms_no_var_size = lambda x, weight, epsilon, variance_size=None: variance_size is None and (weight is None or weight.dtype == x.dtype)`

`module-attribute`

[¶](https://docs.vllm.ai#vllm.kernels.vllm_c.rms_no_var_size)

vLLM kernel requires no variance_size override and matching input/weight dtype.