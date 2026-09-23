source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration)

Modules:

Classes:

##

`LMCacheMPSchedulerAdapter`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter)

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.__init__)Args:

-
–[check_lookup_result](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.check_lookup_result)Check the result of a previously submitted lookup request.

-
–[cleanup_lookup_result](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.cleanup_lookup_result)Clean up lookup future for a finished request to prevent memory leak.

-
–[end_session](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.end_session)Notify LMCache server to remove the session for a finished request.

-
–[maybe_submit_lookup_request](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.maybe_submit_lookup_request)Submit a new lookup request to LMCache if there is no ongoing request.

-
–[num_blocks_per_chunk](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.num_blocks_per_chunk)Returns:


Attributes:

-
([tp_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.tp_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The tensor parallel size.

-
([worker_id](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.worker_id)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The worker id.

-
([world_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.world_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The world size.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


|
|

###

`tp_size`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.tp_size)

The tensor parallel size.

###

`worker_id`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.worker_id)

The worker id.

###

`world_size`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.world_size)

The world size.

###

`__init__(server_url, context, model_name, vllm_block_size, parallel_strategy)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.__init__)

Args: server_url: The server URL for the LMCache message queue context: The ZMQ context

model_name: The model name used for LMCache keys vllm_block_size: The block size used in vLLM parallel_strategy: The parallel strategy, which includes `use_mla`

, `world_size`

, `worker_id`

and so on

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`_create_hash_key(chunk_hash, request_id=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter._create_hash_key)

Create a hash-mode IPC cache engine key.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`_create_key(token_ids, start=0, end=0, request_id=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter._create_key)

Convert token IDs to an IPC cache engine key.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`check_lookup_result(request_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.check_lookup_result)

Check the result of a previously submitted lookup request.

Parameters:

Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)| NoneAn integer representing the total number of tokens matched

-

–[int](https://docs.python.org/3/builtins/functions.html#int)| Nonein LMCache (prefix matching), or

-

–[int](https://docs.python.org/3/builtins/functions.html#int)| NoneNone if the lookup request is not finished yet.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`cleanup_lookup_result(request_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.cleanup_lookup_result)

Clean up lookup future for a finished request to prevent memory leak.

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`end_session(request_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.end_session)

Notify LMCache server to remove the session for a finished request.

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`maybe_submit_lookup_request(request_id, block_hashes=None, token_ids=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.maybe_submit_lookup_request)

Submit a new lookup request to LMCache if there is no ongoing request.

Supports both token-based and hash-based vLLM: - token_ids: token IDs (token-based vLLM) -> single token-mode key - block_hashes: block hashes (hash-based vLLM) -> strided hash-mode keys

Exactly one of block_hashes or token_ids must be provided.

Parameters:

-

(`request_id`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.maybe_submit_lookup_request(request_id))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The ID of the lookup request. The same ID indicates it's from the same request

-

(`block_hashes`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.maybe_submit_lookup_request(block_hashes))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes)] | None`None`

) –Block hashes to lookup from LMCache (hash mode)

-

(`token_ids`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.maybe_submit_lookup_request(token_ids))

, default:[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | None`None`

) –Token IDs to lookup from LMCache (token mode)


Returns:

-
`None`

–None


## Notes

This function will have a side-effect: submitting a look up request to LMCache, which will essentially 'lock' the KV cache chunks in the LMCache for later retrieve operations. In the meantime, this function will record the lookup request, and the status of the look up request can be checked by `check_lookup_result`

.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`num_blocks_per_chunk()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPSchedulerAdapter.num_blocks_per_chunk)

Returns: The number of vllm blocks in a LMCache data chunk

##

`LMCacheMPWorkerAdapter`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter)

Methods:

-
–[batched_submit_retrieve_requests](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_retrieve_requests)Submit a batched retrieve request to LMCache.

-
–[batched_submit_store_requests](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_store_requests)Submit a batched store request to LMCache.

-
–[get_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.get_finished)Check and get the finished store and retrieve requests.

-
–[num_blocks_per_chunk](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.num_blocks_per_chunk)Returns:

-
–[register_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.register_kv_caches)Register the kv caches with LMCache server.

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.shutdown)Shutdown the LMCache MP worker adapter.

-
–[submit_retrieve_request](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_retrieve_request)Submit a KV cache retrieve request to LMCache.

-
–[submit_store_request](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_store_request)Submit a KV cache store request to LMCache.


Attributes:

-
([is_first_rank_of_pp_group](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.is_first_rank_of_pp_group)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Is the first rank of the pipeline parallel group.

-
([use_mla](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.use_mla)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use MLA.

-
([worker_id](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.worker_id)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The worker id.

-
([world_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.world_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The world size.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


|
|

###

`is_first_rank_of_pp_group`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.is_first_rank_of_pp_group)

Is the first rank of the pipeline parallel group.

###

`use_mla`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.use_mla)

Whether to use MLA.

###

`worker_id`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.worker_id)

The worker id.

###

`world_size`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.world_size)

The world size.

###

`_create_hash_key(chunk_hash, request_id=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter._create_hash_key)

Create a hash-mode IPC cache engine key.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`_create_key(token_ids, start=0, end=0, request_id=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter._create_key)

Convert token IDs to an IPC cache engine key.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`_update_and_get_finished_store()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter._update_and_get_finished_store)

Converge the internal states about finished stores and returns the 'safe finished store request ids' back

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`batched_submit_retrieve_requests(request_ids, ops, event)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_retrieve_requests)

Submit a batched retrieve request to LMCache.

Parameters:

-

(`request_ids`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_retrieve_requests(request_ids))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The IDs of the requests

-

(`ops`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_retrieve_requests(ops))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[LoadStoreOp](https://docs.vllm.ai/multi_process_adapter/#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.multi_process_adapter.LoadStoreOp)]The LoadStoreOps describing the retrieve operations. Should have the same length as request_ids

-

(`event`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_retrieve_requests(event))

) –[Event](https://pytorch.org/docs/stable/generated/torch.cuda.Event.html#torch.cuda.Event)The CUDA event that is recorded after the current model inference step


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`batched_submit_store_requests(request_ids, ops, event)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_store_requests)

Submit a batched store request to LMCache.

Parameters:

-

(`request_ids`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_store_requests(request_ids))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]The IDs of the requests

-

(`ops`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_store_requests(ops))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[LoadStoreOp](https://docs.vllm.ai/multi_process_adapter/#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.multi_process_adapter.LoadStoreOp)]The LoadStoreOps describing the store operations. Should have the same length as request_ids

-

(`event`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.batched_submit_store_requests(event))

) –[Event](https://pytorch.org/docs/stable/generated/torch.cuda.Event.html#torch.cuda.Event)The CUDA event that is recorded after the current model inference step


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`get_finished(finished_req_ids_from_engine)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.get_finished)

Check and get the finished store and retrieve requests.

Parameters:

-

(`finished_req_ids_from_engine`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.get_finished(finished_req_ids_from_engine))

) –[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)]the set of request ids that are reported as finished from the vLLM engine side.


Returns:

-

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneA tuple of two sets:

-

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None- The first set contains the finished store request ids. The returned store request ids MUST be seen before in the
`finished_req_ids_from_engine`

.

- The first set contains the finished store request ids. The returned store request ids MUST be seen before in the
-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None,[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None]- The second set contains the finished retrieve request ids.


## Notes

When enabling async scheduling in vLLM, the same request ID may appear multiple times in `finished_req_ids_from_engine`

. The adapter should take care of deduplicating the request IDs and only return the request IDs that have not been returned before.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


|
|

###

`num_blocks_per_chunk()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.num_blocks_per_chunk)

Returns: The number of vllm blocks in a LMCache data chunk

###

`register_kv_caches(kv_caches)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.register_kv_caches)

Register the kv caches with LMCache server.

Parameters:

-

(`kv_caches`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.register_kv_caches(kv_caches))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)]A dict of kv caches to register. The keys are the layer names and the values are the corresponding tensors.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.shutdown)

Shutdown the LMCache MP worker adapter.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`submit_retrieve_request(request_id, op, event)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_retrieve_request)

Submit a KV cache retrieve request to LMCache.

Parameters:

-

(`request_id`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_retrieve_request(request_id))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The ID of the request

-

(`op`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_retrieve_request(op))

) –[LoadStoreOp](https://docs.vllm.ai/multi_process_adapter/#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.multi_process_adapter.LoadStoreOp)The LoadStoreOp describing the retrieve operation.

-

(`event`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_retrieve_request(event))

) –[Event](https://pytorch.org/docs/stable/generated/torch.cuda.Event.html#torch.cuda.Event)The CUDA event that is recorded after the current model inference step


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`submit_store_request(request_id, op, event)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_store_request)

Submit a KV cache store request to LMCache.

Parameters:

-

(`request_id`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_store_request(request_id))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The ID of the request

-

(`op`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_store_request(op))

) –[LoadStoreOp](https://docs.vllm.ai/multi_process_adapter/#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.multi_process_adapter.LoadStoreOp)The LoadStoreOp describing the store operation.

-

(`event`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LMCacheMPWorkerAdapter.submit_store_request(event))

) –[Event](https://pytorch.org/docs/stable/generated/torch.cuda.Event.html#torch.cuda.Event)The CUDA event that is recorded after the current model inference step


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


##

`LoadStoreOp`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp)

Attributes:

-
([block_hashes](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.block_hashes)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[bytes](https://docs.python.org/3/builtins/stdtypes.html#bytes)] | NoneBlock hashes for the load/store operation (hash mode)

-
([block_ids](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.block_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Block ids for the load/store operation

-
([end](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.end)

) –[int](https://docs.python.org/3/builtins/functions.html#int)End token index (token mode only)

-
([start](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.start)

) –[int](https://docs.python.org/3/builtins/functions.html#int)Start token index (token mode only)

-
([token_ids](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.token_ids)

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)] | NoneToken IDs for the load/store operation (token mode)


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`block_hashes = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.block_hashes)

Block hashes for the load/store operation (hash mode)

###

`block_ids`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.block_ids)

Block ids for the load/store operation

###

`end = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.end)

End token index (token mode only)

###

`start = 0`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.start)

Start token index (token mode only)

###

`token_ids = None`

`class-attribute`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.LoadStoreOp.token_ids)

Token IDs for the load/store operation (token mode)

##

`ParallelStrategy`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy)

Attributes:

-
([actual_worker_id](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.actual_worker_id)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The actual worker id of the sub-process.

-
([actual_world_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.actual_world_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The actual world size.

-
([kv_worker_id](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.kv_worker_id)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The kv worker id of the sub-process, kv_worker_id may not be equal to the

-
([kv_world_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.kv_world_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The kv world size, kv_world_size may not be equal to the actual_world_size,

-
([pp_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.pp_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The pipeline parallel size.

-
([tp_size](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.tp_size)

) –[int](https://docs.python.org/3/builtins/functions.html#int)The tensor parallel size.

-
([use_mla](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.use_mla)

) –[bool](https://docs.python.org/3/builtins/functions.html#bool)Whether to use the MLA.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/lmcache_integration/multi_process_adapter.py`


###

`actual_worker_id`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.actual_worker_id)

The actual worker id of the sub-process.

###

`actual_world_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.actual_world_size)

The actual world size.

###

`kv_worker_id`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.kv_worker_id)

The kv worker id of the sub-process, kv_worker_id may not be equal to the actual_worker_id, in the case of mla, it will 'exclude' the effect of TP, the value is calculated by `extract_world_size_and_kv_rank`

in `lmcache_mp_connector.py`

.

###

`kv_world_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.kv_world_size)

The kv world size, kv_world_size may not be equal to the actual_world_size, in the case of mla, it will 'exclude' the effect of TP, the value is calculated by `extract_world_size_and_kv_rank`

in `lmcache_mp_connector.py`

.

###

`pp_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.pp_size)

The pipeline parallel size.

###

`tp_size`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.tp_size)

The tensor parallel size.

###

`use_mla`

`instance-attribute`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.lmcache_integration.ParallelStrategy.use_mla)

Whether to use the MLA.