# [Issue #4294] [Store] Clarify repeated setup behavior in the Python binding

source: https://github.com/kvcache-ai/Mooncake/issues/4294
state: open | updated: 2026-09-23T11:53:54Z
labels: 

## 正文

## Problem

The Python wrapper's positional `setup()`, dictionary `setup()` and
`setup_dummy()` can replace an existing native client. There is no shared check
or documented contract for calling them again while the wrapper is active, or
after setup has failed. The replacement can also change which real/dummy client
the wrapper retains.

This came up in [the review of #3335](https://github.com/kvcache-ai/Mooncake/pull/3335#discussion_r4080699889).
A guard had been added there, but it affects every Store user and is being
removed from the EGM change so the API decision can be reviewed separately.

## Proposed follow-up

Decide whether repeated setup should be rejected until `close()` or whether
replacing an active client is supported with explicit teardown semantics.
Apply the chosen contract consistently across all three entry points, including
failed setup and transitions between real and dummy clients. Add Python tests
for those cases and document when a new setup is allowed.

This issue does not propose changing the native C++ repeated-setup contract or
adding retryable EGM cleanup. The generic mount/MR failure cleanup has its own
existing work in #2336.


## 评论 (1)

### github-actions[bot] · 2026-09-23

Thanks for opening this issue, @neverhook!

| Field | Value |
|-------|-------|
| **Issue** | #4294 |
| **GitHub user ID** | `41352674` |
| **Reporter** | @neverhook |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
