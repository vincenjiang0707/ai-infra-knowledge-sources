# [Issue #4211] [Bug]: NoF endpoint reuse during unmount can delete a new registration's name index and metrics

source: https://github.com/kvcache-ai/Mooncake/issues/4211
state: open | updated: 2026-09-18T03:57:38Z
labels: bug

## 正文

### Bug Report

While a NoF segment is being unmounted, another UUID can register the same endpoint. The standard SSD registration path also uses the endpoint as the segment name, so the old segment's Commit operation may remove the new registration's name index and metrics.

Unmounting consists of three stages: Prepare, object metadata cleanup, and Commit. Prepare marks the old segment as `UNMOUNTING`, then releases the NoF manager lock before cleaning up object metadata.

However, endpoint deduplication in `ScopedNoFSegmentAccess::MountSegment` only checks segments in the `OK` state:

```cpp
if (existing_segment.status == SegmentStatus::OK &&
    existing_segment.segment.te_endpoint == segment.te_endpoint) {
    return ErrorCode::SEGMENT_ALREADY_EXISTS;
}
```

Consequently, a new UUID can pass the duplicate check and register the same endpoint between Prepare and Commit.

The issue can occur with the following interleaving:

1. Register segment A with both its endpoint and name set to E.
2. Begin unmounting A: Prepare marks it as `UNMOUNTING` and releases the manager lock.
3. During metadata cleanup, segment B, with a different UUID, successfully registers using the same endpoint and name E.
4. A's Commit unconditionally removes `client_by_name_[E]` and the metrics associated with name E, affecting the state established by B.

At this point, B's UUID registration record and allocator still exist, but its name index and metrics may have been removed, leaving the internal state inconsistent.

The expected behavior is to return a retryable error for registrations using the same endpoint until the old segment finishes Commit. Registration should succeed when retried after Commit completes.

The suggested fix is to check all existing registration records when deduplicating endpoints:

- If the existing segment is `OK`, preserve `SEGMENT_ALREADY_EXISTS`.
- If the existing segment is non-OK, return `UNAVAILABLE_IN_CURRENT_STATUS`.

These return codes must remain distinct because the upper layer converts `SEGMENT_ALREADY_EXISTS` into an idempotent success. Returning it during unmount would incorrectly tell the caller that the new registration succeeded.

### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (2)

### github-actions[bot] · 2026-09-18

Thanks for opening this issue, @cage-goat!

| Field | Value |
|-------|-------|
| **Issue** | #4211 |
| **GitHub user ID** | `318081269` |
| **Reporter** | @cage-goat |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### cage-goat · 2026-09-18

I'll open a PR with the implementation.
