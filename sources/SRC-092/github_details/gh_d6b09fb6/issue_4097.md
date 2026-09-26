# [Issue #4097] [Store] Report skipped-duplicate keys to the Master so source replicas release on time

source: https://github.com/kvcache-ai/Mooncake/issues/4097
state: closed | updated: 2026-09-24T03:19:33Z
labels: 

## 正文

Follow-up from the #3135 review: skipped-duplicate keys never reach the Master in either direction, so their offloading tasks and source-replica (DRAM) refcounts linger until the TTL reaper — systematically delaying source release exactly when memory is tightest under the #2827 retry-storm conditions.

**Mechanism** (line numbers on #3135's head): skipped keys land in `all_bucket_keys` (`file_storage.cpp:382`), so the sweep does not NACK them, and they are not in `committed_keys`, so the complete handler does not report them either.

**Suggested shape** (credit @LujhCoconut's review): surface the skipped set out of `BatchOffload` and NACK it with the -1 sentinel so the Master releases the source replica immediately. Cross-layer (BatchOffload result surface + Master notification path), so it wants its own PR after #3135 lands.


## 评论 (1)

### github-actions[bot] · 2026-09-14

Thanks for opening this issue, @he-yufeng!

| Field | Value |
|-------|-------|
| **Issue** | #4097 |
| **GitHub user ID** | `40085740` |
| **Reporter** | @he-yufeng |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
