# [Issue #4945] [RFC][MP] Configurable L2 Load Timeout with Recompute Fallback

source: https://github.com/LMCache/LMCache/issues/4945
state: open | updated: 2026-09-19T10:26:59Z
labels: 

## 正文

## Background

LMCache MP mode currently lacks a general timeout policy for L2 prefetch/load operations. When loading data from L2 is slow or never completes, inference requests may keep waiting for cached KV data indefinitely.

We would like to support a configurable waiting limit. Once that limit is reached, LMCache should allow the caller to stop waiting for the cache and fall back to recomputation.

## Motivation

Loading cached KV data is intended to reduce computation and request latency. However, when L2 queuing or loading takes too long, continuing to wait may be slower than recomputing the missing KV data.

A configurable timeout would let users set a waiting budget based on their latency requirements. Fallback should be possible when loading exceeds that budget, even if the storage system has not reported an error and the operation might eventually succeed.

## Expected Behavior

1. **A configurable L2 loading deadline**

   Users can configure the maximum waiting time for an L2 prefetch/load request, including time spent queuing and loading. This deadline is independent of the timeout for an individual message-queue request.

2. **Cache-miss fallback on timeout**

   When the deadline expires, LMCache stops making the caller wait and reports the portions that have not finished loading as cache misses, allowing the caller to recompute them. Data that is already available continues to follow the existing cache-hit semantics.

3. **Fallback for slow operations**

   The timeout policy applies to operations that exceed the waiting budget, including those that might eventually complete successfully. It should not require an explicit storage error.

4. **Correct handling of tasks and resources after timeout**

   LMCache handles late completion and resources associated with timed-out tasks correctly, preventing incorrect cache hits, duplicate completion, or persistent disruption to other requests.

5. **Compatibility and observability**

   The policy is optional, preserving the existing behavior when disabled. Logs or metrics indicate load timeouts and recompute fallbacks so users can understand their impact and tune the waiting budget.

## Discussion

We would like to discuss whether this should be a general capability of LMCache MP mode and whether related work is already planned. Configuration names, default timeout values, and implementation details can be determined in follow-up discussions.

## 评论 (2)

### JulianZJN · 2026-09-11

Hi, I’d like to work on this.

My starting point would be an opt-in monotonic deadline covering queueing and L2 lookup/load, separate from the MQ timeout in #4935. When it expires, the caller should get only the subset currently usable under the existing trim policy and recompute the rest. Late I/O would keep ownership of its buffers and locks until completion, so a timed-out request cannot free memory that an adapter is still using.

I’ll start with deterministic controller tests for timeout during lookup/load, partial completion, late completion, and a subsequent request for the same key, then add a small MP end-to-end test. Please let me know if there is existing cancellation or drain work this should build on.

### JulianZJN · 2026-09-19

PR is up: #5255.

It follows what I sketched above: an opt-in monotonic deadline from submission through queueing, L2 lookup and load; on expiry the caller gets the subset that is usable under the existing trim policy and recomputes the rest, while adapters that are still running keep their buffers and locks until they finish and the request then drains. No cancellation, no adapter interface change, default off.

Two things I'd like an opinion on:

1. Naming/placement. I put it on the server side as `--l2-prefetch-load-timeout` next to `--l2-prefetch-max-in-flight` rather than as an `lmcache.mp.*` key like `mq_timeout`, since that namespace is read by the connector and the controller is configured from `StorageManagerConfig`.
2. A draining request keeps its `max_in_flight` slot until its late I/O completes. Under a persistently slow L2 that means queued requests fall back at their own deadline (with their L1 hits) instead of piling more loads onto the adapter. It is exposed as `draining_request_count`.

With a throttled mock L2 and vLLM, the request that previously waited 2.7 s for the L2 load returns in 0.8 s with a 0.2 s deadline, and its greedy output matches a no-cache run.

