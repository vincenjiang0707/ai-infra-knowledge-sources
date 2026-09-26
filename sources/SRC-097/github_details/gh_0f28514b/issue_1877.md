# [Issue #1877] Query: Developing new plugin for device memory.

source: https://github.com/ai-dynamo/nixl/issues/1877
state: closed | updated: 2026-07-02T15:07:32Z
labels: 

## 正文

we are developing a new nixl bacnkend plugin to a FPGA based high speed device memory, 
where GPU VRAM to Device memory KV Transfers happens via our plugin.
we are corrently doing 1:1 mapping , but since our device has large memory ( more than VRAM) 
How should plugin handle that case , e.g GPU VRAM - 64gb and our device RAM has 512GB .?

## 评论 (2)

### linear-code[bot] · 2026-07-02

from mikhailb:
> NIXL doesn't require a 1:1 address mapping between GPU VRAM and your backend's memory — the transfer descriptors (`nixl_xfer_dlist`) just carry addr/len/devID pairs, and your plugin owns how "addr" gets interpreted on the device side. So the fix isn't really a capacity problem (512GB > 64GB means you'll never run out first), it's an addressing/allocator design problem.
> 
> A few options, roughly in order of complexity:
> 
> 1. **Offset allocator in the plugin.** On `registerMem`, don't try to preserve the GPU's literal address — allocate a range out of your 512GB pool (simple free-list or bump allocator) and keep a translation table (GPU addr/block ID → device offset) inside the plugin. `deregisterMem` returns the range to the free list.
> 2. **Block-level mapping.** If the upper layer works in fixed-size KV blocks (vLLM/Dynamo-style), size your device-side slabs to match the block granularity and maintain a bitmap/free-list of slabs. Then a transfer just needs (GPU block ID → device slab ID), which is a much simpler lookup than general offset allocation and mirrors how the KV block manager already thinks about memory.
> 3. **Treat it like a storage-class backend.** NIXL's existing GDS and OBJ (S3) backends already deal with backing stores that aren't 1:1 with GPU memory — they address via file offset / object key rather than raw pointer. Same pattern applies here: define your own addressing scheme (e.g., device-local block/segment ID) instead of trying to mirror GPU VRAM addresses directly.
> 
> One thing worth flagging: since 512GB is finite too, once total resident KV across all attached GPUs exceeds it, you'll eventually need the same kind of eviction/backpressure policy you'd need for VRAM — the bigger pool just buys you headroom (e.g., support for 8 GPUs' worth of KV, or much longer context/more concurrent sequences), it doesn't remove the need for a policy longer-term.

### alokprasad · 2026-07-02

Thanks for clarifying it nicely.
