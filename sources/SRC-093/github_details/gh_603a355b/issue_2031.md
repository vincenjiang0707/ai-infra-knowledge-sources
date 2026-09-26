# [Issue #2031] Few blockers to extend service discovery to other methods

source: https://github.com/vllm-project/aibrix/issues/2031
state: open | updated: 2026-09-24T00:58:31Z
labels: 

## 正文

### 🚀 Feature Description and Motivation

We add some static way to discover the worker pods in router here https://github.com/vllm-project/aibrix/pull/1873. 

While, there're still some issues we have not fully resolved yet.

- `*v1.Pod` as the universal internal representation forces every non-K8s provider to synthesize fake K8s objects
- Routing logic is coupled to K8s labels (`pod.Labels["role-name"]`) instead of semantic concepts
- Naming is inconsistent — FileProvider = mechanism, KubernetesProvider = platform, EtcdProvider =  backend (etcd is not added yet)
- Static config format leaks K8s internals to users instead of using intuitive domain concepts like
  prefill_servers/decode_servers



### Use Case

To better serve other service discovery methods

### Proposed Solution

_No response_

## 评论 (3)

### Jeffwan · 2026-03-20

- v1.Pod coupling: Proposes a platform-agnostic Endpoint type (ID, Address, Port, Model, Labels, Ready) that replaces *v1.Pod as the internal currency. No more synthesizing fake K8s objects
- Label coupling in routing: Standardizes label keys (role, roleset, engine, group) that are domain concepts. Each provider maps its native metadata into these labels. EndpointList.ListByLabel("role", "prefill") replaces pod.Labels["role-name"]
- Naming: FileProvider → StaticProvider (behavior), alongside KubernetesProvider, ConsulProvider,
  EtcdProvider (backend). Consistent naming by what the provider is, not how it reads data.
- Static config — TRT-LLM style with workers/prefill_workers/decode_workers: The provider internally maps these to Endpoint{Labels: {"role": "prefill"}}. Users never see internal labels. 
```
  models:
    - name: "Qwen/Qwen2.5-72B"
      prefill_workers: ["host1:8001", "host2:8002"]
      decode_workers: ["host3:8003"]
```

### Jeffwan · 2026-03-20

Let's handle the naming consistent and static config first. rest two needs lots of changes, need some alignment first.

### bolubo · 2026-09-24

Hi @Jeffwan. This has been open for a while, so I spent some time reading the discovery, cache, and gateway code to see where things actually stand. I want to take the remaining pieces here together with #2033, and before I start I have three things I want to get your call on. Suggested order: static config first, then label semantics, then the Endpoint type. etcd/consul after that.

Quick note on etcd: #2692 has been idle for about two weeks and now conflicts with main. I asked the author if they are still on it ([link](https://github.com/vllm-project/aibrix/pull/2692#issuecomment-5805407089)). If it is stalled, I can pick up etcd once the Endpoint abstraction lands, and it should be a much smaller change by then.

**1. Static config.** Today the surface is `models[].endpoints` and `models[].rolesets[].prefill/decode` (`pkg/cache/discovery/static.go:37-64`). I want to add your `workers` / `prefill_workers` / `decode_workers` form on top, keep the old keys readable so existing configs keep working, and do the mapping to internal role labels inside the provider. Users never see those labels, as you said. One thing your example does not cover: the roleset layer. My default would be that `prefill_workers`/`decode_workers` mean a single default roleset, and multi-roleset setups keep using the `rolesets` form, since the roleset name is the PD pairing key today (`pkg/plugins/gateway/algorithms/pd_roleset.go:34`). Does that work, or do you want roleset names in the new surface too?

**2. Label semantics.** One thing I noticed: role, roleset, and replica index are read from two places today. Routing reads labels `role-name`, `roleset-name`, `pod-group-index`, `role-replica-index` (`pkg/plugins/gateway/algorithms/pd_disaggregation.go:51-56`), while parts of the metrics path read the same values from pod env vars `ROLE_NAME`, `ROLESET_NAME`, `ROLE_REPLICA_INDEX` (`pkg/cache/utils.go:71-73`, `pkg/metrics/custom_metrics.go:510-512`). The two can disagree. Plan: standard keys (`role`, `roleset`, `engine`, `group`); the K8s provider maps the old labels into them, reading both during the transition, and does not write back to pods so controllers stay the only writers; env fallbacks fold into the same path. Then `EndpointList.ListByLabel('role', 'prefill')` replaces direct label access. Question: for `group`, do you mean the TP pod group, where only index 0 serves HTTP, or the replica index used for dedup? We have both today. Also let me know if you would handle the env part differently.

**3. Endpoint type.** Your six fields cover most of what routing reads. Three details from the code: (a) a pod can expose multiple ports. `GetPortsForPod` expands base port + `data-parallel-size` ranks, and ModelClaim pods get a per-model port (`pkg/utils/util.go:216`, `pkg/utils/pod.go:464`), so I would keep port resolution in the provider and have Endpoint carry the resolved routing port, unless you want `Port` as a list. (b) Ready comes from four inputs today (PodIP set, not terminating, not draining, Ready condition) in `FilterReadyPod` (`pkg/utils/pod.go:201`), so it works better as a provider-computed state than a raw pod condition. (c) ID probably needs both name and namespace, since they form the `namespace/name` key used across cache lookups and routing stats.

For rollout I would split it in two steps. L1: providers emit Endpoint at the discovery boundary and the gateway data plane consumes it, with cache internals still on `*v1.Pod` behind an adapter. L2: swap the internal currency inside cache (metrics, kv events, ModelClaim), which is where most of the v1.Pod references live. L1 does not touch the controllers. Fine to start with L1?
