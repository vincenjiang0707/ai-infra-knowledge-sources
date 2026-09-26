# [Issue #2408] NCCL_CHUNK_SIZE / NCCL_P2P_NET_CHUNKSIZE >= 1MiB gives incorrect results and Xid 31 GPU MMU faults (H100, 8x400G RoCE)

source: https://github.com/NVIDIA/nccl/issues/2408
state: open | updated: 2026-09-21T00:11:10Z
labels: 

## 正文

### Summary

Setting `NCCL_CHUNK_SIZE` / `NCCL_P2P_NET_CHUNKSIZE` to **>= 1 MiB** makes `sendrecv_perf` (and `alltoall_perf`) return **incorrect results**, and both nodes log **GPU MMU faults (Xid 31)**. The throughput increase is large (~7x), but the data is wrong.

Values <= 512 KiB with matched `NCCL_CHUNK_SIZE`/`NCCL_P2P_NET_CHUNKSIZE` are correct, but give no speedup at all.

We hit this while investigating why a single GPU<->GPU connection only reaches ~13 GB/s on a 400Gb/s RoCE rail (details at the end — enlarging the chunk is the only knob that helps), so a correct way to enlarge the chunk would be very useful.

### Environment

| | |
|---|---|
| NCCL | `2.31.2-1+cuda13.3` (`libnccl.so.2.31.2`, md5 `241dc74211d08b2986ad36e478069974`) |
| nccl-tests | master `a0b82b2260cf5152b9f8c061bbf7eaf0ba096432` |
| GPUs | 2 nodes x 8x H100 80GB HBM3 SXM. GPUi <-> NICi all PIX, PCIe Gen5 x16 |
| NICs | 8x ConnectX-7 per node, 400 Gb/s, RoCEv2, MTU 9000, fw `28.43.8016` |
| Driver / CUDA | `595.71.05` / `13.2` |
| OS / kernel | Ubuntu 24.04 / `6.8.0-137-generic` |
| RDMA stack | NVIDIA OFED 24.10 (`mlx5_core` 24.10-5.1.6), `nvidia_peermem` loaded |
| Fabric | single leaf switch, PFC + ECN enabled |

### Reproduction (2 ranks, 1 rail)

```bash
mpirun -np 2 --hostfile <2 nodes, 1 slot each> --map-by ppr:1:node \
  -x NCCL_IB_HCA=mlx5_0 \
  -x NCCL_CHUNK_SIZE=1048576 -x NCCL_P2P_NET_CHUNKSIZE=1048576 \
  ./build/sendrecv_perf -b 1G -e 1G -n 20 -w 5 -g 1
```

### Observed

Default (no chunk env) — correct:

```
# Avg bus bandwidth    : 13.09
# Out of bounds values : 0 OK
```

With chunk = 1 MiB (fails on both processes):

```
.. node-a pid 1871349: Test failure common.cu:1454
.. node-b pid 2073154: Test failure common.cu:1454
prterun detected that one or more processes exited with non-zero status,
thus causing the job to be terminated. Exit code: 7
```

`dmesg` on both nodes immediately after that run:

```
NVRM: Xid (PCI:0000:18:00): 31, pid=1847919, name=sendrecv_perf, channel 0x0000000a, intr 00000000.
      MMU Fault: ENGINE GRAPHICS GPC1 GPCCLIENT_T1_7 faulted @ 0x7b79_6ba00000.
      Fault is of type FAULT_PDE ACCESS_TYPE_VIRT_READ            # node A
NVRM: Xid (PCI:0000:18:00): 31, pid=2048399, name=sendrecv_perf, channel 0x0000000a, intr 00000000.
      MMU Fault: ENGINE GRAPHICS GPC1 GPCCLIENT_T1_7 faulted @ 0x7646_91a04000.
      Fault is of type FAULT_PDE ACCESS_TYPE_VIRT_READ            # node B
```

The fault is a kernel read of a virtual address outside the registered buffer, i.e. this looks like a genuine size/payload-count bug, not a test artifact.

### Characterised behaviour (sendrecv_perf, 2 ranks, 1 rail, 1 GiB)

| configuration | algbw | result correct? |
|---|---|---|
| default | 13.08 GB/s | yes |
| `CHUNK_SIZE`=256K (P2P default) | 26.11 GB/s | no |
| `CHUNK_SIZE`=512K (P2P default) | 52.29 GB/s | no |
| `CHUNK_SIZE`=256K + `P2P_NET_CHUNKSIZE`=256K | 12.17 GB/s | yes (no speedup) |
| `CHUNK_SIZE`=512K + `P2P_NET_CHUNKSIZE`=512K | 12.24 GB/s | yes (no speedup) |
| `CHUNK_SIZE`=1M + `P2P_NET_CHUNKSIZE`=1M | 87.57 GB/s | **no** (`#wrong` ~4.7e8) |
| `CHUNK_SIZE`=4M + `P2P_NET_CHUNKSIZE`=4M, `QPS_PER_CONNECTION`=1, `SPLIT_DATA_ON_QPS`=0 | 93.12 GB/s | **no** |

So: (a) an unmatched `CHUNK_SIZE` vs `P2P_NET_CHUNKSIZE` breaks correctness at any size (same as #1496), and (b) even with the two matched, >= 1 MiB still breaks correctness. The mismatch also holds for `NCCL_IB_QPS_PER_CONNECTION` in {1, 8, 16} and `NCCL_IB_SPLIT_DATA_ON_QPS` in {0, 1}.

### Relevant source (master, `src/enqueue/enqueue.cc`)

```c
1009:    stepSize[dir] = comm->buffSizes[protocol[dir]] / NCCL_STEPS;   /* NCCL_STEPS == 8, src/include/device.h:26 */
1010:    if (protocol[dir] == NCCL_PROTO_SIMPLE) stepSize[dir] = comm->p2pChunkSize;
1011:    chunkSize[dir] = stepSize[dir];
1012:    if (paramChunkSize != 0) {
1013:      chunkSize[dir] = paramChunkSize;                 /* no upper-bound validation */
1014:    } else if (network[dir]) {
1015:      /* Tune chunk size for the network */
1016:      if (protocol[dir] == NCCL_PROTO_SIMPLE && bytes[dir] < stepSize[dir]) chunkSize[dir] /= 4;
1017:      else if (bytes[dir] < 8 * stepSize[dir]) chunkSize[dir] /= 2;
1018:    }
1020:    chunkDataSize[dir] = chunkSize[dir];
1021:    if (protocol[dir] == NCCL_PROTO_LL) chunkDataSize[dir] /= 2;
1022:    chunkDataSize_u32fp8[dir] = u32fp8Encode(chunkDataSize[dir]);
1023:    chunkDataSize[dir] = u32fp8Decode(chunkDataSize_u32fp8[dir]);
1024:    chunkSize[dir] = chunkDataSize[dir];
1025:    if (protocol[dir] == NCCL_PROTO_LL) chunkSize[dir] *= 2;
```

### Questions

1. Is `NCCL_CHUNK_SIZE >= 1 MiB` a supported value? If not, should `paramChunkSize` be validated/clamped (line 1013 currently applies it unconditionally)? If it is supported, what is the cause of the wrong payload size / the Xid 31 read past the buffer?
2. Is the fixed 8-step in-flight window per connection (`NCCL_STEPS == 8`, `buffSizes[protocol]/NCCL_STEPS`) intended, and is there any supported way to increase the per-WQE payload (or the window) so a single connection can use more of a 400 Gb/s rail?
3. Are the `chunkSize /= 4` (line 1016) and `/2` (line 1017) network-tuning steps the reason why a 1 GiB `sendrecv` with a 128 KiB step ends up with only ~16 KiB per WQE?

### Motivation (why we were tuning the chunk at all)

On the same rail the hardware is demonstrably fine:

* `ib_write_bw` (perftest, host memory): **392 Gb/s** unidirectional, **779 Gb/s** bidirectional; 384–391 Gb/s with 1–8 MiB messages; **307 Gb/s even with a single WR (1 MiB) in flight**
* `ib_write_bw --use_cuda` (GPUDirect RDMA, GPU memory): identical to host memory, 384–391 Gb/s

but NCCL:

* single GPU<->GPU connection (`sendrecv_perf`, 2 ranks, 1 rail): **13.1 GB/s** (send 6.99 + recv 6.99)
* `all_reduce` 16 ranks x 8 rails: **217 GB/s** busbw at 1 GiB, 231 GB/s at 8 GiB (2 nodes x 8x400G, would expect ~470 GB/s)

`NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=NET` shows a per-connection in-flight window of 8 WQEs that does not change with `NCCL_IB_QPS_PER_CONNECTION` (1..16), `NCCL_MIN_NCHANNELS`/`NCCL_MAX_NCHANNELS` (1..32) or `NCCL_IB_SPLIT_DATA_ON_QPS`, and the built-in WQE latency monitor reports `inflight=8`, p50 post-to-poll ~110 us. With the effective per-WQE payload at `chunk / QPS_PER_CONNECTION` ~= 16 KiB, the single-connection rate lands at ~13 GB/s. Enlarging the chunk is the only thing that moved the needle (up to 87 GB/s), but it is unusable because of the corruption reported above.


## 评论 (3)

### Ndministrator · 2026-09-14

Follow-up with the throughput side of this problem (perftest reaches line rate on the same rail, NCCL reaches ~46% of expected aggregate bandwidth): #2409

### Ndministrator · 2026-09-15

**Reporter update: not blocking us, but still a real bug.**

Our reason for tuning the chunk was #2409 — that turned out to be a platform issue plus a misconfiguration on our side, and with those fixed the default chunk path reaches line rate, so we are no longer pursuing `NCCL_CHUNK_SIZE`.

Caution for anyone finding this looking for a quick win: >= 1 MiB gave us ~7x the bandwidth with **silently wrong results** plus Xid 31 (table above). Don't use those values, and keep the correctness check on.

Happy to test a patch if you add validation/clamping for `paramChunkSize`.

### stephenmsachs · 2026-09-16

Thanks for reporting. I am able to reproduce a failure when setting `NCCL_CHUNK_SIZE`, but not by only setting `NCCL_P2P_NET_CHUNKSIZE`. Have you been able to produce an error with only the latter variable?

Since the former is an undocumented variable, there are no guarantees that setting this will work in the intended way and the meaning of it will remain constant over different versions. So, I would not expect there to be any check whether we can use a specific setting on a given system. Please let me know if you agree.
