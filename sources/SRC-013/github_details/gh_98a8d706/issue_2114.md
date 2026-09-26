# [Issue #2114] [Flow Control] Guide posture, docs, and validation for flow control (GA, opt-in)

source: https://github.com/llm-d/llm-d/issues/2114
state: open | updated: 2026-09-01T16:08:03Z
labels: 

## 正文

Flow control is GA in llm-d-router 0.10 but stays explicitly opt-in; the default flip is deferred (decision: https://github.com/llm-d/llm-d-router/pull/2180#issuecomment-5119639333, router tracker llm-d-router#1187). This issue covers the llm-d side: the surfaces that run the gate on, what the docs need to say for anyone opting in, and how we validate flow control behavior. Router work stays on llm-d-router#1187.

With the gate off by default, nothing changes for the guides that do not set it. Two shipped surfaces run flow control on today: the `flow-control` guide and `workload-autoscaling`'s `keda-epp` path. They are the scope here, together with the shared opt-in note. Nothing below binds on the v0.9.0 code freeze, though the two pre-existing breaks are still worth fixing for the release.

## What changes when the gate is on

Under saturation, requests queue and are admitted by priority instead of being rejected. Sheddable (negative-priority) requests buffer until TTL or a capacity limit.

With zero ready endpoints, requests wait rather than fast-failing; `controller/internal/processor.go:297` calls the empty pool a scale-from-zero waiting room.

`defaultRequestTTL` is 60s (`controller/config.go:33`). An explicit `0s` disables it, and validation rejects only negatives (`config.go:45,127`). Six guides set `requestTimeout: "0s"` via `recipes/router/features/httproute-flags.yaml` (`pd-disaggregation`, `wide-ep-lws`, `flow-control`, `precise-prefix-cache-routing`, `predicted-latency-routing`, `multimodal-serving/e-disaggregation`); if any of those opts in, the TTL is the only shed valve in the stack. The rest inherit the provider's gateway timeout, usually shorter than 60s, so a queued request there surfaces as a 504 before the TTL fires. Both behaviours belong in the shared note.

## Fixes

Four fixes, one PR.

- [ ] The `flow-control` guide's CRD prerequisite 404s. `guides/flow-control/README.md:92` builds the URL from `${ROUTER_CHART_VERSION}`, which `guides/env.sh:8` pins to `v0`, an OCI chart tag being used as a GitHub release tag. That URL returns 404; `v0.9.0` returns 200 and contains `inferenceobjectives.llm-d.ai`. The line can't just be deleted: `guides/flow-control/objectives.yaml` is `apiVersion: llm-d.ai/v1alpha2`, and GAIE v1.5.0's `v1-manifests.yaml` ships only `inferencepools.inference.networking.k8s.io`. So nobody following this guide by hand can create the InferenceObjectives, and the priority bands it exists to demonstrate never get defined. `env.sh` needs a router release version variable; there isn't one today.
- [ ] `workload-autoscaling`'s scale-to-zero docs promise more than the gate delivers. `README.hpa-epp.md:407` says EPP holds incoming requests until a model server becomes Ready. The 60s TTL bounds that hold, and a vLLM cold start doesn't fit inside it. Fix the text and add a cold-start-sized `flowControl.defaultRequestTTL` to the scale-to-zero opt-in.
- [ ] One shared flow-control note in `guides/recipes/router/README.md`. Every guide layers `recipes/router/base.values.yaml`, and that README already has a Values Layering section. There are 28 READMEs under `guides/`, so a per-guide note would be an unreviewable PR.
- [ ] `guides/README.md:29` links to `./rollouts/README.md`, which doesn't exist.

### Where the keda-epp TTL goes

`keda-epp/scaledobject.yaml:30` is `minReplicaCount: 1`, so the shipped path always has a ready endpoint and the empty-pool wait never triggers. Scale-to-zero is optional and lives only in prose at `README.hpa-epp.md:401-417`.

That decides where the fix lands. `defaultRequestTTL: 10m` in `keda-epp/router.values.yaml` would give the default `minReplicaCount: 1` path a ten-minute queue wait under saturation, worse than the 60s it has today. The TTL belongs beside `minReplicaCount: 0` in the opt-in.

Turning the gate off is wrong either way: it would throw away the priority behaviour that path demonstrates, and the KEDA trigger scales on `llm_d_epp_flow_control_queue_size`, which only exists when the gate is on.

### What the shared docs note should cover

- Flow control is GA and opt-in; `featureGates: ["flowControl"]` turns it on
- Requests queue under saturation and are admitted by priority
- With zero ready endpoints requests wait, bounded by `defaultRequestTTL` (60s) or by the gateway timeout where that's shorter
- The six `requestTimeout: "0s"` guides would have the TTL as their only shed valve if they opt in; the rest see a provider 504 first
- Tuning: per-band `maxRequests` and `maxBytes`, `defaultRequestTTL`, priority holdback
- The dependency on model-server scrape health. The saturation detector scores each pod from `WaitingQueue` and `KVCacheUsage`, pulled by the EPP's own poll of the model servers. If that goes stale or empty across all endpoints, everything reads as saturated and dispatch halts (llm-d-router#2100). Separate from the Prometheus-scrapes-the-router path in #1777.

## Validation

- [ ] #1918, restore the bespoke flow-control nightly. With the fleet running the gate-off default, this is the only automated lane that exercises flow control behaviour at all (backpressure, per-band isolation, priority QoS).
- [ ] Write `guide_flow-control_1.yaml`. The one guide whose purpose is queue contention has no workload that produces any, which is why #1918 carries it commented out.
- [ ] A/B at saturating load: `optimized-baseline` first, then `pd-disaggregation`, which is the interesting one because P/D saturation gating (llm-d-router#1186) isn't ready and the saturation signal there is untested. Not time-pressured: the FC-off arm is the shipped default and stays dispatchable indefinitely. This is the operator-facing evidence for opting in (goals 2 and 3) and the baseline for any future default-flip revisit.

| # | Goal | Covered by | State |
|---|---|---|---|
| 1 | Feature completeness: the gate-on surfaces stand up and serve | #1918's lane; `keda-epp` has none (see CI) | gap |
| 2 | Change of behavior: what an operator sees differently after opting in | the A/B | not started |
| 3 | Performance: cost of opting in against published numbers | the A/B | not started |
| 4 | Logging, metrics, tracing: queue state is observable | #1777, llm-d-router#2102 | not started |
| 5 | Reliability: failure modes known and bounded | #1918's lane | in progress |
| 6 | Operations: how to run it, tune it, turn it off | the docs note above, #1519 | not started |

All 34 lanes run `sanity_random.yaml` (#1725, merged Jun 8, described as temporary, with nothing tracking the revert), so there has been no perf signal from CI for six weeks. A sanity workload also never queues, and flow control is work-conserving, so under non-saturating load FC-on and FC-off are identical by construction.

The A/B doesn't need manual standup: per-guide profiles exist in `llm-d-benchmark/workload/profiles/inference-perf/` and every lane still declares a `workload` dispatch input. Six guides publish committed benchmark reports with hardware specified (`optimized-baseline`, `tiered-prefix-cache`, `precise-prefix-cache-routing`, `predicted-latency-routing` and `agentic-serving` under `benchmark-results/`, `pd-disaggregation` inline in its README); where that hardware isn't reproducible, an FC-off control run on whatever is available does the same job.

Goals 4, 5 and 6 are desk work: metrics and tracing coverage (#1777, llm-d-router#2102), the failure-mode enumeration, and the operations guide (#1519). #1918's lane covers the backpressure, per-band isolation and priority-QoS half of goal 5 once it's green.

The 2026-07-25 per-lane pass-rate baseline on llm-d-router#1187 stays the reference point for any future default-flip revisit.

## CI

- [ ] #1918, see above.
- [ ] `keda-epp` has no nightly coverage. `grep -rn keda-epp .github/` returns nothing, and the green OCP lane exercises the FC-off path. Tracked separately in TBD.
- [ ] llm-d-infra's `reusable-ci-nightly-benchmark.yaml` has a flow-control special case that borrows optimized-baseline's modelserver overlay, but it runs after the model-detection step that needs the missing directory. Dead code.

## Related issues

None of these block v0.9.0; they matter to anyone opting in.

- #1777, router monitoring in the well-lit guides. The monitoring sections cover model servers only, so the EPP's own metrics aren't scraped anywhere. With flow control on they're the only view of whether a request is queued or in flight, and a dispatch halt otherwise looks like everything hanging and then 503ing.
- #1519, operational flows documentation. FC state is per-replica, so in active-active mode fairness holds only within each replica's slice and per-band limits multiply by replica count. llm-d-router#2180 documents that in the router's `docs/operations.md`, which guide readers never open.
- #1525, request draining in all guides. Drain semantics and 503 mapping are FC-adjacent; llm-d-router#1187 has an open question on dispatch-until-deadline against immediate evict.
- #1516, migrate CI to nightly images. Because the charts pin EPP to `:main`, a default flip could not have been staged from the router side; pinned nightly images would make a future one controllable.

## Not tracked here

Router hardening, perf numbers, and router-side observability and reliability work all live on llm-d-router#1187. The deferred default flip is llm-d-router#2104.


## 评论 (3)

### LukeAVanDrie · 2026-07-25

/assign

### LukeAVanDrie · 2026-07-25

I'm keeping tabs on this and will likely drive most of this myself, but this is an area I could use help if guide owners have cycles.

### LukeAVanDrie · 2026-07-31

Update: the default flip is deferred; flow control is GA but stays explicitly opt-in (decision: https://github.com/llm-d/llm-d-router/pull/2180#issuecomment-5119639333). I have retitled this issue and reframed the body for the opt-in posture; the flip plan is in the edit history.
