source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector)

Classes:

-
–[FlexKVConnectorV1](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1)KV Connector that offloads KV cache to FlexKV.


##

`FlexKVConnectorV1`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1)

Bases: [KVConnectorBase_V1](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorBase_V1)

KV Connector that offloads KV cache to FlexKV.

FlexKV is a distributed KV Store and multi-level cache management system designed for ultra-large-scale LLM inference. It supports offloading KV cache to CPU memory, SSD, and remote storage.

## Installation

See https://github.com/taco-project/FlexKV for installation instructions. Quick start::

`git clone `[[email protected]](https://docs.vllm.ai/cdn-cgi/l/email-protection):taco-project/FlexKV.git
cd FlexKV && bash build.sh


## Configuration

Pass `kv_connector="FlexKVConnectorV1"`

via `--kv-transfer-config`

::

```
--kv-transfer-config '{"kv_connector":"FlexKVConnectorV1","kv_role":"kv_both"}'
```


Methods:

-
–[build_connector_meta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.build_connector_meta)Build the connector metadata for this step.

-
–[get_block_ids_with_load_errors](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_block_ids_with_load_errors)Get the block ids that have failed to load.

-
–[get_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_finished)Notify worker-side connector of requests that have finished

-
–[get_kv_connector_stats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_kv_connector_stats)Get the KV connector stats collected during the last interval.

-
–[get_num_new_matched_tokens](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_num_new_matched_tokens)Get the number of new tokens that can be loaded from the

-
–[register_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.register_kv_caches)Initialize with the KV caches. Useful for pre-registering the

-
–[request_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.request_finished)Called when a request has finished, before its blocks are freed.

-
–[save_kv_layer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.save_kv_layer)No-op for FlexKV (currently).

-
–[start_load_kv](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.start_load_kv)No-op for FlexKV (currently).

-
–[take_events](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.take_events)Collect buffered KV cache events.

-
–[update_connector_output](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.update_connector_output)Update KVConnector state from worker-side connectors output.

-
–[update_state_after_alloc](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.update_state_after_alloc)Update KVConnector state after block allocation.

-
–[wait_for_layer_load](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.wait_for_layer_load)No-op for FlexKV (currently).

-
–[wait_for_save](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.wait_for_save)No-op for FlexKV (currently).


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


|
|

###

`build_connector_meta(scheduler_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.build_connector_meta)

Build the connector metadata for this step.

This function should NOT modify fields in the scheduler_output. Also, calling this function will reset the state of the connector.

Parameters:

-

(`scheduler_output`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.build_connector_meta(scheduler_output))`SchedulerOutput`

) –the scheduler output object.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`get_block_ids_with_load_errors()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_block_ids_with_load_errors)

Get the block ids that have failed to load.

###

`get_finished(finished_req_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_finished)

Notify worker-side connector of requests that have finished generating tokens.

Returns:

-

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | NoneTuple of (sending/saving ids, recving/loading ids) for requests

-

–[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | Nonethat have finished asynchronous transfer. The finished saves/sends

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None,[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None]req ids must belong to a set provided in a call to this method

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None,[set](https://docs.python.org/3/builtins/stdtypes.html#set)[[str](https://docs.python.org/3/builtins/stdtypes.html#str)] | None](this call or a prior one).


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`get_kv_connector_stats()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_kv_connector_stats)

Get the KV connector stats collected during the last interval.

###

`get_num_new_matched_tokens(request, num_computed_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_num_new_matched_tokens)

Get the number of new tokens that can be loaded from the external KV cache beyond `num_computed_tokens`

.

Parameters:

-

(`request`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_num_new_matched_tokens(request))

) –[Request](https://docs.vllm.ai/v1/request/#vllm.v1.request.Request)the request object.

-

(`num_computed_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.get_num_new_matched_tokens(num_computed_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)the number of locally computed tokens for this request.


Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)Tuple of (num_external_tokens, is_ready) where

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)num_external_tokens is the number of additional tokens that

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[bool](https://docs.python.org/3/builtins/functions.html#bool)]can be loaded from the external KV cache.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`register_kv_caches(kv_caches)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.register_kv_caches)

Initialize with the KV caches. Useful for pre-registering the KV caches in the KVConnector (e.g. for NIXL).

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`request_finished(request, block_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.request_finished)

Called when a request has finished, before its blocks are freed.

Returns:

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)Tuple of (async_save, kv_transfer_params) where async_save is

-

–[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | NoneTrue if the request is being saved/sent asynchronously and blocks

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]should not be freed until the request_id is returned from

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]meth:

`get_finished`

. kv_transfer_params is an optional dict of -

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[bool](https://docs.python.org/3/builtins/functions.html#bool),[dict](https://docs.python.org/3/builtins/stdtypes.html#dict)[[str](https://docs.python.org/3/builtins/stdtypes.html#str),[Any](https://docs.python.org/3/library/typing.html#typing.Any)] | None]KVTransferParams to be included in the request outputs.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`save_kv_layer(layer_name, kv_layer, attn_metadata, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.save_kv_layer)

No-op for FlexKV (currently).

FlexKV offloads KV cache asynchronously from the scheduler side after a request finishes (see `request_finished`

). It does not intercept individual layer tensors during the forward pass.

This hook is retained to satisfy `KVConnectorBase_V1`

and as an extension point for future per-layer async offload support.

Parameters:

-

(`layer_name`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.save_kv_layer(layer_name))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)the name of the layer (unused).

-

(`kv_layer`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.save_kv_layer(kv_layer))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)the paged KV buffer (unused).

-

(`attn_metadata`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.save_kv_layer(attn_metadata))`AttentionMetadata`

) –the attention metadata (unused).

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.save_kv_layer(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –additional arguments (unused).


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`start_load_kv(forward_context, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.start_load_kv)

No-op for FlexKV (currently).

FlexKV manages all KV transfers on the **scheduler side** via `build_connector_meta`

(which calls `launch_tasks`

) and `update_connector_output`

(which polls `query_finished_task`

). KV blocks are transferred directly between the FlexKV server and vLLM's GPU memory without worker-side intervention during the forward pass — similar to how NIXL operates.

These worker-side hooks are kept (rather than omitted) to satisfy the `KVConnectorBase_V1`

interface contract and to serve as extension points for a future worker-side layer-pipelining path.

Parameters:

-

(`forward_context`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.start_load_kv(forward_context))

) –[ForwardContext](https://docs.vllm.ai/forward_context/#vllm.forward_context.ForwardContext)the forward context.

-

(`**kwargs`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.start_load_kv(**kwargs))

, default:[Any](https://docs.python.org/3/library/typing.html#typing.Any)`{}`

) –additional arguments (unused).


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`take_events()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.take_events)

Collect buffered KV cache events.

Returns:

-

–[Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable)[[KVCacheEvent](https://docs.vllm.ai/kv_events/#vllm.distributed.kv_events.KVCacheEvent)]New KV cache events since the last call.


###

`update_connector_output(connector_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.update_connector_output)

Update KVConnector state from worker-side connectors output.

Parameters:

-

(`connector_output`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.update_connector_output(connector_output))`KVConnectorOutput`

) –the worker-side connectors output.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`update_state_after_alloc(request, blocks, num_external_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.update_state_after_alloc)

Update KVConnector state after block allocation.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`wait_for_layer_load(layer_name)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.wait_for_layer_load)

No-op for FlexKV (currently).

FlexKV manages all KV transfers on the scheduler side. This hook is retained for `KVConnectorBase_V1`

API compatibility.

Parameters:

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/flexkv_connector.py`


###

`wait_for_save()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.flexkv_connector.FlexKVConnectorV1.wait_for_save)

No-op for FlexKV (currently).

KV offload tasks are tracked asynchronously by the scheduler connector via `request_finished`

/ `query_finished_task`

. There is no pending worker-side save to wait for at forward-context exit.

Retained to satisfy `KVConnectorBase_V1`

and as an extension point for future worker-side save-completion signalling.