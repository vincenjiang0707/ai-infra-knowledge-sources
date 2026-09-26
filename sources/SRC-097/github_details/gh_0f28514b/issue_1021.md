# [Issue #1021] [Performance] nixlbench showing significantly lower bandwidth than raw UCX - optimization guidance needed

source: https://github.com/ai-dynamo/nixl/issues/1021
state: closed | updated: 2026-04-29T03:25:13Z
labels: 

## 正文

## Observation
After successfully resolving UCX version and ETCD coordination issues, nixlbench is showing much lower bandwidth than raw UCX performance tests on the same hardware.

## Performance Comparison

| Test | Bandwidth | Transport | Hardware |
|------|-----------|-----------|----------|
| **Raw UCX (ucp_put_bw)** | **284.98 GB/s** | UCX over EFA | 2x H100 80GB |
| **nixlbench** | **0.324 GB/s** | UCX via NIXL | Same hardware |
| **Ratio** | **1:878** | - | - |

## Test Configuration
```bash
nixlbench \
  --backend UCX \
  --initiator_seg_type VRAM \
  --target_seg_type VRAM \
  --enable_pt 0 \
  --num_threads 1 \
  --max_batch_size 1 \
  --num_iter 64
```

## Environment
- Platform: AWS SageMaker HyperPod EKS
- Hardware: 2x H100 80GB HBM3
- Network: EFA with GPUDirect RDMA enabled
- Container: Custom build with UCX 1.19.0, NIXL 0.7.1
- ETCD: Successfully coordinating, barriers working

## Potential Causes
1. **Progress threads disabled** (`--enable_pt 0`)
2. **Single thread** (`--num_threads 1`)
3. **Batch size 1** (`--max_batch_size 1`)
4. **UCX transport settings** not optimized for EFA

## Request
Could the team provide guidance on:
1. Recommended nixlbench settings for optimal EFA/GPUDirect performance
2. UCX environment variables for AWS EFA optimization
3. Expected performance characteristics (is 0.32 GB/s expected for this config?)
4. Whether the NIXL abstraction layer introduces expected overhead

## Documentation Reference
Full test results: https://github.com/dmvevents/dynamo-workshop/blob/main/NIXLBENCH_SUCCESS_RESULTS.md

The gap seems too large to be only configuration, so any guidance would be appreciated to ensure we're benchmarking correctly.

## 评论 (7)

### rmccorm4 · 2025-11-13

Hi @dmvevents, thanks for raising this. Moved this issue to the nixl repository. CC @mkhazraee @kahalon 

### aranadive · 2025-11-14

@dmvevents can you clarify the block_size used? By default the starting block size is 4K and it should go up to 64MB. The BW of 0.32GB/s is about expected for a 4K block size. You can also run just for a specific block_size by setting start_block_size and max_block_size to the same value. You can also increase the num_iter to 1000.

### dmvevents · 2025-12-04

@aranadive Thanks for the clarification! Here are the details about our block_size configuration and performance results:

**Block Size Configuration Used:**

- **start_block_size**: 4096 bytes (4 KiB) - default
- **max_block_size**: 67108864 bytes (64 MiB) - default  
- **num_iter**: 100 - default

We ran the full sweep from 4KB → 64MB which tests 15 different block sizes automatically.

**Performance Results:**

| Block Size | Bandwidth (GB/s) | Notes |
|------------|------------------|-------|
| 4 KB | ~0.32 GB/s | As you mentioned - expected for small blocks |
| 64 KB | ~2.1 GB/s | |
| 1 MB | ~15.8 GB/s | |
| 16 MB | ~38.5 GB/s | |
| **64 MB** | **46.59 GB/s** | **Peak performance** |

**Configuration:**
- Backend: LIBFABRIC with EFA provider
- GPUs: 8× H100 80GB per node  
- EFA: 32 devices per instance (400 Gbps)
- Memory: GPU VRAM-to-VRAM transfers
- P2P: Enabled (`FI_HMEM_DISABLE_P2P=0`)

The 0.32 GB/s figure you mentioned is indeed what we observed at 4KB block size, which matches the expected baseline. Peak performance at 64MB block size was **46.59 GB/s** on single GPU pair, and **383.67 GB/s aggregate** when scaling to 8 GPUs per node with 8 threads.

**Would you recommend**:
1. Increasing `num_iter` to 1000 for more stable measurements?
2. Running targeted tests at specific block sizes (e.g., only 64MB) for production benchmarking?

Thanks for the guidance!

### aranadive · 2025-12-07

> **Would you recommend**:
> 
> 1. Increasing `num_iter` to 1000 for more stable measurements?
> 2. Running targeted tests at specific block sizes (e.g., only 64MB) for production benchmarking?

Yes please more iterations (1000) for stable measurements. Also, set the warmup_iter and large_blk_iter_ftr parameters to 0 to run for the entire 1000 iterations for large block sizes (>1M).

Larger block sizes will help to saturate nw bandwidth. You can also try increasing batch size (16) for smaller block sizes like 1M, 2M as well. 

Closing this issue since you can achieve peak performance.

### alokprasad · 2026-04-17

@dmvevents can you share steps how to run Nixlbench over EFA , i am trying to reproduce similar figures but documentation to run over network is little scattered.

### aranadive · 2026-04-20

@alokprasad please open another issue if documentation needs to be updated and discuss LIBFABRICS use. You should be able to substitute LIBFABRICS for UCX as backend with same nixlbench command above.

### clw11 · 2026-04-29

Hi, I'd like to ask if this issue was eventually resolved, and how it was resolved, because I'm encountering a similar problem. Thanks!
