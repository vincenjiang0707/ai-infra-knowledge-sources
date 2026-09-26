# [Issue #358] [Proposal] Integrate some enhancements from TensorRT-LLM

source: https://github.com/deepseek-ai/DeepEP/issues/358
state: open | updated: 2026-09-19T09:25:56Z
labels: 

## 正文

Hi, DeepEP team,

I'm a collaborator to the TensorRT-LLM project. First, thank you for creating such a performant library. We have successfully integrated it into our project. To better align with TensorRT-LLM's data format, we've made a few modifications to DeepEP. The specific commit we are using is [515a311](https://github.com/deepseek-ai/DeepEP/commits/515a311f290eb6d9592fcccfcc80c40f5123ca72/). The main changes are as follows:

(1) Besides `torch.distributed.ProcessGroup`, support for initializing buffers with `mpi4py.MPI.Comm` ( @yuantailing )
(2) Change the dtype of `topk_idx` from `int64_t` to `int` and add an offset to expert id  ( @yifeizhang-c )
(3) Avoid cleaning after each change in hidden_size/token_num (Already merged in #313, @yilin-void )
(4) Add an FP4 low-latency dispatch kernel, where the tensor is quantized outside of the kernel ( @yilin-void )
(5) Add an FP4 low-latency combine kernel, where the tensor is quant/dequant inside of the kernel ( @yilin-void )

**Before we create pull requests, we would like to discuss whether the community would be open to these changes and how we can make them more general, especially for (2), (4), and (5).**

For point (2), our proposal is to add a conditional type definition, such as `using topk_idx_t = int64_t` or `int` which depends on a macro.
For point (4), the FP4 dispatch is currently a separate kernel, but we could merge it into the original dispatch kernel by adding an input tensor to indicate that the scale is quantized outside of the kernel.
For point (5), the FP4 combine is currently a separate kernel, but we could merge it into the original dispatch kernel by adding an template argument to indicate whether quant/dequant should be performance before/after the communication.

We hope these contributions will broaden DeepEP's applications and allow us to stay aligned with the main branch of your library.

Thanks
Tailing


## 评论 (3)

### sphish · 2025-08-15

Thank you for your proposal! 

For (1) and (2), we are happy to merge these changes. 

Regarding the FP4 kernels, we haven’t yet found a way to use FP4 for data transfer without losing model performance, so we’re still unsure about the best approach moving forward. However, I think we can maintain an FP4 branch in the DeepEP repo to facilitate further exploration around FP4. If it's convenient, feel free to add me on WeChat (ID: Sphizzz) for further discussion.

### yuantailing · 2025-09-30

Added
(6) Support CUDA Graph for internode dispatch normal kernel (@yifeizhang-c )

### 0z5a · 2026-09-19

Hi, I’d be happy to take a narrow follow-up for the MPI initialization path on hybrid-ep. @yuantailing @sphish 

I already have #730 on main, where I worked on communicator-aware topology/preflight handling and multi-rank failure propagation.
