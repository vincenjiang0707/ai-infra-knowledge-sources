# [Issue #63] Why the round_size in NPUcachingAllocator.cpp adds 32?

source: https://github.com/Ascend/pytorch/issues/63
state: open | updated: 2025-07-04T01:39:52Z
labels: 

## 正文

same as the title, following is the code segement.
https://github.com/Ascend/pytorch/blob/c402d601b63e690dbf6889eb83d6c66de46ca232/torch_npu/csrc/core/npu/NPUCachingAllocator.cpp#L1640
```C++  
    static size_t round_size(size_t size)
    {
        size = size + 32;
        if (size < kMinBlockSize) {
            return kMinBlockSize;
        } else {
            return kMinBlockSize * ((size + kMinBlockSize - 1) / kMinBlockSize);
        }
    }
```

## 评论 (1)

### yunyiyun · 2025-07-04

考虑软件栈之间的兼容性
