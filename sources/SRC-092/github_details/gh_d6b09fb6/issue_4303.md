# [Issue #4303] [Bug]: P2P Store `GetReplica` does not validate the caller's `sizeList` against the stored payload layout

source: https://github.com/kvcache-ai/Mooncake/issues/4303
state: open | updated: 2026-09-23T22:42:41Z
labels: bug

## 正文

### Bug Report

**Environment:** main (`e88aacf2`), `mooncake-p2p-store/src/p2pstore/core.go`. Not platform specific.

### What happens

`GetReplica` only checks that `addrList` and `sizeList` have the same non-zero length (`core.go:401-404`). It never compares `sizeList` with the `SizeList`, `Size` or shard count stored in etcd for that payload. `hasSameLayout` (`core.go:363`) only compares two etcd snapshots to each other.

`doGetReplica` (`core.go:284-303`) then walks the caller's buffers in `MaxShardSize` steps, indexes `payload.Shards[taskID]` with no bounds check, and transfers the **stored** `shard.Length` into the caller's address:

```go
for ; offset < size; offset += maxShardSize {
    source := addr + uintptr(offset)
    shard := payload.Shards[taskID]   // unchecked
    taskID++
    ...
    store.performTransfer(ctx, source, shard)   // copies shard.Length bytes
}
```

If the caller's sizes do not match the registered layout, one of three things happens:

1. **Caller passes more bytes than stored:** `taskID` runs past `len(payload.Shards)` and the process panics with `index out of range` on the calling goroutine.
2. **Caller passes a buffer shorter than a shard:** the full stored shard length is written into the caller's buffer, past its end. On TCP this is a plain out-of-bounds write (`tcp_transport.cpp:606` uses the raw pointer). On RDMA the slicer clamps to the registered buffer, so it fails unless the neighbouring memory is also registered, in which case the data silently lands there.
3. **Caller passes fewer total bytes than stored:** only the first shards are fetched, `GetReplica` returns `nil`, and `updatePayloadMetadata` advertises this node as a replica source. The caller believes it has the whole file.

The shipped example passes a hardcoded `fileSize`, not the layout from `List()`, so a mismatch reaches this path directly.

### To reproduce

Using the existing test fakes in `metadata_recheck_test.go`:

```go
store, _ := newMetadataRecheckStore(scripted) // scripted returns payloadWithLayout(4096, source)
err := store.GetReplica(ctx, "payload", []uintptr{buf}, []uint64{8192})
// today: panic: runtime error: index out of range [1] with length 1
// expected: ErrInvalidArgument
```

### Expected

`GetReplica` should return `ErrInvalidArgument` unless `len(sizeList) == len(payload.SizeList)` and every entry matches, checked right after the first `metadata.Get`. That one check closes all three cases.

### Suggested fix

Add the layout check in `GetReplica` before calling `doGetReplica`, and add a regression test with the fakes above (mismatched larger size, mismatched smaller size, and a matching layout that still succeeds).

### Before submitting...

- [x] Ensure you searched for relevant issues and read the [documentation]

## 评论 (1)

### github-actions[bot] · 2026-09-23

Thanks for opening this issue, @yaojiejia!

| Field | Value |
|-------|-------|
| **Issue** | #4303 |
| **GitHub user ID** | `70050131` |
| **Reporter** | @yaojiejia |

A maintainer will triage this when possible. To help us respond faster, please include:

- Mooncake version or commit SHA
- Environment (OS, CUDA/driver, RDMA stack if relevant)
- Steps to reproduce and expected vs. actual behavior

Useful links: [Documentation](https://kvcache-ai.github.io/Mooncake/) · [Contributing guide](https://github.com/kvcache-ai/Mooncake/blob/main/CONTRIBUTING.md)

> This message was posted automatically by the issue bot.
