# [Issue #4054] [Bug]: Ascend wildcard location probe fails on host memory instead of falling back

source: https://github.com/kvcache-ai/Mooncake/issues/4054
state: closed | updated: 2026-09-14T06:56:12Z
labels: 

## 正文

### Environment

- Hardware: Ascend 910B (NPU)
- Mooncake: `kvcache-ai/Mooncake` `main` (`mooncake-transfer-engine-npu` wheel / source build)
- Protocol: `ascend` (host-memory buffers)

### Description

`AscendDirectTransport::ResolveAscendMemType()` in
`mooncake-transfer-engine/src/transport/ascend_transport/ascend_direct_transport/ascend_direct_transport.cpp`
uses `CHECK_ACL(aclrtPointerGetAttributes(addr, &attributes))` for the wildcard location
`"*"`. When the buffer is host memory that is not managed by ACL (hugepage, shm, or plain
`malloc`), `aclrtPointerGetAttributes` fails, so `ResolveAscendMemType` returns an error and
registration fails (in some code paths this surfaces as `location:* is not supported`).

CUDA already falls back to host memory when the wildcard probe cannot identify the address;
Ascend should behave the same way. The same pattern was previously applied to the
heterogeneous RDMA transport in PR #1657.

### Steps to reproduce

1. Build the Ascend wheel / enable the Ascend transport.
2. Mount a CPU hugepage/shm buffer (or call `allocate_managed_buffer` on a host buffer) so
   that a host buffer is registered with the wildcard location `"*"`.
3. Observe the wildcard probe failure (`aclrtPointerGetAttributes` error / `location:* is not
   supported`).

### Expected behavior

The Ascend wildcard location should fall back to host memory when the probe cannot identify
the address (matching CUDA and the heterogeneous-RDMA transport).

### Proposed fix

Treat `aclrtPointerGetAttributes` failure as host memory (`adxl::MEM_HOST`) instead of a hard
error. See the linked PR.


## 评论 (1)

### github-actions[bot] · 2026-09-11

Thanks for opening this issue, @gygdh-001!

| Field | Value |
|-------|-------|
| **Issue** | #4054 |
| **GitHub user ID** | `43057576` |
| **Reporter** | @gygdh-001 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
