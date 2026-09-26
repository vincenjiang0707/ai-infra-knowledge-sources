source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1)

Modules:

-
–[base](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base)KVConnectorBase_V1 Class for Distributed KV Cache & Hidden State

-
–[decode_bench_connector](https://docs.vllm.ai/decode_bench_connector/#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector)DecodeBenchConnector: A KV Connector for decode instance performance testing.

-
–[example_connector](https://docs.vllm.ai/example_connector/#vllm.distributed.kv_transfer.kv_connector.v1.example_connector) -
–[example_hidden_states_connector](https://docs.vllm.ai/example_hidden_states_connector/#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector) -
–[flexkv_connector](https://docs.vllm.ai/flexkv_connector/#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector) -
–[hf3fs](https://docs.vllm.ai/hf3fs/#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs) -
–[hisparse](https://docs.vllm.ai/hisparse/#vllm.distributed.kv_transfer.kv_connector.v1.hisparse) -
–[lmcache_connector](https://docs.vllm.ai/lmcache_connector/#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_connector) -
–[lmcache_integration](https://docs.vllm.ai/lmcache_integration/#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration) -
–[lmcache_mp_connector](https://docs.vllm.ai/lmcache_mp_connector/#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector) -
–[metrics](https://docs.vllm.ai/metrics/#vllm.distributed.kv_transfer.kv_connector.v1.metrics) -
–[mooncake](https://docs.vllm.ai/mooncake/#vllm.distributed.kv_transfer.kv_connector.v1.mooncake) -
–[moriio](https://docs.vllm.ai/moriio/#vllm.distributed.kv_transfer.kv_connector.v1.moriio) -
–[multi_connector](https://docs.vllm.ai/multi_connector/#vllm.distributed.kv_transfer.kv_connector.v1.multi_connector) -
–[nixl](https://docs.vllm.ai/nixl/#vllm.distributed.kv_transfer.kv_connector.v1.nixl)NIXL KV-cache transfer connector (disaggregated prefill / decode).

-
–[offloading](https://docs.vllm.ai/offloading/#vllm.distributed.kv_transfer.kv_connector.v1.offloading) -
–[offloading_connector](https://docs.vllm.ai/offloading_connector/#vllm.distributed.kv_transfer.kv_connector.v1.offloading_connector) -
–[simple_cpu_offload_connector](https://docs.vllm.ai/simple_cpu_offload_connector/#vllm.distributed.kv_transfer.kv_connector.v1.simple_cpu_offload_connector)SimpleCPUOffloadConnector: minimal CPU KV cache offloading.

-
–[ssm_conv_transfer_utils](https://docs.vllm.ai/ssm_conv_transfer_utils/#vllm.distributed.kv_transfer.kv_connector.v1.ssm_conv_transfer_utils)Mamba conv-state sub-projection decomposition for NIXL transfer.


Classes:

-
–[DecodeBenchConnector](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.DecodeBenchConnector)A KV Connector for decode instance performance testing.

-
–[KVConnectorBase_V1](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1)Base class for KV connectors.

-
–[SupportsHMA](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.SupportsHMA)The class that indicates the corresponding connector supports hybrid memory


##

`DecodeBenchConnector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.DecodeBenchConnector)

Bases:

, [KVConnectorBase_V1](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1)[SupportsHMA](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.SupportsHMA)

A KV Connector for decode instance performance testing.

This connector fills the KV cache with dummy values to emulate a prefill-decode disaggregated setting, enabling performance testing of the decoder with larger input sequence lengths.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


|
|

##

`KVConnectorBase_V1`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Base class for KV connectors.

Methods:

-
–[bind_connector_metadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.bind_connector_metadata)Set the connector metadata from the scheduler.

-
–[bind_gpu_block_pool](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.bind_gpu_block_pool)Bind the GPU block pool to the connector for per-GPU block status tracking.

-
–[bind_kv_cache_manager](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.bind_kv_cache_manager)Bind the scheduler's cache manager after it has been constructed.

-
–[build_connector_meta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_connector_meta)Build the connector metadata for this step.

-
–[build_connector_worker_meta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_connector_worker_meta)Build the KVConnector worker metadata for this engine step.

-
–[build_kv_connector_stats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_kv_connector_stats)KVConnectorStats resolution method. This method allows dynamically

-
–[build_prom_metrics](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_prom_metrics)Create a KVConnectorPromMetrics subclass which should register

-
–[clear_connector_metadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.clear_connector_metadata)Clear the connector metadata.

-
–[finish_forward](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.finish_forward)Notify the connector that the model no longer reads this step's KV.

-
–[get_block_ids_with_load_errors](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_block_ids_with_load_errors)Get the set of block IDs that failed to load.

-
–[get_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_finished)Notifies worker-side connector ids of requests that have

-
–[get_finished_count](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_finished_count)Get the count of requests expected to complete send/receive operations

-
–[get_handshake_metadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_handshake_metadata)Get the KVConnector handshake metadata for this connector.

-
–[get_kv_connector_kv_cache_events](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_kv_connector_kv_cache_events)Get the KV connector kv cache events collected during the last interval.

-
–[get_kv_connector_stats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_kv_connector_stats)Get the KV connector stats collected during the last interval.

-
–[get_num_new_matched_tokens](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_num_new_matched_tokens)Get number of new tokens that can be loaded from the

-
–[get_required_kvcache_layout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_required_kvcache_layout)Get the required KV cache layout for this connector.

-
–[get_transfer_results](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_transfer_results)Return completed sends, receives, and receive failures together.

-
–[handle_preemptions](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.handle_preemptions)Handle preempted requests or evicted blocks BEFORE they are overwritten.

-
–[has_connector_metadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.has_connector_metadata)Check whether the connector metadata is currently set.

-
–[has_pending_block_frees](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.has_pending_block_frees)Whether pending transfers can release blocks instead of preemption.

-
–[has_pending_push_work](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.has_pending_push_work)Return True if the connector has push-mode work that requires

-
–[on_new_request](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.on_new_request)Called by the scheduler when a new request is added.

-
–[register_finished_partial_tail](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.register_finished_partial_tail)Register finish-time partial-tail sources before block cleanup.

-
–[register_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.register_kv_caches)Initialize with the KV caches. Useful for pre-registering the

-
–[request_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.request_finished)Called exactly once when a request has finished, before its blocks are

-
–[requires_piecewise_for_cudagraph](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.requires_piecewise_for_cudagraph)Check if this connector requires PIECEWISE CUDA graph mode.

-
–[reset_cache](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.reset_cache)Reset the connector's internal cache.

-
–[reset_capture_state](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.reset_capture_state)Reset worker state mutated while capturing CUDA graphs.

-
–[save_kv_layer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.save_kv_layer)Start saving a layer of KV cache from vLLM's paged buffer

-
–[set_host_xfer_buffer_ops](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.set_host_xfer_buffer_ops)Set the xPU-specific ops for copying KV between host and device.

-
–[set_xfer_handshake_metadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.set_xfer_handshake_metadata)Set the KV connector handshake metadata for this connector.

-
–[set_xfer_handshake_metadata_pp_aware](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.set_xfer_handshake_metadata_pp_aware)Set handshake metadata keyed by (pp_rank, tp_rank).

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.shutdown)Shutdown the connector. This is called when the worker process

-
–[start_load_kv](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.start_load_kv)Start loading the KV cache from the connector to vLLM's paged

-
–[take_events](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.take_events)Take the KV cache events from the connector.

-
–[update_connector_output](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.update_connector_output)Update KVConnector state from worker-side connectors output.

-
–[update_state_after_alloc](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.update_state_after_alloc)Update KVConnector state after block allocation.

-
–[wait_for_layer_load](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.wait_for_layer_load)Block until the KV for a specific layer is loaded into vLLM's

-
–[wait_for_save](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.wait_for_save)Block until all the save operations is done. This is called


Attributes:

-
([requires_kv_delivery](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.requires_kv_delivery)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether this connector hands off KV that must be reliably delivered.

-
([supports_divergent_local_hybrid_hits](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.supports_divergent_local_hybrid_hits)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether external hits can complete divergent local hybrid hits.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


|
|

###

`requires_kv_delivery`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.requires_kv_delivery)

Whether this connector hands off KV that must be reliably delivered.

If True, a request preempted while its hand-off is still pending is recomputed rather than allowed to finish and hand off blocks that the preemption already freed. Defaults to the producer role, since only a producer hands KV off when a request completes. Best-effort caches return False, as a dropped save is just a future cache miss.

###

`supports_divergent_local_hybrid_hits`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.supports_divergent_local_hybrid_hits)

Whether external hits can complete divergent local hybrid hits.

A capable connector restores lagging recurrent state when the local full-attention group reaches a deeper boundary. Defaults to False.

###

`_get_connector_metadata()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1._get_connector_metadata)

Get the connector metadata.

This function should only be called inside the connector.

Returns:

-
(`ConnectorMetadata`


) –[KVConnectorMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorMetadata)the connector metadata.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`bind_connector_metadata(connector_metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.bind_connector_metadata)

Set the connector metadata from the scheduler.

This function should be called by the model runner every time before the model execution. The metadata will be used for runtime KV cache loading and saving.

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`bind_gpu_block_pool(gpu_block_pool)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.bind_gpu_block_pool)

Bind the GPU block pool to the connector for per-GPU block status tracking. For example, inc/dec ref counts, or iterate over the prefix cache blocks.

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`bind_kv_cache_manager(kv_cache_manager)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.bind_kv_cache_manager)

Bind the scheduler's cache manager after it has been constructed.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`build_connector_meta(scheduler_output)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_connector_meta)

Build the connector metadata for this step.

This function should NOT modify fields in the scheduler_output. Also, calling this function will reset the state of the connector.

Parameters:

-

(`scheduler_output`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_connector_meta(scheduler_output))`SchedulerOutput`

) –the scheduler output object.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`build_connector_worker_meta()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_connector_worker_meta)

Build the KVConnector worker metadata for this engine step.

Returns:

-
(`KVConnectorWorkerMetadata`


) –[KVConnectorWorkerMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorWorkerMetadata)| Nonethe worker metadata.

-

–[KVConnectorWorkerMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorWorkerMetadata)| NoneNone if no worker metadata is available.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`build_kv_connector_stats(data=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_kv_connector_stats)

KVConnectorStats resolution method. This method allows dynamically registered connectors to return their own KVConnectorStats object, which can implement custom aggregation logic on the data dict.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`build_prom_metrics(vllm_config, metric_types, labelnames, per_engine_labelvalues)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.build_prom_metrics)

Create a KVConnectorPromMetrics subclass which should register per-connector Prometheus metrics and implement observe() to expose connector transfer stats via Prometheus.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`clear_connector_metadata()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.clear_connector_metadata)

Clear the connector metadata.

This function should be called by the model runner every time after the model execution.

###

`finish_forward()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.finish_forward)

###

`get_block_ids_with_load_errors()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_block_ids_with_load_errors)

Get the set of block IDs that failed to load.

Returns:

-

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[int](https://docs.python.org/3/builtins/functions.html#int)]Set of block IDs that encountered load errors.

-

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[int](https://docs.python.org/3/builtins/functions.html#int)]Empty set if no load errors occurred.


## Notes

- Applies to both sync- and async-loading requests.
- Async loading: failed blocks may be reported in any forward pass up to and including the pass where the request ID is returned by
`get_transfer_results()`

. Even if failures occur, the request must still be reported as finished receiving, and the failed block IDs must appear here no later than that same pass. - Sync loading: failed blocks should be reported in the forward pass in which they are detected.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`get_finished(finished_req_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_finished)

Notifies worker-side connector ids of requests that have finished generating tokens on the worker. The scheduler process (via the Executors) will use this output to track which workers are done.

Returns:

-

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | Noneids of requests that have finished asynchronous transfer

-

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None(requests that previously returned True from request_finished()),

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None,[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None]tuple of (sending/saving ids, recving/loading ids).

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None,[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None]The finished saves/sends req ids must belong to a set provided in a

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None,[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None]call to this method (this call or a prior one).


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`get_finished_count()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_finished_count)

Get the count of requests expected to complete send/receive operations via this connector. This method is used to initialize the KVOutputAggregator, overwriting the default world_size.

Returns:

-
(`int`


) –[int](https://docs.python.org/3/builtins/functions.html#int)| Noneexpected sending or receiving completion count.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`get_handshake_metadata()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_handshake_metadata)

Get the KVConnector handshake metadata for this connector. This metadata is used for out-of-band connector handshake between P/D workers.

Returns:

-
(`KVConnectorHandshakeMetadata`


) –[KVConnectorHandshakeMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorHandshakeMetadata)| Nonethe handshake metadata.

-

–[KVConnectorHandshakeMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorHandshakeMetadata)| NoneNone if no handshake metadata is available.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`get_kv_connector_kv_cache_events()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_kv_connector_kv_cache_events)

Get the KV connector kv cache events collected during the last interval. This function should be called by the model runner every time after the model execution and before cleanup.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`get_kv_connector_stats()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_kv_connector_stats)

###

`get_num_new_matched_tokens(request, num_computed_tokens)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_num_new_matched_tokens)

Get number of new tokens that can be loaded from the external KV cache beyond the num_computed_tokens.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_num_new_matched_tokens(request))

) –[Request](https://docs.vllm.ai/v1/request/#vllm.v1.request.Request)the request object.

-

(`num_computed_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_num_new_matched_tokens(num_computed_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of locally computed tokens for this request


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int)| None,[bool](https://docs.python.org/3/builtins/functions.html#bool)]A tuple with the following elements: - An optional number of tokens that can be loaded from the external KV cache beyond what is already computed. If None, it means that the connector needs more time to determine the number of matched tokens, and the scheduler should query for this request again later. -

`True`

if external KV cache tokens will be loaded asynchronously (between scheduler steps). Must be 'False' if the first element is 0.

## Notes

The connector should only consider the largest prefix of prompt- tokens for which KV cache is actually available at the time of the call. If the cache cannot be loaded for some tokens (e.g., due to connectivity issues or eviction), those tokens must not be taken into account.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`get_required_kvcache_layout(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_required_kvcache_layout)

Get the required KV cache layout for this connector.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_required_kvcache_layout(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)the vllm config.


Returns:

-
(`str`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Nonethe required KV cache layout. e.g. HND, or NHD.

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneNone if the connector does not require a specific layout.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`get_transfer_results(finished_req_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.get_transfer_results)

Return completed sends, receives, and receive failures together.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`handle_preemptions(kv_connector_metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.handle_preemptions)

Handle preempted requests or evicted blocks BEFORE they are overwritten. Needed for connectors which use async saves (e.g., OffloadingConnector)

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`has_connector_metadata()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.has_connector_metadata)

Check whether the connector metadata is currently set.

Returns:

-
(`bool`


) –[bool](https://docs.python.org/3/builtins/functions.html#bool)True if connector metadata exists, False otherwise.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`has_pending_block_frees()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.has_pending_block_frees)

###

`has_pending_push_work()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.has_pending_push_work)

Return True if the connector has push-mode work that requires the engine main loop to keep stepping (e.g. a P-side request whose KV blocks are waiting to be WRITTEN to a D node).

Connectors that don't implement push-based KV transfer should leave this as False.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`on_new_request(request)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.on_new_request)

Called by the scheduler when a new request is added.

Connectors can override this to inspect the request and perform bookkeeping. The default implementation is a no-op.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`register_finished_partial_tail(request, block_ids, partial_tail_offloads)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.register_finished_partial_tail)

Register finish-time partial-tail sources before block cleanup.

Returns True when the connector accepts responsibility for the sources and the request's blocks must remain alive until `get_finished()`

.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`register_kv_caches(kv_caches)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.register_kv_caches)

Initialize with the KV caches. Useful for pre-registering the KV Caches in the KVConnector (e.g. for NIXL).

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`request_finished(request, block_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.request_finished)

Called exactly once when a request has finished, before its blocks are freed.

The connector may assumes responsibility for freeing the blocks asynchronously by returning True.

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the request is being saved/sent asynchronously and blocks

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | Noneshould not be freed until the request_id is returned from

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]get_finished().

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]Optional KVTransferParams to be included in the request outputs

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]returned by the engine.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`requires_piecewise_for_cudagraph(extra_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.requires_piecewise_for_cudagraph)

Check if this connector requires PIECEWISE CUDA graph mode.

Connectors that use asynchronous layer-by-layer operations (wait_for_layer_load/save_kv_layer) should override this method to return True when those operations are enabled. These operations cannot be captured in CUDA graphs and will be skipped during replay, causing data races. PIECEWISE mode allows Python code to execute between graph pieces, ensuring proper synchronization.

Parameters:

Returns:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`reset_cache()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.reset_cache)

Reset the connector's internal cache.

Returns:

-
(`bool`


) –[bool](https://docs.python.org/3/builtins/functions.html#bool)| NoneTrue if the cache was successfully reset, False otherwise.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`reset_capture_state()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.reset_capture_state)

###

`save_kv_layer(layer_name, kv_layer, attn_metadata, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.save_kv_layer)

Start saving a layer of KV cache from vLLM's paged buffer to the connector. This is called from within attention layer to enable async copying during execution.

Parameters:

-

(`layer_name`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.save_kv_layer(layer_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)the name of the layer.

-

(`kv_layer`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.save_kv_layer(kv_layer))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)the paged KV buffer of the current layer in vLLM.

-

(`attn_metadata`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.save_kv_layer(attn_metadata))`AttentionMetadata`

) –the attention metadata.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.save_kv_layer(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –additional arguments for the save operation.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`set_host_xfer_buffer_ops(copy_operation)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.set_host_xfer_buffer_ops)

Set the xPU-specific ops for copying KV between host and device. Needed when host buffer is used for kv transfer (e.g., in NixlConnector)

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`set_xfer_handshake_metadata(metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.set_xfer_handshake_metadata)

Set the KV connector handshake metadata for this connector.

Parameters:

-

(`metadata`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.set_xfer_handshake_metadata(metadata))

) –[KVConnectorHandshakeMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorHandshakeMetadata)the handshake metadata to set.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`set_xfer_handshake_metadata_pp_aware(metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.set_xfer_handshake_metadata_pp_aware)

Set handshake metadata keyed by (pp_rank, tp_rank). - Default implementation assumes pp_rank is always 0 - PP-aware connectors override this to consume all PP producer shards.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.shutdown)

Shutdown the connector. This is called when the worker process is shutting down to ensure that all the async operations are completed and the connector is cleaned up properly.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`start_load_kv(forward_context, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.start_load_kv)

Start loading the KV cache from the connector to vLLM's paged KV buffer. Loads required by the current forward start before it; independent asynchronous loads may start after it is submitted.

Parameters:

-

(`forward_context`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.start_load_kv(forward_context))

) –[ForwardContext](https://docs.vllm.ai/forward_context/#vllm.forward_context.ForwardContext)the forward context.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.start_load_kv(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –additional arguments for the load operation


## Note

The number of elements in kv_caches and layer_names should be the same.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`take_events()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.take_events)

Take the KV cache events from the connector.

Yields:

-

–[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[KVCacheEvent](https://docs.vllm.ai/kv_events/#vllm.distributed.kv_events.KVCacheEvent)]New KV cache events since the last call.


###

`update_connector_output(connector_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.update_connector_output)

Update KVConnector state from worker-side connectors output.

Parameters:

-

(`connector_output`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.update_connector_output(connector_output))`KVConnectorOutput`

) –the worker-side connectors output.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`update_state_after_alloc(request, blocks, num_external_tokens)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.update_state_after_alloc)

Update KVConnector state after block allocation.

If get_num_new_matched_tokens previously returned True for a request, this function may be called twice for that same request - first when blocks are allocated for the connector tokens to be asynchronously loaded into, and second when any additional blocks are allocated, after the load/transfer is complete.

Decide whether to load based on `num_external_tokens`

, not on whether `blocks`

is empty: `blocks`

may be non-empty even when `num_external_tokens == 0`

(e.g. a non-chosen sub-connector of MultiConnector still receives the request's real blocks).

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.update_state_after_alloc(request))

) –[Request](https://docs.vllm.ai/v1/request/#vllm.v1.request.Request)the request object.

-

(`blocks`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.update_state_after_alloc(blocks))

) –[KVCacheBlocks](https://docs.vllm.ai/v1/core/kv_cache_manager/#vllm.v1.core.kv_cache_manager.KVCacheBlocks)the blocks allocated for the request.

-

(`num_external_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.update_state_after_alloc(num_external_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of tokens to load from the external KV cache. 0 means nothing should be loaded.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`wait_for_layer_load(layer_name)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.wait_for_layer_load)

Block until the KV for a specific layer is loaded into vLLM's paged buffer. This is called from within attention layer to ensure async copying from start_load_kv is complete.

This interface will be useful for layer-by-layer pipelining.

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`wait_for_save()`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1.wait_for_save)

Block until all the save operations is done. This is called as the forward context exits to ensure that the async saving from save_kv_layer is complete before finishing the forward.

This prevents overwrites of paged KV buffer before saving done.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


##

`SupportsHMA`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.SupportsHMA)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

The class that indicates the corresponding connector supports hybrid memory allocator (HMA). This is required to use the connector together with hybrid memory allocator.

Methods:

-
–[request_finished_all_groups](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.SupportsHMA.request_finished_all_groups)Called exactly once when a request has finished for all kv cache groups,


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/base.py`


###

`request_finished_all_groups(request, block_ids)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.SupportsHMA.request_finished_all_groups)

Called exactly once when a request has finished for all kv cache groups, before its blocks are freed for each group.

NOTE(Kuntai): This function is only supported by connectors that support HMA.

The connector may assumes responsibility for freeing the blocks asynchronously by returning True.

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the request is being saved/sent asynchronously and blocks

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | Noneshould not be freed until the request_id is returned from

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]get_finished().

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]Optional KVTransferParams to be included in the request outputs

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]returned by the engine.