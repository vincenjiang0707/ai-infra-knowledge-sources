# [Issue #93] Tesla T4 Feature '.m16n8k16' requires .target sm_80 or higher

source: https://github.com/mit-han-lab/llm-awq/issues/93
state: open | updated: 2024-08-14T11:06:50Z
labels: 

## 正文

Can i run AWQ on Testla T4?

`
/app/repositories/llm-awq/awq/kernels/csrc/quantization/gemm_cuda_gen.cu(22): warning #177-D: function "__pack_half2" was declared but never referenced

ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 928; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 932; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 936; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 940; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 944; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 948; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 952; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 956; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1000; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1004; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1008; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1012; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1016; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1020; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1024; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1028; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1854; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1858; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1862; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1866; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1894; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1898; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1902; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas /tmp/tmpxft_00000033_00000000-6_gemm_cuda_gen.ptx, line 1906; error   : Feature '.m16n8k16' requires .target sm_80 or higher
ptxas fatal   : Ptx assembly aborted due to errors
[4/7] /usr/local/cuda-11/bin/nvcc  -I/usr/local/lib/python3.10/dist-packages/torch/include -I/usr/local/lib/python3.10/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.10/dist-packages/torch/include/TH -I/usr/local/lib/python3.10/dist-packages/torch/include/THC -I/usr/local/cuda-11/include -I/usr/include/python3.10 -c -c /app/repositories/llm-awq/awq/kernels/csrc/position_embedding/pos_encoding_kernels.cu -o /app/repositories/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/position_embedding/pos_encoding_kernels.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O3 -std=c++17 -DENABLE_BF16 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U__CUDA_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math --threads=8 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1011"' -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_75,code=compute_75 -gencode=arch=compute_75,code=sm_75 -ccbin gcc
/usr/local/lib/python3.10/dist-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
/usr/local/lib/python3.10/dist-packages/torch/include/c10/core/TensorImpl.h(77): here

/usr/local/lib/python3.10/dist-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
/usr/local/lib/python3.10/dist-packages/torch/include/ATen/core/qualified_name.h(73): here

[5/7] /usr/local/cuda-11/bin/nvcc  -I/usr/local/lib/python3.10/dist-packages/torch/include -I/usr/local/lib/python3.10/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.10/dist-packages/torch/include/TH -I/usr/local/lib/python3.10/dist-packages/torch/include/THC -I/usr/local/cuda-11/include -I/usr/include/python3.10 -c -c /app/repositories/llm-awq/awq/kernels/csrc/layernorm/layernorm.cu -o /app/repositories/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/layernorm/layernorm.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O3 -std=c++17 -DENABLE_BF16 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U__CUDA_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math --threads=8 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1011"' -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_75,code=compute_75 -gencode=arch=compute_75,code=sm_75 -ccbin gcc
/usr/local/lib/python3.10/dist-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
/usr/local/lib/python3.10/dist-packages/torch/include/c10/core/TensorImpl.h(77): here

/usr/local/lib/python3.10/dist-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
/usr/local/lib/python3.10/dist-packages/torch/include/ATen/core/qualified_name.h(73): here

[6/7] /usr/local/cuda-11/bin/nvcc  -I/usr/local/lib/python3.10/dist-packages/torch/include -I/usr/local/lib/python3.10/dist-packages/torch/include/torch/csrc/api/include -I/usr/local/lib/python3.10/dist-packages/torch/include/TH -I/usr/local/lib/python3.10/dist-packages/torch/include/THC -I/usr/local/cuda-11/include -I/usr/include/python3.10 -c -c /app/repositories/llm-awq/awq/kernels/csrc/quantization/gemv_cuda.cu -o /app/repositories/llm-awq/awq/kernels/build/temp.linux-x86_64-3.10/csrc/quantization/gemv_cuda.o -D__CUDA_NO_HALF_OPERATORS__ -D__CUDA_NO_HALF_CONVERSIONS__ -D__CUDA_NO_BFLOAT16_CONVERSIONS__ -D__CUDA_NO_HALF2_OPERATORS__ --expt-relaxed-constexpr --compiler-options ''"'"'-fPIC'"'"'' -O3 -std=c++17 -DENABLE_BF16 -U__CUDA_NO_HALF_OPERATORS__ -U__CUDA_NO_HALF_CONVERSIONS__ -U__CUDA_NO_BFLOAT16_OPERATORS__ -U__CUDA_NO_BFLOAT16_CONVERSIONS__ -U__CUDA_NO_BFLOAT162_OPERATORS__ -U__CUDA_NO_BFLOAT162_CONVERSIONS__ --expt-relaxed-constexpr --expt-extended-lambda --use_fast_math --threads=8 -DTORCH_API_INCLUDE_EXTENSION_H '-DPYBIND11_COMPILER_TYPE="_gcc"' '-DPYBIND11_STDLIB="_libstdcpp"' '-DPYBIND11_BUILD_ABI="_cxxabi1011"' -DTORCH_EXTENSION_NAME=awq_inference_engine -D_GLIBCXX_USE_CXX11_ABI=0 -gencode=arch=compute_75,code=compute_75 -gencode=arch=compute_75,code=sm_75 -ccbin gcc
/app/repositories/llm-awq/awq/kernels/csrc/quantization/gemv_cuda.cu(224): warning #177-D: variable "blockDim_z" was declared but never referenced

/usr/local/lib/python3.10/dist-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=size_t, one_sided=false, <unnamed>=0]" 
/usr/local/lib/python3.10/dist-packages/torch/include/c10/core/TensorImpl.h(77): here

/usr/local/lib/python3.10/dist-packages/torch/include/c10/util/irange.h(54): warning #186-D: pointless comparison of unsigned integer with zero
          detected during:
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator==(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
(61): here
            instantiation of "__nv_bool c10::detail::integer_iterator<I, one_sided, <unnamed>>::operator!=(const c10::detail::integer_iterator<I, one_sided, <unnamed>> &) const [with I=std::size_t, one_sided=true, <unnamed>=0]" 
/usr/local/lib/python3.10/dist-packages/torch/include/ATen/core/qualified_name.h(73): here
`

## 评论 (7)

### sevenseven91 · 2023-10-22

Fixed

### hongyeon-yu · 2023-11-26

> Fixed

I am also facing the same issue. Could you please tell me how you fixed it?

### fxmarty · 2023-11-30

`Feature '.m16n8k16' requires .target sm_80 or higher`

IMO AWQ can't run on T4 GPUs. On A100 you need `TORCH_CUDA_ARCH_LIST="8.0" python setup.py install`

### pribadihcr · 2024-03-22

Hi @fxmarty this is the example workaround for older gpu https://github.com/vllm-project/vllm/pull/1252 How to adapt to this repo?  thanks

### starsy · 2024-05-13

> `Feature '.m16n8k16' requires .target sm_80 or higher`
> 
> IMO AWQ can't run on T4 GPUs. On A100 you need `TORCH_CUDA_ARCH_LIST="8.0" python setup.py install`

this trick works for H100. 

### ao-zz · 2024-06-03

@hongyeonyu @pribadihcr
```bash
cd awq/kernels
export TORCH_CUDA_ARCH_LIST="x.y"  # add this
python setup.py install
```

"x.y" should be `8.0` or higher, which depends on your GPU (see [here](https://developer.nvidia.com/cuda-gpus#compute))
For personal users, **RTX 3060** or newer is required.
For data center users, **A2** or newer is required.

### Ali-Flt · 2024-08-14

This should be in the README
