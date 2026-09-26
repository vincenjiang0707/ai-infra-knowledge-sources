source: https://docs.nvidia.com/gpudirect-storage/cuobject/cuObjServer-api/index.html

# 1. cuObjServer API Specification[#](https://docs.nvidia.com#cuobjserver-api-specification)

## 1.1. Overview[#](https://docs.nvidia.com#overview)

The `cuObjServer`

library provides server-side C++ APIs to create an
RDMA-capable server endpoint, register host memory, prepare registered memory
views, and service GET/PUT requests using RDMA descriptors received through the
application control path.

Key features include:

Server endpoint setup with IPv4 and IPv6 address support.

Host memory registration for single-buffer and scatter-gather transfers.

Synchronous GET/PUT operations.

Optional asynchronous completion through

`poll()`

.Per-thread channel allocation for concurrent callers.

Configurable RDMA tuning parameters.

Telemetry and logging capabilities.

Maximum operation size of 1 GiB per

`handleGetObject()`

or`handlePutObject()`

call.

Protocol support:

`CUOBJ_PROTO_RDMA_DC_V1`

(RDMA Dynamically Connected version 1)

## 1.2. Architecture[#](https://docs.nvidia.com#architecture)

The application owns the control path between the client and server. The server
receives the operation type, request size, remote buffer start address, and
opaque RDMA descriptor over that control path. `cuObjServer`

then uses a
registered local host buffer and an allocated channel to complete the requested
GET or PUT operation.

Typical flow:

Create a

`cuObjServer`

object with the server address, port, and protocol.Verify readiness with

`isConnected()`

.Allocate a channel with

`allocateChannelId()`

.Allocate host memory or provide application-owned host memory.

Register the host memory with

`registerBuffer()`

.For each request, call

`handleGetObject()`

or`handlePutObject()`

.For asynchronous submissions, call

`poll()`

on the same channel.Complete cleanup with

`deRegisterBuffer()`

,`free()`

, and`freeChannelId()`

.

## 1.3. Core Types and Enumerations[#](https://docs.nvidia.com#core-types-and-enumerations)

### 1.3.1. Error Types[#](https://docs.nvidia.com#error-types)

```
typedef enum cuObjErr_enum {
CU_OBJ_SUCCESS = 0,
CU_OBJ_FAIL = 1
} cuObjErr_t;
```

### 1.3.2. Protocol Types[#](https://docs.nvidia.com#protocol-types)

```
typedef enum cuObjProto_enum {
CUOBJ_PROTO_RDMA_DC_V1 = 1001,
CUOBJ_PROTO_MAX
} cuObjProto_t;
```

`CUOBJ_PROTO_RDMA_DC_V1`

is the supported protocol value for
`cuObjServer`

. Current behavior accepts the `proto`

argument in the
constructor and does not report an error for unsupported values.

### 1.3.3. Operation Types[#](https://docs.nvidia.com#operation-types)

```
typedef enum cuObjOpType_enum {
CUOBJ_GET = 0,
CUOBJ_PUT = 1,
CUOBJ_INVALID = 9999
} cuObjOpType_t;
```

`CUOBJ_GET`

and `CUOBJ_PUT`

are the operation values used by the server
I/O path.

### 1.3.4. Channel ID States[#](https://docs.nvidia.com#channel-id-states)

```
typedef enum cuObjChannelIdState_enum {
CHANNEL_ID_FREE = 0,
CHANNEL_ID_ALLOCATED = 1,
CHANNEL_ID_IN_USE = 2,
INVALID_CHANNEL_ID = UINT16_MAX
} cuObjChannelIdState_t;
```

Applications normally use only `INVALID_CHANNEL_ID`

, which is returned by
`allocateChannelId()`

when no channel is available.

### 1.3.5. Delay Modes[#](https://docs.nvidia.com#delay-modes)

```
typedef enum cuObjDelayMode {
CUOBJ_DELAY_NONE = 0,
CUOBJ_DELAY_BATCH = 1,
CUOBJ_DELAY_ENTRY = 2,
CUOBJ_DELAY_ADAPTIVE = 3,
CUOBJ_DELAY_INVALID = 4
} cuObjDelayMode_t;
```

Delay mode controls the polling behavior used by synchronous
`handleGetObject()`

and `handlePutObject()`

calls. The default is
`CUOBJ_DELAY_BATCH`

.

## 1.4. RDMAConnection Base Class[#](https://docs.nvidia.com#rdmaconnection-base-class)

`RDMAConnection`

is the public base class used by `cuObjServer`

.
Applications should normally construct and use `cuObjServer`

directly.

### 1.4.1. Class Declaration[#](https://docs.nvidia.com#class-declaration)

```
class RDMAConnection {
public:
cuObjRDMATunable params;
RDMAConnection(const char* ip, unsigned short port);
RDMAConnection(const RDMAConnection&) = delete;
RDMAConnection& operator=(const RDMAConnection&) = delete;
RDMAConnection(RDMAConnection&&) = delete;
RDMAConnection& operator=(RDMAConnection&&) = delete;
~RDMAConnection();
int startRDMASession();
void initRDMAConfigParams(cuObjRDMATunable config_params);
void closeRDMASession();
void handleDisconnectEvent(struct rdma_cm_id* id);
char* getChannelIP(struct rdma_cm_id* id);
int getChannelPort(struct rdma_cm_id* id);
void getConfigTunableParam(struct cuObjRDMATunableParam* param);
};
```

### 1.4.2. `RDMAConnection(const char* ip, unsigned short port)`

[#](https://docs.nvidia.com#rdmaconnection-const-char-ip-unsigned-short-port)

Initializes address state for a server endpoint.

Parameters:

`ip`

: Server endpoint address string. IPv4 and IPv6 address strings are supported.`port`

: Server port.

Notes:

The constructor stores address state. The RDMA session is started by

`startRDMASession()`

, which`cuObjServer`

calls during construction.Invalid address strings are marked invalid and cause

`startRDMASession()`

to fail.Copy and move construction and assignment are deleted.


### 1.4.3. `startRDMASession()`

[#](https://docs.nvidia.com#startrdmasession)

```
int startRDMASession();
```

Returns:

`0`

on success.`-1`

if the address is invalid or the RDMA session cannot be opened.

### 1.4.4. `initRDMAConfigParams()`

[#](https://docs.nvidia.com#initrdmaconfigparams)

```
void initRDMAConfigParams(cuObjRDMATunable config_params);
```

Copies tunable values into the connection object. This API does not return a status value.

### 1.4.5. `closeRDMASession()`

[#](https://docs.nvidia.com#closerdmasession)

```
void closeRDMASession();
```

Closes the RDMA session if one is open. This API does not return a status value.

### 1.4.6. `handleDisconnectEvent()`

[#](https://docs.nvidia.com#handledisconnectevent)

```
void handleDisconnectEvent(struct rdma_cm_id* id);
```

This method is declared in the public header but is not documented as an
application-facing `cuObjServer`

operation. Applications should not call it
directly.

### 1.4.7. `getChannelIP()`

[#](https://docs.nvidia.com#getchannelip)

```
char* getChannelIP(struct rdma_cm_id* id);
```

Returns a string representation of the channel IP address. IPv4 and IPv6 addresses are returned in text form. The returned pointer refers to static storage owned by the library.

### 1.4.8. `getChannelPort()`

[#](https://docs.nvidia.com#getchannelport)

```
int getChannelPort(struct rdma_cm_id* id);
```

Returns the channel source port.

### 1.4.9. `getConfigTunableParam()`

[#](https://docs.nvidia.com#getconfigtunableparam)

```
void getConfigTunableParam(struct cuObjRDMATunableParam* param);
```

Copies the current tunable values into `param`

. `param`

must be non-null.

## 1.5. cuObjServer Class API[#](https://docs.nvidia.com#cuobjserver-class-api)

### 1.5.1. Class Declaration[#](https://docs.nvidia.com#id1)

```
class cuObjServer : public RDMAConnection {
public:
cuObjServer(const char* ip, unsigned short port, unsigned proto);
cuObjServer(const char* ip, unsigned short port, unsigned proto,
cuObjRDMATunable params);
cuObjServer() = default;
~cuObjServer();
void* allocHostBuffer(size_t size);
struct rdma_buffer* registerBuffer(void* ptr, size_t size);
struct rdma_buffer* registerBuffer(
std::vector<cuObjScatterGatherEntry_t> sglist);
struct rdma_buffer* getRDMABufferFromSgList(
struct rdma_buffer* rdma_buffer,
std::vector<cuObjScatterGatherEntryWithOffset_t> sglist);
void putRDMABufferFromSgList(struct rdma_buffer* rdma_buffer);
void deRegisterBuffer(struct rdma_buffer* rdma_buff);
ssize_t handleGetObject(const std::string& key,
struct rdma_buffer* local_rdma_buff,
uint64_t remote_buf_start, size_t size,
const std::string& rdma_descr,
uint32_t poll_delay,
uint16_t channel = 0,
uint64_t local_offset = 0,
ibv_wc_status* status = nullptr,
void* async_handle = nullptr);
ssize_t handleGetObject(const std::string& key,
struct rdma_buffer* local_rdma_buff,
uint64_t remote_buf_start, size_t size,
const std::string& rdma_descr,
uint16_t channel = 0,
uint64_t local_offset = 0,
ibv_wc_status* status = nullptr,
void* async_handle = nullptr);
ssize_t handlePutObject(const std::string& key,
struct rdma_buffer* local_rdma_buff,
uint64_t remote_buf_start, size_t size,
const std::string& rdma_descr,
uint32_t poll_delay,
uint16_t channel = 0,
uint64_t local_offset = 0,
ibv_wc_status* status = nullptr,
void* async_handle = nullptr);
ssize_t handlePutObject(const std::string& key,
struct rdma_buffer* local_rdma_buff,
uint64_t remote_buf_start, size_t size,
const std::string& rdma_descr,
uint16_t channel = 0,
uint64_t local_offset = 0,
ibv_wc_status* status = nullptr,
void* async_handle = nullptr);
int poll(cuObjAsyncEvent_t* events,
int max_events,
uint16_t channel = 0);
bool isConnected();
uint16_t allocateChannelId();
void freeChannelId(uint16_t channel_id);
static void setupTelemetry(bool use_OTEL, std::ostream* os);
static void shutdownTelemetry();
static void setTelemFlags(unsigned flags);
};
```

### 1.5.2. Constructors[#](https://docs.nvidia.com#constructors)

#### 1.5.2.1. Basic Constructor[#](https://docs.nvidia.com#basic-constructor)

```
cuObjServer(const char* ip, unsigned short port, unsigned proto);
```

Creates a server object with default RDMA tunables and starts the RDMA session.

Parameters:

`ip`

: Server endpoint address string.`port`

: Server port.`proto`

: RDMA descriptor protocol. Use`CUOBJ_PROTO_RDMA_DC_V1`

.

Notes:

Check

`isConnected()`

after construction.A failed session start does not prevent object construction. Use

`isConnected()`

to report readiness.Current behavior does not validate unsupported

`proto`

values.

#### 1.5.2.2. Constructor With Tunables[#](https://docs.nvidia.com#constructor-with-tunables)

```
cuObjServer(const char* ip, unsigned short port, unsigned proto,
cuObjRDMATunable params);
```

Creates a server object with caller-provided RDMA tunables and starts the RDMA session.

Parameters:

`ip`

: Server endpoint address string.`port`

: Server port.`proto`

: RDMA descriptor protocol. Use`CUOBJ_PROTO_RDMA_DC_V1`

.`params`

: RDMA tunables copied into the server before session start.

#### 1.5.2.3. Default Constructor[#](https://docs.nvidia.com#default-constructor)

```
cuObjServer() = default;
```

The endpoint constructors above are the application-facing construction path.
Applications should construct `cuObjServer`

with `ip`

, `port`

, and
`proto`

, then check `isConnected()`

.

### 1.5.3. Memory Management APIs[#](https://docs.nvidia.com#memory-management-apis)

#### 1.5.3.1. `allocHostBuffer()`

[#](https://docs.nvidia.com#allochostbuffer)

```
void* allocHostBuffer(size_t size);
```

Allocates host memory aligned to the system page size.

Parameters:

`size`

: Allocation size in bytes.

Returns:

Pointer to the allocated buffer on success.

`nullptr`

when`size == 0`

or allocation fails.

Notes:

The returned memory should be released with

`free()`

.This API is optional. Applications may register their own host memory.


#### 1.5.3.2. `registerBuffer()`

for a Single Buffer[#](https://docs.nvidia.com#registerbuffer-for-a-single-buffer)

```
struct rdma_buffer* registerBuffer(void* ptr, size_t size);
```

Registers a contiguous host buffer.

Parameters:

`ptr`

: Host memory start address.`size`

: Buffer size in bytes.

Returns:

Opaque RDMA buffer handle on success.

`nullptr`

on failure.

Failure cases:

Server RDMA device is not available.

`ptr == nullptr`

.`size == 0`

.Buffer registration fails.


Notes:

The memory must remain valid until

`deRegisterBuffer()`

is called.The returned

`struct rdma_buffer*`

is an opaque handle for`cuObjServer`

APIs.Server registration supports host memory.


#### 1.5.3.3. `registerBuffer()`

for a Scatter-Gather List[#](https://docs.nvidia.com#registerbuffer-for-a-scatter-gather-list)

```
struct rdma_buffer* registerBuffer(
std::vector<cuObjScatterGatherEntry_t> sglist);
```

Registers a scatter-gather list of host buffers.

Parameters:

`sglist`

: Vector of scatter-gather entries.

Returns:

Opaque RDMA buffer handle on success.

`nullptr`

on failure.

Failure cases:

Server RDMA device is not available.

`sglist`

is empty.`sglist.size() > 10`

.Any entry has

`addr == nullptr`

.Any entry has

`size == 0`

.Allocation or registration fails.


Notes:

The maximum number of entries is 10.

All entries must remain valid until

`deRegisterBuffer()`

is called.For a registered scatter-gather buffer with more than one entry,

`handleGetObject()`

and`handlePutObject()`

treat nonzero`local_offset`

as 0.

#### 1.5.3.4. `getRDMABufferFromSgList()`

[#](https://docs.nvidia.com#getrdmabufferfromsglist)

```
struct rdma_buffer* getRDMABufferFromSgList(
struct rdma_buffer* rdma_buffer,
std::vector<cuObjScatterGatherEntryWithOffset_t> sglist);
```

Creates a scatter-gather view over a previously registered buffer.

Parameters:

`rdma_buffer`

: Opaque handle returned by`registerBuffer()`

.`sglist`

: Offset and size entries relative to the registered base buffer.

Returns:

Opaque RDMA buffer view on success.

`nullptr`

on failure.

Failure cases:

`sglist`

is empty.`rdma_buffer == nullptr`

.`rdma_buffer`

was not created by`registerBuffer()`

.`rdma_buffer`

has more than one registered entry.Allocation fails.

Sum of view entry sizes is greater than the base registered buffer size.


Notes:

The returned view must be released with

`putRDMABufferFromSgList()`

.The base registered buffer must remain registered while the view exists.

Current validation checks the total view size against the base registered buffer size. Callers must provide offsets that are within the registered base buffer.


#### 1.5.3.5. `putRDMABufferFromSgList()`

[#](https://docs.nvidia.com#putrdmabufferfromsglist)

```
void putRDMABufferFromSgList(struct rdma_buffer* rdma_buffer);
```

Releases a view created by `getRDMABufferFromSgList()`

.

Parameters:

`rdma_buffer`

: View returned by`getRDMABufferFromSgList()`

.

Notes:

Passing

`nullptr`

logs an error and returns.Passing a buffer that is not a scatter-gather view logs an error and returns.

This API does not deregister the base registered buffer.


#### 1.5.3.6. `deRegisterBuffer()`

[#](https://docs.nvidia.com#deregisterbuffer)

```
void deRegisterBuffer(struct rdma_buffer* rdma_buff);
```

Deregisters a buffer returned by `registerBuffer()`

.

Parameters:

`rdma_buff`

: Opaque handle returned by`registerBuffer()`

.

Notes:

Passing

`nullptr`

is a no-op.Complete all synchronous and asynchronous I/O using the buffer before deregistering it.

This API does not free the underlying application memory.


### 1.5.4. I/O Operations[#](https://docs.nvidia.com#i-o-operations)

#### 1.5.4.1. `handleGetObject()`

[#](https://docs.nvidia.com#handlegetobject)

```
ssize_t handleGetObject(const std::string& key,
struct rdma_buffer* local_rdma_buff,
uint64_t remote_buf_start, size_t size,
const std::string& rdma_descr,
uint16_t channel = 0,
uint64_t local_offset = 0,
ibv_wc_status* status = nullptr,
void* async_handle = nullptr);
ssize_t handleGetObject(const std::string& key,
struct rdma_buffer* local_rdma_buff,
uint64_t remote_buf_start, size_t size,
const std::string& rdma_descr,
uint32_t poll_delay,
uint16_t channel = 0,
uint64_t local_offset = 0,
ibv_wc_status* status = nullptr,
void* async_handle = nullptr);
```

Services a GET request using data already present in the registered server
buffer. `handleGetObject()`

performs an RDMA WRITE to the client buffer.

Parameters:

`key`

: Request identifier used for telemetry.`local_rdma_buff`

: Registered server buffer containing the data to send.`remote_buf_start`

: Remote buffer start address for this request.`size`

: Transfer size in bytes.`rdma_descr`

: Opaque RDMA descriptor string received from the client.`poll_delay`

: Per-request polling delay in nanoseconds for synchronous calls. The overload without this argument uses`params.getDelayInterval()`

.`channel`

: Channel returned by`allocateChannelId()`

.`local_offset`

: Offset into`local_rdma_buff`

.`status`

: Optional completion status output for synchronous calls.`async_handle`

: User handle for asynchronous completion. Use`nullptr`

for synchronous operation.

Returns:

Number of bytes transferred on synchronous success.

`0`

when asynchronous submission succeeds.Negative errno-style value on failure.


Synchronous success normally returns `size`

. Asynchronous success, when
`async_handle != nullptr`

, returns `0`

after successful submission.
Completion status is reported later by `poll()`

.

Failure values:

`-ENODEV`

: Server RDMA device is not available.`-EIO`

: Invalid input, descriptor parse failure, invalid or unallocated channel, requested size exceeds the registered local buffer range, requested remote range is outside the descriptor range, submission failure, or completion failure.`-ENOMEM`

: Allocation failure.`-EAFNOSUPPORT`

: Address family is not supported by the active path.`-EPROTO`

is not a documented return value for`handleGetObject()`

or`handlePutObject()`

in this release.

Notes:

`local_rdma_buff`

must be non-null.`remote_buf_start`

and`size`

must be nonzero.`size + local_offset`

must not exceed the registered local buffer size.For a registered scatter-gather buffer with more than one entry, current behavior first validates

`size + local_offset`

against the total registered size. If that validation passes and`local_offset`

is nonzero, the call logs an error, treats`local_offset`

as 0, and continues.`channel`

must be allocated before the call. The default argument value`0`

is not automatically allocated.When

`async_handle == nullptr`

, the call returns after completion.When

`async_handle != nullptr`

, the call returns after submission and the application must call`poll()`

on the same channel.For synchronous completion failures,

`status`

receives the completion status value and the function returns`-EIO`

.`status`

is not populated for pre-submission validation errors.

#### 1.5.4.2. `handlePutObject()`

[#](https://docs.nvidia.com#handleputobject)

```
ssize_t handlePutObject(const std::string& key,
struct rdma_buffer* local_rdma_buff,
uint64_t remote_buf_start, size_t size,
const std::string& rdma_descr,
uint16_t channel = 0,
uint64_t local_offset = 0,
ibv_wc_status* status = nullptr,
void* async_handle = nullptr);
ssize_t handlePutObject(const std::string& key,
struct rdma_buffer* local_rdma_buff,
uint64_t remote_buf_start, size_t size,
const std::string& rdma_descr,
uint32_t poll_delay,
uint16_t channel = 0,
uint64_t local_offset = 0,
ibv_wc_status* status = nullptr,
void* async_handle = nullptr);
```

Services a PUT request by populating the registered server buffer.
`handlePutObject()`

performs an RDMA READ from the client buffer.

Parameters and return values match `handleGetObject()`

.

Notes:

`local_rdma_buff`

is the destination buffer for the request data.For synchronous success, the requested data is available in

`local_rdma_buff`

when the call returns.For asynchronous success, wait for

`poll()`

to report completion before reading or reusing the destination buffer.

### 1.5.5. Asynchronous Completion[#](https://docs.nvidia.com#asynchronous-completion)

#### 1.5.5.1. `poll()`

[#](https://docs.nvidia.com#poll)

```
int poll(cuObjAsyncEvent_t* events, int max_events, uint16_t channel = 0);
```

Polls for completions submitted with non-null `async_handle`

.

Parameters:

`events`

: Output array for completion events.`max_events`

: Maximum number of events to return.`channel`

: Channel used for the asynchronous submissions.

Returns:

Number of completion events returned.

`0`

when no completions are available.`-ENODEV`

if the server RDMA device is not available.`-EINVAL`

if`events == nullptr`

or`channel`

is invalid or unallocated.`-EIO`

if any polled completion reports a failure.

Notes:

Successful completions return a count from 0 to

`max_events`

, after the`max_events`

cap is applied.Pass a non-negative

`max_events`

value.`max_events`

values greater than 16 are capped to 16.`channel`

must be allocated before`poll()`

is called.`poll()`

must be called on the same channel used for the asynchronous`handleGetObject()`

or`handlePutObject()`

submission.For a non-negative return value

`n`

, entries`events[0]`

through`events[n - 1]`

are valid.`events[i].async_handle`

is the user handle passed to`handleGetObject()`

or`handlePutObject()`

.`events[i].status`

is the completion status.`IBV_WC_SUCCESS`

(0) means success.If

`poll()`

returns`-EIO`

because a completion has non-success status, completion status is still filled for the completions processed before the error return. In this error case, the return value is not a completion count.If a completion failure is reported and

`qp_reset_on_failure`

is true, the server attempts queue-pair reset before`poll()`

returns`-EIO`

.

### 1.5.6. Channel Management[#](https://docs.nvidia.com#channel-management)

#### 1.5.6.1. `allocateChannelId()`

[#](https://docs.nvidia.com#allocatechannelid)

```
uint16_t allocateChannelId();
```

Allocates a channel for I/O submission and polling.

Returns:

Allocated channel ID in the range

`0`

to`num_dcis - 1`

.`INVALID_CHANNEL_ID`

(`UINT16_MAX`

) when no channel is available.

Notes:

The first successful allocation returns channel 0.

A channel must be allocated before it is passed to

`handleGetObject()`

,`handlePutObject()`

, or`poll()`

.Use one channel from only one thread at a time.


#### 1.5.6.2. `freeChannelId()`

[#](https://docs.nvidia.com#freechannelid)

```
void freeChannelId(uint16_t channel_id);
```

Releases a channel returned by `allocateChannelId()`

.

Parameters:

`channel_id`

: Channel to release.

Notes:

Passing a value greater than or equal to

`num_dcis`

is a no-op.Do not free a channel while operations submitted on that channel are still in progress.


### 1.5.7. Connection Management[#](https://docs.nvidia.com#connection-management)

#### 1.5.7.1. `isConnected()`

[#](https://docs.nvidia.com#isconnected)

```
bool isConnected();
```

Returns:

`true`

if the server RDMA session was started successfully.`false`

otherwise.

### 1.5.8. Telemetry Management[#](https://docs.nvidia.com#telemetry-management)

#### 1.5.8.1. `setupTelemetry()`

[#](https://docs.nvidia.com#setuptelemetry)

```
static void setupTelemetry(bool use_OTEL, std::ostream* os);
```

Configures telemetry output for subsequently created `cuObjServer`

objects.

Parameters:

`use_OTEL`

: Request OpenTelemetry telemetry when OpenTelemetry support is built in.`os`

: Output stream for stream telemetry.

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

before creating the first`cuObjServer`

object. Current behavior applies the setting when the telemetry object is created.If OpenTelemetry support is not built in, stream telemetry is used.

`os`

must be non-null when stream telemetry is used.`os`

must remain valid until all`cuObjServer`

objects are destroyed.

#### 1.5.8.2. `shutdownTelemetry()`

[#](https://docs.nvidia.com#shutdowntelemetry)

```
static void shutdownTelemetry();
```

Resets telemetry configuration to the default output stream.

Notes:

Call

`shutdownTelemetry()`

before closing a custom stream passed to`setupTelemetry()`

.Telemetry resources are fully released when the last

`cuObjServer`

object is destroyed.

#### 1.5.8.3. `setTelemFlags()`

[#](https://docs.nvidia.com#settelemflags)

```
static void setTelemFlags(unsigned flags);
```

Configures telemetry logging flags.

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

Flags may be combined with bitwise OR:

```
cuObjServer::setTelemFlags(CUOBJ_LOG_PATH_ERROR | CUOBJ_LOG_PATH_INFO);
```

Passing `0`

disables info, debug, and error telemetry messages. Bits other
than the valid values listed above have no defined effect.

Notes:

Call

`setTelemFlags()`

before creating the first`cuObjServer`

object. Current behavior applies the flags when the telemetry object is created.The API does not return a status value.


## 1.6. Supporting Structures[#](https://docs.nvidia.com#supporting-structures)

### 1.6.1. `cuObjScatterGatherEntry`

[#](https://docs.nvidia.com#cuobjscattergatherentry)

```
typedef struct cuObjScatterGatherEntry {
void* addr;
size_t size;
} cuObjScatterGatherEntry_t;
```

Fields:

`addr`

: Host memory address.`size`

: Segment size in bytes.

### 1.6.2. `cuObjScatterGatherEntryWithOffset`

[#](https://docs.nvidia.com#cuobjscattergatherentrywithoffset)

```
typedef struct cuObjScatterGatherEntryWithOffset {
loff_t offset;
size_t size;
} cuObjScatterGatherEntryWithOffset_t;
```

Fields:

`offset`

: Offset from the base registered buffer.`size`

: Segment size in bytes.

### 1.6.3. `cuObjAsyncEvent_t`

[#](https://docs.nvidia.com#cuobjasyncevent-t)

```
typedef struct cuObjAsyncEvent_s {
void* async_handle;
ssize_t status;
} cuObjAsyncEvent_t;
```

Fields:

`async_handle`

: User handle provided during asynchronous submission.`status`

: Completion status. The field is declared as`ssize_t`

, but`poll()`

stores an enum`ibv_wc_status`

value in it.`IBV_WC_SUCCESS`

(0) means success. For nonzero values, interpret the field as`ibv_wc_status_str((enum ibv_wc_status)event.status)`

.

### 1.6.4. `cuObjRDMATunableParam`

[#](https://docs.nvidia.com#cuobjrdmatunableparam)

```
struct cuObjRDMATunableParam {
int num_dcis;
unsigned cq_depth;
unsigned long dc_key;
int ibv_poll_max_comp_event;
int service_level;
uint8_t timeout;
unsigned hop_limit;
int pkey_index;
int max_wr;
int max_sge;
uint32_t delay_interval;
cuObjDelayMode_t delay_mode;
bool qp_reset_on_failure;
uint8_t retry_cnt;
unsigned traffic_class;
int max_rd_atomic;
};
```

### 1.6.5. `cuObjRDMATunable`

[#](https://docs.nvidia.com#cuobjrdmatunable)

`cuObjRDMATunable`

stores `cuObjRDMATunableParam`

values and provides
getters and setters.

Parameter |
Setter |
Getter |
Default |
Valid Values / Current Behavior |
|---|---|---|---|---|
|
|
|
|
Number of channels/DCIs. Must be usable by the RDMA device. Values greater than the device QP limit cause session start failure. |
|
|
|
|
Completion queue depth. |
|
|
|
|
DC key value. |
|
|
|
|
Not used currently. |
|
|
|
|
Service level value. |
|
|
|
|
Timeout value used by the RDMA connection. |
|
|
|
|
Hop limit value. |
|
|
|
|
Partition key index. |
|
|
|
|
Not used currently. |
|
|
|
|
Maximum scatter-gather entries per operation. |
|
|
|
|
Polling delay interval in nanoseconds. |
|
|
|
|
One of the |
|
|
|
|
Enables queue-pair reset after completion failure. |
|
|
|
|
Retry count value. The header documents this as a 3-bit value, 0 through 7. |
|
|
|
|
Values below 256 are applied. Values greater than or equal to 256 are logged as invalid. |
|
|
|
|
|

The setters do not return status values and do not perform full range validation. Configure values that are valid for the RDMA device and workload.

## 1.7. Error Handling[#](https://docs.nvidia.com#error-handling)

### 1.7.1. Return Value Conventions[#](https://docs.nvidia.com#return-value-conventions)

Constructors do not return a value. Call

`isConnected()`

to check session readiness.Memory registration APIs return an opaque pointer on success and

`nullptr`

on failure.I/O APIs return

`ssize_t`

. Synchronous success returns a byte count, asynchronous submission success returns`0`

, and failure returns a negative errno-style value.`poll()`

returns a completion count or a negative errno-style value.Channel allocation returns a channel ID or

`INVALID_CHANNEL_ID`

.

### 1.7.2. I/O API Failure Values[#](https://docs.nvidia.com#i-o-api-failure-values)

Return value |
Meaning |
|---|---|
|
Server RDMA device is not available. |
|
Invalid argument, invalid descriptor, invalid channel, request range failure, submission failure, or completion failure. |
|
Allocation failure. |
|
Address family is not supported by the active path. |

### 1.7.3. `poll()`

Failure Values[#](https://docs.nvidia.com#poll-failure-values)

Return value |
Meaning |
|---|---|
|
Server RDMA device is not available. |
|
|
|
One or more completions reported failure. |

### 1.7.4. Completion Status[#](https://docs.nvidia.com#completion-status)

For synchronous `handleGetObject()`

and `handlePutObject()`

, the optional
`status`

parameter is populated after polling when a completion status is
available. `IBV_WC_SUCCESS`

(0) means success.

For asynchronous operations, `poll()`

reports completion status in
`cuObjAsyncEvent_t.status`

. A non-negative `poll()`

return value gives the
number of valid events in the output array.

Common completion status values include:

Value |
Status |
Meaning |
|---|---|---|
|
|
Operation completed successfully. |
|
|
Outstanding work request was flushed after queue-pair error/reset. |
|
|
Local memory registration, key, or access error. |
|
|
Remote key, address, or access error. |
|
|
Remote operation error. |
|
|
Retry count exceeded; usually a path or reachability issue. |
|
|
Receiver-not-ready retry count exceeded. |
|
|
Fatal completion error. |
|
|
Response timeout. |
|
|
General completion error. |

## 1.8. Server IPv6 Endpoint Support[#](https://docs.nvidia.com#server-ipv6-endpoint-support)

`cuObjServer`

accepts IPv4 and IPv6 endpoint address strings in the `ip`

constructor argument. The constructor takes address and port separately, so an
IPv6 literal is passed without square brackets:

```
cuObjServer server("fd00::10", 18515, CUOBJ_PROTO_RDMA_DC_V1);
```

IPv4 usage is unchanged:

```
cuObjServer server("192.168.1.100", 18515, CUOBJ_PROTO_RDMA_DC_V1);
```

Invalid address strings cause the RDMA session start to fail. Check
`isConnected()`

after construction.

When the application control path represents an IPv6 endpoint as a combined
address-and-port string, use square brackets in that control-path format, for
example `[fd00::10]:18515`

. Do not use square brackets for the
`cuObjServer`

constructor because `ip`

and `port`

are separate
arguments.

## 1.9. Usage Patterns[#](https://docs.nvidia.com#usage-patterns)

### 1.9.1. Basic Server Usage[#](https://docs.nvidia.com#basic-server-usage)

```
cuObjServer server("192.168.1.100", 18515, CUOBJ_PROTO_RDMA_DC_V1);
if (!server.isConnected()) {
return;
}
uint16_t channel = server.allocateChannelId();
if (channel == INVALID_CHANNEL_ID) {
return;
}
void* buffer = server.allocHostBuffer(1024 * 1024);
if (buffer == nullptr) {
server.freeChannelId(channel);
return;
}
struct rdma_buffer* rdma_buf = server.registerBuffer(buffer, 1024 * 1024);
if (rdma_buf == nullptr) {
free(buffer);
server.freeChannelId(channel);
return;
}
ssize_t result = server.handleGetObject("request-1",
rdma_buf,
remote_addr,
request_size,
rdma_descriptor,
channel);
if (result < 0) {
// Handle error.
}
server.deRegisterBuffer(rdma_buf);
free(buffer);
server.freeChannelId(channel);
```

### 1.9.2. Synchronous PUT Usage[#](https://docs.nvidia.com#synchronous-put-usage)

```
ssize_t result = server.handlePutObject("request-2",
rdma_buf,
remote_addr,
request_size,
rdma_descriptor,
channel);
if (result > 0) {
// result bytes are available in rdma_buf-backed local memory.
}
```

### 1.9.3. Asynchronous Usage[#](https://docs.nvidia.com#asynchronous-usage)

```
void* async_handle = reinterpret_cast<void*>(0x1);
ssize_t submit = server.handleGetObject("async-get",
rdma_buf,
remote_addr,
request_size,
rdma_descriptor,
channel,
0,
nullptr,
async_handle);
if (submit == 0) {
cuObjAsyncEvent_t events[16];
int count = 0;
do {
count = server.poll(events, 16, channel);
} while (count == 0);
if (count > 0) {
for (int i = 0; i < count; ++i) {
if (events[i].status == IBV_WC_SUCCESS) {
// events[i].async_handle identifies the completed request.
}
}
}
}
```

### 1.9.4. Scatter-Gather Registration[#](https://docs.nvidia.com#scatter-gather-registration)

```
void* buf1 = server.allocHostBuffer(4096);
void* buf2 = server.allocHostBuffer(8192);
std::vector<cuObjScatterGatherEntry_t> sglist = {
{ buf1, 4096 },
{ buf2, 8192 }
};
struct rdma_buffer* rdma_buf = server.registerBuffer(sglist);
if (rdma_buf != nullptr) {
ssize_t result = server.handleGetObject("sg-get",
rdma_buf,
remote_addr,
12288,
rdma_descriptor,
channel);
server.deRegisterBuffer(rdma_buf);
}
free(buf1);
free(buf2);
```

### 1.9.5. Registered Buffer View[#](https://docs.nvidia.com#registered-buffer-view)

```
void* base = server.allocHostBuffer(1024 * 1024);
struct rdma_buffer* base_buf = server.registerBuffer(base, 1024 * 1024);
std::vector<cuObjScatterGatherEntryWithOffset_t> view_entries = {
{ 0, 4096 },
{ 16384, 8192 }
};
struct rdma_buffer* view =
server.getRDMABufferFromSgList(base_buf, view_entries);
if (view != nullptr) {
server.handleGetObject("view-get",
view,
remote_addr,
12288,
rdma_descriptor,
channel);
server.putRDMABufferFromSgList(view);
}
server.deRegisterBuffer(base_buf);
free(base);
```

### 1.9.6. Custom RDMA Tuning[#](https://docs.nvidia.com#custom-rdma-tuning)

```
cuObjRDMATunable params;
params.setNumDcis(256);
params.setCqDepth(1024);
params.setTimeout(20);
params.setRetryCount(7);
params.setDelayInterval(10000);
params.setQPResetOnFailure(true);
params.setMaxRdAtomic(16);
cuObjServer server("fd00::10", 18515, CUOBJ_PROTO_RDMA_DC_V1, params);
```

### 1.9.7. Telemetry Configuration[#](https://docs.nvidia.com#telemetry-configuration)

```
std::ofstream log_file("cuobj_server.log");
cuObjServer::setupTelemetry(false, &log_file);
cuObjServer::setTelemFlags(CUOBJ_LOG_PATH_ERROR |
CUOBJ_LOG_PATH_INFO |
CUOBJ_LOG_PATH_DEBUG);
{
cuObjServer server("192.168.1.100", 18515, CUOBJ_PROTO_RDMA_DC_V1);
// Use server.
}
cuObjServer::shutdownTelemetry();
log_file.close();
```

## 1.10. Constants and Limits[#](https://docs.nvidia.com#constants-and-limits)

### 1.10.1. Operation Limits[#](https://docs.nvidia.com#operation-limits)

Maximum operation size: 1 GiB per

`handleGetObject()`

or`handlePutObject()`

call.`remote_buf_start`

and`size`

must identify a range within the client descriptor range.`size + local_offset`

must not exceed the registered local buffer size.Registered scatter-gather buffers have a maximum of 10 entries.

`handleGetObject()`

and`handlePutObject()`

fail with`-EIO`

if the registered buffer entry count exceeds`params.getMaxSge()`

.

### 1.10.2. Poll Limits[#](https://docs.nvidia.com#poll-limits)

`poll()`

caps`max_events`

to 16.`poll()`

returns`0`

when no completions are available.

### 1.10.3. Channel Limits[#](https://docs.nvidia.com#channel-limits)

Default number of channels/DCIs: 128.

Valid allocated channel IDs are in the range

`0`

to`num_dcis - 1`

.`INVALID_CHANNEL_ID`

is`UINT16_MAX`

.

### 1.10.4. Memory Requirements[#](https://docs.nvidia.com#memory-requirements)

Server memory registration is for host memory.

`allocHostBuffer()`

returns memory aligned to the system page size.Application-owned host memory must remain valid until

`deRegisterBuffer()`

is called.

## 1.11. Thread Safety and Channel Management[#](https://docs.nvidia.com#thread-safety-and-channel-management)

### 1.11.1. Channel Rules[#](https://docs.nvidia.com#channel-rules)

Call

`allocateChannelId()`

before passing a channel to`handleGetObject()`

,`handlePutObject()`

, or`poll()`

.Use one channel from one thread at a time.

Call

`poll()`

on the same channel used for asynchronous submission.Do not free a channel until all operations submitted on that channel have completed.


### 1.11.3. Telemetry Configuration[#](https://docs.nvidia.com#id2)

Configure telemetry before constructing `cuObjServer`

objects. Do not change
telemetry stream configuration while server objects using telemetry are active.

## 1.12. API Usage Notes[#](https://docs.nvidia.com#api-usage-notes)

Check

`isConnected()`

after constructing`cuObjServer`

.Allocate a channel before

`handleGetObject()`

,`handlePutObject()`

, or`poll()`

. The default argument`channel = 0`

does not allocate channel 0.Release registered buffers with

`deRegisterBuffer()`

after all operations using those buffers have completed.Release buffer views from

`getRDMABufferFromSgList()`

with`putRDMABufferFromSgList()`

.For asynchronous operations, wait for

`poll()`

completion before reusing or deregistering the buffer.Use the

`CUOBJ_LOG_PATH_INFO`

,`CUOBJ_LOG_PATH_DEBUG`

, and`CUOBJ_LOG_PATH_ERROR`

flags with`setTelemFlags()`

.Use

`cuObjRDMATunable`

setters to configure tunables before constructing`cuObjServer`

with custom parameters.