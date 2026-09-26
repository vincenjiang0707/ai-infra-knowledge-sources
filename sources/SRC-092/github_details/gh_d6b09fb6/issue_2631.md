# [Issue #2631] [Usage]: NoF write/read requires strict block-size alignment but neither allocators nor value_size guarantee it — is this by design?

source: https://github.com/kvcache-ai/Mooncake/issues/2631
state: open | updated: 2026-09-25T03:14:18Z
labels: stale

## 正文

### Describe your usage question

### Description
While investigating the NoF (NVMe-oF) replica path, I found that submitSpdkNofOperation enforces strict block-size alignment on three dimensions, but none of them appear to be guaranteed by the current codebase. I'd like to understand whether this is an intentional design constraint (e.g., only uniform block-size KVCache workloads are supported) or a gap to be addressed.

### The Alignment Check
In mooncake-store/src/transfer_task.cpp (lines 1280-1288), the function performs a hard alignment check before submitting any SPDK I/O:
```cpp
uint32_t block_size = SpdkWrapper::GetInstance().GetBlockSize(seg_handle);
if (block_size == INVALID_BLOCK_SIZE ||
    handle.buffer_address_ % block_size != 0 ||   // ① NVMe offset
    size % block_size != 0 ||                      // ② data size
    reinterpret_cast<std::uintptr_t>(ptr) % block_size != 0) {  // ③ memory ptr
    LOG(ERROR) << "NoF request offset=" << handle.buffer_address_
               << ", ptr=" << ptr << ", size=" << size
               << " is not aligned to block size " << block_size;
    return std::nullopt;  // fails silently, no padding
}
```
If any check fails, the operation returns std::nullopt with no padding or retry mechanism.


### Why None of the Three Checks Are Guaranteed

① buffer_address_ — NVMe offset from Master-side allocator
The NoF segment's buffer_address_ is produced by either CachelibBufferAllocator or OffsetBufferAllocator (selected via config.memory_allocator):
CachelibBufferAllocator: Slab base is 16MB-aligned (✅ for 4096), but individual allocations within a slab use CacheLib allocation class sizes (e.g., 64, 80, 96...), which are not necessarily multiples of block_size.
OffsetBufferAllocator: Uses multiplier_bits to scale offsets. For typical segment sizes (e.g., 64GB → multiplier_bits=5 → 32-byte granularity), the allocated offset is not guaranteed to be block-aligned.

② size — User's value_length, passed through without padding
The user's value_length flows directly from mc.put(key, value, value_length) → master_service.cpp (Allocate(..., value_length, ...)) → AllocatedBuffer(size=value_length) → submitSpdkNofOperation(handle, ptr, size, ...).No rounding or padding is applied at any layer. If value_length is, say, 3000 bytes with block_size=4096, the size % block_size != 0 check fails.Note: CachelibBufferAllocator::allocate does use padding_size = std::max(size, kMinSliceSize) for the actual allocation, but the AllocatedBuffer::size_ field still records the original requested size, which is what gets checked.

③ ptr — Client-side DMA buffer from ClientBufferAllocator
In real_client.cpp, when USE_NOF is defined, the client buffer allocator is created with use_spdk_dma=true:
```cpp
// real_client.cpp:746-752
bool use_spdk_dma_for_client_buffer = false;
#ifdef USE_NOF
use_spdk_dma_for_client_buffer = true;
#endif
client_buffer_allocator_ = ClientBufferAllocator::create(
    local_buffer_size, this->protocol, should_use_hugepage,
    use_spdk_dma_for_client_buffer);
```
Inside ClientBufferAllocator (client_buffer.cpp:42):
```cpp
constexpr size_t alignment = 64;  // hardcoded 64-byte alignment
buffer_ = allocate_buffer_allocator_memory(size, protocol, 64, use_spdk_dma_);
// → SpdkWrapper::Alloc(size, 64, -1)
// → spdk_zmalloc(size, 64, ..., SPDK_MALLOC_DMA)
```
The DMA base is only 64-byte aligned, not 4096-byte aligned. The OffsetAllocator inside ClientBufferAllocator also doesn't add any block-alignment guarantee (for typical local_buffer_size < 3.75GB, multiplier_bits=0, meaning 1-byte granularity).In practice, the e2e test passes because spdk_zmalloc for large allocations typically returns hugepage-backed memory (2MB-aligned), which happens to be 4096-aligned. But this is an SPDK implementation detail, not a code-level guarantee.

### Questions
1. Is this alignment-only design intentional? Is NoF replica currently meant only for uniform block-size workloads (e.g., vLLM fixed-size KVCache pages)?
2. Are there plans to support arbitrary value sizes? For example:
Padding size up to block_size boundary in submitSpdkNofOperation (write padded zeros, truncate on read)
Enforcing block-aligned allocation in the Master-side allocators for NOF_SSD replica type
Increasing ClientBufferAllocator alignment from 64 to at least block_size (4096)
3. Should the error be more explicit? Currently the failure is a LOG(ERROR) + return std::nullopt, which could be confusing to debug. Would a dedicated error code (e.g., NOT_ALIGNED) be appropriate?


### Before submitting a new issue...

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)

## 评论 (5)

### github-actions[bot] · 2026-06-26

Thanks for opening this issue, @mzygQAQ!

| Field | Value |
|-------|-------|
| **Issue** | #2631 |
| **GitHub user ID** | `30590325` |
| **Reporter** | @mzygQAQ |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### LujhCoconut · 2026-06-26

Based on my understanding, the current proposal and implementation may not yet represent a fully mature solution. 

The original design was predicated on the assumption that LMCache would be used on top of Mooncake. In that design, LMCache allocates pinned CPU memory (in 4KB pages) on the computing node via `cudaHostAlloc()` in CUDA. In the SPDK-based approach, enabling huge page support is additionally required to achieve zero-copy. For further details, please refer to the RFC (Issue #1940 ). 

As for improving the error handling (e.g., a dedicated `NOT_ALIGNED` error code instead of `LOG(ERROR) + return nullopt`), that seems like a reasonable enhancement — PRs are welcome.

I will relay this concern to the designers and implementers of the RFC.

### SoftwareDogZ · 2026-06-26

Hi @mzygQAQ , we are the contributors of this feature. Thank you for the in-depth analysis, and we also appreciate the maintainer @LujhCoconut referencing our RFC. Below are our responses to your questions:

1. The original motivation of this PR is to increase KV cache capacity for LLM inference. Therefore, the current implementation is specifically designed for fixed-size KV cache chunks.

2. We are actively working on support for arbitrary chunk sizes. This will be addressed in an upcoming PR.

3. The current error reporting mechanism follows Mooncake’s native implementation. Please refer to the `BatchPut` and `BatchGet` functions in `client_service.cpp`: any transfer failure is reported as `ErrorCode::TRANSFER_FAIL`. In addition, introducing new error code types would require changes across the entire call chain and multiple data structures (e.g., ErrorCode, OperationState, TransferFuture, etc.), so we would prefer to seek feedback from the community before making such changes.

### mzygQAQ · 2026-06-26

> Hi [@mzygQAQ](https://github.com/mzygQAQ) , we are the contributors of this feature. Thank you for the in-depth analysis, and we also appreciate the maintainer [@LujhCoconut](https://github.com/LujhCoconut) referencing our RFC. Below are our responses to your questions:
> 
> 1. The original motivation of this PR is to increase KV cache capacity for LLM inference. Therefore, the current implementation is specifically designed for fixed-size KV cache chunks.
> 2. We are actively working on support for arbitrary chunk sizes. This will be addressed in an upcoming PR.
> 3. The current error reporting mechanism follows Mooncake’s native implementation. Please refer to the `BatchPut` and `BatchGet` functions in `client_service.cpp`: any transfer failure is reported as `ErrorCode::TRANSFER_FAIL`. In addition, introducing new error code types would require changes across the entire call chain and multiple data structures (e.g., ErrorCode, OperationState, TransferFuture, etc.), so we would prefer to seek feedback from the community before making such changes.

thanks for your reply !

### github-actions[bot] · 2026-09-25

This issue has had no activity for 90 days and will be closed in 7 days if there is no further activity. Please comment or react if it should stay open.
