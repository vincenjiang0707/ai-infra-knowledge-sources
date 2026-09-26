source: https://docs.vllm.ai/en/latest/api/vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine/
lastmod: 2026-09-24

#

`vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine)

Classes:

-
–[MoRIIOWrapper](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper)Wrapper for MoRIIO engine operations.

-
–[MoRIIOWriter](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter)Handles write operations for KV cache transfers.


##

`MoRIIOWrapper`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper)

Wrapper for MoRIIO engine operations.

Handles both producer and consumer roles for KV cache transfers.

Parameters:

-

(`moriio_engine`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper(moriio_engine))`IOEngine | None`

, default:`None`

) –MoRIIO engine instance

-

(`tp_rank`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper(tp_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Tensor parallel rank

-

(`dp_rank`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper(dp_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Data parallel rank


Methods:

-
–[poll_transfer_batch](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper.poll_transfer_batch)Non-blocking verdict over every status of one request.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


|
|

###

`_handle_message(msg)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper._handle_message)

Handles incoming messages from remote nodes.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_poll_transfers_until_done(transfers_to_wait)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper._poll_transfers_until_done)

Fallback for mori builds without the batched wait.

Gives failure precedence over pending: once any status has failed the request is lost, so waiting out the remaining ones would only delay the barrier by up to transfer_timeout.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`poll_transfer_batch(transfer_statuses)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWrapper.poll_transfer_batch)

Non-blocking verdict over every status of one request.

Judging a request by its newest status alone calls it done while an earlier layer is unfinished or already failed; failures do land on layers other than the last, because _post_read_with_backoff returns a failed status when the send queue never drains.

This stays a Python scan so it does not drive the backend's progress callback from the engine thread alongside MoRIIO's own poller.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


##

`MoRIIOWriter`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter)

Handles write operations for KV cache transfers.

WRITE mode state machine: D sends destination block allocation, P schedules one write per layer after the layer CUDA event, P seals the scheduled write count after forward, then P notifies D and releases P blocks after all scheduled writes complete.

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.__init__)Initialize the writer.

-
–[ensure_worker_started](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.ensure_worker_started)Ensure the background write worker is running.

-
–[schedule_write](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.schedule_write)Schedule a write task.

-
–[seal_pending_transfers](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.seal_pending_transfers)Seal expected WRITE counts after the model forward has run.


Attributes:

-
([worker](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.worker)

) –[MoRIIOConnectorWorker](https://docs.vllm.ai/moriio_connector/#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_connector.MoRIIOConnectorWorker)Get the worker instance.


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


|
|

###

`worker`

`property`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.worker)

Get the worker instance.

Returns:

-

–[MoRIIOConnectorWorker](https://docs.vllm.ai/moriio_connector/#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_connector.MoRIIOConnectorWorker)The parent worker instance


Raises:

-

–[RuntimeError](https://docs.python.org/3/builtins/exceptions.html#RuntimeError)If worker has been garbage collected


###

`__init__(worker)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.__init__)

Initialize the writer.

Parameters:

-

(`worker`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.__init__(worker))

) –[MoRIIOConnectorWorker](https://docs.vllm.ai/moriio_connector/#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_connector.MoRIIOConnectorWorker)Reference to the parent worker


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_do_layer_write(plan, sessions)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._do_layer_write)

Perform the actual layer write.

Parameters:

-

(`plan`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._do_layer_write(plan))

) –[LayerTransferPlan](https://docs.vllm.ai/moriio_common/#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.LayerTransferPlan)The transfer plan

-

(`sessions`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._do_layer_write(sessions))

) –[list](https://docs.python.org/3/builtins/stdtypes.html#list)List of transfer sessions


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_execute_write_task(task)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._execute_write_task)

Execute a single write task.

Parameters:

-

(`task`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._execute_write_task(task))`WriteTask`

) –The write task to execute


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_finalize_if_complete(transfer_id, request_info)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._finalize_if_complete)

Finalize transfer if all scheduled writes are complete.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_get_remote_alloc_info(transfer_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._get_remote_alloc_info)

Get remote allocation info for a request.

Parameters:

Returns:

-

–[RemoteAllocInfo](https://docs.vllm.ai/moriio_common/#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RemoteAllocInfo)Remote allocation information


Raises:

-

–[KeyError](https://docs.python.org/3/builtins/exceptions.html#KeyError)If allocation info is missing


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_is_remote_ready(task)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._is_remote_ready)

###

`_mark_request_done(transfer_id)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._mark_request_done)

Mark a request done so its blocks are freed, even on transfer failure.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_mark_write_done(transfer_id, request_info)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._mark_write_done)

Record one completed WRITE task and finalize if sealed.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_prepare_transfer_plan(task, request_info, remote_moriio_meta)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._prepare_transfer_plan)

Prepare the transfer plan for a layer.

Parameters:

-

(`task`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._prepare_transfer_plan(task))`WriteTask`

) –The write task

-

(`request_info`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._prepare_transfer_plan(request_info))

) –[RemoteAllocInfo](https://docs.vllm.ai/moriio_common/#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.RemoteAllocInfo)Remote allocation information

-

(`remote_moriio_meta`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._prepare_transfer_plan(remote_moriio_meta))`MoRIIOAgentMetadata`

) –Metadata of the remote MoRIIO agent


Returns:

-

–[LayerTransferPlan](https://docs.vllm.ai/moriio_common/#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_common.LayerTransferPlan)The transfer plan


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_process_deferred_tasks()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._process_deferred_tasks)

Process tasks that were previously deferred.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`_write_worker_loop()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter._write_worker_loop)

Main loop for the write worker thread.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`ensure_worker_started()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.ensure_worker_started)

Ensure the background write worker is running.

## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`schedule_write(task)`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.schedule_write)

Schedule a write task.

Parameters:

-

(`task`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.schedule_write(task))`WriteTask`

) –The write task to schedule


## Source code in `vllm/distributed/kv_transfer/kv_connector/v1/moriio/moriio_engine.py`


###

`seal_pending_transfers()`

[¶](https://docs.vllm.ai#vllm.distributed.kv_transfer.kv_connector.v1.moriio.moriio_engine.MoRIIOWriter.seal_pending_transfers)

Seal expected WRITE counts after the model forward has run.

`save_kv_layer`

is only invoked for attention layers whose backend uses the standard KV connector hook. Hybrid models can register more KV cache tensors than the number of hooks that fire in a forward, so WRITE completion must be based on the tasks actually queued for the transfer.