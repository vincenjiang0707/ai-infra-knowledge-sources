# [Issue #2680] [RFC]: Token-weighted prefill load policies for the PD router (token_load, hybrid_cache_load)

source: https://github.com/vllm-project/aibrix/issues/2680
state: closed | updated: 2026-09-09T06:57:40Z
labels: area/gateway

## 正文

> **Status (2026-09-09):** implemented and merged. PR 1 #2681 (`token_load`, tracker, metrics, wiring) and PR 2 #2682 (`hybrid_cache_load`, `AIBRIX_MIN_MATCH_PCT`, `new_tokens` charge) are both on `main`. The text below is the original proposal; the places where the merged code differs from it (session header name, session-table bounds, env variable ranges, metric names) are marked **[as merged]**.

### Summary

Add two prefill score policies to the PD router that measure a prefill pod's load in **estimated prompt tokens** instead of in requests:

- `token_load`: pick the pod with the lowest token-weighted load.
- `hybrid_cache_load`: same load figure, discounted by the pod's prefix-cache match so that cache affinity can override *small* load differences but never large ones.

Both read one shared in-memory `TokenLoadTracker` that the router keeps in step with its own routing decisions:

```
priority(pod) = active_prefill_tokens(pod) + kv_weight * resident_kv_tokens(pod)

token_load:         score = priority
hybrid_cache_load:  score = priority * (1 - (match_pct/100)^2 * cache_factor)
```

Lower is better. `active_prefill_tokens` is charged when the pod is selected and released when the prefill HTTP call returns. `resident_kv_tokens` is charged at the same time and released when the whole request finishes, because the prefill pod keeps that request's KV cache until the decoder has pulled it.

No new dependencies, no engine-side changes, no change to the `PrefillScorePolicy` interface. Selection is `AIBRIX_PREFILL_SCORE_POLICY=token_load|hybrid_cache_load` or `routingConfig.prefillScorePolicy`, like the existing policies.

The design was developed by my colleague @zhutong196 and me on a downstream fork of AIBrix; PRs will carry `Co-authored-by` for both of us.

### Motivation

The three existing prefill policies all count **requests**, not tokens, when they look at load:

| Policy | Load term |
| --- | --- |
| `prefix_cache` | `req_count / max_req_count` (tie-break after prefix match) |
| `least_request` | `req_count` |
| `conductor` | `queue = req_count * avg_prefill_seconds` |

For prefill this is a poor proxy. Prefill cost is roughly linear in prompt length, and on the workloads we run (a mix of short chat turns and long multi-turn agent prompts, several prefill replicas per model) prompt lengths in the same second routinely differ by an order of magnitude or more. With `least_request`, a pod holding one 40k prompt looks *less* loaded than a pod holding two 500-token prompts, so the next long prompt is sent to the pod that is already busiest. `conductor` scales the queue by the pod's historical average prefill time, which helps when the length mix is stationary but still charges every in-flight request the same amount. `prefix_cache` only consults load as a tie-breaker, so it has the same pile-up, and in addition a 1% incidental prefix match (a shared system prompt) outweighs the whole load range: `(100-1)*0.1 = 9.9` versus `10`.

We have been running these policies on a downstream fork since August 2026, with SGLang prefill engines and HiCache (L3 KV storage); the gateway code path is engine-agnostic. Measured on that setup:

- against the previous gateway build (`prefix_cache`-style affinity plus request-count load) at 70 concurrency, 500-request multi-turn replays, 4 prefill replicas (a prefill-only deployment, DP4/TP8, so the numbers are for the prefill scoring path rather than a full PD pair): input throughput +3.4%, P50 -1.6%, P95 -13.7%, P99 -21.2%, max latency -26.0%; per-replica compute imbalance (coefficient of variation) stayed around 5%;
- `hybrid_cache_load` keeps prefix-cache hits for multi-turn traffic while still spreading cold long prompts;
- the tracker is cheap: two lock-free counters per pod and no allocation on the score path, so it adds nothing measurable to the per-request cost inside `selectMu` (#2678).

The `resident_kv_tokens` term exists because in PD the prefill pod is not free the moment its HTTP call returns: its KV blocks for that request stay allocated until decode has finished pulling them. Weighting resident KV at a fraction of active prefill (default `0.3`) keeps a pod that has just prefilled several long prompts from being picked again immediately, which otherwise shows up as KV-cache pressure on the prefiller while the decoders are still pulling.

### Proposed Change

All changes are inside `pkg/plugins/gateway/algorithms` and `pkg/plugins/gateway/algorithms/pd`.

**1. Cost of a request**

```
cost(request) = request_cost + new_tokens
```

- `new_tokens` is the part of the prompt the selected pod actually has to compute, resolved in this order:
  1. when the request carries the caller-owned `x-aibrix-session-key` header (`constants.HeaderSessionKey`, the same opaque key `session-affinity` routing uses), the growth of the prompt since the previous turn of that session (a small TTL'd map of (model, session) -> last prompt size). In multi-turn traffic each turn resends the whole history but the engine only computes the new turn, so charging the full prompt overstates the load by the length of the history. **[as merged]** The proposal originally named the gateway-issued `x-session-id` (`constants.HeaderSessionID`); review pointed out that token is minted by the gateway per client connection, not by the caller, so the merged code reads `x-aibrix-session-key` instead and never consults `x-session-id`. The rule assumes the earlier turns' KV is reachable from whichever prefill pod is selected (shared or tiered KV store, sticky routing, or the pod's own prefix cache); deployments where that does not hold should not send the key, or set `AIBRIX_TOKEN_LOAD_SESSION_TTL_SECONDS=0` to turn the rule off and fall through to rule 2. Because the key is client-supplied, keys longer than 256 bytes are ignored and the table holds at most `AIBRIX_TOKEN_LOAD_MAX_SESSIONS` entries; once full, new keys are charged by rules 2 and 3 until the janitor frees slots;
  2. otherwise, when the policy has prefix-match information for the selected pod (`hybrid_cache_load`), `prompt_tokens * (1 - match_pct/100)`;
  3. otherwise the full `prompt_tokens`.
- `prompt_tokens` defaults to `len(ctx.ReqBody) / 4`, the same heuristic the vLLM PD proxy examples use; `hybrid_cache_load` already tokenizes the prompt for prefix matching and uses the real count.
- `request_cost` (default `3500` tokens) is a fixed per-request overhead. It models scheduling and KV transfer setup that do not scale with prompt length; it also keeps very short requests from looking free (`AIBRIX_TOKEN_LOAD_REQUEST_COST`).

The same `cost` is added to both `active_prefill_tokens` and `resident_kv_tokens` of the prefill pod.

**2. `pd.TokenLoadTracker` (new file `pd/token_load_tracker.go`)**

```go
func NewTokenLoadTracker() *TokenLoadTracker
func (t *TokenLoadTracker) AcquirePrefill(requestID, pod string, cost float64) // + active, + kv
func (t *TokenLoadTracker) ReleaseTokens(requestID string)                    // - active (prefill returned)
func (t *TokenLoadTracker) ReleaseKVCache(requestID string)                   // - kv     (request finished)
func (t *TokenLoadTracker) ReleaseAll(requestID string)
func (t *TokenLoadTracker) GetPriority(pod string) float64                    // active + kv_weight*kv
```

- Per-pod counters are `atomic.Uint64` holding float64 bits, updated with a CAS loop and clamped at zero; every `Release*` is idempotent per request ID, so a double release can never drive a pod negative.
- A janitor goroutine sweeps entries older than `AIBRIX_TOKEN_LOAD_TTL_SECONDS` (default `3600`) so a request whose completion path never ran cannot pin load on a pod forever. **[as merged]** The env variable must be positive (`utils.LoadEnvInt` rejects `0`); `TTL: 0` in `TokenLoadConfig` disables the sweep for tests. The same janitor also drops the counters and metric series of pods that have been idle at zero load for a minute, so autoscaled prefill pods do not accumulate on the gateway.

**3. Policies (`pd/prefill_scorer.go`)**

- `token_load`: `Prepare` is trivial, `ScorePod` returns `GetPriority(pod)`, `PrefixHashes` returns nil (no prefix-index update, like `least_request`).
- `hybrid_cache_load`: `Prepare` tokenizes and calls `MatchPrefix` exactly as `prefix_cache` does. `ScorePod` returns `priority * (1 - r^2 * cache_factor)` with `r = match_pct/100`. The quadratic curve keeps load dominant at low hit ratios and only lets high hit ratios (a real multi-turn continuation) win against a less loaded pod; with the default `cache_factor = 0.5`, a 100% hit is worth a 50% load difference, a 50% hit only 12.5%. When every candidate is idle (`priority == 0`), the pod with the highest match wins, so a warm continuation still lands on its cache.
- `AIBRIX_MIN_MATCH_PCT` (default `0`, off): matches below this percentage are treated as 0. Concurrent cold requests share a preamble (system prompt, cache-namespace line), so they match each other's heads by a few percent on whichever pod was inserted first. Without the clamp that incidental overlap makes one pod a deterministic magnet for the whole warm-up burst at idle. This would be useful for `prefix_cache` too (same 9.9-vs-10 effect above). **[as merged]** PR 2 applies the clamp to `hybrid_cache_load` only, both in the score and in the `new_tokens` charge; extending it to `prefix_cache` is a possible follow-up, not part of this RFC.

**4. Wiring in `pdRouter` (`pd_disaggregation.go`)**

- `NewPDRouter` creates one tracker per router; both new policies are registered in the existing policy switch (env and routing-config paths).
- Charging happens inside the region that #2678 protects with `selectMu`, right after the prefill pod is chosen, so concurrent selections see each other's charges.
- `ReleaseTokens` runs where `RemovePrefillRequest` already runs (after the prefill HTTP call, sync and async paths).
- `ReleaseKVCache` runs on request completion: `pdRouter` implements `cache.RequestTracker` (`DoneRequestCount` / `DoneRequestTrace`; `AddRequestCount` is a no-op) and registers itself with `cache.RegisterRequestTracker`, which is how `PowerOfTwoRouter` gets its completion callback today. No new hook in `RoutingContext` or `gateway.go`.

**5. Metrics**

Two gauges labelled by `pod_name`: `pd_token_load_active_tokens` and `pd_token_load_kv_tokens` (**[as merged]** registered in `pkg/metrics/gateway_metrics.go` without the `aibrix_gateway_` prefix the draft used, matching the other gateway metrics there). They make "why did the router pick this pod" answerable from Grafana.

**6. Configuration**

| Env | Default | Meaning |
| --- | --- | --- |
| `AIBRIX_PREFILL_SCORE_POLICY` | `prefix_cache` | `token_load` / `hybrid_cache_load` select the new policies |
| `AIBRIX_TOKEN_LOAD_KV_WEIGHT` | `0.3` | weight of resident KV tokens in the priority |
| `AIBRIX_TOKEN_LOAD_REQUEST_COST` | `3500` | fixed per-request cost, in tokens |
| `AIBRIX_TOKEN_LOAD_TTL_SECONDS` | `3600` | janitor TTL for stale charges; must be positive |
| `AIBRIX_TOKEN_LOAD_SESSION_TTL_SECONDS` | `1800` | how long a session's last prompt size is remembered; `0` turns the session-delta rule off **[as merged]** |
| `AIBRIX_TOKEN_LOAD_MAX_SESSIONS` | `100000` | upper bound on remembered (model, session) entries **[as merged]** |
| `AIBRIX_HYBRID_CACHE_LOAD_FACTOR` | `0.5` | maximum discount at 100% prefix match, `0` to `1` (`1` lets a full match always win, `0` turns the discount off) |
| `AIBRIX_MIN_MATCH_PCT` | `0` | matches below this are ignored, `0` to `100` |

Out-of-range or unparsable values log a warning and fall back to the default.

**7. Delivery**

Two PRs, both merged:

1. #2681 (merged 2026-09-09, a374e4c1): `TokenLoadTracker` + `token_load` policy + metrics + router wiring + docs (full-prompt cost).
2. #2682 (merged 2026-09-09, 7a346b9f): `hybrid_cache_load` + `AIBRIX_MIN_MATCH_PCT` + the `new_tokens` cost (session delta / prefix match). This is the combination we validated, so it shipped as one unit.

Tests: tracker unit tests (acquire / release ordering, idempotent release, clamp at zero, janitor with an injected clock), policy tests, and a router-level burst test in the style of `TestPDRouter_ConcurrentBurstSeesPriorSelections` (#2678) with mixed prompt lengths. Docs: a section in `docs/source/features/pd-disaggregation.rst` next to `conductor` and rows in the policy tables.

**Out of scope**: per data-parallel-rank load keys. Our fork tracks load per DP rank and picks a rank inside the pod, but that needs DP-rank aware PD routing (#1858 was closed in favour of #1866, which covers the non-PD path only) and is a separate proposal.

### Alternatives Considered

- **Extend `conductor` instead of adding policies.** Conductor already estimates prefill time from token counts for the *candidate* request; what it lacks is token-weighted *queue* state. Its queue term could adopt the tracker in a follow-up, but conductor depends on engine histograms (`RequestPrefillTimeSeconds`) that not every engine exports and has several other knobs. Standalone policies are easier to reason about and to compare against.
- **Read the engine's own metrics** (`num_requests_waiting`, KV cache usage) instead of tracking in the gateway. Those are scraped on a multi-second interval, so during a burst every selection sees the same stale value and the burst lands on one pod. The gateway-side ledger is updated synchronously with the decision; the two are complementary, and `load_balancing` on the decode side already uses the scraped values.
- **Charge the full prompt and let the prefix discount do the rest.** We ran this variant (`hybrid_cache_load` with full-prompt cost) against the session-delta variant on the same replays as above: throughput was equal within noise and P50 was 4% better with the full-prompt cost, but P95 / P99 / max latency were 11% / 14% / 25% higher and per-replica compute was less even (CV 8.8% versus 5.0%). Charging history tokens the engine never computes makes a warm replica look busier than it is, so the router steers new sessions away from it too aggressively.
- **Linear instead of quadratic cache discount.** Linear would let a 30% incidental match override a 30% load difference, which is exactly the pile-up the policy is meant to remove; quadratic keeps small matches nearly weightless and only rewards real continuations. We did not benchmark a linear variant separately; the choice follows from the incidental-match observation behind `AIBRIX_MIN_MATCH_PCT`.



## 评论 (1)

### qidaye · 2026-09-09

Delivered: #2681 (token_load, merged as a374e4c1) and #2682 (hybrid_cache_load, AIBRIX_MIN_MATCH_PCT, new_tokens charge, merged as 7a346b9f). The body above is updated to what landed. The prefix_cache follow-up mentioned in the RFC is #2689. Closing.

