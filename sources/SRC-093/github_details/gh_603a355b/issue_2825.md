# [Issue #2825] [RFC]: Autoscaler-driven elastic EP: observe-first staging, membership semantics, and failure rules

source: https://github.com/vllm-project/aibrix/issues/2825
state: open | updated: 2026-09-27T05:03:40Z
labels: kind/feature, area/orchestration

## 正文

### Summary

AIBrix's PodAutoscaler scales replicas, and for MoE serving that unit is coarse: one replica can span dozens of GPUs, and traffic rarely varies in whole-replica quanta. vLLM can now resize DP/EP membership at runtime (`enable_elastic_ep`, `POST /scale_elastic_ep`, `POST /is_scaling_elastic_ep`, plus the DP-coordinator wave protocol), and #2288 asks AIBrix to drive it, starting observe-only. This RFC proposes how that drive should work, staged as observe, act, and graceful draining, and focuses on the platform-side semantics that are missing today: aligning three divergent states (Kubernetes resources, engine-committed membership, routable capacity), treating an engine resize as a transaction inside a reconcile loop, and writing down failure rules before production discovers them. The proposal is deliberately conservative: default off, hold rather than auto-recover, never act on unverified state. The observe stage is already in flight (#2812); we are asking for feedback on the act-side semantics before implementing them.

### Motivation

Whole-replica scaling is coarse and expensive for MoE: one replica may span dozens of GPUs, and traffic variation is rarely a whole-replica quantum. The engine now exposes the levers to resize DP/EP membership at runtime, but nothing in AIBrix drives them. Existing platform attempts in this space are either heavy (new CRDs, gated off) or still exploratory, and the upstream external-orchestration contract is not frozen yet (vllm/vllm#42515, vllm/vllm#43202).

**Benefit hypothesis (to be measured).** Two effects decide whether elastic EP is worth enabling. Sub-replica demand changes can be absorbed inside a footprint instead of moving whole replicas, which makes capacity quantization finer and avoids provisioning for step peaks; and ramps can be served as soon as the engine commits new ranks, without waiting for new pods. The cost side is the commit window (the engine answers 503 while resizing) and the added control complexity this RFC addresses. Enabling is least attractive when demand is stable at whole-replica quanta or when the window is not acceptable for the served workload. We plan to measure the deciding axes on one node first (time to add capacity for a width move versus a replica move, GPU-hours per unit of served traffic under bursty load, and error budget consumed during commit windows); multi-footprint economics need a larger setup and remain future work.

Three properties make this harder than an HPA-style target:

1. **Three states, not one.** Kubernetes knows which pods and processes exist; the engine knows which ranks are committed; the router knows which endpoints can take traffic. These states move at different speeds and in different orders: during a scale-up, capacity exists before the engine accepts it; during scale-down, the engine stops first and capacity is reclaimed after; after a rank failure, the desired state is unchanged while the engine serves degraded. "Replica count" cannot express any of this.

2. **A transaction inside a control loop.** An engine resize is a one-shot operation that takes tens of seconds, has intermediate states, and has no generic rollback. Today's known upstream bugs include a cancel path that corrupts engine state without rollback (vllm/vllm#57691) and a scale-up crash under EAGLE3 + CUDA graphs (vllm/vllm#58479). Kubernetes reconciliation, by contrast, assumes idempotent, replayable steps with eventual convergence; it has no word for "commit or hold". That gap has to be designed rather than coded ad hoc.

3. **No failure vocabulary.** Every step can fail quietly: partial joins, a controller restarting mid-commit, outcomes that cannot be verified after a timeout. Writing down the required behavior for these cases is the core of this RFC.

### Proposed Change

| Stage | What it adds | State |
|---|---|---|
| 0: observe | record engine scaling state in PodAutoscaler status; no decisions | in flight (#2812) |
| 1: act | opt-in width changes with transaction discipline and gates | this RFC |
| 2: draining | gateway policy for the engine's 503 window | this RFC (design) |

**Stage 0: observe (in flight: #2812).** PodAutoscaler records whether a scaling commit is in progress on the target's elastic-EP engines in `status.elasticEPScaling` (`inProgress`, `observedEngines`, `scalingEngines`, `lastTransitionTime`; no width read exists yet). No replica decisions change. This gives operators visibility and gives the controller a trustworthy read path for Stage 1.

**Stage 1: act with guardrails (opt-in, default off).** For deployments that enable elastic EP and opt in:

1. Read the **committed** width from the engine; never trust the last requested value.
2. Use target semantics: ask the engine to *be N* (the engine call takes `new_data_parallel_size` and a `drain_timeout`, default 120s), not to add one, so retries and re-ordering are harmless.
3. Treat each call as a transaction inside reconcile: one bounded operation per attempt (call, wait for commit up to a bound, verify, record the outcome, continue).
4. Gate every operation: never act while the engine reports scaling; never act on degraded or partially committed membership; enforce a settle window and hysteresis so a tens-of-seconds operation cannot oscillate.
5. Re-read state every reconcile; the controller never trusts its own last command (level-triggered).
6. Single writer for width: while act mode is on, the controller is the intended single writer for width; other writers are outside this contract and are surfaced as drift (F7).

**Stage 2: graceful draining.** While a commit is in flight, the engine answers 503 to all requests, including readiness probes. In our single-node test (4 x RTX 4090 48G, DeepSeek-V2-Lite, DP 2 to 4) the window lasted 37.2s on scale-up and 15.3s on scale-down; the raw evidence is recorded in #2812. The window affects the data plane of the deployment as a whole, not only the resized ranks. AIBrix holds the autoscaler, the gateway, and the controllers in one project, which makes the data-plane policy around this window definable end to end: hold with timeout, bounded retry, or route around; and how probes should be interpreted while the engine reports scaling. The goal is that a width change should not become a user-visible incident.

**Engine contract assumptions (interim).** Until the upstream contract settles, the platform path assumes: (a) a committed membership read becomes available and authoritative (today only the scaling flag has an HTTP surface); (b) a scaling-in-flight flag is available (Stage 0 uses it); (c) scale requests are target-shaped and their outcome becomes verifiable; (d) during a commit, the 503 window is expected behavior rather than an error. These assumptions track vllm/vllm#42515 and vllm/vllm#43202; if the final contract differs, the platform-side semantics below stay the same.

**Activation gates.** Stage 1 requires assumptions (a) and (c): until an authoritative committed-width read and a verifiable outcome exist, the autoscaler stays observe-only. Stage 2 relies on (b), which the engine already exposes.

**Failure rules (draft; the core of this RFC).** These rules govern autoscaler-initiated width moves. Engine-side fault-tolerance flows (for example, retiring failed ranks) are separate: while one is in flight, the engine reports scaling and the act path holds. Rather than discover them in production, we propose to write them down:

| ID | Condition | Detection | Proposed behavior |
|---|---|---|---|
| F1 | Observed capacity drops (rank loss / partial failure) | committed width below the last known-good width, engine not scaling | Never shrink around the failure; hold and surface a condition |
| F2 | Commit timeout / unknown outcome | call returned, state not verifiable | Block further operations; re-read until state is explicit |
| F3 | Interrupted / canceled commit | engine reports unsafe or inconsistent state | No automatic retry; require an explicit re-sync before acting |
| F4 | Probe failures during scaling | readiness fails while engine reports scaling | Do not count as unready; do not trigger a rollback; treat routable availability as membership-based during the window; pod readiness is not the routing signal while scaling |
| F5 | Controller restart mid-operation | restarted process finds in-flight or unknown engine state | Re-observe before acting; treat unknown as blocking until resolved |
| F6 | Contention: width vs replicas | both targets achievable in one pass | Apply the decision-order rule below; never both in one step |
| F7 | External width drift | committed width diverges from the committed target of the operation, or changes without a controller-initiated operation | During a commit, treat the outcome as unverifiable and block (UnknownOutcome); while idle, re-derive from the observed width and record the drift |

Re-attempt policy: once a blocking outcome resolves, the next action is a fresh decision from re-read state; a failed command is never automatically resumed.

**Interface sketch (illustrative; names not final).** To make the act side reviewable, here is the shape we intend, extending what #2812 already adds on the observe path:

- **Opt-in.** A mode switch, declared on the engine workload or on the PodAutoscaler (placement is Open Question 1; the sketch uses `elastic-ep-mode: observe | act` as a placeholder, default observe). Width bounds (a floor and a ceiling per footprint) would be declared with it.
- **Status.** Extend `status.elasticEPScaling` (today: `inProgress`, `observedEngines`, `scalingEngines`, `lastTransitionTime`) with: the committed width and its observation time, once the upstream read exists; an act phase (`idle`, `requesting`, `committing`, `verifying`, `blocked`); and a last-operation record (action, from, to, started, result).
- **Conditions.** One condition type with reasons rather than a growing set of types: `ElasticEPReady=False` with reason `DegradedMembership` (F1), `UnknownOutcome` (F2, F5, and the commit branch of F7), or `ResyncRequired` (F3). F4 and F6 are interpretation and ordering rules and do not raise conditions. Normal in-flight scaling is reflected in the phase, not as a failure condition.
- **Metrics.** Transaction attempts, outcomes, and commit latency.
- **Discipline.** The controller never rewrites the workload or the PodAutoscaler spec to represent width. Engine state is the source of truth; status only mirrors it.

**Decision framework (proposal: width x replicas).** There are two degrees of freedom: the committed EP width inside a footprint (the worker slots one replica group reserves), and the number of replicas. This RFC does not fix the policy. It proposes a conservative default that keeps the two levers separate and the envelope safe.

*Trigger semantics.* The act path reuses the signals that already drive the PodAutoscaler today (the existing metric windows, fluctuation tolerance, and `spec.metricsSources`); no new metric source is introduced. What changes is the mapping: the recommended capacity is resolved onto a width move or a replica move. The controller considers a move only when (a) the failure rules report no blocking state, (b) no engine reports scaling in progress, (c) the candidate size is one the engine can commit, and (d) the settle window has elapsed since the last commit. Otherwise it holds and records why.

*Decision order (fine lever first).* Each replica count defines a capacity band: from replica count times the width floor to replica count times the width ceiling. A width move resizes the deployment inside its current band; a replica move changes the band. Proposed default:

1. Resolve the recommended capacity to a target within the allowed replica bounds and width bounds; a recommendation outside the envelope is clamped to the nearest bound and the clamp is recorded in status.
2. If the current band can cover the target, move width toward it: one bounded transaction per decision, targeting the computed size within the band.
3. Otherwise add or remove replicas so that a band covers the target, then adjust width in a later step. Never both levers in one step; one transaction and one settle window at a time.
4. When in doubt (unknown engine state, conflicting reads, a recent failed commit), hold.

Widening before adding replicas uses headroom the footprint already reserves, and narrowing before removing replicas keeps reversals cheap. Whether scale-down should instead reclaim a footprint earlier for cost is an open question. The metric-to-capacity mapping, the width step shape, and the settle window value are also open (see Open Questions).

**Scope and non-goals.** Scope: platform-side orchestration for a single model deployment. Non-goals: engine-internal changes (we track and will contribute to the vLLM work); defining the upstream contract; fault recovery beyond safe-hold (retirement/FT is a separate effort); multi-node topology and NVLink locality; and choosing between equivalent stack shapes (for example 1xEP32 vs 2xEP16) as a planner problem.

### Relationship to Existing PodAutoscaler Mechanisms

The act path resolves the same chain the PodAutoscaler already runs: metrics to a recommended capacity, and a recommended capacity to target replicas. Three mechanisms on that chain have landed or are in flight, and this proposal is written to compose with them.

1. **Scheduled replica bounds (#2529, merged).** Effective replica bounds can now vary with daily time windows. In this proposal, bounds remain the outer envelope for replica decisions: a width move happens only inside a footprint whose replica count is legal under the bounds in effect, and when the bounds change, both width and replica targets are re-resolved on the next reconcile. The width floor and ceiling stay per footprint; we do not add a second bounds vocabulary.
2. **Pending replica guard (#2671, merged).** The guard dampens pod and resource metric recommendations while selected pods are not ready. A commit window produces that same signal by design, since the engine answers 503 to readiness probes while it resizes; the two mechanisms then read one signal differently. F4 says readiness is not a routing or rollback signal during the window, while the guard applies a conservative filter. Because the act path holds decisions during a commit, the visible risk is the handoff after the window: how long the guard dampening persists, and how it composes with the settle window. Proposed: the guard keeps its behavior, the act path defines the handoff, and whether the guard should be made scaling-aware (and whether its cooldown and the settle window should be unified) is an open question.
3. **Predictive projection (#2804, open).** The projection is recorded in `status.predictive` today and intentionally does not change decisions; the piece that turns it into a decision follows separately. When it lands, its recommendation is replica-shaped. With act mode enabled, the resolver would map a recommendation to a width move first when the band can cover it, and to a replica move otherwise. Whether previews should move from replica space to capacity space is future work.

The proposal also follows the working discipline on state used in this repository: one source of truth per value, and one writer per field. Width reads come from the engine; status only mirrors them; and the controller is the single writer for width while act mode is on (F7).

### Alternatives Considered

1. **Whole-replica scaling only (status quo).** Coarse and expensive; it is the problem #2288 asks to fix.
2. **A new CRD / engine-group resource (Dynamo-style, see ai-dynamo/dynamo#13121).** More expressive, but it introduces a parallel vocabulary and duplicates the autoscaler; the heavy paths are also gated off pending the same upstream work. We prefer to reuse the KPA/APA semantics users already know.
3. **An out-of-tree operator driving the engine directly.** Duplicates decision logic outside the autoscaler, loses familiar autoscaling semantics, and fragments ownership of the status users already watch.
4. **Delegate to an external scaler (KEDA-style live resize; llm-d is exploring this in llm-d/llm-d-autoscaling#1568).** Changing the trigger source does not remove the hard parts: membership semantics and failure rules still need a home. We would rather define them where the autoscaler already lives.

### Open Questions (feedback requested)

1. Act-mode scope: enable per-deployment (annotation/spec on the engine workload) or per-autoscaler? Is default-off the right call?
2. Which read is the authoritative "committed membership" signal, and how often should it be re-read?
3. Width vs replicas ordering: is the fine-lever-first ladder (move width inside the current band before changing the replica count, never both in one step) the right default, and should scale-down follow the same order?
4. Where should the 503-window data-plane policy live: gateway configuration or the autoscaler? Both are in this repo, and we want the maintainers' preferred split.
5. Would a dry-run mode (report the decision it would make without acting) be useful for rollout?
6. Step shape: should a width move target the computed size directly within its band, or be capped per transaction (for example, at double)?
7. Should the width floor double as the minimum serving width, or is a distinct minimum-serving threshold needed (for example, while a footprint is degraded)?
8. External width changes: should the controller only surface drift (fail closed), or also attempt to take back ownership on the next decision?
9. Composition: when scheduled replica bounds and width bounds disagree at a point in time, which should take precedence, and should the resolver prefer holding width or holding replicas?
10. Composition: should the pending-replica guard cooldown and the settle window in this proposal be one mechanism or two, and which should gate replica moves during and right after a commit?
11. Composition: should predictive previews move from replica space to capacity space (width-aware), or stay replica-shaped with the resolver translating?

### Expected Behavior (examples)

- **Traffic ramp**: width 8 to 16 with no replica change; during the commit, traffic is held or routed per the Stage 2 policy; the new width is verified from the engine after the commit; status records the transaction.
- **Ramp beyond one band**: widths reach each footprint ceiling and demand still rises; one replica is added in its own transaction (the new footprint starts at its base width), and widths are rebalanced in a later step.
- **Rank failure**: observed width drops below expected; the autoscaler holds, sets a condition, and does not shrink around the failure.
- **Canceled commit**: subsequent reconciles block (condition set) until the engine state is explicitly re-synchronized; the incident is visible in status and metrics.

### Verification and Acceptance

This section states how the act-side behavior above will be verified. Stage 0 is covered by #2812 and its test suite; this section covers Stages 1 and 2. Each failure rule maps to an observable signal and a pass condition, and each behavior layer maps to the cheapest layer that can prove it.

**Test layers.**

1. **Unit tests (no cluster).** The decision function is kept pure: inputs are the recommendation, the bounds, the observed width, engine flags, and the failure-rule state; outputs are a hold, a width move, or a replica move, with a reason. Unit tests cover gate precedence, clamping, the one-lever rule, the settle window and hysteresis, and the F4 interpretation (a probe failure during a commit is not an unready signal).
2. **Controller tests with a fake engine (envtest).** Reuse the harness built for #2812: a fake engine exposes the scaling flag and, once assumption (a) holds, the committed width. Tests cover the transaction discipline (one bounded operation per attempt, re-read after each call, record the outcome), the timeout and cancel paths (F2, F3), a controller restart mid-operation (F5), and drift detection with a second writer (F7).
3. **Single-node end-to-end (real GPU).** Reuse the environment and scripts from the #2812 evidence run: real commits, commit latency, the committed-width readback, the 503 window and the Stage 2 routing behavior during it, and a ramp scenario that would oscillate without the settle window. The scenarios follow the examples in Expected Behavior. Multi-node and multi-footprint behavior is out of scope for the first acceptance pass.

**Acceptance criteria (draft).** The act path is acceptable when, for each rule, the observable signal behaves as stated:

| Rule | Observable | Pass condition |
|---|---|---|
| F1 | width below the last known-good width, engine not scaling | no shrink decision; condition set; the held decision recorded in status |
| F2 | call returned, state not verifiable | further operations blocked; state re-read until explicit; no retry loop |
| F3 | canceled or interrupted commit | no automatic retry; an explicit resync recorded before further action |
| F4 | probe failures during a commit | not counted as unready; no rollback; the routing decision unchanged during the window |
| F5 | controller restart mid-operation | no action before re-observe; unknown state blocks |
| F6 | both levers available in one pass | one move per transaction; the ordering decision recorded |
| F7 | committed width diverges from the operation target, or changes while idle | blocked or recorded per the rule; drift visible in status |

Beyond rule-level checks, the transaction discipline is accepted when no two width operations overlap, every operation records from, to, result, and timing in status, and a ramp test shows at most one move per settle window.

**Rollout path.** The mode stays off by default. The intended sequence is: dry-run (the controller reports the move it would make; see Open Questions), then act mode on a non-critical deployment, then wider use. Rollback is switching the mode off; the engine keeps its last committed width, so no state migration is required.

**Compatibility.** With the mode off, behavior is unchanged for existing users: no new decisions, no writes, and the added status fields remain empty. We will record this as verified in the implementation PR (for example, upgrade notes and a no-op test) rather than as a claim in this document.

**Success metrics (draft).** After act mode is enabled somewhere, we would report: commit latency and outcomes; replica moves avoided during ramp tests; the error budget consumed during commit windows; and blocked-state duration with reasons, so that stuck states are visible.

### Area

Orchestration (controllers, CRDs)


## 评论 (1)

### github-actions[bot] · 2026-09-27

<!-- aibrix-bot-guide -->
Thanks for contributing to AIBrix! Please review the [contribution guide](https://github.com/vllm-project/aibrix/blob/main/CONTRIBUTING.md) and make sure this issue contains enough context for maintainers to reproduce or evaluate it.

