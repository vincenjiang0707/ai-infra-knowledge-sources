# [Issue #491] Question about eager rdma

source: https://github.com/deepseek-ai/DeepEP/issues/491
state: closed | updated: 2026-09-18T10:05:56Z
labels: 

## 正文

hello~ @Gaojiaqi  I’d like to ask some questions about eager rdma.

1. what is the purpose of the flag "CU_POINTER_ATTRIBUTE_SYNC_MEMOPS". I understand that it only affects the asynchronous behavior of cudaMemcpy, is it right? In nvshmem, the static heap and qp control object uses this flag, but the default dynamic heap does not.
2. I see that the tag only uses 4 bytes out of the 16 bytes allocated. Why was a 16-byte space designed for it?
thx~


## 评论 (3)

### Gaojiaqi · 2025-12-07

Hi @Thunderbrook, 

1. After double check the setting, CU_POINTER_ATTRIBUTE_SYNC_MEMOPS is indeed not enabled on dynamic heap during our internal pressure-testing, so it is not necessary (or potential data race still exist but with really low chance).
2. 16-byte tag is for int4 alignments, it has the minimal impact to the current dispatch pipeline.

### Thunderbrook · 2025-12-17

@Gaojiaqi thanks for reply~, but i wonder where exactly does the data race mentioned here occur? And how CU_POINTER_ATTRIBUTE_SYNC_MEMOPS solve the data race, thx~

### Gaojiaqi · 2026-01-08

Hey, the data race we meant was the DMA writing from the NIC to the GPU. When an RDMA packet arrives, for example with 4k MTU, the data is split into muliple writes from the NIC to the GPU memory. We were worried the mulitple writes were not in order, since the tag is only in the last write (at the tail of the 4096 bytes). We might experience correctness issue if reorder happens between the GPU and the NIC. That's why we disabled NVSHMEM_IB_ENABLE_RELAXED_ORDERING. CU_POINTER_ATTRIBUTE_SYNC_MEMOPS is irrelevant this problem.
