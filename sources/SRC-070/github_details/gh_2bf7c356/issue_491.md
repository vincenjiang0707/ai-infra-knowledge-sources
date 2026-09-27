# [Issue #491] Question about eager rdma

source: https://github.com/deepseek-ai/DeepEP/issues/491
state: closed | updated: 2026-09-18T10:05:56Z
labels: 

## 正文

hello~ @Gaojiaqi  I’d like to ask some questions about eager rdma.

1. what is the purpose of the flag "CU_POINTER_ATTRIBUTE_SYNC_MEMOPS". I understand that it only affects the asynchronous behavior of cudaMemcpy, is it right? In nvshmem, the static heap and qp control object uses this flag, but the default dynamic heap does not.
2. I see that the tag only uses 4 bytes out of the 16 bytes allocated. Why was a 16-byte space designed for it?
thx~


## 评论 (0)
