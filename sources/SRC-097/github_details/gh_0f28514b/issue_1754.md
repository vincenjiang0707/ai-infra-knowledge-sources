# [Issue #1754] UCX: PyTorch expandable_segments / CUDA VMM memory silently falls back to slow path (no cuda_ipc)

source: https://github.com/ai-dynamo/nixl/issues/1754
state: closed | updated: 2026-07-16T07:57:53Z
labels: Network

## 正文

## Summary

When CUDA memory registered with the UCX backend was allocated by PyTorch with `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` (i.e. CUDA VMM / `cuMemCreate` memory), registration **succeeds** but READ transfers silently fall back to UCX's software-emulated RMA over TCP at **~0.3 GB/s**, instead of the `cuda_ipc` zero-copy path at **~200 GB/s** (same-node H100/NVLink). A single env var produces a silent ~600x slowdown with no warning anywhere, and the data remains correct — which makes this brutal to diagnose in production.

We hit this through Ray's RDT integration (`ray.put(_tensor_transport="nixl")`, Ray 2.55.1 hardcodes the UCX backend) while implementing RL weight sync (trainer → inference engine) in [miles](https://github.com/radixark/miles). `expandable_segments:True` is a very common setting in large-model training (fragmentation mitigation), so this trap is broadly armed for the RL/LLM audience.

## Environment

- nixl 1.2.0 (`nixl-cu12` pip wheel, bundled UCX)
- Ray 2.55.1 (`ray.experimental` RDT, NIXL transport), torch 2.11, CUDA 12.9
- 8x H100 (NVLink), single node, AWS EKS pod

## Reproduction

Two single-GPU Ray actors, source registers a 512 MiB buffer, destination does a one-sided READ (mirrors Ray's `nixl_tensor_transport`). Identical code, one env var difference on the source actor:

| Source allocator | Steady-state READ | UCX proto (`UCX_PROTO_INFO=y`) |
|---|---|---|
| default (`cudaMalloc`) | 179-201 GB/s | `zero-copy \| cuda_ipc/cuda` |
| `expandable_segments:True` | **0.29-0.32 GB/s** | `software emulation \| tcp/eth0` |

Controls that did NOT matter (all 170-230 GB/s): `CUDA_VISIBLE_DEVICES` masking, `UCX_TLS`/`UCX_RNDV_THRESH` overrides, `CUDA_DEVICE_MAX_CONNECTIONS=1`, NCCL initialized in the source process. We can share the full repro scripts (self-contained, ~150 lines each) on request.

## Root cause (as far as we traced it)

- PyTorch expandable segments allocate physical blocks via `cuMemCreate` with `CU_MEM_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR` requested.
- `cuIpcGetMemHandle` does not work on VMM memory, so the legacy cuda_ipc export fails.
- The bundled UCX appears to support VMM sharing only via **fabric handles** (strings in `libuct_cuda.so`: "allocated memory at %p of size %ld does not have fabric property"), which requires fabric-enabled allocations + IMEX — not what PyTorch produces, and unavailable on most deployments.
- Net result: the cuda_ipc lane silently drops for that memory region and the transfer runs on the emulated TCP path.

## Requests

1. **Loud failure over silent degradation**: when a registered CUDA region cannot be exported for cuda_ipc (and no NIC lane exists), emit a warning naming the memory and the consequence. A one-line log would have saved us days of bisecting.
2. **Support POSIX-FD VMM handles intra-node**: PyTorch's own IPC path shows a workable protocol without sockets or IMEX — serialize `(pid, fd)` from `cuMemExportToShareableHandle(..., POSIX_FILE_DESCRIPTOR)` and import via `pidfd_open`/`pidfd_getfd` + `cuMemImportFromShareableHandle` (see `c10/cuda/CUDACachingAllocator.cpp`, `ExpandableSegment::share`/`fromShared`). Same-node, same-user processes (the common RL/inference colocation case) need no extra privileges.
3. **Document the limitation** (and ideally surface it through Ray RDT docs): "PyTorch `expandable_segments:True` memory currently transfers via the slow path unless fabric handles are available."

## Workaround we shipped

Allocate the transfer staging buffer outside expandable segments:

```python
torch.cuda.memory._set_allocator_settings("expandable_segments:False")
bucket = torch.empty(nbytes, dtype=torch.uint8, device="cuda")
torch.cuda.memory._set_allocator_settings("expandable_segments:True")
```

This restored 0.3 GB/s → ~150 GB/s end-to-end through Ray RDT.

## Proposed PR

I've opened a PR that addresses requests #1 and #3 as a first step:

- Emits a one-time `NIXL_WARN` from the UCX plugin's `memReg` when a registered CUDA region is not legacy-CUDA-IPC-capable (detected via `cuPointerGetAttribute(CU_POINTER_ATTRIBUTE_IS_LEGACY_CUDA_IPC_CAPABLE)`), naming the region and the consequence.
- Adds a `src/plugins/ucx/README.md` documenting the limitation and the workaround.

Request #2 (POSIX-FD VMM IPC support) is a larger feature; happy to discuss a design here first per CONTRIBUTING before attempting it.


## 评论 (4)

### xyuzh · 2026-06-10

Opened #1755 addressing requests #1 (one-time `NIXL_WARN` from the UCX plugin when a registered CUDA region is not legacy-CUDA-IPC-capable) and #3 (new `src/plugins/ucx/README.md` documenting the limitation + workaround). Request #2 (intra-node POSIX-FD VMM IPC support) left for design discussion here first.

### xyuzh · 2026-06-11

Filed the underlying transport feature request upstream: openucx/ucx#11548 — adding a pidfd-based POSIX_FD arm to cuda_ipc's existing handle-type dispatch, so default-configured PyTorch VMM memory (`expandable_segments:True`, and `cudaMallocAsync` mempools) gets the zero-copy lane on non-fabric machines. NIXL would inherit the fix by bundling a UCX release containing it; #1755 covers detection/warning in the meantime.

### linear-code[bot] · 2026-07-02

from mikhailb:
> should be fixed by [https://github.com/openucx/ucx/pull/11183](<https://github.com/openucx/ucx/pull/11183>)

### linear-code[bot] · 2026-07-16

from mikhailb:
> Fix will land in NIXL 1.4
