# [Issue #2179] [BUG] Deterministic deadlock: CUDA graph + multi-stream + multi-comm + IB transport on gfx1100

source: https://github.com/ROCm/rccl/issues/2179
state: closed | updated: 2026-05-29T18:23:06Z
labels: 

## 正文

# [BUG] Deterministic deadlock: CUDA graph + multi-stream + multi-comm + IB transport on gfx1100

**RCCL version**: 7.2.3 (also confirmed against pristine upstream tree)
**ROCm**: 7.2.3
**HIP**: 7.2.53211-ebb5915
**PyTorch**: 2.11.0+riscv64.rocm
**GPU**: AMD Radeon RX 7900 XTX (gfx1100), 2 GPUs across 2 nodes
**NIC**: Mellanox CX-7 (RoCE), 2 ports
**Transport**: NCCL_NET=IB (RoCE)
**Host platform**: 2x QEMU/VFIO RISC-V VMs (each with 1 GPU + 1 NIC port via VFIO)

## TL;DR

When CUDA graphs that share a single `ncclComm` are replayed concurrently
from multiple streams across nodes over IB/net transport, RCCL
**deterministically** deadlocks. We hit this in production with vLLM 0.21
serving Qwen3.6-27B-INT8 TP=2 cross-node, where 4 concurrent OpenAI-API
requests hang after ~10 s. We have isolated the bug to a 120-LOC Python
reproducer with no model / no vLLM / no PyTorch inductor.

The root cause is a per-comm device-side state race in the NCCL kernel
(`channels[ch].workCounter`, `conn->step`). NCCL's framework-level
serialization mechanism (`launchOrder` strong stream) is bypassed in the
CUDA-graph code path, allowing concurrent in-flight kernels on the same
comm to race the per-channel state. P2P transport (NVLink/XGMI) tolerates
this race because data flows GPU↔GPU directly; proxy-mediated transports
(IB/net) require strict CPU↔GPU head/tail discipline and deadlock.

## 1. Real-world reproduction: vLLM 0.21 + Qwen3.6-27B-INT8 TP=2

This is the production scenario that surfaced the bug.

### Setup

- **Model**: Qwen3.6-27B-VL Quark W8A8-INT8 (`/data/Qwen3.6-27B-Quark-W8A8-INT8`)
- **vLLM**: `0.21.1.dev0+gad7125a43` (vLLM v1 engine)
- **Parallelism**: TP=2, one GPU per VM (cross-VM, one NIC port each)
- **NCCL comms created at init**: 2 (`_WORLD` size=2 + `_TP` size=2; both
  cover the same 2-rank set, so both get real ncclComms)
- **CUDA graph mode**: `FULL_DECODE_ONLY` (full graph for decode, eager for
  prefill). Capture sizes `[1, 2, 4, 8]` → 4 captured graphs that share
  the same TP/WORLD comms.

### Launch (rank 0 / leader)

```bash
source /home/ubuntu/vllm-serve-env.sh        # PyTorch 2.11 + ROCm 7.2.3 venv
unset NCCL_TOPO_FILE NCCL_P2P_DISABLE NCCL_SHM_DISABLE
export NCCL_IB_DISABLE=0 NCCL_IB_HCA=roceP3p1s0 NCCL_NET=IB \
       NCCL_IB_GID_INDEX=3 \
       NCCL_SOCKET_IFNAME=enP3p1s0np0 \
       GLOO_SOCKET_IFNAME=enP3p1s0np0 \
       TP_SOCKET_IFNAME=enP3p1s0np0 \
       VLLM_HOST_IP=10.99.0.1

python -m vllm.entrypoints.openai.api_server \
    --model /data/Qwen3.6-27B-Quark-W8A8-INT8 \
    --served-model-name qwen3_6-27b-int8 \
    --quantization quark --dtype bfloat16 \
    --max-model-len 2048 --max-num-seqs 8 --max-num-batched-tokens 2048 \
    --gpu-memory-utilization 0.85 \
    --tensor-parallel-size 2 --nnodes 2 --node-rank 0 \
    --master-addr 10.99.0.1 --master-port 29500 \
    --distributed-executor-backend mp --trust-remote-code \
    --no-enable-prefix-caching \
    --mm-processor-kwargs '{"max_pixels":451584,"min_pixels":3136}' \
    --disable-custom-all-reduce \
    --compilation-config '{"mode":0,"cudagraph_mode":"FULL_DECODE_ONLY","cudagraph_capture_sizes":[1,2,4,8],"max_cudagraph_capture_size":8,"cudagraph_num_of_warmups":0}' \
    --host 0.0.0.0 --port 8000
```

### Launch (rank 1 / headless follower)

Mirror of the above, with `--node-rank 1`, `--headless`, and
`NCCL_SOCKET_IFNAME=enP3p1s0np1`, `VLLM_HOST_IP=10.99.0.2`.

### Triggering the hang

After both ranks reach "Application startup complete", fire 4 concurrent
streaming completion requests:

```bash
for i in $(seq 4); do
  curl -sN http://127.0.0.1:8000/v1/chat/completions \
    -H 'content-type: application/json' \
    -d "{\"model\":\"qwen3_6-27b-int8\",\"messages\":[{\"role\":\"user\",
         \"content\":\"Write 300 words about $i.\"}],
         \"max_tokens\":300,\"stream\":true}" &
done; wait
```

(any concurrent OpenAI-compatible client works — `vegeta`, `hey`, asyncio
script, etc.)

### Observed behavior

- **N=1, N=2**: stable indefinitely.
- **N≥4**: deterministic hang **after ~10 s of generation** (~85 cudagraph
  replays). vLLM then logs:

  ```
  EngineCore INFO shm_broadcast.py:681 No available shared memory broadcast
  block found in 60 seconds. This typically happens when some processes
  are hanging or doing some time-consuming work …
  ```

  (repeated every 60 s — it's a real hang, not a stall).

- NCCL trace shows the TP comm's `AllReduce` opCount stops advancing at
  ~`0x2a45` (~10,821). Each cudagraph replay issues ~128 AllReduces (64
  transformer layers × 2 AR/layer), so `10821 / 128 ≈ 85` replays.

- The two ranks are **asymmetric**: rank 1 queued ~119 ops past where
  rank 0 stopped — rank 1 fire-and-forget'd ahead, rank 0 is stuck.

## 2. Control experiments (isolation matrix)

Same hardware, same RCCL build, same NCCL env vars. Toggled one variable
at a time:

| Variable | Result |
|----------|--------|
| `--enforce-eager` / `cudagraph_mode=NONE` | ✅ Stable. `agg_tps=1.0`, `ok_clients=4/4`, `garbage_clients=0`. Throughput ~18× slower than cudagraph mode but **no hang** |
| Cudagraph + N=1 only (single client) | ✅ Stable indefinitely |
| Cudagraph + N=2 concurrent | ✅ Stable (≥200 iters in minimal repro, no hang in vLLM at small batch) |
| Cudagraph + N=4 + IB cross-node | ❌ **HANG (the bug)** |
| Cudagraph + N=4 + same-host P2P (NVLink/XGMI) | ✅ Stable (user-confirmed) |
| Cudagraph + N=4 + IB + **one comm per stream** (`new_group`) | ✅ Stable. **Same hardware/RCCL — only thing changed is comm sharing.** |

**Decisive A/B**: same RCCL, same N=4, same cudagraph, same IB, same
nranks, same op pattern. Only difference is whether the captured graphs
share a `ncclComm` or each gets its own `dist.new_group`:

```
┌─────────────────────────────────────────┬─────────────────┐
│  Setup                                   │  Result         │
├─────────────────────────────────────────┼─────────────────┤
│  shared ncclComm across 4 streams        │  HANG iter 0→1  │
│  4 distinct new_group, one per stream    │  DONE 30/30     │
└─────────────────────────────────────────┴─────────────────┘
```

This isolates the bug to **per-comm device-side state being raced across
concurrent in-flight kernels of the same comm**.

## 3. Minimal 120-LOC reproducer

Distillation of the vLLM scenario — no model, no vLLM, no inductor.
Reproduces 100% deterministically.

```python
# repro_cudagraph_ib_deadlock.py
import argparse, os, time
import torch, torch.distributed as dist

def parse():
    p = argparse.ArgumentParser()
    p.add_argument('--n-streams', type=int, default=4)
    p.add_argument('--ops-per-step', type=int, default=128)
    p.add_argument('--ar-count', type=int, default=20480)
    p.add_argument('--ag-count', type=int, default=496640)
    p.add_argument('--iters', type=int, default=200)
    p.add_argument('--no-capture', action='store_true', help='Eager.')
    p.add_argument('--no-cp', action='store_true', help='Skip 2nd comm.')
    return p.parse_args()

def main():
    args = parse()
    rank = int(os.environ['RANK']); world = int(os.environ['WORLD_SIZE'])
    dist.init_process_group('nccl',
        init_method=f"tcp://{os.environ['MASTER_ADDR']}:{os.environ['MASTER_PORT']}",
        world_size=world, rank=rank)
    comm_cp = None if args.no_cp else dist.new_group(list(range(world)),
                                                     backend='nccl')

    device = torch.device('cuda:0')
    ar_buf = torch.ones(args.ar_count, dtype=torch.bfloat16, device=device)
    ag_input = torch.ones(args.ag_count, dtype=torch.bfloat16, device=device)
    ag_output = torch.empty(args.ag_count * world,
                            dtype=torch.bfloat16, device=device)

    def step_body():
        for _ in range(args.ops_per_step):
            dist.all_reduce(ar_buf, op=dist.ReduceOp.SUM)
        if comm_cp is not None:
            dist.all_gather_into_tensor(ag_output, ag_input, group=comm_cp)

    for _ in range(3):                # warmup JIT
        step_body(); torch.cuda.synchronize()

    if not args.no_capture:
        graphs, streams = [], []
        for s in range(args.n_streams):
            stream = torch.cuda.Stream()
            with torch.cuda.stream(stream):
                g = torch.cuda.CUDAGraph()
                with torch.cuda.graph(g, stream=stream):
                    step_body()
            graphs.append(g); streams.append(stream)

    for it in range(args.iters):
        t0 = time.time()
        if args.no_capture:
            for s in range(args.n_streams):
                with torch.cuda.stream(streams[s] if it else torch.cuda.Stream()):
                    step_body()
        else:
            for s in range(args.n_streams):
                with torch.cuda.stream(streams[s]):
                    graphs[s].replay()
        torch.cuda.synchronize()
        dt = time.time() - t0
        if it < 20 or it % 5 == 0:
            print(f'[rank{rank}] iter {it:3d} wall={dt*1000:.1f}ms',
                  flush=True)
        if dt > 30:
            print(f'[rank{rank}] HANG at iter {it}', flush=True); break
    print(f'[rank{rank}] DONE iters={args.iters}', flush=True)

if __name__ == '__main__': main()
```

Launcher:

```bash
# rank 0 (node A)
RANK=0 WORLD_SIZE=2 MASTER_ADDR=10.99.0.1 MASTER_PORT=29500 \
  NCCL_NET=IB NCCL_IB_HCA=roceP3p1s0 NCCL_IB_GID_INDEX=3 \
  NCCL_SOCKET_IFNAME=enP3p1s0np0 \
  python repro_cudagraph_ib_deadlock.py --n-streams 4 --iters 200

# rank 1 (node B) — mirror, RANK=1, NCCL_SOCKET_IFNAME=...np1
```

**Result with `--n-streams 4`: HANG at iter 0→1 (deterministic, 100% repro).**

### Mapping vLLM → minimal repro

| vLLM | Minimal repro |
|------|---------------|
| 4 captured graphs (one per `capture_size ∈ {1,2,4,8}`) | 4 captured graphs (one per stream) |
| 2 ncclComms (`_WORLD` AG + `_TP` AR) | 2 ncclComms (default group AR + `comm_cp` AG) |
| TP=2 cross-VM via IB | 2 ranks cross-VM via IB |
| 64 layers × 2 AR + 1 AG per replay | 128 AR + 1 AG per replay |
| N=4 concurrent requests → 4 in-flight graphs | `--n-streams 4` replays 4 graphs concurrently |
| HANG after ~85 replays | HANG after 5–20 iters (each iter does more ops) |

## 4. Observed hang state (gdb on both ranks)

CPU proxy threads on both ranks are in `sched_yield()` inside
`ncclProxyProgress` at `proxy.cc:995`. All active ops report `idle=1`
because they're each waiting for the other rank or for the GPU. From
`thread apply all bt 4` + custom dump scripts:

```
Rank 0 (VM1) TP comm, 4 active ops at opCount=2300:
  RECV ch=1: base=1150 posted=1 recvd=0    (waiting on rank 1 SEND ch=1)
  RECV ch=0: base=1150 posted=1 recvd=1 txd=1 done=0
                                           (data flushed, GPU has not
                                            advanced sendMem->head)
  SEND ch=0: base=1150 posted=1 txd=0      (GPU hasn't written connFifo)
  SEND ch=1: base=1150 posted=1 txd=0      (same)

Rank 1 (VM2) TP comm:
  SEND ch=0: base=1151 txd=0   (1 op ahead — GPU wrote 2 slots to
                                 connFifo, but matching IB-fifo on remote
                                 not posted by rank 0)
  others stuck same way
```

IB-level `ncclIbSendComm::fifo` inspection confirms the inter-rank symptom:
3 of 4 SEND directions show `slot.idx == fifoHead+1` (matching receiver
already posted `ncclIbPostFifo` over RDMA), but the local GPU has not
written the corresponding `connFifo[slot].size`, so `sendProxyProgress`
cannot post an `isend`. The CPU proxy is doing the right thing — it's
literally waiting for the GPU.

## 5. Suspected root cause (kernel-side per-comm state race)

The NCCL kernel reads and writes per-comm device-side state without
atomics or device-side serialization. With concurrent kernels in flight
on the same comm (one per replayed graph), the RMW races.

### `channels[ch].workCounter` race

Read at kernel entry (`src/device/common.h:552`):
```c
if (tid == 0) {
    ncclShmem.aborted = 0;
    ncclShmem.channel.workCounter =
      ((ncclDevCommAndChannels*)ncclShmem.args.comm)
        ->channels[ncclShmem.channelId].workCounter;
}
```

Written at FINI (`src/device/common.h:480`):
```c
ncclShmem.channel.workCounter += ncclShmem.nWorks;
if (action == FINI)
  ((ncclDevCommAndChannels*)ncclShmem.args.comm)
    ->channels[ncclShmem.channelId].workCounter =
    ncclShmem.channel.workCounter;
```

Plain read → modify → write, no atomic. With N concurrent kernels, all
read the same value, increment locally, write back the same value →
lost increments.

### `conn->step` race

Read in primitive init (`src/device/prims_simple.h:665` and `:710`):
```c
step = conn->step;
step = roundUp(step, SlicePerChunk*StepPerSlice);
```

Written at primitive destructor (`prims_simple.h:886`):
```c
if (flags & (RolePostSend|RolePostRecv)) conn->step = step;
```

Same RMW pattern. `step` then drives buffer-slot index
`(step % NCCL_STEPS)` for `connFifo[slot]` writes (e.g., `prims_simple.h:155`).
Concurrent kernels reading the same starting `step` write to overlapping
buffer slots → data corruption + tail/head flags out of sync → CPU proxy
view diverges from GPU view → deadlock.

### Why this race isn't normally prevented

NCCL's framework has a `launchOrder` strong-stream mechanism specifically
designed to serialize kernel launches per (context, comm). At
`src/enqueue.cc:1729`:

```c
if (implicitOrder != ncclImplicitOrderNone) {
    bool concurrent = capturing;       // <-- problem
    ncclStrongStreamAcquire(planner->capturingGraph,
                            &comm->context->launchOrder,
                            concurrent, &launchOrder);
    ncclStreamWaitStream(launchStream, launchOrder, ...);
}
```

Two issues, either of which would alone prevent the mechanism from
kicking in:

1. **`NCCL_LAUNCH_ORDER_IMPLICIT` defaults to `0`** at
   `src/enqueue.cc:1604`, causing `implicitOrder == ncclImplicitOrderNone`
   and the entire serialization block to be **skipped**.

2. **Even when enabled, in capture mode `concurrent=true`**, so each
   captured graph acquires its own `captureStream` from the strong stream
   (`src/misc/strongstream.cc:148`+) — there is no cross-graph
   dependency, so distinct graphs replay concurrently.

Net effect: in default config, captured graphs sharing a comm replay with
no serialization at all, racing the per-comm device state.

## 6. Hypotheses ruled out

| Hypothesis | Status |
|------------|--------|
| CPU proxy state-machine bug | Refuted — proxy state is internally consistent at hang |
| `resources->step` (CPU side) race | Refuted — all conns show consistent values; the "non-monotonic base" in `nextPeer` chain is stale `allocateArgs` pool memory (memset commented out at `proxy.cc:376`) |
| `hostStreamPlanCallback` not re-fired on replay | Refuted — added a counter; it fires every replay |
| GDR / HDP cache stale on gfx1100 | Refuted — `RCCL_NET_HDP_FLUSH=1` only extends progress (step ~1150 → ~1400), then hangs the same way. Buffers are GPU VRAM via GDR, not system memory through HDP cache |
| `comm->sharedRes->collOpCount` RMW race in host callback | Partial — adding `pthread_mutex_lock` around `uploadProxyOps + ncclProxyStart` slightly delays the hang but doesn't fix it. **Confirms the dominant race is device-side, not host-side.** |

## 7. Attempted fixes and outcomes

1. **Set `NCCL_LAUNCH_ORDER_IMPLICIT=1` (env)** — deterministic SIGSEGV in
   `ncclSocketProgress` inline `WARN` call, exact PC `0x4e318eac`, every
   retry / both ranks. There appears to be a **separate** AMD/HIP-path bug
   in the `launchOrder` activation path that surfaces when this feature
   is turned on. This blocks the obvious "use the existing mechanism"
   fix.

2. **Source patch: force `concurrent = false` for `launchOrder` even
   during capture** — same SIGSEGV signature as (1). Confirms the crash
   is in the `launchOrder` code path itself, not the env-parsing.

3. **Source patch: capture-time `cudaStreamWaitEvent(launchStream,
   comm->doneEvent)` in `ncclLaunchPrepare`** — built/tested, hang
   persists. CUDA event semantics ("wait for last record") are
   insufficient to serialize concurrent graph replays; the wait is
   satisfied by the previous iteration's record and all replays proceed
   in parallel.

4. **Source patch: per-channel device-side spin lock added to
   `ncclDevChannel`** — kernel entry `CAS(channels[ch].kernelLock, 0→1)`
   on `tid==0`, FINI `store(0)`.
   - **Fully fixes the minimal repro** (`DONE iters=30`, no perf drop
     because tied per-channel).
   - Mitigates vLLM workload (advances **5× further** before hang —
     opCount ~10,800 → ~53,400) but doesn't fully fix it. There are
     additional cross-channel races we have not yet covered.

5. **Source patch: comm-wide spin lock (`channels[0].kernelLock` as
   master)** — deadlocks at init. Every block of every kernel acquires
   the master lock, but blocks of a single kernel rely on a shared
   intra-grid barrier; if one block holds the lock while another spins
   waiting for it, the intra-kernel barrier deadlocks. Per-channel is
   the right granularity; per-channel alone is insufficient.

## 8. Suggested fix paths (for upstream)

In order of preference / risk:

1. **Fix the AMD/HIP-path bug in `launchOrder` activation** so that
   `NCCL_LAUNCH_ORDER_IMPLICIT=1` works on ROCm, and consider changing
   the default to `1` for net (proxy-mediated) transports. This is the
   "right" upstream design — the existing mechanism is just unreachable
   on AMD.

2. **In `ncclLaunchPrepare` (capture path), force `concurrent=false` for
   the `launchOrder` strong stream when the comm uses net transport.**
   Accept the extra capture-time overhead in exchange for correct
   replay-time ordering across graphs.

3. **Device-side atomic claim on `channels[ch].workCounter` and
   `conn->step`** — make each kernel atomically claim a range instead
   of plain RMW. Requires careful work on the primitive layer but
   eliminates the race at its root.

4. **At minimum: explicit documentation** that sharing an `ncclComm`
   across distinct captured CUDA graphs that are replayed concurrently
   is unsupported on net transports. Today this is a silent footgun.

## 9. Workarounds (for affected users today)

- **`--enforce-eager` / `cudagraph_mode=NONE`** in vLLM: verified works
  for vLLM 27B INT8 TP=2 cross-VM N=4 (`agg_tps=1.0`, `ok_clients=4/4`,
  `garbage_clients=0`, no hang). Throughput ~18× lower than cudagraph
  mode.
- **Single stream (`n_streams=1`)** for CUDA-graph workloads on net
  transport: works at ~25–40% throughput cost.
- **Per-stream `new_group` (one comm per captured graph)** at the
  application layer: works (verified). Architecturally invasive in most
  applications.

## Notes

- The hang is **deterministic** (not race-on-timing); wall time to hang
  scales inversely with `n_streams` and with op size / layer count.
- The CPU proxy threads do the right thing at hang time — they are
  literally waiting on the GPU/peer to make progress, not stuck in
  their own state machine. **The bug is on the GPU side.**
- Same-host P2P (NVLink/XGMI) is unaffected: P2P doesn't use proxy-mediated
  head/tail, GPUs write each other's memory directly. The race on
  per-comm state still exists but doesn't manifest as a deadlock.

## Files attached

- `repro_cudagraph_ib_deadlock.py` (~120 LOC) — the minimal repro
- `run_repro.sh` — cross-VM launcher
- `dump_all_proxies.gdb` — proxy-state inspection script for gdb
- Full session timeline and gdb dumps available on request

## Reproduces on

- ✅ **2x AMD 7900 XTX (gfx1100) over RoCE/IB cross-VM (VFIO passthrough,
  QEMU/RISC-V host)** — 100% deterministic.
- ❓ Standard x86 + MI200/MI300 multi-node hardware not tested by us.
  Given the bug is in arch-agnostic kernel code paths gated on a NCCL
  launch-ordering mechanism that is uniformly disabled by default, we
  expect it to reproduce broadly on any net-transport multi-node setup
  that uses captured CUDA graphs sharing a comm.


## 评论 (1)

### thananon · 2026-05-29

Running different replays on multiple streams at the same time without stream synchronization is not what we supported. The workaround is to set stream to 1 which serialized everything. NCCL_LAUNCH_ORDER_IMPLICIT will not help in this use case.
