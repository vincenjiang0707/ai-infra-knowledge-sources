source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common/
lastmod: 2026-09-23

#

`vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common)

Classes:

-
–[AtomicCounter](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.AtomicCounter)Thread-safe atomic counter for round-robin operations.

-
–[HF3FSConnectorMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSConnectorMetadata)Container for HF3FS connector metadata.

-
–[HF3FSRequestMetadata](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSRequestMetadata)Metadata for a single request in HF3FS connector.

-
–[LoadBlockInfo](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.LoadBlockInfo)Operation for loading blocks from external storage.

-
–[RequestSchedulingState](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState)Unified request scheduling state management.

-
–[SaveBlockInfo](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.SaveBlockInfo)Operation for saving blocks to external storage.


##

`AtomicCounter`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.AtomicCounter)

Thread-safe atomic counter for round-robin operations.

Methods:

-
–[next](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.AtomicCounter.next)Get next value in round-robin fashion.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`


###

`next()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.AtomicCounter.next)

##

`HF3FSConnectorMetadata`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSConnectorMetadata)

Bases: [KVConnectorMetadata](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorMetadata)

Container for HF3FS connector metadata.

Methods:

-
–[add_request](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSConnectorMetadata.add_request)Add request to metadata.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`


##

`HF3FSRequestMetadata`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSRequestMetadata)

Metadata for a single request in HF3FS connector.

Methods:

-
–[from_scheduling_state](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSRequestMetadata.from_scheduling_state)Create request metadata from scheduling state.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`


###

`from_scheduling_state(state, block_size, load_op=None, skip_leading_blocks=None)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.HF3FSRequestMetadata.from_scheduling_state)

Create request metadata from scheduling state.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`


##

`LoadBlockInfo`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.LoadBlockInfo)

Operation for loading blocks from external storage.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`


##

`RequestSchedulingState`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState)

Unified request scheduling state management.

Methods:

-
–[is_ready_to_load](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.is_ready_to_load)Check if request is ready for loading.

-
–[needs_loading](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.needs_loading)Check if request needs loading.

-
–[update_tokens_and_blocks](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.update_tokens_and_blocks)Update with new tokens and blocks.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`


###

`_normalize_block_ids(block_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState._normalize_block_ids)

Normalize block_ids to list format.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/utils/common.py`


###

`is_ready_to_load()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.is_ready_to_load)

###

`needs_loading()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.needs_loading)

###

`update_tokens_and_blocks(new_token_ids, new_block_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.utils.common.RequestSchedulingState.update_tokens_and_blocks)

Update with new tokens and blocks.