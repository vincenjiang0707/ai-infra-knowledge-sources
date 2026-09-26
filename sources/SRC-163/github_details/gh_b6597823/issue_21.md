# [Issue #21] SwitfTransformer compilation fails with ambiguous conversion error at PyTorch 24.05 container.

source: https://github.com/LLMServe/DistServe/issues/21
state: closed | updated: 2025-05-21T06:14:41Z
labels: 

## 正文

SwitfTransformer compilation fails with ambiguous conversion error function from "const half" to a built-in type applies in `count_nan.cu`:

```
csrc/kernel/count_nan.cu(14): error: more than one conversion function from "const half" to a built-in type applies
```

## Reproducing the error


Start docker container with PyTorch 24.05

```
docker run -ti nvcr.io/nvidia/pytorch:24.05-py3 bash
```

Install miniconda3:

```
mkdir -p ~/miniconda3 && \
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh && \
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
```

Activate conda environment:

```
source ~/miniconda3/bin/activate
```

Clone, install and activate DistServe:

```
git clone https://github.com/LLMServe/DistServe.git && \
    cd DistServe && \
    conda env create -f environment.yml && conda activate distserve
```

Clone SwiftTransformer and compile:

```
git clone https://github.com/LLMServe/SwiftTransformer.git && \
    cd SwiftTransformer && \
    git submodule update --init --recursive && \
    cmake -B build && \
    cmake --build build -j$(nproc)
```


## Compilation log

```
-- The CXX compiler identification is GNU 11.4.0
-- The CUDA compiler identification is NVIDIA 12.1.66
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Check for working CXX compiler: /usr/bin/c++ - skipped
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Detecting CUDA compiler ABI info
-- Detecting CUDA compiler ABI info - done
-- Check for working CUDA compiler: /root/miniconda3/envs/distserve/bin/nvcc - skipped
-- Detecting CUDA compile features
-- Detecting CUDA compile features - done
-- Found CUDAToolkit: /root/miniconda3/envs/distserve/include (found suitable version "12.1.66", minimum required is "11.4")
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
No build type selected, defaulting to RELEASE mode
Use -DBUILD_MODE=DEBUG or -DBUILD_MODE=RELEASE to specify build type
Building in release mode
Building with MPI and NCCL
-- Found NCCL: /usr/include
-- Determining NCCL version from /usr/include/nccl.h...
-- Looking for NCCL_VERSION_CODE
-- Looking for NCCL_VERSION_CODE - not found
-- Found NCCL (include: /usr/include, library: /usr/lib/x86_64-linux-gnu/libnccl.so.2.21.5)
-- Found MPI_CXX: /opt/hpcx/ompi/lib/libmpi.so (found version "3.1")
-- Found MPI: TRUE (found version "3.1")
-- Found CUDA: /root/miniconda3/envs/distserve (found version "12.1") 
-- Found CUDAToolkit: /root/miniconda3/envs/distserve/include (found version "12.1.66")
-- Caffe2: CUDA detected: 12.1
-- Caffe2: CUDA nvcc is: /root/miniconda3/envs/distserve/bin/nvcc
-- Caffe2: CUDA toolkit directory: /root/miniconda3/envs/distserve
-- Caffe2: Header version is: 12.1
-- /root/miniconda3/envs/distserve/lib/stubs/libnvrtc.so shorthash is 0ced1d3e
-- Found CUDNN: /usr/lib/x86_64-linux-gnu/libcudnn.so
-- USE_CUSPARSELT is set to 0. Compiling without cuSPARSELt support
CMake Warning at /root/miniconda3/envs/distserve/lib/python3.10/site-packages/torch/share/cmake/Caffe2/public/utils.cmake:385 (message):
  In the future we will require one to explicitly pass TORCH_CUDA_ARCH_LIST
  to cmake instead of implicitly setting it as an env variable.  This will
  become a FATAL_ERROR in future version of pytorch.
Call Stack (most recent call first):
  /root/miniconda3/envs/distserve/lib/python3.10/site-packages/torch/share/cmake/Caffe2/public/cuda.cmake:342 (torch_cuda_get_nvcc_gencode_flag)
  /root/miniconda3/envs/distserve/lib/python3.10/site-packages/torch/share/cmake/Caffe2/Caffe2Config.cmake:87 (include)
  /root/miniconda3/envs/distserve/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:68 (find_package)
  CMakeLists.txt:100 (find_package)


-- Added CUDA NVCC flags for: -gencode;arch=compute_52,code=sm_52;-gencode;arch=compute_60,code=sm_60;-gencode;arch=compute_61,code=sm_61;-gencode;arch=compute_70,code=sm_70;-gencode;arch=compute_72,code=sm_72;-gencode;arch=compute_75,code=sm_75;-gencode;arch=compute_80,code=sm_80;-gencode;arch=compute_86,code=sm_86;-gencode;arch=compute_87,code=sm_87;-gencode;arch=compute_90,code=sm_90;-gencode;arch=compute_90,code=compute_90
CMake Warning at /root/miniconda3/envs/distserve/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:22 (message):
  static library kineto_LIBRARY-NOTFOUND not found.
Call Stack (most recent call first):
  /root/miniconda3/envs/distserve/lib/python3.10/site-packages/torch/share/cmake/Torch/TorchConfig.cmake:127 (append_torchlib_if_found)
  CMakeLists.txt:100 (find_package)


-- Found Torch: /root/miniconda3/envs/distserve/lib/python3.10/site-packages/torch/lib/libtorch.so
-- USE_CXX11_ABI=False
-- The C compiler identification is GNU 11.4.0
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Check for working C compiler: /usr/bin/cc - skipped
-- Detecting C compile features
-- Detecting C compile features - done
-- Found Python: /root/miniconda3/envs/distserve/bin/python3.10 (found version "3.10.14") found components: Interpreter
CMake Warning (dev) at /usr/local/lib/python3.10/dist-packages/cmake/data/share/cmake-3.29/Modules/FetchContent.cmake:1352 (message):
  The DOWNLOAD_EXTRACT_TIMESTAMP option was not given and policy CMP0135 is
  not set.  The policy's OLD behavior will be used.  When using a URL
  download, the timestamps of extracted files should preferably be that of
  the time of extraction, otherwise code that depends on the extracted
  contents might not be rebuilt if the URL changes.  The OLD behavior
  preserves the timestamps from the archive instead, but this is usually not
  what you want.  Update your project to the NEW behavior or specify the
  DOWNLOAD_EXTRACT_TIMESTAMP option with a value of true to avoid this
  robustness issue.
Call Stack (most recent call first):
  CMakeLists.txt:139 (FetchContent_Declare)
This warning is for project developers.  Use -Wno-dev to suppress it.

CMake Deprecation Warning at build/_deps/json-src/CMakeLists.txt:1 (cmake_minimum_required):
  Compatibility with CMake < 3.5 will be removed from a future version of
  CMake.

  Update the VERSION argument <min> value or use a ...<max> suffix to tell
  CMake that the project does not need compatibility with older versions.


-- Using the multi-header code from /workspace/DistServe/DistServe/SwiftTransformer/build/_deps/json-src/include/
-- Configuring done (10.4s)
-- Generating done (0.1s)
-- Build files have been written to: /workspace/DistServe/DistServe/SwiftTransformer/build
[  1%] Building CXX object _deps/googletest-build/googletest/CMakeFiles/gtest.dir/src/gtest-all.cc.o
[  2%] Building CXX object src/csrc/util/CMakeFiles/util.dir/cublas_wrapper.cc.o
[  2%] Building CXX object src/csrc/util/CMakeFiles/nccl_utils.dir/nccl_utils.cc.o
[  3%] Building CXX object src/csrc/util/CMakeFiles/py_nccl_utils.dir/py_nccl.cc.o
[  4%] Building CXX object src/examples/CMakeFiles/st_args.dir/lib/st_args.cc.o
[  5%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k128.cu.o
[  6%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k128_dropout.cu.o
[  6%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k32_dropout.cu.o
[  7%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k32.cu.o
[  8%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k128.cu.o
[  9%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k128_dropout.cu.o
[  9%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k32.cu.o
[ 10%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k64.cu.o
[ 11%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k65536_dropout.cu.o
[ 11%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k64.cu.o
[ 12%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k96.cu.o
[ 13%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k65536.cu.o
[ 15%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_notaligned_k128_dropout.cu.o
[ 15%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k32_dropout.cu.o
[ 16%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_bf16_aligned_k64_dropout.cu.o
[ 17%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_notaligned_k128.cu.o
[ 18%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_notaligned_k32_dropout.cu.o
[ 18%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_notaligned_k32.cu.o
[ 19%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_notaligned_k65536_dropout.cu.o
[ 21%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k96.cu.o
[ 21%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k64_dropout.cu.o
[ 21%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k65536_dropout.cu.o
[ 22%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_aligned_k64_dropout.cu.o
[ 23%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_notaligned_k64_dropout.cu.o
[ 24%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_notaligned_k64.cu.o
[ 26%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_aligned_k128_dropout.cu.o
[ 26%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_aligned_k128.cu.o
[ 27%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_aligned_k32_dropout.cu.o
[ 28%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k65536.cu.o
[ 28%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_notaligned_k65536.cu.o
[ 29%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_notaligned_k128_dropout.cu.o
[ 29%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_aligned_k65536_dropout.cu.o
[ 30%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_notaligned_k32.cu.o
[ 31%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_notaligned_k128.cu.o
[ 32%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_aligned_k32.cu.o
[ 32%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_aligned_k65536.cu.o
[ 34%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_notaligned_k64.cu.o
[ 34%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_aligned_k64.cu.o
[ 35%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_notaligned_k65536.cu.o
[ 36%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_notaligned_k65536_dropout.cu.o
[ 36%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassF_bf16_aligned.cu.o
[ 38%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassF_f32_notaligned.cu.o
[ 38%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_notaligned_k64_dropout.cu.o
[ 38%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f32_notaligned_k32_dropout.cu.o
[ 39%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassF_f32_aligned.cu.o
[ 39%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassF_f16_notaligned.cu.o
[ 40%] Building CUDA object src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassF_f16_aligned.cu.o
[ 41%] Linking CUDA device code CMakeFiles/nccl_utils.dir/cmake_device_link.o
[ 41%] Linking CXX static library libutil.a
[ 41%] Built target util
[ 42%] Linking CXX static library libst_args.a
[ 43%] Building CXX object src/csrc/util/CMakeFiles/py_block_migration.dir/py_block_migration.cc.o
[ 43%] Building CXX object src/csrc/util/CMakeFiles/py_swapping.dir/py_swapping.cc.o
[ 43%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/count_nan.cu.o
[ 44%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/fused_decoding_stage_attention.cu.o
[ 45%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/addbias.cu.o
[ 45%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/fused_addbias_activ.cu.o
[ 45%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/softmax.cu.o
[ 46%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/embedding.cu.o
[ 47%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/gather_last_tokens.cu.o
[ 48%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/layernorm.cu.o
[ 49%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/fused_decoding_stage_attention_mha.cu.o
[ 50%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/rotary_posi_embedding.cu.o
[ 50%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/kvcache_mgmt.cu.o
[ 52%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/fused_activ_multiply.cu.o
[ 52%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/unfused_attention.cu.o
[ 54%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/findmax.cu.o
[ 54%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/fused_context_stage_attention.cu.o
[ 55%] Building CUDA object src/csrc/kernel/CMakeFiles/kernel.dir/rmsnorm.cu.o
[ 56%] Linking CXX static library libnccl_utils.a
[ 56%] Built target st_args
[ 56%] Built target nccl_utils
/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/count_nan.cu(14): error: more than one conversion function from "const half" to a built-in type applies:
            function "__half::operator float() const" (declared at line 217 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator short() const" (declared at line 235 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned short() const" (declared at line 238 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator int() const" (declared at line 241 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned int() const" (declared at line 244 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator long long() const" (declared at line 247 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned long long() const" (declared at line 250 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator __nv_bool() const" (declared at line 254 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
    if (arr[i] != arr[i]) {
        ^
          detected during:
            instantiation of "void st::kernel::countNanKernel(int *, const T *, int) [with T=half]" at line 31
            instantiation of "int st::kernel::countNan(const T *, int) [with T=half]" at line 43

/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/count_nan.cu(14): error: more than one conversion function from "const half" to a built-in type applies:
            function "__half::operator float() const" (declared at line 217 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator short() const" (declared at line 235 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned short() const" (declared at line 238 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator int() const" (declared at line 241 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned int() const" (declared at line 244 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator long long() const" (declared at line 247 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned long long() const" (declared at line 250 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator __nv_bool() const" (declared at line 254 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
    if (arr[i] != arr[i]) {
                  ^
          detected during:
            instantiation of "void st::kernel::countNanKernel(int *, const T *, int) [with T=half]" at line 31
            instantiation of "int st::kernel::countNan(const T *, int) [with T=half]" at line 43

2 errors detected in the compilation of "/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/count_nan.cu".
gmake[2]: *** [src/csrc/kernel/CMakeFiles/kernel.dir/build.make:92: src/csrc/kernel/CMakeFiles/kernel.dir/count_nan.cu.o] Error 1
gmake[2]: *** Waiting for unfinished jobs....
/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_decoding_stage_attention.cu(80): warning #177-D: variable "my_q_head_end" was declared but never referenced
   const int64_t my_q_head_end = (blockIdx.x+1)*Q_HEADS_PER_THREAD_BLOCK;
                 ^
          detected during instantiation of "void st::kernel::fusedDecodingStageAttention(T *, const T *, T *, T *, float, const int64_t *, const int64_t *, int64_t, const int64_t *, const int64_t *, int64_t, int64_t, int64_t, int64_t, int64_t, int64_t, int64_t, int64_t) [with T=float]" at line 347

Remark: The warnings can be suppressed with "-diag-suppress <warning-number>"

/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu(40): error: more than one conversion function from "__half" to a built-in type applies:
            function "__half::operator float() const" (declared at line 217 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator short() const" (declared at line 235 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned short() const" (declared at line 238 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator int() const" (declared at line 241 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned int() const" (declared at line 244 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator long long() const" (declared at line 247 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned long long() const" (declared at line 250 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator __nv_bool() const" (declared at line 254 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
     applyActivation<T, ACTIVATION_TYPE>(input_elem.x + bias_elem.x),
                                         ^
          detected during:
            instantiation of "void st::kernel::fusedAddbiasBatchedActivationKernel<T,ACTIVATION_TYPE>(T *, const T *, const T *, int64_t, int64_t) [with T=half, ACTIVATION_TYPE=st::kernel::ActivationType::RELU]" at line 62
            instantiation of "void st::kernel::fusedAddbiasBatchedActivation(T *, const T *, const T *, int64_t, int64_t, st::kernel::ActivationType) [with T=half]" at line 75

/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/embedding.cu(31): error: no operator "+=" matches these operands
            operand types are: half += const half
     cur_result += embed_positions_weight[my_position_id * hidden_size + hidden_size_index];
                ^
          detected during:
            instantiation of "void st::kernel::embedAndPosiEncodeBatchedKernel<T,DO_POSI_ENCODING>(T *, const int64_t *, const int64_t *, const T *, const T *, int64_t) [with T=half, DO_POSI_ENCODING=true]" at line 56
            instantiation of "void st::kernel::embedAndPosiEncodeBatched(T *, const int64_t *, const int64_t *, const T *, const T *, int64_t, int64_t) [with T=half]" at line 80

/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu(40): error: more than one conversion function from "__half" to a built-in type applies:
            function "__half::operator float() const" (declared at line 217 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator short() const" (declared at line 235 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned short() const" (declared at line 238 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator int() const" (declared at line 241 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned int() const" (declared at line 244 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator long long() const" (declared at line 247 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned long long() const" (declared at line 250 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator __nv_bool() const" (declared at line 254 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
     applyActivation<T, ACTIVATION_TYPE>(input_elem.x + bias_elem.x),
                                                        ^
          detected during:
            instantiation of "void st::kernel::fusedAddbiasBatchedActivationKernel<T,ACTIVATION_TYPE>(T *, const T *, const T *, int64_t, int64_t) [with T=half, ACTIVATION_TYPE=st::kernel::ActivationType::RELU]" at line 62
            instantiation of "void st::kernel::fusedAddbiasBatchedActivation(T *, const T *, const T *, int64_t, int64_t, st::kernel::ActivationType) [with T=half]" at line 75

/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/activations.cuh(13): error: more than one conversion function from "const half" to a built-in type applies:
            function "__half::operator float() const" (declared at line 217 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator short() const" (declared at line 235 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned short() const" (declared at line 238 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator int() const" (declared at line 241 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned int() const" (declared at line 244 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator long long() const" (declared at line 247 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned long long() const" (declared at line 250 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator __nv_bool() const" (declared at line 254 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
     return x > (T)0 ? x : (T)0;
            ^
          detected during:
            instantiation of "T st::kernel::applyActivation<T,activation_type>(const T &) [with T=half, activation_type=st::kernel::ActivationType::RELU]" at line 40 of /workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu
            instantiation of "void st::kernel::fusedAddbiasBatchedActivationKernel<T,ACTIVATION_TYPE>(T *, const T *, const T *, int64_t, int64_t) [with T=half, ACTIVATION_TYPE=st::kernel::ActivationType::RELU]" at line 62 of /workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu
            instantiation of "void st::kernel::fusedAddbiasBatchedActivation(T *, const T *, const T *, int64_t, int64_t, st::kernel::ActivationType) [with T=half]" at line 75 of /workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu

/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/activations.cuh(13): error: more than one conversion function from "half" to a built-in type applies:
            function "__half::operator float() const" (declared at line 217 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator short() const" (declared at line 235 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned short() const" (declared at line 238 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator int() const" (declared at line 241 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned int() const" (declared at line 244 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator long long() const" (declared at line 247 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned long long() const" (declared at line 250 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator __nv_bool() const" (declared at line 254 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
     return x > (T)0 ? x : (T)0;
                ^
          detected during:
            instantiation of "T st::kernel::applyActivation<T,activation_type>(const T &) [with T=half, activation_type=st::kernel::ActivationType::RELU]" at line 40 of /workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu
            instantiation of "void st::kernel::fusedAddbiasBatchedActivationKernel<T,ACTIVATION_TYPE>(T *, const T *, const T *, int64_t, int64_t) [with T=half, ACTIVATION_TYPE=st::kernel::ActivationType::RELU]" at line 62 of /workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu
            instantiation of "void st::kernel::fusedAddbiasBatchedActivation(T *, const T *, const T *, int64_t, int64_t, st::kernel::ActivationType) [with T=half]" at line 75 of /workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu

/workspace/DistServe/DistServe/SwiftTransformer/src/csrc/kernel/fused_addbias_activ.cu(41): error: more than one conversion function from "__half" to a built-in type applies:
            function "__half::operator float() const" (declared at line 217 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator short() const" (declared at line 235 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned short() const" (declared at line 238 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator int() const" (declared at line 241 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned int() const" (declared at line 244 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator long long() const" (declared at line 247 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator unsigned long long() const" (declared at line 250 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
            function "__half::operator __nv_bool() const" (declared at line 254 of /root/miniconda3/envs/distserve/include/cuda_fp16.hpp)
     applyActivation<T, ACTIVATION_TYPE>(input_elem.y + bias_elem.y)
                                         ^
          detected during:
            instantiation of "void st::kernel::fusedAddbiasBatchedActivationKernel<T,ACTIVATION_TYPE>(T *, const T *, const T *, int64_t, int64_t) [with T=half, ACTIVATION_TYPE=st::kernel::ActivationType::RELU]" at line 62
            instantiation of "void st::kernel::fusedAddbiasBatchedActivation(T *, const T *, const T *, int64_t, int64_t, st::kernel::ActivationType) [with T=half]" at line 75
```

## 评论 (3)

### irasin · 2024-07-08

NGC images will auto set `TORCH_CUDA_ARCH_LIST=5.2 6.0 6.1 7.0 7.2 7.5 8.0 8.6 8.7 9.0+PTX` and  half is not supported on SM52, you may need to to specify the TORCH_CUDA_ARCH_LIST env variable based on your gpu device before cmake, for example, `export TORCH_CUDA_ARCH_LIST=8.6` for A10 or `export TORCH_CUDA_ARCH_LIST=8.0` for A100

### piotrm-nvidia · 2024-07-08

I used range from 8.0 to 9.0 and compilation is successful:

```
export TORCH_CUDA_ARCH_LIST="8.0 8.6 8.7 9.0+PTX"
```

Thank you for explanation.

### YitaoYuan · 2025-05-21

Thanks. That works for me, too.
