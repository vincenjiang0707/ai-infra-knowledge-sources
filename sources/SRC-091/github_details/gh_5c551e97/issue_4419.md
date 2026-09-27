# [Issue #4419] [MP][ROCm] lmcache_driven deadlocks at TP=1 in Event.from_ipc_handle (import_event) — infinite block, distinct from #3362

source: https://github.com/LMCache/LMCache/issues/4419
state: open | updated: 2026-09-20T11:43:32Z
labels: bug, mp_mode, amd

## 正文

## Summary

In the default `lmcache_driven` MP transfer mode (the mode `auto` selects on a HIP device), **vLLM EngineCore deadlocks on the very first retrieve** on AMD ROCm — at **TP=1, single GPU, with no sustained load**. The deadlock is an infinite block inside `torch.cuda.Event.from_ipc_handle` (which internally calls `torch.cuda.Stream.from_ipc_handle`), **not** the GIL × `hipEventDestroy` AB-BA documented in #3362.

This is different from #3362 (which only reproduces at TP>=4 under load, and is fixed at the LMCache level by #3336). The `import_event` path used to *import* the peer process's completion event deadlocks even at TP=1, so #3336 alone does not cover it.

A minimal 8-line ROCm-specific patch in `event_ipc.py` works around it and makes `lmcache_driven` fully functional on AMD, with a real latency win (see below).

---

## Environment

- **Host**: Ubuntu 22.04, 8× AMD MI300X (gfx942, 192 GB each), ROCm 7.0.2 host driver, Docker 29.1.3
- **vLLM image**: `rocm/vllm:rocm7.14.0_cdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0` (official Docker Hub)
- **Python**: 3.14 (in-image)
- **torch**: 2.11.0+rocm7.14 (in-image)
- **LMCache**: source-built from the `dev` branch (commit `3b8093c`, shallow clone depth=1)
- **GPU**: AMD MI300X (gfx942), **single GPU, TP=1**
- **Model**: `deepseek-ai/DeepSeek-V2-Lite` (MLA, 27 layers, ~16 GB weights)

---

## Step 0: Pull the official ROCm vLLM image

```bash
# On the host with MI300X GPUs
docker pull rocm/vllm:rocm7.14.0_cdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0
```

Verify it pulled correctly:

```bash
docker images | grep rocm/vllm
# Expected: rocm/vllm  rocm7.14.0_cdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0  <size>
```

---

## Step 1: Create and enter the Docker container

```bash
docker run -d --name lmcache-repro \
  --device=/dev/kfd --device=/dev/dri \
  --group-add video --cap-add SYS_PTRACE --security-opt seccomp=unconfined \
  --ipc=host --shm-size 16G \
  -v /PATH/TO/huggingface_cache:/root/.cache/huggingface \
  rocm/vllm:rocm7.14.0_cdna_ubuntu24.04_py3.14_pytorch_2.11.0_vllm_0.23.0 \
  sleep infinity
```

> **Important flags explained**:
> - `--device=/dev/kfd --device=/dev/dri --group-add video`: GPU access
> - `--cap-add SYS_PTRACE`: required for `py-spy` later
> - `--ipc=host --shm-size 16G`: shared memory for IPC
> - `-v ...:/root/.cache/huggingface`: mount a **pre-downloaded model cache** (avoids a huge download in the container); the model `deepseek-ai/DeepSeek-V2-Lite` should exist in this cache directory

Verify the container is running:

```bash
docker ps --filter name=lmcache-repro
docker exec lmcache-repro python -c "import vllm; print('vllm', vllm.__version__)"
# Expected: vllm 0.23.1.dev...  (or 0.23.x)
```

Enter the container:

```bash
docker exec -it lmcache-repro bash
# All subsequent commands run inside the container unless noted otherwise
```

---

## Step 2: Check available GPUs and pick a free one

```bash
# On the host (outside the container):
rocm-smi --showmeminfo vram | grep -E "GPU\[|Used"
```

Make sure at least one GPU has plenty of free VRAM (e.g. only 297 MB baseline usage). Pick a GPU index that is **not occupied** by other users. In this reproduction we use **GPU 1** (GPU 0 happened to be taken by another workload).

---

## Step 3: Clone and build LMCache from source

### 3.1 Clone the `dev` branch

```bash
cd /root
git clone --depth 1 --branch dev https://github.com/LMCache/LMCache.git
cd LMCache
git log --oneline -1  # confirm: 3b8093c "feat(cli): Add MLA/TP support..."
```

### 3.2 Check key version constraints

The official ROCm vLLM image ships with **numpy 2.4.4**. LMCache's `requirements/common.txt` has `numpy<=2.2.6`. If you run a full `uv pip install`, uv will try to downgrade numpy to 2.2.6 → triggers a from-source compilation (because 2.2.6 has no Python 3.14 wheel) → fails due to missing `meson-python` → the entire LMCache installation aborts silently.

```bash
python -c "import numpy; print(numpy.__version__)"   # expect 2.4.4
grep 'numpy' requirements/common.txt                   # expect numpy<=2.2.6
```

### 3.3 Build LMCache with `--no-deps` (retain image's numpy/torch/vllm)

```bash
export PYTORCH_ROCM_ARCH=gfx942
export TORCH_DONT_CHECK_COMPILER_ABI=1
export CXX=hipcc
export BUILD_WITH_HIP=1

uv pip install --system -e . --no-build-isolation --no-deps
```

This compiles the HIP `c_ops` extension for `gfx942` but **skips all dependency resolution**, so the image's numpy 2.4.4, torch 2.11.0+rocm7.14, and vllm 0.23.x stay untouched.

> **Why `--no-build-isolation`?** Without it, pip creates a temporary venv for the build and the compiled HIP extension can't find the image's torch/ROCm headers.
>
> **Why `--no-deps`?** Without it, uv downgrades numpy → from-source build → `meson-python` not found → installation fails. The image already has most dependencies.

### 3.4 Verify the build

```bash
python -c 'import lmcache, lmcache.c_ops; print("lmcache", lmcache.__version__, "c_ops OK")'
# Expected: lmcache 0.1.dev1 c_ops OK
# (0.1.dev1 is fine — it's from setuptools_scm on a shallow clone without tags)
```

### 3.5 Install the remaining runtime dependencies

Three packages are needed for MP mode but were skipped by `--no-deps`:

```bash
uv pip install --system aiofile aiofiles sortedcontainers pyzmq msgspec safetensors
uv pip install --system "opentelemetry-exporter-prometheus>=0.50b0"
```

> **Python 3.14 / CuPy note:** `cupy-rocm-7-0` can resolve NumPy 2.5. That version is incompatible with the Numba version used by this environment (NumPy 2.4 or lower is required), and LMCache can then fall back to CLI-only mode before failing to import `device_ops`. After installing or reinstalling ROCm CuPy, run `uv pip install --system --force-reinstall numpy<2.5` before starting the MP server.
>
> **Source-tree dependency note:** `--no-deps` intentionally skips dependencies. The MP e2e needs `aiofile`, `aiofiles`, `sortedcontainers`, `pyzmq`, `msgspec`, `safetensors`, and `opentelemetry-exporter-prometheus`; the commands above install them explicitly.

Verify all critical imports work:

```bash
python -c "import zmq, msgspec, fastapi, httpx, aiofiles, sortedcontainers, redis, safetensors, yaml; print('all deps ok')"
```

---

## Step 4: Start the LMCache MP server

> **Critical**: the MP server **must see all GPUs** so it can resolve the physical GPU UUID that vLLM sends when registering KV caches. Do **not** set `HIP_VISIBLE_DEVICES` on the server.

```bash
export LMCACHE_TRACK_USAGE=false
export LMCACHE_DISABLE_BANNER=1

lmcache server \
  --host localhost --port 5555 \
  --http-host 0.0.0.0 --http-port 8085 \
  --chunk-size 256 \
  --l1-size-gb 20 \
  --eviction-policy LRU \
  > /tmp/mp_server.log 2>&1 &
```

Wait ~15 seconds and verify:

```bash
# Check the server is listening on ZMQ + HTTP
ss -tlnp | grep -E "5555|8085"
# Or: netstat -tlnp | grep -E "5555|8085"

# Check the HTTP metrics endpoint
curl -s -o /dev/null -w "metrics=%{http_code}\n" http://localhost:8085/metrics
# Expected: metrics=200

# Confirm the log shows startup
grep -i "ZMQ cache server is running\|Supported transfer mode" /tmp/mp_server.log
# Expected: Supported transfer mode: auto
#          LMCache ZMQ cache server is running on tcp://localhost:5555
```

---

## Step 5: Start vLLM with LMCacheMPConnector

> **Critical**: vLLM must be constrained to **one free GPU** (e.g. GPU 1) with `HIP_VISIBLE_DEVICES=1`. The MP server must see all GPUs (no constraint), but vLLM should only use the free one.

```bash
export HIP_VISIBLE_DEVICES=1        # use only GPU 1 (physical)
export VLLM_USE_V1=1
export SAFETENSORS_FAST_GPU=1
export LMCACHE_TRACK_USAGE=false

vllm serve deepseek-ai/DeepSeek-V2-Lite \
  --trust-remote-code \
  --max-model-len 8192 \
  --gpu-memory-utilization 0.4 \
  --disable-hybrid-kv-cache-manager \
  --no-enable-prefix-caching \
  --kv-transfer-config '{"kv_connector":"LMCacheMPConnector","kv_role":"kv_both","kv_connector_extra_config":{"lmcache.mp.host":"tcp://localhost","lmcache.mp.port":5555}}' \
  > /tmp/vllm_mp.log 2>&1 &
```

> **Why `--disable-hybrid-kv-cache-manager` and `--no-enable-prefix-caching`?** DeepSeek-V2-Lite uses MLA attention which requires these flags. Disabling internal prefix caching also makes the external LMCache hit the *only* source of cache hits — cleaner evidence.

Wait ~60-100 seconds for model loading + CUDA graph capture:

```bash
# Check health
curl -s -o /dev/null -w "health=%{http_code}\n" --max-time 5 http://localhost:8000/health
# Expected: health=200

# Check the log for successful startup
grep -i "Application startup complete\|Registering kv caches" /tmp/vllm_mp.log
# Expected: Registering kv caches!
#          Application startup complete.

# Confirm the transfer mode is "auto" (→ lmcache_driven on HIP)
grep -i "mp_transfer_mode" /tmp/vllm_mp.log | tail -1
# Expected: lmcache.mp.mp_transfer_mode = auto

# Confirm MP server registered the KV caches via lmcache_driven
grep -i "Registered KV cache\|lmcache_driven" /tmp/mp_server.log | tail -3
# Expected: Registered KV cache for GPU ID <uuid> with 27 layers (lmcache_driven_transfer.py)
```

---

## Step 6: Reproduce the deadlock

### 6.1 Prepare a request with a long shared prefix

First request (cold — this will STORE successfully):

```bash
# Inside the container:
PREFIX=$(python3 -c "
block = 'LMCache is a KV cache layer for LLM serving. In multiprocess mode, an independent LMCache server process holds the KV cache, and vLLM connects to it as a client over ZMQ, transferring KV tensors via CUDA/HIP IPC with zero copy. This decouples cache lifetime from the inference engine and enables cache sharing. '
print('You are a meticulous technical assistant specializing in GPU inference systems. Background you must remember:\n\n' + block * 85)
")

# Send cold request (A)
curl -s -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"deepseek-ai/DeepSeek-V2-Lite\",\"prompt\":$(python3 -c "import json; print(json.dumps('$PREFIX'))"),\"max_tokens\":32,\"temperature\":0.0}" \
  -o /tmp/rA.json

python3 -c "import json; print('A usage:', json.load(open('/tmp/rA.json')).get('usage'))"
# Expected: {'prompt_tokens': 5989, 'total_tokens': 6021, 'completion_tokens': 32}

# Check MP server — store should have succeeded
grep -i "Stored\|lmcache_mp_l1_memory_usage" /tmp/mp_server.log | tail -2
curl -s http://localhost:8085/metrics | grep -E "lmcache_mp_l1_memory_usage_bytes|lmcache_mp_lookup_hit_tokens_total" | grep -v "#"
# Expected: Stored 5888 tokens in 0.065s
#          lmcache_mp_l1_memory_usage_bytes > 0
#          lmcache_mp_lookup_hit_tokens_total = 0
```

### 6.2 Send the SAME request again (retrieve — this WILL deadlock)

```bash
# Send identical request (C) — this will hang forever
timeout 120 curl -s -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"deepseek-ai/DeepSeek-V2-Lite\",\"prompt\":$(python3 -c "import json; print(json.dumps('$PREFIX'))"),\"max_tokens\":32,\"temperature\":0.0}" \
  -o /tmp/rC.json

# The above command will time out after 120s — C never returns
```

> **Expected deadlock behavior**:
> - The curl command hangs indefinitely (the 120s timeout will kill it)
> - `rC.json` is never written
> - After ~130s, the MP server logs: `Reaped GPU instance ... silent for ~130s (pinged=True)`
> - vLLM health endpoint still returns 200 (API server is alive, but EngineCore is wedged)

---

## Step 7: Locate the root cause with py-spy

### 7.1 Install py-spy

```bash
uv pip install --system py-spy
```

### 7.2 Find the wedged EngineCore PID and dump its stack

```bash
PID=$(ps aux | grep "VLLM::EngineCore" | grep -v grep | awk '{print $2}' | head -1)
echo "EngineCore PID: $PID"

# Check process state — should be Rl (runnable/busy, not sleeping)
ps -p $PID -o pid,stat,wchan,comm

# Dump the Python call stack
py-spy dump --pid $PID --nonblocking 2>&1
```

### 7.3 Expected py-spy output (the deadlock stack)

```
Process <PID>: VLLM::EngineCore
Python v3.14.6 (...)

Thread <PID> (active+gil)
    from_ipc_handle          (torch/cuda/streams.py:197)   <-- BLOCKS FOREVER
    import_event             (lmcache/v1/platform/base/event_ipc.py:225)
    _on_raw_future_complete  (lmcache/v1/multiprocess/futures.py:134)
    query                    (lmcache/v1/multiprocess/futures.py:203)
    get_finished             (lmcache/integration/vllm/vllm_multi_process_adapter.py:1609)
    get_finished             (lmcache/integration/vllm/lmcache_mp_connector.py:984)
    _get_kv_connector_output (vllm/v1/worker/kv_connector_model_runner_mixin.py:103)
    __exit__                 (contextlib.py:148)
    execute_model            (vllm/v1/worker/gpu_model_runner.py:4276)
    ...
```

### 7.4 Interpret the stack

1. vLLM `execute_model` finishes, enters `_get_kv_connector_output`
2. This calls `get_finished` on the retrieve future
3. The future's `_on_raw_future_complete` tries to **import the MP server's completion event** via `import_event`
4. `import_event` calls `torch.cuda.Event.from_ipc_handle(device, handle)`
5. **`from_ipc_handle` blocks forever on ROCm** — the cross-process event IPC ABI is unsupported or hangs

The code that blocks:

```python
# lmcache/v1/platform/base/event_ipc.py, line 222-225
class DefaultEventIPCBackend:
    def import_event(self, handle: bytes, device: object) -> object:
        return self._event_module.Event.from_ipc_handle(  # ← hangs here on ROCm
            device, handle
        )
```

Compare with the store path (which succeeds): store only does a local `event.record(stream)` — no cross-process import needed.

---

## Step 8: Apply the workaround and verify it works

### 8.1 The patch

Edit `lmcache/v1/platform/base/event_ipc.py`, in the `DefaultEventIPCBackend` class, replace the `import_event` method:

```python
# BEFORE (original, deadlocks on ROCm):
def import_event(self, handle: bytes, device: object) -> object:
    """Reconstruct an event from an IPC handle on ``device``."""
    return self._event_module.Event.from_ipc_handle(  # type: ignore[union-attr]
        device, handle
    )

# AFTER (patched, works on ROCm):
def import_event(self, handle: bytes, device: object) -> object:
    """Reconstruct an event from an IPC handle on ``device``.

    ROCm workaround (PRE_HIP_PATCH): on AMD ROCm,
    torch.cuda.Event.from_ipc_handle blocks indefinitely in the
    lmcache_driven multiprocess path, so cross-process event IPC
    cannot be used. Fall back to synchronizing the current stream
    (which orders the IPC KV-copy on this device) and return a
    local already-signaled event so downstream synchronize/query
    calls stay correct.
    """
    import torch
    if getattr(torch.version, "hip", None) is not None:
        torch.cuda.current_stream(device).synchronize()
        return self._event_module.Event()
    return self._event_module.Event.from_ipc_handle(
        device, handle
    )
```

> **What the patch does**: On ROCm, instead of importing the peer's event (which hangs), it synchronizes the current stream on this device (flushing all pending GPU ops, including the IPC KV-copy). It returns a local already-signaled event so that the downstream `synchronize_event`/`query_event` calls work correctly.

### 8.2 Restart everything with the patch

```bash
# Kill old processes
pkill -9 -f vllm
pkill -9 -f "VLLM::EngineCore"
pkill -9 -f "lmcache server"
sleep 3

# Verify clean
ps aux | grep -E "vllm|lmcache server|EngineCore" | grep -v grep | grep -v defunct
# Should be empty

# Clear old logs
rm -f /tmp/vllm_mp.log /tmp/mp_server.log

# Restart MP server (same command as Step 4)
lmcache server \
  --host localhost --port 5555 \
  --http-host 0.0.0.0 --http-port 8085 \
  --chunk-size 256 --l1-size-gb 20 --eviction-policy LRU \
  > /tmp/mp_server.log 2>&1 &

# Wait for server
sleep 15
curl -s -o /dev/null -w "metrics=%{http_code}\n" http://localhost:8085/metrics
# Expected: metrics=200

# Restart vLLM (same command as Step 5)
HIP_VISIBLE_DEVICES=1 VLLM_USE_V1=1 SAFETENSORS_FAST_GPU=1 \
vllm serve deepseek-ai/DeepSeek-V2-Lite \
  --trust-remote-code --max-model-len 8192 --gpu-memory-utilization 0.4 \
  --disable-hybrid-kv-cache-manager --no-enable-prefix-caching \
  --kv-transfer-config '{"kv_connector":"LMCacheMPConnector","kv_role":"kv_both","kv_connector_extra_config":{"lmcache.mp.host":"tcp://localhost","lmcache.mp.port":5555}}' \
  > /tmp/vllm_mp.log 2>&1 &

# Wait for vLLM (60-100s)
sleep 90
curl -s -o /dev/null -w "health=%{http_code}\n" --max-time 5 http://localhost:8000/health
# Expected: health=200
```

### 8.3 Re-run the cold + repeat test

```bash
# Cold (A) — same as before, should still work
PREFIX=$(python3 -c "...")  # same as Step 6.1
curl -s -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"deepseek-ai/DeepSeek-V2-Lite\",\"prompt\":$(python3 -c "import json; print(json.dumps('$PREFIX'))"),\"max_tokens\":32,\"temperature\":0.0}" \
  -o /tmp/rA.json

# Repeat (C) — this time it should RETURN, not hang
time curl -s -X POST http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d "{\"model\":\"deepseek-ai/DeepSeek-V2-Lite\",\"prompt\":$(python3 -c "import json; print(json.dumps('$PREFIX'))"),\"max_tokens\":32,\"temperature\":0.0}" \
  -o /tmp/rC.json

echo "C exit code: $?"
# Expected: C exit code: 0, latency ~0.36s (vs cold ~1.4s)
```

### 8.4 Verify the cache hit

```bash
# MP server — retrieve should have succeeded
grep -i "Stored\|Retrieved" /tmp/mp_server.log | tail -4
# Expected:
#   Stored 5888 tokens in 0.065s (lmcache_driven_transfer.py)
#   Retrieved 5888 tokens in 0.030s (lmcache_driven_transfer.py)

# MP metrics — should show hit
curl -s http://localhost:8085/metrics | grep -E "lmcache_mp_l1_memory_usage_bytes|lmcache_mp_lookup_hit_tokens_total" | grep -v "#"
# Expected:
#   lmcache_mp_l1_memory_usage_bytes 1.83140352e+08     (183 MB)
#   lmcache_mp_lookup_hit_tokens_total{...} 5888.0

# py-spy — EngineCore should be back to idle
PID=$(ps aux | grep "VLLM::EngineCore" | grep -v grep | awk '{print $2}' | head -1)
py-spy dump --pid $PID --nonblocking 2>&1 | head -8
# Expected: Thread <PID> (idle) — wait (queue.py:199)
```

---

## Observed behavior (before patch)

- First (cold) request: store succeeds (`Stored 5888 tokens in 0.065s`, `lmcache_driven_transfer.py`), curl returns normally
- Second (identical) request for retrieve: **never returns**; after ~130s the MP server `Reaped` the GPU instance (`silent for ~130s, pinged=True`); curl times out
- No `memory access fault` — the process is truly alive (state `Rl` runnable) but stuck in `from_ipc_handle`
- This is NOT the same as #3362 (which only reproduces at TP>=4 under load)

## Root cause

`lmcache/v1/platform/base/event_ipc.py` — `DefaultEventIPCBackend.import_event` calls `torch.cuda.Event.from_ipc_handle(device, handle)`, which internally calls `torch.cuda.Stream.from_ipc_handle`. On AMD ROCm, this cross-process event/stream IPC import blocks indefinitely.

The store path works because it only does a local `event.record(stream)` — no cross-process import is needed. The retrieve path must import the peer process's completion event to order the GPU copy, and that import never returns.

The module docstring already acknowledges this: *"The `lmcache_driven` multiprocess handle path orders cross-process KV-cache transfers with device events. Accelerators expose different event IPC ABIs."* On AMD that ABI is unsupported for `from_ipc_handle`.

## Minimal workaround

```python
def import_event(self, handle, device):
    import torch
    if getattr(torch.version, "hip", None) is not None:
        torch.cuda.current_stream(device).synchronize()
        return self._event_module.Event()
    return self._event_module.Event.from_ipc_handle(device, handle)
```

## Result after the workaround (default `lmcache_driven`, TP=1)

| Metric | Source | Cold (A) | Repeat (C) |
|---|---|---|---|
| STORE / RETRIEVE | MP server log | `Stored 5888 tokens in 0.065s` | `Retrieved 5888 tokens in 0.030s` |
| `lmcache_mp_lookup_hit_tokens_total` | MP metrics | 0 | 5888 |
| `lmcache_mp_l1_memory_usage_bytes` | MP metrics | 0 | 1.83e8 (183 MB) |
| request latency | curl | ~1.4 s | 0.36 s (~4× faster) |
| GPU memory faults | both logs | 0 | 0 |

After the patch, py-spy shows EngineCore back to `idle` (waiting on the input queue). Notably, `lmcache_driven` (zero-copy HIP IPC) yields a real latency win here (~4× vs cold), whereas the `engine_driven` fallback mode is slower than a cold request due to gather/scatter overhead.

## Additional pitfall: MP server GPU visibility

If the MP server has `HIP_VISIBLE_DEVICES` constrained (e.g. to a single GPU), it may fail to resolve the physical GPU UUID that vLLM reports during KV-cache registration. The error is:

```
Device UUID ... not found in the discovered devices
```

**Fix**: the MP server must see **all GPUs** (do not set `HIP_VISIBLE_DEVICES` on the server). Only constrain vLLM's GPU visibility. The server then iterates all visible GPUs by UUID to find the matching physical device for each IPC handle.

## Ask

1. Is `Event.from_ipc_handle` on peer events expected to work on ROCm, or is the event IPC ABI unsupported there? (cc @ROCm — this looks like the same root defect family as #3362.)
2. Should `check_event_support` / `import_event` degrade gracefully on HIP rather than hang indefinitely? A backend-neutral HIP branch in `event_ipc.py` would let AMD users run the default `lmcache_driven` mode.

## References

- #3362 — AMD/HIP deadlock at TP>=4 (`hipEventDestroy → SyncAllStreams` GIL AB-BA); the `import_event` hang here is a separate, TP=1-reproducible failure of the same HIP event IPC ABI
- LMCache/LMCache#3336 — LMCache-side fix for #3362 (does not cover `import_event`)
- Related installation issues affecting AMD users: vllm-project/vllm#50953 (same `--no-deps` / `sortedcontainers` / `opentelemetry` pain points on ROCm)




## 评论 (2)

### stefanskiasan · 2026-09-19

Confirming this on different hardware and a different topology: **MI350X (gfx950), TP=4**, not just MI300X at TP=1.

**Environment**
- 8x AMD Instinct MI350X (gfx950), ROCm 7.2.3, TP=4
- LMCache 0.5.4, `lmcache_driven`, MP connector, L1 only (no L2 adapter)
- Model: GLM-5.3 (MoE, MLA), vLLM v1 engine

**One difference worth noting:** for us it does not even reach the first retrieve. The engine hangs during **startup**, right after `Using external LMCacheMPConnector`. The only thing the log produces afterwards is the once-a-minute `No available shared memory broadcast block found in 60 seconds`. Three of the four GPUs spin at 100% utilisation while one sits at 0% — one rank is stuck in a collective while the others wait.

The reliable way to tell this apart from a long compilation phase: **no file grows**. Over 90 seconds, nothing was written to `~/.cache/vllm`, `~/.triton` or the aiter JIT cache. A genuine autotune run writes hundreds of files per minute.

**The patch from the issue body fixes it.** With `import_event` synchronising the current stream on HIP instead of importing the peer event, the engine comes up normally and the cache works:

| | |
|---|---|
| Test instance, 27k-token prompt sent twice | 3.93 s → 0.39 s (**10x**) |
| Production under real load, same prompt | 45.1 s → 11.5 s (**3.9x**) |
| Hang signature / hipError / "no lookup ipc key" | 0 / 0 / 0 |

Confirmed from the server side, not just from wall-clock:

```
LMCache INFO: Stored 8192 tokens in 0.007 seconds
LMCache INFO: Prefetch request completed (L1+L2): 114/215 retained keys
              (lmcache_driven_transfer.py)
```

The first measurement has vLLM's own prefix cache disabled (`--no-enable-prefix-caching`), otherwise it masks LMCache entirely and the number says nothing.

**A warning about the workaround people are likely to reach for first.** Setting `HSA_ENABLE_IPC_MODE_LEGACY=1` does make the hang go away — but it silently disables the cache. In our case that ran for eight days before anyone noticed: zero hits across ~36k requests, with ~13k `no lookup ipc key` messages as the only symptom. It looks healthy and serves traffic, it just never caches. So the two observations that seem contradictory actually fit together: **with** the legacy flag the cache never hits, **without** it the engine hangs. This patch is what makes the combination work.

Happy to test a proper fix on gfx950 if a backend-neutral HIP branch lands, as suggested in the open questions.


### stefanskiasan · 2026-09-20

**`from_ipc_handle` works across container boundaries on gfx950 / ROCm 7.2 — and the fabricated-event fallback measurably corrupts reads**

We hit this on MI350X (gfx950, ROCm 7.2.53211, HIP 7.2) running `lmcache_driven` with TP=4, where the vLLM workers and the LMCache server are **separate containers**. Two findings that may help narrow this down.

**1. We could not reproduce the hang.**

A minimal two-container reproducer — producer writes a pattern into a shared GPU buffer and records an interprocess event, consumer imports it via `from_ipc_handle`, waits on it on its own stream, reads — completed **8/8** with import times of 0.1–0.3 ms. Same result with `HSA_ENABLE_IPC_MODE_LEGACY=1`. In production our LMCache server has since performed **577,847 imports without a single hang**.

So on this configuration the import path appears healthy. If the hang is specific to same-process or same-container producers/consumers, that would be worth noting in the issue title — we spent a while assuming it applied to our setup.

**2. The fallback proposed in #4422 does corrupt reads — independently measured.**

We had shipped exactly that workaround (synchronize the local stream, return a fresh `Event()`). With **varying** buffer sizes:

| variant | reads returning unwritten data |
|---|---|
| fabricated-event fallback | **9 of 12** (values 3.97–4.55 where 7.0 was expected) |
| producer synchronizes before publishing the handle | **0 of 12** |
| real `from_ipc_handle` + `wait_event` | 0 of 6 |

This reproduces @andyluo7's 12/12 result on MI300X/MI355X and supports the review verdict on #4422.

Worth spelling out why this is easy to miss: a freshly created event that was never recorded reports as already complete — `query()` returns `True` and `synchronize()` returns in 0.002 ms. Every subsequent `wait`/`synchronize` becomes a no-op, so there is no error, no hang, and no warning. The symptom that eventually led us here was not a deadlock but **garbled model output under long contexts**.

The reproducer is two small scripts (one intra-container, one across two containers). Happy to upstream them as a regression test if that would be useful.

