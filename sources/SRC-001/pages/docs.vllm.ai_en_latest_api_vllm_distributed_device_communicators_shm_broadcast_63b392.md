source: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/shm_broadcast/
lastmod: 2026-09-24

#

`vllm.distributed.device_communicators.shm_broadcast`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast)

Classes:

-
–[MessageQueue](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue) -
–[ShmRingBuffer](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.ShmRingBuffer) -
–[SpinCondition](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.SpinCondition)This class implements an interface similar to a threading.Condition. It


Functions:

-
–[check_shm_free_space](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.check_shm_free_space)Raise if SHM cannot fit a shared segment and log cgroup headroom.

-
–[memory_fence](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.memory_fence)Full memory barrier for shared memory synchronization.


##

`MessageQueue`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue)

Classes:

Methods:

-
–[create_from_process_group](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group)Creates a MessageQueue for a distributed process group with one writer and

-
–[create_from_process_group_single_reader](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group_single_reader)Creates a MessageQueue for a process group with a single reader.

-
–[dequeue](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.dequeue)Read from message queue with optional timeout (in seconds)

-
–[enqueue](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.enqueue)Write to message queue with optional timeout (in seconds)

-
–[shutdown](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.shutdown)If this is an idle reader, wakes it up so it can clean up and shut

-
–[wait_until_ready](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.wait_until_ready)This is a collective operation. All processes (including the


## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


|
|

###

`ReadTimeoutWithWarnings`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.ReadTimeoutWithWarnings)

Methods:

-
–[should_warn](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.ReadTimeoutWithWarnings.should_warn)Returns true if it's time to log a warning for a timeout that is not

-
–[timeout_ms](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.ReadTimeoutWithWarnings.timeout_ms)Returns a timeout, capped at the recheck interval, that is:


## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


####

`should_warn()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.ReadTimeoutWithWarnings.should_warn)

Returns true if it's time to log a warning for a timeout that is not indefinite

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


####

`timeout_ms()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.ReadTimeoutWithWarnings.timeout_ms)

Returns a timeout, capped at the recheck interval, that is: - min(time to deadline, time to next warning) if we're logging warnings - time to deadline, if we're not logging warnings - recheck interval if the timeout is None and we're not logging warnings - raise TimeoutError if we are past the deadline

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


###

`create_from_process_group(pg, max_chunk_bytes, max_chunks, writer_rank=0, external_writer_handle=None, blocking=True)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group)

Creates a MessageQueue for a distributed process group with one writer and multiple readers.

This method is designed for scenarios where one process (the writer) sends messages, and all other processes (the readers) receive messages. It sets up the shared memory buffer and socket communication handles accordingly, and broadcasts the handle from the writer to all readers.

Parameters:

-

(`pg`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group(pg))`ProcessGroup |`

) –[StatelessProcessGroup](https://docs.vllm.ai/utils/#vllm.distributed.utils.StatelessProcessGroup)The torch distributed process group.

-

(`max_chunk_bytes`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group(max_chunk_bytes))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum size in bytes for each chunk in the buffer.

-

(`max_chunks`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group(max_chunks))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of chunks in the buffer.

-

(`writer_rank`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group(writer_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –The global rank that will act as the writer. Defaults to 0.

-

(`external_writer_handle`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group(external_writer_handle))`Handle`

, default:`None`

) –Used when there is a handle from an external Message Queue. If provided, use this handle to init PG writer message queue instead of creating a new one. Defaults to None.

-

(`blocking`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group(blocking))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`True`

) –If True, blocks until all processes are ready. Defaults to True.


Returns:

-
(`MessageQueue`


) –[MessageQueue](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue)The MessageQueue instance for the calling process.


## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


|
|

###

`create_from_process_group_single_reader(pg, max_chunk_bytes, max_chunks, reader_rank=0, blocking=False)`

`staticmethod`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group_single_reader)

Creates a MessageQueue for a process group with a single reader.

This method is designed for scenarios where only one process (the reader) will consume messages, and all other processes are writers. It sets up the shared memory buffer and communication handles accordingly, and gathers the handles from all processes to the reader.

Parameters:

-

(`pg`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group_single_reader(pg))`ProcessGroup`

) –The torch distributed process group.

-

(`max_chunk_bytes`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group_single_reader(max_chunk_bytes))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum size in bytes for each chunk in the buffer.

-

(`max_chunks`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group_single_reader(max_chunks))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum number of chunks in the buffer.

-

(`reader_rank`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group_single_reader(reader_rank))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –The global rank that will act as the reader. Defaults to 0.

-

(`blocking`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.create_from_process_group_single_reader(blocking))

, default:[bool](https://docs.python.org/3/builtins/functions.html#bool)`False`

) –If True, blocks until all processes are ready. Defaults to False.


Returns:

-

–[MessageQueue](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue)tuple[MessageQueue, list[Handle]]:

-

–[list](https://docs.python.org/3/builtins/stdtypes.html#list)[Handle]The MessageQueue instance for the calling process,

-

–[tuple](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[MessageQueue](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue),[list](https://docs.python.org/3/builtins/stdtypes.html#list)[Handle]]and a list of handles (only non-empty for the reader process).


## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


###

`dequeue(timeout=None, indefinite=False)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.dequeue)

Read from message queue with optional timeout (in seconds)

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


###

`enqueue(obj, timeout=None)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.enqueue)

Write to message queue with optional timeout (in seconds)

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


###

`shutdown()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.shutdown)

If this is an idle reader, wakes it up so it can clean up and shut down

###

`wait_until_ready()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.MessageQueue.wait_until_ready)

This is a collective operation. All processes (including the readers and the writer) should call this function.

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


##

`ShmRingBuffer`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.ShmRingBuffer)

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.ShmRingBuffer.__init__)A shared memory ring buffer implementation for broadcast communication.


## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


|
|

###

`__init__(n_reader, max_chunk_bytes, max_chunks, name=None)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.ShmRingBuffer.__init__)

A shared memory ring buffer implementation for broadcast communication. Essentially, it is a queue where only one will `enqueue`

and multiple will `dequeue`

. The max size of each item, together with the max number of items that can be stored in the buffer are known in advance. In this case, we don't need to synchronize the access to the buffer.

## Buffer memory layout

data metadata | | | (current_idx) | (current_idx) v v

+-------------------------------+----------------------------------------+ | chunk0 | chunk1 | ... | chunk | metadata0 | metadata1 | ... | metadata | +-------------------------------+----------------------------------------+ | max_chunks x max_chunk_bytes | max_chunks x (1 + n_reader) bytes |

metadata memory layout: each byte is a flag, the first byte is the written flag, and the rest are reader flags. The flags are set to 0 by default. +--------------+--------------+--------------+-----+--------------+ | written_flag | reader0_flag | reader1_flag | ... | readerN_flag | +--------------+--------------+--------------+-----+--------------+

The state of metadata is as follows:

(case 1) 0???...???: the block is not written yet, cannot read, can write (case 2) 1000...000: the block is just written, can read, cannot write (case 3) 1???...???: the block is written and read by some readers, can read if not read, cannot write (case 4) 1111...111: the block is written and read by all readers, cannot read, can write

State transition for readers:

When a reader finds a block that it can read (case 2 or 3), it can yield the block for caller to read. Only after the caller finishes reading the block, the reader can mark the block as read. Readers only mark the block as read (from 0 to 1), the writer marks the block as ready to read (from 1 to 0).

State transition for writer:

When the writer writes to a block (case 1 or 4), it first resets the written flag to 0, converting either case to case 1. Then it can yield the block for caller to write. After the caller finishes writing the block, the writer can reset the reader flags to 0, and mark the block as written (from 0 to 1). NOTE: the order is important here, first reset the reader flags (so that we are still in case 1), then mark the block as written. The state transition is atomic. If we do it in the reverse order, it will go through case 3 and then back to case 2, and readers might read the intermediate case 3, which is not correct.

During creation, `name`

is None and the buffer is created. We can pass the created object to other processes by pickling it. The other processes will get the name of the shared memory and open it, so that they can access the same shared memory buffer.

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


|
|

##

`SpinCondition`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.SpinCondition)

This class implements an interface similar to a threading.Condition. It allows a writer to notify readers to wake up and read from the shared memory buffer. This notification is done over a zmq socket.

For optimal performance under load we don't want the readers to need to poll the zmq socket for every read. So the `wait`

method here will return immediately when reads are frequent, and will only enter "idle mode" and await a notification on the zmq socket after a period of inactivity. This allows the readers to spin quickly, hence "SpinCondition".

To support clean shutdown, a separate thread in the reader's process must be able to wake the reader so that it can exit. A separate cancel() method is implemented with an in-process socket to allow this interruption.

Methods:

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


|
|

###

`notify()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.SpinCondition.notify)

###

`wait(timeout_ms=None)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.SpinCondition.wait)

Wait for data on the shared memory buffer.

Yields the scheduler then returns immediately if it has been less than self.busy_loop_s since the last read.

Otherwise, enters idle mode and awaits a socket ping for at most `timeout_ms`

milliseconds, or indefinitely if timeout_ms is None.

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


##

`_rebuild_tensor(buf, shape, dtype_str)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast._rebuild_tensor)

Rebuild a tensor from an out-of-band pickle buffer.

Counterpart of `_reduce_tensor`

. Note that pickle passes the original buffer-providing object from `loads(buffers=...)`

straight to this function (no `PickleBuffer`

wrapper on the receiving side), so `buf`

is a `zmq.Frame`

, a `memoryview`

of a shared-memory ring chunk, or `bytes`

if the buffer was serialized in-band.

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


##

`_reduce_tensor(tensor)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast._reduce_tensor)

Reduce a CPU tensor to a `PickleBuffer`

for out-of-band pickling.

`torch.Tensor.__reduce_ex__`

copies the tensor bytes into the pickle byte stream via `torch.serialization`

and never emits a `PickleBuffer`

, which defeats the out-of-band buffer handling in `MessageQueue.enqueue`

. This reducer instead exposes the tensor's memory directly, so large tensors (e.g. `prompt_embeds`

in `SchedulerOutput`

) traverse the queue without being copied into and back out of the pickled message.

## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


##

`check_shm_free_space(required_bytes, shm_path=SHM_PATH, *, allocation_name='shared-memory allocation')`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.check_shm_free_space)

Raise if SHM cannot fit a shared segment and log cgroup headroom.

Parameters:

-

(`required_bytes`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.check_shm_free_space(required_bytes))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Size of the shared-memory segment to be created.

-

(`shm_path`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.check_shm_free_space(shm_path))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`SHM_PATH`

) –Mount point backing POSIX shared memory; its filesystem check is skipped if absent.

-

(`allocation_name`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.check_shm_free_space(allocation_name))

, default:[str](https://docs.python.org/3/builtins/stdtypes.html#str)`'shared-memory allocation'`

) –Human-readable name used in errors and logs.


Raises:

-

–[RuntimeError](https://docs.python.org/3/builtins/exceptions.html#RuntimeError)If the SHM filesystem has insufficient space.


## Source code in `vllm/distributed/device_communicators/shm_broadcast.py`


##

`memory_fence()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_broadcast.memory_fence)

Full memory barrier for shared memory synchronization.

Ensures all prior memory writes are visible to other processes before any subsequent reads. This is critical for lock-free producer-consumer patterns using shared memory.

Implementation acquires and immediately releases a lock. Python's threading.Lock provides sequentially consistent memory barrier semantics across all major platforms (POSIX, Windows). This is a lightweight operation (~20ns) that guarantees: - All stores before the barrier are visible to other threads/processes - All loads after the barrier see the latest values