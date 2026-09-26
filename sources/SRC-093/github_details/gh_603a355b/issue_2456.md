# [Issue #2456] [ModelClaim] Surface invalid pool policy configuration to operators

source: https://github.com/vllm-project/aibrix/issues/2456
state: closed | updated: 2026-09-04T02:28:38Z
labels: kind/enhancement, good first issue, help wanted, area/observation, area/orchestration

## 正文

### Feature Description and Motivation

The experimental ModelClaim pool policy is configured through the Deployment annotation `pool.aibrix.ai/policy`. Invalid JSON, unknown fields, unsupported modes, or invalid values currently disable policy execution safely, but the error is primarily visible in controller logs and can repeat on every reconciliation.

Operators need a Kubernetes-native indication that the policy is invalid without introducing a new CRD or adding fields to ModelClaim.

### Use Case

A platform administrator applies or edits a warm-pool Deployment annotation and expects KV policy behavior. A typo should be visible immediately through `kubectl describe deployment`, Events, and metrics rather than appearing as a silent lack of policy actions.

### Proposed Solution

When resolving a pool policy:

- emit a Warning Event on the owning Deployment when parsing or validation fails;
- deduplicate/rate-limit repeated Events for the same Deployment generation and error class;
- expose an additive low-cardinality policy-valid/config-error metric keyed by namespace and pool/Deployment;
- emit a Normal Event when a previously invalid policy becomes valid again;
- retain fail-closed behavior: invalid configuration must never apply a partial or speculative KV plan;
- retain strict unknown-field validation.

Use fixed error classes such as `invalid_json`, `unknown_field`, `invalid_capacity`, `invalid_floor`, and `unsupported_mode`. Keep the detailed parser message in the Event/log, not in metric labels.

Do not add a ModelPoolPolicy CRD, mutate Deployment status, or add ModelClaim spec fields.

### Acceptance Criteria

- `kubectl describe deployment <warm-pool>` clearly reports an invalid policy.
- Reconciliation does not flood Events or logs for an unchanged invalid annotation.
- A corrected annotation produces a recovery signal and policy execution resumes.
- Invalid policy remains fail-closed.
- Unit tests cover invalid, unchanged-invalid, corrected, and valid configurations.


## 评论 (5)

### FAUST-BENCHOU · 2026-07-17

/assign


### k-adm · 2026-07-17

I'd like to work on this

### FAUST-BENCHOU · 2026-07-18

/close

### SarnadAbhilash · 2026-09-04

I'll take this one. Plan: emit rate-limited Warning Events (and a recovery Normal Event) for invalid `pool.aibrix.ai/policy` annotations, plus a low-cardinality policy-valid/config-error metric, without adding CRD/status fields. Fail-closed behavior stays as-is. I'll open a focused PR with unit tests.

### SarnadAbhilash · 2026-09-04

Quick follow-up: after looking at `main`, this appears to already be covered by #2462 (`pool_policy` Events + `aibrix_modelclaim_pool_policy_valid` metric, with the fail-closed / recovery behavior from the issue). I'll step back so maintainers can close this if that matches. Sorry for the noise on the claim earlier.
