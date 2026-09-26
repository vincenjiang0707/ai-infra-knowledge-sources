# [Issue #2569] Gateway cache metrics collection is too aggressive and lacks freshness semantics

source: https://github.com/vllm-project/aibrix/issues/2569
state: open | updated: 2026-09-24T17:22:11Z
labels: area/gateway

## 正文

## Summary

Gateway cache currently pulls and parses engine metrics very aggressively, stores values without freshness metadata, and emits high-cardinality Prometheus series from the same path. The main issue is not just metric-name mapping. The deeper problems are duplicated collection responsibility, mismatched refresh cadence, and inconsistent failure semantics between collection, cache, routing, and observability.

This issue proposes splitting the fix into three PRs:

1. Reduce pod metrics fetch pressure and isolate failing pods.
2. Add metric freshness semantics for routing and narrow routing metric collection.
3. Reduce Prometheus cardinality and clean stale metric series.

## Current behavior

Relevant files:

- `pkg/cache/cache_metrics.go`
- `pkg/cache/cache_init.go`
- `pkg/cache/cache_impl.go`
- `pkg/cache/cache_api.go`
- `pkg/cache/informers.go`
- `pkg/cache/pod.go`
- `pkg/metrics/engine_fetcher.go`
- `pkg/metrics/types.go`
- `pkg/metrics/custom_metrics.go`
- `pkg/plugins/gateway/algorithms/least_kv_cache.go`

Today Gateway cache uses a default pod metrics refresh interval of `50ms`.

On every tick:

1. `Store.updatePodMetrics()` iterates all cached ready pods.
2. Each ready pod is non-blockingly enqueued into `podMetricsJobs`.
3. Workers call `FetchAllTypedMetrics()`.
4. The fetcher pulls the engine `/metrics` endpoint and parses Prometheus text.
5. Parsed values are stored in `Pod.Metrics` or `Pod.ModelMetrics`.
6. Values are also emitted to Prometheus.
7. Routing algorithms later read cached values through getters such as `GetMetricValueByPodModel()`.

Important current limits:

- Default refresh interval is `50ms`, which is very aggressive for a full ready-pod scan.
- Worker count defaults to `10` and is not env-configurable.
- Pod metrics job queue size defaults to `100` and is not env-configurable.
- Queue full behavior skips collection for that pod and tick, but there is no explicit counter.
- A failing pod can be re-enqueued repeatedly on future ticks.
- `EngineMetricsFetcher` has per-call retry/backoff, but cache scheduling does not have per-pod failure backoff.
- Cached metric values do not include a last-success timestamp.
- Routing algorithms cannot distinguish fresh values from old retained values.
- `least-kv-cache` uses cached `KVCacheUsagePerc` and `CPUCacheUsagePerc` without freshness checks.
- Engine metric Prometheus labels include high-cardinality dimensions such as `pod` and `gateway_pod`.
- Histogram emission also creates `_p50`, `_p90`, and `_p99` gauge series.
- Pod deletion clears some cache state and rate history, but there is no unified gauge/counter/histogram series deletion.

## Why this matters

### 1. `50ms` full ready-pod scan is too aggressive

At larger pod counts, a `50ms` tick means Gateway repeatedly walks all ready pods and tries to enqueue HTTP fetch work. Each worker then performs an HTTP GET to `/metrics` and parses Prometheus text.

This scales with:

- ready pod count
- number of gateway replicas
- engine `/metrics` response size
- number of metric families parsed
- number of models exposed by a pod

For routing, a `50ms` cache refresh is also unlikely to provide proportional value because the engine metrics themselves may not update at that cadence.

### 2. Bad pods can continuously consume collection capacity

If a pod's metrics endpoint is slow, unreachable, or malformed, the worker returns an error and the next refresh cycle may enqueue the same pod again. This creates a loop where bad pods can repeatedly consume queue and worker capacity.

The fetcher-level retry/backoff handles retries inside a single fetch attempt, but it does not prevent future cache ticks from scheduling the same bad pod immediately again.

### 3. Routing reads values without freshness semantics

The cache getters return `metrics.MetricValue` only. They do not expose when the value was last successfully updated.

This means a stale value can remain in memory after repeated collection failures. Routing algorithms such as `least-kv-cache` may continue to route based on outdated `KVCacheUsagePerc` or `CPUCacheUsagePerc`.

### 4. Default collection set is broader than routing needs

`getAllAvailableMetrics()` currently returns broad metric sets, including counter/gauge metrics, histogram metrics, and label-query metrics. Even if a routing algorithm needs only a small subset, Gateway still pulls `/metrics` and processes more metric families than necessary.

The fetch still has to GET `/metrics`, but parsing and storing should be limited to metrics actually required by enabled routing algorithms or explicitly configured by operators.

### 5. Prometheus output mixes internal scheduling dimensions with external observability

The internal cache needs pod/model-level detail for routing. Prometheus does not always need that full dimensionality by default.

Current default labels include dimensions such as:

- `namespace`
- `pod`
- `model`
- `engine_type`
- `roleset`
- `role`
- `role_replica_index`
- `gateway_pod`

`pod` and `gateway_pod` can multiply series count significantly, especially with multiple gateway replicas and pod churn.

### 6. Pod deletion does not uniformly clear metric series

Pod delete handling clears `metaPods` and rate history, but custom gauge/counter/histogram collectors do not have one unified deletion path by pod. Histogram snapshots in particular need delete support.

### 7. Histogram percentile gauges increase series count

Each histogram emit also produces derived percentile gauges:

- `_p50`
- `_p90`
- `_p99`

This increases series count and pushes percentile calculation into Gateway, while Prometheus can usually compute percentiles with `histogram_quantile` over a range.

## Proposed implementation plan

## PR1: Reduce fetch pressure and isolate bad pods

### Goal

Reduce Gateway resource pressure from pod metrics collection without changing routing semantics or Prometheus label behavior.

### Scope

Implement:

- Change default pod metrics refresh interval from `50ms` to `1000ms`.
- Add env-configurable pod metrics worker count.
- Add env-configurable pod metrics job queue size.
- Add cache-level per-pod fetch failure backoff.
- Skip pods under backoff before enqueueing them.
- Add low-cardinality counters for enqueue drops and fetch failures.
- Add tests for defaults, env overrides, queue-full behavior, and backoff reset behavior.

Do not implement in PR1:

- Routing metric collection narrowing.
- Queue deduplication.
- Freshness-aware routing.
- Prometheus label/cardinality changes.
- Histogram percentile gauge changes.
- Worker fetch timeout changes.

### Config changes

Existing env:

```text
AIBRIX_POD_METRIC_REFRESH_INTERVAL_MS
```

Change default:

```text
old default: 50
new default: 1000
```

Add:

```text
AIBRIX_POD_METRICS_WORKER_COUNT
AIBRIX_POD_METRICS_JOB_QUEUE_SIZE
```

Defaults:

```text
AIBRIX_POD_METRICS_WORKER_COUNT=10
AIBRIX_POD_METRICS_JOB_QUEUE_SIZE=10 * workerCount
```

Invalid values less than `1` should fall back to defaults.

### Backoff behavior

Backoff should be cache-layer scheduling state.

Key:

```text
<namespace>/<name>
```

Also store pod UID in the state. If UID changes for the same namespace/name, clear the previous state.

Trigger:

- Only when the whole `FetchAllTypedMetrics()` call returns an error.
- Do not trigger for `result.Errors` after a successful fetch.

Schedule:

```text
1s, 2s, 4s, 8s, ... max 30s
```

No jitter in this PR.

Reset or clear when:

- Fetch succeeds.
- Pod UID changes.
- Pod is deleted.

Backoff should be checked in `updatePodMetrics()` before enqueue. A pod under backoff should not enter `podMetricsJobs`.

### New counters

Add:

```text
aibrix_pod_metrics_enqueue_dropped_total{reason}
```

Initial reasons:

- `queue_full`
- `backoff`

Add:

```text
aibrix_pod_metrics_fetch_failures_total{engine_type,reason}
```

Initial reason:

- `fetch_error`

Do not include `pod` or `namespace` labels on these counters.

### Suggested code shape

Add a small backoff state type in the cache package:

```go
type podMetricsBackoffState struct {
    uid         string
    failures    int
    nextFetchAt time.Time
}
```

Add helpers:

```go
func podMetricsBackoffKey(pod *Pod) string
func (c *Store) shouldSkipPodMetricsFetch(pod *Pod, now time.Time) bool
func (c *Store) recordPodMetricsFetchFailure(pod *Pod, now time.Time)
func (c *Store) recordPodMetricsFetchSuccess(pod *Pod)
func (c *Store) clearPodMetricsBackoff(namespace, name string)
```

Expected behavior:

- `shouldSkipPodMetricsFetch()` returns true only when the stored UID matches and `now < nextFetchAt`.
- UID mismatch deletes old state and allows enqueue.
- `recordPodMetricsFetchFailure()` increments consecutive failures and sets `nextFetchAt`.
- `recordPodMetricsFetchSuccess()` clears state.
- `clearPodMetricsBackoff()` is called from pod deletion.

### PR1 implementation refinements

After reviewing the current code shape, keep PR1 intentionally narrow:

- Keep env parsing as package-level helpers rather than expanding `InitOptions`.
- Compute worker count before queue size; when queue size is unset or invalid, default to `10 * workerCount`.
- Preserve the historical default behavior as `10` workers and queue size `100`.
- Add `podMetricsBackoff utils.SyncMap[string, podMetricsBackoffState]` on `Store`, instead of adding mutable scheduling state to `Pod`.
- Keep backoff helpers deterministic by passing `now time.Time` into `shouldSkipPodMetricsFetch()` and `recordPodMetricsFetchFailure()`.
- In `recordPodMetricsFetchFailure()`, increment the consecutive failure count first, then calculate delay as `1 << (failures-1)` seconds, capped at `30s`.
- In `updatePodMetrics()`, check backoff before enqueue. A backoff skip should not enter `podMetricsJobs`.
- In `worker()`, only add two hooks around the existing fetch call:
  - On whole `FetchAllTypedMetrics()` error: increment fetch failure counter and record backoff.
  - On successful `FetchAllTypedMetrics()` return: clear backoff.
- Do not treat `result.Errors` from a successful fetch as a whole-pod fetch failure.
- Clear backoff from pod delete handling in `pkg/cache/informers.go`.
- Define PR1 counters as explicit `pkg/metrics` constants/helpers, not as raw engine metrics in the central engine collection registry.
- Remove comments that hard-code `50ms`; refer to the next refresh cycle instead.

### PR1 tests

Cover:

- Default refresh interval is `1000ms`.
- Worker count env override is respected.
- Invalid worker count falls back to default.
- Queue size default is `10 * workerCount`.
- Queue size env override is respected.
- Invalid queue size falls back to computed default.
- `updatePodMetrics()` remains non-blocking when queue is full.
- Queue full increments drop counter with `reason=queue_full`.
- Fetch failure records backoff state.
- Pod under backoff is not enqueued and increments drop counter with `reason=backoff`.
- Fetch success clears backoff.
- Pod UID change clears old backoff and allows enqueue.
- Pod delete clears backoff.

Prefer deterministic tests that pass `now` into helpers rather than tests that sleep.

For counter tests, replace `metrics.IncrementCounterMetricFnForTest` and capture calls instead of registering real Prometheus collectors. This avoids global collector pollution and matches the existing custom metric test style.

For queue-full behavior, assert that the queue length does not change and the `queue_full` counter is emitted. Avoid timeout-based "does not block" tests.

### PR1 acceptance criteria

- Default refresh is `1000ms`.
- Worker count and queue size are env-configurable.
- Existing default worker/queue behavior remains equivalent to `10/100`.
- Bad pods enter cache-layer exponential backoff after whole-fetch errors.
- Backoff pods are skipped before enqueue.
- Fetch success, pod UID change, and pod delete clear backoff.
- Queue full and backoff skips are observable by counter.
- Fetch failures are observable by counter.
- Existing routing behavior is unchanged.
- Existing Prometheus label behavior is unchanged.

## PR2: Add freshness semantics and narrow routing collection

### Goal

Make routing algorithms freshness-aware and reduce unnecessary metric parsing/storage for routing.

### Scope

Implement:

- Add cache-local metric records with timestamps.
- Preserve existing metric value getter compatibility.
- Add record getters for freshness-sensitive callers.
- Add routing stale threshold configuration.
- Update `least-kv-cache` to skip pods with missing or stale required metrics.
- Fall back to random when all pods are unscorable.
- Add low-cardinality metric staleness visibility.
- Narrow routing collection to subscribed or explicitly allowed metrics.

Do not implement in PR2:

- Prometheus label/cardinality changes.
- Histogram percentile gauge changes.
- Collector series deletion.
- Queue deduplication.

### MetricRecord

Add in `pkg/cache`:

```go
type MetricRecord struct {
    Value     metrics.MetricValue
    Timestamp time.Time
}
```

This belongs in cache, not in `pkg/metrics`, because freshness is cache/storage semantics.

Do not include `LastError` or `ConsecutiveFailures` in `MetricRecord`. Failure/backoff state is covered by PR1 and should remain separate from the last successful metric value.

### Storage

Preferred implementation:

```go
Metrics      utils.SyncMap[string, MetricRecord]
ModelMetrics utils.SyncMap[string, MetricRecord]
```

Old getters should unwrap `.Value`.

Alternative implementation is timestamp side maps, but that is more error-prone because value and timestamp can drift.

### API

Keep existing getters source-compatible:

```go
GetMetricValueByPod(podName, podNamespace, metricName string) (metrics.MetricValue, error)
GetMetricValueByPodModel(podName, podNamespace, modelName, metricName string) (metrics.MetricValue, error)
```

Add:

```go
GetMetricRecordByPod(podName, podNamespace, metricName string) (MetricRecord, error)
GetMetricRecordByPodModel(podName, podNamespace, modelName, metricName string) (MetricRecord, error)
```

Old getters should call the new record getters and return `record.Value`.

Add comments indicating that freshness-sensitive routing should use record getters.

### Timestamp behavior

Set `Timestamp` when a metric is successfully written to cache.

For engine metrics:

- Capture one `now := time.Now()` after successful fetch.
- Use it for all metric records from that fetch result.

For local request-tracing metrics:

- Set timestamp when the local value is written.

For PromQL metrics:

- Set timestamp when the PromQL query succeeds and the cache is updated.

### Stale threshold

Add:

```text
AIBRIX_ROUTING_METRIC_STALE_THRESHOLD_MS
```

Behavior:

- If env is set to a valid positive value, use it.
- Otherwise default to:

```text
max(5s, 3 * podMetricRefreshInterval)
```

### least-kv-cache behavior

Update `pkg/plugins/gateway/algorithms/least_kv_cache.go`.

Required metrics:

- `KVCacheUsagePerc`
- `CPUCacheUsagePerc`

New behavior per pod:

1. Read both records with `GetMetricRecordByPodModel()`.
2. If either record is missing, the pod is unscorable.
3. If either record is stale, the pod is unscorable.
4. Score only pods with both fresh required metrics.
5. If no pods are scorable, use existing random fallback behavior.

Do not treat missing `CPUCacheUsagePerc` as zero. That would bias routing toward pods or engines with incomplete metrics.

### Staleness metric

Add:

```text
aibrix_metric_staleness_seconds
```

Labels:

```text
metric
engine_type
```

Do not include pod or namespace labels.

This is intentionally low-cardinality. It can show systemic stale behavior but cannot identify a single stale pod. Pod-level diagnosis can be handled through logs or a future opt-in debug mode.

### Narrow routing collection

Current default collection uses a broad hardcoded set. Replace the default routing collection set with metrics required by enabled routing algorithms and cache subscribers.

Suggested env override:

```text
AIBRIX_POD_METRICS_ALLOWLIST
```

Format:

```text
metric_a,metric_b,metric_c
```

Behavior:

- If set, collect only listed valid raw pod metrics.
- If unset, collect subscribed metrics.
- Invalid names should be logged and ignored.
- Histogram metrics should not be collected by default unless explicitly subscribed or explicitly allowed.

Before narrowing, verify that all algorithms that read cache metrics correctly expose `SubscribedMetrics()` or equivalent metadata.

### PR2 tests

Cover:

- `updatePodRecord()` stores `MetricRecord` with a non-zero timestamp.
- Existing `GetMetricValueByPod()` still returns only `MetricValue`.
- New `GetMetricRecordByPod()` returns value and timestamp.
- New `GetMetricRecordByPodModel()` returns value and timestamp.
- Missing record returns the same style of error as missing metric today.
- Stale threshold uses env when valid.
- Stale threshold defaults to `max(5s, 3*refreshInterval)` when env is unset.
- `least-kv-cache` skips pod when `KVCacheUsagePerc` is stale.
- `least-kv-cache` skips pod when `CPUCacheUsagePerc` is stale.
- `least-kv-cache` uses random fallback when all pods are unscorable.
- Collection set uses subscribed metrics when allowlist is unset.
- Collection set uses env allowlist when set.
- Invalid allowlist entries are ignored.
- Histogram metrics are not collected by default unless subscribed or explicitly allowed.

### PR2 acceptance criteria

- Cache records carry timestamps.
- Old metric value getters remain compatible.
- New record getters are available.
- `least-kv-cache` no longer routes based on stale required metrics.
- All-stale or all-missing behavior falls back to random.
- Staleness threshold is configurable and has a safe default.
- Staleness is observable with low-cardinality labels.
- Default routing collection no longer means collecting every available raw metric.

## PR3: Reduce Prometheus cardinality and clean stale series

### Goal

Separate internal routing dimensions from external observability dimensions, and prevent Prometheus series growth from pod churn and histogram-derived gauges.

### Scope

Implement:

- Add low-cardinality Prometheus exposure mode.
- Keep pod-level metric detail behind an explicit env/debug switch.
- Revisit default `gateway_pod` label usage.
- Add unified pod metric series deletion.
- Add histogram collector delete support.
- Disable histogram percentile gauges by default.

Do not implement in PR3:

- Routing behavior changes.
- Collection scheduling changes.
- MetricRecord/freshness changes.
- Routing collection narrowing.

### Label mode

Add:

```text
AIBRIX_ENGINE_METRICS_LABEL_MODE
```

Supported values:

```text
detailed
compact
```

`detailed` mode preserves current labels.

`compact` mode should use a lower-cardinality default such as:

- `model`
- `engine_type`
- `roleset`
- `role`

Do not include `gateway_pod` on engine metrics in compact mode. Reserve `gateway_pod` for gateway-local metrics where the gateway replica is the measured target.

Compatibility note:

- If backwards compatibility is required, initially default to `detailed`.
- If maintainers accept an observability-breaking change, default directly to `compact`.

### Internal vs external dimensions

Do not remove pod/model detail from the internal routing cache. The cache still needs pod-level data for routing.

The label reduction applies only to Prometheus emission.

### Series deletion

Add a unified deletion API in `pkg/metrics/custom_metrics.go`:

```go
func DeleteMetricSeriesForPod(pod *v1.Pod)
```

or, if model extras are needed:

```go
func DeleteMetricSeriesForPod(pod *v1.Pod, modelNames []string)
```

Expected behavior:

- Delete matching gauge series.
- Delete matching counter series where supported.
- Delete matching histogram series.
- Delete derived percentile gauge series when enabled.

Call this from pod delete handling in `pkg/cache/informers.go`.

### Histogram collector delete support

The custom histogram collector stores snapshots in:

```go
data map[string]*histogramSnapshot
```

Add delete support, preferably predicate-based:

```go
func (c *histogramCollector) DeleteMatching(predicate func(labelNames []string, labelValues []string) bool)
```

Predicate-based deletion is more flexible than exact label-value deletion because label sets may differ between detailed and compact modes.

### Histogram percentile gauges

Add:

```text
AIBRIX_ENABLE_HISTOGRAM_PERCENTILE_GAUGES
```

Default:

```text
false
```

Behavior:

- When false, emit only the histogram.
- When true, keep current `_p50`, `_p90`, and `_p99` gauge behavior.

Longer term, percentile calculation should generally happen in Prometheus queries using `histogram_quantile`.

### PR3 tests

Cover:

- `compact` label mode omits `pod` and `gateway_pod` for engine metrics.
- `detailed` label mode preserves current labels.
- Gateway-local metrics can still include `gateway_pod` where appropriate.
- `DeleteMetricSeriesForPod()` removes gauge series for deleted pods.
- `DeleteMetricSeriesForPod()` removes counter series for deleted pods where supported.
- `DeleteMetricSeriesForPod()` removes histogram snapshots for deleted pods.
- Pod delete handler calls unified metric deletion.
- Histogram percentile gauges are not emitted by default.
- Histogram percentile gauges are emitted when `AIBRIX_ENABLE_HISTOGRAM_PERCENTILE_GAUGES=true`.

### PR3 acceptance criteria

- Operators can choose compact or detailed engine metric labels.
- Compact mode avoids pod/gateway fan-out for engine metrics.
- Internal routing cache keeps pod-level detail.
- Pod deletion clears gauge/counter/histogram series where possible.
- Histogram snapshots do not grow indefinitely due to deleted pods.
- Histogram percentile gauges are off by default and controlled by env.
- Compatibility impact is documented in release notes or the PR description.

## Proposed PR titles

```text
gateway: reduce pod metrics fetch pressure and add failure backoff
```

```text
gateway: add metric freshness records for routing decisions
```

```text
metrics: reduce engine metric cardinality and clean pod series
```

## Validation plan

### PR1 validation

- Unit tests for env defaults and overrides.
- Unit tests for queue full non-blocking behavior.
- Unit tests for backoff state transitions.
- Manual or integration validation with many ready pods and failing `/metrics` endpoints.
- Confirm bad pods stop occupying workers every tick.

### PR1 benchmark validation

Add a focused benchmark to quantify scheduler pressure before and after PR1. The benchmark should not require real engine pods or network I/O; it should exercise the cache-layer scan/enqueue/backoff path directly.

Suggested benchmark shape:

```go
func BenchmarkUpdatePodMetricsEnqueue(b *testing.B)
```

Scenarios:

- `pods=100`, no backoff, queue large enough.
- `pods=1000`, no backoff, queue large enough.
- `pods=1000`, queue full.
- `pods=1000`, 50% pods under backoff.
- `pods=1000`, 90% pods under backoff.

Measure:

- `ns/op` for `Store.updatePodMetrics()`.
- allocations per operation.
- number of jobs enqueued per iteration.
- number of drops by reason (`queue_full`, `backoff`) using the test counter hook.

Acceptance signal:

- Backoff-heavy scenarios should enqueue dramatically fewer jobs than the no-backoff scenario.
- Queue-full scenarios should remain bounded and non-blocking.
- The benchmark should demonstrate that bad pods are skipped before they consume worker queue capacity.

Optional integration benchmark:

- Start `httptest` metrics endpoints for many pods.
- Compare fetch attempts per second with default refresh `50ms` versus `1000ms`.
- Include a mix of healthy, slow, and failing endpoints.
- Validate that failing endpoints stop receiving fetch attempts while under cache-layer backoff.

### PR2 validation

- Unit tests for record getters and stale threshold calculation.
- Unit tests for `least-kv-cache` stale/missing behavior.
- Unit tests for all-stale random fallback.
- Verify staleness metric emits with expected low-cardinality labels.
- Verify routing collection no longer includes broad histogram sets by default.

### PR3 validation

- Unit tests for compact and detailed label modes.
- Unit tests for gauge/counter/histogram deletion.
- Unit tests for histogram percentile gauge switch.
- Compare Prometheus series count before and after compact mode.
- Delete pods repeatedly and confirm collector in-memory series do not grow indefinitely.

## Final decision log

- Default pod metrics refresh should become `1000ms`.
- Worker count and queue size should be env-configurable.
- Queue size default should be `10 * workerCount`.
- Per-pod backoff should be added in the cache layer.
- Backoff should be deterministic exponential backoff with base `1s` and max `30s`.
- Backoff should not use jitter in PR1.
- Backoff should be checked before enqueue.
- Backoff should trigger only on whole-fetch errors.
- Fetch success, pod UID change, and pod delete should reset or clear backoff.
- Queue full and backoff skips should increment `aibrix_pod_metrics_enqueue_dropped_total{reason}`.
- Fetch failures should increment `aibrix_pod_metrics_fetch_failures_total{engine_type,reason}`.
- Metric freshness should use cache-local `MetricRecord{Value, Timestamp}`.
- Old value getters should remain compatible.
- New record getters should be added for freshness-sensitive consumers.
- Routing stale threshold should use `AIBRIX_ROUTING_METRIC_STALE_THRESHOLD_MS`.
- Default stale threshold should be `max(5s, 3*refreshInterval)`.
- `least-kv-cache` should skip pods with missing/stale required metrics.
- All-missing or all-stale `least-kv-cache` should fall back to random.
- Staleness metric should be low-cardinality: `metric,engine_type`.
- Prometheus label/cardinality cleanup should be isolated to PR3.
- Histogram percentile gauges should be disabled by default in PR3.


## 评论 (1)

### bolubo · 2026-09-24

Part 1 is in main via #2635 (1000ms default, worker/queue envs, per-pod backoff, both counters), so this note is about the two parts that are still open.

One thing that matters for part 2: the design treats a missing required metric as unscorable and falls back to random when no pod is scorable. least-kv-cache handles the missing CPU metric differently today, and that behavior arrived after this issue was written. `cpuCacheUsage()` (`least_kv_cache.go:59-71`) returns 0 when `CPUCacheUsagePerc` is absent. On V1 the engine does not emit `cpu_cache_usage_perc` at all (it went away with KV swapping), so the fetch reports it in `result.Errors` and the cache slot is never written. The comment there says treating that as fatal "would mark every pod unscored and drop this router to its random fallback". The carve-out came in with #2365, merged later the same day as #2635.

On V1 there is one more distinction to make, because `CPUCacheUsagePerc` is permanently missing there. If missing simply means unscorable, every pod becomes unscorable and each request goes to the random fallback, which is what the current carve-out exists to prevent.

One way to add freshness: treat "no record yet" and "record too old" as separate states. A metric with no record keeps today's treatment (missing GPU already makes a pod unscorable, missing CPU stays 0 on V1), while a record that ages past the stale threshold makes the pod unscorable. That still covers the incomplete-metrics bias this issue mentions: a pod with failing collection ages out of scoring, while the V1 CPU metric is never recorded at all. `ScoreAll` already returns the `scored []bool` for this, and the same scorer is reused as the load_balance tie-breaker (`load_balance.go:259`), so both callers would share one rule.

For part 3: the percentile gauges are still emitted unconditionally (`custom_metrics.go:451-455`), and I could not find a per-pod delete path for the engine metric counters or histograms. `deletePod` (`informers.go:228`) clears the cache maps, backoff, and rate history, but not the exported series. The gauge side already has `DeleteGaugeMetricForPod` (`custom_metrics.go:125`), so there is a pattern to extend.

Not sure if a part 2 branch is already in flight; if so, feel free to ignore this.

