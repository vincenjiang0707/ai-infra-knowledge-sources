source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/nixl/stats/
lastmod: 2026-09-24

@dataclass
class NixlKVConnectorStats(KVConnectorStats):
"""Container for transfer performance metrics."""
def __post_init__(self):
if not self.data:
# Empty container init, no data is passed in.
self.reset()
def reset(self):
# Must be serializable
self.data: dict[str, list[float | int]] = {
"transfer_duration": [],
"post_duration": [],
"bytes_transferred": [],
"num_descriptors": [],
"num_failed_transfers": [],
"num_failed_notifications": [],
"num_failed_handshakes": [],
"num_kv_expired_reqs": [],
}
def record_transfer(self, res: "nixlXferTelemetry"):
# Keep metrics units consistent with rest of the code: time us->s
self.data["transfer_duration"].append(res.xferDuration / 1e6)
self.data["post_duration"].append(res.postDuration / 1e6)
self.data["bytes_transferred"].append(res.totalBytes)
self.data["num_descriptors"].append(res.descCount)
def record_failed_transfer(self):
"""Record a failed NIXL transfer operation."""
self.data["num_failed_transfers"].append(1)
def record_failed_notification(self):
"""Record a failed NIXL notification (send_notif)."""
self.data["num_failed_notifications"].append(1)
def record_failed_handshake(self):
"""Record a failed NIXL handshake."""
self.data["num_failed_handshakes"].append(1)
def record_kv_expired_req(self):
"""Record a request that had its KV blocks expire."""
self.data["num_kv_expired_reqs"].append(1)
def clone_and_reset(self) -> "NixlKVConnectorStats":
old = copy.copy(self)
self.reset()
return old
def is_empty(self) -> bool:
# Do not discard metrics update that are entirely failures related.
return (
self.num_successful_transfers == 0
and len(self.data["num_failed_transfers"]) == 0
and len(self.data["num_failed_notifications"]) == 0
and len(self.data["num_failed_handshakes"]) == 0
and len(self.data["num_kv_expired_reqs"]) == 0
)
def aggregate(self, other: KVConnectorStats) -> KVConnectorStats:
if not other.is_empty():
for k, v in other.data.items():
accumulator = self.data[k]
assert isinstance(accumulator, list)
accumulator.extend(v)
return self
def reduce(self) -> dict[str, int | float]:
# Compute compact representative stats suitable for CLI logging.
# Failure counts are reported on every interval: transfer, handshake
# and notification failures are grouped as sporadic
# lower-transport-layer events, while KV expiry is reported separately
# as it is an actionable autoscaler signal rather than a transport
# issue.
failure_counts = {
"Num failed transfers": len(self.data["num_failed_transfers"])
+ len(self.data["num_failed_handshakes"])
+ len(self.data["num_failed_notifications"]),
"Num KV expired reqs": len(self.data["num_kv_expired_reqs"]),
}
if self.num_successful_transfers == 0:
# Timing / throughput stats only cover successful transfers. If
# all requests in the interval were unsuccessful, the failure
# counts above still surface what happened.
return {
"Num successful transfers": 0,
"Avg xfer time (ms)": 0,
"P90 xfer time (ms)": 0,
"Avg post time (ms)": 0,
"P90 post time (ms)": 0,
"Avg MB per transfer": 0,
"Throughput (MB/s)": 0,
"Avg number of descriptors": 0,
**failure_counts,
}
xfer_time = np.asarray(self.data["transfer_duration"])
post_time = np.asarray(self.data["post_duration"])
# Convert to MB for CLI logging.
mb = np.asarray(self.data["bytes_transferred"]) / 2**20
descs = np.asarray(self.data["num_descriptors"], dtype=np.uint32)
n = len(descs)
assert n == self.num_successful_transfers
total_mb = mb.sum()
avg_mb = total_mb / n
total_time_seconds = xfer_time.sum()
throughput_mb_s = total_mb / total_time_seconds
return {
"Num successful transfers": n,
"Avg xfer time (ms)": round(xfer_time.mean().item() * 1e3, 3),
"P90 xfer time (ms)": round(np.percentile(xfer_time, 90).item() * 1e3, 3),
"Avg post time (ms)": round(post_time.mean().item() * 1e3, 3),
"P90 post time (ms)": round(np.percentile(post_time, 90).item() * 1e3, 3),
"Avg MB per transfer": round(avg_mb.item(), 3),
"Throughput (MB/s)": round(throughput_mb_s.item(), 3),
"Avg number of descriptors": round(descs.mean().item(), 1),
**failure_counts,
}
@property
def num_successful_transfers(self) -> int:
return len(self.data["transfer_duration"])