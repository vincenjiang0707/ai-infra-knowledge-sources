source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector)

Classes:

-
–[ExampleHiddenStatesConnector](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector)Simple debug implementation of a HiddenStatesConnector.


Functions:

-
–[cleanup_hidden_states](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.cleanup_hidden_states)Clean up hidden states file and lock file after loading.

-
–[extract_from_kv_cache](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.extract_from_kv_cache)Extract data from KV cache.

-
–[load_hidden_states](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.load_hidden_states)Load hidden states written by ExampleHiddenStatesConnector.


##

`ExampleHiddenStatesConnector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector)

Bases:

, [KVConnectorBase_V1](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorBase_V1)[SupportsHMA](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.SupportsHMA)

Simple debug implementation of a HiddenStatesConnector.

Simply extracts the hidden states from the kv cache and stores them to disk. Must be used in conjunction with the `extract_hidden_states`

spec decoding method.

Methods:

-
–[build_connector_meta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.build_connector_meta)Build the connector metadata for this step.

-
–[get_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_finished)Extract hidden states and poll DtoH-copy completion.

-
–[get_finished_count](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_finished_count)Number of

`finished_sending`

notifications expected per request. -
–[get_num_new_matched_tokens](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_num_new_matched_tokens)Get number of new tokens that can be loaded from the

-
–[get_required_kvcache_layout](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_required_kvcache_layout)Get the required KV cache layout for this connector.

-
–[request_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.request_finished)Called exactly once when a request has finished, before its blocks are

-
–[wait_for_save](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.wait_for_save)Pre-create lock files for newly arrived requests.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


|
|

###

`_find_cache_kv_group_id(kv_cache_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector._find_cache_kv_group_id)

Index of the KV cache group holding the extracted hidden states.

Located by spec type so it resolves on both scheduler and worker side.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`_get_cache_block_size(vllm_config, kv_cache_config, cache_kv_group_id)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector._get_cache_block_size)

Block size of the hidden-states group, read from its own spec.

cache_config.block_size is bumped to a common multiple for hybrid verifiers; the page-aligned hidden-states group keeps a smaller one.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`_get_copy_stream()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector._get_copy_stream)

Lazily create the copy stream (CUDA must be initialized).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`_on_write_done(req_id, future)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector._on_write_done)

Surface any exception from the disk-write thread and drop the completed future from the in-flight tracking dict.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`_submit_async_write(pending)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector._submit_async_write)

Extract hidden states from KV cache and submit async DtoH + disk write.

Called from get_finished for each request that has finished generating.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


|
|

###

`_write_tensors(tensors, event, filename, lock_fd)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector._write_tensors)

Thread worker: wait for async DtoH copy, write to disk, release lock.

`lock_fd`

is an open file descriptor on the companion `.lock`

file with `LOCK_EX`

already held. Closing it releases the lock, which unblocks any client sleeping on `LOCK_SH`

.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`build_connector_meta(scheduler_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.build_connector_meta)

Build the connector metadata for this step.

This function should NOT modify any fields in the scheduler_output. Also, calling this function will reset the state of the connector.

Parameters:

-

(`scheduler_output`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.build_connector_meta(scheduler_output))`SchedulerOutput`

) –the scheduler output object.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`get_finished(finished_req_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_finished)

Extract hidden states and poll DtoH-copy completion.

On the worker side, connector metadata carries pending saves from the scheduler. For each one we extract from the KV cache and launch an async DtoH copy + thread-pool disk write.

We then poll accumulated finished req_ids: a request is "done sending" once its DtoH copy event is complete. The subsequent disk write may still be in flight; clients block on the per-file flock to wait for it.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`get_finished_count()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_finished_count)

Number of `finished_sending`

notifications expected per request.

Only TP rank 0 writes hidden states to disk, so each request yields a single notification. The default (`None`

) makes `KVOutputAggregator`

wait for every worker in the world size; since ranks 1..N-1 never submit a copy, the request would never be reported as finished and its blocks would be leaked forever (the scheduler then spins on `has_finished_requests()`

).

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`get_num_new_matched_tokens(request, num_computed_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_num_new_matched_tokens)

Get number of new tokens that can be loaded from the external KV cache beyond the num_computed_tokens.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_num_new_matched_tokens(request))

) –[Request](https://docs.vllm.ai/v1/request/#vllm.v1.request.Request)the request object.

-

(`num_computed_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_num_new_matched_tokens(num_computed_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of locally computed tokens for this request


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)| Nonethe number of tokens that can be loaded from the

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)external KV cache beyond what is already computed.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`get_required_kvcache_layout(vllm_config)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_required_kvcache_layout)

Get the required KV cache layout for this connector.

Parameters:

-

(`vllm_config`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.get_required_kvcache_layout(vllm_config))

) –[VllmConfig](https://docs.vllm.ai/config/#vllm.config.VllmConfig)the vllm config.


Returns:

-
(`str`


) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)| Nonethe required KV cache layout. e.g. HND, or NHD.

-

–[str](https://docs.python.org/3/builtins/stdtypes.html#str)| NoneNone if the connector does not require a specific layout.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`request_finished(request, block_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.request_finished)

Called exactly once when a request has finished, before its blocks are freed.

Returns True to delay block freeing until get_finished extracts the hidden states from the KV cache.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


###

`wait_for_save()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.ExampleHiddenStatesConnector.wait_for_save)

Pre-create lock files for newly arrived requests.

This runs on the worker BEFORE the scheduler returns the output path to the client, guaranteeing that the lock file exists (and LOCK_EX is held) by the time the client tries to open it.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


##

`cleanup_hidden_states(path, keep_hidden_states=False)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.cleanup_hidden_states)

Clean up hidden states file and lock file after loading.

If keep_hidden_states is True, only removes the lock file and keeps the hidden states file.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


##

`extract_from_kv_cache(kv_cache, slot_mapping, num_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.extract_from_kv_cache)

Extract data from KV cache.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/example_hidden_states_connector.py`


##

`load_hidden_states(path)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.example_hidden_states_connector.load_hidden_states)

Load hidden states written by ExampleHiddenStatesConnector.

Blocks (without polling) until the async write is complete by acquiring a shared flock on the companion lock file. The kernel puts the caller to sleep until the writer releases its exclusive lock.

Parameters:

Returns: