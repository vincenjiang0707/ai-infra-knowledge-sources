# [Issue #4280] [RFC][TENT] Hylink transport for Hygon DCU

source: https://github.com/kvcache-ai/Mooncake/issues/4280
state: open | updated: 2026-09-22T12:53:58Z
labels: 

## 正文

## Summary

We propose adding a new TENT transport, **hylink**, to support **HSL (Hygon Scale-up Link)**, the high-speed interconnect on Hygon DCU supernodes. HSL is a GPU-centric fabric that connects DCUs across nodes **without requiring IB/RoCE NICs**; on the software side it is exposed through DTK fabric shareable handles. The transport also covers intra-node GPU-to-GPU copies via IPC, so a single transport serves both the in-node and the HSL scale-up domain.

A working implementation is ready (~1050 lines, 21 files); we are opening this RFC to align on the design before submitting the PR.

## Motivation

Hygon DCU supernodes use HSL as the high-speed interconnect between GPUs, including across chassis. Unlike the scale-out RDMA path, HSL:

- connects GPUs directly, **no IB/RoCE NIC involved**;
- is managed by the DTK driver stack, which exports device memory to peer nodes as fabric shareable handles instead of going through a NIC MR/lkey model.

Mooncake/TENT today cannot use HSL at all:

- **RDMA** requires NICs and cannot address HSL-attached memory.
- **TCP** would stage through host memory, defeating the purpose of a high-speed GPU fabric.
- Existing GPU transports (nvlink, musa, tpu) are vendor-specific and same-machine-only; none of them speaks DTK fabric handles.

For KV-cache transfer on Hygon supernodes this is the difference between using the dedicated scale-up fabric and falling back to a much slower network path. The hylink transport makes HSL a first-class TENT citizen.

## Design

### Two data paths, one transport

| Scope | Mechanism | HIP/DTK APIs |
|---|---|---|
| Intra-node (same machine) | IPC memory handle + async memcpy | `hipIpcGetMemHandle`, `hipIpcOpenMemHandle`, `hipMemcpyAsync` |
| Inter-node over HSL | DTK VMM fabric shareable handle + VMM mapping | `hipMemExportToShareableHandle` (type `0x8`), `hipMemImportFromShareableHandle`, `hipMemAddressReserve`, `hipMemMap` |

Same-machine vs HSL is decided by comparing TENT `machine_id`s; the exported handle advertises which kind(s) it carries. No NIC, QP, or MR is involved on either path.

### Export handle format

`encodeExport` serializes a small header plus an optional IPC handle (64 bytes) and/or an optional DTK fabric handle (512 bytes, the exact DTK fabric blob layout). Export prefers IPC; fabric export is attempted when IPC is unavailable (e.g. VMM-allocated memory). `decodeExport` validates the blob and rejects malformed handles gracefully.

### Address relocation

On the opener side, `relocateSharedMemoryAddress` translates the exporter's device pointer into a locally mapped address:

- IPC path: `hipIpcOpenMemHandle` with lazy peer-access setup.
- HSL fabric path: import the shareable handle, reserve VA with `hipMemAddressReserve`, and `hipMemMap` exactly the exported length. The mapping gives direct GPU access to the remote node's memory over HSL.

Opened mappings are cached in a thread-local relocate map, invalidated by an epoch counter on `uninstall()`/`removeMemoryBuffer()` so stale mappings are never reused.

### Async execution model

Each sub-batch owns a dedicated HIP stream and one completion event per task. `submitTransfer` issues `hipMemcpyAsync` for all tasks onto the stream and records events; `getTransferStatus` polls event completion. Stream creation failures roll back the batch cleanly so TENT's submit-stage failover can pick the next transport.

### Transport selection and failover

- New `TransportType::HYLINK`, parsed as `"hylink"` in policies.
- Unlike nvlink, hylink is **not** restricted to same-machine transfers (the HSL fabric path is cross-node), so it is deliberately excluded from the same-machine-only guard in the transport selector.
- Failover is generic TENT policy behavior: e.g. policy `["hylink", "rdma", "tcp"]` falls back to RDMA when hylink submit fails.

### Build integration

- New CMake option `USE_HYLINK` (requires `USE_TENT=ON`) to enable the transport independently.
- When `USE_HYLINK=ON`, the build locates HIP/DTK, reuses the ROCm platform plugin, and compiles `tent_xport_hylink`.
- The transport stays **off at runtime** unless `transports/hylink/enable` is set; DTK builds keep RDMA/TCP defaults.
- `transfer_engine_bench --protocol=hylink` forces a hylink-only policy for benchmarking.

## Testing

We plan to cover the following before/with the PR:

- **Unit tests**: transport selector candidacy for hylink in both same-machine and cross-machine scenarios.
- **Intra-node IPC path**: `transfer_engine_bench --protocol=hylink` with VRAM buffers on a Hygon DCU node, verifying correctness and bandwidth.
- **HSL cross-node fabric path**: the same benchmark across two nodes connected by HSL, verifying fabric handle export/import and transfer correctness.
- **Failover**: with a `["hylink", "rdma", "tcp"]` policy, force hylink submission to fail and verify the transfer completes over RDMA (GDR) or TCP.
- **Regression**: existing TENT test suites (selector, config, engine lifecycle) to confirm no impact on other transports.

## Compatibility and risks

- Purely additive: new transport, new CMake option, no changes to existing transport behavior. Builds without DTK are unaffected.
- The fabric handle format (type `0x8`, 512-byte blob) is a DTK ABI detail; if DTK changes the layout, only `encodeExport`/`decodeExport` need updates.

## 评论 (1)

### github-actions[bot] · 2026-09-22

Thanks for opening this issue, @huojianqiangg!

| Field | Value |
|-------|-------|
| **Issue** | #4280 |
| **GitHub user ID** | `209053019` |
| **Reporter** | @huojianqiangg |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
