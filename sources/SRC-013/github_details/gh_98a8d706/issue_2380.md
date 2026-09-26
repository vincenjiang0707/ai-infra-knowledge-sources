# [Issue #2380] RFC: Fleet-level multi-cluster inference orchestration for llm-d

source: https://github.com/llm-d/llm-d/issues/2380
state: open | updated: 2026-09-09T23:22:44Z
labels: 

## 正文

# RFC: Fleet-level multi-cluster inference orchestration for llm-d

## Problem

llm-d provides routing and inference optimization within a Kubernetes
deployment. Operators running independent llm-d deployments across regions,
failure domains, or hardware pools still need a fleet-level mechanism to:

- discover cluster capabilities and health;
- place a requested physical model on compatible hardware;
- select a healthy cluster before handing the request to that cluster's
  llm-d routing path;
- fail over without silently changing the requested model or capability; and
- expose fleet-wide status, policy decisions, and routing evidence.

This is not intended to replace the llm-d Router or its Endpoint Picker. The
fleet layer selects a cluster and compatible physical model; the selected
cluster's llm-d components retain ownership of endpoint selection and
within-cluster inference optimization.

## Alignment with Router v0.10 multi-cluster plugins

llm-d Router v0.10 introduced an Alpha multi-cluster plugin family for a
cluster-scoped EPP. It can discover peer cluster gateways from a watched file,
scrape their aggregate queue and KV-cache metrics over verified HTTPS, and
select a cluster using queue depth, KV-cache utilization, approximate prefix
affinity, and session affinity. This is a strong candidate for the fleet data
plane and makes the responsibility boundary more concrete.

We do not propose a competing cluster scorer. Instead, llm-d Fleet could
reconcile its dynamic cluster, provider, model, health, and draining state into
the Router's cluster-endpoint input. Router would score eligible clusters and
retain ownership of queue/KV/prefix/session routing intelligence. The fleet
layer would retain the production semantics that the Alpha plugin family does
not currently define:

- authenticated cluster registration and dynamic endpoint reconciliation;
- model and accelerator capability filtering before scoring;
- exact logical-to-physical model resolution with no silent downgrade;
- active health probing, freshness, hysteresis, and bounded removal/restore;
- failure-domain-aware `healthy`, `degraded/non-HA`, `draining`, and
  `unavailable` status;
- tenant admission and policy enforcement; and
- structured no-compatible-capacity behavior and auditable routing metadata.

This suggests a layered integration: llm-d Fleet produces the eligible cluster
set and policy constraints; the cluster-scoped EPP selects among those eligible
destinations; each selected cluster's local llm-d Router selects the serving
endpoint. The initial integration can use the plugin's watched endpoint file,
while a future API may replace that adapter if SIG Router prefers a native
discovery contract.

## Experience report

We implemented this boundary in the Apache-2.0
[llm-d Fleet](https://github.com/jkershawrh/llm-d-fleet) project and tested it
on three physical OpenShift clusters:

- two CPU inference providers in separate clusters;
- one H100 GPU provider, explicitly reported as degraded/non-HA because no
  second compatible GPU provider exists; and
- a redundant fleet inference entry point and routing data plane.

The current implementation has exercised OpenAI-compatible chat and completion
requests, CPU distribution, exact GPU placement, session escalation from a
CPU model to a GPU model, caller routing-header spoof attempts, and provider
loss. When the sole compatible GPU provider is unavailable, the gateway
returns an explicit `503 no_compatible_capacity` rather than silently
downgrading the request.

The session-escalation path uses llm-d-sc as one optional semantic
classification signal. This demonstrates that workload classification can
inform fleet placement without making the classifier authoritative: the fleet
layer still enforces model compatibility, policy, health, and capacity. The
proposed fleet interface does not require llm-d-sc and can accept equivalent
signals from other classifiers or explicit application policy.

Longer historical runs have exercised the broader control plane, but they used
earlier topology and transport revisions. The initial upstream claim is
therefore limited to the behaviors above; current-release certification data
will be published separately as it completes.

## Proposed outcome

Define a supported, composable fleet boundary for multiple llm-d installations:

1. A fleet capability and health model that distinguishes healthy,
   degraded/non-HA, draining, and unavailable providers.
2. Exact-model placement and cluster selection before within-cluster routing.
3. Health-aware failover with bounded convergence and no retry after a streamed
   response begins.
4. An OpenAI-compatible entry point that preserves streaming and backend error
   semantics while preventing callers from selecting internal clusters.
5. Conformance tests for exact-model routing, cluster loss, spoofed routing
   metadata, and no-compatible-capacity behavior.
6. An optional, implementation-neutral classification input that can influence
   placement or session escalation without bypassing policy and compatibility
   checks.

## Questions for SIG Router

1. Is generating the watched cluster-endpoint file an appropriate first
   integration with the v0.10 multi-cluster plugins, or should fleet state use
   a different discovery API?
2. Should model/capability/health filtering happen before the cluster-scoped
   EPP, or become additional EPP filter plugins?
3. Which Gateway API or Inference Extension resources should represent the
   handoff between fleet admission, cluster selection, and cluster-local
   routing?
4. Should the fleet control plane be developed in `llm-d-router`, in
   `llm-d-incubation`, or as a Well-Lit Path composing multiple routers?
5. Which minimum APIs and conformance behaviors would maintainers want before
   considering implementation, and which SIGs should co-review them?

## Non-goals for the initial contribution

- Replacing cluster-local EPP scoring, flow control, autoscaling, or KV-cache
  optimization.
- Standardizing a particular cross-cluster network product.
- Operating Kubernetes clusters, databases, certificate authorities, or model
  servers.
- Requiring the governance and immutable-evidence integrations used by the
  reference implementation.
- Requiring llm-d-sc or standardizing semantic classification behavior as part
  of the initial fleet API.
- Claiming high availability for a model with only one compatible provider.

## 评论 (3)

### jkershawrh · 2026-08-27

## Implementation update — 2026-08-27

The proposal now has a topology-neutral Apache-2.0 reference implementation in [llm-d Fleet](https://github.com/jkershawrh/llm-d-fleet). The public repository excludes environment-specific overlays and optional governed-observability dependencies from its default installation.

The implementation boundary has also been narrowed to align with existing owners:

- **llm-d Fleet** owns cluster registration, capability inventory, exact-model resolution, tenant admission, placement constraints, health/freshness/draining state, failure-domain classification, and reconciliation of the eligible provider set.
- **llm-d Router/EPP** retains cluster/endpoint scoring, including queue, KV-cache, prefix, and session intelligence.
- **KServe** retains cluster-local model workload lifecycle when selected as the serving target.
- **KEDA/HPA** retains pod autoscaling; WVA is treated as an optional heterogeneous-variant optimizer rather than a replacement autoscaler.
- Cross-cluster transport is represented by a portable endpoint/TLS/authentication contract. OpenShift Routes are one validated deployment choice, not a required fleet API.

### Routing-provider adapters

The control plane now has a single-authoritative-provider adapter boundary:

- `praxis` remains the validated reference data plane and backward-compatible default.
- `llm-d-router` is the upstream-native beta adapter and produces deterministic watched endpoint state for the Router multi-cluster plugin family.
- `disabled` supports control-plane-only operation.

Both adapters receive the same fleet-qualified provider set. Adapters may translate that set, but cannot add incompatible providers or change fleet policy. Exact physical-model filtering occurs before EPP scoring, and loss of the sole compatible provider produces `503 no_compatible_capacity` rather than model substitution.

### Current evidence and limitations

The published qualification snapshot records:

- 306/306 CPU smoke requests over 15 minutes, distributed evenly across two independent CPU providers, with no pod restarts.
- 29/29 exact-model GPU requests routed to the sole compatible GPU provider, with no substitution.
- A bounded CPU staircase where concurrency 2 at 1.627 RPS was the highest clean level for that measured topology/workload; concurrency 4 reached the configured 70% resource guardrail and concurrency 8 was intentionally not attempted.

These are topology-specific engineering results, not universal capacity claims. The single-provider GPU model remains explicitly `degraded/non-HA`. Intermittent transport disconnects observed during the staircase still require attribution, and comparable one-hour failure certification plus extended Router durability qualification remain open.

References:

- [White paper](https://github.com/jkershawrh/llm-d-fleet/blob/main/docs/whitepaper.md)
- [Architecture](https://github.com/jkershawrh/llm-d-fleet/blob/main/docs/architecture.md)
- [Responsibility boundary](https://github.com/jkershawrh/llm-d-fleet/blob/main/docs/responsibility-boundary.md)
- [Routing adapters](https://github.com/jkershawrh/llm-d-fleet/blob/main/docs/routing-adapters.md)
- [Qualification report](https://github.com/jkershawrh/llm-d-fleet/blob/main/docs/qualification-report.md)

This is independent community work and is not presented as accepted or endorsed by llm-d. A preview tag will follow separately after release notes and remaining packaging checks.

For initial upstream discussion, I would like to keep the contribution surface small: provider discovery, exact-model eligibility, health/freshness/draining semantics, and conformance behavior. Governance, immutable evidence, external observability systems, and semantic classification remain optional integrations outside the initial acceptance criteria.

Feedback from SIG Router would be especially useful on whether watched-file generation is the right first adapter and what a future native cluster-discovery contract should minimally contain.


### hexfusion · 2026-09-09

/assign

### hexfusion · 2026-09-09

hi @jkershawrh thank you for the proposal I am going to reach out directly so we can talk about your goals and requirements.
