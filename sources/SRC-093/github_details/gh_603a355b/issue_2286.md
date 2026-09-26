# [Issue #2286] Map gateway SLO tiers to vLLM request priority

source: https://github.com/vllm-project/aibrix/issues/2286
state: open | updated: 2026-09-24T10:27:39Z
labels: area/gateway, kind/feature

## 正文

### Feature Description and Motivation

We rank and queue requests by SLO at the gateway (`slo.go`, `queue/slo_queue.go`), but once dispatched the engine schedules FCFS, so that ordering doesn't survive into vLLM. vLLM supports `--scheduling-policy priority` with a per-request `priority`. Passing our SLO tier through as priority lets the engine preempt/order in line with SLO, so a latency-sensitive request that lands behind a batch of low-tier ones still runs first inside the engine.

### Use Case

Mixed-tier traffic on shared replicas (interactive vs batch). Today a burst of low-priority work can head-of-line block latency-sensitive requests at the engine, even when the gateway tried to prioritize them.

### Proposed Solution

Gateway derives a `priority` from the request's SLO class and sets it on the upstream vLLM request; deployments run with `scheduling-policy=priority`. Map a small fixed set of tiers and document the semantics (lower value = higher priority in vLLM).


## 评论 (4)

### dreamer-89 · 2026-06-23

Thanks @Jeffwan for creating this issue. I am interested in taking this issue. Please let me know. 

As mentioned in the proposed solution, my plan is to derive a request priority from the SLO tier at the gateway and set it on the upstream vLLM request, with the tier to priority mapping and document the semantics. 

### bolubo · 2026-09-22

Thanks @Jeffwan. This is a real gap: the gateway orders by SLO, but that ordering doesn't survive past dispatch, so a batch burst on a shared replica can still head-of-line block interactive traffic.

@dreamer-89 I saw you raised your hand for this back in June. Are you still planning to work on it? If you've moved on (or don't have the bandwidth right now), **I'd like to take this issue.**

I checked the request path first: nothing reads or writes the vLLM `priority` field today, and a client-supplied value passes through as-is. Assuming nobody objects, here's the plan I'd start from:

- Derive `priority` at the gateway from the request's SLO tier and set it on the upstream vLLM request (inject at the existing request-body rewrite point); when the deployment isn't opted in, nothing is sent and behavior is unchanged.
- Keep the mapping small and fixed, with lower = higher (matching vLLM), and restrict v0 to de-prioritizing: batch/background tiers get a positive value while everything else stays at the engine default `0`, so no traffic gets silently promoted ahead of the default.
- Add unit tests for the mapping and the on/off injection matrix, and document the `--scheduling-policy=priority` deployment requirement.

Two things I'd love a steer on before I start writing code:

1. Where should the tier come from in v0: the deployment's config profile, or a per-request declaration?
2. Is "v0 only de-prioritizes" acceptable, or would you rather have an explicit priority for the interactive tier as well?

I'll wait a couple of days for objections (and in case @dreamer-89 is still on it); if none, I'll open a draft PR so we can iterate on the code directly.

### bolubo · 2026-09-23

A couple of days have passed with no objections, and @dreamer-89 has not posted since June, so I went ahead and opened the draft PR: #2787.

Two notes on how I settled the questions I raised above, both easy to change while the PR is a draft:

1. **Tier source: a request header (`x-aibrix-slo-tier`).** A header keeps v0 independent of the config profile machinery and of the deployment manifest, so any client the gateway already serves can use it, and adding a profile field later on top of it stays possible.
2. **v0 only de-prioritizes**, as proposed. `batch` maps to `100` and `background` to `1000`, both below the engine default of `0`, so there is no path by which turning the feature on pulls a request ahead of one that did not set a tier. An explicit head start for a latency-sensitive tier is a separate change; keeping it out of this one is what makes this one safe to switch on for a shared endpoint.

The rest of the v0 shape:

- Off by default behind `AIBRIX_SLO_TIER_PRIORITY_ENABLED`; while it is off the header is ignored and request bodies are forwarded byte for byte.
- A `priority` the caller already set in the body is never overwritten.
- Requests without the header, with a tier outside the table, or with a body the rewrite cannot extend (non-JSON, truncated, or the multipart audio/video endpoints) are forwarded unchanged. The tier is a hint and never fails a request.
- The rewrite lands at the existing request-body rewrite point, after a target pod is chosen, and the `content-length` sent to Envoy is recomputed from the rewritten body.
- vLLM deployments need `--scheduling-policy=priority` for the field to have an effect; that requirement is documented in the PR.

Please take a look when you have a moment.

### bolubo · 2026-09-24

#2787 merged today, so this should be covered now. One naming note compared to the earlier comment: after review the header ended up as `x-aibrix-priority-tier`, with `AIBRIX_PRIORITY_TIER_ENABLED` as the opt-in env var.

Behavior is as described: `batch` 100 and `background` 1000, de-prioritize only; requests without the header, or with a tier outside the table, are forwarded unchanged, and a caller-set `priority` is kept. Tests and docs are included, and vLLM deployments need `--scheduling-policy=priority` for the field to have an effect. If this looks complete, the issue can be closed.

