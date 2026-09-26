source: https://docs.nvidia.com/gpudirect-storage/cuobject/cuObjClient-api/index.html

# 1. cuObjClient API Specification[#](https://docs.nvidia.com#cuobjclient-api-specification)

## 1.1. Overview[#](https://docs.nvidia.com#overview)

The cuObjClient library provides client-side C++ APIs to prepare GET and PUT operations for high-performance out-of-band RDMA I/O operations and GPUDirect Storage support.

Key features include:

Memory registration and management for system memory and CUDA device memory.

Synchronous GET and PUT operations with user-defined callbacks.

Support for system, CUDA managed, and CUDA device memory.

RDMA descriptor generation and management for registered memory.

Telemetry and logging capabilities.

Maximum memory registration size of

`4 GiB - 64 KiB`

per buffer.

Protocol support:

`CUOBJ_PROTO_RDMA_DC_V1`

: RDMA Dynamically Connected version 1.

## 1.2. Architecture[#](https://docs.nvidia.com#architecture)

cuObjClient follows a callback-based architecture:

The user application creates a

`cuObjClient`

instance with callback operations.Memory registration through

`cuMemObjGetDescriptor()`

prepares system memory or CUDA device memory buffers for RDMA.I/O operations, such as

`cuObjGet()`

and`cuObjPut()`

, trigger callbacks with RDMA information.Callbacks handle the data transfer logic and communication with the server.

Cleanup through

`cuMemObjPutDescriptor()`

deregisters memory.

## 1.3. Core Types and Enumerations[#](https://docs.nvidia.com#core-types-and-enumerations)

### 1.3.1. Error Types[#](https://docs.nvidia.com#error-types)

```
typedef enum cuObjErr_enum {
CU_OBJ_SUCCESS = 0, // Operation successfully completed
CU_OBJ_FAIL = 1 // Operation failed
} cuObjErr_t;
```

### 1.3.2. Protocol Types[#](https://docs.nvidia.com#protocol-types)

```
typedef enum cuObjProto_enum {
CUOBJ_PROTO_RDMA_DC_V1 = 1001, // RDMA Dynamically Connected version 1
CUOBJ_PROTO_MAX
} cuObjProto_t;
```

`CUOBJ_PROTO_RDMA_DC_V1`

is the supported protocol value for cuObjClient.
Current behavior stores the `proto`

value passed to the constructor and does
not report an error for unsupported values.

### 1.3.3. Operation Types[#](https://docs.nvidia.com#operation-types)

```
typedef enum cuObjOpType_enum {
CUOBJ_GET = 0, // GET operation
CUOBJ_PUT = 1, // PUT operation
CUOBJ_INVALID = 9999
} cuObjOpType_t;
```

`CUOBJ_GET`

and `CUOBJ_PUT`

are the valid operation values for
`cuMemObjGetRDMAToken()`

.

### 1.3.4. Memory Types[#](https://docs.nvidia.com#memory-types)

```
typedef enum cuObjMemoryType_enum {
CUOBJ_MEMORY_SYSTEM = 0, // System (host) memory
CUOBJ_MEMORY_CUDA_MANAGED = 1, // CUDA unified/managed memory
CUOBJ_MEMORY_CUDA_DEVICE = 2, // CUDA device memory
CUOBJ_MEMORY_UNKNOWN = 3, // Unknown memory type
CUOBJ_MEMORY_INVALID = 4 // Invalid memory type
} cuObjMemoryType_t;
```

## 1.4. cuObjClient Class API[#](https://docs.nvidia.com#cuobjclient-class-api)

### 1.4.1. Class Declaration[#](https://docs.nvidia.com#class-declaration)

```
class cuObjClient {
public:
// Constructor & Destructor
cuObjClient(CUObjOps_t& ops, cuObjProto_t proto = CUOBJ_PROTO_RDMA_DC_V1);
~cuObjClient();
// Memory Management
cuObjErr_t cuMemObjGetDescriptor(void* ptr, size_t size);
cuObjErr_t cuMemObjPutDescriptor(void* ptr);
ssize_t cuMemObjGetMaxRequestCallbackSize(void* ptr);
cuObjErr_t cuMemObjGetRDMAToken(void* ptr, size_t size, size_t buffer_offset,
cuObjOpType_t operation, char** desc_str_out);
cuObjErr_t cuMemObjPutRDMAToken(char* desc_str);
// I/O Operations
ssize_t cuObjGet(void* ctx, void* ptr, size_t size, loff_t offset = 0,
loff_t buf_offset = 0);
ssize_t cuObjPut(void* ctx, void* ptr, size_t size, loff_t offset = 0,
loff_t buf_offset = 0);
// Connection Management
bool isConnected(void);
// Static Utilities
static void* getCtx(const void* handle);
static cuObjMemoryType_t getMemoryType(const void* ptr);
// Telemetry Management
static void setupTelemetry(bool use_OTEL, std::ostream* os);
static void shutdownTelemetry();
static void setTelemFlags(unsigned flags);
};
```

### 1.4.2. Constructor[#](https://docs.nvidia.com#constructor)

Creates a new `cuObjClient`

instance with user-defined callback operations.

```
cuObjClient(CUObjOps_t& ops, cuObjProto_t proto = CUOBJ_PROTO_RDMA_DC_V1);
```

Parameters:

`ops`

: Reference to callback operations structure,`CUObjIOOps`

.`proto`

: RDMA descriptor protocol. The default value is`CUOBJ_PROTO_RDMA_DC_V1`

.

Notes:

`CUOBJ_PROTO_RDMA_DC_V1`

is the supported protocol value.Current behavior does not validate unsupported

`proto`

values.The callbacks are invoked during

`cuObjGet()`

and`cuObjPut()`

operations.Callbacks may be called from threads other than the caller thread.

Use

`isConnected()`

after construction to verify that the client is ready for operations.If a required GET or PUT callback is not provided, the corresponding operation fails when the callback is needed.


## 1.5. Memory Management APIs[#](https://docs.nvidia.com#memory-management-apis)

### 1.5.1. cuMemObjGetDescriptor[#](https://docs.nvidia.com#cumemobjgetdescriptor)

Acquires an RDMA memory descriptor for user memory.

```
cuObjErr_t cuMemObjGetDescriptor(void* ptr, size_t size);
```

Parameters:

`ptr`

: Start address of user memory.`size`

: Size of memory to register. The maximum size is`4 GiB - 64 KiB`

.

Returns:

`CU_OBJ_SUCCESS`

on successful registration.`CU_OBJ_FAIL`

on failure.

`CU_OBJ_FAIL`

is returned for `ptr == nullptr`

, `size == 0`

, sizes greater
than `CUOBJ_MAX_MEMORY_REG_SIZE`

, unsupported memory types, unsupported memory
configuration, or registration failure.

Notes:

Memory sizes greater than

`CUOBJ_MAX_MEMORY_REG_SIZE`

are not supported.System memory and CUDA device memory are supported.

CUDA managed memory cannot be registered with this API. Use CUDA managed memory only with unregistered

`cuObjGet()`

or`cuObjPut()`

operations.Memory must remain valid until

`cuMemObjPutDescriptor()`

is called.

### 1.5.2. cuMemObjPutDescriptor[#](https://docs.nvidia.com#cumemobjputdescriptor)

Releases the RDMA memory descriptor for user memory.

```
cuObjErr_t cuMemObjPutDescriptor(void* ptr);
```

Parameters:

`ptr`

: Start address of memory. This address must match the`cuMemObjGetDescriptor()`

call.

Returns:

`CU_OBJ_SUCCESS`

.

Notes:

Call this API after all I/O operations on this memory have completed.

`ptr`

must match the address used in`cuMemObjGetDescriptor()`

.Passing

`nullptr`

returns`CU_OBJ_SUCCESS`

.Current behavior does not report deregistration failures through the return value.


### 1.5.3. Registered and Unregistered Memory[#](https://docs.nvidia.com#registered-and-unregistered-memory)

Applications may call `cuMemObjGetDescriptor()`

before `cuObjGet()`

or
`cuObjPut()`

to register system memory or CUDA device memory explicitly.
Explicit registration is required before calling `cuMemObjGetRDMAToken()`

.

When `cuMemObjGetDescriptor()`

is not called, `cuObjGet()`

and
`cuObjPut()`

may be used with CUDA device memory and CUDA managed memory.
In this mode, the request size is limited by the configured GPU bounce-buffer
capacity.

For unregistered CUDA device memory, call
`cuMemObjGetMaxRequestCallbackSize()`

before issuing the operation to get the
maximum callback size for the pointer.

System memory must be registered with `cuMemObjGetDescriptor()`

before
`cuObjGet()`

or `cuObjPut()`

. Unregistered system memory is not supported.

CUDA managed memory cannot be registered with `cuMemObjGetDescriptor()`

. Use
CUDA managed memory only with unregistered `cuObjGet()`

or `cuObjPut()`

operations. Its request size is bounded by the configured GPU bounce-buffer
capacity. Because `cuMemObjGetRDMAToken()`

requires registered memory, it is
not supported for CUDA managed memory.

If `cuMemObjGetMaxRequestCallbackSize()`

returns `-1`

, the pointer does not
have an advertised callback size. For system memory, register the memory
explicitly before `cuObjGet()`

or `cuObjPut()`

.

### 1.5.4. cuMemObjGetMaxRequestCallbackSize[#](https://docs.nvidia.com#cumemobjgetmaxrequestcallbacksize)

Gets the maximum callback size for a memory pointer.

```
ssize_t cuMemObjGetMaxRequestCallbackSize(void* ptr);
```

Parameters:

`ptr`

: Start address of user memory.

Returns:

Maximum callback size in bytes for this memory pointer.

`-1`

if the callback size cannot be determined for this pointer.`-1`

for`ptr == nullptr`

.

Notes:

The callback may be invoked multiple times if the requested I/O size exceeds this limit.

The returned value is the chunk size that is used in each callback invocation.

The returned size may be smaller than the allocated memory size.

For unregistered CUDA device memory, this API returns the configured GPU bounce-buffer capacity.

For unregistered CUDA managed memory, current behavior returns

`-1`

.Positive values greater than

`CUOBJ_MAX_MEMORY_REG_SIZE`

are capped at`CUOBJ_MAX_MEMORY_REG_SIZE`

.

### 1.5.5. cuMemObjGetRDMAToken[#](https://docs.nvidia.com#cumemobjgetrdmatoken)

Generates an RDMA descriptor string for a registered memory buffer.

```
cuObjErr_t cuMemObjGetRDMAToken(void* ptr, size_t size, size_t buffer_offset,
cuObjOpType_t operation, char** desc_str_out);
```

Parameters:

`ptr`

: Start address of registered memory. The memory must have been registered previously.`size`

: Size of the memory region for the descriptor.`buffer_offset`

: Offset from the base address to start the descriptor region.`operation`

: Operation type. Use`CUOBJ_GET`

or`CUOBJ_PUT`

.`desc_str_out`

: Output pointer that stores the allocated descriptor string.

Returns:

`CU_OBJ_SUCCESS`

on success.`CU_OBJ_FAIL`

on failure.

`CU_OBJ_FAIL`

is returned when `operation`

is not `CUOBJ_GET`

or
`CUOBJ_PUT`

, or when the descriptor string cannot be generated.

Notes:

Memory must be registered with

`cuMemObjGetDescriptor()`

before calling this function.The descriptor string is allocated on success.

The caller must release the descriptor string using

`cuMemObjPutRDMAToken()`

.`operation`

must be`CUOBJ_GET`

or`CUOBJ_PUT`

.`buffer_offset + size`

must not exceed the originally registered buffer size.The buffer must be RDMA capable for this function to succeed.

`desc_str_out`

must be non-null.Applications should pass the descriptor string as returned.


### 1.5.6. cuMemObjPutRDMAToken[#](https://docs.nvidia.com#cumemobjputrdmatoken)

Frees an RDMA descriptor string allocated by `cuMemObjGetRDMAToken()`

.

```
cuObjErr_t cuMemObjPutRDMAToken(char* desc_str);
```

Parameters:

`desc_str`

: Descriptor string to free. It must have been allocated by`cuMemObjGetRDMAToken()`

.

Returns:

`CU_OBJ_SUCCESS`

on success.`CU_OBJ_FAIL`

on failure.

`CU_OBJ_FAIL`

is returned if the descriptor string cannot be released.

Notes:

Call this API to free memory allocated by

`cuMemObjGetRDMAToken()`

.

## 1.6. I/O Operations[#](https://docs.nvidia.com#i-o-operations)

### 1.6.1. cuObjGet[#](https://docs.nvidia.com#cuobjget)

Performs a GET operation using cuObject.

```
ssize_t cuObjGet(void* ctx, void* ptr, size_t size, loff_t offset = 0,
loff_t buf_offset = 0);
```

Parameters:

`ctx`

: User context pointer. This pointer is passed to the GET callback and can be retrieved with`getCtx()`

.`ptr`

: Pointer to user memory.`size`

: Size of the GET operation in bytes.`offset`

: Object offset. This value is reserved for future use and should be set to`0`

.`buf_offset`

: Buffer offset. This value is reserved for future use and should be set to`0`

.

Returns:

Number of bytes transferred on success.

Negative failure value for I/O or callback failure.

`CU_OBJ_FAIL`

for invalid arguments detected before I/O submission.

Notes:

The GET callback is invoked one or more times during this operation.

If

`size`

exceeds`MaxRequestCallbackSize`

, multiple callbacks are invoked.This is a synchronous operation. It returns after the operation completes.

`ctx`

and`ptr`

must be non-null.`size`

must be greater than`0`

.`offset`

and`buf_offset`

are reserved. Pass`0`

. Negative values return`CU_OBJ_FAIL`

.

### 1.6.2. cuObjPut[#](https://docs.nvidia.com#cuobjput)

Performs a PUT operation using cuObject.

```
ssize_t cuObjPut(void* ctx, void* ptr, size_t size, loff_t offset = 0,
loff_t buf_offset = 0);
```

Parameters:

`ctx`

: User context pointer. This pointer is passed to the PUT callback and can be retrieved with`getCtx()`

.`ptr`

: Pointer to user memory.`size`

: Size of the PUT operation in bytes.`offset`

: Object offset. This value is reserved for future use and should be set to`0`

.`buf_offset`

: Buffer offset. This value is reserved for future use and should be set to`0`

.

Returns:

Number of bytes transferred on success.

Negative failure value for I/O or callback failure.

`CU_OBJ_FAIL`

for invalid arguments detected before I/O submission.

Notes:

The PUT callback is invoked one or more times during this operation.

If

`size`

exceeds`MaxRequestCallbackSize`

, multiple callbacks are invoked.This is a synchronous operation. It returns after the operation completes.

`ctx`

and`ptr`

must be non-null.`size`

must be greater than`0`

.`offset`

and`buf_offset`

are reserved. Pass`0`

. Negative values return`CU_OBJ_FAIL`

.

## 1.7. Connection Management[#](https://docs.nvidia.com#connection-management)

### 1.7.1. isConnected[#](https://docs.nvidia.com#isconnected)

Checks whether the client is connected and ready for operations.

```
bool isConnected(void);
```

Returns:

`true`

if the client is connected and operational.`false`

otherwise.

## 1.8. Static Utility Methods[#](https://docs.nvidia.com#static-utility-methods)

### 1.8.1. getCtx[#](https://docs.nvidia.com#getctx)

Extracts the user context from the callback handle.

```
static void* getCtx(const void* handle);
```

Parameters:

`handle`

: Handle from the GET or PUT callback function.

Returns:

User context pointer that was passed to

`cuObjGet()`

or`cuObjPut()`

.`nullptr`

if`handle`

is null or no context is active for this callback.

Notes:

This API must be called within the callback to retrieve the user’s context.

The

`handle`

parameter is the first parameter passed to the callback.

### 1.8.2. getMemoryType[#](https://docs.nvidia.com#getmemorytype)

Determines the memory type of a pointer.

```
static cuObjMemoryType_t getMemoryType(const void* ptr);
```

Parameters:

`ptr`

: Memory pointer to analyze.

Returns:

Memory type enumeration,

`cuObjMemoryType_t`

.`CUOBJ_MEMORY_INVALID`

for`ptr == nullptr`

.

Possible values:

`CUOBJ_MEMORY_SYSTEM`

: System or host memory.`CUOBJ_MEMORY_CUDA_MANAGED`

: CUDA managed memory.`CUOBJ_MEMORY_CUDA_DEVICE`

: CUDA device memory.`CUOBJ_MEMORY_UNKNOWN`

: Unknown memory type.`CUOBJ_MEMORY_INVALID`

: Invalid memory type.

Notes:

CUDA device memory returns

`CUOBJ_MEMORY_CUDA_DEVICE`

.CUDA unified or array memory returns

`CUOBJ_MEMORY_CUDA_MANAGED`

.Host memory, unregistered memory, and memory whose type cannot be determined return

`CUOBJ_MEMORY_SYSTEM`

.

## 1.9. Telemetry Management[#](https://docs.nvidia.com#telemetry-management)

### 1.9.1. setupTelemetry[#](https://docs.nvidia.com#setuptelemetry)

Configures the telemetry output stream for logging and monitoring.

```
static void setupTelemetry(bool use_OTEL, std::ostream* os);
```

Parameters:

`use_OTEL`

: Request OpenTelemetry integration when OpenTelemetry support is built in.`os`

: Output stream for telemetry data.

Valid values:

Parameter |
Value |
Description |
|---|---|---|
|
|
Use stream telemetry through |
|
|
Request OpenTelemetry telemetry when OpenTelemetry support is built in. |

Notes:

Call

`setupTelemetry()`

before creating the first`cuObjClient`

object. Current behavior applies the setting when the telemetry object is created.If OpenTelemetry support is not built in, stream telemetry is used.

`os`

must be non-null when stream logging is used.Call

`shutdownTelemetry()`

before closing`os`

.`os`

must remain valid until all`cuObjClient`

objects are destroyed.

### 1.9.2. shutdownTelemetry[#](https://docs.nvidia.com#shutdowntelemetry)

Shuts down telemetry and resets the default output stream.

```
static void shutdownTelemetry();
```

Notes:

Call this API before closing custom output streams.

Telemetry is fully closed when all

`cuObjClient`

objects are destroyed.

### 1.9.3. setTelemFlags[#](https://docs.nvidia.com#settelemflags)

Configures telemetry logging flags.

```
static void setTelemFlags(unsigned flags);
```

Parameters:

`flags`

: Bitmask of telemetry logging flags.

Valid values:

Flag |
Value |
Description |
|---|---|---|
|
|
Enables informational telemetry messages. |
|
|
Enables debug telemetry messages. |
|
|
Enables error telemetry messages. |

Flags may be combined with bitwise OR. For example:

```
cuObjClient::setTelemFlags(CUOBJ_LOG_PATH_ERROR | CUOBJ_LOG_PATH_INFO);
```

Passing `0`

disables info, debug, and error telemetry messages. Bits other
than the valid values listed above have no defined effect.

Notes:

Call

`setTelemFlags()`

before creating the first`cuObjClient`

object. Current behavior applies the flags when the telemetry object is created.This API does not return a status value.


## 1.10. Callback Interface[#](https://docs.nvidia.com#callback-interface)

### 1.10.1. CUObjIOOps Structure[#](https://docs.nvidia.com#cuobjioops-structure)

User-defined callback operations structure.

```
typedef struct CUObjIOOps {
ssize_t (*get)(const void* handle, char* ptr, size_t size, loff_t offset,
const cufileRDMAInfo_t* rdma_info);
ssize_t (*put)(const void* handle, const char* ptr, size_t size, loff_t offset,
const cufileRDMAInfo_t* rdma_info);
} CUObjOps_t;
```

### 1.10.2. GET Callback[#](https://docs.nvidia.com#get-callback)

Called during a `cuObjGet()`

operation to handle data retrieval.

```
ssize_t (*get)(const void* handle, char* ptr, size_t size, loff_t offset,
const cufileRDMAInfo_t* rdma_info);
```

Parameters:

`handle`

: Cookie to user context. Use`cuObjClient::getCtx(handle)`

to extract the context.`ptr`

: Pointer to the memory chunk to be filled with data.`size`

: Size of the memory chunk being read.`offset`

: Starting object offset for this chunk.`rdma_info`

: RDMA memory descriptor string for out-of-band communication.

Returns:

Size of data read on success.

Negative failure value on failure.

One of the retryable negative

`errno`

values listed in the[RDMA Multipathing](https://docs.nvidia.com#cuobjclient-rdma-multipathing)section to allow retry on eligible failures.

Notes:

`offset`

is`0`

when`MaxRequestCallbackSize`

is greater than or equal to the total request size.`size`

equals the total request size when`MaxRequestCallbackSize`

is greater than or equal to the total request size.Multiple callbacks may be invoked for large requests.

The callback may be called from a thread other than the caller thread.

The callback must communicate with

`cuObjServer`

using the RDMA descriptor information.`rdma_info`

and the descriptor string it references are valid only for the duration of the callback invocation.

### 1.10.3. PUT Callback[#](https://docs.nvidia.com#put-callback)

Called during a `cuObjPut()`

operation to handle data transmission.

```
ssize_t (*put)(const void* handle, const char* ptr, size_t size, loff_t offset,
const cufileRDMAInfo_t* rdma_info);
```

Parameters:

`handle`

: Cookie to user context. Use`cuObjClient::getCtx(handle)`

to extract the context.`ptr`

: Pointer to the memory chunk containing data to write.`size`

: Size of the memory chunk being written.`offset`

: Starting object offset for this chunk.`rdma_info`

: RDMA memory descriptor string for out-of-band communication.

Returns:

Size of data written on success.

Negative failure value on failure.

One of the retryable negative

`errno`

values listed in the[RDMA Multipathing](https://docs.nvidia.com#cuobjclient-rdma-multipathing)section to allow retry on eligible failures.

Notes:

`offset`

is`0`

when`MaxRequestCallbackSize`

is greater than or equal to the total request size.`size`

equals the total request size when`MaxRequestCallbackSize`

is greater than or equal to the total request size.Multiple callbacks may be invoked for large requests.

The callback may be called from a thread other than the caller thread.

The callback must communicate with

`cuObjServer`

using the RDMA descriptor information.`rdma_info`

and the descriptor string it references are valid only for the duration of the callback invocation.

## 1.11. Error Handling[#](https://docs.nvidia.com#error-handling)

### 1.11.1. Error Codes[#](https://docs.nvidia.com#error-codes)

`CU_OBJ_SUCCESS`

(`0`

): Operation completed successfully.`CU_OBJ_FAIL`

(`1`

): Operation failed.

`cuObjGet()`

and `cuObjPut()`

return `CU_OBJ_FAIL`

as the numeric
`ssize_t`

value `1`

for invalid arguments detected before I/O submission.

### 1.11.2. Return Value Conventions[#](https://docs.nvidia.com#return-value-conventions)

Memory management APIs return the

`cuObjErr_t`

enumeration.I/O operations return

`ssize_t`

. Successful operations return the byte count. I/O and callback failures return negative values. Current pre-submission argument validation failures return`CU_OBJ_FAIL`

.Connection status APIs return boolean values.

Utility functions return pointers or specific types as documented.


### 1.11.3. Best Practices[#](https://docs.nvidia.com#best-practices)

Callbacks should return a non-negative byte count on success and a negative
value on failure. To trigger retry behavior, return one of the retryable
negative `errno`

values listed in the [RDMA Multipathing](https://docs.nvidia.com#cuobjclient-rdma-multipathing)
section.

## 1.12. Client IPv6 Endpoint Support[#](https://docs.nvidia.com#client-ipv6-endpoint-support)

Client applications may use IPv4 or IPv6 endpoint address strings for the application control path used by their GET and PUT callbacks.

Use plain IPv6 literals when the address and port are represented separately:

```
fd00::10
```

When an endpoint is represented as an address-and-port string, wrap the IPv6 address in square brackets so the address colons are not confused with the port separator:

```
[fd00::10]:18515
```

This endpoint notation is separate from `rdma_dev_addr_list`

. IPv6 addresses
in `rdma_dev_addr_list`

are JSON string values and should not be wrapped in
square brackets.

## 1.13. Usage Patterns[#](https://docs.nvidia.com#usage-patterns)

### 1.13.1. Basic Client Usage With Explicit Descriptor Acquisition[#](https://docs.nvidia.com#basic-client-usage-with-explicit-descriptor-acquisition)

```
// 1. Define callback operations
CUObjOps_t ops = {
.get = my_get_callback,
.put = my_put_callback
};
// 2. Create client instance
cuObjClient client(ops, CUOBJ_PROTO_RDMA_DC_V1);
if (!client.isConnected()) {
// Handle connection error
return;
}
// 3. Allocate and register memory
void* buffer = malloc(1024 * 1024); // 1MB buffer
if (buffer == nullptr) {
// Handle allocation error
return;
}
if (client.cuMemObjGetDescriptor(buffer, 1024 * 1024) != CU_OBJ_SUCCESS) {
// Handle registration error
free(buffer);
return;
}
// 4. Perform GET operation
MyContext ctx = { /* user data */ };
ssize_t result = client.cuObjGet(&ctx, buffer, 1024, 0, 0);
if (result < 0) {
// Handle error
client.cuMemObjPutDescriptor(buffer);
free(buffer);
return;
}
// 5. Perform PUT operation
result = client.cuObjPut(&ctx, buffer, 1024, 0, 0);
if (result < 0) {
// Handle error
client.cuMemObjPutDescriptor(buffer);
free(buffer);
return;
}
// 6. Cleanup
client.cuMemObjPutDescriptor(buffer);
free(buffer);
```

### 1.13.2. Callback Implementation Example[#](https://docs.nvidia.com#callback-implementation-example)

```
ssize_t my_get_callback(const void* handle, char* ptr, size_t size,
loff_t offset, const cufileRDMAInfo_t* rdma_info) {
// Extract user context
MyContext* ctx = (MyContext*)cuObjClient::getCtx(handle);
if (ctx == nullptr || rdma_info == nullptr || rdma_info->desc_str == nullptr) {
return -EINVAL;
}
// Get RDMA descriptor string
const char* rdma_desc = rdma_info->desc_str;
// Communicate with the remote endpoint via control path
// Send: operation=GET, size, offset, rdma_desc
ssize_t bytes_read = send_request_on_control_path(ctx->connection,
"GET", size, offset, rdma_desc);
// Return the amount of data transferred
return bytes_read;
}
ssize_t my_put_callback(const void* handle, const char* ptr, size_t size,
loff_t offset, const cufileRDMAInfo_t* rdma_info) {
// Extract user context
MyContext* ctx = (MyContext*)cuObjClient::getCtx(handle);
if (ctx == nullptr || rdma_info == nullptr || rdma_info->desc_str == nullptr) {
return -EINVAL;
}
// Get RDMA descriptor string
const char* rdma_desc = rdma_info->desc_str;
// Communicate with the remote endpoint via control path
// Send: operation=PUT, size, offset, rdma_desc
ssize_t bytes_written = send_request_on_control_path(ctx->connection,
"PUT", size, offset, rdma_desc);
// Return the amount of data transferred
return bytes_written;
}
```

### 1.13.3. CUDA Device Memory Usage[#](https://docs.nvidia.com#cuda-device-memory-usage)

```
// Allocate CUDA device memory
void* d_buffer = nullptr;
if (cudaMalloc(&d_buffer, 1024 * 1024) != cudaSuccess) {
// Handle allocation error
return;
}
// Check memory type
cuObjMemoryType_t mem_type = cuObjClient::getMemoryType(d_buffer);
assert(mem_type == CUOBJ_MEMORY_CUDA_DEVICE);
// Register for RDMA
if (client.cuMemObjGetDescriptor(d_buffer, 1024 * 1024) != CU_OBJ_SUCCESS) {
// Handle registration error
cudaFree(d_buffer);
return;
}
// Perform I/O operations
ssize_t result = client.cuObjGet(&ctx, d_buffer, 1024, 0, 0);
if (result < 0) {
// Handle error
}
// Cleanup
client.cuMemObjPutDescriptor(d_buffer);
cudaFree(d_buffer);
```

### 1.13.4. Manual RDMA Token Management[#](https://docs.nvidia.com#manual-rdma-token-management)

```
// Register memory
void* buffer = malloc(1024 * 1024);
if (buffer == nullptr) {
// Handle allocation error
return;
}
if (client.cuMemObjGetDescriptor(buffer, 1024 * 1024) != CU_OBJ_SUCCESS) {
// Handle registration error
free(buffer);
return;
}
// Get RDMA token for a specific region
char* rdma_token = nullptr;
size_t region_size = 4096;
size_t region_offset = 1024;
cuObjErr_t err = client.cuMemObjGetRDMAToken(buffer, region_size,
region_offset, CUOBJ_GET,
&rdma_token);
if (err == CU_OBJ_SUCCESS) {
// Pass rdma_token on the application control path
// ...
// Free the token
client.cuMemObjPutRDMAToken(rdma_token);
}
// Cleanup
client.cuMemObjPutDescriptor(buffer);
free(buffer);
```

### 1.13.5. Telemetry Configuration[#](https://docs.nvidia.com#telemetry-configuration)

```
// Setup telemetry with custom output stream
std::ofstream log_file("cuobj_client.log");
cuObjClient::setupTelemetry(false, &log_file);
cuObjClient::setTelemFlags(CUOBJ_LOG_PATH_ERROR |
CUOBJ_LOG_PATH_INFO |
CUOBJ_LOG_PATH_DEBUG);
{
// Create and use client
cuObjClient client(ops);
// ... perform operations ...
}
// Shutdown telemetry before closing file
cuObjClient::shutdownTelemetry();
log_file.close();
```

## 1.14. Logging Configuration[#](https://docs.nvidia.com#logging-configuration)

cuObjClient uses the JSON configuration selected by the
`CUFILE_ENV_PATH_JSON`

environment variable. The `logging.max_file_size_mb`

field controls the maximum log file size in megabytes.

```
{
"logging": {
"level": "ERROR",
"max_file_size_mb": 32
}
}
```

`max_file_size_mb`

defaults to `32`

. Set it to `-1`

for no limit. Valid
values are `-1`

or `1`

through `4096`

.

The same setting can be provided with the `CUFILE_LOGFILE_MAX_SIZE_MB`

environment variable:

```
CUFILE_LOGFILE_MAX_SIZE_MB=32
```

## 1.15. RDMA Peer Memory Configuration[#](https://docs.nvidia.com#rdma-peer-memory-configuration)

cuObjClient uses the JSON configuration selected by the
`CUFILE_ENV_PATH_JSON`

environment variable. The `properties.rdma_peer_type`

field selects the RDMA peer-memory type used with CUDA device memory.

```
CUFILE_ENV_PATH_JSON=/path/to/cuobj.json
```

```
{
"properties": {
"rdma_peer_type": "dmabuf"
}
}
```

`rdma_peer_type`

defaults to `"nvidia_peermem"`

. Valid values are
`"dmabuf"`

and `"nvidia_peermem"`

. Set `"rdma_peer_type": "dmabuf"`

to
request DMA-BUF support. DMA-BUF use requires platform support for DMA-BUF.

The same selection can be made with the `CUFILE_DMABUF_ENABLE`

environment
variable. Set `CUFILE_DMABUF_ENABLE=TRUE`

to request `"dmabuf"`

, or
`CUFILE_DMABUF_ENABLE=FALSE`

to request `"nvidia_peermem"`

. The environment
variable is applied after the JSON configuration.

This setting does not make CUDA managed memory registerable. CUDA managed memory
is supported only with unregistered `cuObjGet()`

or `cuObjPut()`

operations.

## 1.16. Constants and Limits[#](https://docs.nvidia.com#constants-and-limits)

### 1.16.1. Memory Limits[#](https://docs.nvidia.com#memory-limits)

```
#define CUOBJ_MAX_MEMORY_REG_SIZE (4ULL * 1024 * 1024 * 1024 - 64 * 1024) // 4GiB - 64KiB
```

Maximum memory registration size:

`4 GiB - 64 KiB`

per`cuMemObjGetDescriptor()`

call.

### 1.16.2. Protocol Constants[#](https://docs.nvidia.com#protocol-constants)

```
#define OBJ_RDMA_V1 "CUOBJ"
```

Protocol identifier string:

`"CUOBJ"`

.Default protocol:

`CUOBJ_PROTO_RDMA_DC_V1`

with value`1001`

.

### 1.16.3. Operation Limits[#](https://docs.nvidia.com#operation-limits)

I/O operations are split into chunks if they exceed

`MaxRequestCallbackSize`

.Each callback invocation receives a contiguous memory chunk.

`cuMemObjGetMaxRequestCallbackSize()`

returns the maximum callback size for a memory pointer.

## 1.17. RDMA Multipathing[#](https://docs.nvidia.com#rdma-multipathing)

cuObjClient uses the JSON configuration selected by the
`CUFILE_ENV_PATH_JSON`

environment variable. For example:

```
CUFILE_ENV_PATH_JSON=/path/to/cuobj.json
```

Add RDMA multipathing settings under the `properties`

object in the JSON
file. The `rdma_dev_addr_list`

field lists the client-side RDMA device
addresses or interfaces available to cuObjClient. Configure multiple entries to
make multiple RDMA devices available for multipathing.

```
{
"properties": {
"rdma_dev_addr_list": [
"192.168.1.10",
"192.168.1.11",
"fd00::10",
"fd00::11"
],
"rdma_peer_type": "dmabuf",
"rdma_multipath_enabled": true,
"rdma_max_backup_devices": 2,
"rdma_io_retry_count": 3,
"rdma_io_retry_delay_ms": 100,
"rdma_failback_enabled": true,
"rdma_failback_delay_ms": 100,
"rdma_health_check_interval_ms": 100,
"rdma_async_event_monitoring": true,
"rdma_unhealthy_threshold": 3
}
}
```

`rdma_peer_type`

is shown for completeness and is described in
[RDMA Peer Memory Configuration](https://docs.nvidia.com#rdma-peer-memory-configuration).

`rdma_dev_addr_list`

accepts JSON strings. IPv6 addresses are specified as
plain IPv6 string literals, such as `"fd00::10"`

. Do not wrap IPv6 addresses
in square brackets in this field. For link-local IPv6 addresses, include the
zone identifier in the string, for example `"fe80::1%mlx5_0"`

.

RDMA device or interface names may be used instead of IP addresses:

```
"rdma_dev_addr_list": ["mlx5_0", "mlx5_1"]
```

IP addresses and RDMA device or interface names may also be mixed:

```
"rdma_dev_addr_list": ["192.168.1.10", "mlx5_1", "fd00::11"]
```

RDMA multipathing fields:

Field |
Type |
Default |
Values |
Description |
|---|---|---|---|---|
|
array of strings |
empty |
IPv4 address, IPv6 address, or RDMA device/interface name strings |
Client-side RDMA device address list. Multiple entries make multiple RDMA devices available for multipathing. |
|
boolean |
|
|
Enables or disables RDMA multipathing. |
|
unsigned integer |
|
|
Maximum number of backup RDMA devices. Values above |
|
unsigned integer |
|
|
Number of I/O retries on retryable errors before the operation gives up.
Values above |
|
unsigned integer |
|
|
Delay, in milliseconds, between I/O retries. Values above |
|
boolean |
|
|
Enables or disables automatic failback to the primary RDMA device when it recovers. |
|
unsigned integer |
|
|
Minimum delay, in milliseconds, after failover before failback is
attempted. Values above |
|
unsigned integer |
|
|
Health check polling interval, in milliseconds. Values below |
|
boolean |
|
|
Enables or disables async RDMA event monitoring for failure detection. |
|
unsigned integer |
|
|
Number of consecutive health check failures before a device is marked
unhealthy. Values below |

When RDMA multipathing is enabled, at least two active RDMA devices are required for failover.

### 1.17.1. How RDMA Multipathing Is Used[#](https://docs.nvidia.com#how-rdma-multipathing-is-used)

When `rdma_multipath_enabled`

is set to `true`

, cuObjClient can use the
RDMA devices listed in `rdma_dev_addr_list`

for GET and PUT operations. One
device is used as the active path. If a retryable I/O error is reported and
another configured RDMA device is available, a retry can continue on the active
path or use another path.

`rdma_io_retry_count`

controls the number of retry attempts.
`rdma_io_retry_delay_ms`

controls the delay between retry attempts when the
active path is not changed. `rdma_failback_enabled`

allows the operation path
to return to the primary device after it recovers, subject to
`rdma_failback_delay_ms`

.

### 1.17.2. Callback Return Values That Can Trigger Retry[#](https://docs.nvidia.com#callback-return-values-that-can-trigger-retry)

GET and PUT callbacks should return the number of bytes transferred on success.
On failure, callbacks may return a negative `errno`

value. The following
callback return values are treated as retryable:

Callback return value |
Meaning |
|---|---|
|
Operation not permitted. |
|
Connection timed out. |
|
Connection reset. |
|
Network unreachable. |
|
Host unreachable. |
|
Connection refused. |
|
Network is down. |
|
No buffer space available. |
|
Try again. |
|
Operation would block. |
|
Interrupted operation. |
|
I/O error. |
|
Device unavailable. |
|
Link severed. |
|
Communication error. |
|
Protocol error. |
|
Permission denied. |
|
Endpoint not connected. |
|
Connection aborted. |

Other negative callback return values are not retryable. `-ENOTSUP`

is
returned without retry.

## 1.18. Thread Safety[#](https://docs.nvidia.com#thread-safety)

### 1.18.1. Client Thread Safety[#](https://docs.nvidia.com#client-thread-safety)

Callbacks can be called from a thread other than the caller thread. Users must lock shared resources that can be used concurrently across multiple callers.

## 1.19. API Usage Notes[#](https://docs.nvidia.com#api-usage-notes)

Memory passed to

`cuMemObjGetDescriptor()`

must remain valid until`cuMemObjPutDescriptor()`

is called.Descriptor strings returned by

`cuMemObjGetRDMAToken()`

must be released with`cuMemObjPutRDMAToken()`

.For

`cuObjGet()`

and`cuObjPut()`

, the GET or PUT callback receives the RDMA descriptor through the`rdma_info`

parameter.`cuMemObjGetRDMAToken()`

is used when an application needs to acquire a descriptor string explicitly.The

`os`

stream passed to`setupTelemetry()`

must remain valid until all`cuObjClient`

objects are destroyed. Call`shutdownTelemetry()`

before closing that stream.Callback implementations must synchronize access to shared resources that can be used concurrently across multiple callers.