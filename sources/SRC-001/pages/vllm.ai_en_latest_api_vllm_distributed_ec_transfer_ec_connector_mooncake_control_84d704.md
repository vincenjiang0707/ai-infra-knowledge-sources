source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/mooncake/control/
lastmod: 2026-09-24

class ConsumerControlServer:
"""Expose Consumer reservations and readiness events over ZMQ.
One server runs on every receiving TP rank. The REP channel handles
reservation operations, while a PUSH channel publishes newly ready items
to the Scheduler.
"""
def __init__(
self,
host: str,
port: int,
reserve: Callable[[dict[str, Any]], dict[str, Any]],
status: Callable[[str], dict[str, Any] | None],
complete: Callable[[str, str], tuple[bool, bool]],
cancel: Callable[[str, str, bool, bool], bool],
reap: Callable[[], int],
peer_ports: list[int] | None = None,
device: torch.device | None = None,
drain_ready: Callable[[], list[str]] = lambda: [],
) -> None:
self.host = host
self.port = port
self.peer_ports = peer_ports or [port]
self._device = device
self.event_port: int | None = None
self._reserve = reserve
self._status = status
self._complete = complete
self._cancel = cancel
self._reap = reap
self._drain_ready = drain_ready
self._stop = threading.Event()
self._started = threading.Event()
self._thread: threading.Thread | None = None
self._startup_error: Exception | None = None
def start(self) -> None:
def loop() -> None:
if self._device is not None and self._device.type == "cuda":
torch.accelerator.set_device_index(self._device.index or 0)
context = zmq.Context()
socket = context.socket(zmq.REP)
event_socket = context.socket(zmq.PUSH)
socket.setsockopt(zmq.IPV6, 1)
event_socket.setsockopt(zmq.IPV6, 1)
pending_events: deque[dict[str, Any]] = deque()
def queue_event(event: dict[str, Any]) -> None:
event["shard"] = self.port
if len(pending_events) >= _MAX_PENDING_EVENTS:
dropped = pending_events.popleft()
logger.warning(
"EC Mooncake event backlog full on port %d; dropping "
"readiness for transfer_id=%s",
self.port,
dropped.get("transfer_id"),
)
pending_events.append(event)
def queue_ready(transfer_id: str) -> None:
status = self._status(transfer_id)
if status is not None:
queue_event({"transfer_id": transfer_id, **status})
last_reap_at = time.monotonic()
socket.setsockopt(zmq.RCVTIMEO, 100)
try:
socket.bind(make_zmq_path("tcp", self.host, self.port))
event_socket.bind(make_zmq_path("tcp", self.host, 0))
self.event_port = int(
event_socket.getsockopt(zmq.LAST_ENDPOINT)
.decode()
.rsplit(":", 1)[1]
)
except Exception as e:
self._startup_error = e
self._started.set()
socket.close(linger=0)
event_socket.close(linger=0)
context.term()
return
self._started.set()
try:
while not self._stop.is_set():
while pending_events:
try:
event_socket.send_json(
pending_events[0], flags=zmq.DONTWAIT
)
except zmq.Again:
break
pending_events.popleft()
now = time.monotonic()
if now - last_reap_at >= _RESERVATION_REAP_INTERVAL_SECONDS:
self._reap()
last_reap_at = now
try:
request = socket.recv_json()
except zmq.Again:
continue
except Exception:
# The frame arrived but did not decode. REP still owes a
# reply, so answer before returning to the loop.
logger.exception(
"EC Mooncake control channel on port %d received an "
"undecodable request",
self.port,
)
socket.send_json(
{"ok": False, "error": "malformed control request"}
)
continue
try:
op = request.get("op")
result: Any = None
if op in ("reserve", "reserve_batch"):
items = (
request["items"] if op == "reserve_batch" else [request]
)
results = []
for item in items:
try:
reserved = self._reserve(item)
results.append({"ok": True, "result": reserved})
if reserved.get("ready"):
queue_ready(str(item["transfer_id"]))
except Exception as exc:
results.append({"ok": False, "error": str(exc)})
if op == "reserve_batch":
result = {"items": results}
elif not results[0]["ok"]:
raise RuntimeError(results[0]["error"])
else:
result = results[0]["result"]
elif op == "status":
result = self._status(str(request["transfer_id"]))
elif op == "event_port":
result = self.event_port
elif op == "peers":
result = {"ports": self.peer_ports}
elif op in ("complete", "complete_batch"):
items = (
request["items"]
if op == "complete_batch"
else [request]
)
completions = []
for item in items:
transfer_id = str(item["transfer_id"])
accepted, became_ready = self._complete(
transfer_id, str(item["reservation_id"])
)
for ready_id in self._drain_ready():
queue_ready(ready_id)
completions.append(
{
"completed": accepted,
"became_ready": became_ready,
}
)
if not became_ready:
continue
queue_ready(transfer_id)
result = (
{"items": completions}
if op == "complete_batch"
else completions[0]
)
elif op == "cancel":
result = {
"cancelled": self._cancel(
str(request["transfer_id"]),
str(request.get("reservation_id", "")),
bool(request.get("abandon", False)),
bool(request.get("refresh", False)),
)
}
else:
raise ValueError(f"unknown control op: {op!r}")
socket.send_json({"ok": True, "result": result})
except Exception as e:
socket.send_json({"ok": False, "error": str(e)})
except Exception:
# `finally` closes the sockets and the thread ends, so without
# this every later reserve against this shard would surface
# only as a control timeout with nothing to attribute it to.
logger.exception(
"EC Mooncake control channel on port %d stopped serving",
self.port,
)
raise
finally:
socket.close(linger=0)
event_socket.close(linger=0)
context.term()
self._thread = threading.Thread(
target=loop, name="ec-mooncake-control", daemon=True
)
self._thread.start()
if not self._started.wait(timeout=5):
raise RuntimeError("EC Mooncake control channel failed to start")
if self._startup_error is not None:
raise RuntimeError("EC Mooncake control channel failed to bind") from (
self._startup_error
)
logger.info(
"EC Mooncake control channel listening on tcp://%s:%d (events tcp://%s:%d)",
self.host,
self.port,
self.host,
self.event_port,
)
def close(self) -> None:
if self._thread is None:
return
self._stop.set()
self._thread.join()
self._thread = None