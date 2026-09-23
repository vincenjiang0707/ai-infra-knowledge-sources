source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_connector/
lastmod: 2026-09-23

class MoRIIOConnectorWorker:
"""Implementation of Worker side methods."""
def __init__(
self,
vllm_config: VllmConfig,
engine_id: str,
kv_cache_config: "KVCacheConfig",
):
if not is_moriio_available():
raise RuntimeError(
"MoRIIO is not available. Please ensure the 'mori' package "
"is installed and properly configured."
)
assert vllm_config.kv_transfer_config is not None
self.moriio_config = MoRIIOConfig.from_vllm_config(vllm_config)
self.mode = (
MoRIIOMode.READ if self.moriio_config.read_mode else MoRIIOMode.WRITE
)
logger.info("Initializing MoRIIO worker %s", engine_id)
logging.getLogger("aiter").disabled = True
# Config.
self.vllm_config = vllm_config
assert vllm_config.kv_transfer_config is not None, (
"kv_transfer_config must be set for MoRIIOConnector"
)
self.kv_transfer_config = vllm_config.kv_transfer_config
self.is_producer = self.kv_transfer_config.is_kv_producer
self.layer_to_spec = build_layer_to_spec(kv_cache_config)
# we transfer by layer, but store by kv cache group
self.layer_to_group = dict(kv_cache_config.transfer_group_index_by_layer)
self._transfer_layer_names = set(self.layer_to_group)
_, mamba_transfer_group_ids = _split_kv_cache_group_kinds(kv_cache_config)
self._num_mamba_transfer_groups = len(mamba_transfer_group_ids)
self._mamba_payload_index_by_layer = {
layer_name: payload_index
for payload_index, group_id in enumerate(mamba_transfer_group_ids, start=1)
for layer_name in kv_cache_config.transfer_groups[group_id].layer_names
}
if self.is_producer:
set_role(ROLE.PRODUCER)
else:
set_role(ROLE.CONSUMER)
# mori engine
self._rank = get_world_group().rank
self._local_rank = get_world_group().local_rank
self.tp_rank = self.moriio_config.tp_rank
self.dp_rank = self.moriio_config.dp_rank
self.local_ip = self.moriio_config.local_ip
self.local_kv_port = self.moriio_config.local_kv_port
self.proxy_ip = self.moriio_config.proxy_ip
self.local_ping_port = self.moriio_config.local_ping_port
self.proxy_ping_port = self.moriio_config.proxy_ping_port
self.http_port = self.moriio_config.http_port
self.handshake_port = self.moriio_config.handshake_port
self.notify_port = self.moriio_config.notify_port
self.zmq_context = zmq.Context()
self.metadata_address = (
f"{self.moriio_config.local_ip}:{self.moriio_config.local_ping_port}"
)
self.request_address = (
f"{self.moriio_config.local_ip}:{self.moriio_config.http_port}"
)
self.moriio_engine = None
self._handle_request_thread = None
self._ping_thread = None
self._writer = MoRIIOWriter(self)
# Completions that arrived before transfer_id_to_request_id was populated.
# Retried each step until the mapping is established.
self._unmatched_write_completions: set[str] = set()
# Producer-side READ-mode ACK fan-in. When decode TP is larger than
# prefill TP, multiple decode ranks can read from one prefill rank and
# notify the same transfer_id. Blocks are reusable only after all ACKs.
self._consumer_notification_counts: dict[TransferId, int] = {}
self._completed_consumer_notifications: set[TransferId] = set()
role = "producer" if self.is_producer else "consumer"
engine_suffix = (
f"{self.moriio_config.local_ip}:{self.moriio_config.handshake_port}:"
f"tp{self.tp_rank}:dp{self.dp_rank}"
)
self.moriio_engine = IOEngine(
f"{role}:{engine_suffix}",
IOEngineConfig(
self.moriio_config.local_ip, self.moriio_config.local_kv_port
),
)
logger.debug(
"build MORI IOEngine %s (ip=%s port=%s)",
f"{role}:{engine_suffix}",
self.moriio_config.local_ip,
self.moriio_config.local_kv_port,
)
if self._rank == 0 and self.moriio_config.proxy_ip:
self._ping_thread = threading.Thread(
target=self._ping, args=(self.zmq_context,), daemon=True
)
self._ping_thread.start()
logger.info(
"Initializing MoRIIO Engine, engine = %s, role = %s",
self.moriio_engine,
"producer" if self.is_producer else "consumer",
)
# Agent.
self.moriio_wrapper = MoRIIOWrapper(
tp_rank=self.tp_rank,
dp_rank=self.dp_rank,
transfer_timeout=self.moriio_config.transfer_timeout,
)
self.moriio_wrapper.set_moriio_engine(self.moriio_engine)
backend = (
BackendType.XGMI
if self.moriio_config.backend == "xgmi"
else BackendType.RDMA
)
self.moriio_wrapper.set_backend_type(
backend,
qp_per_transfer=self.moriio_config.qp_per_transfer,
post_batch_size=self.moriio_config.post_batch_size,
num_workers=self.moriio_config.num_workers,
)
self.moriio_wrapper.notify_port = self.moriio_config.notify_port
self.local_kv_cache_metadata: list[bytes] = []
self.local_kv_cache_size: list[int] = []
self.layer_name_to_local_kv_cache_metadata: dict[str, list[bytes]] = {}
self.remote_kv_cache_metadata: list[bytes] = []
self.remote_kv_cache_size: list[int] = []
self.layer_name_to_remote_kv_cache_metadata: dict[str, dict[str, list[Any]]] = (
dict()
)
self.remote_moriio_metadata: dict[EngineId, MoRIIOAgentMetadata] = {}
self.slot_size_bytes = 0
self.load_ready_flag: dict[str, bool] = {}
self.write_ready_flags: dict[str, bool] = {}
self.kv_cache_shape = None
self.block_shape = None
self.kv_element_size = 0
self.kv_cache_shapes: dict[str, torch.Size] = {}
self.block_lens: dict[str, int] = {}
# Map of engine_id -> {agent_name0, agent_name1..}.
self._remote_agents: dict[EngineId, set[str]] = {}
self.side_channel_port: int = (
self.moriio_config.handshake_port
+ get_port_offset(self.dp_rank, self.tp_rank)
)
self.engine_id: EngineId = engine_id
self.world_size = get_tensor_model_parallel_world_size()
self.tp_group = get_tp_group()
# KV Caches and moriio tracking data.
self.kv_caches: dict[str, torch.Tensor] = {}
self.kv_layer_mr_offset: dict[str, int] = {}
self.layer_base_addr_index: dict[str, int] = {}
# Map of engine_id -> kv_caches_base_addr. For TP case, each local
# rank will still only pull from a single remote TP worker.
self.kv_caches_base_addr: dict[EngineId, list[int]] = {}
# Number of MoRIIO regions. Currently one region per cache
# (so 1 per layer for MLA, otherwise 2 per layer)
self.num_regions = 0
self.num_layers = 0
# Map of engine_id -> num_blocks. All ranks in the same deployment will
# have the same number of blocks.
self.dst_num_blocks: dict[EngineId, int] = {}
# In-progress READ transfers: req_id -> {layer_name: [statuses]}.
# A KDA layer posts two reads (conv + ssm), so a layer maps to a list.
self._recving_transfers: defaultdict[ReqId, dict] = defaultdict(dict)
# Values are (remote_host, remote_notify_port, transfer_id).
self._recving_transfers_callback_addr: dict[ReqId, tuple[str, str, str]] = {}
# Monotonic-clock start times for each in-flight recv transfer.
# Used by _pop_done_transfers to abort transfers whose RDMA
# completion is lost, instead of hanging forever.
self._recving_transfers_start: dict[str, float] = {}
# Destination attention blocks per in-flight recv. Failed non-HMA reads
# report these to the scheduler's single-group recovery path.
self._recving_local_blocks: dict[ReqId, list[int]] = {}
# Drained by get_block_ids_with_load_errors.
self._invalid_block_ids: set[int] = set()
# This step's posted reads, awaited before the forward when the
# per-layer barrier cannot run.
self._reads_issued_this_step: list = []
# This step's posted recurrent-state reads. Mamba layers are not
# wrapped by the attention KV-transfer decorator, so wait_for_layer_load
# never fires for them and these must be awaited in start_load_kv.
self._mamba_reads_this_step: list = []
# Track the expiration time of requests that are waiting to be sent.
self._reqs_to_send: dict[ReqId, float] = {}
# Background thread for handling new handshake requests.
self._moriio_handshake_listener_t: threading.Thread | None = None
# Background thread for initializing new MoRIIO handshakes.
self._handshake_initiation_executor = ThreadPoolExecutor(
# MoRIIO is not guaranteed to be thread-safe, limit 1 worker.
max_workers=1,
thread_name_prefix="vllm-moriio-handshake-initiator",
)
self._ready_requests = queue.Queue[tuple[ReqId, ReqMeta]]()
self._handshake_futures: dict[EngineId, Future[set[str]]] = {}
# Protects _handshake_futures and _remote_agents.
self._handshake_lock = threading.RLock()
# Remote engines already covered by the eager pre-forward handshake.
self._eager_handshaked_engines: set[EngineId] = set()
self.block_size = vllm_config.cache_config.block_size
self.model_config = vllm_config.model_config
self.cache_config = vllm_config.cache_config
self.block_window_per_layer: list[int | None] = []
self.use_mla = self.model_config.use_mla
# Hybrid (mamba/KDA) recurrent-state transfer. Populated in
# register_kv_caches when the model has a MambaSpec kv_cache group.
self._has_mamba = False
self._conv_decomp: MambaConvSplitInfo | None = None
self._mamba_offset_templates: dict[str, MambaOffsetTemplate] = {}
# layer_name -> flat session indices (one per registered region:
# 1 for attention, 2 (conv, ssm) for a KDA layer). Built once lazily.
self._region_session_index: dict[str, list[int]] | None = None
self.built_session = False
self.built_write_session: defaultdict[str, list] = defaultdict(list)
backend = get_attn_backend(
self.model_config.get_head_size(),
self.model_config.dtype,
self.cache_config.cache_dtype,
use_mla=self.use_mla,
)
self.transfer_id_to_request_id: dict[TransferId, ReqId] = {}
# READ-mode producer: a decode release-ACK can arrive BEFORE
# start_load_kv populates transfer_id_to_request_id (the notify races
# ahead of the scheduler->worker sync). Buffer such ACKs and retry them
# next get_finished tick instead of dropping them -- dropping loses the
# completion, so the request is never marked done_sending, its KV blocks
# leak, and the prefill KV cache wedges at high concurrency. Buffered
# BEFORE resolve_moriio_transfer_ack, so each ACK is counted exactly once
# (on the tick its mapping exists) -- the heterogeneous-TP ack-counting
# is preserved.
self._pending_unmapped_acks: list = []
# TODO: consider the integration of flashinfer or other backends.
self.backend_name = backend.get_name()
logger.debug("Detected attention backend %s", self.backend_name)
def schedule_write_blocks(
self,
request_id: ReqId,
transfer_id: TransferId,
dst_engine_id: str,
local_block_ids: list[int],
remote_block_ids: list[int] | None,
layer_name: str,
kv_layer: torch.Tensor,
remote_notify_port: int,
remote_ip: str,
) -> None:
"""Schedule a block write operation.
Args:
request_id: Unique identifier for the request
transfer_id: Unique identifier for the transfer
dst_engine_id: Destination engine ID
local_block_ids: Local block IDs to transfer
remote_block_ids: Hint for remote block IDs
layer_name: Name of the layer
kv_layer: KV cache tensor
remote_notify_port: Port for completion notification
remote_ip: IP address of remote node
"""
# synchronization to prevent dirty reads between
# transfer and attention operations
# we can consider removing this synchronization after ibgda is enabled.
# when mori-io supports ibgda functionality
stream = torch.cuda.current_stream()
event = torch.cuda.Event()
event.record(stream)
task = WriteTask(
request_id=request_id,
transfer_id=transfer_id,
dst_engine_id=dst_engine_id,
local_block_ids=local_block_ids,
remote_block_ids_hint=remote_block_ids,
layer_name=layer_name,
event=event,
remote_notify_port=remote_notify_port,
remote_ip=remote_ip,
)
self._writer.schedule_write(task)
def _get_built_session(self, remote_engine_id):
if remote_engine_id not in self.built_write_session:
remote_layer_map = self.layer_name_to_remote_kv_cache_metadata[
remote_engine_id
]
cur_remote_engine_sessions = []
for ln, local_metas in self.layer_name_to_local_kv_cache_metadata.items():
remote_metas = remote_layer_map[ln]
if len(remote_metas) != len(local_metas):
# Sessions are addressed by region index, so a peer that
# registered a different number of regions for this layer
# would not just lose a region to zip(): every later index
# would point into the wrong layer's session.
raise MoRIIOError(
f"peer {remote_engine_id} registered "
f"{len(remote_metas)} region(s) for layer {ln}, this "
f"engine has {len(local_metas)}; the two sides must run "
"the same model and KV cache layout"
)
# One session per registered region, in registration order:
# attention layers have a single region; KDA layers have two
# (conv then ssm). This flat layout is indexed via
# _region_session_indices(layer_name).
for local_meta, remote_meta in zip(local_metas, remote_metas):
unpacked_local_memory_meta = (
self.moriio_wrapper.get_unpack_memory_metadata(local_meta)
)
unpacked_remote_memory_meta = (
self.moriio_wrapper.get_unpack_memory_metadata(remote_meta)
)
cur_remote_engine_sessions.append(
self.moriio_wrapper.build_session(
unpacked_local_memory_meta, unpacked_remote_memory_meta
)
)
self.built_write_session[remote_engine_id] = cur_remote_engine_sessions
return self.built_write_session[remote_engine_id], self.remote_moriio_metadata[
remote_engine_id
]
def _ping(self, zmq_context):
# Use host:port format for http_address (compatible with official router)
http_address = f"{self.request_address}"
# Include host so the router embeds it in the request_id; the connector
# on the other side parses host/ports from there.
zmq_address = (
f"host:{self.local_ip},"
f"handshake:{self.handshake_port},"
f"notify:{self.notify_port}"
)
role = "P" if self.is_producer else "D"
retry_count = 0
index = 1
with zmq_context.socket(zmq.DEALER) as sock:
sock.connect(f"tcp://{self.proxy_ip}:{self.proxy_ping_port}")
while True:
try:
data = {
"type": role, # "P" or "D"
"http_address": http_address,
"zmq_address": zmq_address,
# dp_size/tp_size are not used by the official vLLM router
# (routing operates at the http_address level); they are
# consumed only by the toy proxy server.
"dp_size": self.moriio_config.dp_size,
"tp_size": self.moriio_config.tp_size,
# transfer_mode is included so the router can distinguish
# READ (prefill-then-decode, sequential) from WRITE (concurrent)
# scheduling.
"transfer_mode": self.mode.name,
}
sock.send(msgpack.dumps(data))
# logger.debug(f"Successfully sent ping message #{index}")
retry_count = 0
except ConnectionRefusedError:
logger.info(
"Connection refused: %s:%s -> %s:%s",
self.local_ip,
self.local_ping_port,
self.proxy_ip,
self.proxy_ping_port,
)
retry_count += 1
except OSError as e:
logger.info("OS error when sending ping: %s", e)
retry_count += 1
except Exception as e:
logger.info("Unexpected error when sending ping: %s", e)
retry_count += 1
if retry_count >= MoRIIOConstants.MAX_PING_RETRIES:
logger.error(
"Max retries (%s) exceeded. Stopping ping loop.",
MoRIIOConstants.MAX_PING_RETRIES,
)
raise RuntimeError(
f"Ping failed after {retry_count} retries"
) from e
finally:
time.sleep(MoRIIOConstants.PING_INTERVAL)
index += 1
def shutdown(self):
if hasattr(self, "moriio_wrapper") and self.moriio_wrapper:
self.moriio_wrapper.shutdown()
if hasattr(self, "_handshake_initiation_executor"):
self._handshake_initiation_executor.shutdown(wait=False)
if (
hasattr(self, "_moriio_handshake_listener_t")
and self._moriio_handshake_listener_t
):
self._moriio_handshake_listener_t.join(timeout=0)
if hasattr(self, "zmq_context") and self.zmq_context:
self.zmq_context.destroy(linger=0)
self.zmq_context = None
def __del__(self):
self.shutdown()
@staticmethod
def _moriio_handshake_listener(
metadata: MoRIIOAgentMetadata,
ready_event: threading.Event,
base_port: int,
tp_rank: int,
dp_rank: int,
layer_name_to_local_kv_cache_metadata: dict,
):
"""Background thread for getting new MoRIIO handshakes."""
encoder = msgspec.msgpack.Encoder()
encoded_data = encoder.encode(metadata)
size_in_bytes = len(encoded_data)
logger.debug(
"Size of encoded MoRIIOAgentMetadata: %s bytes", str(size_in_bytes)
)
# Listen for new requests for metadata.
host = "*"
path = make_zmq_path("tcp", host, base_port)
logger.debug("mori handshake starting listening on path: %s", path)
with zmq_ctx(zmq.ROUTER, path) as sock:
ready_event.set()
while True:
identity, msg = sock.recv_multipart()
if (
msg != MoRIIOConstants.GET_META_MSG
and msg != MoRIIOConstants.POP_DONE_RECV
):
logger.error("Connection listener got unexpected message")
raise HandshakeError("handshake failed, unexpected msg type")
elif msg == MoRIIOConstants.GET_META_MSG:
sock.send_multipart(
(identity, b"", encoded_data)
) # send local mori io engine meta data
logger.debug("MoRIIO handshake listener sent metadata")
# now we send tensor meta data for each block
buf = msgpack.dumps(layer_name_to_local_kv_cache_metadata)
sock.send_multipart((identity, b"", buf))
elif msg == MoRIIOConstants.POP_DONE_RECV:
_, req_id = sock.recv_multipart()
logger.debug(
"MoRIIO handshake listener received done recv for req",
req_id.decode(),
)
def _moriio_handshake(
self,
host: str,
port: int,
remote_tp_size: int,
expected_engine_id: str,
remote_dp_rank: int = 0,
remote_tp_rank: int | None = None,
) -> set[str]:
"""Do a MoRIIO handshake with a remote instance.
remote_tp_rank: explicit remote TP index to dial. Flexible-read callers
pass the chosen prefill TP rank so the handshake, the (dp, tp) session
key and the notify port all address the SAME rank. None falls back to the
local-rank mapping _remote_tp_rank -- byte-identical for callers not yet
TP-aware.
"""
start_time = time.perf_counter()
# NOTE(rob): we need each rank to have a unique port. This is
# a hack to keep us moving. We will switch when moving to etcd
# or where we have a single ZMQ socket in the scheduler.
dial_tp_rank = (
self._remote_tp_rank(remote_tp_size)
if remote_tp_rank is None
else int(remote_tp_rank)
)
port_offset = get_port_offset(remote_dp_rank, dial_tp_rank, remote_tp_size)
path = make_zmq_path("tcp", host, port + port_offset)
logger.debug("handshake Querying metadata on path: %s", path)
# Send query for the request.
with zmq_ctx(zmq.DEALER, path) as sock:
logger.debug("prepare send msg INSTAZNCE: %s", path)
sock.send(MoRIIOConstants.GET_META_MSG)
received_frame = sock.recv_multipart()
if len(received_frame) != 2 or received_frame[0] != b"":
raise HandshakeError(f"Unexpected frame! {received_frame = }")
metadata_bytes = received_frame[1]
decoder = msgspec.msgpack.Decoder(MoRIIOAgentMetadata)
metadata = decoder.decode(metadata_bytes)
got_metadata_time = time.perf_counter()
logger.info(
"MoRIIO handshake: get metadata took: %s",
got_metadata_time - start_time,
)
self.moriio_wrapper.remote_engine_ip = host
remote_agent_name = self.moriio_wrapper.register_remote_engine(
metadata.agent_metadata
)
logger.debug(
"MoRIIO handshake: registered"
"remote agent %s for engine ID %s, path = %s",
remote_agent_name,
expected_engine_id,
path,
)
if len(self.local_kv_cache_metadata) > 0:
logger.warning(
"len(self.local_kv_cache_metadata) = %s,"
"maybe you didnt clear this buffer correctly",
len(self.local_kv_cache_metadata),
)
self.local_kv_cache_metadata = []
if len(self.remote_kv_cache_metadata) > 0:
logger.warning(
"len(self.remote_kv_cache_metadata) = %s,"
"maybe you didnt clear this buffer correctly",
len(self.remote_kv_cache_metadata),
)
self.remote_kv_cache_metadata = []
received_frame = sock.recv_multipart()
if len(received_frame) != 2 or received_frame[0] != b"":
raise HandshakeError(f"unexpected frame! {received_frame = }")
buf = received_frame[1]
self.layer_name_to_remote_kv_cache_metadata[expected_engine_id] = (
msgpack.loads(buf)
)
self.remote_moriio_metadata[expected_engine_id] = metadata
setup_agent_time = time.perf_counter()
logger.debug(
"MoRIIO handshake: add agent took: %s",
setup_agent_time - got_metadata_time,
)
return {remote_agent_name}
def _remote_tp_rank(self, remote_tp_size: int) -> int:
# 0/unknown remote TP == homogeneous (avoids collapsing all ranks to 0).
if remote_tp_size == 0:
remote_tp_size = self.world_size
return get_moriio_remote_tp_rank(self.tp_rank, self.world_size, remote_tp_size)
def _background_moriio_handshake(
self, req_id: ReqId, remote_engine_id: EngineId, meta: ReqMeta
):
# Do MoRIIO handshake in background and add to _ready_requests when done.
fut = None
if remote_engine_id is not None:
fut = self._handshake_futures.get(remote_engine_id)
if fut is None:
host = meta.remote_host
port = int(meta.remote_handshake_port)
tp_size = int(meta.tp_size)
remote_dp_size = int(meta.remote_dp_size)
# Wide-EP multi-pod: remote DP ranks span pods at different IPs
# (ranks per pod = dp_local), so resolve the host per cur_dp_rank
# below instead of using a single host for all ranks.
pod_hosts = list(meta.multi_pod_hosts) if meta.multi_pod_hosts else [host]
remote_dp_size_local = int(meta.remote_dp_size_local) or remote_dp_size
def request_ready(_f: Future[Any], entry=(req_id, meta)):
logger.info("MoRIIO handshake done for request %s", req_id)
self._ready_requests.put(entry)
self.load_ready_flag[remote_engine_id] = True
self.write_ready_flags[remote_engine_id] = True
fut_list = []
# In dp(prefill)<->dp(decode) communication, we require an all-to-all handshake.
for cur_dp_rank in range(remote_dp_size):
dp_engine_id = self.get_engine_name_with_dp(remote_engine_id, cur_dp_rank)
_pod_idx = pod_index(cur_dp_rank, remote_dp_size_local)
if _pod_idx >= len(pod_hosts):
_pod_idx = 0
_per_rank_host = pod_hosts[_pod_idx]
# The handshake port offset must use the per-pod local rank, since
# each pod binds sockets only for its local ranks; dp_engine_id
# keeps the global rank for uniqueness. Single-pod is bit-identical.
_per_rank_local_dp = fold_local_rank(cur_dp_rank, remote_dp_size_local)
future = self._handshake_initiation_executor.submit(
self._moriio_handshake,
_per_rank_host,
port,
tp_size,
dp_engine_id,
_per_rank_local_dp,
)
fut_list.append(future)
def done_callback(f: Future[set[str]], eid=dp_engine_id):
with self._handshake_lock:
self._handshake_futures.pop(eid, None)
try:
self._remote_agents[eid] = f.result()
except Exception:
logger.exception("Handshake with %s failed", eid)
future.add_done_callback(done_callback)
self._handshake_futures[dp_engine_id] = future
# fut = fut_list
def wait_all_dp():
for future in fut_list:
future.result()
return True
all_done_future = self._handshake_initiation_executor.submit(wait_all_dp)
all_done_future.add_done_callback(request_ready)
def _is_mla_cache_layer(self, layer_name: str) -> bool:
return is_mla_cache_layer(self.layer_to_spec, layer_name)
def _is_mamba_layer(self, layer_name: str) -> bool:
"""True for a hybrid/KDA layer backed by a packed state page."""
return isinstance(self.layer_to_spec.get(layer_name), MambaSpec)
@staticmethod
def _contiguous_byte_alias(tensor: torch.Tensor) -> torch.Tensor:
"""Return a contiguous uint8 view over ``tensor``'s full byte extent.
KDA conv/ssm caches are slot-strided views (``stride(0)`` may exceed the
per-slot element count), so they are non-contiguous and cannot be passed
to ``register_torch_tensor``. This aliases the same storage (zero-copy,
identical ``data_ptr``) as a flat uint8 tensor spanning
``shape[0] * stride(0)`` elements -- the full slot-strided extent that
transfer offsets (``slot * stride(0) * elem``) address.
"""
esz = tensor.element_size()
storage_nbytes = tensor.untyped_storage().nbytes()
offset_bytes = tensor.storage_offset() * esz
extent_bytes = tensor.shape[0] * tensor.stride(0) * esz
# Clamp to the bytes remaining from the view's storage offset. In a
# packed page, the ssm view starts after conv, so its slot-strided extent
# would otherwise run past the backing allocation.
extent_bytes = min(extent_bytes, storage_nbytes - offset_bytes)
assert extent_bytes > 0, (
"KDA byte alias empty: storage_offset="
f"{tensor.storage_offset()} * esz={esz} >= "
f"storage_nbytes={storage_nbytes}"
)
alias = torch.empty(0, dtype=torch.uint8, device=tensor.device)
alias.set_(
tensor.untyped_storage(),
tensor.storage_offset() * esz,
(extent_bytes,),
(1,),
)
return alias
def _get_layer_transfer_geometry(
self, layer_name: str, remote_num_blocks: int | None = None
) -> LayerTransferGeometry:
geometry = get_layer_transfer_geometry(
layer_name,
self.kv_caches[layer_name],
self.layer_to_spec,
remote_num_blocks,
)
# get_layer_transfer_geometry also serves mamba layers, whose geometry
# is a different NamedTuple with no block fields. Every caller here is
# on the attention path (mamba layers return before reaching it), so
# narrow the type instead of leaking the union.
assert isinstance(geometry, LayerTransferGeometry), (
f"layer {layer_name} is a mamba layer; use get_mamba_transfer_geometry"
)
return geometry
def _iter_layer_registration_regions(
self, layer_name: str
) -> list[tuple[torch.Tensor, int]]:
return iter_layer_registration_regions(
layer_name,
self.kv_caches[layer_name],
self.layer_to_spec,
)
def _build_shared_kv_mr(
self, kv_caches: dict[str, torch.Tensor]
) -> tuple[torch.Tensor, dict[str, int]]:
page_size = 4096
backing = next(iter(kv_caches.values())).view(torch.uint8)
nbytes = backing.untyped_storage().nbytes()
base = torch.as_strided(backing, (nbytes,), (1,), 0)
ptr = base.data_ptr()
slack = ptr % page_size
end = 0
for layer_name in kv_caches:
_, region_len = next(
iter(self._iter_layer_registration_regions(layer_name))
)
end = max(end, kv_caches[layer_name].data_ptr() - ptr + region_len)
reg_nbytes = ((slack + end + page_size - 1) // page_size) * page_size
if reg_nbytes > nbytes:
raise ValueError(
f"shared KV backing too small for page-aligned MR: "
f"need {reg_nbytes}, have {nbytes}"
)
reg = torch.as_strided(base, (reg_nbytes,), (1,), 0 if slack == 0 else -slack)
mr_ptr = reg.data_ptr()
return reg, {
name: cache.data_ptr() - mr_ptr for name, cache in kv_caches.items()
}
def _remote_layer_mr_offset(
self,
layer_name: str,
remote_moriio_meta: MoRIIOAgentMetadata,
remote_engine_id: EngineId | None,
) -> int:
if not self.kv_layer_mr_offset or not remote_engine_id:
return 0
idx = self.layer_base_addr_index[layer_name]
metas = self.layer_name_to_remote_kv_cache_metadata.get(
remote_engine_id, {}
).get(layer_name)
if not metas or idx >= len(remote_moriio_meta.kv_caches_base_addr):
return 0
mr_base = self.moriio_wrapper.get_unpack_memory_metadata(metas[0]).data
return remote_moriio_meta.kv_caches_base_addr[idx] - mr_base
def register_kv_caches(self, kv_caches: dict[str, torch.Tensor]):
"""Register the KV Cache data in moriio."""
kv_caches = {
layer_name: kv_cache
for layer_name, kv_cache in kv_caches.items()
if layer_name in self._transfer_layer_names
}
if not kv_caches:
raise MoRIIOError("MoRIIO has no transfer-enabled KV cache layers")
self.kv_caches = kv_caches # layer name to kv cache
self._has_mamba = any(
self._is_mamba_layer(layer_name) for layer_name in kv_caches
)
if self._has_mamba and self.mode == MoRIIOMode.WRITE:
# WRITE needs a distinct conv/ssm transfer plan. Reject before
# allocating or registering any regions rather than silently
# serving a zero recurrent state.
raise MoRIIOError(
"MoRIIO hybrid (mamba/KDA) transfer is implemented for READ "
"mode only; set kv_connector_extra_config.read_mode=true "
"for hybrid models"
)
if self._has_mamba:
mamba_specs = [
cast(MambaSpec, self.layer_to_spec[layer_name])
for layer_name in kv_caches
if self._is_mamba_layer(layer_name)
]
mamba_spec = _validate_mamba_specs(mamba_specs)
assert mamba_spec is not None
from vllm.model_executor.layers.mamba.mamba_utils import (
is_conv_state_dim_first,
)
if not is_conv_state_dim_first():
raise MoRIIOError(
"MoRIIO KDA conv transfer requires the DS (dim-first) "
"state layout; set VLLM_SSM_CONV_STATE_LAYOUT=DS"
)
self._conv_decomp = derive_mamba_conv_split(mamba_spec, self.world_size)
# KDA layers use packed pages with different geometry; only record
# attention tensor shapes here.
self.kv_cache_shapes = {
layer_name: kv_cache.shape
for layer_name, kv_cache in kv_caches.items()
if not self._is_mamba_layer(layer_name)
}
# Geometry selection must pick an attention layer (never a KDA tuple):
# prefer a standard 5-D K/V layer, else the first attention layer.
attn_items = [
(layer_name, kv_cache)
for layer_name, kv_cache in kv_caches.items()
if not self._is_mamba_layer(layer_name)
]
first_layer_name, first_kv_cache = next(
(
(layer_name, kv_cache)
for layer_name, kv_cache in attn_items
if (
not self._is_mla_cache_layer(layer_name)
and len(kv_cache.shape) == 5
and (kv_cache.shape[0] == 2 or kv_cache.shape[1] == 2)
)
),
attn_items[0] if attn_items else next(iter(kv_caches.items())),
)
kv_elem_size = first_kv_cache.element_size()
use_mla = self._is_mla_cache_layer(first_layer_name)
first_geometry = self._get_layer_transfer_geometry(first_layer_name)
if use_mla:
# MLA case.
block_rank = 2 # [block_size, latent_dim]
block_shape = first_kv_cache.shape[-block_rank:]
else:
# [2, num_blocks, ...] or [num_blocks, 2, ...]
block_rank = 3 # [block_size, kv_heads, head_dim]
block_shape = first_kv_cache.shape[-block_rank:]
self.num_blocks = first_geometry.num_blocks
self.slot_size_bytes = first_geometry.slot_size_bytes
if first_geometry.block_size != self.block_size:
# DeepSeek-V3 / MLA backends (e.g. FlashMLA) override the
# configured block_size at attention-layer creation time, so
# the KV cache tensor is laid out with a different (usually
# larger) block_size than vllm_config.cache_config.block_size.
# Trust the actual tensor shape and reconcile.
logger.info(
"KV cache block_size=%d differs from config block_size=%d; "
"using actual tensor shape (attention backend override).",
first_geometry.block_size,
self.block_size,
)
self.block_size = first_geometry.block_size
# block size in bytes
self.block_len = first_geometry.block_len
self.kv_cache_shape = first_kv_cache.shape
self.block_shape = block_shape
self.kv_element_size = kv_elem_size
self.dst_num_blocks[self.engine_id] = self.num_blocks
kv_caches_base_addr = []
caches_data = []
self.layer_base_addr_index = {}
base_addr_idx = 0
hma_enabled = (
not self.vllm_config.scheduler_config.disable_hybrid_kv_cache_manager
)
for layer_name in kv_caches:
self.layer_base_addr_index[layer_name] = base_addr_idx
if self._is_mamba_layer(layer_name):
# KDA layer: two whole-tensor regions (conv, ssm); no block-size
# geometry (recurrent state is per-slot, not paged).
for cache, region_len in self._iter_layer_registration_regions(
layer_name
):
base_addr = cache.data_ptr()
caches_data.append((base_addr, region_len, cache.device.index, ""))
kv_caches_base_addr.append(base_addr)
base_addr_idx += 1
continue
geometry = self._get_layer_transfer_geometry(layer_name)
if hma_enabled:
if geometry.block_len != self.block_len:
raise ValueError(
"MoRIIO KV cache block length mismatch for layer "
f"{layer_name}: {geometry.block_len} != {self.block_len}"
)
elif geometry.block_size != self.block_size:
raise ValueError(
"MoRIIO KV cache block size mismatch for layer "
f"{layer_name}: {geometry.block_size} != {self.block_size}"
)
# num_blocks is advertised as a single scalar to the peer, so must it
# be uniform
if geometry.num_blocks != self.num_blocks:
raise ValueError(
"MoRIIO KV cache num_blocks mismatch for layer "
f"{layer_name}: {geometry.num_blocks} != {self.num_blocks}"
)
self.block_lens[layer_name] = geometry.block_len
for cache, region_len in self._iter_layer_registration_regions(layer_name):
base_addr = cache.data_ptr()
caches_data.append((base_addr, region_len, cache.device.index, ""))
kv_caches_base_addr.append(base_addr)
base_addr_idx += 1
shared_backing = (
all(isinstance(t, torch.Tensor) for t in kv_caches.values())
and len({id(t.untyped_storage()) for t in kv_caches.values()}) == 1
)
shared_mr = None
if shared_backing:
reg_tensor, self.kv_layer_mr_offset = self._build_shared_kv_mr(kv_caches)
shared_mr = self.moriio_wrapper.register_local_tensor(reg_tensor)
# Say it out loud when the groups disagree. This is expected on a hybrid
# model and used to be fatal, so a run that silently had one page size
# and a run that has three should not look identical in the log.
distinct_block_lens = sorted(set(self.block_lens.values()))
if len(distinct_block_lens) > 1:
logger.info(
"MoRIIO registered %d attention layers with %d distinct block "
"lengths (bytes): %s; transfer sizes and strides are per layer, "
"and %d is the page advertised to the peer.",
len(self.block_lens),
len(distinct_block_lens),
distinct_block_lens,
self.block_len,
)
for layer_name, kv_cache in kv_caches.items():
if layer_name not in self.layer_name_to_local_kv_cache_metadata:
self.layer_name_to_local_kv_cache_metadata[layer_name] = []
if self._is_mamba_layer(layer_name):
# Register conv and ssm as two whole-tensor regions, appending
# both metadata blobs (order: conv then ssm) so the session
# layout matches iter_layer_registration_regions. conv/ssm are
# slot-strided views and are not contiguous, which
# register_torch_tensor rejects; register a contiguous uint8
# alias over each tensor's full byte extent instead (zero-copy:
# same storage and data_ptr).
conv, ssm = kda_conv_ssm(
kv_cache, cast(MambaSpec, self.layer_to_spec[layer_name])
)
logger.debug(
"MoRIIO KDA register %s: conv shape=%s stride=%s contig=%s "
"storage_nbytes=%s ; ssm shape=%s stride=%s contig=%s "
"storage_nbytes=%s",
layer_name,
tuple(conv.shape),
tuple(conv.stride()),
conv.is_contiguous(),
conv.untyped_storage().nbytes(),
tuple(ssm.shape),
tuple(ssm.stride()),
ssm.is_contiguous(),
ssm.untyped_storage().nbytes(),
)
for tensor in (conv, ssm):
alias = self._contiguous_byte_alias(tensor)
meta = self.moriio_wrapper.register_local_tensor(alias)
self.layer_name_to_local_kv_cache_metadata[layer_name].append(meta)
self.local_kv_cache_size.append(alias.numel())
else:
moriio_mem_metadata = shared_mr or (
self.moriio_wrapper.register_local_tensor(kv_cache)
)
self.layer_name_to_local_kv_cache_metadata[layer_name].append(
moriio_mem_metadata
)
self.local_kv_cache_size.append(
kv_cache.nelement() * kv_cache.element_size()
)
self.kv_caches_base_addr[self.engine_id] = kv_caches_base_addr
self.num_regions = len(caches_data)
self.num_layers = len(self.kv_caches.keys())
# Report the prevalidated KDA decomposition after registration.
if self._has_mamba:
assert self._conv_decomp is not None
logger.info(
"MoRIIO registered %d KDA (conv+ssm) layer(s); ssm sizes=%s",
sum(1 for ln in kv_caches if self._is_mamba_layer(ln)),
self._conv_decomp.ssm_sizes,
)
# Optimization for models with local attention (Llama 4)
if self.vllm_config.model_config.hf_config.model_type == "llama4":
from transformers import Llama4TextConfig
assert isinstance(
self.vllm_config.model_config.hf_text_config, Llama4TextConfig
)
llama4_config = self.vllm_config.model_config.hf_text_config
no_rope_layers = llama4_config.no_rope_layers
chunk_size = llama4_config.attention_chunk_size
chunk_block_size = math.ceil(chunk_size / self.block_size)
for layer_idx in range(self.num_layers):
# no_rope_layers[layer_idx] == 0 means NoPE (global)
# Any other value means RoPE (local chunked)
is_local_attention = no_rope_layers[layer_idx] != 0
block_window = chunk_block_size if is_local_attention else None
self.block_window_per_layer.append(block_window)
logger.debug(
"Llama 4 block window per layer mapping: %s",
self.block_window_per_layer,
)
assert len(self.block_window_per_layer) == self.num_layers
metadata = MoRIIOAgentMetadata(
engine_id=self.engine_id,
agent_metadata=self.moriio_wrapper.get_agent_metadata(),
kv_caches_base_addr=self.kv_caches_base_addr[self.engine_id],
num_blocks=self.num_blocks,
block_len=self.block_len,
attn_backend_name=self.backend_name,
)
ready_event = threading.Event()
self._moriio_handshake_listener_t = threading.Thread(
target=self._moriio_handshake_listener,
args=(
metadata,
ready_event,
self.side_channel_port,
self.tp_rank,
self.dp_rank,
self.layer_name_to_local_kv_cache_metadata,
),
daemon=True,
name="moriio_handshake_listener",
)
self._moriio_handshake_listener_t.start()
ready_event.wait() # Wait for listener ZMQ socket to be ready.
self.moriio_wrapper.async_wait_reqid()
def get_finished(self) -> tuple[set[str], set[str]]:
"""Get requests that are done sending or recving on this specific worker.
The scheduler process (via the MultiprocExecutor) will use this output
to track which workers are done.
"""
done_sending, done_recving = set(), set()
if self.is_producer:
# pop_finished_req_ids returns release ACKs sent by decode. Keep
# duplicate ACKs because heterogeneous TP can fan multiple decode
# ranks into one prefill rank for the same transfer_id.
# Combine freshly-arrived ACKs with any buffered from prior ticks
# whose transfer_id wasn't mapped yet (notify raced ahead of
# start_load_kv); retry the lookup every tick. Buffered before
# resolve_moriio_transfer_ack so each ACK is counted exactly once.
finished_acks = self._pending_unmapped_acks + list(
self.moriio_wrapper.pop_finished_req_ids()
)
self._pending_unmapped_acks = []
resolved_transfer_ids: set[TransferId] = set()
for ack in finished_acks:
transfer_id = ack if isinstance(ack, str) else ack.transfer_id
if transfer_id not in self.transfer_id_to_request_id:
# Mapping not populated yet -- buffer and retry next tick,
# do NOT drop (dropping leaks producer KV at high conc and
# wedges the prefill).
self._pending_unmapped_acks.append(ack)
continue
resolved_transfer_id = resolve_moriio_transfer_ack(
ack,
producer_tp_size=self.world_size,
live_transfer_ids=self.transfer_id_to_request_id.keys(),
notification_counts=self._consumer_notification_counts,
completed_transfer_ids=(self._completed_consumer_notifications),
)
if resolved_transfer_id is not None:
resolved_transfer_ids.add(resolved_transfer_id)
done_sending = {
self.transfer_id_to_request_id[xfer_id]
for xfer_id in resolved_transfer_ids
}
else:
if self.mode == MoRIIOMode.WRITE:
fresh = self.moriio_wrapper.pop_finished_write_req_ids()
# Accumulate with any completions that arrived before their
# transfer_id was registered in transfer_id_to_request_id.
self._unmatched_write_completions |= fresh
done_recving = self._unmatched_write_completions
else:
# READ mode: the scheduler treats KV loads as synchronous
# (load_kv_async=False), so requests go directly to RUNNING
# instead of WAITING_FOR_REMOTE_KVS. We still call
# _pop_done_transfers() to send the notify to the prefill
# side and clean up internal state, but we must NOT report
# these as done_recving because the scheduler doesn't
# expect a finished_recving signal for RUNNING requests.
self._pop_done_transfers()
done_recving = {
self.transfer_id_to_request_id[id]
for id in filter(
lambda id: id in self.transfer_id_to_request_id, done_recving
)
}
if self.mode == MoRIIOMode.WRITE and not self.is_producer:
# Remove the ones we successfully matched; leave unmatched for retry.
matched_xfer_ids = {
id
for id in self._unmatched_write_completions
if id in self.transfer_id_to_request_id
}
self._unmatched_write_completions -= matched_xfer_ids
return done_sending, done_recving
def wait_for_layer_load(self, layer_name: str) -> None:
"""Block until all in-flight READs of this layer have landed.
A host-side blocking wait must not run during full-graph capture.
"""
if self.is_producer or self.mode != MoRIIOMode.READ:
return
if get_forward_context().cudagraph_runtime_mode == CUDAGraphMode.FULL:
return
with self.moriio_wrapper.lock:
pending = [
status
for status_by_layer in self._recving_transfers.values()
for status in status_by_layer.get(layer_name, ())
]
if not pending:
return
try:
self.moriio_wrapper.waiting_for_transfer_complete(pending)
except TransferError:
if self._has_mamba:
logger.exception(
"MoRIIO hybrid READ failed before layer %s; aborting the "
"forward because HMA load-error recovery is unsupported.",
layer_name,
)
raise
logger.warning(
"MoRIIO READ barrier did not complete for layer %s; proceeding "
"to transfer cleanup.",
layer_name,
exc_info=True,
)
def _pop_done_transfers(self) -> set[str]:
done_req_ids: set[str] = set()
_xfer_timeout = self.moriio_config.recv_abort_timeout
with self.moriio_wrapper.lock:
to_remove = []
for req_id, status_by_layer in self._recving_transfers.items():
# Every layer's read must land before the request is complete,
# so the whole batch is polled rather than just the newest
# status.
statuses = [
status
for layer_statuses in status_by_layer.values()
for status in layer_statuses
]
state = self.moriio_wrapper.poll_transfer_batch(statuses)
if statuses and state is TransferBatchState.DONE:
host, port, xfer_id = self._recving_transfers_callback_addr[req_id]
done_req_ids.add(xfer_id)
self.moriio_wrapper.send_notify(
xfer_id,
host,
port,
message_type="release",
message_fields={"consumer_tp_size": self.world_size},
)
to_remove.append(req_id)
elif state is TransferBatchState.FAILED:
failed_status = next(
(status for status in statuses if status.Failed()), None
)
logger.error(
"RDMA transfer failed for request %s: %s (code=%s). "
"Notifying prefill to free blocks and recording the "
"load error where scheduler recovery is supported.",
req_id,
failed_status.Message() if failed_status else "unknown",
failed_status.Code() if failed_status else "unknown",
)
self._record_failed_recv(req_id)
host, port, xfer_id = self._recving_transfers_callback_addr[req_id]
try:
self.moriio_wrapper.send_notify(
xfer_id,
host,
port,
message_type="release",
message_fields={"consumer_tp_size": self.world_size},
)
except Exception:
logger.exception(
"Failed to send error notification for request %s",
req_id,
)
to_remove.append(req_id)
# Deliberately not in done_req_ids: the decode KV is
# incomplete, so this is a load error rather than a
# completion.
elif req_id in self._recving_transfers_start:
# Abort still-in-flight transfers that exceed the
# configured deadline. Otherwise a lost RDMA
# completion would leave the decode worker hung
# indefinitely on this request.
_age = time.monotonic() - self._recving_transfers_start[req_id]
if _age > _xfer_timeout:
logger.error(
"RDMA read TIMED OUT for req %s after %.1fs "
"(kv_connector_extra_config.recv_abort_timeout=%.0f)",
req_id,
_age,
_xfer_timeout,
)
self._record_failed_recv(req_id)
to_remove.append(req_id)
for req_id in to_remove:
del self._recving_transfers[req_id]
del self._recving_transfers_callback_addr[req_id]
self._recving_transfers_start.pop(req_id, None)
self._recving_local_blocks.pop(req_id, None)
return done_req_ids
def _await_reads_issued_this_step(self) -> None:
"""Step-level READ barrier, for the reads no per-layer barrier covers.
load_kv_async=False promises the KV is in place before the forward runs.
wait_for_layer_load keeps that promise per layer, letting early layers
overlap later transfers, but it only fires for layers that go through
the attention KV-transfer decorator. Two cases fall through it:
* mamba/KDA layers have no such hook at all, so their conv+ssm reads
would otherwise be consumed while still in flight;
* under CUDAGraphMode.FULL a host-side blocking wait is illegal
anywhere in the graph, so every read is awaited here instead.
start_load_kv runs outside the graph, so blocking here is safe.
Attention reads keep their per-layer overlap in the non-FULL case.
Attention-only failures are reported via
get_block_ids_with_load_errors. Hybrid failures are re-raised because
the scheduler's recovery path does not support multiple cache groups;
this fails the step closed instead of running forward with incomplete
recurrent state.
"""
all_statuses = self._reads_issued_this_step
self._reads_issued_this_step = []
mamba_statuses = self._mamba_reads_this_step
self._mamba_reads_this_step = []
if get_forward_context().cudagraph_runtime_mode == CUDAGraphMode.FULL:
statuses = all_statuses
else:
statuses = mamba_statuses
if not statuses:
return
try:
self.moriio_wrapper.waiting_for_transfer_complete(statuses)
except TransferError:
if self._has_mamba:
logger.exception(
"MoRIIO hybrid READ failed before the forward; aborting "
"because HMA load-error recovery is unsupported."
)
raise
logger.exception(
"MoRIIO reads did not complete before the forward; proceeding "
"to transfer cleanup."
)
def _record_failed_recv(self, req_id: ReqId) -> None:
"""Hand a failed attention-only read to scheduler recovery.
The scheduler's invalid-block recovery currently assumes exactly one
KV cache group. Reporting IDs for a hybrid request would crash it while
unpacking the request's groups, so match NIXL and keep HMA failures out
of this API until scheduler recovery carries group identity.
"""
if self._has_mamba:
return
self._invalid_block_ids.update(self._recving_local_blocks.get(req_id, ()))
def get_block_ids_with_load_errors(self) -> set[int]:
"""Drain the blocks whose read failed, for the scheduler to recompute."""
invalid, self._invalid_block_ids = self._invalid_block_ids, set()
return invalid
def save_kv_layer(
self,
metadata: MoRIIOConnectorMetadata,
layer_name: str,
kv_layer: torch.Tensor,
attn_metadata: "AttentionMetadata | None",
**kwargs,
):
if not self.is_producer:
return
if self.mode == MoRIIOMode.READ:
return
remote_engine_id = None
for req_id, meta in metadata.reqs_to_save.items():
# we only need to check if dp0 in rank
remote_engine_id = (
str(meta.remote_host) + ":" + str(meta.remote_handshake_port)
)
meta.remote_engine_id = remote_engine_id
dp0_remote_engine_id = self.get_engine_name_with_dp(remote_engine_id, 0)
if dp0_remote_engine_id not in self._remote_agents:
# Initiate handshake with remote engine to exchange metadata.
with self._handshake_lock:
if remote_engine_id not in self._remote_agents:
self._background_moriio_handshake(
req_id, remote_engine_id, meta
)
continue
self._write_blocks_for_req(req_id, meta, layer_name, kv_layer)
if remote_engine_id is None:
return
_deadline = time.monotonic() + self.moriio_config.transfer_timeout
while True:
if (
self._ready_requests.empty()
and remote_engine_id not in self.write_ready_flags
):
if time.monotonic() > _deadline:
logger.warning(
"Timed out waiting for write_ready_flags[%s]; "
"adjust with kv_connector_extra_config.transfer_timeout",
remote_engine_id,
)
break
time.sleep(0.001)
continue
elif not self._ready_requests.empty() and (
remote_engine_id in self.write_ready_flags
):
self._write_blocks_for_req(
*self._ready_requests.get_nowait(), layer_name, kv_layer
)
break
else:
break
def get_engine_name_with_dp(self, engine_name, dp_rank):
return f"{engine_name}_dp{dp_rank}"
def get_engine_name_with_dp_tp(self, engine_name, dp_rank, tp_rank):
# Per-(dp, tp) session key. The flexible mirror read keys sessions per
# (dp, tp) so one decode worker can hold a session to EACH prefill TP
# rank and spread reads across them; other configs keep the DP-only key.
return f"{engine_name}_dp{dp_rank}_tp{tp_rank}"
def _eager_handshake_all_dp_ranks(self, metadata: MoRIIOConnectorMetadata) -> None:
"""Handshake EVERY remote prefill DP rank BEFORE the decode forward pass,
identically across all local TP workers.
Why this exists (the deadlock it prevents): with heterogeneous DP prefill
a decode TP worker reads KV from whichever prefill DP rank owns the
request, so across requests every worker must reach several prefill DP
ranks. The decode forward issues per-layer TP collectives (e.g. an
all-gather) that all local TP workers must enter together. If the
handshakes are left to fire lazily on the read path, the workers diverge:
a worker whose target rank is already cached races ahead into the forward
collective while a peer is still blocked in a handshake recv(). The first
worker then waits inside the collective for the stuck peer -> 600s NCCL
timeout / hang. This was observed directly with mixed TP<->DP configs.
Fix: complete ALL prefill-DP-rank handshakes for every referenced remote
engine HERE, before any read enters the forward, so no worker is still
handshaking once its peers reach a collective. Fires ONCE per remote
engine (first contact), gated by _eager_handshaked_engines. The engine
set comes from scheduler-built metadata (identical on every TP worker),
so all workers run the same handshakes in the same order and reach the
all-reduce barrier below together.
Failure handling: handshake exceptions are caught, never raised before
the collective (raising early would hang the peers still waiting for it).
Every worker reaches the all-reduce(MIN) vote; if ANY worker failed, ALL
raise the same error AFTER the collective, so the step fails fast and
uniformly in ~seconds instead of one rank hanging the forward for 600s.
"""
import torch.distributed as dist
# Distinct remote engines referenced this step, in metadata (==
# scheduler) order so every TP worker iterates engines identically.
engines: dict[str, ReqMeta] = {}
for _req_id, meta in metadata.reqs_to_recv.items():
remote_engine_id = (
str(meta.remote_host) + ":" + str(meta.remote_handshake_port)
)
engines.setdefault(remote_engine_id, meta)
for remote_engine_id, meta in engines.items():
if remote_engine_id in self._eager_handshaked_engines:
continue
remote_dp_size = int(meta.remote_dp_size)
port = int(meta.remote_handshake_port)
tp_size = int(meta.tp_size)
# Flexible mirror (TP prefill + MLA, world_size==1 decode): the read
# round-robins over prefill TP ranks, so pre-warm a session to EVERY
# (dp, tp) rank. Other configs pre-warm per DP rank (tp resolved by
# the fixed local-rank mapping) -- byte-identical to before. The
# mirror's decode is DP+EP, whose forward all-to-all is the collective
# that the eager barrier keeps everyone in step for.
flexible = (
self.world_size == 1
and self.use_mla
and remote_dp_size == 1
and tp_size > 1
)
# (engine_id, dp_rank, tp_rank_or_None); tp_rank is None on the legacy
# path so _moriio_handshake falls back to its _remote_tp_rank mapping.
targets: list[tuple[Any, int, int | None]]
if flexible:
targets = [
(self.get_engine_name_with_dp_tp(remote_engine_id, dp, tp), dp, tp)
for dp in range(remote_dp_size)
for tp in range(max(1, tp_size))
]
else:
targets = [
(self.get_engine_name_with_dp(remote_engine_id, dp), dp, None)
for dp in range(remote_dp_size)
]
# Submit handshakes for every not-yet-known target UNDER the lock; do
# NOT hold it across the join or the collective (a stalled recv must
# not block another thread's lock acquisition). Gate on BOTH
# _remote_agents AND layer metadata: a rank with an agent entry but no
# layer metadata is half-handshaked and would KeyError at read time.
futures: list[tuple[str, Future[set[str]]]] = []
with self._handshake_lock:
for eid, cur_dp_rank, cur_tp_rank in targets:
if (
eid in self._remote_agents
and eid in self.layer_name_to_remote_kv_cache_metadata
):
continue
fut = self._handshake_initiation_executor.submit(
self._moriio_handshake,
meta.remote_host,
port,
tp_size,
eid,
cur_dp_rank,
cur_tp_rank,
)
futures.append((eid, fut))
# Join outside the lock. Bounded handshake errors are recorded here
# and reported after the all-reduce.
all_ok = True
results: dict[str, set[str]] = {}
for eid, fut in futures:
try:
results[eid] = fut.result()
except Exception:
logger.exception("Eager MoRIIO handshake failed for %s", eid)
all_ok = False
with self._handshake_lock:
for eid, agents in results.items():
self._remote_agents[eid] = agents
logger.info(
"Eager MoRIIO handshake: engine=%s dp_size=%d new_ranks=%d "
"ok=%s tp_rank=%d",
remote_engine_id,
remote_dp_size,
len(futures),
all_ok,
self.tp_rank,
)
# CPU all-reduce = TP-uniform success vote AND lockstep barrier: it
# blocks until every TP worker arrives, gives them the same verdict,
# and stays off the model compute stream.
vote = torch.tensor([1 if all_ok else 0], device="cpu", dtype=torch.int32)
dist.all_reduce(vote, group=self.tp_group.cpu_group, op=dist.ReduceOp.MIN)
if int(vote.item()) == 0:
raise HandshakeError(
f"Eager MoRIIO handshake failed for {remote_engine_id} on "
"at least one TP rank; failing this step fast to avoid a "
"TP collective hang"
)
self._eager_handshaked_engines.add(remote_engine_id)
def start_load_kv(self, metadata: MoRIIOConnectorMetadata):
"""Start loading by triggering non-blocking moriio_xfer.
We check for these trnxs to complete in each step().
"""
self.transfer_id_to_request_id = metadata.transfer_id_to_request_id
if self.is_producer:
live_transfer_ids = set(self.transfer_id_to_request_id)
self._consumer_notification_counts = {
transfer_id: count
for transfer_id, count in self._consumer_notification_counts.items()
if transfer_id in live_transfer_ids
}
self._completed_consumer_notifications.intersection_update(
live_transfer_ids
)
self.moriio_wrapper.async_wait_reqid()
return
if self.mode == MoRIIOMode.WRITE:
return
# Handshake every referenced remote prefill rank up front, before any
# read enters the forward pass. A lazy per-rank handshake on the read
# path lets TP workers diverge into a forward collective while a peer is
# still blocked handshaking -> NCCL hang (see below).
self._eager_handshake_all_dp_ranks(metadata)
wait_handshake_readd_req = False
remote_engine_id = None
for req_id, meta in metadata.reqs_to_recv.items():
remote_engine_id = (
str(meta.remote_host) + ":" + str(meta.remote_handshake_port)
)
meta.remote_engine_id = remote_engine_id
# The eager handshake above already covered every referenced engine
# (and keys the mirror per (dp, tp), which the DP-only dp0 probe below
# would miss). Only fall back to the lazy background handshake for an
# engine it did not cover.
dp0_remote_engine_id = self.get_engine_name_with_dp(remote_engine_id, 0)
if (
remote_engine_id not in self._eager_handshaked_engines
and dp0_remote_engine_id not in self._remote_agents
):
# Initiate handshake with remote engine to exchange metadata.
with self._handshake_lock:
if remote_engine_id not in self._remote_agents:
self._background_moriio_handshake(
req_id, remote_engine_id, meta
)
wait_handshake_readd_req = True
continue
# Handshake already completed, start the read xfer.
self._read_blocks_for_req(req_id, meta)
# Start transfers for requests whose handshakes have now finished.
if remote_engine_id is None and not wait_handshake_readd_req:
self._await_reads_issued_this_step()
return
_deadline = time.monotonic() + self.moriio_config.transfer_timeout
while True:
if (
self._ready_requests.empty()
and remote_engine_id not in self.load_ready_flag
and wait_handshake_readd_req
):
if time.monotonic() > _deadline:
logger.warning(
"Timed out waiting for load_ready_flag[%s]; "
"adjust with kv_connector_extra_config.transfer_timeout",
remote_engine_id,
)
break
time.sleep(0.001)
continue
elif (
not self._ready_requests.empty()
and remote_engine_id in self.load_ready_flag
):
self._read_blocks_for_req(*self._ready_requests.get_nowait())
break
else:
break
self._await_reads_issued_this_step()
self._reqs_to_send.update(metadata.reqs_to_send)
def wait_for_save(self, metadata: MoRIIOConnectorMetadata):
if self.mode == MoRIIOMode.WRITE and self.is_producer:
for layer_name, kv_layer in self.kv_caches.items():
self.save_kv_layer(metadata, layer_name, kv_layer, None)
self._writer.seal_pending_transfers()
def _next_flex_tp_rank(self, remote_tp_size: int) -> int:
"""Deterministic round-robin over prefill tp0..N-1 for the flexible read.
Round-robin (not random): exactly uniform and testable, with the same
prefill-NIC balancing. Seeded from this decode rank's dp_rank so
concurrent decode DP ranks are phase-staggered -- at a given read index
distinct decode ranks target distinct prefill TP ranks.
"""
rr = getattr(self, "_flex_tp_rr", None)
if rr is None:
rr = int(getattr(self, "dp_rank", 0) or 0)
self._flex_tp_rr = rr + 1
return rr % remote_tp_size
def _resolve_read_source(self, meta: ReqMeta) -> tuple[int, bool]:
"""Resolve (chosen_tp, flexible) for reading this request's KV.
Flexible mirror (decode world_size==1 + MLA + pure-TP prefill): MLA
replicates the latent KV across the prefill TP ranks, so any is a valid
source; round-robin across them to spread RDMA/NIC load. Otherwise the
source TP rank is fixed by the local-rank mapping (_remote_tp_rank) --
forward DP8EP->TP8 -> tp0; symmetric TP -> tp_rank -- byte-identical to
prior behaviour. chosen_tp is the single value threaded into the (dp, tp)
session key, the handshake dial and the notify port, so all three address
the SAME prefill rank (drift -> read one rank but notify another -> the
read rank's prefill buffer is never freed).
"""
remote_tp_size = int(meta.tp_size)
flexible = (
self.world_size == 1
and self.use_mla
and int(meta.remote_dp_size) == 1
and remote_tp_size > 1
)
if flexible:
chosen_tp = self._next_flex_tp_rank(remote_tp_size)
else:
chosen_tp = self._remote_tp_rank(remote_tp_size)
return chosen_tp, flexible
def _read_blocks_for_req(self, req_id: str, meta: ReqMeta):
logger.debug(
"Remote agent %s available, calling _read_blocks for req %s",
meta.remote_engine_id,
req_id,
)
chosen_tp, flexible = self._resolve_read_source(meta)
self._read_blocks(
request_id=req_id,
transfer_id=meta.transfer_id,
dst_engine_id=meta.remote_engine_id,
local_block_ids=meta.local_block_ids,
remote_block_ids=meta.remote_block_ids,
remote_host=meta.remote_host,
remote_notify_port=meta.remote_notify_port,
remote_tp_size=meta.tp_size,
remote_dp_rank=meta.remote_dp_rank,
chosen_tp=chosen_tp,
flexible=flexible,
)
def _write_blocks_for_req(self, req_id: ReqId, meta: ReqMeta, layer_name, kv_layer):
# Stash multi_pod_hosts + local DP size on the worker so
# MoRIIOEngine._finalize_if_complete (which sees only the WriteTask,
# not ReqMeta) can pick the per-rank pod IP for the completion notify.
# Last-writer-wins is safe: all requests share the same topology.
if meta.multi_pod_hosts:
self.multi_pod_hosts = list(meta.multi_pod_hosts)
else:
self.multi_pod_hosts = [meta.remote_host]
if meta.remote_dp_size_local:
self.remote_dp_size_local = int(meta.remote_dp_size_local)
else:
self.remote_dp_size_local = int(meta.remote_dp_size)
# WRITE does not support HMA, so unwrap blocks into flat lists.
# remote_block_ids can itself be empty so need to be careful when unwrapping.
local_block_ids = meta.local_block_ids[0]
remote_block_ids = meta.remote_block_ids[0] if meta.remote_block_ids else []
self.schedule_write_blocks(
request_id=req_id,
transfer_id=meta.transfer_id,
dst_engine_id=meta.remote_engine_id,
local_block_ids=local_block_ids,
remote_block_ids=remote_block_ids,
layer_name=layer_name,
kv_layer=kv_layer,
remote_notify_port=meta.remote_notify_port,
remote_ip=meta.remote_host,
)
def merge_contiguous_blocks(
self,
offsets_local: list[int],
offsets_remote: list[int],
sizes: list[int],
assume_sorted: bool = False,
) -> tuple[list[int], list[int], list[int]]:
n = len(offsets_local)
if n == 0:
return [], [], []
if not (n == len(offsets_remote) == len(sizes)):
raise ValueError("Input list lengths mismatch")
local_arr = np.fromiter(offsets_local, dtype=np.int64, count=n)
remote_arr = np.fromiter(offsets_remote, dtype=np.int64, count=n)
sizes_arr = np.fromiter(sizes, dtype=np.int64, count=n)
if assume_sorted:
local_sorted = local_arr
remote_sorted = remote_arr
sizes_sorted = sizes_arr
else:
if np.all(local_arr[:-1] <= local_arr[1:]):
local_sorted = local_arr
remote_sorted = remote_arr
sizes_sorted = sizes_arr
else:
sort_idx = np.argsort(local_arr, kind="stable")
local_sorted = local_arr[sort_idx]
remote_sorted = remote_arr[sort_idx]
sizes_sorted = sizes_arr[sort_idx]
if n == 1:
return (
[int(local_sorted[0])],
[int(remote_sorted[0])],
[int(sizes_sorted[0])],
)
diff_local = local_sorted[1:] - local_sorted[:-1]
diff_remote = remote_sorted[1:] - remote_sorted[:-1]
prev_size = sizes_sorted[:-1]
contiguous = (diff_local == prev_size) & (diff_remote == prev_size)
if not contiguous.any():
return local_sorted.tolist(), remote_sorted.tolist(), sizes_sorted.tolist()
if contiguous.all():
total_size = int(sizes_sorted.sum())
return [int(local_sorted[0])], [int(remote_sorted[0])], [total_size]
break_positions = np.flatnonzero(~contiguous) + 1
segment_starts = np.concatenate(([0], break_positions))
segment_ends = np.concatenate((break_positions, [n]))
seg_count = len(segment_starts)
merged_local = [0] * seg_count
merged_remote = [0] * seg_count
merged_sizes = [0] * seg_count
for si in range(seg_count):
s = segment_starts[si]
e = segment_ends[si]
merged_local[si] = int(local_sorted[s])
merged_remote[si] = int(remote_sorted[s])
merged_sizes[si] = int(
local_sorted[e - 1] + sizes_sorted[e - 1] - local_sorted[s]
)
return merged_local, merged_remote, merged_sizes
def _compute_block_transfer_offsets(
self,
layer_name: str,
local_block_ids: list[int],
remote_block_ids: list[int],
remote_moriio_meta: MoRIIOAgentMetadata,
remote_tp_size: int | None = None,
remote_engine_id: EngineId | None = None,
) -> tuple[list[int], list[int], list[int]]:
"""Compute transfer offsets for block data.
Args:
layer_name: Name of the layer to transfer
local_block_ids: IDs of local blocks
remote_block_ids: IDs of remote blocks
remote_moriio_meta: Metadata of the remote MoRIIO agent
remote_tp_size: Tensor parallel size of the remote engine. Falls
back to the locally recorded value when None.
remote_engine_id: Id of the remote engine the blocks live on.
Returns:
Tuple of (local_offsets, remote_offsets, transfer_sizes)
"""
validate_moriio_heterogeneous_tp_kv_heads(
local_tp_size=self.world_size,
remote_tp_size=(
remote_tp_size
if remote_tp_size and remote_tp_size > 0
else self.world_size
),
total_num_kv_heads=self.model_config.get_total_num_kv_heads(),
is_mla=self._is_mla_cache_layer(layer_name),
)
local, remote, sizes = compute_block_transfer_offsets(
layer_name=layer_name,
kv_cache=self.kv_caches[layer_name],
layer_to_spec=self.layer_to_spec,
local_block_ids=local_block_ids,
remote_block_ids=remote_block_ids,
remote_num_blocks=remote_moriio_meta.num_blocks,
merge_fn=lambda local, remote, sizes: self.merge_contiguous_blocks(
local, remote, sizes, assume_sorted=False
),
)
if self.kv_layer_mr_offset:
local_off = self.kv_layer_mr_offset[layer_name]
remote_off = self._remote_layer_mr_offset(
layer_name, remote_moriio_meta, remote_engine_id
)
local = [x + local_off for x in local]
remote = [x + remote_off for x in remote]
return local, remote, sizes
def _region_session_indices(self, layer_name: str) -> list[int]:
"""Flat session indices for a layer's registered regions.
Sessions are built one per region in registration order (see
_get_built_session), so an attention layer maps to a single index and a
KDA layer to two indices ([conv, ssm]). Built once and cached.
"""
if self._region_session_index is None:
mapping: dict[str, list[int]] = {}
idx = 0
for ln, metas in self.layer_name_to_local_kv_cache_metadata.items():
mapping[ln] = list(range(idx, idx + len(metas)))
idx += len(metas)
self._region_session_index = mapping
return self._region_session_index[layer_name]
def _mamba_tp_ratio(self, remote_tp_size: int | None) -> int:
"""Validate the homogeneous-TP KDA contract."""
remote = self.world_size if remote_tp_size is None else remote_tp_size
if remote != self.world_size:
raise NotImplementedError(
"heterogeneous-TP mamba/KDA transfer is not supported yet "
f"(local_tp={self.world_size}, remote_tp={remote}); use equal "
"prefill/decode TP for hybrid models"
)
return 1
def _mamba_blocks_for_layer(
self,
layer_name: str,
block_groups: BlockIds,
) -> list[int]:
payload_index = self._mamba_payload_index_by_layer.get(layer_name)
if payload_index is None or payload_index >= len(block_groups):
raise MoRIIOError(
f"KDA layer {layer_name} has no block group in the transfer payload"
)
return list(block_groups[payload_index])
def _compute_mamba_transfer_offsets(
self,
layer_name: str,
local_slots: list[int],
remote_slots: list[int],
remote_tp_size: int | None = None,
) -> tuple[list[int], list[int], list[int], int]:
"""Compute (local, remote, sizes, n_conv) for a KDA layer.
Entries [:n_conv] address the conv region/session; entries [n_conv:]
address the ssm region/session.
"""
assert self._conv_decomp is not None, "KDA decomposition not derived"
conv, ssm = kda_conv_ssm(
self.kv_caches[layer_name],
cast(MambaSpec, self.layer_to_spec[layer_name]),
)
tp_ratio = self._mamba_tp_ratio(remote_tp_size)
# Cache the slot-independent geometry per layer; only the per-request
# slot bases vary, and heterogeneous TP is rejected above.
template = self._mamba_offset_templates.get(layer_name)
if template is None:
template = build_mamba_offset_template(
conv,
ssm,
self._conv_decomp,
tp_ratio,
)
self._mamba_offset_templates[layer_name] = template
local_offs, remote_offs, sizes = apply_mamba_offset_template(
template, local_slots, remote_slots
)
n_conv = compute_mamba_conv_split_count(local_slots, self._conv_decomp)
return local_offs, remote_offs, sizes, n_conv
def _post_mamba_reads(
self,
layer_name: str,
sessions: list,
region_sessions: list[int],
local_slots: list[int],
remote_slots: list[int],
remote_tp_size: int,
request_id: str,
deadline: float,
) -> list:
"""Post one KDA layer's conv and ssm reads; return their statuses.
The layer owns two registered regions, so the offset list is split at
the conv/ssm boundary and each half goes to its own session. A half
with nothing to move is skipped rather than posted empty.
"""
local, remote, sizes, n_conv = self._compute_mamba_transfer_offsets(
layer_name,
local_slots,
remote_slots,
remote_tp_size=remote_tp_size,
)
statuses: list = []
for sess_idx, sl in (
(region_sessions[0], slice(0, n_conv)),
(region_sessions[1], slice(n_conv, None)),
):
region_sizes = sizes[sl]
if not region_sizes:
continue
statuses.append(
self._post_read_with_backoff(
sessions[sess_idx],
region_sizes,
local[sl],
remote[sl],
request_id,
layer_name,
deadline,
)
)
return statuses
def _post_read_with_backoff(
self,
session,
sizes: list[int],
local_offsets: list[int],
remote_offsets: list[int],
request_id: str,
layer_name: str,
deadline: float,
):
"""Post one RDMA READ, backing off on transient SQ-full rejection.
read_remote_data posts synchronously, so a send-queue-full rejection is
a Failed() status on return; a separate CQ-poll thread drains
completions and frees SQ depth, so we back off and re-post until
transfer_timeout, then store the failed status (get_finished notifies
prefill and drops the request non-fatally).
"""
_backoff = _SQ_FULL_BACKOFF_INITIAL_S
while True:
transfer_status = self.moriio_wrapper.read_remote_data(
sizes, local_offsets, remote_offsets, session
)
if not self._is_sq_full_status(transfer_status):
break
if time.monotonic() > deadline:
logger.warning(
"MoRIIO READ send queue stayed full past "
"transfer_timeout for req %s layer %s; storing failed "
"status (get_finished notifies prefill and drops the "
"request). Raise qp_per_transfer if frequent.",
request_id,
layer_name,
)
break
time.sleep(_backoff)
_backoff = min(_backoff * 2, _SQ_FULL_BACKOFF_MAX_S)
return transfer_status
@staticmethod
def _is_sq_full_status(status) -> bool:
"""True if a MoRIIO transfer status is a transient RDMA send-queue-full
rejection (retryable backpressure), not a terminal failure.
read_remote_data posts the RDMA READ synchronously (the mori executor
joins its worker before returning and marks the status on the calling
thread), so a send-queue-full rejection is a Failed() status the moment
the call returns. mori surfaces it as a generic ERR_RDMA_OP carrying
"SQ full" in the message (no distinct code), so we match the message.
Only meaningful once status.Failed() is True.
"""
try:
return bool(status.Failed()) and "SQ full" in (status.Message() or "")
except Exception:
return False
def _read_blocks(
self,
local_block_ids: BlockIds,
remote_block_ids: BlockIds,
dst_engine_id: str,
request_id: str,
transfer_id: str,
remote_host: str,
remote_notify_port: int,
remote_tp_size: int,
remote_dp_rank: int = 0,
chosen_tp: int | None = None,
flexible: bool = False,
) -> None:
if self.mode == MoRIIOMode.WRITE:
return
# Read from the prefill rank that actually computed this request's KV
# (forwarded by the proxy). Hardcoding DP0 reads from a different rank's
# memory registration; per-rank num_blocks differ, so high block ids can
# overrun the wrong rank's region.
#
# eff_tp = the remote TP rank this read targets. The flexible mirror
# reads from a round-robin-chosen prefill TP rank and keys the session
# per (dp, tp); other configs use the fixed local-rank mapping (eff_tp ==
# _remote_tp_rank), byte-identical to before. This key MUST match the one
# the eager handshake stored the session under.
eff_tp = (
int(chosen_tp)
if chosen_tp is not None
else self._remote_tp_rank(remote_tp_size)
)
if not any(local_block_ids):
# A request aborted before decode allocation still carries the
# producer's block table. There is no local destination or forward,
# so release the producer blocks without building sessions or
# posting RDMA reads.
self.moriio_wrapper.send_notify(
transfer_id,
remote_host,
str(
remote_notify_port
+ get_port_offset(
int(remote_dp_rank),
eff_tp,
remote_tp_size,
)
),
message_type="release",
message_fields={"consumer_tp_size": self.world_size},
)
return
if self._has_mamba:
expected_groups = 1 + self._num_mamba_transfer_groups
if (
len(local_block_ids) != expected_groups
or len(remote_block_ids) != expected_groups
):
raise MoRIIOError(
"MoRIIO hybrid READ block group count mismatch: "
f"expected={expected_groups}, local={len(local_block_ids)}, "
f"remote={len(remote_block_ids)}"
)
local_attn = list(local_block_ids[0])
remote_attn = list(remote_block_ids[0])
self._mamba_tp_ratio(remote_tp_size)
else:
local_attn = remote_attn = []
if flexible:
remote_dp_engine_id = self.get_engine_name_with_dp_tp(
dst_engine_id, int(remote_dp_rank), eff_tp
)
else:
remote_dp_engine_id = self.get_engine_name_with_dp(
dst_engine_id, int(remote_dp_rank)
)
sessions, remote_moriio_meta = self._get_built_session(remote_dp_engine_id)
# SQ-full backpressure deadline, shared across this request's layers.
_sq_deadline = time.monotonic() + self.moriio_config.transfer_timeout
# TODO: apply multi-session batch-read when MoRIIO supports it.
for layer_name in self.layer_name_to_local_kv_cache_metadata:
region_sessions = self._region_session_indices(layer_name)
statuses = []
if self._is_mamba_layer(layer_name):
local_mamba = self._mamba_blocks_for_layer(layer_name, local_block_ids)
remote_mamba = self._mamba_blocks_for_layer(
layer_name, remote_block_ids
)
# KDA layer: pull conv (sub-projection offsets) and ssm at the
# request's recurrent-state slot. Two regions -> two sessions.
if not local_mamba or not remote_mamba:
if not local_attn and not remote_attn:
# Whole-request no-op (e.g. full prefix cache hit):
# nothing to transfer for any layer.
continue
# A KDA layer must have its recurrent-state slot in the
# block-id tuple; missing it (while attention blocks are
# present) means the mamba KV-cache group is absent -> bug.
raise MoRIIOError(
f"KDA layer {layer_name}: missing mamba recurrent-state "
f"block ids (local={local_mamba}, remote={remote_mamba}) "
f"with attention blocks present for request {request_id}; "
"the mamba KV-cache group is absent from the transfer "
"block-id tuple"
)
statuses = self._post_mamba_reads(
layer_name,
sessions,
region_sessions,
local_mamba,
remote_mamba,
remote_tp_size,
request_id,
_sq_deadline,
)
else:
if self._has_mamba:
local_layer_blocks = local_attn
remote_layer_blocks = remote_attn
else:
group_idx = self.layer_to_group[layer_name]
local_layer_blocks = local_block_ids[group_idx]
remote_layer_blocks = remote_block_ids[group_idx]
offs = self._compute_block_transfer_offsets(
layer_name,
local_layer_blocks,
remote_layer_blocks,
remote_moriio_meta,
remote_tp_size=remote_tp_size,
remote_engine_id=remote_dp_engine_id,
)
statuses.append(
self._post_read_with_backoff(
sessions[region_sessions[0]],
offs[2],
offs[0],
offs[1],
request_id,
layer_name,
_sq_deadline,
)
)
with self.moriio_wrapper.lock:
self._recving_transfers[request_id][layer_name] = statuses
self._recving_transfers_start.setdefault(request_id, time.monotonic())
# Destination blocks, kept for _record_failed_recv.
if self._has_mamba:
failed_recv_blocks = local_attn
else:
failed_recv_blocks = [
block_id for group in local_block_ids for block_id in group
]
self._recving_local_blocks.setdefault(
request_id, list(failed_recv_blocks)
)
# Awaited before the forward when the per-layer barrier cannot
# run (see _await_reads_issued_this_step).
self._reads_issued_this_step.extend(statuses)
if self._is_mamba_layer(layer_name):
# No per-layer barrier exists for mamba layers, so these are
# always awaited in start_load_kv.
self._mamba_reads_this_step.extend(statuses)
self._recving_transfers_callback_addr[request_id] = (
remote_host,
str(
remote_notify_port
+ get_port_offset(
int(remote_dp_rank),
eff_tp,
remote_tp_size,
)
),
transfer_id,
)