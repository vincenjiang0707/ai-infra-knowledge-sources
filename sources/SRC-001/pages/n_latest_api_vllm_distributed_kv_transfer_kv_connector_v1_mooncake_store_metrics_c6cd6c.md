source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/metrics/
lastmod: 2026-09-24

class MooncakeStorePromMetrics(KVConnectorPromMetrics):
"""Prometheus metrics for Mooncake store communication."""
def __init__(
self,
vllm_config: VllmConfig,
metric_types: dict[type[PromMetric], type[PromMetricT]],
labelnames: list[str],
per_engine_labelvalues: dict[int, list[object]],
):
super().__init__(vllm_config, metric_types, labelnames, per_engine_labelvalues)
metric_labelnames = labelnames + ["operation", "status"]
self._metric_cache: dict[tuple[int, str, str], dict[str, PromMetric]] = {}
self._histogram_operation_time = self._histogram_cls(
name="vllm:mooncake_store_operation_time_seconds",
documentation="Histogram of Mooncake store communication time.",
buckets=[
1e-3,
5e-3,
1e-2,
5e-2,
1e-1,
2e-1,
3e-1,
4e-1,
5e-1,
7.5e-1,
1.0,
1.5,
2.0,
3.0,
4.0,
],
labelnames=metric_labelnames,
)
self._counter_operation_calls = self._counter_cls(
name="vllm:mooncake_store_operation_total",
documentation="Number of Mooncake store communication operations.",
labelnames=metric_labelnames,
)
self._counter_operation_keys = self._counter_cls(
name="vllm:mooncake_store_operation_keys_total",
documentation="Number of Mooncake store keys touched by operations.",
labelnames=metric_labelnames,
)
self._counter_operation_bytes = self._counter_cls(
name="vllm:mooncake_store_operation_bytes_total",
documentation="Number of bytes transferred by Mooncake store operations.",
labelnames=metric_labelnames,
)
self._counter_failed_keys = self._counter_cls(
name="vllm:mooncake_store_operation_failed_keys_total",
documentation="Number of Mooncake store keys that failed in operations.",
labelnames=metric_labelnames,
)
def _get_metrics(
self,
engine_idx: int,
operation: str,
status: str,
) -> dict[str, PromMetric]:
cache_key = (engine_idx, operation, status)
if cache_key not in self._metric_cache:
label_values = self.per_engine_labelvalues[engine_idx] + [operation, status]
self._metric_cache[cache_key] = {
"time": self._histogram_operation_time.labels(*label_values),
"calls": self._counter_operation_calls.labels(*label_values),
"keys": self._counter_operation_keys.labels(*label_values),
"bytes": self._counter_operation_bytes.labels(*label_values),
"failed_keys": self._counter_failed_keys.labels(*label_values),
}
return self._metric_cache[cache_key]
def observe(self, transfer_stats_data: dict[str, Any] | None, engine_idx: int = 0):
if not transfer_stats_data:
return
for operation, records in transfer_stats_data.items():
assert isinstance(records, list)
for record in records:
assert isinstance(record, dict)
status = str(record["status"])
metrics = self._get_metrics(engine_idx, operation, status)
metrics["time"].observe(float(record["duration_seconds"]))
metrics["calls"].inc()
metrics["keys"].inc(int(record["num_keys"]))
metrics["bytes"].inc(int(record["num_bytes"]))
metrics["failed_keys"].inc(int(record["num_failed_keys"]))