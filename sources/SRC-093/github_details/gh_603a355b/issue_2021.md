# [Issue #2021] [Feat] Add observability for P/D disaggregated serving —  gateway metrics + trtllm engine dashboard

source: https://github.com/vllm-project/aibrix/issues/2021
state: open | updated: 2026-09-25T00:15:04Z
labels: priority/important-soon, kind/feature, area/observation

## 正文

### 🚀 Feature Description and Motivation

The pd router currently has no gateway-level Prometheus metrics for P/D operations. There's only structured logging via klog. This makes it impossible to monitor P/D health, debug latency issues, or set up alerts in  production.

Two Grafana dashboards covering:
### Gateway
1. P/D Overview — prefill success rate, prefill latency p50/p95/p99, decode routing latency, active prefill requests
2. Per-Worker Health? 
3. KV Transfer — transfer duration distribution, transfer size, reused vs new blocks ratio

### TRTLLM Dashboard
similar one like this
https://github.com/vllm-project/aibrix/blob/main/observability/grafana/AIBrix_vLLM_Engine_Dashboard.json



### Use Case

improve observability

### Proposed Solution

_No response_

## 评论 (3)

### DaveLi8086 · 2026-03-17

Picking up https://github.com/vllm-project/aibrix/issues/2021

### varungup90 · 2026-03-18

There are already metrics to cover success/failure of prefill request, distribution of time taken at prefill, ttft, kv_transfer. Audit them and add the missing ones

### bolubo · 2026-09-25

Took a pass at the audit requested above, against the current main (`294b1445`). Most of it has landed since the issue was filed, so below is a pass over what is in place and what still looks missing. Corrections welcome if any of it is stale.

**Already in place**

- prefill success rate: `gateway_prefill_request_success_total` and `gateway_prefill_request_fail_total`, labeled by model and status (`pkg/plugins/gateway/algorithms/pd/prefill/default.go:192` covers the async path, `pkg/plugins/gateway/algorithms/pd_disaggregation.go:447` the sync one).
- prefill latency distribution: `gateway_prefill_time_bucket_total` (`pkg/plugins/gateway/gateway_rsp_body.go:624`), with `gateway_routing_time_bucket_total` (`gateway_rsp_body.go:607`) for the routing segment.
- active prefill requests: `gateway_prefill_outstanding_requests` (`pkg/plugins/gateway/algorithms/pd/prefill/default.go:40`).
- ttft: `gateway_ttft_bucket_total` (`gateway_rsp_body.go:598`).
- kv transfer duration: `gateway_kv_transfer_time_bucket_total` (`gateway_rsp_body.go:625`).
- On the dashboard side, the PD Disaggregation section of `observability/grafana/AIBrix_Envoy_Gateway_Plugins_Dashboard.json` covers prefill success/fail, outstanding prefills, routing/prefill/KV transfer/decode time buckets, pod selection, and replica counts. The full metric list lives in `pkg/metrics/gateway_metrics.go`.

**What still looks missing**

1. Per-Worker Health. There is no per-prefill-pod success or failure signal. The pod dimension today shows up mostly in the selection counters (`pd_selected_prefill_pod_total`, `pd_disaggregation.go:1142`), the token-load gauges (`pkg/plugins/gateway/algorithms/pd/token_load_tracker.go:531`), and the ready-replica counts (`model_replicas`, `pkg/cache/cache_metrics.go:652`). The failure log already carries `prefill_pod` (`pd/prefill/default.go:185`), so the pod identity is available where the metrics are emitted.

2. KV transfer size. There is no metric for this yet, and no obvious data source either: `pkg/plugins/gateway/algorithms/pd/transfer/` only rewrites connector JSON (SHFS fills `kv_transfer_params`, NIXL wraps `disagg_prefill_resp`), nothing parses bytes or block counts.

3. Reused vs new blocks ratio. Similar picture; it would need block-level data that the gateway does not currently read.

4. TRT-LLM dashboard. There is no TRT-LLM dashboard under `observability/grafana` yet, while `samples/quickstart/tensorrt/` has P/D samples. The `undefined` model/engine label issue on that path (#2008) was fixed by #2118 in May.

**Two notes**

- The time buckets use string bucket labels (`"0-1ms"` style), not `le` histograms, so p50/p95/p99 are not directly computable from them. The dashboard's percentile panels currently read `e2e_request_latency_seconds_{p50,p90,p99}` (p90, not p95).
- There is no separate decode routing latency metric; `gateway_routing_time_bucket_total` covers arrival through prefill start instead.

If any of this is already in flight, please ignore it. Otherwise the four gaps above look like the natural places for a first cut.

