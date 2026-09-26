# [Issue #4240] [Bug]: Multi-transport memory unregister cannot recover after a partial failure

source: https://github.com/kvcache-ai/Mooncake/issues/4240
state: open | updated: 2026-09-20T13:46:40Z
labels: 

## 正文

### Bug Report

In a multi-transport Transfer Engine, a transient unregister failure can leave the engine permanently unable to reuse a memory address even after every transport has eventually removed the registration.

`TransferEngineImpl::unregisterLocalMemory()` and `unregisterLocalMemoryBatch()` attempt every installed transport and return the first non-zero result. They erase the top-level `local_memory_regions_` entry only when every transport returns zero in the same call. This does not converge across retries:

1. A region is registered in transports A and B.
2. The first unregister removes it from A, while B returns a transient error. The top-level region is retained, correctly preventing premature address reuse.
3. A retry asks both transports again. A now returns `ERR_ADDRESS_NOT_REGISTERED`, while B succeeds.
4. `ERR_ADDRESS_NOT_REGISTERED` becomes `first_error`, so the top-level region is retained again even though neither transport still owns the registration.
5. Further retries repeat the same result, and registering the same or an overlapping address returns `ERR_ADDRESS_OVERLAPPED`.

The batch path has the same state machine. This affects allocator reuse and teardown/recovery in long-running processes with multiple installed transports. It can leave the Transfer Engine bookkeeping permanently split from RDMA/TCP/SHM registration state until the engine is recreated.

The behavior is present on current `main` at `9b5adcd4`. It is also consistent with the unresolved high-priority review finding on merged PR #2962, which identified permanent address blocking after partial unregister failures. Simply erasing the top-level region on every error would be unsafe because a transport may still retain a live MR; the safe convergence rule is narrower: treat `ERR_ADDRESS_NOT_REGISTERED` as an idempotent successful terminal state, retain the region for any other error, and erase it only when every transport reports either success or already-unregistered.

I searched current open/recent issues and PRs for partial unregister, `ERR_ADDRESS_NOT_REGISTERED`, and address-overlap recovery and found no active implementation. I plan to add hardware-free regressions for the single and batch APIs that exercise partial failure followed by retry, plus a negative case proving a genuine remaining transport error still blocks address reuse. I expect to have the focused fix ready within one day.

## 评论 (4)

### github-actions[bot] · 2026-09-20

Thanks for opening this issue, @CorgiBoyG!

| Field | Value |
|-------|-------|
| **Issue** | #4240 |
| **GitHub user ID** | `111257566` |
| **Reporter** | @CorgiBoyG |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### CorgiBoyG · 2026-09-20

Scope correction after auditing the batch contract: I will fix the single-address API in this issue/PR first. For a single address, `ERR_ADDRESS_NOT_REGISTERED` unambiguously means that transport has reached the desired terminal state.

The batch API needs a separate design. Several transport implementations return only the first per-address error; an early `ERR_ADDRESS_NOT_REGISTERED` can therefore mask a later genuine failure in the same batch. Treating that aggregate result as idempotent success at the Transfer Engine layer could release bookkeeping while a live MR remains. I will add a regression documenting that batch must continue to retain its top-level regions for this ambiguous result, rather than claiming an unsafe one-line fix. A future batch fix should expose per-address outcomes or otherwise guarantee error prioritization across every transport implementation.

### CorgiBoyG · 2026-09-20

A deeper production review invalidated the initial idea of treating `ERR_ADDRESS_NOT_REGISTERED` as idempotent success. Some transports remove their metadata entry before hardware deregistration; if the latter fails, a retry can return `ERR_ADDRESS_NOT_REGISTERED` while an MR or other resource still remains. Ignoring that result would report false success and permit unsafe address reuse.

The implementation therefore uses a stricter rule: persist only transports that explicitly returned success in an earlier attempt, skip those transports on retry, and continue treating every error from a previously failed transport as a failure. The top-level region is erased only after every installed transport has explicitly succeeded. Same-address unregister attempts are serialized while this state is updated, and the existing missing-address error remains unchanged.

This keeps the fix bounded to the cross-transport recovery bug without claiming to repair partial cleanup inside an individual transport. A regression also models metadata/state removal followed by an error and verifies that a later `ERR_ADDRESS_NOT_REGISTERED` remains fail-closed.

### CorgiBoyG · 2026-09-20

Implementation is ready for review on `CorgiBoyG:fix/4240-partial-unregister-recovery` at `9d89a95b`.

The production review expanded the fix beyond the initial scalar-only sketch because the same address state is shared by scalar, batch, multi-protocol, dynamic transport installation, and shared-memory free paths. The final design records the transport instances that actually registered each address, persists only explicit unregister successes, retries only unfinished `(address, transport)` pairs, rejects concurrent same-address lifecycle operations with `ERR_TOO_MANY_REQUESTS`, and keeps the full address range reserved through physical shared-memory release. Batch unregister now evaluates per-address outcomes instead of relying on an aggregate transport error that can hide partial success.

The change includes hardware-free regressions for scalar and batch partial-failure recovery, fail-closed partial cleanup, missing-address compatibility, and both register→unregister and unregister→register races. clang-format 20, all applicable pre-commit hooks, codespell, and `git diff --check` pass. Full C++/CTest execution remains pending because this macOS host lacks the Linux dependency environment, and the fork default branch does not expose the upstream `workflow_dispatch`; the upstream Linux matrix will run after the required human review and PR creation.
