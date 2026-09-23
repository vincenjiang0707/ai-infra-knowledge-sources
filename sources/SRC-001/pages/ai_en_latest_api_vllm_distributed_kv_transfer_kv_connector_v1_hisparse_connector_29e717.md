source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hisparse/connector/
lastmod: 2026-09-23

class HiSparseConnector(KVConnectorBase_V1, SupportsHMA):
"""Join the scheduler coordinator to the worker's transfer engine."""
@classmethod
def get_required_kvcache_layout(cls, vllm_config: VllmConfig) -> str:
return "BLHNC"
def __init__(
self,
vllm_config: VllmConfig,
role: KVConnectorRole,
kv_cache_config: KVCacheConfig,
) -> None:
super().__init__(vllm_config, role, kv_cache_config)
if kv_cache_config.hisparse_host_num_blocks is None:
raise ValueError("HiSparseConnector requires a HiSparse host pool")
self.connector_scheduler: HiSparseConnectorScheduler | None = None
self.connector_worker: HiSparseConnectorWorker | None = None
if role == KVConnectorRole.SCHEDULER:
speculative_config = vllm_config.speculative_config
self.connector_scheduler = HiSparseConnectorScheduler(
async_speculative=bool(
vllm_config.scheduler_config.async_scheduling
and speculative_config is not None
),
draft_kv_lookahead=vllm_config.num_lookahead_tokens,
)
elif role == KVConnectorRole.WORKER:
self.connector_worker = HiSparseConnectorWorker(
vllm_config, kv_cache_config
)
else:
raise ValueError(f"Unsupported KV connector role: {role}")
def bind_kv_cache_manager(self, kv_cache_manager: KVCacheManager) -> None:
assert self.connector_scheduler is not None
self.connector_scheduler.bind_coordinator(
get_hisparse_coordinator(kv_cache_manager)
)
@property
def requires_kv_delivery(self) -> bool:
return False
def has_pending_push_work(self) -> bool:
assert self.connector_scheduler is not None
assert self.connector_scheduler.coordinator is not None
return self.connector_scheduler.coordinator.has_pending_work()
def has_pending_block_frees(self) -> bool:
assert self.connector_scheduler is not None
assert self.connector_scheduler.coordinator is not None
return self.connector_scheduler.coordinator.has_pending_reclamation()
def finish_forward(self) -> None:
assert self.connector_worker is not None
self.connector_worker.finish_forward()
def register_kv_caches(self, kv_caches: dict[str, torch.Tensor]) -> None:
assert self.connector_worker is not None
self.connector_worker.register_kv_caches(kv_caches)
def reset_capture_state(self) -> None:
assert self.connector_worker is not None
self.connector_worker.reset_hot_state()
def get_kv_connector_stats(self) -> KVConnectorStats | None:
if self.connector_worker is None:
return None
return self.connector_worker.get_kv_connector_stats()
@classmethod
def build_kv_connector_stats(
cls, data: dict[str, Any] | None = None
) -> KVConnectorStats | None:
return (
HiSparseKVConnectorStats(data=data)
if data is not None
else HiSparseKVConnectorStats()
)
@classmethod
def build_prom_metrics(
cls,
vllm_config: VllmConfig,
metric_types: dict[type[PromMetric], type[PromMetricT]],
labelnames: list[str],
per_engine_labelvalues: dict[int, list[object]],
) -> KVConnectorPromMetrics:
return HiSparsePromMetrics(
vllm_config, metric_types, labelnames, per_engine_labelvalues
)
def start_load_kv(self, forward_context: ForwardContext, **kwargs: Any) -> None:
assert self.connector_worker is not None
metadata = self._get_connector_metadata()
assert isinstance(metadata, HiSparseConnectorMetadata)
request_state_indices = kwargs.get("request_state_indices")
assert request_state_indices is None or isinstance(
request_state_indices, torch.Tensor
)
request_ids = kwargs.get("request_ids")
assert request_ids is None or isinstance(request_ids, list)
attn_metadata = kwargs.get("attn_metadata")
assert attn_metadata is None or isinstance(attn_metadata, dict)
self.connector_worker.start_step(
metadata,
request_state_indices,
request_ids,
num_tokens=int(kwargs.get("num_tokens") or 0),
)
self.connector_worker.prepare_forward(attn_metadata)
def wait_for_layer_load(self, layer_name: str) -> None:
return
def save_kv_layer(
self,
layer_name: str,
kv_layer: torch.Tensor,
attn_metadata: AttentionMetadata,
**kwargs: Any,
) -> None:
return
def wait_for_save(self) -> None:
return
def build_connector_worker_meta(self) -> KVConnectorWorkerMetadata | None:
assert self.connector_worker is not None
enqueued, completed = self.connector_worker.take_transfer_updates()
host_copies = self.connector_worker.take_completed_host_copies()
if not enqueued and not completed and not host_copies:
return None
return HiSparseConnectorWorkerMetadata(
enqueued_transfer_counts={transfer_id: 1 for transfer_id in enqueued},
completed_transfer_counts={transfer_id: 1 for transfer_id in completed},
completed_host_copy_dst_ids=tuple(host_copies),
)
def shutdown(self) -> None:
if self.connector_worker is not None:
self.connector_worker.shutdown()
def get_num_new_matched_tokens(
self, request: Request, num_computed_tokens: int
) -> tuple[int | None, bool]:
return 0, False
def update_state_after_alloc(
self,
request: Request,
blocks: KVCacheBlocks,
num_external_tokens: int,
) -> None:
assert self.connector_scheduler is not None
self.connector_scheduler.requests[request.request_id] = request
def build_connector_meta(
self, scheduler_output: SchedulerOutput
) -> KVConnectorMetadata:
assert self.connector_scheduler is not None
return self.connector_scheduler.build_connector_meta(scheduler_output)
def update_connector_output(self, connector_output: KVConnectorOutput) -> None:
assert self.connector_scheduler is not None
self.connector_scheduler.update_connector_output(connector_output)
def request_finished_all_groups(
self,
request: Request,
block_ids: tuple[list[int], ...],
) -> tuple[bool, dict[str, Any] | None]:
assert self.connector_scheduler is not None
self.connector_scheduler.requests.pop(request.request_id, None)
return False, None