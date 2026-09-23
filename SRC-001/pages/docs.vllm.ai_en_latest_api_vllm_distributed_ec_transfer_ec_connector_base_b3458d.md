source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/base/
lastmod: 2026-09-23

#

`vllm.distributed.ec_transfer.ec_connector.base`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base)

ECConnectorBase Class for Distributed Encoder Cache & P2P Encoder cache communication in V1

## The class provides the following primitives

Scheduler-side: runs in the scheduler, binds metadata, which is used by the worker-side to load/save Encoder cache. check_caches_exist() - Check whether Encoder cache of requests exist update_state_after_alloc() - update ECConnector state after allocate. This will decide to load the cache or not request_finished() - called when a request is finished, free the cache with the requests

Worker-side: runs in each worker, loads/saves Encoder Cache to/from the Connector based on the metadata. start_load_ec() - starts loading all ECs (maybe async) wait_for_save() - blocks until all saves are done

```
get_finished() - called with ids of finished requests, returns
ids of requests that have completed async sending/recving.
build_connector_worker_meta() - builds metadata to be sent
back to the scheduler-side connector
```


Classes:

-
–[ECConnectorBase](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase) -
–[ECConnectorMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorMetadata)Abstract Metadata used to communicate between the

-
–[ECConnectorWorkerMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorWorkerMetadata)Abstract Metadata used to communicate back


##

`ECConnectorBase`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[bind_connector_metadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.bind_connector_metadata)Set the connector metadata from the scheduler.

-
–[build_connector_meta](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_connector_meta)Build the connector metadata for this step.

-
–[build_connector_worker_meta](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_connector_worker_meta)Build the ECConnector worker metadata for this engine step.

-
–[build_ec_connector_stats](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_ec_connector_stats)ECConnectorStats resolution method. This method allows dynamically

-
–[build_prom_metrics](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_prom_metrics)Create an ECConnectorPromMetrics subclass which should register

-
–[clear_connector_metadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.clear_connector_metadata)Clear the connector metadata.

-
–[ensure_cache_available](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.ensure_cache_available)Ensure encoder cache items are available for the given request.

-
–[get_ec_connector_stats](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.get_ec_connector_stats)Get the EC connector stats collected during the last interval.

-
–[get_finished](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.get_finished)Notifies worker-side connector ids of requests that have

-
–[has_cache_item](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.has_cache_item)Check if a single encoder cache exists.

-
–[has_pending_push_work](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.has_pending_push_work)Return True if the connector has push-mode work that requires

-
–[register_caches](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.register_caches)Initialize with the EC caches.

-
–[request_finished](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.request_finished)Called when a request has finished, before its encoder cache is freed.

-
–[save_caches](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.save_caches)Save the encoder cache to the connector.

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.shutdown)Shutdown the connector. This is called when the process

-
–[start_load_caches](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_load_caches)Start loading the cache from the connector into vLLM's encoder cache.

-
–[start_save_caches](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_save_caches)Prepare this step's outbound pushes before the model runs.

-
–[start_worker_services](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_worker_services)Start Worker-side services once the model is resident.

-
–[take_unavailable_requests](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.take_unavailable_requests)Request IDs whose encoder inputs the connector can no longer obtain.

-
–[update_connector_output](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_connector_output)Update ECConnector state from worker-side connectors output.

-
–[update_state_after_alloc](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_state_after_alloc)Update ECConnector state to decide allocate cache for requests.

-
–[update_state_after_free](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_state_after_free)Notify the connector that an encoder cache entry was released.


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


|
|

###

`_get_connector_metadata()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase._get_connector_metadata)

Get the connector metadata.

This function should only be called inside the connector.

Returns:

-
(`ConnectorMetadata`


) –[ECConnectorMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorMetadata)the connector metadata.


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`bind_connector_metadata(connector_metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.bind_connector_metadata)

Set the connector metadata from the scheduler.

This function should be called by the model runner every time before the model execution. The metadata will be used for runtime EC cache loading.

Parameters:

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`build_connector_meta(scheduler_output)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_connector_meta)

Build the connector metadata for this step.

This function should NOT modify fields in the scheduler_output. Also, calling this function will reset the state of the connector.

Parameters:

-

(`scheduler_output`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_connector_meta(scheduler_output))`SchedulerOutput`

) –the scheduler output object.


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`build_connector_worker_meta()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_connector_worker_meta)

Build the ECConnector worker metadata for this engine step.

Returns:

-
(`ECConnectorWorkerMetadata`


) –[ECConnectorWorkerMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorWorkerMetadata)| Nonethe worker metadata.

-

–[ECConnectorWorkerMetadata](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorWorkerMetadata)| NoneNone if no worker metadata is available.


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`build_ec_connector_stats(data=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_ec_connector_stats)

ECConnectorStats resolution method. This method allows dynamically registered connectors to return their own ECConnectorStats object, which can implement custom aggregation logic on the data dict.

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`build_prom_metrics(vllm_config, metric_types, labelnames, per_engine_labelvalues)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.build_prom_metrics)

Create an ECConnectorPromMetrics subclass which should register per-connector Prometheus metrics and implement observe() to expose connector transfer stats via Prometheus.

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`clear_connector_metadata()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.clear_connector_metadata)

Clear the connector metadata.

This function should be called by the model runner every time after the model execution.

###

`ensure_cache_available(request, num_computed_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.ensure_cache_available)

Ensure encoder cache items are available for the given request. May initiate asynchronous transfers for items not yet local.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.ensure_cache_available(request))

) –[Request](https://docs.vllm.ai/v1/request/#vllm.v1.request.Request)the request whose multimodal features to check.

-

(`num_computed_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.ensure_cache_available(num_computed_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)tokens already covered by cached KV blocks.


Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if all items are ready or no transfer is needed.

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)False if any items are still in transit (request should be deferred).


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`get_ec_connector_stats()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.get_ec_connector_stats)

Get the EC connector stats collected during the last interval.

Callable on either a worker-side or scheduler-side connector instance: the worker-side instance reports stats gathered during cache save/load, while the scheduler-side instance reports stats gathered during scheduling decisions.

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`get_finished(finished_req_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.get_finished)

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


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`has_cache_item(identifier)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.has_cache_item)

Check if a single encoder cache exists.

Parameters:

Returns:

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`has_pending_push_work()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.has_pending_push_work)

Return True if the connector has push-mode work that requires the engine main loop to keep stepping (e.g. for EPD, Producer has push work when Xfer is in progress - Consumer is reading it). This mirrors exactly the KV Connector's has_pending_push_work().

Connectors that don't implement push-based EC transfer should leave this as False.

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`register_caches(ec_caches)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.register_caches)

Initialize with the EC caches.

Parameters:

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`request_finished(request)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.request_finished)

Called when a request has finished, before its encoder cache is freed.

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)True if the request is being saved/sent asynchronously and cached

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | Noneshould not be freed until the request_id is returned from

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]get_finished().


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`save_caches(encoder_cache, mm_hash, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.save_caches)

Save the encoder cache to the connector.

This method saves the encoder cache from the worker's local storage to shared storage or another external connector.

Parameters:

-

(`encoder_cache`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.save_caches(encoder_cache))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]A dictionary mapping multimodal data hashes (

`mm_hash`

) to encoder cache tensors. -

(`mm_hash`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.save_caches(mm_hash))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The hash of the multimodal data whose cache is being saved.

-

(`kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.save_caches(kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)`{}`

) –Additional keyword arguments for the connector.


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.shutdown)

Shutdown the connector. This is called when the process is shutting down to ensure that all the async operations are completed and the connector is cleaned up properly.

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`start_load_caches(encoder_cache, **kwargs)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_load_caches)

Start loading the cache from the connector into vLLM's encoder cache.

This method loads the encoder cache based on metadata provided by the scheduler. It is called before `_gather_mm_embeddings`

for the EC Connector. For EC, the `encoder_cache`

and `mm_hash`

are stored in `kwargs`

.

Parameters:

-

(`encoder_cache`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_load_caches(encoder_cache))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]A dictionary mapping multimodal data hashes (

`mm_hash`

) to encoder cache tensors. -

(`kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_load_caches(kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)`{}`

) –Additional keyword arguments for the connector.


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`start_save_caches(**kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_save_caches)

###

`start_worker_services()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.start_worker_services)

###

`take_unavailable_requests()`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.take_unavailable_requests)

Request IDs whose encoder inputs the connector can no longer obtain.

The Scheduler fails these; re-issuing the request re-runs the encode.

###

`update_connector_output(connector_output)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_connector_output)

Update ECConnector state from worker-side connectors output.

Parameters:

-

(`connector_output`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_connector_output(connector_output))`ECConnectorOutput`

) –the worker-side connectors output.


## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`update_state_after_alloc(request, index)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_state_after_alloc)

###

`update_state_after_free(request, index)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase.update_state_after_free)

##

`ECConnectorMetadata`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorMetadata)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract Metadata used to communicate between the Scheduler ECConnector and Worker ECConnector.

##

`ECConnectorWorkerMetadata`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorWorkerMetadata)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Abstract Metadata used to communicate back Worker ECConnector -> Scheduler ECConnector.

Each worker can output its own metadata. For a single engine step, all metadata objects returned by workers will be aggregated using the `aggregate`

method below, before being passed to the Scheduler ECConnector.

Methods:

-
–[aggregate](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorWorkerMetadata.aggregate)Aggregate metadata with another

`ECConnectorWorkerMetadata`

object.

## Source code in `vllm/distributed/ec_transfer/ec_connector/base.py`


###

`aggregate(other)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorWorkerMetadata.aggregate)

Aggregate metadata with another `ECConnectorWorkerMetadata`

object.