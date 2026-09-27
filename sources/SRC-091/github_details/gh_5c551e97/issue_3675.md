# [Issue #3675] feature(multiprocess): add device-agnostic base DeviceIPCWrapper for KV-cache IPC

source: https://github.com/LMCache/LMCache/issues/3675
state: closed | updated: 2026-09-24T01:49:07Z
labels: stale

## 正文

# `DeviceIPCWrapper` — A device-agnostic base for KV-cache IPC

## Motivation

The multiprocess (MP) transport shares a paged KV-cache buffer between the producer process (vLLM / SGLang / TRT-LLM) and the LMCache server by sending an **IPC handle** for the underlying storage once, at `REGISTER_KV_CACHE` time. Every later `STORE`/`RETRIEVE` carries only paged block IDs, never tensors.

Historically all of these handle wrappers subclassed `CudaIPCWrapper`:

```text
CudaIPCWrapper
├── RawCudaIPCWrapper      (TRT-LLM raw cudaMalloc pool)
└── CpuShmTensorWrapper    (CPU POSIX-SHM, in platform/cpu/shm.py)
```

 A CPU shared-memory wrapper and a TRT-LLM raw-pointer wrapper are **not** CUDA caching-allocator tensors,
they inherited `_share_cuda_`-based machinery they never used. It made XPU (SYCL) support impossible to be added cleanly.

## The new hierarchy

A device-agnostic base, `DeviceIPCWrapper`, now owns everything that is not transport-specific. Each concrete wrapper is a **direct** sibling:

```text
DeviceIPCWrapper                        base: contract + (de)serialize
├── CudaIPCWrapper                      cuda  — torch caching allocator
├── RawCudaIPCWrapper                   cuda — raw cudaMalloc, TRT-LLM
├── SyclIPCWrapper                      xpu   — future torch XPU storage-sharing (placeholder)
├── RawSyclIPCWrapper                   xpu   — SYCL IPC (raw USM, current)
└── CpuShmTensorWrapper                 cpu   — POSIX shared memory
```

## What the base class owns

`DeviceIPCWrapper` (in `custom_types.py`) provides the parts that every transport shares:

- **Field contract** — `dtype`, `shape`, `stride`, `storage_offset`, `device_uuid`.
- **Device discovery** — `_get_device_uuid`, `_discover_gpu_devices`,  `_get_device_index_from_uuid`.  Route through the `torch_dev` abstraction and a subclass can override `_get_device_uuid` if its backend needs a different identity source.
- **Equality** — `__eq__` uses a `type(self) is type(other)` guard, so two different wrapper subclasses never compare equal even if their fields coincide.
- **Serialization** — `Serialize`/`Deserialize` are `pickle.dumps` / `pickle.loads`. 
- **`to_tensor()`** — abstract; raises `NotImplementedError`. Every subclass overrides it with its transport-specific reconstruction.

## How to dispatch

- `_CUSTOMERIZED_SERIALIZERS` is keyed on `DeviceIPCWrapper` with **ext code 1**, dispatched by `isinstance` in the encoder hook. Every subclass instance therefore encodes through the same path.
- `Serialize` is `pickle.dumps(obj)` → the concrete subclass survives on the wire. `Deserialize` reconstructs it and `to_tensor()` dispatches to the correct override.
- `KVCache = list[DeviceIPCWrapper]` is the registered msgspec type, so a single `list[...]` payload can mix any of the four wrappers and the server needs **zero** per-type branching.

e.g.,
RawSyclIPCWrapper          --->       Ext(1, pickle_bytes)      --->     RawSyclIPCWrapper
CudaIPCWrapper              --->       Ext(1, pickle_bytes)      --->       CudaIPCWrapper
CpuShmTensorWrapper    --->         Ext(1, pickle_bytes)    --->       CpuShmTensorWrapper

Base class simply makes it explicit and device-neutral.

## The concrete wrappers

| Wrapper | Device type | Transport | Reconstruction |
|---|---|---|---|
| `CudaIPCWrapper` | `cuda` | `UntypedStorage._share_cuda_()` | `_new_shared_cuda` + `set_()` |
| `RawCudaIPCWrapper` | `cuda` | `cudaIpcGetMemHandle` (raw ptr) | `cudaIpcOpenMemHandle` → CuPy → DLPack |
| `SyclIPCWrapper` | `xpu` | torch XPU storage-sharing (future) | placeholder — raises `NotImplementedError` |
| `RawSyclIPCWrapper` | `xpu` | `ipc_get_mem_handle` (raw USM) | `ipc_open_mem_handle` → `view`/`as_strided` |
| `CpuShmTensorWrapper` | `cpu` | POSIX `shm_open` | `mmap` same segment |


## XPU: `RawSyclIPCWrapper` and the future `SyclIPCWrapper`

PyTorch's XPU backend does yet expose a storage-level IPC sharing API analogous to the CUDA path. So today there is exactly one XPU transport, and it is a *raw* one, mirroring `RawCudaIPCWrapper`:

- **Sender** — `RawSyclIPCWrapper.__init__` calls `lmcache.c_ops.ipc_get_mem_handle(tensor)` (merged from
  `lmcache.xpu_ops`), which bridges `sycl::ext::oneapi::experimental::ipc::memory` (`ipc::get` / `ipc::open`).
  It stores the opaque handle bytes and the byte size.
- **Receiver** — `to_tensor()` calls `lmcache.c_ops.ipc_open_mem_handle(handle, nbytes, device_index)`,
  which returns a 1-D `uint8` XPU tensor owning a SYCL IPC close via its storage deleter, then restores the layout with `.view(dtype).as_strided(shape, stride, storage_offset)`.


## Platform registration

The factory lookup (`platform/_registry.py`) keys on `tensor.device.type`, so the integration adapter never has an if/elif chain. Each platform sub-package self-registers at import time:

```text
platform/cuda/__init__.py  →  register_kv_wrapper("cuda", CudaIPCWrapper)
platform/cpu/__init__.py   →  register_kv_wrapper("cpu",  migrate_to_shm)
platform/xpu/__init__.py   →  register_kv_wrapper("xpu",  RawSyclIPCWrapper)
```


## 评论 (4)

### ftian1 · 2026-06-15

looks good to me.

    

### zxue2 · 2026-06-24

@maobaolong, as discussed, a rough plan for LMCache MP XPU enablement as below. The target is to formulate cuda-equivalent solutions.

Phase 1:     Add DeviceIPCWrapper and refactor existing IPCWrapper.
Phase 2.1:  Add XPU RawSyclIPCWrapper with sycl ipc::memory  +  torch xpu synchronization + D2H/H2D copy. 
Phase 2.2:  Add sycl event ipc for XPU RawSyclIPCWrapper.
Phase 3:     Add SyclIPCWrapper with torch ipc.

### github-actions[bot] · 2026-08-24

This issue has been automatically marked as stale because it has not had activity within 60 days. It will be automatically closed if no further activity occurs within 30 days.

### github-actions[bot] · 2026-09-24

This issue has been automatically closed due to inactivity. Please feel free to reopen if you feel it is still relevant!
