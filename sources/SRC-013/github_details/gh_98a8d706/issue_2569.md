# [Issue #2569] [Proposal] Upstream llm-d Unified Model Server Telemetry to OpenTelemetry GenAI Semantic Conventions (gen_ai.server.*)

source: https://github.com/llm-d/llm-d/issues/2569
state: open | updated: 2026-09-24T01:42:48Z
labels: enhancement

## 正文

### Feature Area

Observability / Monitoring

### Problem Statement

# [Proposal] Upstream `llm-d` Unified Model Server Telemetry to OpenTelemetry GenAI Semantic Conventions (`gen_ai.server.*`)

## Summary

Following up on https://github.com/llm-d/llm-d-router/issues/708 and [PR #2516](https://github.com/llm-d/llm-d-router/pull/2516) (`pkg/common/observability/semconv/`), we have drafted a proposal for the **OpenTelemetry GenAI Semantic Conventions SIG** to standardize **server-side LLM inference infrastructure metrics** (`gen_ai.server.*`).

Before presenting this to the upstream OTel GenAI SIG, we want to share the proposal with the `llm-d` community for feedback and alignment. Please share your insights by leaving comments there. 

- 📄 **Full Proposal & Cross-Engine Evidence Doc:** [OpenTelemetry Semantic Conventions for LLM Inference Serving Infrastructure ](https://docs.google.com/document/d/1YuaGm7m4wOkROT9dMZuxnbLiVWclqZNXE3vV0QKZbYY/edit?usp=sharing)
---

## Motivation: Why Upstream `llm-d`'s Unification Layer?

Today, `llm-d` routes across heterogeneous inference engines (**vLLM, SGLang, TensorRT-LLM (`trtllm-serve`), and Triton (`triton-tensorrt-llm`)**). Because OpenTelemetry does not yet define model-server runtime metrics (queue depth, KV-cache saturation, prefix cache hits, phase breakdown, LoRA slot capacity), `llm-d` had to build its own 3-stage normalization pipeline:

1. **Per-Engine `MappingRegistry`** ([`pkg/epp/framework/plugins/datalayer/extractor/metrics/factories.go`](https://github.com/llm-d/llm-d-router/blob/main/pkg/epp/framework/plugins/datalayer/extractor/metrics/factories.go)): Selects metric mappings per Pod via `llm-d.ai/engine-type`.
2. **In-Memory `Extractor` Normalization** ([`extractor.go`](https://github.com/llm-d/llm-d-router/blob/main/pkg/epp/framework/plugins/datalayer/extractor/metrics/extractor.go)): Parses incompatible formats—such as vLLM's string labels on info gauges (`vllm:cache_config_info{block_size, num_gpu_blocks}` and `vllm:lora_requests_info` CSV labels) vs. SGLang/TRT-LLM numeric gauges—into `MetricsState`.
3. **Re-Emission of `llm_d_epp_*` Metrics** ([`pkg/epp/metrics/llm_d_router_metrics.go`](https://github.com/llm-d/llm-d-router/blob/main/pkg/epp/metrics/llm_d_router_metrics.go)): Re-publishes unified metrics (`llm_d_epp_per_endpoint_queue_size`, `llm_d_epp_request_streaming_itl_seconds`, etc.) for dashboards and autoscalers.

**Goal:** By upstreaming the per-server schema proven in `llm-d`'s `MappingRegistry` into OpenTelemetry (`gen_ai.server.*`), we can:
- Align `llm-d`, vLLM, SGLang, and TensorRT-LLM on a single vendor-neutral OTel metric contract.
- Eventually eliminate fragile label-parsing workarounds in `extractor.go` (e.g., `strconv.Atoi` on `cache_config_info` and CSV splitting on `lora_requests_info`).

---

## Scope & Boundary: What Goes to OTel vs. What Stays in `llm-d`

We classify `llm-d`'s telemetry into three clear buckets:

1. **Bucket 1 — Already in OTel `gen_ai.*` (Direct Adoption):**
   - `llm_d_epp_request_duration_seconds` $\rightarrow$ `gen_ai.server.request.duration`
   - `llm_d_epp_request_ttft_seconds` $\rightarrow$ `gen_ai.server.time_to_first_token`
   - `llm_d_epp_request_streaming_tpot_seconds` $\rightarrow$ `gen_ai.server.time_per_output_token`
   - `llm_d_epp_request_{input,output}_tokens` $\rightarrow$ `gen_ai.client.token.usage`
2. **Bucket 2 — Per-Engine Runtime & Streaming Metrics Unified by `llm-d` (Proposed to OTel in Sections 2.1–2.8):**
   - See mapping table below. Every model-server metric normalized by `MappingRegistry` is included.
3. **Bucket 3 — Router-Internal & Pool Statistical Rollups (Kept Private in `llm_d.*` / `llm_d_epp_*`):**
   - Pool-wide mean/std-dev across pods (`llm_d_epp_average_*`, `llm_d_epp_std_dev_*`, `llm_d_epp_ready_endpoints`).
   - EPP scheduler, plugin DAG, flow-control priority bands, and ZMQ KV-index internals (`llm_d_epp_scheduler_*`, `llm_d_epp_plugin_*`, `llm_d_epp_flow_control_*`, and the 60+ span attributes in `semconv/llm_d.go`).

---

## Proposed OTel Conventions vs. Current `llm-d` & Engine Metrics

| # | Proposed OTel Convention | Current `llm-d` Metric / `MetricsState` | Backend Engine Metrics (`vLLM` / `SGLang` / `TRT-LLM`) | Target Upstream Issue / PR |
| :--- | :--- | :--- | :--- | :--- |
| **2.1** | **`gen_ai.server.request.count`** (`state=queued\|running\|preempted`) + **`.limit`** | • `llm_d_epp_per_endpoint_queue_size`<br>• `llm_d_epp_request_running`<br>• `WaitingQueueSize`, `RunningRequestsSize` | • **vLLM:** `vllm:num_requests_{waiting,running}`<br>• **SGLang:** `sglang:num_{queue,running}_reqs`<br>• **TRT-LLM:** `trtllm_num_requests_{waiting,running}`, `nv_trt_llm_request_metrics{request_type=waiting\|scheduled}` | [OTel Issue #87](https://github.com/open-telemetry/semantic-conventions-genai/issues/87) |
| **2.2** | **`gen_ai.server.kv_cache.usage`** / **`.limit`** / **`.utilization`** + **`gen_ai.kv_cache.block.size`** | • `llm_d_epp_average_kv_cache_utilization`<br>• `KVCacheUsagePercent`, `CacheBlockSize`, `CacheNumBlocks` (`limit = num_blocks × block_size`) | • **vLLM:** `vllm:kv_cache_usage_perc` + `vllm:cache_config_info{block_size, num_gpu_blocks}`<br>• **SGLang:** `sglang:token_usage` + `sglang:page_size`, `sglang:num_pages`<br>• **TRT-LLM:** `trtllm_kv_cache_{utilization,tokens_per_block,max_blocks}` | [OTel Issue #87](https://github.com/open-telemetry/semantic-conventions-genai/issues/87) |
| **2.3** | **`gen_ai.server.prefix_cache.queries`** / **`.hits`** | • `llm_d_epp_request_cached_tokens`<br>• `gen_ai.usage.cache_read.input_tokens`<br>• `CachePrefixMatchUnit` + prefix indexer | • **vLLM:** `vllm:prefix_cache_{queries,hits}`, `vllm:cache_config_info{prefix_match_unit}`<br>• **SGLang:** `sglang:cached_tokens`, `sglang:cache_hit_rate` | [OTel Issue #87](https://github.com/open-telemetry/semantic-conventions-genai/issues/87) |
| **2.4** | **`gen_ai.server.inter_token_latency`** | • `llm_d_epp_request_streaming_itl_seconds` *(emitted alongside `tpot_seconds`)* | • **vLLM:** `vllm:inter_token_latency_seconds`<br>• **SGLang:** `sglang:inter_token_latency_seconds` | [OTel PR #164](https://github.com/open-telemetry/semantic-conventions-genai/pull/164) |
| **2.5** | **`gen_ai.server.phase.duration`** (`phase=queue\|prefill\|decode\|inference`) | • `llm_d_epp_flow_control_request_queue_duration_seconds`<br>• `llm_d_epp_request_{ttft,streaming_tpot}_seconds` | • **vLLM:** `vllm:request_{queue,prefill,decode,inference}_time_seconds`<br>• **SGLang:** `sglang:queue_time` | [OTel Issue #408](https://github.com/open-telemetry/semantic-conventions-genai/issues/408) & [#231](https://github.com/open-telemetry/semantic-conventions-genai/issues/231) |
| **2.6** | **`gen_ai.server.kv_transfer.duration`** / **`.size`** | • `llm_d_epp_flow_control_pool_saturation{stage="prefill"\|"decode"}`<br>• Spans: `llm_d.pd_proxy.coordinator_overhead_ms` | • Custom NIXL / Mooncake / Dynamo KV-connector stats | Hold for discussion |
| **2.7** | **`gen_ai.server.lora.adapter.count`** (`state=active\|waiting`) / **`.limit`** | • `ActiveModels`, `WaitingModels`, `MaxActiveModels` (`LoRASpec`) | • **vLLM:** `vllm:lora_requests_info{running_lora_adapters, waiting_lora_adapters, max_lora}` *(CSV labels)* | Hold for discussion |
| **2.8** | **`gen_ai.request.id`** *(Span Attribute)* | • `semconv.GenAIRequestIDKey` (`gen_ai.request.id` in [PR #2516](https://github.com/llm-d/llm-d-router/pull/2516)) | • **vLLM:** `request_id` (`cmpl-*` / `chatcmpl-*`)<br>• **SGLang:** `rid` | [OTel Issue #231](https://github.com/open-telemetry/semantic-conventions-genai/issues/231) |

---

## Proposed Plan for `llm-d`

1. **No Breaking Changes to `llm_d_epp_*`:** Existing `llm_d_epp_*` metrics remain intact while `gen_ai.server.*` conventions are in `development` status upstream.
2. **Add OTel SemConv Constants & Optional Bridge:** Once Slices 1–3 land in `open-telemetry/semantic-conventions-genai`, we can add the corresponding metric definitions to `pkg/common/observability/semconv/genai.go` and optionally expose OTel-compliant `gen_ai.server.*` metrics from `llm-d`'s collector/bridge.
3. **Support Native Engine Adoption:** Collaborate with vLLM and SGLang maintainers so `MappingRegistry` can add a single `"otel"` engine profile once engines emit `gen_ai.server.*` natively.

## Feedback Requested from `llm-d` Maintainers

1. Does the **3-bucket boundary** (what we propose to OTel `gen_ai.server.*` vs. what stays private under `llm_d_epp_*` / `llm_d.*`) look right?
2. Are there any additional engine metrics in `MappingRegistry` or P/D disaggregation (`llm_d.pd_proxy.*`) that we should include or hold back?
3. Any concerns with referencing `llm-d`'s `MappingRegistry` and [PR #2516](https://github.com/llm-d/llm-d-router/pull/2516) as the production reference implementation in the OTel GenAI SIG meeting?


### Proposed Solution

n/a

### Alternatives Considered

_No response_

### Willingness to Contribute

Yes, I can submit a PR

### Additional Context

_No response_

## 评论 (2)

### PlateauGao · 2026-09-23

CC: @gyliu513  @ahg-g 

### gyliu513 · 2026-09-24


Thanks @PlateauGao for driving this. From the SIG-Observability side, the direction and the 3-bucket split look right, and using MappingRegistry as cross-engine evidence is fine. A few mappings in the table may need fixing before this goes to the OTel SIG:

1. Bucket 1: `llm_d_epp_*` latencies are measured at the router and include EPP flow-control queueing and network time, so they aren't `gen_ai.server.*` (server-measured). EPP token counts also shouldn't map to `gen_ai.client.token.usage`. I'd keep these under `llm_d_epp_*`.
2. 2.1: `llm_d_epp_request_running` counts requests in flight at the EPP, not the engine's running queue. The per-server source is `WaitingQueueSize`/`RunningRequestsSize` (`llm_d_epp_per_endpoint_queue_size`).
3. 2.5: `flow_control_request_queue_duration_seconds` is EPP queueing, not the engine's queue phase.
4. 2.6: neither `flow_control_pool_saturation` nor `pd_proxy.coordinator_overhead_ms` measures KV transfer. llm-d has no reference for this today, so please mark it as such.
5. 2.3: `llm_d_epp_request_cached_tokens` corresponds to `gen_ai.usage.cache_read.input_tokens`, not server-side prefix cache queries/hits.

It's also worth noting that `gen_ai.request.id` is a key llm-d defines itself until [#231](https://github.com/open-telemetry/semantic-conventions-genai/issues/231) lands. When presenting, I'd frame llm-d as evidence that these signals are available across engines, not as an existing implementation of `gen_ai.server.*`.
