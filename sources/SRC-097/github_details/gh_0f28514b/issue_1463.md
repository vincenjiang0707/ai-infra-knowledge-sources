# [Issue #1463] nixlbench: #1407 introduces 8x inflated B/W in pairwise SG mode with multiple initiator devices

source: https://github.com/ai-dynamo/nixl/issues/1463
state: closed | updated: 2026-04-14T20:19:03Z
labels: 

## 正文

## Bug Description

Commit 7c4f144 ([#1407](<https://github.com/ai-dynamo/nixl/issues/1407>), fix for [NIX-1062](https://linear.app/nvidia/issue/NIX-1062/nixlbench-incorrect-statistics-calculation-for-multi-initiator-devices)) added `IS_PAIRWISE_AND_SG() && num_initiator_dev > 1` to the stats scaling condition in printStats(). This causes per-device B/W to be multiplied by `num_initiator_dev`, reporting aggregate throughput in the per-device B/W column. Downstream consumers (e.g. wrapper scripts computing aggregate as sum of per-device) then double-count, producing results that exceed theoretical hardware limits.

## Root Cause

```cpp
// utils.cpp:1118
if (IS_PAIRWISE_AND_MG() || (IS_PAIRWISE_AND_SG() && xferBenchConfig::num_initiator_dev > 1)) {
    total_data_transferred *= xferBenchConfig::num_initiator_dev;
    avg_latency /= xferBenchConfig::num_initiator_dev;
}
```

In SG mode, each device runs in its own thread with independent timing. `total_duration.avg()` is the average per-device wall-clock time, and total_data_transferred is already the correct per-device data volume. Multiplying by num_initiator_dev conflates per-device and aggregate throughput.

This scaling is correct for MG mode (where multiple devices share a single timing measurement), but not for SG mode.

## Reproduction

8-device VRAM-VRAM WRITE, pairwise SG, block=64MB, batch=16:

BEFORE 7c4f144 (parent 7c42f81):

```
Block Size    B/W (GB/s)   Aggregate (GB/s)
67108864      48.71        389.67       ← correct, near 400 GB/s theoretical limit
```

AFTER 7c4f144:

```
Block Size    B/W (GB/s)   Aggregate (GB/s)
67108864      389.79       3117.46      ← Aggregate exceeds theoretical limit by 8x
```

Per-device B/W jumped exactly 8x (num_initiator_dev). The 64MB aggregate of 3117 GB/s is physically<br>impossible on this hardware (p6 with 8 EFA devices, \~400 GB/s max).

Do you mind taking a further look? I don't think I agree that [NIX-1062](https://linear.app/nvidia/issue/NIX-1062/nixlbench-incorrect-statistics-calculation-for-multi-initiator-devices) is a legit issue given the reasons above.

## 评论 (3)

### aranadive · 2026-03-30

@yexiang-aws can you add the reproduction command?

### yexiangd · 2026-03-30

The key options are `--num-devices 8 --mode SG`.  If you run it comparing before and after the mentioned commit, you should be able to see the 8x BW and numbers exceeded the theoretical bandwidth limit.

e.g.

```bash
nixlbench \
  --runtime_type ETCD --etcd_endpoints http://<node1-ip>:2379 \
  --backend LIBFABRIC \ # or UCX
  --initiator_seg_type VRAM --target_seg_type VRAM \
  --num_initiator_dev 8 --num_target_dev 8 \
  --op_type WRITE --mode SG --scheme pairwise \
  --num_threads 1 \
  --start_block_size 67108864 --max_block_size 67108864 \
  --start_batch_size 16 --max_batch_size 16 \
  --total_buffer_size 8589934592 \
  --check_consistency=0
```

### omer-b1 · 2026-04-05

Thanks.
I opened PR with a fix in #1495. The scaling is correct for single-process storage backends (getSize()==1) where all devices share one timer, but wrong for multi-rank VRAM where each rank has its own device and timer. The fix guards the SG scaling with rt->getSize() == 1.

