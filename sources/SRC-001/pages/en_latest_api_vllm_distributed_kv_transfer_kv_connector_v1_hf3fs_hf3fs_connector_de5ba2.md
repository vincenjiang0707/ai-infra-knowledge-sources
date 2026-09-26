source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector)

HF3FS KV Connector Implementation for vLLM.

This module implements a KV connector that uses the 3FS for storing and retrieving KV cache data.

Key components: 1. HF3FSConnector: Main connector implementation 2.1 AsyncOperationManager: Manages async save/load operations with background threads 2.2 HF3FSConnectorMetadata: Container for connector metadata 3. HF3FSMetadataServer: Mini Metadata server for HF3FS connector 4. HF3FSClient: 3FS Client Implementation

Classes:

-
–[AsyncOperationManager](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager)Manages async save/load operations with background threads.

-
–[HF3FSKVConnector](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector)HF3FS KV Connector implementation.

-
–[HF3FSKVConnectorStats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnectorStats)Container for transfer performance metrics.


##

`AsyncOperationManager`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager)

Manages async save/load operations with background threads.

Methods:

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager.shutdown)Clean shutdown of all background threads and resources.

-
–[submit_load_operation](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager.submit_load_operation)Submit a load operation for async execution.

-
–[submit_save_operation](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager.submit_save_operation)Submit a save operation for async execution.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


|
|

###

`_all_saves_done(request_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._all_saves_done)

Check if all save operations for a request are completed.

###

`_check_completed_loads()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._check_completed_loads)

Check for completed load operations.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_check_completed_saves(finished_req_ids)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._check_completed_saves)

Check for completed save operations.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_fail_task(operation, error_msg, request_id, future)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._fail_task)

Helper to fail task with error logging.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_handle_load_task(task)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._handle_load_task)

Handle individual load task.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_handle_save_task(task)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._handle_save_task)

Handle individual save task with proper stream synchronization.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


|
|

###

`_init_cuda_resources()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._init_cuda_resources)

Initialize CUDA streams, events and buffer allocators.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_init_worker_threads()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._init_worker_threads)

Initialize worker threads and I/O executor.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_load_worker()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._load_worker)

Background worker for handling load operations.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_save_worker()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._save_worker)

Background worker for handling save operations.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_succeed_task(operation, start_time, request_id, block_count, future)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager._succeed_task)

Helper to succeed task with logging.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager.shutdown)

Clean shutdown of all background threads and resources.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`submit_load_operation(request_id, block_ids, block_hashes)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager.submit_load_operation)

Submit a load operation for async execution.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`submit_save_operation(request_id, block_ids, block_hashes)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.AsyncOperationManager.submit_save_operation)

Submit a save operation for async execution.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


##

`HF3FSKVConnector`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector)

Bases: [KVConnectorBase_V1](https://docs.vllm.ai/base/#vllm.distributed.kv_transfer.kv_connector.v1.base.KVConnectorBase_V1)

HF3FS KV Connector implementation.

Methods:

-
–[build_connector_meta](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.build_connector_meta)Build connector metadata for scheduling step.

-
–[build_kv_connector_stats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.build_kv_connector_stats)KVConnectorStats resolution method. This method allows dynamically

-
–[get_kv_connector_stats](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.get_kv_connector_stats)Get the KV connector stats collected during the last interval.

-
–[get_num_new_matched_tokens](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.get_num_new_matched_tokens)Get number of new tokens that can be loaded from external cache.

-
–[save_kv_layer](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.save_kv_layer)HF3FSConnector does not do layerwise saving.

-
–[update_state_after_alloc](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.update_state_after_alloc)Update state after block allocation.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


|
|

###

`_align_to_block_size(num_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector._align_to_block_size)

###

`_compute_prefix_hash(token_ids, previous_hash='')`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector._compute_prefix_hash)

Compute prefix hash for token block.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_generate_block_hashes(token_ids, start_block_id, max_blocks_count=None)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector._generate_block_hashes)

Generate block hashes for token sequence.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_get_or_create_scheduling_state(request_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector._get_or_create_scheduling_state)

Get existing or create new scheduling state.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_initialize_state_from_new_request(state, request, num_tokens_to_compute)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector._initialize_state_from_new_request)

Initialize state from new request data.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_process_cached_requests(scheduler_output, metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector._process_cached_requests)

Process cached requests.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_process_new_requests(scheduler_output, metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector._process_new_requests)

Process new requests.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`_process_waiting_to_load_requests(metadata)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector._process_waiting_to_load_requests)

Process requests waiting to load.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`build_connector_meta(scheduler_output)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.build_connector_meta)

Build connector metadata for scheduling step.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`build_kv_connector_stats(data=None)`

`classmethod`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.build_kv_connector_stats)

KVConnectorStats resolution method. This method allows dynamically registered connectors to return their own KVConnectorStats object, which can implement custom aggregation logic on the data dict.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`get_kv_connector_stats()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.get_kv_connector_stats)

Get the KV connector stats collected during the last interval.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`get_num_new_matched_tokens(request, num_computed_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.get_num_new_matched_tokens)

Get number of new tokens that can be loaded from external cache.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


###

`save_kv_layer(layer_name, kv_layer, attn_metadata, **kwargs)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.save_kv_layer)

HF3FSConnector does not do layerwise saving.

###

`update_state_after_alloc(request, blocks, num_external_tokens)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnector.update_state_after_alloc)

Update state after block allocation.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


##

`HF3FSKVConnectorStats`

`dataclass`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.hf3fs.hf3fs_connector.HF3FSKVConnectorStats)

Bases: [KVConnectorStats](https://docs.vllm.ai/metrics/#vllm.distributed.kv_transfer.kv_connector.v1.metrics.KVConnectorStats)

Container for transfer performance metrics.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/hf3fs/hf3fs_connector.py`


|
|