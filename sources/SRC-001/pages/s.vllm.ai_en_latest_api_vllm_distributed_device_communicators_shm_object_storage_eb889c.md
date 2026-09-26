source: https://docs.vllm.ai/en/latest/api/vllm/distributed/device_communicators/shm_object_storage/
lastmod: 2026-09-24

#

`vllm.distributed.device_communicators.shm_object_storage`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage)

Classes:

-
–[ObjectSerde](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde) -
–[SingleWriterShmObjectStorage](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage)A single-writer, multiple-reader object storage system built on top of a

-
–[SingleWriterShmRingBuffer](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer)A single-writer, multiple-reader ring buffer implementation using shared


##

`ObjectSerde`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde)

Bases: [ABC](https://docs.python.org/3/library/abc.html#abc.ABC)

Methods:

-
–[deserialize](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde.deserialize)Deserialize bytes back to an object.

-
–[serialize](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde.serialize)Serialize an object to bytes.


## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`deserialize(data)`

`abstractmethod`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde.deserialize)

##

`SingleWriterShmObjectStorage`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage)

A single-writer, multiple-reader object storage system built on top of a shared memory ring buffer. Provides key-value storage with automatic memory management and cross-process serialization support.

This storage system follows a FIFO (First-In-First-Out) eviction policy where the oldest objects are automatically freed when memory runs low. Memory is reclaimed based on reader reference counting - objects are only freed when all readers have finished accessing them.

Architecture: - Single writer process can put(key, value) objects - Multiple reader processes can get(address, monotonic_id) objects - Built on SingleWriterShmRingBuffer for efficient shared memory management - Thread-safe operations with reader synchronization via locks

Key Features: - FIFO Eviction: Oldest objects are evicted first when memory is full - Reference Counting: Objects are only freed when no readers are accessing them - Duplicate Key Handling: Existing keys are not overwritten, just re-referenced - Customized Serialization: By default uses Msgpack for efficient serialization of Python objects, but can be extended for custom types - Cross-Process Safety: Uses shared memory with proper synchronization - Automatic Cleanup: Garbage collection happens transparently during allocation

Memory Layout per Object: `[4-byte reference_count][metadata_size][serialized_object_data]`


Thread Safety: - Writer operations (put, clear) are single-threaded by design - Reader operations (get) are thread-safe with lock-based reference counting - Memory reclamation is handled exclusively by the writer process

Methods:

-
–[__init__](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.__init__)Initialize the object storage.

-
–[clear](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.clear)Clear the object storage.

-
–[close](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.close)Close the shared memory.

-
–[default_is_free_check](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.default_is_free_check)Default is_free function that checks if the first 4 bytes are zero.

-
–[free_unused](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.free_unused)Free unused buffers in the ring buffer.

-
–[get_cached](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.get_cached)Get the cached object by key if it exists.

-
–[handle](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.handle)Get handle for sharing across processes.

-
–[increment_reader_flag](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.increment_reader_flag)Set the in-use flag for the reader.

-
–[increment_writer_flag](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.increment_writer_flag)Set the in-use flag for the writer.

-
–[is_cached](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.is_cached)Check if the object with the given key is cached.

-
–[put](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.put)Store a key-value pair in the object storage.

-
–[touch](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.touch)Touch an existing cached item to update its eviction status.


## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


|
|

###

`__init__(max_object_size, n_readers, ring_buffer, serde_class=MsgpackSerde, reader_lock=None)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.__init__)

Initialize the object storage.

Parameters:

-

(`max_object_size`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.__init__(max_object_size))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Maximum size for a single object in bytes.

-

(`n_readers`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.__init__(n_readers))

) –[int](https://docs.python.org/3/builtins/functions.html#int)Number of reader processes that can access the storage.

-

(`ring_buffer`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.__init__(ring_buffer))

) –[SingleWriterShmRingBuffer](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer)The shared memory ring buffer for storing objects.

-

(`serde_class`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.__init__(serde_class))

, default:[type](https://docs.python.org/3/builtins/functions.html#type)[[ObjectSerde](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.ObjectSerde)]`MsgpackSerde`

) –Serializer/deserializer for objects.

-

(`reader_lock`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.__init__(reader_lock))`Lock | None`

, default:`None`

) –Optional lock for synchronizing reader access.


Raises:

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If reader_lock is None for readers.


## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`clear()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.clear)

Clear the object storage.

## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`close()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.close)

###

`default_is_free_check(id, buf)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.default_is_free_check)

Default is_free function that checks if the first 4 bytes are zero. This indicates that the buffer is free.

## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`free_unused()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.free_unused)

Free unused buffers in the ring buffer.

## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`get_cached(key)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.get_cached)

Get the cached object by key if it exists.

## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`handle()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.handle)

Get handle for sharing across processes.

## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`increment_reader_flag(data_view)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.increment_reader_flag)

Set the in-use flag for the reader.

## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`increment_writer_flag(id)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.increment_writer_flag)

###

`is_cached(key)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.is_cached)

###

`put(key, value)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.put)

Store a key-value pair in the object storage. Attempts to free max_object_size bytes using FIFO order when the ring buffer runs out of space during a put() operation.

Parameters:

Raises:

-

–[MemoryError](https://docs.python.org/3/builtins/exceptions.html#MemoryError)If there's not enough space in the buffer

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the serialized object is too large

-

–[ValueError](https://docs.python.org/3/builtins/exceptions.html#ValueError)If the key already exists in the storage


## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`touch(key, address=0, monotonic_id=0)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.touch)

Touch an existing cached item to update its eviction status.

For writers (ShmObjectStoreSenderCache): Increment writer_flag For readers (ShmObjectStoreReceiverCache): Increment reader_count

Parameters:

-

(`key`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.touch(key))

) –[str](https://docs.python.org/3/builtins/stdtypes.html#str)String key of the object to touch

-

(`address`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.touch(address))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Address of the object (only for readers)

-

(`monotonic_id`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmObjectStorage.touch(monotonic_id))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`0`

) –Monotonic ID of the object (only for readers)


## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


##

`SingleWriterShmRingBuffer`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer)

A single-writer, multiple-reader ring buffer implementation using shared memory. This class provides a thread-safe ring buffer where one process can write data while multiple processes/threads can read from it.

Architecture: - Uses shared memory for cross-process communication - Maintains metadata for each allocated buffer chunk in the writer process - Supports custom "is_free_fn" functions to determine when buffers can be reused - Each buffer chunk contains: `[4-byte id][4-byte size][actual_data]`


Key Concepts: - monotonic_id_start/end: Track the range of active buffer IDs - data_buffer_start/end: Track the physical memory range in use - Automatic wraparound when reaching buffer end - Lazy garbage collection based on is_free_fn checks

Example Usage Scenarios:

Scenario 1: Simple Linear Allocation

Buffer size: 100 bytes
Initial state: [................................................. ]
^start=end(0)
After allocating 20 bytes (id=0):
[id:0|size:20|data........][...................................]
^start(0) ^end(28)
After allocating 30 bytes (id=1):
[id:0|size:20|data........][id:1|size:30|data..............][..]
^start(0) ^end(66)


Scenario 2: Memory Reclamation

Before freeing (both buffers still in use):
[id:0|size:20|data........][id:1|size:30|data..............][..]
^start(0) ^end(66)
After id:0 is marked free by readers:
[FREED.................... ][id:1|size:30|data..............][..]
^start(28) ^end(66)
After both are freed:
[FREED..............................................][..]
^start=end(66)


Scenario 3: Wraparound Allocation (continuing from Scenario 2)

Starting from after memory reclamation in Scenario 2:
[FREED..............................................][..]
^start=end(66)
Allocate 40 bytes (id=2) - only 34 bytes available at end, so wraparound:
[id:2|size:40|data........................][FREED.............][..]
^end(148) ^start(66)


Scenario 4: Error Handling - Out of Space

Starting from after wraparound allocation in Scenario 3:
[id:2|size:40|data........................][FREED.............][..]
^end(148) ^start(66)
Trying to allocate 20 more bytes:
occupied_size_new = end + size - start = 148 + 28 - 66 > buffer_size(100)
-> Raises MemoryError: "Not enough space in the data buffer"


Thread Safety: - Single writer: Only one process/thread should write (allocate_buf) - Multiple readers: Multiple processes/threads can read (access_buf) - Reader synchronization handled by is_free_fn callback - Writer handles garbage collection (free_buf) based on reader feedback

Memory Layout per Buffer Chunk: `[4-byte monotonic_id][4-byte chunk_size][actual_data...]`

^metadata_start ^data_start

The monotonic_id ensures data integrity - readers can verify they're accessing the correct data even after buffer wraparound or reuse.

Methods:

-
–[allocate_buf](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.allocate_buf)Allocate a buffer

`MD_SIZE`

+`size`

bytes in the shared memory. -
–[byte2int](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.byte2int)Convert bytes back to an integer.

-
–[clear](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.clear)Clear the ring buffer.

-
–[close](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.close)Close the shared memory.

-
–[free_buf](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.free_buf)Free a buffer of the given size. This is a no-op in shared memory,

-
–[int2byte](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.int2byte)Convert an integer to bytes.


## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


|
|

###

`allocate_buf(size)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.allocate_buf)

Allocate a buffer `MD_SIZE`

+ `size`

bytes in the shared memory. Memory layout: `[4-byte monotonic_id][4-byte size][buffer data...]`


## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`byte2int(byte_data)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.byte2int)

###

`clear()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.clear)

Clear the ring buffer.

## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`close()`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.close)

Close the shared memory.

## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


###

`free_buf(is_free_fn, nbytes=None)`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.free_buf)

Free a buffer of the given size. This is a no-op in shared memory, but we need to keep track of the metadata.

If freed memory spreads across the end and start of the ring buffer, the actual freed memory will be in two segments. In this case there still might not be a contiguous space of `nbytes`

available.

Parameters:

-

(`is_free_fn`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.free_buf(is_free_fn))

) –[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable)[[[int](https://docs.python.org/3/builtins/functions.html#int),[memoryview](https://docs.python.org/3/builtins/stdtypes.html#memoryview)],[bool](https://docs.python.org/3/builtins/functions.html#bool)]Predicate called with a monotonic id and the buffer, returning True when that buffer can be reclaimed.

-

(`nbytes`

[¶](https://docs.vllm.ai#vllm.distributed.device_communicators.shm_object_storage.SingleWriterShmRingBuffer.free_buf(nbytes))

, default:[int](https://docs.python.org/3/builtins/functions.html#int)`None`

) –The size of the buffer to free. If None, frees the maximum size of the ring buffer.


## Source code in `vllm/distributed/device_communicators/shm_object_storage.py`


|
|