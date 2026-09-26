# [Issue #37] 编译SwiftTransformer失败

source: https://github.com/LLMServe/DistServe/issues/37
state: open | updated: 2024-08-13T11:17:25Z
labels: 

## 正文

**执行命令：**
                    git clone https://github.com/LLMServe/SwiftTransformer.git cd SwiftTransformergit；submodule update --init --recursive；cmake -B build；cmake --build build -j$(nproc)

**报错原因：**
                    (截取部分具有代表性的错误)
                   /workspace/DistServe/SwiftTransformer/src/unittest/util/../unittest_utils.h:93:45: error: call of overloaded ‘fabs(__half)’ is ambiguous
                      93 |                                         fabs(answer[i]-reference[i]), fabs(answer[i]-reference[i])/fabs(reference[i]));
                         |                                         ~~~~^~~~~~~~~~~~~~~~~~~~~~~~
                  /workspace/DistServe/SwiftTransformer/src/unittest/util/../unittest_utils.h:93:75: error: call of overloaded ‘fabs(__half)’ is ambiguous
                     93 |                                         fabs(answer[i]-reference[i]), fabs(answer[i]-reference[i])/fabs(reference[i]));
                        |                                                                       ~~~~^~~~~~~~~~~~~~~~~~~~~~~~
                /workspace/DistServe/SwiftTransformer/src/csrc/kernel/fused_context_stage_attention.cu(145): error: name followed by "::" must be a class or namespace name
                   wmma::fragment<wmma::matrix_a, 16ul, 16ul, 16ul, __half, wmma::row_major> a_frag;
                                                                                                                        ^
              /workspace/DistServe/SwiftTransformer/src/csrc/kernel/fused_context_stage_attention.cu(146): error: type name is not allowed
                 wmma::fragment<wmma::matrix_b, 16ul, 16ul, 16ul, __half, wmma::col_major> b_frag;
                                                                                                          ^
            /workspace/DistServe/SwiftTransformer/src/csrc/kernel/fused_context_stage_attention.cu(146): error: identifier "b_frag" is undefined
               wmma::fragment<wmma::matrix_b, 16ul, 16ul, 16ul, __half, wmma::col_major> b_frag;
                                                                                         ^
**编译环境**
nvcr.io/nvidia/pytorch/23.10-py3镜像
CXX compiler: GNU 11.4.0
CUDA: NVIDIA 12.2.140
CUDAToolkit: 12.2.140
NCCL: libnccl.so.2.19.3
MPI: 3.1  

## 评论 (5)

### duihuhu · 2024-08-09

is it version problem?

### interestingLSY · 2024-08-12

Have you added the `--gpus=all` argument when you launch the docker container, or equivalently, can you see your GPUs when you type `nvidia-smi` **inside** your docker container?

### FredHuang99 · 2024-08-13

> Have you added the `--gpus=all` argument when you launch the docker container, or equivalently, can you see your GPUs when you type `nvidia-smi` **inside** your docker container?

i have added --gpus all

### William12github · 2024-08-13

what's the GPU type in the system?

### TZHelloWorld · 2024-08-13

maybe you can execute ` submodule update --init --recursive；`  to make sure that submodule installs all the sub-modules.
