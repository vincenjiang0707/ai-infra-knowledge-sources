# [Issue #4322] [Bug]: Host RDMA regression from resolving NUMA before memory registration (0.3.13.post1)

source: https://github.com/kvcache-ai/Mooncake/issues/4322
state: open | updated: 2026-09-24T18:18:28Z
labels: bug

## 正文

### Bug Report

With classic TransferEngine RDMA auto-discovery, `mooncake-transfer-engine==0.3.13.post1` can register an **untouched anonymous host-memory mapping** with location `*` instead of its eventual `cpu:0` locality. The wildcard broadens NIC selection across NUMA nodes and causes a large steady-state throughput regression in our two-host test.

The same allocation/register/fill sequence works substantially better with **0.3.9**. On **0.3.13.post1**, touching the mapping **before** `register_memory()` restores `cpu:0` in slice-affinity logs and largely restores throughput. All compared transfers completed successfully and the checked data remained correct; this is a performance/locality issue, not a reported corruption issue.

### Reproduced versions and environment

- Runtime comparison: public cp312 wheels **0.3.9** and **0.3.13.post1**, with matching wheel/loaded-engine hashes on both endpoints.
- Two distinct Alibaba Cloud DSW Linux x86_64 hosts; two CPU NUMA domains, eight mlx5 RDMA HCAs per host, four HCAs local to each NUMA domain. GPU-equipped hosts, but the affected test uses ordinary host `mmap`, not GPU memory.
- Python 3.12.11; kernel 5.10.134; same CUDA 12 runtime and driver-matching libcuda for both versions. Test processes were launched with CPU affinity 16–31, on NUMA node 0.
- Classic RDMA / RoCE, `P2PHANDSHAKE`, automatic device selection (`device=""`). Both sides register a 256 MiB private anonymous mapping. Inherited MC/MOONCAKE/NCCL/GLOO/UCX tuning variables were cleared for the baseline.
- Fresh processes, 0.1 s warmup per case, 1 s measurement, three independent repetitions. The default-version comparison alternated execution order. These were shared hosts, not an exclusive cluster; repeat ranges are included below.

### Observed performance

The following cases use **32 requests × 1 MiB per synchronous batch, one submission thread**. Bandwidth is completed payload bytes divided by measurement wall time, in decimal GB/s. Values are **median [min, max] across three runs**. Registration, connection setup, control messages, memory initialization, and full touched-region checks are outside the measured interval. Data is filled before measurement in **all** variants; the controlled change is whether pages are first touched **before registration**.

| Version / registration preparation / NIC policy | WRITE GB/s | READ GB/s |
|---|---:|---:|
| 0.3.9, untouched mapping, auto | 82.09 [79.76, 87.30] | 77.44 [71.45, 81.63] |
| 0.3.13.post1, untouched mapping, auto | 2.45 [2.38, 2.58] | 1.30 [1.20, 2.58] |
| 0.3.13.post1, pre-touch before registration, auto | 78.34 [77.99, 80.61] | 69.63 [69.10, 71.84] |
| 0.3.9, untouched mapping, restrict to mlx5_0 | 37.26 [35.94, 37.94] | 34.71 [34.41, 36.46] |
| 0.3.13.post1, untouched mapping, restrict to mlx5_0 | 34.47 [33.96, 34.93] | 34.53 [33.24, 34.92] |

The host-memory baseline plus pre-touch control covered **270 cases**, with **1,080/1,080 pre/post local/remote region checks passing** and no transfer errors. Checks surround each timed phase; they do not validate every repeated transfer individually. The byte pattern repeats, so it does not detect swapping identical-content blocks.

Only the newer version was additionally benchmarked with pre-touch: this is a within-version control, **not** a complete comparison with both versions pre-touched. This report does not claim that all host allocations or all RDMA workloads regress.

### Runtime locality evidence

Separate, short diagnostic runs used `MC_LOG_RDMA_SLICE_AFFINITY=1 GLOG_v=1`. These logs were **disabled during performance measurements**. Sanitized excerpts, retaining the relevant fields:

```text
# 0.3.13.post1: untouched mmap -> register -> fill -> transfer
RDMA slice affinity: source_location=*, target_location=*, local_device_name=mlx5_3, peer_device_name=mlx5_5, ... length=65536

# 0.3.13.post1: mmap -> pre-touch -> register -> fill -> transfer
RDMA slice affinity: source_location=cpu:0, target_location=cpu:0, local_device_name=mlx5_3, peer_device_name=mlx5_1, ... length=65536
```

All 48 diagnostic slices in the first run reported `*`/`*`, with target NICs spanning `mlx5_0`–`mlx5_7`. All 48 in the pre-touch run reported `cpu:0`/`cpu:0`, with target NICs limited to `mlx5_0`–`mlx5_3`. Baseline NIC counters also showed traffic on the first four HCAs with 0.3.9, versus all eight with 0.3.13.post1. This supports the locality/selection mechanism, although we have not separately quantified remote-NUMA traffic and worker-contention contributions.

### Source-level explanation

The important difference is **when** the wildcard location is resolved, not a change in the Python API's default location:

1. In [v0.3.9, MR registration happens first](https://github.com/kvcache-ai/Mooncake/blob/v0.3.9/mooncake-transfer-engine/src/transport/rdma_transport/rdma_transport.cpp#L251-L260), and [`getMemoryLocation` is called afterward](https://github.com/kvcache-ai/Mooncake/blob/v0.3.9/mooncake-transfer-engine/src/transport/rdma_transport/rdma_transport.cpp#L283-L293), with a comment explicitly referring to pinned memory.
2. In [v0.3.13.post1, `resolved_name` is computed before registration](https://github.com/kvcache-ai/Mooncake/blob/v0.3.13.post1/mooncake-transfer-engine/src/transport/rdma_transport/rdma_transport.cpp#L319-L329). The code later [registers the MR](https://github.com/kvcache-ai/Mooncake/blob/v0.3.13.post1/mooncake-transfer-engine/src/transport/rdma_transport/rdma_transport.cpp#L458-L473) and [publishes the previously computed name](https://github.com/kvcache-ai/Mooncake/blob/v0.3.13.post1/mooncake-transfer-engine/src/transport/rdma_transport/rdma_transport.cpp#L489-L498), without re-querying residency/locality.
3. The host query uses `numa_move_pages`; a not-yet-resident page can produce a negative per-page status. [`genCpuNodeName` maps a negative node to `*`](https://github.com/kvcache-ai/Mooncake/blob/v0.3.13.post1/mooncake-transfer-engine/src/memory_location.cpp#L23-L26); see also the [query path](https://github.com/kvcache-ai/Mooncake/blob/v0.3.13.post1/mooncake-transfer-engine/src/memory_location.cpp#L80-L120). The runtime probe verified the resulting wildcard location, not the individual syscall's errno.
4. [`cpu:N` prefers NUMA-local HCAs](https://github.com/kvcache-ai/Mooncake/blob/v0.3.13.post1/mooncake-transfer-engine/src/topology.cpp#L453-L487), whereas [`*` includes all discovered HCAs](https://github.com/kvcache-ai/Mooncake/blob/v0.3.13.post1/mooncake-transfer-engine/src/topology.cpp#L794-L829). Filling the buffer **after** registration does not update the published location.

This ordering change appears in [7a938fb3 / #2644](https://github.com/kvcache-ai/Mooncake/commit/7a938fb359883838c65a1605f777257789cc1522). This is source-history inspection, not a binary performance bisect.

I also checked current main at **16b7ba3c7364eb8d36d04378bc7d28013bea1a1e**: [resolution before MR registration](https://github.com/kvcache-ai/Mooncake/blob/16b7ba3c7364eb8d36d04378bc7d28013bea1a1e/mooncake-transfer-engine/src/transport/rdma_transport/rdma_transport.cpp#L361-L371) and [reuse after registration](https://github.com/kvcache-ai/Mooncake/blob/16b7ba3c7364eb8d36d04378bc7d28013bea1a1e/mooncake-transfer-engine/src/transport/rdma_transport/rdma_transport.cpp#L530-L540) remain. **Runtime results above are for the released wheels, not a build of current main.**

### Reproduction

The critical sequence is:

```python
buf = mmap.mmap(-1, 256 << 20,
                flags=mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS)
ptr = ctypes.addressof(ctypes.c_char.from_buffer(buf))
# No memset / first-touch here.
assert engine.register_memory(ptr, 256 << 20) == 0
# Fill/initialize only AFTER registration, then transfer.
```

A complete tested Python harness is included below. Save it as `te_bench.py` on both RDMA-connected hosts. Use the **same wheel version on both endpoints**, in isolated environments, and make sure the CUDA-enabled wheel's libraries match the host driver. Choose a reachable control-plane IP per host; no external metadata service is required. Select an available NUMA-local CPU set appropriate for your machine (the commands use our test's 16–31).

```bash
# Install in each endpoint's isolated environment; repeat with 0.3.9.
python -m pip install 'mooncake-transfer-engine==0.3.13.post1'

# Target; leave running until the client finishes.
taskset -c 16-31 python te_bench.py --role server \
  --ip "$TARGET_IP" --port 29851 --mode host --device ''

# Initiator, in a separate shell/host.
taskset -c 16-31 python te_bench.py --role client \
  --ip "$INITIATOR_IP" --server "$TARGET_IP:29851" \
  --mode host --device '' --duration 1 --warmup 0.1 --out result.json
```

Start fresh endpoints for each repetition; the client stops the target after its matrix completes. For the single-HCA control, pass `--device mlx5_0` on **both** sides. For the pre-touch control, make only this change to `setup()` on **both** sides, then restart them:

```diff
     buffer = Buffer(args.mode)
+    if args.mode == "host":
+        buffer.fill(CAPACITY)
     started = time.perf_counter_ns()
     ret = engine.register_memory(buffer.ptr, CAPACITY)
```

For the **diagnostic only**, set `MC_LOG_RDMA_SLICE_AFFINITY=1 GLOG_v=1` on the newer-version processes and inspect the location fields. Do not compare timings collected with per-slice logging enabled. The diagnostic excerpts above came from a shortened one-batch probe, not the logged full performance matrix.

### Expected behavior / possible fix direction

For an ordinary host mapping registered with automatic location inference, publish locality reflecting the resident/pinned pages, instead of permanently retaining a wildcard inferred before those pages exist.

Could wildcard-inferred host locality be resolved/revalidated after MR pinning and before publishing the buffer descriptor, while preserving explicit location hints, GPU registration, and chunked-MR handling? A regression test should cover an untouched anonymous mapping as well as a pre-touched mapping. Pre-touching before registration is a tested workaround; selecting a single HCA avoids this particular multi-NUMA selection path but also restricts available rails.

### Measurement boundaries

- The issue concerns classic host-memory RDMA auto-selection. The separately observed GPU benefit from the changed relaxed-ordering default is not being reported as a bug here.
- These are synchronous TransferEngine API payload rates, not SGLang serving throughput. In the single-HCA checks, port counters track payload volume (approximately 1.016×, consistent with additional protocol/control bytes), but sysfs's nominal 200-Gbps rate does not agree with the observed counter rate in this cloud environment. The physical/virtual port mapping has not been resolved, so no line-rate utilization claim is made.
- No fix has been applied or validated yet.

### Before submitting

- [x] Searched existing issues for NUMA registration, `getMemoryLocation`, `resolved_name`, prefault and pre-touch. I did not find a direct duplicate of this registration-order regression.

<details>
<summary>Complete tested harness (Python; host and GPU modes, 256 MiB registered buffer)</summary>

```python
#!/usr/bin/env python3
"""Wheel-level Mooncake RDMA A/B benchmark; control traffic is outside timing.

Server: python te_bench.py --role server --ip IP --port PORT --mode host
Client: python te_bench.py --server IP:PORT --ip LOCAL_IP --mode host --out run.json
Use the same wheel on each peer. Latencies are synchronous *batch* call latencies.
"""
import argparse
import ctypes
import ctypes.util
import glob
import hashlib
import importlib.metadata
import json
import mmap
import os
import platform
import socket
import statistics
import sys
import threading
import time
import traceback

CAPACITY = 256 << 20
CHUNK = 4 << 20


def emit(value):
    print(json.dumps(value, sort_keys=True), flush=True)


def sha_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for data in iter(lambda: f.read(4 << 20), b""):
            h.update(data)
    return h.hexdigest()


def metadata():
    import mooncake.engine as module
    relevant = {}
    try:
        with open("/proc/self/maps") as f:
            for line in f:
                path = line.rstrip().split()[-1]
                if path.startswith("/") and ".so" in path and (
                    "mooncake" in path or "libtransfer" in path
                ):
                    relevant[path] = sha_file(path)
    except OSError:
        pass
    return {
        "version": importlib.metadata.version("mooncake-transfer-engine"),
        "module": module.__file__, "module_sha256": sha_file(module.__file__),
        "loaded_so_sha256": relevant, "python": sys.version,
        "hostname": socket.gethostname(), "pid": os.getpid(),
        "platform": platform.platform(),
        "cpu_affinity": sorted(os.sched_getaffinity(0)),
        "environment": {k: v for k, v in os.environ.items()
                        if k.startswith(("MC_", "NCCL_", "MOONCAKE_")) or k in
                        ("CUDA_VISIBLE_DEVICES", "GLOG_minloglevel")},
    }


class Buffer:
    def __init__(self, mode):
        self.mode = mode
        self.mm = None
        self.cuda = None
        self.ptr = 0
        if mode == "host":
            self.mm = mmap.mmap(-1, CAPACITY, flags=mmap.MAP_PRIVATE | mmap.MAP_ANONYMOUS)
            self.ptr = ctypes.addressof(ctypes.c_char.from_buffer(self.mm))
        else:
            candidates = [os.environ.get("CUDA_RUNTIME_LIBRARY"),
                          ctypes.util.find_library("cudart"), "libcudart.so.12", "libcudart.so"]
            for root in sys.path:
                candidates += glob.glob(os.path.join(root, "nvidia/cuda_runtime/lib/libcudart.so*"))
            candidates += glob.glob("/usr/local/cuda*/lib64/libcudart.so*")
            errors = []
            for candidate in dict.fromkeys(x for x in candidates if x):
                try:
                    self.cuda = ctypes.CDLL(candidate)
                    self.cuda_library = candidate
                    break
                except OSError as exc:
                    errors.append(str(exc))
            if self.cuda is None:
                raise RuntimeError("Cannot load libcudart: " + "; ".join(errors))
            self.cuda.cudaSetDevice.argtypes = [ctypes.c_int]
            self.cuda.cudaMalloc.argtypes = [ctypes.POINTER(ctypes.c_void_p), ctypes.c_size_t]
            self.cuda.cudaFree.argtypes = [ctypes.c_void_p]
            self.cuda.cudaMemcpy.argtypes = [ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t, ctypes.c_int]
            self.cuda.cudaDeviceSynchronize.argtypes = []
            self.activate()
            ptr = ctypes.c_void_p()
            self.check(self.cuda.cudaMalloc(ctypes.byref(ptr), CAPACITY), "cudaMalloc")
            self.ptr = ptr.value

    @staticmethod
    def check(ret, name):
        if ret:
            raise RuntimeError(f"{name} failed: CUDA error {ret}")

    def activate(self):
        if self.cuda:
            self.check(self.cuda.cudaSetDevice(0), "cudaSetDevice")

    @staticmethod
    def pattern(seed, size):
        base = bytes((i + seed) % 256 for i in range(256))
        return (base * ((size + 255) // 256))[:size]

    def fill(self, length, seed=None):
        assert 0 <= length <= CAPACITY
        self.activate()
        data = self.pattern(seed, CHUNK) if seed is not None else bytes(CHUNK)
        src = ctypes.create_string_buffer(data, len(data))
        for offset in range(0, length, CHUNK):
            n = min(CHUNK, length - offset)
            if self.cuda:
                self.check(self.cuda.cudaMemcpy(self.ptr + offset, ctypes.addressof(src), n, 1), "cudaMemcpy H2D")
            else:
                ctypes.memmove(self.ptr + offset, src, n)
        if self.cuda:
            self.check(self.cuda.cudaDeviceSynchronize(), "cudaDeviceSynchronize")

    def verify(self, length, seed):
        assert 0 <= length <= CAPACITY
        self.activate()
        actual_hash = hashlib.sha256()
        expected_hash = hashlib.sha256()
        first_bad_offset = None
        expected = self.pattern(seed, CHUNK)
        host = ctypes.create_string_buffer(CHUNK) if self.cuda else None
        for offset in range(0, length, CHUNK):
            n = min(CHUNK, length - offset)
            if self.cuda:
                self.check(self.cuda.cudaMemcpy(ctypes.addressof(host), self.ptr + offset, n, 2), "cudaMemcpy D2H")
                data = host.raw[:n]
            else:
                data = ctypes.string_at(self.ptr + offset, n)
            wanted = expected[:n]
            if data != wanted and first_bad_offset is None:
                first_bad_offset = offset + next(i for i, pair in enumerate(zip(data, wanted)) if pair[0] != pair[1])
            actual_hash.update(data)
            expected_hash.update(wanted)
        return {"ok": first_bad_offset is None, "verified_bytes": length,
                "sha256": actual_hash.hexdigest(), "expected_sha256": expected_hash.hexdigest(),
                "first_bad_offset": first_bad_offset}

    def close(self):
        if self.cuda and self.ptr:
            self.activate()
            self.check(self.cuda.cudaFree(self.ptr), "cudaFree")
        elif self.mm is not None:
            self.mm.close()
        self.ptr = 0


def setup(args):
    from mooncake.engine import TransferEngine
    engine = TransferEngine()
    ret = engine.initialize(args.ip, "P2PHANDSHAKE", "rdma", args.device)
    if ret:
        raise RuntimeError(f"initialize failed: {ret}")
    buffer = Buffer(args.mode)
    started = time.perf_counter_ns()
    ret = engine.register_memory(buffer.ptr, CAPACITY)
    elapsed = time.perf_counter_ns() - started
    if ret:
        buffer.close()
        raise RuntimeError(f"register_memory failed: {ret}")
    info = metadata()
    info.update({"segment": f"{args.ip}:{engine.get_rpc_port()}", "buffer": buffer.ptr,
                 "capacity": CAPACITY, "mode": args.mode, "device": args.device,
                 "register_memory_ms": elapsed / 1e6,
                 "cuda_library": getattr(buffer, "cuda_library", None)})
    return engine, buffer, info


def write_json(file, obj):
    file.write((json.dumps(obj) + "\n").encode())
    file.flush()


def read_json(file):
    line = file.readline(1 << 20)
    if not line:
        raise EOFError("control peer closed connection")
    return json.loads(line)


class Control:
    def __init__(self, address):
        host, port = address.rsplit(":", 1)
        self.socket = socket.create_connection((host, int(port)), timeout=120)
        self.file = self.socket.makefile("rwb")

    def call(self, **kwargs):
        write_json(self.file, kwargs)
        result = read_json(self.file)
        if "error" in result:
            raise RuntimeError("server: " + result["error"])
        return result

    def close(self):
        self.file.close()
        self.socket.close()


def server(args):
    engine, buffer, info = setup(args)
    try:
        with socket.socket() as listener:
            listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            listener.bind((args.ip, args.port))
            listener.listen(1)
            emit({"event": "READY", "control": f"{args.ip}:{args.port}", **info})
            stop = False
            while not stop:
                conn, _ = listener.accept()
                with conn, conn.makefile("rwb") as file:
                    while True:
                        try:
                            req = read_json(file)
                        except EOFError:
                            break
                        try:
                            cmd = req["cmd"]
                            if cmd == "info":
                                result = info
                            elif cmd == "fill":
                                buffer.fill(int(req["length"]), req.get("seed"))
                                result = {"ok": True}
                            elif cmd == "verify":
                                result = buffer.verify(int(req["length"]), int(req["seed"]))
                            elif cmd == "stop":
                                result = {"ok": True, "event": "STOPPING"}
                                stop = True
                            else:
                                raise ValueError(f"unknown command {cmd}")
                        except Exception as exc:
                            result = {"error": repr(exc), "traceback": traceback.format_exc()}
                        write_json(file, result)
                        if stop:
                            break
    finally:
        ret = engine.unregister_memory(buffer.ptr)
        emit({"event": "unregister", "return_code": ret})
        buffer.close()


def percentile(values, q):
    if not values:
        return None
    ordered = sorted(values)
    position = (len(ordered) - 1) * q
    low = int(position)
    high = min(low + 1, len(ordered) - 1)
    return ordered[low] + (ordered[high] - ordered[low]) * (position - low)


def transfer_phase(engine, buffer, peer, block, batch, threads, operation, duration, once=False):
    barrier = threading.Barrier(threads + 1)
    calls = [0] * threads
    samples = [[] for _ in range(threads)]
    failures = [[] for _ in range(threads)]
    ends = [0] * threads
    begin = [0]
    deadline = [0]
    method = getattr(engine, "batch_transfer_sync_" + operation)

    def worker(tid):
        try:
            buffer.activate()
            offset = tid * batch * block
            local = [buffer.ptr + offset + i * block for i in range(batch)]
            remote = [peer["buffer"] + offset + i * block for i in range(batch)]
            sizes = [block] * batch
            barrier.wait(timeout=30)
            while once or time.perf_counter_ns() < deadline[0]:
                start = time.perf_counter_ns()
                ret = method(peer["segment"], local, remote, sizes)
                end = time.perf_counter_ns()
                if ret:
                    failures[tid].append({"return_code": ret, "batch_index": calls[tid]})
                    break
                calls[tid] += 1
                samples[tid].append((end - start) / 1e3)
                if once:
                    break
        except Exception as exc:
            failures[tid].append({"exception": repr(exc)})
            barrier.abort()
        finally:
            ends[tid] = time.perf_counter_ns()

    workers = [threading.Thread(target=worker, args=(tid,)) for tid in range(threads)]
    for thread in workers:
        thread.start()
    begin[0] = time.perf_counter_ns()
    deadline[0] = begin[0] + int(duration * 1e9)
    try:
        barrier.wait(timeout=30)
    except threading.BrokenBarrierError:
        pass
    for thread in workers:
        thread.join()
    elapsed = (max(ends) - begin[0]) / 1e9
    latencies = [lat for sample in samples for lat in sample]
    completed = sum(calls)
    transferred = completed * block * batch
    return {"elapsed_s": elapsed, "completed_batches": completed,
            "completed_requests": completed * batch, "completed_bytes": transferred,
            "throughput_GB_s": transferred / elapsed / 1e9 if elapsed else 0,
            "per_thread_completed_batches": calls, "error_count": sum(map(len, failures)),
            "errors_by_thread": failures,
            "batch_latency_us": {"p50": percentile(latencies, .5), "p95": percentile(latencies, .95),
                                 "p99": percentile(latencies, .99),
                                 "mean": statistics.fmean(latencies) if latencies else None,
                                 "max": max(latencies) if latencies else None},
            "latency_sample_count": len(latencies)}


def cases(quick):
    matrix = [(s, 1, 1) for s in (4 << 10, 64 << 10, 1 << 20, 16 << 20, 64 << 20)]
    matrix += [(s, 32, 1) for s in (4 << 10, 64 << 10, 1 << 20)]
    matrix += [(1 << 20, 32, 4)]
    if quick:
        matrix = [(4 << 10, 1, 1), (1 << 20, 32, 1), (1 << 20, 32, 4)]
    return [(op, *case) for op in ("write", "read") for case in matrix]


def save(path, result):
    absolute = os.path.abspath(path)
    os.makedirs(os.path.dirname(absolute), exist_ok=True)
    tmp = absolute + ".tmp"
    with open(tmp, "w") as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write("\n")
    os.replace(tmp, absolute)


def client(args):
    control = Control(args.server)
    engine = buffer = None
    result = {"schema_version": 1, "start_unix_s": time.time(), "cases": [],
              "harness_sha256": sha_file(__file__), "argv": sys.argv,
              "latency_definition": "wall time of each successful synchronous batch API call, microseconds",
              "throughput_definition": "successful completed batch payload bytes / shared phase wall seconds / 1e9"}
    try:
        peer = control.call(cmd="info")
        engine, buffer, info = setup(args)
        result.update({"local": info, "peer": peer})
        if info["version"] != peer["version"] or args.mode != peer["mode"] or args.device != peer["device"]:
            raise RuntimeError("peer version/memory mode/device differs from client")
        for index, (op, block, batch, threads) in enumerate(cases(args.quick)):
            length = block * batch * threads
            assert length <= CAPACITY
            seed = (index * 17 + 31) % 256
            case = {"operation": op, "block_bytes": block, "batch_size": batch,
                    "threads": threads, "touched_bytes_per_peer": length, "seed": seed}
            if op == "write":
                buffer.fill(length, seed)
                control.call(cmd="fill", length=length)
            else:
                buffer.fill(length)
                control.call(cmd="fill", length=length, seed=seed)
            case["validation_transfer"] = transfer_phase(engine, buffer, peer, block, batch, threads, op, 0, once=True)
            case["before_local"] = buffer.verify(length, seed)
            case["before_peer"] = control.call(cmd="verify", length=length, seed=seed)
            if case["validation_transfer"]["error_count"] or not case["before_local"]["ok"] or not case["before_peer"]["ok"]:
                case["ok"] = False
                result["cases"].append(case)
                raise RuntimeError("pre-measurement correctness validation failed")
            case["warmup"] = transfer_phase(engine, buffer, peer, block, batch, threads, op, args.warmup)
            case["measurement"] = transfer_phase(engine, buffer, peer, block, batch, threads, op, args.duration)
            case["after_local"] = buffer.verify(length, seed)
            case["after_peer"] = control.call(cmd="verify", length=length, seed=seed)
            case["ok"] = (not case["warmup"]["error_count"] and not case["measurement"]["error_count"]
                          and case["measurement"]["completed_batches"] > 0
                          and case["after_local"]["ok"] and case["after_peer"]["ok"])
            result["cases"].append(case)
            save(args.out, result)
            emit({"event": "CASE", "index": index, "operation": op,
                  "block_bytes": block, "batch_size": batch, "threads": threads,
                  "ok": case["ok"], **case["measurement"]})
            if not case["ok"]:
                raise RuntimeError("measurement or post-measurement validation failed")
        result["ok"] = True
    except BaseException as exc:
        result.update({"ok": False, "error": repr(exc), "traceback": traceback.format_exc()})
        raise
    finally:
        result["finish_unix_s"] = time.time()
        if engine is not None and buffer is not None:
            result["unregister_return_code"] = engine.unregister_memory(buffer.ptr)
            buffer.close()
        if not args.keep_server:
            try:
                result["server_stop"] = control.call(cmd="stop")
            except Exception as exc:
                result["server_stop_error"] = repr(exc)
        control.close()
        save(args.out, result)
        emit({"event": "DONE", "ok": result.get("ok", False), "cases": len(result["cases"]), "out": args.out})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--role", choices=("server", "client"), default="client")
    parser.add_argument("--ip", required=True, help="reachable local control/TE IP")
    parser.add_argument("--port", type=int, default=29851)
    parser.add_argument("--server", help="target control IP:PORT")
    parser.add_argument("--mode", choices=("host", "cuda", "cuda0"), default="host")
    parser.add_argument("--device", default="", help="empty for auto discovery, or mlx5_0 etc.")
    parser.add_argument("--out", default="te-bench.json")
    parser.add_argument("--duration", type=float, default=1.0)
    parser.add_argument("--warmup", type=float, default=.1)
    parser.add_argument("--quick", action="store_true")
    parser.add_argument("--keep-server", action="store_true")
    args = parser.parse_args()
    if args.mode == "cuda0":
        args.mode = "cuda"
    if args.duration <= 0 or args.warmup <= 0:
        parser.error("duration and warmup must be positive")
    if args.role == "client" and not args.server:
        parser.error("client requires --server")
    server(args) if args.role == "server" else client(args)


if __name__ == "__main__":
    main()
```

</details>


## 评论 (1)

### github-actions[bot] · 2026-09-24

Thanks for opening this issue, @stmatengss!

| Field | Value |
|-------|-------|
| **Issue** | #4322 |
| **GitHub user ID** | `11641725` |
| **Reporter** | @stmatengss |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
