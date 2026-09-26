# [Issue #6] Support for Ada Lovelace & Blackwell

source: https://github.com/deepseek-ai/DeepGEMM/issues/6
state: open | updated: 2026-05-22T07:59:40Z
labels: 

## 正文

This is perhaps better served as a feature request, but I can see wide interest in proper F8 implementation for the 4090/5090 series of GPUs. Is there any interest in adapting this for sm_89 & sm_100/a? Is it a steep challenge or is it feasible?

Many thanks for providing this repo. It is a remarkable contribution to the field.

## 评论 (13)

### LyricZhao · 2025-02-26

I'm not sure whether it is hard to add other arch-support and maximize the performance. We may release new version if we get some other arch support, also, open-source community PRs are welcomed.


### nupam · 2025-02-26

when openCL+RISC-V? :P 

### eternaphia · 2025-03-01

i'm working on adapting to Ada Lovelace

### leedrake5 · 2025-03-04

An update on my efforts:

First step is to install cutlass within the third_party folder for the intended architecture: 
```
cd ~/GitHub/DeepGEMM/third_party/cutlass
mkdir build && cd build
cmake .. -DCUTLASS_NVCC_ARCHS="89"
make test_unit -j 18
```
I am using 18 cores since I have an intel i9, but specify a number here! -j flag will go nuts and consume all RAM during the tests if you don't tailor it for your system. 

Next, change references from SM90 & sm_90 to SM89 & sm_89 in the following files:

> ~/GitHub/DeepGEMM/deep_gemm/include/deep_gemm/fp8_gemm.cuh
> ~/GitHub/DeepGEMM/deep_gemm/include/deep_gemm/mma_utils.cuh
> ~/GitHub/DeepGEMM/deep_gemm/include/deep_gemm/tma_utils.cuh
> ~/GitHub/DeepGEMM/deep_gemm/jit/compiler.py
> ~/GitHub/DeepGEMM/deep_gemm/jit_kernels/gemm.py

Then install. The recommended python server.py install didn't work, but the much simpler pip install did, though perhaps this is connected to later problems with test_core.py: 

```
cd ~/GitHub/DeepGEMM
pip install .
```

Next, run tests. Right now test_jit.py works: 
```
cd ~/GitHub/DeepGEMM/tests
:~/GitHub/DeepGEMM/tests$ python test_jit.py
NVCC compiler: ('/usr/local/cuda-12.6/bin/nvcc', '12.6')

Generated code:
// DeepGEMM auto-generated JIT CUDA source file

#include <cuda.h>
#include <cuda_fp8.h>
#include <cuda_runtime.h>
#include <iostream>

#include "cutlass/cutlass.h"

extern "C" void launch(void* __raw_lhs, void* __raw_rhs, void* __raw_scale, void* __raw_out, bool enable_double_streams, void* __raw_stream, int& __return_code) {
    // Cast raw types (if needed)
    auto lhs = reinterpret_cast<__nv_fp8_e4m3*>(__raw_lhs);
    auto rhs = reinterpret_cast<__nv_fp8_e4m3*>(__raw_rhs);
    auto scale = reinterpret_cast<float*>(__raw_scale);
    auto out = reinterpret_cast<__nv_bfloat16*>(__raw_out);
    auto stream = reinterpret_cast<cudaStream_t>(__raw_stream);

    std::cout << reinterpret_cast<uint64_t>(lhs) << std::endl;
    std::cout << reinterpret_cast<uint64_t>(rhs) << std::endl;
    std::cout << reinterpret_cast<uint64_t>(scale) << std::endl;
    std::cout << reinterpret_cast<uint64_t>(out) << std::endl;
    std::cout << enable_double_streams << std::endl;
    std::cout << reinterpret_cast<uint64_t>(stream) << std::endl;
}


Building ...
Running ...
JIT test passed
```
But test_core.py fails: 

```
python test_core.py
Library path:
 > ['~/.local/lib/python3.11/site-packages/deep_gemm']

Testing GEMM:
In file included from ~/.deep_gemm/cache/kernel.gemm_fp8_fp8_bf16_nt.70b5a94ce876/kernel.cu:9:
~/.local/lib/python3.11/site-packages/deep_gemm/jit/../include/deep_gemm/fp8_gemm.cuh:8:10: fatal error: cute/arch/cluster_sm89.hpp: No such file or directory
    8 | #include <cute/arch/cluster_sm89.hpp>
      |          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~
compilation terminated.
Traceback (most recent call last):
  File "~/GitHub/DeepGEMM/tests/test_core.py", line 156, in <module>
    test_gemm()
  File "~/GitHub/DeepGEMM/tests/test_core.py", line 70, in test_gemm
    deep_gemm.gemm_fp8_fp8_bf16_nt(x_fp8, y_fp8, out)
  File "~.local/lib/python3.11/site-packages/deep_gemm/jit_kernels/gemm.py", line 156, in gemm_fp8_fp8_bf16_nt
    runtime = jit_tuner.compile_and_tune(
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~/.local/lib/python3.11/site-packages/deep_gemm/jit_kernels/tuner.py", line 40, in compile_and_tune
    kernels.append((build(name, arg_defs, code), tuned_keys))
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "~/.local/lib/python3.11/site-packages/deep_gemm/jit/compiler.py", line 139, in build
    return_code = subprocess.check_call(command)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.11/subprocess.py", line 413, in check_call
    raise CalledProcessError(retcode, cmd)
subprocess.CalledProcessError: Command '['/usr/local/cuda-12.6/bin/nvcc', '~/.deep_gemm/cache/kernel.gemm_fp8_fp8_bf16_nt.70b5a94ce876/kernel.cu', '-o', '~/.deep_gemm/tmp/nvcc.tmp.003194d1-f5d3-4a66-a54c-866bb24b6506.fe7708dc26e3.so', '-std=c++17', '-shared', '-O3', '--expt-relaxed-constexpr', '--expt-extended-lambda', '-gencode=arch=compute_89,code=sm_89', '--ptxas-options=--register-usage-level=10', '--diag-suppress=177,174,940', '--compiler-options=-fPIC,-O3,-Wno-deprecated-declarations,-Wno-abi', '-I~/.local/lib/python3.11/site-packages/deep_gemm/jit/../include']' returned non-zero exit status 1.
```

This is because it looks like cutlass doesn't compile a cluster_sm89.hpp file similar to a cluster_sm90.hpp file, presumably because these GPUs aren't intended to be server workhorses. So it is possible that cluster won't work. But it might be possible to split the test file to see if it runs on a single GPU. Working on that next. For now, just encouraged that jit still works. 

My hope, which I'm pursuing right now, is that I've got to rebuild their version of cutlass for sm_89, and that these files just need to be compiled. So exploring ways to do that, and will report progress, if any. 

### leedrake5 · 2025-03-04

An update on my end, and possibly fatal block. In [fp8_gemm.cuh](https://github.com/deepseek-ai/DeepGEMM/blob/main/deep_gemm/include/deep_gemm/fp8_gemm.cuh), the following libraries must be included: 

```
#include <cute/arch/cluster_sm90.hpp>
#include <cute/arch/copy_sm90_desc.hpp>
#include <cute/arch/copy_sm90_tma.hpp>
```
Now, for Ada Lovelace in particular, one can link the sm80 versions of files. But after re-compiling cutlass, I don't think there are instructions to build sm_80/sm_89 versions. They are specific to sm_90 and sm_100. So unless a way can be found away this, I think we're stuck. 

### galileilei · 2025-03-17

From a cursory look, only cluster = (1, 2) is used in the cuda file.

If cluster = 1, is it equivalent to running without TMA cluster on sm_80/sm_89?

### ZhangChuann · 2025-03-24

Has anyone successfully run on the sm_89 platform?

### engineer1109 · 2025-03-25

 Ada Lovelace doesn't support TMA.

### leedrake5 · 2025-03-26

@engineer1109 Would lack of support of TMA preclude running Deep GEMM on sm_80/sm_89?

### sshkhr · 2025-04-24

@leedrake5 It wouldn't necessarily preclude it, but you cannot use the library in its current form. For example, you won't be able to use the `cute::SM90_TMA_LOAD_2D::copy` or `cute::SM90_TMA_LOAD_MULTICAST_2D::copy` anymore. So you will have re-write the async matrix copying instructions between global and shared memory using the operations implemented here instead [cute/arch/copy_sm80.hpp](https://github.com/NVIDIA/cutlass/blob/main/include/cute/arch/copy_sm80.hpp). These will be via `LoadGlobalStoreShared` which are not directly from DRAM to SMEM, instead have to use registers. So these operations will be slower - see this image from [NVIDIA Hopper Architecture In-Depth](https://developer.nvidia.com/blog/nvidia-hopper-architecture-in-depth/). 

![Hopper vs Ada](https://developer-blogs.nvidia.com/wp-content/uploads/2022/03/Asynchronous-Memory-Copy-with-TMA-on-H100-vs-LDGSTS-Instruction-on-A100.jpg)

Similarly there are other SM90 specific instructions used elsewhere which you will have to replace.

### celsowm · 2025-06-24

Any updates? I am trying to use fp8 model on sglang on a 5090 but deepgemm still not compatible with sm120 :(

### LugerW-A · 2025-07-14

Any update for Ada?

### lucifer1004 · 2025-07-14

For those interested in Ada DeepGEMM, you may refer to https://github.com/NVIDIA/TensorRT-LLM/tree/main/cpp/tensorrt_llm/kernels/cutlass_kernels/fp8_blockscale_gemm/ada_blockwise_gemm
