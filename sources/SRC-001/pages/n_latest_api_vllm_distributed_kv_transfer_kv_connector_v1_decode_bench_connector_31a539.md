source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector)

DecodeBenchConnector: A KV Connector for decode instance performance testing.

This connector emulates a prefill-decode disaggregated setting by filling the KV cache with dummy values, allowing measurement of decoder performance under larger input sequence lengths (ISL) in resource-limited environments.

## Usage

To use this connector for benchmarking, configure it in the kv_transfer_config:

## Example

vllm serve

```
Then run your benchmark with desired input/output lengths:
vllm bench serve --base-url http://127.0.0.1:8000 --model <model> \
--dataset-name random --random-input-len 40000 \
--random-output-len 100 --max-concurrency 10
Configuration options (via kv_connector_extra_config):
- fill_mean (float): Mean value for random normal fill (default: 0.015)
- fill_std (float): Standard deviation for random fill (default: 0.0)
Set to 0 for constant values, >0 for random sampling
```


Classes:

-
–[DecodeBenchConnector](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnector)A KV Connector for decode instance performance testing.

-
–[DecodeBenchConnectorMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorMetadata)Metadata for DecodeBenchConnector.

-
–[DecodeBenchConnectorScheduler](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler)Scheduler-side implementation for DecodeBenchConnector.

-
–[DecodeBenchConnectorWorker](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker)Worker-side implementation for DecodeBenchConnector.


##

`DecodeBenchConnector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnector)

Bases:

, [KVConnectorBase_V1](https://docs.vllm.ai/#vllm.distributed.kv_transfer.kv_connector.v1.KVConnectorBase_V1)[SupportsHMA](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.SupportsHMA)

A KV Connector for decode instance performance testing.

This connector fills the KV cache with dummy values to emulate a prefill-decode disaggregated setting, enabling performance testing of the decoder with larger input sequence lengths.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


|
|

##

`DecodeBenchConnectorMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorMetadata)

Bases: [KVConnectorMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorMetadata)

Metadata for DecodeBenchConnector.

Contains information about which requests need their KV cache filled with dummy values for benchmarking purposes.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


##

`DecodeBenchConnectorScheduler`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler)

Scheduler-side implementation for DecodeBenchConnector.

Methods:

-
–[build_connector_meta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.build_connector_meta)Build metadata containing information about which blocks to fill

-
–[get_num_new_matched_tokens](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.get_num_new_matched_tokens)For new requests, return the number of tokens that should be filled

-
–[request_finished](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.request_finished)Called when a request has finished. Clean up any state.

-
–[update_state_after_alloc](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.update_state_after_alloc)Called after blocks are allocated. Store the block IDs so we can


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


|
|

###

`build_connector_meta(scheduler_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.build_connector_meta)

Build metadata containing information about which blocks to fill with dummy KV values.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


###

`get_num_new_matched_tokens(request, num_computed_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.get_num_new_matched_tokens)

For new requests, return the number of tokens that should be filled with dummy KV cache values.

Returns:

-

–[int](https://docs.python.org/3/builtins/functions.html#int)(num_tokens_to_fill, is_async)

-

–[bool](https://docs.python.org/3/builtins/functions.html#bool)- num_tokens_to_fill: number of uncomputed tokens minus 1 (we fill everything except the last token for decode)

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[int](https://docs.python.org/3/builtins/functions.html#int),[bool](https://docs.python.org/3/builtins/functions.html#bool)]- is_async: False (synchronous filling)


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


###

`request_finished(request)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.request_finished)

Called when a request has finished. Clean up any state.

###

`update_state_after_alloc(request, blocks, num_external_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorScheduler.update_state_after_alloc)

Called after blocks are allocated. Store the block IDs so we can fill them with dummy values.

Supports both single- and multi-group KV cache configurations.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


|
|

##

`DecodeBenchConnectorWorker`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker)

Worker-side implementation for DecodeBenchConnector.

Methods:

-
–[register_kv_caches](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker.register_kv_caches)Store references to the KV cache tensors.

-
–[start_fill_kv](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker.start_fill_kv)Fill the allocated KV cache blocks with dummy values.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


|
|

###

`_fill_block_tensor(kv_cache, block_ids, fill_mean, fill_std)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_block_tensor)

Fill the requested block rows of a block-indexed KV cache tensor.

Parameters:

-

(`kv_cache`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_block_tensor(kv_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A KV cache tensor whose first dim is num_blocks.

-

(`block_ids`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_block_tensor(block_ids))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]Block IDs to fill. IDs that are out of range for this tensor's first dim are ignored.

-

(`fill_mean`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_block_tensor(fill_mean))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Mean value for the fill.

-

(`fill_std`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_block_tensor(fill_std))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Standard deviation for the fill.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


###

`_fill_blocks(group_idx, block_ids, num_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_blocks)

Fill specified blocks with dummy values for a specific KV cache group.

Parameters:

-

(`group_idx`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_blocks(group_idx))

) –[int](https://docs.python.org/3/builtins/functions.html#int)The KV cache group index to fill

-

(`block_ids`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_blocks(block_ids))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)[[int](https://docs.python.org/3/builtins/functions.html#int)]List of block IDs to fill in this group

-

(`num_tokens`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_blocks(num_tokens))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Total number of tokens to fill across these blocks


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


###

`_fill_state_tensor(kv_cache, fill_mean, fill_std)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_state_tensor)

Fill an entire non-block-indexed state tensor with dummy values.

Hybrid / linear-attention layers (e.g. Mamba, Kimi Delta Attention) store their per-layer state as tensors with no num_blocks dimension, so the whole tensor is filled with the same constant or random values used for block fills, rather than selected block rows.

Parameters:

-

(`kv_cache`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_state_tensor(kv_cache))

) –[Tensor](https://pytorch.org/docs/stable/tensors.html#torch.Tensor)A state tensor to fill in its entirety.

-

(`fill_mean`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_state_tensor(fill_mean))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Mean value for the fill.

-

(`fill_std`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker._fill_state_tensor(fill_std))

) –[float](https://docs.python.org/3/builtins/functions.html#float)Standard deviation for the fill.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


###

`register_kv_caches(kv_caches)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker.register_kv_caches)

Store references to the KV cache tensors.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/decode_bench_connector.py`


###

`start_fill_kv(metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.decode_bench_connector.DecodeBenchConnectorWorker.start_fill_kv)

Fill the allocated KV cache blocks with dummy values.

This simulates having a populated KV cache from a prefill phase, allowing decode performance testing with larger context sizes.

Supports both single- and multi-group KV cache configurations.