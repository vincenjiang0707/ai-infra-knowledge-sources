source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector)

Classes:

-
–[LMCacheMPConnectorUpstream](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream)The connector for LMCache multi-process mode.

-
–[LMCacheMPRequestMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata) -
–[LMCacheMPRequestState](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestState)State machine:

-
–[LMCacheMPRequestTracker](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker)

Functions:

-
–[extract_world_size_and_kv_rank](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.extract_world_size_and_kv_rank)Convert the rank for the MLA.


##

`LMCacheMPConnectorUpstream`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream)

Bases: [KVConnectorBase_V1](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorBase_V1)

The connector for LMCache multi-process mode.

Extra configs (kv_transfer_config.extra_config): - lmcache.mp.host: the host of the LMCache server. - lmcache.mp.port: the port of the LMCache server. - lmcache.mp.mq_timeout: timeout (seconds) for message queue requests. - lmcache.mp.heartbeat_interval: interval (seconds) between server heartbeat pings.

Methods:

-
–[build_connector_meta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.build_connector_meta)Build the connector metadata for this step.

-
–[build_kv_connector_stats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.build_kv_connector_stats)KVConnectorStats resolution method. This method allows dynamically

-
–[build_prom_metrics](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.build_prom_metrics)Create a KVConnectorPromMetrics subclass which should register

-
–[get_block_ids_with_load_errors](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_block_ids_with_load_errors)Get the set of block IDs that failed to load.

-
–[get_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_finished)Notifies worker-side connector ids of requests that have

-
–[get_finished_count](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_finished_count)Get the count of requests expected to complete send/receive operations

-
–[get_kv_connector_stats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_kv_connector_stats)Get the KV connector stats collected during the last interval.

-
–[get_num_new_matched_tokens](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_num_new_matched_tokens)Get number of new tokens that can be loaded from the

-
–[get_required_kvcache_layout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_required_kvcache_layout)Get the required KV cache layout for this connector.

-
–[register_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.register_kv_caches)Initialize with the KV caches. Useful for pre-registering the

-
–[request_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.request_finished)Called exactly once when a request has finished, before its blocks are

-
–[save_kv_layer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.save_kv_layer)Start saving a layer of KV cache from vLLM's paged buffer

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.shutdown)Shutdown the connector. This is called when the worker process

-
–[start_load_kv](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.start_load_kv)Start loading the KV cache from the connector to vLLM's paged

-
–[take_events](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.take_events)Take the KV cache events from the connector.

-
–[update_connector_output](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.update_connector_output)Update KVConnector state from worker-side connectors output.

-
–[update_state_after_alloc](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.update_state_after_alloc)Update KVConnector state after block allocation.

-
–[wait_for_layer_load](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.wait_for_layer_load)Block until the KV for a specific layer is loaded into vLLM's

-
–[wait_for_save](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.wait_for_save)Block until all the save operations is done. This is called


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


|
|

###

`_cleanup_request_tracker(request_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream._cleanup_request_tracker)

Clean up request tracker and associated lookup future for a request. This should be called when a request is finished to prevent memory leak.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`_get_connector_metadata()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream._get_connector_metadata)

Get the connector metadata.

This function should only be called inside the connector.

Returns:

-
(`ConnectorMetadata`


) –[KVConnectorMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorMetadata)the connector metadata.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`_report_block_allocation_deltas(scheduler_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream._report_block_allocation_deltas)

Gather per-request block allocation deltas and report to LMCache.

For new requests: all allocated_block_ids and token_ids are new. For cached requests: only newly appended block_ids and token_ids.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`build_connector_meta(scheduler_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.build_connector_meta)

Build the connector metadata for this step.

This function should NOT modify fields in the scheduler_output. Also, calling this function will reset the state of the connector.

Parameters:

-

(`scheduler_output`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.build_connector_meta(scheduler_output))`SchedulerOutput`

) –the scheduler output object.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`build_kv_connector_stats(data=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.build_kv_connector_stats)

KVConnectorStats resolution method. This method allows dynamically registered connectors to return their own KVConnectorStats object, which can implement custom aggregation logic on the data dict.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`build_prom_metrics(vllm_config, metric_types, labelnames, per_engine_labelvalues)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.build_prom_metrics)

Create a KVConnectorPromMetrics subclass which should register per-connector Prometheus metrics and implement observe() to expose connector transfer stats via Prometheus.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`get_block_ids_with_load_errors()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_block_ids_with_load_errors)

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

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`get_finished(finished_req_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_finished)

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


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`get_finished_count()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_finished_count)

Get the count of requests expected to complete send/receive operations via this connector. This method is used to initialize the KVOutputAggregator, overwriting the default world_size.

Returns:

-
(`int`


) –[int](https://docs.python.org/3/builtins/functions.html#int)| Noneexpected sending or receiving completion count.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`get_kv_connector_stats()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_kv_connector_stats)

Get the KV connector stats collected during the last interval.

###

`get_num_new_matched_tokens(request, num_computed_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_num_new_matched_tokens)

Get number of new tokens that can be loaded from the external KV cache beyond the num_computed_tokens.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_num_new_matched_tokens(request))

) –[Request](https://docs.vllm.ai/v1/request/#vllm.v1.request.Request)the request object.

-

(`num_computed_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_num_new_matched_tokens(num_computed_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of locally computed tokens for this request


Returns:

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int)| None,[bool](https://docs.python.org/3/builtins/functions.html#bool)]A tuple with the following elements: - An optional number of tokens that can be loaded from the external KV cache beyond what is already computed. If None, it means that the connector needs more time to determine the number of matched tokens, and the scheduler should query for this request again later. -

`True`

if external KV cache tokens will be loaded asynchronously (between scheduler steps). Must be 'False' if the first element is 0.

## Notes

The connector should only consider the largest prefix of prompt- tokens for which KV cache is actually available at the time of the call. If the cache cannot be loaded for some tokens (e.g., due to connectivity issues or eviction), those tokens must not be taken into account.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`get_required_kvcache_layout(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_required_kvcache_layout)

Get the required KV cache layout for this connector.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.get_required_kvcache_layout(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)the vllm config.


Returns:

-
(`str`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Nonethe required KV cache layout. e.g. HND, or NHD.

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneNone if the connector does not require a specific layout.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`register_kv_caches(kv_caches)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.register_kv_caches)

Initialize with the KV caches. Useful for pre-registering the KV Caches in the KVConnector (e.g. for NIXL).

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`request_finished(request, block_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.request_finished)

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


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`save_kv_layer(layer_name, kv_layer, attn_metadata, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.save_kv_layer)

Start saving a layer of KV cache from vLLM's paged buffer to the connector. This is called from within attention layer to enable async copying during execution.

Parameters:

-

(`layer_name`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.save_kv_layer(layer_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)the name of the layer.

-

(`kv_layer`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.save_kv_layer(kv_layer))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)the paged KV buffer of the current layer in vLLM.

-

(`attn_metadata`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.save_kv_layer(attn_metadata))`AttentionMetadata`

) –the attention metadata.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.save_kv_layer(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –additional arguments for the save operation.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.shutdown)

Shutdown the connector. This is called when the worker process is shutting down to ensure that all the async operations are completed and the connector is cleaned up properly.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`start_load_kv(forward_context, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.start_load_kv)

Start loading the KV cache from the connector to vLLM's paged KV buffer. This is called from the forward context before the forward pass to enable async loading during model execution.

Parameters:

-

(`forward_context`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.start_load_kv(forward_context))

) –[ForwardContext](https://docs.vllm.ai/forward_context/#vllm.forward_context.ForwardContext)the forward context.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.start_load_kv(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –additional arguments for the load operation


## Note

The number of elements in kv_caches and layer_names should be the same.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`take_events()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.take_events)

Take the KV cache events from the connector.

Yields:

-

–[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[KVCacheEvent](https://docs.vllm.ai/kv_events/#vllm.distributed.kv_events.KVCacheEvent)]New KV cache events since the last call.


###

`update_connector_output(connector_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.update_connector_output)

Update KVConnector state from worker-side connectors output.

Parameters:

-

(`connector_output`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.update_connector_output(connector_output))`KVConnectorOutput`

) –the worker-side connectors output.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`update_state_after_alloc(request, blocks, num_external_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.update_state_after_alloc)

Update KVConnector state after block allocation.

If get_num_new_matched_tokens previously returned True for a request, this function may be called twice for that same request - first when blocks are allocated for the connector tokens to be asynchronously loaded into, and second when any additional blocks are allocated, after the load/transfer is complete.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.update_state_after_alloc(request))

) –[Request](https://docs.vllm.ai/v1/request/#vllm.v1.request.Request)the request object.

-

(`blocks`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.update_state_after_alloc(blocks))

) –[KVCacheBlocks](https://docs.vllm.ai/v1/core/kv_cache_manager/#vllm.v1.core.kv_cache_manager.KVCacheBlocks)the blocks allocated for the request.

-

(`num_external_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.update_state_after_alloc(num_external_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of tokens that will be loaded from the external KV cache.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


|
|

###

`wait_for_layer_load(layer_name)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.wait_for_layer_load)

Block until the KV for a specific layer is loaded into vLLM's paged buffer. This is called from within attention layer to ensure async copying from start_load_kv is complete.

This interface will be useful for layer-by-layer pipelining.

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`wait_for_save()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPConnectorUpstream.wait_for_save)

Block until all the save operations is done. This is called as the forward context exits to ensure that the async saving from save_kv_layer is complete before finishing the forward.

This prevents overwrites of paged KV buffer before saving done.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


##

`LMCacheMPRequestMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata)

Methods:

-
–[GetRetrieveMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetRetrieveMetadata)Generate the retrieve metadata for the current request tracker.

-
–[GetStoreMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetStoreMetadata)Generate the store metadata for the current request tracker.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


|
|

###

`GetRetrieveMetadata(tracker, blocks_in_chunk, vllm_block_size)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetRetrieveMetadata)

Generate the retrieve metadata for the current request tracker.

Parameters:

-

(`tracker`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetRetrieveMetadata(tracker))

) –[LMCacheMPRequestTracker](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker)The request tracker to generate the metadata from.

-

(`blocks_in_chunk`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetRetrieveMetadata(blocks_in_chunk))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of blocks in a LMCache data chunk

-

(`vllm_block_size`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetRetrieveMetadata(vllm_block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the block size used in vLLM


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`GetStoreMetadata(tracker, blocks_in_chunk, vllm_block_size)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetStoreMetadata)

Generate the store metadata for the current request tracker.

Parameters:

-

(`tracker`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetStoreMetadata(tracker))

) –[LMCacheMPRequestTracker](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker)The request tracker to generate the metadata from.

-

(`blocks_in_chunk`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetStoreMetadata(blocks_in_chunk))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of blocks in a LMCache data chunk

-

(`vllm_block_size`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestMetadata.GetStoreMetadata(vllm_block_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the block size used in vLLM


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


##

`LMCacheMPRequestState`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestState)

Bases: [Enum](https://docs.python.org/3/library/enum.html#enum.Enum)

State machine: PREFETCHING -- update_state_after_alloc --> WAITING_FOR_LOAD WAITING_FOR_LOAD -- process_loading_requests --> READY

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


##

`LMCacheMPRequestTracker`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker)

Methods:

-
–[append_block_ids](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker.append_block_ids)Update the block ids for the current request

-
–[increase_num_stored_blocks](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker.increase_num_stored_blocks)Increase the number of stored blocks for the current request

-
–[is_ready_for_retrieving](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker.is_ready_for_retrieving)Check whether the current request is ready for retrieving,

-
–[needs_retrieve](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker.needs_retrieve)Check whether the current request needs retrieve, will be used


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


|
|

###

`append_block_ids(new_block_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker.append_block_ids)

Update the block ids for the current request This function will be called when processing the cached requests.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`increase_num_stored_blocks(num_new_blocks)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker.increase_num_stored_blocks)

Increase the number of stored blocks for the current request This function will be called when processing the cached requests.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`is_ready_for_retrieving()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker.is_ready_for_retrieving)

Check whether the current request is ready for retrieving, will be used in process_loading_requests

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


###

`needs_retrieve()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.LMCacheMPRequestTracker.needs_retrieve)

Check whether the current request needs retrieve, will be used update_stage_after_alloc

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_mp_connector.py`


##

`extract_world_size_and_kv_rank(world_size, rank, vllm_config)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_mp_connector.extract_world_size_and_kv_rank)

Convert the rank for the MLA.