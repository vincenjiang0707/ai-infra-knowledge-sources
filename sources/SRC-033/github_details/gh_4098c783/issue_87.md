# [Issue #87] adaptive_conv_cuda_impl adaptive_conv_cuda.cpp adaptive_conv_kernel.cu

source: https://github.com/Ascend/pytorch/issues/87
state: open | updated: 2025-11-18T06:23:24Z
labels: 

## 正文

How can I replace the CUDA compilation modules in the code within Ascend?

code link: https://github.com/mhamilton723/FeatUp
pip install git+https://github.com/mhamilton723/FeatUp


#include <cuda.h>
#include <ATen/cuda/CUDAContext.h>
#include <cuda_runtime.h>

    ext_modules=[
        CUDAExtension(
            'adaptive_conv_cuda_impl',
            [
                'featup/adaptive_conv_cuda/adaptive_conv_cuda.cpp',
                'featup/adaptive_conv_cuda/adaptive_conv_kernel.cu',
            ]),
        CppExtension(
            'adaptive_conv_cpp_impl',
            ['featup/adaptive_conv_cuda/adaptive_conv.cpp'],
            undef_macros=["NDEBUG"]),
    ],

## 评论 (1)

### yunyiyun · 2025-11-18

https://www.hiascend.com/document/detail/zh/Pytorch/720/ptmoddevg/Frameworkfeatures/featuresguide_00024.html
