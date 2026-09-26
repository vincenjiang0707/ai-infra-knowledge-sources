# [Issue #2289] SGLang PD: prefill failure is silent and leaves the decode request hanging on bootstrap

source: https://github.com/vllm-project/aibrix/issues/2289
state: open | updated: 2026-09-19T07:37:54Z
labels: kind/bug, area/gateway, area/disaggregated

## 正文

### Describe the bug

In disaggregated mode the SGLang prefill is fired asynchronously and its result is never checked, so a failed prefill is invisible to the request path and the decode request is dispatched anyway.

In `doPrefillRequest` (`pkg/plugins/gateway/algorithms/pd_prefill_request.go`), the SGLang branch runs the prefill HTTP call in a goroutine and only logs on error:

```go
case SGLangEngine:
    go func() {
        defer r.prefillRequestTracker.RemovePrefillRequest(routingCtx.RequestID)
        if _, err := r.executeHTTPRequest(apiURL, routingCtx, payload); err != nil {
            klog.ErrorS(err, "prefill_request_failed", ...)
            return // failure swallowed
        }
        ...
    }()
```

`Route()` does not wait for this goroutine — for SGLang `doPrefillRequest` returns `nil` immediately, then `Route()` sets the decode pod and returns. The decode request already carries the `bootstrap_room` generated in `preparePrefillPayload`. If the prefill 5xx'd, timed out, or never brought up its bootstrap server, the decode pod waits on a `bootstrap_room` rendezvous that never completes and only fails on SGLang's own bootstrap timeout. The client sees a long hang followed by an opaque decode-side error, with no gateway-side signal and no fast failure.

Two consequences:

- This is asymmetric with the vLLM path, which runs the prefill synchronously (`handleSyncPrefill`) and fails the request fast when the prefill errors.
- `Route()` emits `GatewayPrefillRequestSuccessTotal` for SGLang unconditionally, because the async call returns `nil` before the prefill has actually completed — so the success metric does not reflect prefill outcome.

### Steps to Reproduce

1. Disaggregated SGLang deployment (prefill + decode rolesets) with the `pd` router.
2. Make the selected prefill pod fail the prefill as a request arrives (e.g. kill/OOM it, or block its bootstrap port).
3. Send a request → it is not failed fast; the decode pod hangs until SGLang's bootstrap timeout and then returns an opaque error. The gateway logs `prefill_request_failed` but still counts prefill success and proceeds.

### Expected behavior

A failed SGLang prefill should fail (or retry) the request rather than dispatching a decode that will hang. Options:

- gate decode dispatch on the prefill bootstrap being acknowledged / the prefill request succeeding,
- retry on another prefill pod before giving up, and/or
- surface a fast, typed error to the client.

At minimum, prefill failure should be reflected in the request outcome and in metrics (`GatewayPrefillRequestSuccessTotal` should not be emitted for SGLang when the prefill has not been confirmed).

### Environment

AIBrix: main · SGLang prefill/decode (disaggregated, bootstrap mode).


## 评论 (5)

### varungup90 · 2026-06-12

@Jeffwan This is expected behavior for SGLang. Prefill and Decode request must run asynchronously. Sync request to prefill will just hung.

### ankit373 · 2026-09-08

I traced this on current `main`. The code has moved since the report (the SGLang branch is now `DefaultExecutor.Execute`'s `handler.IsAsync()` path in `pkg/plugins/gateway/algorithms/pd/prefill/default.go:122-160`), but the behaviour is unchanged. Two corrections to the record first, one against the issue and one against the objection.

**The issue overstates it.** A failed async prefill is not fully invisible. The goroutine calls `e.executeHTTP`, which already emits `GatewayPrefillRequestFailTotal` on both a transport error (`default.go:227`) and a non-200 (`default.go:242`). So the failure is counted, and you can alert on it today. The part that is genuinely missing is narrower than "invisible".

**The objection answers a different question.** @varungup90 is right that prefill and decode must run asynchronously: SGLang's prefill call blocks on the bootstrap handshake until decode connects, so awaiting it deadlocks by construction. But "must not block on the result" and "may discard the result" are separate decisions. Nothing about the bootstrap protocol requires the second one. The async dispatch is not what I would change.

## What actually breaks

`pd_disaggregation.go:328-341`: for the async engine, `doPrefillRequest` returns `nil` immediately, then `ctx.SetTargetPod(decodePod)` returns the decode address and the decode request goes out. The prefill goroutine may fail milliseconds later. By then the routing decision is already committed.

The decode pod now holds a `bootstrap_room` that nobody will ever connect to. It waits for a KV transfer that is not coming. The client sees a stall that ends in whatever the decode-side timeout is, and the error it eventually gets has nothing to do with the real cause. The `gateway_prefill_request_fail_total` increment and the client's timeout are two facts with no join key between them except `request_id` in the logs.

So the cost is not a lost metric. It is that the system knows the request is doomed and spends the full decode timeout anyway, per failed prefill, while holding a decode slot.

## What I would propose

Keep the dispatch async. Add a completion signal keyed by the thing that already correlates the two halves, `bootstrap_room`, which `SGLangHandler.AugmentPrefillRequest` generates and writes into both the prefill payload and the decode body.

The prefill goroutine already owns the outcome. On error it can record a terminal state for that room in `PrefillRequestTracker` (which is already keyed per request and already has the lifecycle hooks: `RemovePrefillRequest` is deferred in the same goroutine). The decode path then has something to consult, and the request can be failed with the real cause instead of a timeout.

That is bounded work: one state field on an entry the tracker already keeps, one write in the existing error branch, one read on the decode side. It does not touch the handshake, does not make anything synchronous, and does not change the happy path.

The open question, and the reason I am asking rather than sending a PR: how much of the decode side is reachable at that point. If the decode request has already been proxied upstream by the time the prefill fails, the gateway may only be able to shorten the wait rather than fail it cleanly. That is a real constraint and it changes the design.

## Question

@varungup90 @Jeffwan, is the objection to the whole idea of propagating prefill failure, or only to making the prefill call synchronous? If it is the latter, I am happy to prototype the room-keyed completion signal above and put numbers on it: how long a doomed request currently occupies a decode slot versus after. If it is the former, this issue should probably be closed as working as intended so it stops showing up as an open bug, and the hang documented as expected for SGLang PD.

Either answer is useful. I would rather not build it if the team has already decided the decode-side hang is acceptable.


### ankit373 · 2026-09-16

Correction to my own proposal above: the completion signal does not have anywhere to be consulted.

`Route()` does not proxy the decode request. It returns a header mutation naming the decode pod (`gateway.go:678-679`, `HeaderMutation` in `gateway_req_headers.go`), and Envoy does the actual proxying from there. Aibrix's process is a one-shot decision maker at header-processing time; it is not in the data path for the response and has no later callback for that request. So "the decode path has something to consult" was wrong. There is no decode-side code in this gateway for a signal to reach.

Given that, I don't see a fix inside aibrix's Go code that shortens the wait once `Route()` has returned. Making the prefill call block until the bootstrap handshake connects (not full generation, just the handshake) would reintroduce the deadlock @varungup90 flagged, for the same reason: `Execute` cannot know the handshake succeeded without waiting on it. What's left is entirely outside this repo: Envoy's route/cluster timeout for the PD path, or SGLang's own bootstrap timeout, either could turn the hang into a shorter, real error instead of the full default timeout.

I'd suggest closing this as working as intended for the gateway's architecture, with the mitigation documented as an Envoy/SGLang timeout tuning matter rather than an aibrix code change. Happy to be told otherwise if there's a hook here I'm still missing.


### qidaye · 2026-09-18

@ankit373 There is a hook, and the gateway is in the data path. I have a working implementation of the "propagate the failure, keep the dispatch async" design and numbers from a real 2-prefill / 2-decode SGLang deployment, so let me put both on the record before this gets closed as working-as-intended.

## Why the gateway can still act after `Route()` returns

`Route()` only produces the header mutation, but the ext_proc stream that made that decision does not end there. Envoy keeps the same `Process` stream open for the response headers and every response body chunk (that is where the gateway already does token accounting and SSE handling today). While Envoy is waiting for the decode pod's response headers, that stream is parked in `srv.Recv()`. Nothing arrives on it until the decode pod gives up on its bootstrap, minutes later. So the gateway is not a one-shot decision maker; it is blocked on the wrong event.

The fix is to stop blocking on only that event:

- move `srv.Recv()` into one reader goroutine per stream and turn the processing loop into a `select` over the reader, the stream context, and a per-request "prefill failed" channel;
- the async prefill goroutine, which already owns the outcome, closes that channel on a terminal failure (transport error, timeout, non-2xx, cancel) after recording the class;
- when the failure wins the `select` before the decode pod has responded, the gateway sends an `ImmediateResponse` (503 / the upstream 4xx-5xx for `http_status`) with an OpenAI-shaped error body and an `x-error-pd-prefill: true` header, then closes the ext_proc stream with a gRPC error, so `failure_mode_allow: false` makes Envoy reset the decode connection. If the decode pod has already started streaming, the failure is only recorded and the stream is left alone.

Non-PD streams select on exactly the two cases they had before, so nothing changes for them. The prefill call stays async; the bootstrap handshake is never awaited.

## The decode slot

Resetting the client side does not free the decode pod by itself: it is still sitting in its prealloc / bootstrap queue for that `bootstrap_room`. SGLang's `/abort_request` endpoint only matches on `rid` (`AbortReq` has no room field), and SGLang reads `rid` from the request body, not from `X-Request-Id`. So the gateway now owns the rid: it writes `rid = <request id>-<16-hex nonce>` into both legs' bodies (fixed width, because SGLang abort matching is prefix-based), and on a prefill failure POSTs `{"rid": ...}` to the decode pod. The abort is best-effort, on its own goroutine with its own timeout, sent twice (immediately and after a short delay) because a prefill pod that refuses the connection outright lets the first abort overtake the decode leg and the tokenizer manager silently drops an abort for an unknown rid. It is skipped once the decode pod has started responding.

`bootstrap_room` stays untouched; it is only used engine-side for decode → prefill notifications. There is no prefill → decode abort path in the engine at all (`KVSender.abort()` only flips local state), which is why the gateway has to send it.

## Numbers

Fault injection on a 2P/2D deployment, prefill request timeout set to 3 s so that a cold 24k-token prompt times out on the prefill leg:

| scenario | client result | decode pod | prefill pod |
|---|---|---|---|
| prefill timeout, abort enabled | 6/6 requests got 503 at 3.01 s (was: hang until the engine's 300–600 s bootstrap timeout) | `AbortReq` dequeued and ACKed for 6/6 rids, prealloc/transfer queues back to baseline | abort notification received in the same second, 6/6 released |
| prefill timeout, abort disabled (`AIBRIX_DECODE_ABORT_TIMEOUT=0`) | same 503 at 3.01 s | released by the Envoy reset alone, ≈1.1 s after the 503 | released ≈1.1 s after the 503 |
| `kill -9` the prefill pod under load | requests routed to the dead pod: 503 in 2.2 s, class `transport`; requests on the healthy pod: 200 | abort ACKed 4/4 | n/a |

Collateral damage under normal load (≈1,800 requests, ≈65k-token prompts, no injected failures): 199 abort attempts were logged, all of them the "client closed the stream after completion" echo, all landing after the request's own `request_end` (Δ between 0.1 and 0.6 ms), all skipped because the decode pod had already responded; the engines' `num_aborted_requests_total` did not move on any pod. Routing overhead from rid generation and failure bookkeeping: `routing_time` p50 5.4 ms, p99 81 → 185 ms.

## PR

The implementation is up as #2746 (four commits: gateway-owned `rid` + decode abort with `gateway_pd_decode_abort_total{prefill_failure_class,result}`; the reader-goroutine `select` and the client-facing 503 with `gateway_pd_prefill_failure_total{class,stage}`; an e2e test with mock prefill/decode engines asserting the 503, the header and the abort arriving at the decode mock with the same rid). Env vars: `AIBRIX_PREFILL_REQUEST_TIMEOUT` (existing), `AIBRIX_DECODE_ABORT_TIMEOUT` (default 3 s, 0 disables), `AIBRIX_DECODE_ABORT_RETRY_DELAY` (default 2 s, 0 sends one attempt).

@varungup90 this keeps your constraint: nothing waits on the prefill call. It only stops discarding its result.


### ankit373 · 2026-09-19

@qidaye You're right and my correction was wrong. I checked it against `main` (`441af1f`) rather than argue from memory.

`Process` (gateway.go:295) loops on `processOnce` for the whole life of the ext_proc stream and only breaks when `st.completed` (gateway.go:344-350). Routing happens on the `RequestBody` message, but `handleProcessingRequest` keeps switching on `ResponseHeaders` and `ResponseBody` for the same stream afterwards (gateway.go:524-544). So the gateway is still in the data path after `Route()` returns; it is parked in `srv.Recv()` waiting for the decode pod's headers, which is exactly your "blocked on the wrong event". My claim that the completion signal has nowhere to be consulted was wrong, and I should have traced the message loop before writing it.

The part I had not appreciated is how small the change actually is. `processOnce` already wraps `srv.Recv()` in a goroutine and already selects over the result channel and `s.shutdownCh` (gateway.go:376-401), with the comment explaining it exists so a rollout cannot block on an idle stream. Your per-request "prefill failed" channel is a third case in a select that is already there for the same class of reason, not a new concurrency model bolted onto a synchronous loop. That also means the non-PD path keeps exactly the shape it has today, which was my other worry.

Two things I like in your design specifically:

- Making the gateway own the `rid` is the right call given `AbortReq` matches on `rid` and SGLang reads it from the body, not `X-Request-Id`. Deriving it from the request id with a fixed-width nonce keeps prefix matching predictable.
- Skipping the abort once the decode pod has started responding, and treating the abort as best-effort on its own goroutine, keeps the failure path from becoming a second thing that can hang.

The collateral-damage number is the one I would have asked for and you already have it: 199 abort attempts under ~1,800 clean requests, all post-`request_end`, all skipped, with `num_aborted_requests_total` flat on every engine. That is the measurement that makes the double-send defensible rather than just cautious.

Happy to review #2746 if another pair of eyes is useful; I have the repo built locally and I'm familiar with this path now, for whatever that is worth after getting it wrong here. Either way I'm not going to duplicate the work.

