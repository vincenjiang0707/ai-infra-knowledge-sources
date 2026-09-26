source: https://docs.vllm.ai/en/latest/api/vllm/distributed/ec_transfer/ec_connector/example_connector/
lastmod: 2026-09-24

#

`vllm.distributed.ec_transfer.ec_connector.example_connector`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector)

Classes:

##

`ECExampleConnector`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector)

Bases: [ECConnectorBase](https://docs.vllm.ai/base/#vllm.distributed.ec_transfer.ec_connector.base.ECConnectorBase)

Methods:

-
–[build_connector_meta](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.build_connector_meta)Build the connector metadata for this step.

-
–[has_cache_item](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.has_cache_item)Check if cache exist externally for the media.

-
–[request_finished](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.request_finished)Report each item's cache key and grid so a consumer can skip the

-
–[save_caches](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.save_caches)Save the encoder cache to the connector.

-
–[start_load_caches](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.start_load_caches)Start loading the cache from the connector into vLLM's encoder cache.

-
–[update_state_after_alloc](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.update_state_after_alloc)Update ECConnector state after encoder cache allocation.


## Source code in `vllm/distributed/ec_transfer/ec_connector/example_connector.py`


|
|

###

`_found_match_for_mm_data(mm_hash)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector._found_match_for_mm_data)

Check if the cache is hit for the request.

###

`_generate_filename_debug(mm_hash)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector._generate_filename_debug)

Return the full path of the safetensors file for this mm_hash. Ensures the parent directory exists because `_generate_foldername_debug`

is called with its default (`create_folder=True`

).

## Source code in `vllm/distributed/ec_transfer/ec_connector/example_connector.py`


###

`_generate_foldername_debug(mm_hash, create_folder=True)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector._generate_foldername_debug)

Return the folder in which the cache for this mm_hash lives. If `create_folder`

is True (default) the directory is created recursively the first time it is needed.

## Source code in `vllm/distributed/ec_transfer/ec_connector/example_connector.py`


###

`build_connector_meta(scheduler_output)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.build_connector_meta)

Build the connector metadata for this step.

This function should NOT modify any fields in the scheduler_output. Also, calling this function will reset the state of the connector. This only build for load mm_data only Args: scheduler_output (SchedulerOutput): the scheduler output object.

## Source code in `vllm/distributed/ec_transfer/ec_connector/example_connector.py`


###

`has_cache_item(identifier)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.has_cache_item)

Check if cache exist externally for the media.

Parameters:

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)Bool indicate that media exists in cache or not


## Source code in `vllm/distributed/ec_transfer/ec_connector/example_connector.py`


###

`request_finished(request)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.request_finished)

Report each item's cache key and grid so a consumer can skip the image transform.

A consumer only needs the grid to size the prompt's placeholder range; the embedding itself arrives through this connector. Reporting the grid the producer actually computed keeps the two sides in agreement without the caller re-deriving it from the raw media.

## Source code in `vllm/distributed/ec_transfer/ec_connector/example_connector.py`


###

`save_caches(encoder_cache, mm_hash, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.save_caches)

Save the encoder cache to the connector.

This method saves the encoder cache from the worker's local storage to shared storage or another external connector.

Parameters:

-

(`encoder_cache`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.save_caches(encoder_cache))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), Tensor]A dictionary mapping multimodal data hashes (

`mm_hash`

) to encoder cache tensors. -

(`mm_hash`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.save_caches(mm_hash))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)The hash of the multimodal data whose cache is being saved.

-

(`kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.save_caches(kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)`{}`

) –Additional keyword arguments for the connector.


## Source code in `vllm/distributed/ec_transfer/ec_connector/example_connector.py`


###

`start_load_caches(encoder_cache, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.start_load_caches)

Start loading the cache from the connector into vLLM's encoder cache.

This method loads the encoder cache based on metadata provided by the scheduler. It is called before `_gather_mm_embeddings`

for the EC Connector. For EC, the `encoder_cache`

and `mm_hash`

are stored in `kwargs`

.

Parameters:

-

(`encoder_cache`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.start_load_caches(encoder_cache))

) –[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str), Tensor]A dictionary mapping multimodal data hashes (

`mm_hash`

) to encoder cache tensors. -

(`kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.start_load_caches(kwargs))

, default:[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)`{}`

) –Additional keyword arguments for the connector.


## Source code in `vllm/distributed/ec_transfer/ec_connector/example_connector.py`


###

`update_state_after_alloc(request, index)`

[¶](https://docs.vllm.ai#vllm.distributed.ec_transfer.ec_connector.example_connector.ECExampleConnector.update_state_after_alloc)

Update ECConnector state after encoder cache allocation.