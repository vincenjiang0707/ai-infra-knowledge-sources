# [Issue #2409] Low AllReduce bandwidth on 2x8x H100 with 8x 400G RoCE: per GPU<->GPU connection capped at ~13 GB/s while perftest reaches 392 Gb/s line rate

source: https://github.com/NVIDIA/nccl/issues/2409
state: closed | updated: 2026-09-16T14:43:39Z
labels: 

## 正文

### Summary

On 2 nodes x 8x H100 (SXM) with 8x ConnectX-7 400 Gb/s RoCEv2 per node (GPUi <-> NICi, all PIX), NCCL reaches only a fraction of the fabric:

| test | result |
|---|---|
| `all_reduce_perf`, 16 ranks x 8 rails, 1 GiB | **216.5 GB/s** busbw (per rail ~27 GB/s) |
| `all_reduce_perf`, 16 ranks x 8 rails, 8 GiB | **231 GB/s** busbw |
| `sendrecv_perf`, 2 ranks, 1 rail, 1 GiB | **13.1 GB/s** (send 6.99 + recv 6.99) |
| `all_gather_perf` / `reduce_scatter_perf`, 256 MiB | ~101 / ~100 GB/s |
| `alltoall_perf`, 256 MiB | ~25 GB/s |

For 2 nodes x 8x400G we would expect ~470 GB/s busbw for AllReduce (cf. nccl-tests #309 results). The same hardware reaches **line rate** with perftest on a single rail, so this looks like a NCCL-side limit rather than a fabric problem. We have not been able to find any supported setting that changes it, and would like to know whether this is expected or whether we are mis-configuring something.

### Environment

| | |
|---|---|
| NCCL | `2.31.2-1+cuda13.3` (md5 `241dc74211d08b2986ad36e478069974`), also reproduced with `2.29.7` |
| nccl-tests | master `a0b82b2260cf5152b9f8c061bbf7eaf0ba096432` |
| GPUs / NICs | 2 x 8x H100 80GB HBM3 SXM; 8x ConnectX-7 400 Gb/s RoCEv2 per node, fw `28.43.8016`, PCIe Gen5 x16, GPUi<->NICi PIX, MTU 9000 |
| Driver / CUDA / OS | `595.71.05` / `13.2` / Ubuntu 24.04, kernel `6.8.0-137-generic` |
| RDMA stack | NVIDIA OFED 24.10 (`mlx5_core` 24.10-5.1.6), `nvidia_peermem` loaded |
| Fabric | single leaf switch (H3C S9827-128DH), PFC + ECN enabled, verified lossless |

### 1. The hardware is not the limit (perftest, same rail)

| test | throughput |
|---|---|
| `ib_write_bw`, host memory, 1 MiB messages | **392.6 Gb/s** unidirectional (= 400G line rate) |
| `ib_write_bw -b` (bidirectional) | **779.6 Gb/s** |
| `ib_write_bw`, 1 / 2 / 4 / 8 MiB messages | 391.47 / 391.47 / 389.23 / 384.76 Gb/s |
| `ib_write_bw --use_cuda` (GPUDirect RDMA, GPU HBM) | **391.47 Gb/s** — identical to host memory |
| `ib_write_bw -t 1` (a single WR in flight, 1 MiB msg) | **307.6 Gb/s** |
| `ib_read_bw --use_cuda` | 389 Gb/s |

So: a single QP moving a single 1 MiB message already achieves 307 Gb/s, i.e. the GPU<->NIC<->switch path is healthy at both line rate and shape depths.

### 2. NCCL scales linearly with the number of *connections*, not with rail speed

Same AllReduce, varying only `NCCL_IB_HCA` (before any tuning):

| rails used | algbw |
|---|---|
| 1 | 27.0 GB/s |
| 2 | 52.8 GB/s |
| 4 | 101.4 GB/s |
| 8 | 178.3 GB/s |

Perfectly linear (~13.4 GB/s per rail, both directions) => the cap is a **per-GPU<->per-NIC connection limit**, not the rail. `NCCL_IB_HCA=mlx5_0` (1 rail) gives 27 GB/s total, i.e. ~13.5 GB/s each way, which matches the 2-rank `sendrecv_perf` number (13.1 GB/s).

### 3. What NCCL is doing (debug output)

`NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=NET`:
* `Using network IB`, `NET/Socket` count = **0** (no TCP fallback), 256 channels `via NET/IB/0..7` evenly
* GDR: `Enabled=2816 Disabled=0`
* built-in WQE latency monitor: `inflight=8` per QP, p50 post-to-poll **~110 us** (bare RDMA round trip on the same rail: 2.9 us)

The 8-step in-flight window is `NCCL_STEPS` (`src/include/device.h:26`, `stepSize = comm->buffSizes[protocol]/NCCL_STEPS` in `src/enqueue/enqueue.cc:1009`). It does **not** change with `NCCL_IB_QPS_PER_CONNECTION` (1..16), `NCCL_MIN_NCHANNELS`/`NCCL_MAX_NCHANNELS` (1..32) or `NCCL_IB_SPLIT_DATA_ON_QPS`.

### 4. Environment variable sweep (all correctness-checked)

Only three settings helped, all on RoCE QP behaviour:

| setting | busbw @1GiB | vs baseline |
|---|---|---|
| default | 178.3 GB/s | — |
| `NCCL_IB_QPS_PER_CONNECTION=8` | 198.4 | +11% |
| `+ NCCL_IB_SPLIT_DATA_ON_QPS=1` | 201.5 | +13% |
| **`+ NCCL_IB_ADAPTIVE_ROUTING=1`** | **218.3** | **+22%** |
| (final, 8 GiB) | 231.0 GB/s | |

No effect (each with correctness check): `NCCL_MIN/MAX_NCHANNELS` (1..32), `NCCL_NTHREADS=512`, `NCCL_BUFFSIZE` (4M -> 64M), `NCCL_ALGO=Ring|Tree`, `NCCL_CROSS_NIC`, `NCCL_NETDEVS_POLICY`, `NCCL_NET_FORCE_MERGE`, `NCCL_IB_SL=3`, `NCCL_IB_TC`, `NCCL_IB_FIFO_TC`, `NCCL_IB_SHARP_ENABLE=1`, `NCCL_COLLNET_ENABLE=1`, `NCCL_IB_GID_INDEX` (has to stay auto here), `NCCL_P2P_NET_CHUNKSIZE`, `NCCL_NVLS_CHUNKSIZE`, `NCCL_NET_GDR_LEVEL=5`, CPU binding (`NCCL_IGNORE_CPU_AFFINITY`), plus 27 further non-documented `NCCL_*` variables found in the binary.

Worse:

| setting | busbw @1GiB |
|---|---|
| `NCCL_NVLS_ENABLE=0` | 112.3 GB/s |
| `NCCL_PROTO=LL128` | 90.9 GB/s |
| `NCCL_NET_GDR_LEVEL=0` | 72.1 GB/s |
| `NCCL_PROXY_CPUSET=32-63` | 42.0 GB/s |
| tuner plugin (example from `plugins/tuner/`) | 36.4 GB/s |
| `NCCL_PROTO=LL` | 22.0 GB/s |
| `NCCL_CUMEM_ENABLE=0` | 153.8 GB/s |

(A third-party transport plugin that does use all 8 NICs per GPU also reached only 190 GB/s, and crashed intermittently.)

### 5. The only knob that actually helps is broken

`NCCL_CHUNK_SIZE` scales a single connection's throughput linearly (13.1 -> 87.6 GB/s at 1 MiB), which is consistent with the ~110 us per-step latency and the tiny per-WQE payload (chunk / `NCCL_IB_QPS_PER_CONNECTION` ~= 16 KiB). But >= 1 MiB it produces wrong results and GPU MMU faults — reported separately in #2408.

### Questions

1. Is ~13 GB/s per GPU<->GPU connection (and hence ~27 GB/s per 400G rail) expected in this configuration? If not, which component is the limiter — the per-step proxy processing, the 8-step window, or something we should be setting?
2. Is there a *supported* way to increase the per-WQE payload or the in-flight window per connection (other than `NCCL_CHUNK_SIZE`, which is unusable per #2408)?
3. Does `NCCL_IB_ADAPTIVE_ROUTING=1` being worth +22% on a **single-leaf** topology (no multipath) indicate that the default flow/QP scheduling is leaving bandwidth on the table? Is there a recommended companion setting (`NCCL_IB_AR_THRESHOLD` had no effect for us at 4096/32768)?

We are happy to run further tests / provide full logs (`NCCL_DEBUG=INFO` dumps, perftest scripts, switch counters) on request.


## 评论 (4)

### Ndministrator · 2026-09-14

**Follow-up: measured the *same message sizes* with perftest — the payload size is not the limiting factor, the cost is a fixed per-step overhead inside NCCL**

`ib_write_bw`, host memory, single rail (mlx5_0), one direction, same node pair as the NCCL numbers above:

| message size | 1 QP | 8 QPs |
|---|---|---|
| 16 KiB | **380.0 Gb/s** | 391.8 Gb/s |
| 128 KiB (= NCCL's step size) | **392.1 Gb/s (line rate)** | 391.8 Gb/s |
| 1 MiB | 284.4 Gb/s | 391.5 Gb/s |

So a **single QP** moving **128 KiB** messages already reaches full line rate (392 Gb/s = 49 GB/s), and even 16 KiB messages reach 380 Gb/s with one QP. NCCL on the same rail reaches ~13 GB/s (105 Gb/s) with 8 QPs at the same 128 KiB step size.

Combining that with:

* chunk 128 KiB -> 13.1 GB/s; chunk 1 MiB -> 87.6 GB/s, i.e. `throughput ≈ chunk / 10..12 us` (the implied per-step cost is the same 10-12 us for both chunk sizes)
* the built-in WQE latency monitor reporting p50 post-to-poll ~110 us with `inflight=8`
* a 16 KiB payload occupying only ~0.3 us of wire time at line rate

this points to a **fixed ~10-12 us per-step cost inside NCCL's data path**, largely independent of message size, chunk size and QP count — not to anything in the fabric, in the message size, or in the bytes per WQE.

So the question is really: *what costs ~10 us per step, and can more steps be in flight (or the step handoff made cheaper)?* `NCCL_BUFFSIZE` (4M -> 64M, would enlarge the step), `NCCL_MIN/MAX_NCHANNELS` (1..32) and `NCCL_IB_QPS_PER_CONNECTION` (1..16) all changed nothing for us, which is why we were left tuning `NCCL_CHUNK_SIZE` (unusable, #2408).

Happy to run an instrumented build, collect `NCCL_DEBUG_SUBSYS=NET` traces, or try any suggested patch on this cluster.

### Ndministrator · 2026-09-14

**Follow-up 2: with the same QP count and the same per-WQE message size, perftest reaches line rate while a NCCL connection reaches 105 Gb/s**

Same rail (mlx5_0), host memory, one direction, 3 s per data point. `ib_write_bw -s <size> -q <QPs> -t <tx depth>` (default `-t` is 128):

| message size | 1 QP, depth 8 | **8 QPs, depth 8** | 8 QPs, depth 64 | speedup 8QP/1QP |
|---|---|---|---|---|
| 16 KiB | 100.1 Gb/s | **390.9 Gb/s** | 391.8 Gb/s | 3.90x |
| 128 KiB | 293.4 Gb/s | **392.1 Gb/s** | 392.0 Gb/s | 1.34x |

With a single WR in flight the fixed per-operation cost becomes visible:

| message size | 1 QP, depth 1 | implied per-op latency |
|---|---|---|
| 16 KiB | 20.1 Gb/s | ~6.4 us |
| 128 KiB | 117.0 Gb/s | ~8.8 us |
| 1 MiB | 303.4 Gb/s | ~27.6 us (20 us of which is wire time) |
| 4 MiB | 364.2 Gb/s | ~88 us (82 us wire) |

Total data moved per 3 s run was 7.6-146 GB, so these are not small-sample artefacts.

Two conclusions:

1. **Multiple QPs do add in-flight depth on this NIC.** 8 QPs x 8 WQEs x 16 KiB reaches **391.8 Gb/s = 49 GB/s = line rate**, which is precisely the configuration shape NCCL uses for one GPU<->GPU connection.
2. **A NCCL connection on the same rail does 105 Gb/s (13.1 GB/s) — 3.7x lower than perftest with the same QP count and the same message granularity**, and numerically equal to perftest running **one** QP at 16 KiB / depth 8 (100.1 Gb/s). It behaves as if only one QP's worth of work is ever in flight, with a large per-step handoff cost.

Is there an internal reason the 8 QPs of a connection would not all be in flight concurrently (one proxy thread per connection? a shared progress/sync point? per-step costs of ~10 us?), and is there any supported way to improve that — or any counter/trace we can collect on this cluster to help pinpoint it? We can run an instrumented build or a patched version if that helps.

### Ndministrator · 2026-09-15

**Resolved — both causes were on our side; the conclusions in the body need correcting.**

1. **Platform**: the GPU/NIC parent ports had PCIe ACS redirection enabled (`ACS_CTRL=0x001d`) while the kernel ran IOMMU in translated mode (`Default domain type: Translated`). That forces GPU<->NIC GPUDirect P2P DMA up through the root complex — perftest (deep pipelining) hides it, NCCL (shallow pipelining) does not. Fix: `iommu=pt` **and** clearing ACS on those ports (`iommu=pt` alone does not clear ACS).
2. **Our config**: `NCCL_IB_SPLIT_DATA_ON_QPS=1` (default is 0). That is the "+13%" line in the sweep table above — it helped while the machine was in state (1), which is how it got into our config. Once (1) was fixed it became the limiter: it stripes each message across the connection's 8 QPs, shrinking the per-QP in-flight window ~8x.

`all_reduce_perf` 16 ranks x 8 rails 1 GiB busbw / one GPU<->GPU pair (sendrecv), all `Out of bounds values : 0 OK`:

| state | all_reduce 1 GiB | one GPU<->GPU pair |
|---|---|---|
| as filed | 216.5 GB/s | 13.1 GB/s (2 ranks, 1 rail) |
| + platform fix | 358 GB/s | 29.6 GB/s (2 ranks, 1 rail) |
| + `SPLIT_DATA_ON_QPS=0` | **456 GB/s (~97% of the ~470 expected)** | **48.4 GB/s (~99% of perftest line rate)** |

So: (1) ~13 GB/s per connection is not expected; (2) no larger chunk/window is needed once the platform latency is fixed; (3) `NCCL_IB_ADAPTIVE_ROUTING` made no measurable difference post-fix (455.0 vs 455.2 GB/s), so the +22% was the same artifact.

**For anyone landing here:** `NCCL_IB_SPLIT_DATA_ON_QPS` defaults to 0 — if you set it, measure it; on RoCE it can cost ~2x. And when one connection is far below perftest on the same hardware, check IOMMU mode and PCIe ACS before blaming NCCL.

Sorry for the noise — feel free to close this one.

### stephenmsachs · 2026-09-16

Thanks a lot for following up and leaving a description of your resolution for the next reader. Closing as requested.
