# [Issue #621] DeepEP LL Combine Race on NVL72

source: https://github.com/deepseek-ai/DeepEP/issues/621
state: closed | updated: 2026-05-26T02:50:32Z
labels: 

## 正文

# Reproduction Steps

We setup the following test:

* single NVL72 node with 4 GB200s
* `topk` = 2
* only rank 0 has tokens going into dispatch, the rest are marked `-1`
* each tokens gets routed to expert 0 and 1
* both experts weights are 1
* batch size 256 or 1024

with the following code:

```
import os
os.environ['NVSHMEM_QP_DEPTH'] = '4096'

import torch, torch.distributed as dist, deep_ep

dist.init_process_group(backend='nccl')
rank, W = dist.get_rank(), dist.get_world_size()
torch.cuda.set_device(rank)

H, E = 7168, 256
N = 1024

for T in [256, 1024]:
    buf = deep_ep.Buffer(
        dist.new_group(list(range(W))),
        num_nvl_bytes=0,
        num_rdma_bytes=deep_ep.Buffer.get_low_latency_rdma_size_hint(T, H, W, E),
        low_latency_mode=True, num_qps_per_rank=E//W,
        allow_mnnvl=True, explicitly_destroy=True)

    torch.manual_seed(42)
    x = torch.randint(0, 2, (T, H), dtype=torch.bfloat16, device='cuda') if rank == 0 else         torch.zeros(T, H, dtype=torch.bfloat16, device='cuda')

    if rank == 0:
        ids = torch.zeros(T, 2, dtype=torch.int64, device='cuda')
        ids[:, 0] = 0; ids[:, 1] = 1
        w = torch.ones(T, 2, dtype=torch.float32, device='cuda')
        expected = (2.0 * x.float()).bfloat16()
    else:
        ids = torch.full((T, 2), -1, dtype=torch.int64, device='cuda')
        w = torch.zeros(T, 2, dtype=torch.float32, device='cuda')
        expected = torch.zeros(T, H, dtype=torch.bfloat16, device='cuda')

    n_wrong = 0
    for it in range(N):
        buf.clean_low_latency_buffer(T, H, E)
        torch.cuda.synchronize()
        dist.barrier()

        ex, _, h, _, hk = buf.low_latency_dispatch(
            x, ids, T, E, use_fp8=False, async_finish=False, return_recv_hook=True)
        hk()
        torch.cuda.synchronize()

        out = torch.zeros(T, H, dtype=torch.bfloat16, device='cuda')
        _, _, hk_c = buf.low_latency_combine(
            ex.clone(), ids, w, h, async_finish=False,
            return_recv_hook=True, out=out)
        hk_c()
        torch.cuda.synchronize()

        if not torch.equal(out, expected):
            n_wrong += 1

    if rank == 0:
        print(f'T={T}: correct={N-n_wrong}/{N}')

    dist.barrier()
    buf.destroy()

dist.destroy_process_group()
```

If run with `torchrun --nproc-per-node=4 upstream_repro.py` produces

```
T=256: correct=1024/1024
T=1024: correct=229/1024
```
suggesting a race condition of some sort at batch size larger than 256.

If not user error (please let me know if it is), additionally sharing plausible-looking fixes:

# Plausible fixes

1. __ldg on `rdma_recv_x`

```
int num_tma_bytes = num_decode_warps * kNumBF16PerWarpBytes;
auto src = reinterpret_cast<const int4*>(buffer);
auto dst = reinterpret_cast<int4*>(tma_ld_buffers[stage_idx]);
int num_int4 = num_tma_bytes / static_cast<int>(sizeof(int4));
for (int j = lane_id; j < num_int4; j += 32)
    dst[j] = __ldg(&src[j]);
__syncwarp();
if (elect_one_sync(lane_id))
    mbarrier_arrive(full_barriers[stage_idx]);low_latency_combine
```


2.  `asm volatile("fence.proxy.async;");`

```
if (elect_one_sync(lane_id)) {
    int num_casted = 0;
    if constexpr (kUseLogFMT) {
        const auto& info = cast_info_buffers[stage_idx][num_decode_warps - 1];
        num_casted = (info >> 1) + (info & 1);
    }
    int num_tma_bytes = num_casted * kNumLogFMTPerWarpBytes + (num_decode_warps - num_casted) * kNumBF16PerWarpBytes;
    if (use_fence_proxy_async)
        asm volatile("fence.proxy.async;");
    tma_load_1d(tma_ld_buffers[stage_idx], buffer + (kUseLogFMT ? kNumMetaBytes : 0), full_barriers[stage_idx], num_tma_bytes);
    mbarrier_arrive_and_expect_tx(full_barriers[stage_idx], num_tma_bytes);
}
```

Both fixes make this test pass.

Let me know if/how I can provide more info help addressing this issue.

## 评论 (2)

### elvircrn · 2026-05-06

Here is another tests which matches production dimensions more closely:

```
import os
os.environ['NVSHMEM_QP_DEPTH'] = '4096'

import torch, torch.distributed as dist, deep_ep

dist.init_process_group(backend='nccl')
rank, W = dist.get_rank(), dist.get_world_size()
torch.cuda.set_device(rank)

topk = 8
T, H, E = 1024, 7168, 256

buf = deep_ep.Buffer(
    dist.new_group(list(range(W))),
    num_nvl_bytes=0,
    num_rdma_bytes=deep_ep.Buffer.get_low_latency_rdma_size_hint(T, H, W, E),
    low_latency_mode=True, num_qps_per_rank=E//W,
    allow_mnnvl=True, explicitly_destroy=True)

torch.manual_seed(42 + rank)
x = torch.randint(0, 2, (T, H), dtype=torch.bfloat16, device="cuda")

ids = torch.arange(topk, device='cuda', dtype=torch.int64).unsqueeze(0).expand(T, -1).contiguous()
w = torch.ones(T, topk, dtype=torch.float32, device='cuda')

expected = (float(topk) * x.float()).bfloat16()

N = 1024
n_wrong = 0
total_bad_rows = 0
total_bad_cols = 0
for it in range(N):
    buf.clean_low_latency_buffer(T, H, E)
    torch.cuda.synchronize()
    dist.barrier()

    ex, _, h, _, hk = buf.low_latency_dispatch(
        x, ids, T, E, use_fp8=False, async_finish=False, return_recv_hook=True)
    hk()
    torch.cuda.synchronize()

    out = torch.zeros(T, H, dtype=torch.bfloat16, device='cuda')
    _, _, hk_c = buf.low_latency_combine(
        ex.clone(), ids, w, h, async_finish=False,
        return_recv_hook=True, out=out)
    hk_c()
    torch.cuda.synchronize()

    if not torch.equal(out, expected):
        n_wrong += 1
        diff = (out != expected)
        total_bad_rows += diff.any(dim=1).sum().item()
        total_bad_cols += diff.any(dim=0).sum().item()

if rank == 0:
    print(f'upstream main (topk={topk}): correct={N-n_wrong}/{N}')
    if n_wrong > 0:
        print(f'  avg bad rows: {total_bad_rows/n_wrong:.1f}/{T}  avg bad cols: {total_bad_cols/n_wrong:.1f}/{H}')

dist.barrier()
buf.destroy()
dist.destroy_process_group()

```

Output:

```
upstream main (topk=8): correct=74/1024
  avg bad rows: 2.8/1024  avg bad cols: 164.0/7168
```

### sphish · 2026-05-26

Fixed in https://github.com/deepseek-ai/DeepEP/pull/642, Thanks!
