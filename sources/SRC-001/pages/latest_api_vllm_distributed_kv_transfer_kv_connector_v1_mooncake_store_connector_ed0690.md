source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/mooncake/store/connector/
lastmod: 2026-09-24

class MooncakeStoreConnector(KVConnectorBase_V1, SupportsHMA):
"""KV connector using MooncakeDistributedStore as shared KV pool."""
@staticmethod
def _validate_kv_cache_config(
vllm_config: VllmConfig, kv_cache_config: KVCacheConfig
) -> None:
from vllm.v1.kv_cache_interface import CrossAttentionSpec, MambaSpec
unsupported: list[str] = []
store_group_ids = kv_cache_config.prefix_cacheable_group_ids
if not store_group_ids:
raise ValueError(
"MooncakeStore requires at least one prefix-cacheable KV cache group"
)
for group_id in store_group_ids:
spec = kv_cache_config.kv_cache_groups[group_id].kv_cache_spec
if isinstance(spec, CrossAttentionSpec):
unsupported.append(f"group {group_id}: CrossAttentionSpec")
if isinstance(spec, MambaSpec) and spec.mamba_cache_mode != "align":
unsupported.append(
f"group {group_id}: mamba_cache_mode="
f"{spec.mamba_cache_mode!r} != 'align'"
)
pcp = vllm_config.parallel_config.prefill_context_parallel_size
if len(store_group_ids) > 1 and pcp > 1:
unsupported.append(f"PCP > 1 (pcp={pcp}) with hybrid attention")
if unsupported:
raise ValueError(
"MooncakeStoreConnector does not support: " + "; ".join(unsupported)
)
def __init__(
self,
vllm_config: VllmConfig,
role: KVConnectorRole,
kv_cache_config: KVCacheConfig | None = None,
):
super().__init__(
vllm_config=vllm_config,
role=role,
kv_cache_config=kv_cache_config, # type: ignore[arg-type]
)
assert vllm_config.kv_transfer_config is not None
assert kv_cache_config is not None, "kv_cache_config is required"
self.kv_role = vllm_config.kv_transfer_config.kv_role
extra_config = vllm_config.kv_transfer_config.kv_connector_extra_config
save_decode_cache = extra_config.get("save_decode_cache", False)
# Capacity-only: contributes its segment to the store pool but transfers
# no KV, so the KV-cache-shape invariants below cannot be reached.
self._capacity_only = (
self.kv_role == "kv_consumer"
and not extra_config.get("enable_lookup", True)
and not save_decode_cache
)
if not self._capacity_only:
self._validate_kv_cache_config(vllm_config, kv_cache_config)
self._kv_cache_config = kv_cache_config
self._kv_cache_events: MooncakeStoreKVEvents | None = None
self.connector_scheduler: MooncakeStoreScheduler | None = None
self.connector_worker: MooncakeStoreWorker | None = None
if role == KVConnectorRole.SCHEDULER:
self.connector_scheduler = MooncakeStoreScheduler(
vllm_config, kv_cache_config
)
else:
self.connector_worker = MooncakeStoreWorker(vllm_config, kv_cache_config)
def shutdown(self):
"""Release connector resources on teardown.
Closes the worker's MooncakeDistributedStore handle so its
TransferEngine and RDMA registrations are released. Invoked from the
engine's explicit shutdown path and as a backstop from ``__del__``;
a no-op on the scheduler role, which holds no store handle.
"""
worker = getattr(self, "connector_worker", None)
if worker is not None:
worker.close()
def __del__(self):
self.shutdown()
# ============================================================
# Scheduler-side methods
# ============================================================
def get_num_new_matched_tokens(
self,
request: Request,
num_computed_tokens: int,
) -> tuple[int | None, bool]:
assert self.connector_scheduler is not None
return self.connector_scheduler.get_num_new_matched_tokens(
request, num_computed_tokens
)
def update_state_after_alloc(
self,
request: Request,
blocks: KVCacheBlocks,
num_external_tokens: int,
):
assert self.connector_scheduler is not None
return self.connector_scheduler.update_state_after_alloc(
request, blocks, num_external_tokens
)
def bind_gpu_block_pool(self, gpu_block_pool: BlockPool) -> None:
assert self.connector_scheduler is not None
self.connector_scheduler.bind_gpu_block_pool(gpu_block_pool)
def has_pending_push_work(self) -> bool:
assert self.connector_scheduler is not None
return self.connector_scheduler.has_pending_push_work()
def build_connector_meta(
self,
scheduler_output: SchedulerOutput,
) -> KVConnectorMetadata:
assert self.connector_scheduler is not None
return self.connector_scheduler.build_connector_meta(scheduler_output)
def build_connector_worker_meta(self) -> KVConnectorWorkerMetadata | None:
assert self.connector_worker is not None
return self.connector_worker.build_connector_worker_meta()
def request_finished(
self,
request: Request,
block_ids: list[int],
) -> tuple[bool, dict[str, Any] | None]:
return self.request_finished_all_groups(request, (block_ids,))
def request_finished_all_groups(
self,
request: Request,
block_ids: tuple[list[int], ...],
) -> tuple[bool, dict[str, Any] | None]:
# An in-flight store job holds its own reference on the blocks it reads,
# so a finishing request never has to defer freeing them.
return False, None
def register_finished_partial_tail(
self,
request: Request,
block_ids: tuple[list[int], ...],
partial_tail_offloads: list[tuple[int, int, int]],
) -> bool:
assert self.connector_scheduler is not None
return self.connector_scheduler.register_finished_partial_tail(
request, block_ids, partial_tail_offloads
)
def reset_cache(self) -> bool | None:
"""Reset the external Mooncake store on prefix-cache reset.
Drains the worker send queue, then runs ``remove_all`` on the
Mooncake master. Caller must first pause generation (e.g.
``pause_generation``) so no new puts are enqueued during drain.
Returns True on ack, False on failure, None for the worker role.
"""
if self.role == KVConnectorRole.SCHEDULER:
assert self.connector_scheduler is not None
# Clear local references to keys we're about to wipe.
self.connector_scheduler.load_specs.clear()
self._kv_cache_events = None
return self.connector_scheduler.reset_store()
return None
def update_connector_output(self, connector_output: KVConnectorOutput):
assert self.connector_scheduler is not None
self.connector_scheduler.update_connector_output(connector_output)
kv_cache_events = connector_output.kv_cache_events
if not kv_cache_events or not isinstance(
kv_cache_events, MooncakeStoreKVEvents
):
return
if self._kv_cache_events is None:
self._kv_cache_events = kv_cache_events
else:
self._kv_cache_events.add_events(kv_cache_events.get_all_events())
def take_events(self) -> Iterable[KVCacheEvent]:
if self._kv_cache_events is not None:
events = self._kv_cache_events.pop_common_events()
if not self._kv_cache_events.has_events():
self._kv_cache_events = None
yield from events
# ============================================================
# Worker-side methods
# ============================================================
def register_kv_caches(self, kv_caches: dict[str, torch.Tensor]):
assert self.connector_worker is not None
self.connector_worker.register_kv_caches(kv_caches)
def start_load_kv(self, forward_context: ForwardContext, **kwargs: Any) -> None:
assert self.connector_worker is not None
metadata = self._get_connector_metadata()
assert isinstance(metadata, MooncakeStoreConnectorMetadata)
self.connector_worker.start_load_kv(metadata)
def wait_for_layer_load(self, layer_name: str) -> None:
# No layerwise support - no-op
return
def save_kv_layer(
self,
layer_name: str,
kv_layer: torch.Tensor,
attn_metadata: AttentionMetadata,
**kwargs: Any,
) -> None:
# No layerwise support - no-op
return
def wait_for_save(self):
assert self.connector_worker is not None
metadata = self._get_connector_metadata()
assert isinstance(metadata, MooncakeStoreConnectorMetadata)
self.connector_worker.wait_for_save(metadata)
def get_finished(
self, finished_req_ids: set[str]
) -> tuple[set[str] | None, set[str] | None]:
assert self.connector_worker is not None
metadata = self._get_connector_metadata()
assert isinstance(metadata, MooncakeStoreConnectorMetadata)
return self.connector_worker.get_finished(finished_req_ids, metadata)
def get_transfer_results(
self, finished_req_ids: set[str]
) -> KVConnectorTransferResults:
assert self.connector_worker is not None
metadata = self._get_connector_metadata()
assert isinstance(metadata, MooncakeStoreConnectorMetadata)
return self.connector_worker.get_transfer_results(finished_req_ids, metadata)
def get_block_ids_with_load_errors(self) -> set[int]:
assert self.connector_worker is not None
return self.connector_worker.get_block_ids_with_load_errors()
def get_kv_connector_kv_cache_events(
self,
) -> MooncakeStoreKVEvents | None:
assert self.connector_worker is not None
if (
not self.connector_worker.enable_kv_events
or self.connector_worker.kv_send_thread is None
):
return None
events = self.connector_worker.get_kv_events()
# Empty containers still count this worker toward the poll's quorum.
kv_events = MooncakeStoreKVEvents(
num_workers=1,
group_tp_replication_factors=(
self.connector_worker.group_tp_replication_factors
),
)
kv_events.add_events(events)
return kv_events
def get_kv_connector_stats(self) -> KVConnectorStats | None:
if self.connector_worker is None:
return None
return self.connector_worker.get_kv_connector_stats()
@classmethod
def build_kv_connector_stats(
cls, data: dict[str, Any] | None = None
) -> KVConnectorStats | None:
return (
MooncakeStoreConnectorStats(data=data)
if data is not None
else MooncakeStoreConnectorStats()
)
@classmethod
def build_prom_metrics(
cls,
vllm_config: VllmConfig,
metric_types: dict[type[PromMetric], type[PromMetricT]],
labelnames: list[str],
per_engine_labelvalues: dict[int, list[object]],
) -> KVConnectorPromMetrics:
return MooncakeStorePromMetrics(
vllm_config, metric_types, labelnames, per_engine_labelvalues
)