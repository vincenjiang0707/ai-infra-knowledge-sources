# [Issue #4120] [Store] Make non-conflict standby-restore rejections durable

source: https://github.com/kvcache-ai/Mooncake/issues/4120
state: open | updated: 2026-09-14T21:36:27Z
labels: 

## 正文

[Store] Follow-up: make non-conflict standby-restore rejections durable

Split out from the #3806 review discussion with @Icedcoco.

#3806 makes conflict-derived discards durable: when the tolerant standby restore drops ambiguous overlapping descriptors, it writes a fenced OpLog record per affected key (REMOVE for full drops, PUT_END with only the surviving descriptors for partial ones) and fails the restore unless the batch goes durable.

The other rejection kinds still only produce a log line and a metric: `unknown_endpoint`, `invalid_memory_descriptor`, `capacity_overflow`, `invalid_tenant_id`. A later promotion that replays the same snapshot re-rejects the same entries every round. That is safe and idempotent, but it is repeated work, and for permanently-invalid entries (bad descriptor shape) a durable tombstone would be the cleaner end state.

The subtlety that kept this out of #3806: some rejection reasons are transient. `capacity_overflow` in particular reflects this promotion's capacity view, not the entry's validity, so a durable REMOVE could suppress an entry that a later, roomier promotion should accept. `object_already_exists` / `duplicate_object` must never tombstone either, since the key legitimately exists in the index.

Proposed shape when someone picks this up: a per-reason allowlist on the rejection funnel (`NoteLegacyStandbyRejection`) for the permanently-invalid kinds only, reusing the existing `repair_remove_keys` durable write path, with the transient kinds explicitly excluded.

Not blocking #3806; conflict-derived discards are already durable there.


## 评论 (1)

### github-actions[bot] · 2026-09-14

Thanks for opening this issue, @he-yufeng!

| Field | Value |
|-------|-------|
| **Issue** | #4120 |
| **GitHub user ID** | `40085740` |
| **Reporter** | @he-yufeng |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
