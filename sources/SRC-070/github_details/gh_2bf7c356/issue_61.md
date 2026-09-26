# [Issue #61] Questions about Compute-Communication Overlap

source: https://github.com/deepseek-ai/DeepEP/issues/61
state: closed | updated: 2026-09-18T09:57:24Z
labels: 

## 正文

hello, experts. see from codebase, I have several questions:

- I think both `async_finish` and `return_recv_hook` can achieve `compute-communication overlap`, so what's the difference between them ?
- with `saync_finish` mode, communication use `comm_stream`, it's make sense. but why `return_recv_hook` mode use `compute_stream` for communication ?

thanks.

## 评论 (4)

### LyricZhao · 2025-03-10

They are two different ways to overlap:

- `async_finish`: using two CUDA streams to overlap, computation and communication kernels share all the SMs (e.g. internode kernels using 20 SMs, and GEMM on the computation uses 132 - 20 = 112 SMs)
- `return_recv_hook`: communication kernels does not use any SM, it just issue RDMA requests (as soon as possible, using more SMs, so just reuse the computation stream) and just return. The RDMA transmission is hid in the background.

For low-latency kernels, the `async_finish` is a legacy-style API which may not be used (to align with the inter/intra kernels), you can just ignore it. We have it, because when we didn't have the `return_recv_hook ` API, we used it for shared experts overlapping (which is much easier, communication uses 96 SMs, shared GEMM uses 132 - 96 = 36 SMs), now we don't use it anymore.

### chenhongyu2048 · 2025-04-21

> They are two different ways to overlap:
> 
> * `async_finish`: using two CUDA streams to overlap, computation and communication kernels share all the SMs (e.g. internode kernels using 20 SMs, and GEMM on the computation uses 132 - 20 = 112 SMs)
> * `return_recv_hook`: communication kernels does not use any SM, it just issue RDMA requests (as soon as possible, using more SMs, so just reuse the computation stream) and just return. The RDMA transmission is hid in the background.
> 
> For low-latency kernels, the `async_finish` is a legacy-style API which may not be used (to align with the inter/intra kernels), you can just ignore it. We have it, because when we didn't have the `return_recv_hook ` API, we used it for shared experts overlapping (which is much easier, communication uses 96 SMs, shared GEMM uses 132 - 96 = 36 SMs), now we don't use it anymore.

Hello, I would like to ask how to set the amount of SM used for gemm? Or do you think it's possible for me to find the answer in the DeepGEMM library? @LyricZhao Thanks for your reply!



### LyricZhao · 2025-04-22

- DeepGEMM: `deep_gemm.set_num_sms(math_sms)`
- cuBLAS: `CUBLAS_CHECK(cublasLtMatmulDescSetAttribute(desc, CUBLASLT_MATMUL_DESC_SM_COUNT_TARGET, &math_sms, sizeof(math_sms)));`

### chenhongyu2048 · 2025-04-22

> * DeepGEMM: `deep_gemm.set_num_sms(math_sms)`
> * cuBLAS: `CUBLAS_CHECK(cublasLtMatmulDescSetAttribute(desc, CUBLASLT_MATMUL_DESC_SM_COUNT_TARGET, &math_sms, sizeof(math_sms)));`

Thanks for your help!
