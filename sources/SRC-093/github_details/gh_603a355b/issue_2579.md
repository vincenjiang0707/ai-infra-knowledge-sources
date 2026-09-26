# [Issue #2579] [Feature] Model Scaling and Request Routing for Multi-LoRA Serving

source: https://github.com/vllm-project/aibrix/issues/2579
state: open | updated: 2026-09-24T08:48:13Z
labels: area/lora

## 正文

### 🚀 Feature Description and Motivation

I would like to propose support for model scaling and request routing for Multi-LoRA serving in AIBrix.

This feature would enable AIBrix to scale LoRA adapters at runtime and route requests more effectively, improving flexibility and making LoRA serving more practical and efficient.

### Use Case

This feature would make AIBrix more capable in Multi-LoRA serving scenarios where many LoRA adapters need to be served efficiently on shared infrastructure.

### Proposed Solution

## Task Breakdown

1. Add a Multi-LoRA serving example to the documentation and profile Multi-LoRA serving performance in AIBrix.

   - Measure performance tradeoffs, especially TTFT and TPOT latency degradation in Multi-LoRA serving scenarios.

2. Design and implement adapter placement/scaling and LoRA-aware request routing.

   - Currently, `ModelAdapter.spec.replicas` behaves as follows:
     - If `replicas = 1`, AIBrix skips scoring/routing and routes directly.
     - If `replicas` is omitted, the AIBrix gateway load-balances requests among pods.

   - To better support Multi-LoRA serving, I propose introducing two mechanisms:
     - **Adapter placement policies**: control where adapters are loaded based on base-model identity, `max_lora_rank`, `max_loras`, `max_cpu_loras`, and related constraints. Autoscale LoRA adapters when necessary.
     - **LoRA-aware request routing**: make routing decisions based on adapter state and pod load. Routing should prefer pods based on whether the requested adapter is already loaded on GPU and ready, the number of active requests, available capacity, memory pressure, and other relevant signals.

## 评论 (1)

### bolubo · 2026-09-24

The routing part of this task may not need to start from scratch: #1181 (opened 2025, idle since 2025-08) adds a `lora-affinity` routing strategy. I went through it against current main, in case it helps:

- As far as I can tell, all it needs to compile is one accessor rename: `GetLabelValue()` became `GetLabelValues()`, so each call site now reads `GetLabelValues()["value"]` (`pkg/metrics/types.go:277`). Everything else it relies on is unchanged: `Register`/`RouterConstructor`, `PodList.All()`, `cache.GetMetricValueByPod()`, and `SetTargetPod()`/`TargetAddress()`.
- The engine signals it reads are still collected: `max_lora`, `running_lora_adapters`, and `waiting_lora_adapters` are in the cache label-query list (`pkg/cache/cache_metrics.go:122`).
- Adapter awareness landed recently: the cache now maps an adapter to its base model (`cache.ModelBaseModel`, `pkg/cache/cache_api.go:83`), and the routing context keeps the two names apart (`BaseModel`, set at `pkg/plugins/gateway/gateway_req_body.go:86`, read back by `MetricLoraAdapter()`). None of that existed in 2025; it came in with #2623.

On the design side, the point the 2025 review left open still stands: an adapter in `waiting_lora_adapters` is not necessarily loaded yet, so it is a weaker affinity signal than one in `running_lora_adapters`. A tier order of running, then waiting, then free capacity would settle that, replace the 0.999 affinity-versus-capacity probability with a deterministic order, and give the `maxCount == 0` case a defined path. The threshold reasoning and the zero-capacity check were raised in the same review and never answered, so the tier order would close them out too.

Either way, #1181 deserves an ending: rebased and landed as a first cut of this work, or closed with a pointer to this task.

