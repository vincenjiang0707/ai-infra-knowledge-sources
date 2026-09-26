# [Issue #4037] [Feature Request]: Persist NoF storage pool registrations across master restarts

source: https://github.com/kvcache-ai/Mooncake/issues/4037
state: open | updated: 2026-09-15T09:05:48Z
labels: 

## 正文

## Problem

NoF storage pool registrations are not persisted in master snapshots. After a master restart or recovery from a snapshot, previously registered namespaces must be registered again by an external tool before the master can use them as allocatable storage pools.

This is a must-have for our production use: master startup and failure recovery should not depend on an additional registration workflow when the backend namespaces still exist and remain reachable.

## Current behavior

NoF namespaces are registered through `MountNoFSegment`, which supplies the namespace connection information, base offset, and capacity. The master then creates the corresponding space allocator.

On main at `6a55edc668c1320ee7c3ad8da18297ebb0576b4a`:

- [`ScopedNoFSegmentAccess::MountSegment`](https://github.com/kvcache-ai/Mooncake/blob/6a55edc668c1320ee7c3ad8da18297ebb0576b4a/mooncake-store/src/segment.cpp#L1269-L1333) creates an allocator from the registered endpoint, base offset, and size.
- [`MasterSnapshotCodec::EncodeSegments` / `DecodeSegments`](https://github.com/kvcache-ai/Mooncake/blob/6a55edc668c1320ee7c3ad8da18297ebb0576b4a/mooncake-store/src/ha/snapshot/master_snapshot_codec.cpp#L121-L139) do not persist or restore `NoFSegmentManager`. The encoder explicitly documents this omission.

## Requested behavior

- Persist the registered NoF pool metadata needed for recovery, including namespace identity/connection information, base offset, and capacity.

- [x] Make sure you already searched for relevant issues and read the [documentation](https://kvcache-ai.github.io/Mooncake/)


## 评论 (2)

### github-actions[bot] · 2026-09-11

Thanks for opening this issue, @KaiqiChen39!

| Field | Value |
|-------|-------|
| **Issue** | #4037 |
| **GitHub user ID** | `22573449` |
| **Reporter** | @KaiqiChen39 |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.

### cage-goat · 2026-09-15

I’m working on this, The implementation is currently undergoing local testing and review. I’ll share a PR once it’s ready.
