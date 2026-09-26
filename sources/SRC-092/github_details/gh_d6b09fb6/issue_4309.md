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

## 评论 (1)

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
