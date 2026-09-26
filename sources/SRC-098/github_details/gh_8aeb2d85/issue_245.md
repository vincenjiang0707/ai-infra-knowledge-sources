# [Issue #245] What does dma_buf do when gpuDirectRdma is disabled ?

source: https://github.com/NVIDIA/nccl-tests/issues/245
state: open | updated: 2025-04-03T12:19:35Z
labels: 

## 正文

Running nccl test with 2 nodes with one A10G on each node with GDR disabled. 
Why do I see the following line in the logs "DMA-BUF is available on GPU device 0". Will DMA_BUF be used when GDR is disabled ?
Appreciate the help !

```
 [0] NCCL INFO NET/OFI Could not disable CUDA API usage for HMEM, disabling GDR
 [0] NCCL INFO NET/OFI Setting NCCL_PROTO to "simple"
[0] NCCL INFO NET/OFI Could not disable CUDA API usage for HMEM, disabling GDR
[0] NCCL INFO NET/OFI Setting NCCL_PROTO to "simple"
[0] NCCL INFO DMA-BUF is available on GPU device 0
[0] NCCL INFO DMA-BUF is available on GPU device 0
[0] NCCL INFO comm 0x2515e00 rank 0 nranks 2 cudaDev 0 nvmlDev 0 busId 1e0 commId 0x1c71981584deedae - Init START
[0] NCCL INFO comm 0x2b049f0 rank 1 nranks 2 cudaDev 0 nvmlDev 0 busId 1e0 commId 0x1c71981584deedae - Init START
[0] NCCL INFO NET/OFI Libfabric provider associates MRs with domains
[0] NCCL INFO NET/OFI Libfabric provider associates MRs with domains
[0] NCCL INFO Channel 00/02 :    0   1
[0] NCCL INFO Channel 01/02 :    0   1
```

## 评论 (2)

### kiskra-nvidia · 2024-08-05

It's a generic test that's always done during initialization, irrespective of the communication layer used or its configuration.

### alokprasad · 2025-04-03

NCCL Logs should include what exactly it is using GDR or DMA-BUF or none.

