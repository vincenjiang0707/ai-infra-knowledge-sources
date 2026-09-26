# [Issue #2083] [RFC] Mooncake backend: dual-engine support (classic + native TENT mode)

source: https://github.com/ai-dynamo/nixl/issues/2083
state: open | updated: 2026-08-17T20:30:29Z
labels: 

## 正文

## Motivation

Mooncake is developing TENT, its next-generation transfer engine, with
first-class cancellation, aggregated O(1) batch status, built-in failover and
a native C API. The NIXL Mooncake plugin only drives the classic engine. This
RFC proposes (and the linked draft PR implements) a dual-engine plugin: the
classic path stays the default, byte-for-byte untouched, and an opt-in `tent`
mode wraps TENT through its native C interface.

## Related PRs

- ai-dynamo/nixl#2081 — three independent plugin/test fixes
- ai-dynamo/nixl#2082 — the dual-mode implementation (draft)
- kvcache-ai/Mooncake#3405 — tent_shared missing DT_NEEDED on mooncake_common
- kvcache-ai/Mooncake#3406 — transfer-bound notifications delivered before completion (draft)

## Why a new mode rather than a migration

Classic remains the battle-tested default for every current deployment; tent
mode gives NIXL users real cancellation semantics in `releaseReqH()` (the
classic engine cannot cancel, so releasing an in-flight handle leaks its
batch), O(1) completion polling, and a measured performance win — same
binary, same nixlbench flags, DRAM↔DRAM on an 8×H20/RoCE box:
WRITE 64MiB 101.3 vs 31.7 GB/s, READ 88.6 vs 24.2 GB/s, 4KiB latency
13.8 vs 111.4 µs (tent vs classic).

## Known issues found along the way

1. **TENT cannot deliver notifications over local (intra-agent) connections**:
   `TransferEngineImpl::sendNotification` routes every target to the RDMA
   transport and local connections never establish the notification QP
   (`endpoint.cpp` "Notification QP not connected"), so the first intra-agent
   transfer-with-notification hangs its receiver. Cross-process paths are
   unaffected. The intra-agent DRAM unit test upstream is commented out and
   the VRAM one only compiles with CUDA, which is why this had never been hit.
   Candidate fixes: (a) in-process delivery when the target is the local
   segment, (b) establish the notification QP for local connections, or
   (c) a plugin-side local-delivery fallback.
2. `mooncake_backend_test`'s final `allocateWrongGPUTest` asserts the plugin
   returns `NIXL_ERR_NOT_SUPPORTED`, which it never has — the test aborts on
   any multi-GPU machine (gated on `n_vram_dev > 1`, so single-GPU CI never
   sees it).
3. nixlbench hardcodes a notification per transfer for network backends
   (`params.notif = "0xBEEF"`); a `--no-notif` switch would need a different
   target-side completion signal — worth it for overhead measurements?

## Open questions

- Preferred fix among (a)/(b)/(c) for the local-notification gap — I'm happy
  to take it.
- `exportLocalSegment`/`importRemoteSegment` are NotImplemented in TENT; they
  map exactly onto NIXL's serializable-metadata channel. Is there an
  implementation plan?

## 评论 (1)

### xiaodouzi666 · 2026-08-17

Engine-side fix for the intra-agent notification hang is now up: kvcache-ai/Mooncake#3464. It delivers self-targeted notifications in-process, mirroring the data plane's local short-circuit. With that in place the Mooncake-plugin intra-agent notification path (the one failure recorded in this RFC) completes.
