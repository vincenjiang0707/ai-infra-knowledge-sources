# [Issue #2213] [Bug] SIGSEGV in ncclLocalOpAppend after ~1.1M collectives on CPU-path — dual DGX Spark (aarch64, GB10, NCCL 2.28.9+cuda13.0)

source: https://github.com/NVIDIA/nccl/issues/2213
state: open | updated: 2026-08-10T06:36:37Z
labels: 

## 正文

### How is this issue impacting you?

Application crash

### Share Your Debug Logs

dlvsym failed on mlx5dv_reg_dmabuf_mr - /lib/aarch64-linux-gnu/libmlx5.so: undefined symbol: mlx5dv_reg_dmabuf_mr, version MLX5_1.25
dlvsym failed on mlx5dv_get_data_direct_sysfs_path - /lib/aarch64-linux-gnu/libmlx5.so: undefined symbol: mlx5dv_get_data_direct_sysfs_path, version MLX5_1.25
Connected all rings, use ring PXN 0 GDR 0

*** SIGSEGV received at time=1775734074 on cpu 19 ***
PC: @     0xe1e2567f5014  (unknown)  ncclLocalOpAppend()

[Rank 0] Watchdog caught collective operation timeout: WorkNCCL(SeqNum=1155874, OpType=ALLREDUCE, NumelIn=9445376, NumelOut=9445376, Timeout(ms)=1800000) ran for 1800002 milliseconds before timing out.

[1] finished collective #1155873, but didn't join collective #1155874



### Steps to Reproduce the Issue

GPU: 2× NVIDIA GB10 (SM121, 128GB unified memory) — dual DGX Spark
Network: QSFP 200GbE direct cable (RoCE, ConnectX-7)
Environment: bare-metal, Ubuntu 24.04, kernel 6.17.0-1018-nvidia
CUDA driver: 13000, aarch64
Ranks: 2 (one per Spark)
GDR: disabled — mlx5dv_reg_dmabuf_mr not available (MLX5_1.25)
CPU-path transport only

### NCCL Version

2.28.9+cuda13.0

### Your platform details

GPU: 2× NVIDIA GB10 (SM121, 128GB unified memory) — dual DGX Spark
Network: QSFP 200GbE direct cable (RoCE, ConnectX-7)
Environment: bare-metal, Ubuntu 24.04, kernel 6.17.0-1018-nvidia
CUDA driver: 13000, aarch64
Ranks: 2 (one per Spark)
GDR: disabled — mlx5dv_reg_dmabuf_mr not available (MLX5_1.25)
CPU-path transport only

### Error Message & Behavior

First error: SIGSEGV in ncclLocalOpAppend after ~1.1M AllReduce operations on CPU-path

Expected: NCCL CPU-path proxy handles sustained long-running collective operations without memory corruption
Actual: SIGSEGV at ncclLocalOpAppend after ~1,155,873 collectives, rank 1 crashes, rank 0 watchdog fires after 1800s timeout

## 评论 (4)

### parallelArchitect · 2026-06-04

```python
import contextlib, os, torch, torch.distributed as dist
import torch.nn as nn
from torch.nn.parallel import DistributedDataParallel as DDP

hidden_dim, num_blocks, batch_size, seq_len = 1024, 16, 8, 4096
grad_accum_steps = 4

rank = int(os.environ["RANK"])
local_rank = int(os.environ.get("LOCAL_RANK", 0))
device = torch.device(f"cuda:{local_rank}")
torch.cuda.set_device(device)
dist.init_process_group(backend="nccl", init_method="env://")

class StackOfBlocks(nn.Module):
    def __init__(self):
        super().__init__()
        self.blocks = nn.ModuleList(
            nn.Sequential(nn.Linear(hidden_dim, hidden_dim*4), nn.GELU(),
                         nn.Linear(hidden_dim*4, hidden_dim), nn.LayerNorm(hidden_dim))
            for _ in range(num_blocks))
        self.head = nn.Linear(hidden_dim, hidden_dim)
    def forward(self, x):
        for b in self.blocks: x = x + b(x)
        return self.head(x)

model = DDP(StackOfBlocks().to(device), device_ids=[device.index])
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
criterion = nn.MSELoss()
x = torch.empty(batch_size, seq_len, hidden_dim, device=device)
y = torch.empty(batch_size, seq_len, hidden_dim, device=device)

for step in range(10_000_000):
    x.normal_(); y.normal_()
    is_sync = ((step + 1) % grad_accum_steps == 0)
    ctx = contextlib.nullcontext() if is_sync else model.no_sync()
    with ctx:
        loss = criterion(model(x), y) / grad_accum_steps
        loss.backward()
    if is_sync:
        optimizer.step()
        optimizer.zero_grad(set_to_none=True)

dist.barrier()
dist.destroy_process_group()
```

Reproduces consistently at ~1M+ collectives on CPU-path (GDR=0). Does not reproduce on discrete GPU platforms with GPU Direct RDMA enabled.

**Hypothesis**

The CPU-path proxy op buffer (`ncclProxyOps` ring buffer in `proxy.cc`) appears to corrupt after sustained operation (~1M+ cycles). The `proxyOps->nextOps`/`nextOpsEnd` pointers or the `freeOps` tracking may overflow or produce an invalid pointer after enough cycles, causing the SIGSEGV on the next `ncclLocalOpAppend` call.

**Reference**

Full logs and forum thread: https://forums.developer.nvidia.com/t/collective-operations-timeout-on-dual-spark-during-distributed-training/366147

      


### marksunner · 2026-07-15

Cross-linking a related vLLM RFC (#48720) that field-validates multi-node DGX Spark NCCL deadlock detection, including two live deadlock captures showing both collective-desync (51-op spread) and event-sync-hang signatures. The RFC proposes using NCCL's existing RAS (on since 2.24, localhost:28028) for collective-granularity detection.
  
Notable: ncclCommAbort proved unreliable on sm_121 under CUDA graph replay in our live captures — the worker stayed alive after correct abort calls.

### xiaofanl-nvidia · 2026-08-10

> Cross-linking a related vLLM RFC (#48720) that field-validates multi-node DGX Spark NCCL deadlock detection, including two live deadlock captures showing both collective-desync (51-op spread) and event-sync-hang signatures. The RFC proposes using NCCL's existing RAS (on since 2.24, localhost:28028) for collective-granularity detection.
> 
> Notable: ncclCommAbort proved unreliable on sm_121 under CUDA graph replay in our live captures — the worker stayed alive after correct abort calls.

Not sure I follow what this comment is trying to say.. Are you trying to report some more issues are are you reporting the same issue as the original post? 

But anyway ++ @nv-udeodhar please take a look at the original bug report on the segfault on dual spark. 

### marksunner · 2026-08-10

Apologies for the confusion — that comment was too compressed. To be clear: it isn't a "me too" on the segfault, and I'm not reporting a new issue in this thread. We'd been chasing what looked like multi-node NCCL deadlocks on the same hardware family (multi-node DGX Spark, GB10, NCCL-heavy tensor-parallel inference), and I cross-linked the RFC because the detection methodology seemed useful to anyone triaging hangs on this platform — in particular for separating a genuine NCCL fault (like the one reported here) from a stuck kernel that merely presents as one.

Two cheap checks from that work: (1) NCCL RAS (localhost:28028) gives per-rank launched-op counts during a hang — frozen-and-equal counts point at a stuck kernel or host, frozen-with-a-spread at a genuine collective desync; (2) nvidia-smi showing ~96% GPU utilization at near-idle power (~18–21 W, ~0% memory throughput) is a kernel spinning in place, not a collective waiting on a peer. Using exactly these, our hangs ultimately traced not to NCCL at all but to an attention-kernel livelock in flashinfer's sm120 sparse-MLA path on GB10 (mbarrier race, cuda-gdb capture) — full receipts in the RFC results update: https://github.com/vllm-project/vllm/issues/48720#issuecomment-5010866477. So for our symptom class NCCL was exonerated; the SIGSEGV here
looks like a separate, genuine issue and I don't want to muddy its triage.

The one NCCL-adjacent observation from our captures that may still interest the team: on sm_121 under CUDA graph replay, ncclCommAbort did not recover the communicator — every rank called abort correctly and the workers stayed wedged; process exit was the only recovery (observed twice). Scope: one cluster, one model/quant, one patch stack. Happy to open that as its own issue with receipts if useful — otherwise nothing in my earlier comment should hold up the original bug report.
