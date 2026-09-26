# [Issue #2565] Consolidate keda-epp-saturation and keda-epp-queue guides into one

source: https://github.com/llm-d/llm-d/issues/2565
state: open | updated: 2026-09-24T17:52:07Z
labels: 

## 正文

## Problem

`guides/workload-autoscaling/keda-epp-queue` and `guides/workload-autoscaling/keda-epp-saturation`
are two near-identical KEDA + EPP autoscaling guides — the only real difference is which
EPP signal the `ScaledObject` polls (`llm_d_epp_flow_control_queue_size` vs
`llm_d_epp_flow_control_pool_saturation`). Maintaining two full guide trees (manifests,
READMEs, `guide.yaml`, OCP overlays, nightly e2e workflows) for what is essentially one
trigger-query difference is duplicated effort and a drift risk (see the various
"keeps its own ScaledObject" comments in `guides/recipes/autoscaling/metrics-reader/`).

## Proposal

Consolidate the two guides into a single guide with the metric choice as a parameter/overlay,
rather than two parallel directory trees.

While doing this, cover two additional dimensions that today are undocumented/inconsistent
across the two guides:

1. **EPP flow control on vs. off** — both the queue-depth and pool-saturation signals come
   from the EPP flow-control subsystem; the consolidated guide should call out how behavior
   and recommended thresholds differ with flow control enabled vs. disabled.
2. **Long model-server startup time** — currently mitigated ad hoc (large stabilization
   window on the HPA/KEDA side). We should evaluate/document incorporating pending pods into
   the supply calculation in the `scalingModifiers` formula as an alternative (or complement)
   to a large stabilization window, and pick a recommended default.

## Tasks

- [ ] Consolidate `keda-epp-queue` and `keda-epp-saturation` into a single guide
      (parameterize the KEDA trigger metric/threshold instead of duplicating the tree);
      keep redirect stubs for the old paths per existing convention
      (see `guides/workload-autoscaling/README.hpa-epp.md`)
- [ ] Document the flow-control on/off dimension and its effect on thresholds/behavior
- [ ] Document and pick a default startup-time mitigation (stabilization window vs.
      pending-pod-aware `scalingModifiers` supply calculation)
- [ ] Update nightly e2e tests for the consolidated guide:
  - [ ] OCP
  - [ ] CKS
  - [ ] GKE
- [ ] Enable nightly benchmarking for the consolidated guide

## References

- `guides/workload-autoscaling/keda-epp-queue/`
- `guides/workload-autoscaling/keda-epp-saturation/`
- `guides/recipes/autoscaling/metrics-reader/` (shared recipe used by both guides)
- `docs/architecture/advanced/autoscaling/keda-epp.md`
- `.github/workflows/nightly-e2e-workload-autoscaling-keda-epp-ibm-acc-gpu-vllm-x.yaml` (only existing nightly; OCP-only, queue-based only)
- llm-d-autoscaling `docs/developer-guide/autoscaling-workflow.md`

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## 评论 (2)

### mamy-CS · 2026-09-23

## Consolidation target + Plan

One `guides/workload-autoscaling/keda-epp/` guide.
The trigger becomes a kustomize component axis (`trigger-queue`, `trigger-saturation`) composed against the platform overlays (`k8s`, `ocp`), yielding 4 leaf overlays the `deploy:` step selects (annotated, not gated - `when:` is render-only in `guide.py`).
One `guide.yaml`, default = queue; one rendered README documenting both triggers.
Redirect stubs left at `keda-epp-queue/` and `keda-epp-saturation/` per existing convention.

Builds on #2265 (shared OCP `metrics-reader` auth component), which already unified the OCP auth but explicitly deferred the generic-k8s TriggerAuth normalization - PR 1 picks that up.

## PRs

### PR 1 - Normalize the k8s TriggerAuth
Depends on: none
Resolve the #2265-deferred item: pick ONE k8s TriggerAuth pattern (CA-only vs bearer+CA) and align both guides to it, before the structural merge, so PR 2 stays a pure restructure.
Open question this PR must answer: does the bundled kube-prometheus-stack over HTTPS require a bearer token, or is CA-only sufficient? Determine empirically against a live stack and record the finding.

### PR 2 - Consolidate the two trees into `keda-epp/`
Depends on: PR 1
Trigger-agnostic `base/` + 2 trigger components + `k8s`/`ocp` platform overlays (normalized auth from PR 1 + the `metrics-reader` recipe) + 4 leaf overlays.
Single `guide.yaml` (queue default), rendered README documenting both triggers, redirect stubs at the old dirs, port the queue guide's `scale_event` verify. Saturation graduates out of `[Experimental]`.

### PR 3 - Document the flow-control on/off dimension
Depends on: PR 2
Both signals originate in the EPP flow-control subsystem; document how behavior and recommended thresholds differ with flow control enabled vs disabled, for each trigger.

### PR 4 - Startup-time mitigation default
Depends on: PR 2
Spike + decide: large scaleDown stabilization window vs pending-pod-aware `scalingModifiers` supply calc for slow model-server startup. Pick a default, encode it, document the tradeoff.
Lands before the nightly so the nightly tests the chosen default.

### PR 5 - Consolidated guide green on the OCP nightly
Depends on: PR 2, PR 4
Repoint the existing OCP nightly (`...keda-epp-ibm-acc-gpu-vllm-x`) at the consolidated guide.
Keep it on today's script-based harness; the guide.yaml-harness cutover stays the prior epic's blocked PR 5, deliberately not coupled here.

### PR 6 - CKS nightly lane
Depends on: PR 5
Add the CKS nightly lane for the consolidated guide.

### PR 7 - GKE nightly lane (net-new)
Depends on: PR 5
No autoscaling GKE nightly exists today; stand up a new lane. May surface a GKE-specific auth overlay gap.

### PR 8 - Enable nightly benchmarking
Depends on: PR 5
Enable nightly benchmarking for the consolidated guide once a functional nightly is green.

## Tasks

- [x] PR 1 - Normalize the k8s TriggerAuth https://github.com/llm-d/llm-d/pull/2571
- [x] PR 2 - Consolidate into `keda-epp/` https://github.com/llm-d/llm-d/pull/2577
- [ ] PR 3 - Document flow-control on/off
- [ ] PR 4 - Startup-time mitigation default
- [ ] PR 5 - OCP nightly
- [ ] PR 6 - CKS nightly
- [ ] PR 7 - GKE nightly (net-new)
- [ ] PR 8 - Nightly benchmarking

## Two things worth flagging

1. PR 1 carries a genuine open question - does the bundled kube-prometheus-stack over HTTPS need a bearer token, or is CA-only sufficient? - that the PR must answer before unifying.
2. The nightly PRs (5-8) deliberately ride the current script-based harness to avoid inheriting the prior epic's parser/harness block.


### mamy-CS · 2026-09-23

/assign @mamy-CS 
