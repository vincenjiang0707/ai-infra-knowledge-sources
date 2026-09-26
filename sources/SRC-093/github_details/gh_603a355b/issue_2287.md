# [Issue #2287] Prefix cache index not invalidated when a vLLM engine clears its prefix cache (reset/OOM/sleep)

source: https://github.com/vllm-project/aibrix/issues/2287
state: open | updated: 2026-09-16T08:03:30Z
labels: kind/bug, area/gateway

## 正文

### Describe the bug

When an engine clears its prefix cache — `/reset_prefix_cache`, OOM-driven reset, or `/sleep level>=1` — it wipes the cache and enqueues `AllBlocksCleared`. We don't act on it: `handleAllBlocksCleared` is a no-op (`pkg/kvevent/handler.go`), and the only caller of `RemovePrefix` is pod unsubscribe, which doesn't fire here (the pod stays `Running`, `/health` still returns 200). So stale entries linger, and because the prefix router prefers the pod with the most matching blocks, it actively routes prefix traffic to the pod whose cache was just wiped — a cold miss.

The event alone isn't a reliable fix: vLLM publishes queued KV events only from inside a scheduler step (`update_from_output`), so an idle/sleeping engine may never flush `AllBlocksCleared`, and ZMQ delivery is lossy.

### Steps to Reproduce

1. Two replicas with the kv-event prefix router; warm a shared prefix on pod A.
2. `POST /reset_prefix_cache` on pod A (or `/sleep?level=1`).
3. Send the same prefix again → still routed to A, now a cold miss.

### Expected behavior

- `handleAllBlocksCleared` calls `RemovePrefix(model, loraID, podKey)` (already on the `SyncIndexer` interface).
- A reconcile against the scraped `vllm:engine_sleep_state` metric backstops dropped events (purge entries for pods reporting non-awake).
- When AIBrix drives sleep itself (separate sleep-mode RFC), it should also purge synchronously on `/sleep` — tracked there.

### Environment

AIBrix: main · vLLM: main (kv-events enabled).


## 评论 (5)

### Jeffwan · 2026-06-09

wait until #2290 is implemented

### pjdurden · 2026-06-21

Opened #2385 for part 1: handleAllBlocksCleared now calls RemovePrefix(model, loraID, podKey) to purge the pod from the prefix index, mirroring handleBlockRemoved. Tests cover the purge call, temporary-error swallow, and error propagation.

Left the metric-driven reconcile backstop (purge against scraped vllm:engine_sleep_state) for a follow-up since it is a larger change and, as you noted, the event alone is not fully reliable. Happy to take that next if the approach in #2385 looks right.

### ankit373 · 2026-09-08

@pjdurden are you still planning to take the metric backstop? Asking before I start so we do not write it twice. If you are on it, ignore the rest of this except the locking note, which is worth having either way.

I went through what the backstop would touch. Two things decide the design, and neither is obvious from the issue text.

## The purge is expensive and takes the router's lock

`SyncPrefixHashTable.RemovePrefix` (`pkg/utils/syncprefixcacheindexer/sync_hash.go:422`) takes `contextData.prefixMu` and then walks every prefix entry for that `(model, loraID)`:

```go
for prefixHash, pods := range prefixStore.prefixMap {
    delete(pods, podName)
    ...
}
```

That is O(P) in the number of cached prefixes for the model, under a write lock that the prefix router needs for lookups. Fine as an event handler, since `AllBlocksCleared` is rare. Not fine on a scrape loop.

So the backstop has to be **edge triggered, not level triggered**. If it purges on every refresh where the pod reports non-awake, a single sleeping pod takes that write lock and scans the whole prefix map once per `podMetricRefreshInterval`, for as long as it stays asleep, and blocks routing lookups while it does. Keeping the last observed sleep state per pod and purging only on the awake to non-awake transition makes it one O(P) purge per transition instead of one per tick.

This is the same shape as any latched-gauge alert: the interesting thing is the edge, and treating the level as the trigger turns a rare event into a permanent cost.

## Restart has to count as an edge

Edge triggering alone loses the case the backstop exists for. If the gateway restarts while a pod is asleep, there is no previous state, no transition is observed, and the stale entries stay forever, which is exactly the bug. Seeding the per-pod state as awake on first observation fixes it: the first scrape that reports non-awake reads as a transition and purges once. Costs nothing and makes a cold start self-correcting.

## What already exists

- `metrics.EngineSleepState` is defined and mapped to `vllm:engine_sleep_state` (`pkg/metrics/metrics.go:22,156`), so the scrape side needs no new plumbing.
- There is already a pod metric refresh ticker at `pkg/cache/cache_init.go:419`, which is the natural place to hang this rather than adding another loop.
- `RemovePrefix` is already on the `kvevent.SyncIndexer` interface and reachable through `syncIndexerAdapter` (`pkg/cache/store_providers.go:201`), so part 1 already proved the call path.

One thing I have not pinned down: the metric description says `awake`, `weights_offloaded` and `discard_all` are separate signals, so I need to confirm whether that is one gauge with a state label or several series before writing the predicate. Sleep level 1 and level 2 both wipe the KV cache, so both should purge, but I would rather read the exporter than guess.

## Scope

Worth being explicit that this only backstops dropped or never-flushed events. It does not make the index correct in general, since a pod can also lose blocks through ordinary eviction that no event covers. It closes the specific hole in the issue: an engine that wiped its cache and never told us, while `/health` keeps returning 200.

Happy to implement it with the edge trigger and restart seeding, plus tests for the transition, the no-transition steady state, and the restart case. Just say the word, or say you have it and I will stay out of the way.


### ankit373 · 2026-09-16

No response after a week, so I went ahead with the piece that's independently useful either way. #2735 fixes a real bug I hit while scoping the backstop: `vllm:engine_sleep_state` reports three label-differentiated series under one name, and the fetcher was reading whichever one happened to scrape first (`Metric[0]`), not necessarily `awake`. Fixed with a label filter, tested end to end.

The tracker and edge-triggered purge (the actual backstop) are still open. @pjdurden, still happy to take it if you're not already on it, the design in my comment above stands. Let me know either way.


### ankit373 · 2026-09-16

Update: the tracker and edge-triggered purge are done too, added to #2735 (same PR, grew past its original scope). That's the full backstop design from my comment above, implemented and tested.
