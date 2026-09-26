# [Issue #46] Error in building SwiftTransformers (error: more than one conversion function from "half" to a built-in type applies) 

source: https://github.com/LLMServe/DistServe/issues/46
state: open | updated: 2024-10-24T07:16:28Z
labels: 

## 正文

Hi all. I encountered some problems when building SwiftTransforemer as the dependency for DistServer.
My GPU is 4090
nvcc: NVIDIA(R)Cuda compiler driver
Copyright(c)2005-2023 NVIDIA corporation
Built on Tue Feb 7 19:32:13 PST 2023
Cuda compilation tools, release 12.1, V12.1.66
Build cuda 12.1.r12.1/compiler.32415258_0

I would like to ask you if you have encountered the following error:

/home/infer/DistServe/SwiftTransformer/src/csrc/kernel/fused_decoding_stage_attention.cu(213): error: more than one conversion function from "half" to a built-in type applies:
function "__half::operator float() const" (declared at line 217 of /home/infer/anaconda/anaconda3/envs/Distserve/include/cuda_fp16.hpp)
function "__half::operator short() const" (declared at line 235 of /home/infer/anaconda/anaconda3/envs/Distserve/include/cuda_fp16.hpp)
function "__half::operator unsigned short() const" (declared at line 238 of /home/infer/anaconda/anaconda3/envs/Distserve/include/cuda_fp16.hpp)
function "__half::operator int() const" (declared at line 241 of /home/infer/anaconda/anaconda3/envs/Distserve/include/cuda_fp16.hpp)
function "__half::operator unsigned int() const" (declared at line 244 of /home/infer/anaconda/anaconda3/envs/Distserve/include/cuda_fp16.hpp)
function "__half::operator long long() const" (declared at line 247 of /home/infer/anaconda/anaconda3/envs/Distserve/include/cuda_fp16.hpp)
function "__half::operator unsigned long long() const" (declared at line 250 of /home/infer/anaconda/anaconda3/envs/Distserve/include/cuda_fp16.hpp)
function "__half::operator __nv_bool() const" (declared at line 254 of /home/infer/anaconda/anaconda3/envs/Distserve/include/cuda_fp16.hpp)
cur_result += (float)((T)attn_score[q_head_index][block_size_index] * v_block[block_size_index][hd_index]);
^
detected during:
instantiation of "void st::kernel::fusedDecodingStageAttentionKernel<T,Q_HEADS_PER_THREAD_BLOCK,HEAD_DIM,BLOCK_SIZE,THREAD_BLOCK_SIZE>(T *, const T *, T *, T *, float, const int64_t *, const int64_t *, const int64_t *, const int64_t *, int64_t, int64_t, int64_t) [with T=half, Q_HEADS_PER_THREAD_BLOCK=2L, HEAD_DIM=80L, BLOCK_SIZE=1L, THREAD_BLOCK_SIZE=256L]" at line 322
instantiation of "void st::kernel::fusedDecodingStageAttention(T *, const T *, T *, T *, float, const int64_t *, const int64_t *, int64_t, const int64_t *, const int64_t *, int64_t, int64_t, int64_t, int64_t, int64_t, int64_t, int64_t, int64_t) [with T=half]" at line 348

Error limit reached.
100 errors detected in the compilation of "/home/infer/DistServe/SwiftTransformer/src/csrc/kernel/fused_decoding_stage_attention.cu".
Compilation terminated.
make[2]: *** [src/csrc/kernel/CMakeFiles/kernel.dir/build.make:174: src/csrc/kernel/CMakeFiles/kernel.dir/fused_decoding_stage_attention.cu.o] Error 1
make[2]: *** [src/csrc/kernel/CMakeFiles/kernel.dir/build.make:160: src/csrc/kernel/CMakeFiles/kernel.dir/fused_context_stage_attention.cu.o] Error 1
[ 56%] Linking CXX static library ../../../lib/libgtest.a
[ 56%] Built target gtest
[ 57%] Building CXX object _deps/googletest-build/googletest/CMakeFiles/gtest_main.dir/src/gtest_main.cc.o
[ 58%] Building CXX object _deps/googletest-build/googlemock/CMakeFiles/gmock.dir/src/gmock-all.cc.o
[ 59%] Linking CXX static library ../../../lib/libgtest_main.a
[ 59%] Built target gtest_main
[ 60%] Building CXX object src/unittest/util/CMakeFiles/unittest_util.dir/cublas_wrapper.cc.o
[ 60%] Linking CXX static library ../../../lib/libgmock.a
[ 60%] Built target gmock
[ 61%] Building CXX object _deps/googletest-build/googlemock/CMakeFiles/gmock_main.dir/src/gmock_main.cc.o
[ 62%] Linking CXX executable ../../../bin/unittest_util
[ 62%] Built target unittest_util
[ 63%] Linking CXX static library ../../../lib/libgmock_main.a
[ 63%] Built target gmock_main
[ 64%] Linking CUDA device code CMakeFiles/py_nccl_utils.dir/cmake_device_link.o
[ 65%] Linking CXX static library libpy_nccl_utils.a
[ 65%] Built target py_nccl_utils
[ 66%] Linking CXX static library libpy_swapping.a
[ 66%] Built target py_swapping
[ 66%] Linking CXX static library libpy_block_migration.a
[ 66%] Built target py_block_migration
make[1]: *** [CMakeFiles/Makefile2:610: src/csrc/kernel/CMakeFiles/kernel.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
^Cnvcc error : 'cicc' died due to signal 2
make[2]: *** [src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/build.make:202: src/csrc/kernel/CMakeFiles/xformers_autogen_impl.dir/xformers/xformers/csrc/attention/cuda/fmha/autogen/impl/cutlassB_f16_aligned_k128.cu.o] Error 2
![1](https://github.com/user-attachments/assets/9f0c0298-2ab8-4a1a-88ee-03c767c8c1a9)


## 评论 (3)

### hyuenmin-choi · 2024-10-15

did you resolve this problem?? I'm also struggling with that error too...


### tyuechen · 2024-10-24

Hi have you solved this question? we also encounter this one...

### tyuechen · 2024-10-24

solved. refer to https://github.com/LLMServe/DistServe/issues/21
