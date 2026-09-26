source: https://docs.nvidia.com/dynamo/reference/api/python/nixl_connect
lastmod: 2026-09-24T19:58:16.636Z

dynamo.nixl_connect


dynamo.nixl_connect

`dynamo.nixl_connect`

publishes 17 classes and 0 functions. Source: `lib/bindings/python/src/dynamo/nixl_connect/__init__.py`


###### AbstractOperation (class)


Abstract base class for awaitable NIXL based RDMA operations.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L105`


**Public methods**

**init**

No summary available.

#### wait_for_completion

Blocks the caller asynchronously until the operation has completed.

###### ActiveOperation (class)


Abstract class for active operations that initiates a NIXL based RDMA transfer based `RdmaMetadata`

provided by the remote worker’s corresponding `PassiveOperation`

.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L283`


**Public methods**

**init**

No summary available.

#### cancel

Cancels the operation. No affect if the operation has already completed or errored, or has been cancelled.

###### Connection (class)


No summary available.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L586`


**Public methods**

**init**

Creates a new Connection instance.

**Parameters**

The connector associated with this connection.

The connection number. Used to create a unique name for the connection.

**Raises**

`TypeError`

— When`connector`

is provided and not of type`dynamo.nixl_connect.Connector`

.`TypeError`

— When`number`

is provided and not of type`int`

.`ValueError`

— When`number`

is provided and not greater than 0.

#### acquire_remote_ref

No summary available.

#### release_remote_ref

Returns True when the last reference is released.

#### initialize

No summary available.

###### Connector (class)


Core class for managing the connection between workers in a distributed environment. Use this class to create readable and writable operations, or read and write data to remote workers.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L692`


**Public methods**

**init**

Creates a new Connector instance.

**Parameters**

Unique identifier of the worker, defaults to a new UUID when `None`

.

**Raises**

`TypeError`

— When`worker_id`

is provided and not of type`uuid.UUID`

.

#### begin_read

Creates a read operation for fulfilling a remote readable operation.

**Parameters**

RDMA metadata from a remote worker that has created a readable operation.

Local descriptor(s) to receive data from the remote worker described by `remote_metadata`

.

**Returns**

`ReadOperation`

— Awaitable read operation that can be used to transfer data from a remote worker.

**Raises**

`TypeError`

— When`remote_metadata`

is not of type`RdmaMetadata`

.`TypeError`

— When`local_descriptors`

is not of type`dynamo.nixl_connect.Descriptor`

or`list[dynamo.nixl_connect.Descriptor]`

.

#### begin_write

Creates a write operation for transferring data to a remote worker.

**Parameters**

Local descriptors of one or more data objects to be transferred to the remote worker.

Serialized request from a remote worker that has created a readable operation.

#### create_readable

Creates a readable operation for transferring data from a remote worker.

**Returns**

`ReadableOperation`

— A readable operation that can be used to transfer data from a remote worker.

#### create_writable

Creates a writable operation for transferring data to a remote worker.

**Returns**

`WritableOperation`

— A writable operation that can be used to transfer data to a remote worker.

#### initialize

Deprecated method.

###### Descriptor (class)


Memory descriptor that ensures memory is registered w/ NIXL, used for transferring data between workers.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L919`


**Public methods**

**init**

Memory descriptor for transferring data between workers.

**Parameters**

The data to be transferred.

When `torch.Tensor`

is provided, the attributes of the tensor will be used to create the descriptor.

When `tuple[ndarray, Device]`

is provided, the tuple must contain:

`ndarray`

: The CuPy or NumPy array to be transferred.`Device`

: Either a`dynamo.nixl_connect.Device`

or a string representing the device type (e.g., “cuda” or “cpu”).

When `bytes`

is provided, the pointer and size derived from the bytes object and memory type will be assumed to be CPU.

When `tuple[int, int, Device|str, Any]`

is provided, the tuple must contain the following elements:

`int`

: Pointer to the data in memory.`int`

: Size of the data in bytes.`Device`

: Either a`dynamo.nixl_connect.Device`

or a string representing the device type (e.g., “cuda” or “cpu”).`Any`

: Optional reference to the data (e.g., the original tensor or bytes object). This is useful for keeping a reference to the data in memory, but it is not required.

**Raises**

`ValueError`

— When`data`

is`None`

.`TypeError`

— When`data`

is not a valid type (i.e., not`torch.Tensor`

,`bytes`

, or a valid tuple).`TypeError`

— When`data`

is a tuple but the elements are not of the expected types (i.e., [`ndarray`

,`Device|str`

] OR [`int`

,`int`

,`Device|str`

,`Any`

]).

#### from_serialized

Deserializes a `SerializedDescriptor`

into a `Descriptor`

object.

**Parameters**

The serialized descriptor to deserialize.

**Returns**

`Descriptor`

— The deserialized descriptor.

#### deregister_with_connector

Deregisters the memory of the descriptor with NIXL.

#### register_with_connector

Registers the memory of the descriptor with NIXL.

###### Device (class)


Represents a device in the system.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1283`


**Public methods**

**init**

No summary available.

###### DeviceKind (class)


Type of memory a descriptor has been allocated to.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1353`


###### OperationKind (class)


###### OperationStatus (class)


###### PassiveOperation (class)


Abstract class for common functionality of passive operations.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1452`


**Public methods**

**init**

No summary available.

#### metadata

Gets the request descriptor for the operation.

#### wait_for_completion

Blocks the caller asynchronously until the operation has completed.

###### RdmaMetadata (class)


Pydantic serialization type for describing the passive side of a transfer.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1758`


**Public methods**

#### to_descriptors

Deserializes the request descriptor into a `dynamo.nixl_connect.Descriptor`

or list of `dynamo.nixl_connect.Descriptor`

objects.

#### validate_operation_kind

No summary available.

###### ReadOperation (class)


Operation that initiates an RDMA read operation to transfer data from a remote worker’s `ReadableOperation`

, as described by `remote_metadata`

, to local buffers.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1614`


**Public methods**

**init**

Creates a new instance of `ReadOperation`

, registers `local_descriptors`

with NIXL, and begins an RDMA read operation which will transfer data described by `remote_metadata`

to `local_descriptors`

.

**Parameters**

Connection instance to use for the operation.

Serialized request from the remote worker.

Local descriptor(s) to to receive the data from the remote worker.

#### cancel

Cancels the operation. No affect if the operation has already completed or errored, or been cancelled.

#### results

Gets the results of the operation. Returns a single descriptor if only one was requested, or a list of descriptors if multiple were requested.

#### wait_for_completion

Blocks the caller asynchronously until the operation has completed.

###### ReadableOperation (class)


Operation that can be awaited until a remote worker has completed a `ReadOperation`

.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1720`


**Public methods**

**init**

No summary available.

#### wait_for_completion

Blocks the caller asynchronously until the operation has completed.

###### Remote (class)


Identifies a remote NIXL enabled worker relative to a local NIXL enabled worker.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1795`


**Public methods**

**init**

No summary available.

###### SerializedDescriptor (class)


Pydantic serialization type for memory descriptors.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1883`


**Public methods**

#### to_descriptor

Deserialize the serialized descriptor into a `Descriptor`

object.

#### validate_device

No summary available.

#### validate_ptr

No summary available.

#### validate_size

No summary available.

###### WritableOperation (class)


Operation which can be awaited until written to by a `WriteOperation`

from a remote worker.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1933`


**Public methods**

**init**

Creates a new instance of `WritableOperation`

, registers the operation and descriptors w/ NIXL, and enables an RDMA write operation to occur.

**Parameters**

Connection instance to use for the operation.

Descriptors to receive data from a remote worker.

When `connection`

is not a `dynamo.nixl_connect.Connection`

.

When `local_descriptors`

is not a `dynamo.nixl_connect.Descriptor`

or `list[dynamo.nixl_connect.Descriptor]`

.

#### wait_for_completion

Blocks the caller asynchronously until the operation has completed.

###### WriteOperation (class)


Awaitable write operation which initiates an RDMA write operation to a remote worker which provided a `RdmaMetadata`

object from a `WritableOperation`

.

`lib/bindings/python/src/dynamo/nixl_connect/__init__.py#L1988`


**Public methods**

**init**

Creates a new instance of `WriteOperation`

, registers `local_descriptors`

with NIXL, and begins an RDMA write operation which will transfer from `local_descriptors`

to remote target(s) described by `remote_metadata`


**Parameters**

Connection instance to use for the operation.

Local descriptor(s) to send from, to the remote worker.

Serialized request from the remote worker that describes the target(s) to send to.

When `connector`

is not a `dynamo.nixl_connect.Connector`

.

When `remote_metadata`

is not a `dynamo.nixl_connect.RdmaMetadata`

.

When `remote_metadata`

is not of kind `WRITE`

.

When `remote_metadata.nixl_metadata`

is not a non-empty `str`

.

When `local_descriptors`

is not a `dynamo.nixl_connect.Descriptor`

or `list[dynamo.nixl_connect.Descriptor]`

.

#### cancel

Cancels the operation. No affect if the operation has already completed or errored, or has been cancelled.

#### wait_for_completion

Blocks the caller asynchronously until the operation has completed.