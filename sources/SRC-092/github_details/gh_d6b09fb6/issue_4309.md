# [Issue #4309] [Bug]: hard-coded `attr.max_rd_atomic = 16` causes `modify_qp` failure

source: https://github.com/kvcache-ai/Mooncake/issues/4309
state: open | updated: 2026-09-24T07:58:15Z
labels: bug

## 正文

### Bug Report

<img width="1960" height="1900" alt="Image" src="https://github.com/user-attachments/assets/38651d76-2369-44cd-bcd0-e7e3430d8a6d" /> Certain NIC variants do not support `attr.max_rd_atomic = 16`.
Is it feasible to use `ibv_query_device` to retrieve device attributes and configure `max_rd_atomic` respecting the hardware’s supported limits?

### Before submitting...

- [ ] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### github-actions[bot] · 2026-09-24

Thanks for opening this issue, @shenhongqian!

| Field | Value |
|-------|-------|
| **Issue** | #4309 |
| **GitHub user ID** | `37929351` |
| **Reporter** | @shenhongqian |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### he-yufeng · 2026-09-26

Verified the report against current main and sketched the minimal fix, since this has been sitting for two days.

The hardcode is real and singular: `rdma_endpoint.cpp:1221` sets `attr.max_rd_atomic = 16` on the RTR->RTS transition and passes `IBV_QP_MAX_QP_RD_ATOMIC`, so a device whose `max_qp_rd_atom` is below 16 fails `ibv_modify_qp` at setup. The device attributes are already queried once at context construction (`rdma_context.cpp:1250`, then forwarded to `updateGlobalConfig`), so the natural fix needs no new verbs call: carry `device_attr.max_qp_rd_atom` through the context and clamp to `min(16, device_attr.max_qp_rd_atom)` at the endpoint site. Same-pattern precedent one screen down in the same function: the LAG-port block is explicitly a no-op when the device doesn't support it, which is the shape the clamp should take (never raise above device capability, never change behavior on capable NICs).

Verification honesty: Mooncake CI builds the EFA wheel but runs no RDMA hardware (`ci_efa.yml` has BUILD_UNIT_TESTS=OFF), and I have no NIC here either, so whoever picks this up should get one setup confirmation on the affected NIC variant from the reporter before merge; the change itself is compile-level and a few lines. I'm not opening the PR blind for exactly that reason, but the fix above is ready to take.
