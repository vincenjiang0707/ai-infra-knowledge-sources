# [Issue #499] Avoid Prefill/Decode version/configuration mismatch

source: https://github.com/llm-d/llm-d/issues/499
state: open | updated: 2026-09-11T11:02:36Z
labels: 

## 正文

### Summary

The Endpoint Picker (EPP) will pair Prefill and Decode instances with mismatched vLLM versions or configurations during rolling updates, potentially causing crashes or other undefined behavior due to KV cache format incompatibilities, KV transfer metadata mismatches, and other version-specific issues. Further investigation is needed to understand all problematic scenarios.

### Background

In the P/D well-lit path, an `InferencePool` object defines which pods are eligible for selection via label selectors. The EPP then independently selects a pair of Decode and Prefill workers from the pool based on:
- Pod labels (`llm-d.ai/role: prefill` or `decode`)
- Load metrics
- Prefix cache hit probability

However, Prefill and Decode instances are deployed as separate Kubernetes Deployments , each with their own image and configuration specifications.

### Problem

The EPP selection logic does not verify that paired Prefill/Decode instances have matching:
- vLLM version/image digest
- Attention backend configuration (FlashAttention, etc.)
- KV cache configuration
- Other runtime parameters

This creates two high-risk scenarios:

**1. Version Upgrades**: When performing a rolling update of the vLLM image on Decode pods while Prefill pods remain on an older version (or vice versa), the EPP will pair instances with mismatched versions.

**2. Configuration Changes**: Similarly, changing configuration parameters (e.g., `--attention-backend`) on one role but not the other can create incompatible pairings.

### Suggested Approach

The EPP should only consider P/D pairs with matching version and configuration. Possible implementations:

1. **Version Label Matching**: Add a version/configuration hash label (e.g., `llm-d.ai/config-version`) to both Prefill and Decode pods. The EPP filters to only consider pairs with matching values.
2. **InferencePool per Configuration**: For each rollout, create a new InferencePool with unique label selectors (e.g., `llm-d.ai/config-hash: abc123`) that match both the new Prefill and Decode deployments. 
3. **Pod Annotation Verification**: The routing sidecar or EPP could verify compatibility by comparing pod annotations containing version/config metadata before forwarding requests.

Whichever approach is taken, the rollout of Prefill and Decode needs to be coordinated such that the new:old ratio of both matches - e.g. given 4 Prefill workers and 1 Decode workers, there would be no point in upgrading D from new to old before starting to upgrade P, and vice-versa.

At a vLLM level, all we will be able to do is identify such mismatches and reject such requests. Potentially this could form part of the solution - e.g. if the EPP was aware of the failure and rejected that P/D pair when scheduling a retry?

(_Raised by @tlrmchlsmth - I'm trying to capture the issue at a high-level._)






## 评论 (8)

### wseaton · 2025-11-25

Thanks @markmc for describing the issue, I think the requirements are well captured here, just a few thoughts:

> Whichever approach is taken, the rollout of Prefill and Decode needs to be coordinated such that the new:old ratio of both matches - e.g. given 4 Prefill workers and 1 Decode workers, there would be no point in upgrading D from new to old before starting to upgrade P, and vice-versa.

This external coordination requirement leads me to believe that we need some type of outer automation that has custom "stepwise" rollout logic, so some type of `PDDeployment` as an operand that a controller works on. I think this can be thought of a completely seperate concern to the routing logic for compatibility. We could then divide the work into two streams along these lines

Imagine in a situation where you had 2x 1P1D deployments. In order to minimize downtime, you might want a rollout strategy that ensures that there is always an available routable pair while doing your version upgrade or config change. The controller would not need to know anything other than pod readiness to make that determination, I would expect the EPP or routing sidecar to keep track of what backends are "available" and schedule to the proper backend.

> Potentially this could form part of the solution - e.g. if the EPP was aware of the failure and rejected that P/D pair when scheduling a retry?

Yes exactly, agree that the EPP could potentially be involved in retry policy and this seems like a nice UX benefit (like potentially allowing the ability to set very high scheduling priority on retry, or to correct the deadline to account for elapsed time relative to the existing SLO, etc.).

> The EPP should only consider P/D pairs with matching version and configuration. Possible implementations:

I am worried there is so much existing runtime dynamic config in vllm, it might be worth considering the route of using an endpoint or sidechannel that the EPP or routing sidecar could use to do introspection on the config like a hash, instead of relying on the external deployment manifest.

### tlrmchlsmth · 2025-11-25

@markmc I think you've covered the problem quite well.

One thing I want to call out is that there is a case for being _permissive_ with changes in configuration. For instance, people see performance benefits from using P/D disagg with heterogeneous hardwar (e.g. NVIDIA GPUs for prefill and Intel Gaudi GPUs for decode) Or using heterogeneous quantization (for the weights rather than the KV caches).

So whatever approach we take, we may want to leave the door open for select differences between the vLLM configs 

### github-actions[bot] · 2026-02-26

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.

### hexfusion · 2026-03-12

I hit this with disaggregated P/D across mixed GPU architectures (sm_75 + sm_86). vLLM auto-selects different attention backends per architecture (FlashInfer vs FA2), producing incompatible KV cache layouts. NIXL handshake fails. My workaround was to force --attention-backend FLASHINFER on both pods.

With vllm-project/vllm#29503 adding config-hash checking to the NIXL handshake, is this issue considered addressed or is there still work planned at the EPP/scheduling layer?

### robertgshaw2-redhat · 2026-04-13

> I hit this with disaggregated P/D across mixed GPU architectures (sm_75 + sm_86). vLLM auto-selects different attention backends per architecture (FlashInfer vs FA2), producing incompatible KV cache layouts. NIXL handshake fails. My workaround was to force --attention-backend FLASHINFER on both pods.
> 
> With [vllm-project/vllm#29503](https://github.com/vllm-project/vllm/pull/29503) adding config-hash checking to the NIXL handshake, is this issue considered addressed or is there still work planned at the EPP/scheduling layer?

its not addressed. we need a clear way to ensure EPP doesnt do this type of scheduling.

### github-actions[bot] · 2026-07-13

This issue is marked as stale after 90d of inactivity. After an additional 30d of inactivity (15d to become rotten, then 15d more), it will be closed. To prevent this issue from being closed, add a comment or remove the `lifecycle/stale` label.

### dagrayvid · 2026-08-10

The DisaggregatedSet Rollout Screener which has been merged to llm-d-router is relevant to this issue:
https://github.com/llm-d/llm-d-router/tree/main/pkg/epp/framework/plugins/requestcontrol/screener/disaggregatedsetrollout


### markmc · 2026-09-11

As described in detail in https://github.com/llm-d/llm-d-router/pull/2463#issuecomment-5602402634 it looks like `DisaggregatedSet` with the rollout screener is a comprehensive solution to this issue?

I think we should drop the llm-d/llm-d-router#463 compatibility has screener approach - the NIXL compatibility hash in vLLM is an internal safety net, to catch the most obvious ways that a pair of instances are incompatible, as @hasB4K says:

> An older vLLM version may corrupt KV state because of a bug. Its NIXL hash could remain compatible with the patched version, but we still do not want KV state crossing between those revisions.
