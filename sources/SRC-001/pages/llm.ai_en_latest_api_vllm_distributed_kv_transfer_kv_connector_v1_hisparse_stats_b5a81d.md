source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hisparse/stats/
lastmod: 2026-09-23

Bases: [KVConnectorStats](../../metrics/#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats)


Container for HiSparse hot-buffer residency metrics.

Each list entry is the delta recorded over one device counter snapshot interval, so a list can hold multiple snapshots per logging interval.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hisparse/stats.py`


| @dataclass
class HiSparseKVConnectorStats(KVConnectorStats):
"""Container for HiSparse hot-buffer residency metrics.
Each list entry is the delta recorded over one device counter snapshot
interval, so a list can hold multiple snapshots per logging interval.
"""
def __post_init__(self):
if not self.data:
# Empty container init, no data is passed in.
self.reset()
def reset(self):
# Must be serializable
self.data: dict[str, list[int]] = {
"cache_hits": [],
"cache_misses": [],
"host_to_device_bytes": [],
}
def record_snapshot(self, hits: int, misses: int, host_to_device_bytes: int):
self.data["cache_hits"].append(hits)
self.data["cache_misses"].append(misses)
self.data["host_to_device_bytes"].append(host_to_device_bytes)
def aggregate(self, other: KVConnectorStats) -> KVConnectorStats:
if not other.is_empty():
for k, v in other.data.items():
accumulator = self.data[k]
assert isinstance(accumulator, list)
accumulator.extend(v)
return self
def reduce(self) -> dict[str, int | float]:
# Compute compact representative stats suitable for CLI logging.
return {
"HiSparse hot-buffer hits": sum(self.data["cache_hits"]),
"HiSparse hot-buffer misses": sum(self.data["cache_misses"]),
"HiSparse host-to-device bytes": sum(self.data["host_to_device_bytes"]),
}
def is_empty(self) -> bool:
return all(len(values) == 0 for values in self.data.values())
|