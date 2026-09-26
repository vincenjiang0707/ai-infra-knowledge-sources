# [Issue #775] Inconsistent environment variable names

source: https://github.com/AI-Hypercomputer/maxtext/issues/775
state: closed | updated: 2026-04-28T18:19:58Z
labels: feature request

## 正文

MaxText uses the environment variables JAX_COORDINATOR_IP, JAX_COORDINATOR_PORT, NNODES, and NODE_RANK for multi-system GPU training, but JAX_COORDINATOR_ADDRESS, a fixed port, JAX_PROCESS_COUNT, and a combination of several environment variables, and for multi-system CPU training. It would be great if both configurations used the same environment variables

## 评论 (2)

### shralex · 2025-04-17

Since this changes the "api", perhaps we could introduce duplicate variables, and mark others as deprecated while still respecting them for a while.

### sarunsingla11722 · 2026-04-28

We are currently closing stale issues as part of a cleanup initiative. If any of these are still necessary, please feel free to reopen them.
