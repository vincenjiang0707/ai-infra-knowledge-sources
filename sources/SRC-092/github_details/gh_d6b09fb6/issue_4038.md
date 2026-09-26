# [Issue #4038] [Bug]: Master retains NoF heartbeat probe resources after segment unmount

source: https://github.com/kvcache-ai/Mooncake/issues/4038
state: open | updated: 2026-09-15T19:47:24Z
labels: bug

## 正文

### Bug Report

## Description

When NoF is enabled, the Master uses its in-process `SpdkWrapper` to connect to remote NVMe-oF namespaces for heartbeat probes. Although the Master does not forward object data, it holds controllers, I/O qpairs, and DMA buffers for probing.

A `NoFSegment` represents a storage range within a specific namespace. Multiple namespaces accessed through the same subsystem and transport address can share a controller, while each namespace has its own probe qpair in the current implementation.

When heartbeat failures trigger `TryUnmountNoFSegmentByHeartbeat()`, the unmount flow removes the segment registration, allocator, related replica metadata, capacity accounting, and heartbeat state. However, it does not release the corresponding resources in `SpdkWrapper`:

- Namespace handle entries and their I/O qpairs in `ns_seg`.
- Probe DMA buffers in `probe_buffers_`.
- Controllers in `connected_ctrlrs` that are no longer used by any namespace.

These resources remain cached until the global `Cleanup()` runs. Explicit unmounts through `UnmountNoFSegment()` have the same issue.

## Impact

For a long-running Master that repeatedly registers and unmounts different namespaces or endpoints, resources associated with segments that have left the storage pool can accumulate, consuming memory, DMA buffers, and queue capacity. If the connections remain active, they may also continue consuming connection and queue resources on the target, potentially affecting subsequent namespace connections.

The same endpoint normally reuses cached resources, so this is not a new connection leak on every registration/unmount cycle.

Additionally, when the same endpoint is registered again, `OpenNofSegment()` returns the cached handle directly. If its qpair has failed, subsequent heartbeat probes may continue failing even after the remote service has recovered.

### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### github-actions[bot] · 2026-09-11

Thanks for opening this issue, @cage-goat!

| Field | Value |
|-------|-------|
| **Issue** | #4038 |
| **GitHub user ID** | `318081269` |
| **Reporter** | @cage-goat |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### migarci2 · 2026-09-15

Working on a fix in https://github.com/kvcache-ai/Mooncake/pull/4148 — releasing Master `SpdkWrapper` probe resources (`ns_seg` qpairs, `probe_buffers_`, unused `connected_ctrlrs`) from both explicit `UnmountNoFSegment` and heartbeat `TryUnmountNoFSegmentByHeartbeat`, while keeping shared controllers attached when other namespaces remain mounted.
