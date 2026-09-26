# [Issue #2353] [Issue]: Deadlock between `ncclLocalOpAppend` and the proxy progress thread when the proxy op pool is exhausted

source: https://github.com/NVIDIA/nccl/issues/2353
state: closed | updated: 2026-08-28T22:21:18Z
labels: 

## 正文

### How is this issue impacting you?

Application hang

### Share Your Debug Logs

`NCCL_DEBUG=INFO` was enabled for the reproductions. NCCL logs **nothing at all**
when the hang occurs — no `WARN`, no timeout, no async error. The last NCCL output
is from initialisation, and it looks entirely healthy: 16 collective channels
alternating across the two rails.

```
NCCL INFO 16 coll channels, 16 collnet channels, 0 nvls channels, 16 p2p channels
NCCL INFO Channel 00/0 : 0[0] -> 1[0] [send] via NET/IB/0
NCCL INFO Channel 01/0 : 0[0] -> 1[0] [send] via NET/IB/1
NCCL INFO Channel 02/0 : 0[0] -> 1[0] [send] via NET/IB/0
...  (even channels on IB/0, odd on IB/1)
```

The silence is expected given the mechanism: nothing detects the condition. So
the useful evidence is thread state at the moment of the hang, captured with
`eu-stack` on both ranks.

**Rank 1, main thread — blocked in the append path. Note it is still inside
`ncclEnqueueCheck`, so the kernel for this collective was never launched:**

```
#0  __sched_yield
#1  ncclLocalOpAppend(ncclComm*, ncclProxyConnector*, ncclProxyOp*)
#2  SaveProxy(ncclComm*, ncclChannel*, int, int, ncclProxyOp*, int, bool*)
#3  ncclProxySaveOp(ncclComm*, ncclProxyOp*, bool*)
#4  uploadProxyOps(ncclComm*, ncclKernelPlan*)
#5  hostStreamPlanTask(ncclComm*, ncclKernelPlan*)
#6  ncclLaunchKernelAfter_NoCuda(ncclComm*, ncclKernelPlan*)
#7  groupLaunch(ncclAsyncJob*, ncclSimInfo_v22200*)
#8  ncclGroupEndInternal(ncclSimInfo_v22200*)
#9  ncclEnqueueCheck(ncclInfo*)
#10 pncclAllGather
```

**Rank 1, proxy progress thread — asleep at the same instant:**

```
#0  <futex>
#1  pthread_cond_wait
#2  ncclProxyGetPostedOps(ncclProxyState*, int*)
#3  ncclProxyProgress(void*)
```

**Rank 0, proxy progress thread — idle with no work (two samples 8 s apart,
identical):**

```
#0  __sched_yield
#1  ncclProxyProgress(void*)
```

The stalled collective is `ncclAllGather`, `16x64640` bfloat16 (~2 MB).

**Fabric counters while hung** — `port_xmit_data` on both rails of both nodes,
sampled three times over 9 seconds, byte-for-byte unchanged, while both GPUs sit
at 96% utilisation:

```
02:15:32Z  head_xmit=162459179474  worker_xmit=127395400347  gpu 96% / 96%
02:15:36Z  head_xmit=162459179474  worker_xmit=127395400347  gpu 96% / 96%
02:15:41Z  head_xmit=162459179474  worker_xmit=127395400347  gpu 96% / 96%
```

**Collectives are correctly matched.** We instrumented `torch.distributed` to log
every collective's op, shape and dtype on both ranks: **162696 comparable
collectives, 0 mismatches, identical order**. (Comparing call *counts* alone
proves nothing here, since NCCL pairs by enqueue order — a single differing op
would deadlock while both counters stayed equal, so the identity has to be
compared.)

**Every IB error counter is zero** on both rails and both nodes — no
`port_rcv_errors`, `port_xmit_discards`, `local_link_integrity_errors`,
`symbol_error`, `link_downed`, and no `out_of_sequence` / `packet_seq_err` /
`req_cqe_error` in `hw_counters`.

> Not yet attached: `NCCL_TOPO_DUMP_FILE` output. Happy to provide it — say the
> word and we will restart with it set. Also happy to share the full per-rank
> `eu-stack` dumps and the raw collective-identity traces.

### Steps to Reproduce the Issue

### The cycle, from the source

All three legs are in `src/proxy.cc`. Line numbers for **2.28.9** (what we run)
and **v2.31.2-1** (latest release, code unchanged in substance):

| leg | 2.28.9 | v2.31.2-1 | waits for |
| --- | --- | --- | --- |
| appender spins for a free op | `proxy.cc:498` | `proxy.cc:507` | the proxy to return a free op |
| proxy sleeps | `proxy.cc:797` | `proxy.cc:850` | `pool->nextOps != -1`, i.e. something posted |
| the only signal | `ncclProxyPost`, `proxy.cc:468` | `proxy.cc:476` | `++proxyOps->count == MAX_OPS_PER_PEER` (`:516` / `:525`) |

In `ncclLocalOpAppend`:

```c
  int opIndex = proxyOps->freeOp;
  if (opIndex != -1) {
    ...
  } else {
    // Read the freeOps value and wait for a value different than -1. ...
    int freeOp = -1;
    while (freeOp == -1) {
      freeOp = __atomic_exchange_n(&pool->freeOps[tpLocalRank], -1, __ATOMIC_ACQUIRE);
      if (freeOp == -1) sched_yield();      // <-- blocks here forever
    }
    ...
  }
  ...
  if (++proxyOps->count == MAX_OPS_PER_PEER) {
    ...
    NCCLCHECK(ncclProxyPost(proxyOps->pool, nextOps, lastOp));   // <-- the only wakeup
  }
```

At the moment it blocks, this thread holds up to `MAX_OPS_PER_PEER - 1` ops in its
local chain (`proxyOps->nextOps .. nextOpsEnd`) that have **not** been posted. So
`pool->nextOps` stays `-1`, the proxy stays asleep, no ops are freed, `count`
never reaches `MAX_OPS_PER_PEER`, and the post that would break the cycle is
unreachable. The appender waits for the proxy; the proxy waits for the appender.

This is **not** the condition-variable lost wakeup that v2.31.2's new predicate
addresses:

```c
// v2.31.2-1, proxy.cc:849
// Predicate avoids lost wakeups and guarantees we observe stop after ncclProxyProgressDestroy.
pool->cond.wait(lock, [&]() { return pool->nextOps != -1 || state->stop.load(...) != 0; });
```

That predicate is correct. It does not help here, because nothing ever posts and
so the predicate simply stays false.

### What it takes to trigger

One rank must get far enough ahead of its peer to exhaust the pool
(`MAX_OPS_PER_PEER` = `2*MAXCHANNELS*2*NCCL_MAX_DEV_WORK_P2P_PER_BATCH` = **2048**).

That is not an exotic state. Collective calls enqueue and return, so any rank that
does not synchronise pulls ahead of one that does. In our workload, rank 0
synchronises each step to copy sampled tokens back to the host and rank 1 does
not, leaving rank 1 a steady ~61 collectives ahead on every healthy step. With 16
channels active, a few hundred queued collectives reaches 2048 proxy ops.

We do not have a standalone NCCL-only reproducer. What reproduces it reliably is:
2 ranks, 1 GPU each, on separate nodes, TP=2 over RoCE, driving a stream of small
collectives where one rank synchronises per iteration and the other does not, with
frequent mid-iteration cancellation so the queue depth keeps varying. We are glad
to try a minimal `nccl-tests`-style reproducer if that would help — a loop where
rank 0 calls `cudaStreamSynchronize` each iteration and rank 1 does not, run long
enough for rank 1's lead to reach ~2048 proxy ops, looks like it should suffice.

### Intermittency

Timing-sensitive but frequent enough to be practical to hunt:

| | requests to reproduce |
| --- | --- |
| unpatched | 23, 38, 60, 102, 109, 188, 248 — **7 of 8 runs hung** |
| patched | 1546 requests over 150 min, **0 hangs** |

Same seed and settings in every run. The single unpatched run that did not hang
(431 requests) was also the only one with our tracing disabled — extra logging
load makes it markedly more likely, which is what an ordering bug of this shape
would predict. Under ordinary production load, without any tracing, it occurred
roughly once every 24-33 hours.

### Previous versions

Unknown — this is the first NCCL version we have run this workload on. The code
path is unchanged in the latest release, so we would not expect any released
version to differ.

### Suggested fix

Post the accumulated chain before blocking. That signals the proxy, which consumes
those ops and returns free ones, so the appender can proceed. The existing
`MAX_OPS_PER_PEER` branch already has exactly the right logic — including the rule
that the trailing ops of the current `opCount` must be held back, since "posting
them in different batches would break proxyArgs aggregation with subs" — so it can
be factored out and reused:

```c
static ncclResult_t ncclLocalOpFlush(struct ncclProxyOps* proxyOps, bool* posted) {
  struct ncclProxyOpsPool* pool = proxyOps->pool;
  *posted = false;
  if (proxyOps->nextOps == -1) return ncclSuccess;
  uint64_t lastOpCount = pool->ops[proxyOps->nextOpsEnd].opCount;
  int lastOp = -1, toSend = 0, ops = 0;
  for (int op = proxyOps->nextOps; op != proxyOps->nextOpsEnd; op = pool->ops[op].next) {
    ops++;
    if (pool->ops[op].opCount != lastOpCount) { lastOp = op; toSend = ops; }
  }
  if (lastOp == -1) return ncclSuccess;     // nothing safely postable
  int nextOps = proxyOps->nextOps;
  proxyOps->nextOps = pool->ops[lastOp].next;
  pool->ops[lastOp].next = -1;
  NCCLCHECK(ncclProxyPost(pool, nextOps, lastOp));
  proxyOps->count -= toSend;
  *posted = true;
  return ncclSuccess;
}
```

then, in the `else` branch that currently spins:

```c
  } else {
    bool flushed = false;
    NCCLCHECK(ncclLocalOpFlush(proxyOps, &flushed));   // break the cycle
    int freeOp = -1;
    while (freeOp == -1) { ... }                        // unchanged
  }
```

The `MAX_OPS_PER_PEER` site calls the same helper and keeps its existing `WARN` +
`ncclInternalError` when `*posted` comes back false.

One case this does **not** cover: if every op in the local chain shares a single
`opCount`, nothing is safely postable and the wait can still stall. We have not
observed that, and did not want to relax the aggregation rule without knowing why
it exists — flagging it in case it needs handling too.

Happy to open a PR if the approach looks right.

### NCCL Version

2.28.9+cuda13.0

### Your platform details

**GPU & network.** 2 x NVIDIA DGX Spark (GB10, compute capability 12.1),
**1 GPU per node**, aarch64. Driver 580.173.02, CUDA 13.0.88.
ConnectX-7 joined **back-to-back** (no switch) at 200 Gb/s, exposed by the kernel
as two RDMA devices because the card runs multi-host mode:

```
$ nvidia-smi topo -m
        GPU0    NIC0    NIC1    NIC2    NIC3    CPU Affinity  NUMA Affinity  GPU NUMA ID
GPU0     X      NODE    NODE    NODE    NODE    0-19          0              N/A
NIC0    NODE     X      PIX     NODE    NODE
NIC1    NODE    PIX      X      NODE    NODE
NIC2    NODE    NODE    NODE     X      PIX
NIC3    NODE    NODE    NODE    PIX      X

rocep1s0f0:    state=ACTIVE  rate=200 Gb/sec (4X HDR)  link_layer=Ethernet  gid[3]=RoCE v2
roceP2p1s0f0:  state=ACTIVE  rate=200 Gb/sec (4X HDR)  link_layer=Ethernet  gid[3]=RoCE v2
```

Dual-rail: `NCCL_IB_HCA` lists both HCAs, `NCCL_IB_GID_INDEX=3`, the two rails on
disjoint /24s. NCCL puts even channels on IB/0 and odd on IB/1.

**Environment.** Containers (Docker), Ubuntu 24.04.4, kernel 6.17.0-1029-nvidia.
NCCL from the `nvidia-nccl-cu13` wheel, used via PyTorch 2.11.0+cu130.

Non-default NCCL settings:

```
NCCL_CUMEM_ENABLE=0        # GB10 cannot load nvidia-peermem and its allocator
NCCL_NVLS_ENABLE=0         # does not export dmabuf handles
NCCL_IGNORE_CPU_AFFINITY=1 # single NUMA node, HCA numa_node = -1
NCCL_IB_GID_INDEX=3
NCCL_CROSS_NIC=1
```

**Scalability.** Seen at the smallest possible multi-node size: **2 ranks, 2
nodes, 1 GPU each**. We have not tried other rank counts. Since the mechanism is
purely host-side thread ordering within one rank, we would not expect the rank
count to matter, only that one rank runs ahead of another.

It reproduces identically through PyTorch's `ProcessGroupNCCL` and through our
framework's own NCCL wrapper, so it is not specific to either.

### Error Message & Behavior

**First error: there is none.** This is a large part of what made it hard to
diagnose. NCCL emits no `WARN` and no timeout. PyTorch's `ProcessGroupNCCL`
watchdog, which polls `ncclCommGetAsyncError`, also reports nothing and is found
parked in its normal `pthread_cond_timedwait` — we did not call
`ncclCommGetAsyncError` directly, so treat that as indirect evidence.

The collective's own timeout cannot fire either: PyTorch's default collective
timeout is 30 minutes, while the framework above it gives up on its own RPC after
300 s and tears the process down — 25 minutes too early — so
`TORCH_NCCL_DUMP_ON_TIMEOUT` never runs and the flight recorder is never dumped.

**Expected.** `ncclAllGather` completes, or some layer reports an error.

**Actual.** The call never returns. Both ranks' GPUs spin at 96% and the RoCE byte
counters stop moving entirely. We can only bound the duration from below: our
framework kills the engine at its own 300 s RPC timeout, and the longest we
observed before that was 240 s of a completely stalled engine. Nothing in that
window suggested it would ever recover. From
outside, every health signal looks fine: containers up, HTTP endpoint answering,
links up, no error counters, no OOM, memory and disk healthy. Only a thread dump
shows the two threads waiting on each other.


## 评论 (14)

### michaelmanly · 2026-08-18

@Cryspia 
This is a nasty repro. The fact everything still looks healthy while the collective is actually deadlocked is interesting.

Do you have the workload or repro script in a repo somewhere? I can put it through a free Badgr Smoke Test first and see if we can turn the patched vs unpatched case into one clean repeatable command.

### Cryspia · 2026-08-19

Thanks for looking at it.

The original workload is a two-node vLLM inference service — 167 GB of weights, our
tensor-parallel setup, a KV offload tier, all in a private repo. It would never
reduce to one command, and none of it is relevant to the bug.

[nccl_proxy_pool_deadlock.py](https://github.com/user-attachments/files/31206078/nccl_proxy_pool_deadlock.py)

So here is a standalone reproducer instead: **two ranks, one collective in a loop.**
No model, no inference framework, no dataset. It imports `torch` and the standard
library, nothing else.

## What it does

The pool has to be exhausted before the cycle can close, and to exhaust it one rank
must run ahead of the other. The script arranges exactly that — and the asymmetry is
not contrived, it is what any workload does when one rank reads its result back and
another does not:

```
rank 0   all_gather, then .item()   -> synchronises every iteration
rank 1   all_gather, no sync        -> enqueues freely and pulls ahead
```

Each `all_gather` costs ~nChannels proxy ops, so with 16 channels rank 1 needs a lead
of about `MAX_OPS_PER_PEER / nChannels` = 2048/16 = **128** iterations to fill the
pool. Observed stalls: iteration 127, 139, 313, 385, 553.

## How to run it

Same command on both nodes, only `--node_rank` differs. **`--node_rank` must come
before the script name** — anything after it is passed to the script, not to
torchrun, and both ranks then default to 0 and hang in rendezvous with no output.
(That cost us an hour.)

```bash
torchrun --nnodes=2 --node_rank=0 --nproc_per_node=1 \
         --master_addr=<node0-ip> --master_port=29500 \
         nccl_proxy_pool_deadlock.py --iters 20000 --lead 4096
```

Exit **0** = completed. Exit **9** = the progress heartbeat stalled past `--timeout`.

For the evidence rather than just the symptom, run it where `elfutils` is installed
and the process has CAP_SYS_PTRACE — see "Why it dumps its own stacks" below.

<details>
<summary>The container form we used</summary>

```bash
IMG=<any image with torch>
NCCLENV="-e NCCL_IB_HCA=<hca0>,<hca1> -e NCCL_IB_GID_INDEX=3 \
         -e NCCL_SOCKET_IFNAME=<iface> -e NCCL_CUMEM_ENABLE=0 -e NCCL_NVLS_ENABLE=0"
CMD="cd /repro && torchrun --nnodes=2 --node_rank=0 --nproc_per_node=1 \
     --master_addr=<node0-ip> --master_port=29500 \
     nccl_proxy_pool_deadlock.py --iters 20000 --lead 4096"

docker run --rm --network host --ipc host --gpus all $NCCLENV \
  --cap-add SYS_PTRACE -v $PWD:/repro --entrypoint bash $IMG -lc "$CMD"
```

`NCCL_CUMEM_ENABLE=0` / `NCCL_NVLS_ENABLE=0` are ours because GB10 cannot load
nvidia-peermem; drop them if they do not apply to you. We used
`vllm/vllm-openai:v0.26.0-aarch64` with `elfutils` added — vLLM is irrelevant, it
just happened to be the torch environment we had. It also runs unmodified in that
image, minus the stack dumps.
</details>

## Patched vs unpatched

`LD_PRELOAD` does **not** work for this: torch dlopens libnccl by absolute path, so
preloading a second copy leaves both mapped and which one wins is ambiguous. We
verified that. Replace the file torch loads:

```bash
# what torch actually loads
python3 -c "import ctypes,torch; ctypes.CDLL('libnccl.so.2',mode=ctypes.RTLD_GLOBAL); \
  print([l.split()[-1] for l in open('/proc/self/maps') if 'libnccl' in l])"

cp $LIB $LIB.bak && cp /path/to/patched/libnccl.so.2 $LIB   # on BOTH nodes
#   ... run ...
cp $LIB.bak $LIB
```

The reproducer prints the path and md5 of whatever it really mapped, so each leg is
self-verifying.

[proxy-flush-before-block.patch](https://github.com/user-attachments/files/31206090/proxy-flush-before-block.patch)

To build the patched library — the attached diff patch applies cleanly to `v2.28.9-1`:

```bash
git clone --depth 1 --branch v2.28.9-1 https://github.com/NVIDIA/nccl.git && cd nccl
git apply /path/to/proxy-flush-before-block.patch
make -j"$(nproc)" src.build NVCC_GENCODE="-gencode=arch=compute_121,code=sm_121"
#   -> build/lib/libnccl.so.2.28.9
```

It does not apply to `v2.31.2-1` — that file moved to C++ synchronisation primitives
and was reformatted. The logic it patches is unchanged there, so I can rebase it
against latest if you prefer.

## Results

Both legs, same command, only the library differs:

| | libnccl md5 | result |
| --- | --- | --- |
| stock | `7afb8ff8c0c3` | **deadlock at iteration 139** |
| patched | `6e86145b4e56` | **20000 iterations in 8.2 s** |

Stock, rank 1 — frame-for-frame what we captured from the production hang:

```
[rank 1] DEADLOCK: no progress for 120s at iteration 139
#0  __sched_yield
#1  ncclLocalOpAppend(ncclComm*, ncclProxyConnector*, ncclProxyOp*)
#2  SaveProxy(...)  #3 ncclProxySaveOp(...)  #4 uploadProxyOps(...)
#5  hostStreamPlanTask(...)  #6 ncclLaunchKernelAfter_NoCuda(...)
#7  groupLaunch(...)  #8 ncclGroupEndInternal(...)  #9 ncclEnqueueCheck(...)
#10 pncclAllGather
[rank 1] ncclLocalOpAppend: PRESENT
[rank 1] ncclProxyGetPostedOps: PRESENT
```

NCCL logs nothing at all when this happens — no WARN, no timeout, no async error.

## Why it dumps its own stacks

**Exit 9 alone does not mean this bug.** The watchdog only knows "no progress for N
seconds", and unrelated problems look identical: our first run reported a deadlock at
iteration 0, and the stack showed it parked in `bootstrapInit -> ncclSocketAccept ->
accept` because the peer had failed to start.

So gate on the probes, not the exit code:

```
ncclLocalOpAppend: PRESENT        # main thread stuck appending
ncclProxyGetPostedOps: PRESENT    # that rank's own proxy thread asleep
```

Both PRESENT on the same rank is the signature. Anything else is a different problem,
and the dumped stack will say what.

## Knobs

- `--lead N` — how far rank 1 may run ahead before catching up. Must exceed
  `MAX_OPS_PER_PEER / nChannels` (128 with 16 channels) or the pool never fills.
- `--elems N` — all_gather input elements per rank; default 64Ki bf16 = 128 KiB,
  small so enqueue outruns the network.
- `--timeout N` — seconds without progress before declaring a stall. 90-120 works
  for us.
- `--iters N` — 20000 completes in ~8 s patched.

## Environment

2 x DGX Spark (GB10, sm_121), 1 GPU per node, aarch64. Driver 580.173.02, CUDA
13.0.88, PyTorch 2.11.0+cu130, NCCL 2.28.9+cuda13.0 from the `nvidia-nccl-cu13`
wheel. ConnectX-7 200 Gb/s back-to-back, dual-rail RoCE v2, 16 collective channels
alternating across rails. Containers on Ubuntu 24.04.

Reproduces identically through PyTorch's `ProcessGroupNCCL` and through vLLM's own
NCCL wrapper, so it is not specific to either. Nothing in the mechanism looks
platform-specific, but we have only run it here.

### michaelmanly · 2026-08-19

@Cryspia 
This is perfect, thanks. The stack signature check makes this a lot cleaner than just treating exit 9 as the result.

I can map this into a Badgr Smoke Test so the stock and patched cases run the same way and report the actual deadlock signature rather than just pass or fail. You’d run it against your own two nodes.

Want me to put the command together?

### thomasgillis · 2026-08-19

@Cryspia thanks for the analysis. could you share here your nccl-only repro code?
AFAICT the code should already prevent this form appending by flushing the local ops when the last free element is enqueued. I am not sure why this is not happening and therefore the hang you have reported is observed.

### Cryspia · 2026-08-20

> [@Cryspia](https://github.com/Cryspia) thanks for the analysis. could you share here your nccl-only repro code? AFAICT the code should already prevent this form appending by flushing the local ops when the last free element is enqueued. I am not sure why this is not happening and therefore the hang you have reported is observed.

[nccl_proxy_pool_deadlock.py](https://github.com/user-attachments/files/31206078/nccl_proxy_pool_deadlock.py)

Repro attached — `nccl_proxy_pool_deadlock.py`. Two ranks, one collective in a
loop, `torch` and the standard library only, no model or framework:

```bash
# same on both nodes, only --node_rank differs.
# --node_rank must come BEFORE the script name, or torchrun never sees it and
# both ranks default to 0 and hang in rendezvous with no output.
torchrun --nnodes=2 --node_rank=0 --nproc_per_node=1 \
         --master_addr=<node0-ip> --master_port=29500 \
         nccl_proxy_pool_deadlock.py --iters 20000 --lead 4096
```

Exit 0 = completed, 9 = stalled. Give it `elfutils` + CAP_SYS_PTRACE and it dumps
its own stacks on stall, and prints two probe lines — gate on those rather than on
the exit code, since "no progress for N seconds" also matches, say, a peer that
failed to start:

```
ncclLocalOpAppend: PRESENT        # main thread stuck appending
ncclProxyGetPostedOps: PRESENT    # that rank's own proxy thread asleep
```

On 2.28.9 here: stock deadlocks at iteration 139/313/553 across runs; with the
flush patch, 20000 iterations in 8.2 s.

## On the existing flush

You're right that it exists — `ncclProxyStart()` posts every pending chain and
resets `count`, and `hostStreamPlanTask()` calls it immediately after
`uploadProxyOps()`:

```c
  if (ncclIntruQueueHead(&plan->proxyOpQueue)) {
    NCCLCHECK(uploadProxyOps(comm, plan));
    NCCLCHECK(ncclProxyStart(comm));
  }
```

I think it does not save us for two reasons, and the second is the interesting one.

**1. It is only reached after `uploadProxyOps` returns.** If the pool runs dry
*during* that call, `ncclLocalOpAppend` blocks in its `sched_yield()` loop and the
`ncclProxyStart` on the next line is never executed.

**2. The in-append post triggers on `count`, but exhaustion is driven by something
`count` does not track.** `ncclProxyStart` sets `ops->count = 0` on every plan, so
`count` is effectively a *per-plan* counter. Free ops, on the other hand, only come
back once the proxy has **completed** an op — and completion needs the peer to
reach the matching collective. A rank that is running ahead therefore accumulates
in-flight-but-incomplete ops *across* plans while its per-plan `count` stays tiny.

So `count` never approaches `MAX_OPS_PER_PEER` and the post at that threshold
cannot fire, even though the pool is empty. In our repro each iteration is one
all_gather over 16 channels ≈ 16 proxy ops, and it wedges at iteration 139:

```
139 x 16 = 2224 ops in flight   vs   MAX_OPS_PER_PEER = 2*64*2*8 = 2048
```

while `count` at that moment is on the order of the ops in the current plan — tens,
not thousands. The other stall points we saw (313, 553) are the same picture with a
different amount of the lead already drained.

That is also why flushing before the wait works empirically: it posts the pending
chain, the proxy starts those ops, the peer's matching collectives can complete,
and free ops come back. It breaks the cycle rather than enlarging the pool.

If that reading is wrong I would like to know where — the part I am least sure of
is whether there is some other path that returns free ops without the op having
completed, which would invalidate point 2.

## This asymmetry is the normal vLLM path, not something we constructed

Worth stressing, since a synthetic reproducer invites the question: we did not
invent the "one rank syncs, the other does not" pattern to provoke this. We found
the hang first, in ordinary production serving, and only then wrote a reproducer
that isolates the mechanism.

In vLLM the asymmetry is an explicit optimisation. Output is collected from a
single rank:

```python
# vllm/v1/executor/multiproc_executor.py
# OPTIMIZATION: Get output only from a single worker (output_rank)
...
if output_rank is not None:
    response_mqs = (response_mqs[output_rank],)

def _get_output_rank(self) -> int:
    # Only returns ModelRunnerOutput from TP rank=0 and PP rank=-1
```

and fetching that output blocks on a device sync:

```python
# vllm/v1/worker/gpu/async_utils.py
def get_output(self) -> ModelRunnerOutput:
    self.copy_event.synchronize()
```

So TP rank 0 blocks on `copy_event.synchronize()` once per decoding step to bring
sampled tokens back to the host, and the other TP ranks never do — their output is
deliberately not collected. Every vLLM tensor-parallel deployment runs this way by
default; nothing in our configuration selects it.

Measured on our two-rank setup with the flight recorder, rank 1 sat a steady **61
collectives ahead of rank 0 on every healthy step**. The lead is not a pathology —
it is the intended behaviour of the optimisation — it just happens to be unbounded
with respect to the proxy op pool.

For completeness, the two production hangs were on ordinary traffic and on quite
different work: one on a fresh 8412-token prefill, the other on an 8-token decode
step with 7 speculative tokens. Roughly one occurrence per 24-33 hours of serving.

## What the ranks look like when wedged

```
rank 1 main thread                    rank 1 proxy thread
__sched_yield                         pthread_cond_wait
ncclLocalOpAppend                     ncclProxyGetPostedOps
SaveProxy                             ncclProxyProgress
ncclProxySaveOp
uploadProxyOps                        rank 0 proxy thread
hostStreamPlanTask                    __sched_yield  (idle, no work)
ncclLaunchKernelAfter_NoCuda
groupLaunch
ncclGroupEndInternal
ncclEnqueueCheck
pncclAllGather
```

`pool->nextOps == -1` on rank 1, which is why its proxy is asleep: everything
previously posted has already been consumed. Those consumed ops just cannot be
completed yet, so they are never returned to the free list.

No NCCL WARN, no timeout, no async error at any point. Both GPUs sit at 96% and the
RoCE byte counters do not move at all.


### Cryspia · 2026-08-20

```bash
> [@Cryspia](https://github.com/Cryspia) This is perfect, thanks. The stack signature check makes this a lot cleaner than just treating exit 9 as the result.
> 
> I can map this into a Badgr Smoke Test so the stock and patched cases run the same way and report the actual deadlock signature rather than just pass or fail. You’d run it against your own two nodes.
> 
> Want me to put the command together?
```

Yes, please. I am not sure what a Badgr Smoke Test is, but would love to help if the test can contribute to the problem solving.

### thomasgillis · 2026-08-20

@Cryspia thanks, I will try to reproduce on our systems.
To be clear, my concern is that the code already implement the logic of posting the existing list as it reaches the MAX_OPS_PER_PEER value: https://github.com/NVIDIA/nccl/blob/7b83616df3ae082a1f32bb74c27458bfe8153a13/src/proxy.cc#L525

### thomasgillis · 2026-08-20

I have tried to reproduce the hang without success (the following C code removes the pytorch layer and uses NCCL directly).
My repro command used 2 nodes (1 GPU/node), `100 000` iterations and lead = 0:

```bash
nccl_proxy_pool_deadlock --iters 100000 --lead 0
```
@Cryspia pls give a try to the following repro code and let me know if it hangs on your system. Also which system as you using? Can you share the full NCCL logs (`NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ENV,NET,GRAPH`). Thanks you!

[nccl_proxy_pool_deadlock.c](https://github.com/user-attachments/files/31274142/nccl_proxy_pool_deadlock.c)

### Cryspia · 2026-08-21

```bash
> I have tried to reproduce the hang without success (the following C code removes the pytorch layer and uses NCCL directly). My repro command used 2 nodes (1 GPU/node), `100 000` iterations and lead = 0:
> 
> nccl_proxy_pool_deadlock --iters 100000 --lead 0
> [@Cryspia](https://github.com/Cryspia) pls give a try to the following repro code and let me know if it hangs on your system. Also which system as you using? Can you share the full NCCL logs (`NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=INIT,ENV,NET,GRAPH`). Thanks you!
> 
> [nccl_proxy_pool_deadlock.c](https://github.com/user-attachments/files/31274142/nccl_proxy_pool_deadlock.c)
```

Ran your C repro on our systems. **It does not hang here** — which is itself useful,
because it narrows things a lot.

Everything below ran back to back on the same two machines within a few minutes,
same NCCL build, same environment. (Our containers have no MPI launcher, so your
file was compiled unchanged against a small shim that only replaces bootstrap —
rank/size from env, `ncclUniqueId` over TCP, barrier as a byte each way. Happy to
attach it if you want to check it changes nothing.)

| repro | `--lead` | result | log |
| --- | --- | --- | --- |
| your C | 0 | 100000 iterations in 39.2 s — **no hang** | [c-ok-rank0.log](https://github.com/user-attachments/files/31289189/c-ok-rank0.log) |
| your C | 4096 | 20000 iterations in 6.7 s — **no hang** | [c-ok-rank1.log](https://github.com/user-attachments/files/31289191/c-ok-rank1.log) |
| our Python | 4096 | **hangs at iteration 179**, both probes PRESENT | [python-hang-rank0.log](https://github.com/user-attachments/files/31289192/python-hang-rank0.log) |
| our Python, rank 0 syncing instead of `.item()` | 4096 | **hangs at iteration 211**, both probes PRESENT | [python-hang-rank1.log](https://github.com/user-attachments/files/31289190/python-hang-rank1.log) |

## What differs between the two loops

They are the same shape — same dtype, same 65536 elements, same world size, same
rank-0-syncs/rank-1-does-not asymmetry:

```c
// yours
ncclAllGather(src, dst, elems, ncclBfloat16, comm, stream);
if (rank == 0) cudaStreamSynchronize(stream);
```
```python
# ours
dist.all_gather_into_tensor(dst, src)
if rank == 0: _ = dst[0].item()
```

The first thing we checked was the D2H copy in `.item()`, since that is an extra
operation on the stream that your version does not have. **It is not that** —
replacing it with a plain `torch.cuda.synchronize()`, which makes our loop
structurally identical to yours, still hangs (iteration 211 above).

The fabric negotiation is also identical: both get `8 coll channels`, same rails,
same init output. Logs for both attached.

So what is left is what PyTorch's `ProcessGroupNCCL` does around the call that a
direct `ncclAllGather` does not. The candidates we have not eliminated, roughly in
order of how much we suspect them:

1. It runs the collective on its **own internal stream**, not the caller's, and
   couples them with events — so the enqueue is not paced by the same stream the
   host later synchronises on.
2. It wraps each collective in `ncclGroupStart`/`ncclGroupEnd`.
3. Its watchdog thread polls `ncclCommGetAsyncError` on a timer.

If any of those is easy for you to bolt onto your C version, that would probably
settle it faster than anything we can do from outside. We are glad to run whatever
variant you want on this hardware.

## Two corrections to my previous message

**The `count` argument does not hold up.** I claimed `count` cannot reach
`MAX_OPS_PER_PEER` because `ncclProxyStart` resets it per plan. Reading further,
free ops appear to be returned when the proxy *dequeues* posted ops in
`ncclProxyGetPostedOps`, not when they complete — and a proxy asleep in
`pthread_cond_wait` requires `state->active == NULL`, so it should already have
returned everything it took. I cannot reconcile that with the stack we captured, so
please treat my mechanism story as unexplained rather than established.

**The arithmetic was wrong.** I quoted 16 channels; that was from our vLLM
deployment, and the standalone repro negotiates 8. The "139 x 16 = 2224 vs 2048"
line does not apply to it.

What is not in doubt is the observation: one rank spinning in `ncclLocalOpAppend`
while its own proxy thread sleeps in `ncclProxyGetPostedOps`, zero bytes on the
wire, no NCCL warning — and flushing before the wait makes it go away (20000
iterations clean, plus 1546 requests over 150 minutes of real serving with no
recurrence).

## System

2 x NVIDIA DGX Spark, **GB10 (sm_121), 1 GPU per node**, aarch64. Driver 580.173.02,
CUDA 13.0.88, NCCL 2.28.9+cuda13.0 (`nvidia-nccl-cu13` wheel), PyTorch 2.11.0+cu130,
Ubuntu 24.04.4, kernel 6.17.0-1029-nvidia, Docker.

ConnectX-7 **back-to-back, no switch**, 200 Gb/s. Multi-host mode, so the kernel
exposes two RDMA devices (`rocep1s0f0`, `roceP2p1s0f0`) on **two disjoint /24s**;
both go to `NCCL_IB_HCA`, `NCCL_IB_GID_INDEX=3`, RoCE v2.

Non-default settings, all forced by the platform:

```
NCCL_CUMEM_ENABLE=0        # GB10 cannot load nvidia-peermem and its allocator
NCCL_NVLS_ENABLE=0         # does not export dmabuf handles
NCCL_IB_GID_INDEX=3
NCCL_CROSS_NIC=1
```

### xiaofanl-nvidia · 2026-08-23

++ @thomasgillis 

### thomasgillis · 2026-08-24

I will try to add all the missing goodies and see which one triggers the hang

### thomasgillis · 2026-08-26

@Cryspia I haven't been able to reproduce the issue.
However, I see that you use an "old" NCCL (2.28) while we have added fixes for `aarch64` in the newest version. Can you try with 2.32.2? 

EDIT: we solved 2 bugs recently in that part of the code, here are the related commits:
- 2.28.9: https://github.com/NVIDIA/nccl/commit/dbc86fd06e8b0c4517b95d8958a09ccacf9520c9
- 2.29.3: https://github.com/NVIDIA/nccl/commit/25368a7f78bae866f29e46938af94fa586c84484

### Cryspia · 2026-08-27

```bash
> [@Cryspia](https://github.com/Cryspia) I haven't been able to reproduce the issue. However, I see that you use an "old" NCCL (2.28) while we have added fixes for `aarch64` in the newest version. Can you try with 2.32.2?
> 
> EDIT: we solved 2 bugs recently in that part of the code, here are the related commits:
> 
> * 2.28.9: [dbc86fd](https://github.com/NVIDIA/nccl/commit/dbc86fd06e8b0c4517b95d8958a09ccacf9520c9)
> * 2.29.3: [25368a7](https://github.com/NVIDIA/nccl/commit/25368a7f78bae866f29e46938af94fa586c84484)
```

Confirmed fixed — `25368a7f` is it. Bisected the released `nvidia-nccl-cu13`
aarch64 wheels with our reproducer:

| NCCL   | result |
|--------|--------|
| 2.28.9 | deadlock |
| 2.29.2 | deadlock (3/3 runs) |
| 2.29.3 | no deadlock (2/2, 20000 iters in ~8 s) |
| 2.30.7 | no deadlock (4/4) |

The boundary is exactly 2.29.2 → 2.29.3.

Two notes:

- `dbc86fd0` is the v2.28.9-1 release commit itself, so it is already in the
  version we reproduce on — not the fix for this one.
- The weak-CAS bug explains the aarch64-only behaviour: on a spurious failure
  the loop exits as if the CAS succeeded, leaking the freed op chain until the
  pool drains and `ncclLocalOpAppend` waits forever. Spurious failure is an
  LL/SC artifact, so x86 never sees it.

We couldn't test 2.32.2 (no such tag in the public repo — master is v2.31.2-1
— and no wheel on PyPI), but ≥2.29.3 is clearly fine. Good to close from our
side. Thanks for the quick pointer.


### thomasgillis · 2026-08-28

Thanks for the confirmation, I am closing the issue then.
