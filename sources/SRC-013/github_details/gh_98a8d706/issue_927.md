# [Issue #927] Adopt vLLM's --shutdown-timeout for graceful Model Service upgrades

source: https://github.com/llm-d/llm-d/issues/927
state: open | updated: 2026-09-15T01:20:53Z
labels: official-guides, lifecycle/stale, triage-accepted

## 正文

## Description

As of vllm-project/vllm#34730, `vllm serve` now has a `--shutdown-timeout` parameter that will be included in the v0.18.0 release.

llm-d should adopt this parameter for vLLM Model Service instances to ensure graceful shutdowns during upgrades.

## Proposal

1. **Add `--shutdown-timeout` to vLLM Model Service configuration**
   - Set the timeout to an appropriately long interval to allow most requests to complete
   - Make this configurable via helm charts

2. **Update pod `terminationGracePeriodSeconds`**
   - Set this value greater than the `--shutdown-timeout` value
   - Ensures Kubernetes doesn't force-kill the pod before vLLM's graceful shutdown completes

## Benefits

- Minimizes user traffic disruption during Model Service upgrades
- Allows in-flight requests to complete gracefully
- Provides operators with predictable upgrade behavior

## Implementation Notes

The relevant helm charts are in https://github.com/llm-d-incubation/llm-d-modelservice

## References

- vLLM PR: https://github.com/vllm-project/vllm/pull/34730
- Available in: vLLM v0.18.0+

## 评论 (3)

### markmc · 2026-03-09

/cc @wseaton 

### markmc · 2026-05-20

The recommended approach for this is now documented in the vLLM K8s deployment guide (vllm-project/vllm#43208), based on the pattern implemented in KServe (kserve/kserve#5485, kserve/kserve#5496):

1. Add a `preStop` hook (`/bin/sleep 15`) to allow endpoint removal before SIGTERM
2. Set `--shutdown-timeout` to `terminationGracePeriodSeconds - 15` (default: 45s)
3. Raise `terminationGracePeriodSeconds` to 60s

llm-d should adopt the same pattern in its Model Service configuration.

### github-actions[bot] · 2026-09-15

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.
