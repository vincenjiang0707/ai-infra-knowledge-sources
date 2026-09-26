# [Issue #3919] [RFC][TENT] Align Ascend Direct Transport with classic TE (async + AutoConnect only)

source: https://github.com/kvcache-ai/Mooncake/issues/3919
state: closed | updated: 2026-09-22T01:09:30Z
labels: RFC

## 正文

## Changes proposed

TENT's Ascend Direct Transport is an early single-engine HIXL client. Classic TE (non-TENT, the current development trunk) has landed dummy-real multi-engine, fabric mem, LocalCommRes, AutoConnect failure semantics, register rollback, and timeout handling. Those PRs were not ported to TENT.

This RFC proposes rewriting the TENT backend to match **behavior**, not the classic class tree (`TransferExecutorBase` / sync executor / thread-pool dispatcher / `LocalCopyEngine`). TENT already has submit+poll workers and failover; copying those pieces would fight the runtime.

### In scope
- Async only: `TransferAsync` + `getTransferStatus` poll. No `TransferSync`.
- AutoConnect only: `Initialize` always sets `AutoConnect=1`. No `Connect()`, no `ASCEND_AUTO_CONNECT=0`.
- `LocalCommRes` defaults to `{"version":"1.3"}`; `ASCEND_LOCAL_COMM_RES` may override.
- Dummy-real: one HIXL engine per local NPU, dest-addr routing, RoCE serialized with a per-engine mutex (not a dedicated thread pool).
- Fabric mem + `GlobalResourceConfig`, gated so a P2P TE does not inherit Store's process-global fabric flag.
- Submit all-or-nothing validation, timeout units in milliseconds, fail-entire-route on AutoConnect errors, `quiesce()`, register rollback.
- Mock HIXL unit tests in-tree. RoCE e2e stays **out of tree**.

### Out of scope
- Synchronous ADXL transfer
- Local ACL memcpy path (same-engine also uses `TransferAsync`)
- Short connection
- `ASCEND_BUFFER_POOL` (incompatible with async; TENT staging covers constrained HCCS)
- Transport-level 2x retry (TENT runtime failover owns retries)

### Why not share classic TE sources
Classic TE and TENT use different `Transport` contracts, metadata, and threading. Sharing `TransferExecutorBase` would pull sync, local copy, and a dispatcher TENT does not want.

### Testing
- In-repo gtest with a fake HIXL client and mocked ACL (no NPU required; needs CANN headers / `USE_ASCEND_DIRECT`).
- Hardware RoCE e2e kept outside the repository.

### Size
Expected well over 500 LOC excluding tests, hence this RFC.


## 评论 (1)

### github-actions[bot] · 2026-09-07

Thanks for opening this issue, @ascend-direct-dev!

| Field | Value |
|-------|-------|
| **Issue** | #3919 |
| **GitHub user ID** | `215273277` |
| **Reporter** | @ascend-direct-dev |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
