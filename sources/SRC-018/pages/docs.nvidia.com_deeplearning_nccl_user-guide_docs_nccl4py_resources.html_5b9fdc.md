source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/resources.html

# Communicator Resources[](https://docs.nvidia.com#communicator-resources)

Resources owned by a [ Communicator](https://docs.nvidia.com/communicator/class.html#nccl.core.Communicator). The

[subclasses below are tracked by their owning communicator and released either explicitly via](https://docs.nvidia.com#nccl.core.resources.CommResource)

`CommResource`

`close()`

or automatically when the communicator is destroyed
or aborted.## CommResource[](https://docs.nvidia.com#commresource)

Abstract base class of communicator-owned resources; it defines their
`close()`

and `is_valid`

contract.

-
*class*nccl.core.resources.CommResource(*comm: nccl.bindings.nccl.Comm*)[](https://docs.nvidia.com#nccl.core.resources.CommResource) Bases:

`ABC`

Abstract base class for NCCL communicator-owned resources.

Resources are tied to a specific communicator. They can be released explicitly via

. Resources created through a communicator are also released when that communicator is destroyed or aborted.`close()`

-
close() None
[](https://docs.nvidia.com#nccl.core.resources.CommResource.close) Explicitly deallocates the resource.

Idempotent: safe to call multiple times.


-
*property*is_valid*: bool*[](https://docs.nvidia.com#nccl.core.resources.CommResource.is_valid) Whether the resource has been initialized and is still valid (not closed).


-
close() None

## RegisteredBufferHandle[](https://docs.nvidia.com#registeredbufferhandle)

-
*class*nccl.core.RegisteredBufferHandle(*comm: nccl.bindings.nccl.Comm*,*buffer_ptr: int*,*size: int*)[](https://docs.nvidia.com#nccl.core.RegisteredBufferHandle) Bases:

`CommResource`

NCCL registered buffer handle for zero-copy optimized communication.

Registers a user buffer with the communicator to enable performance optimizations in NCCL operations. Created by

. The registration handle can be released explicitly via`Communicator.register_buffer()`

, or automatically when the owning communicator is destroyed or aborted.`close()`

-
*property*handle*: int*[](https://docs.nvidia.com#nccl.core.RegisteredBufferHandle.handle) Registration handle for NCCL operations.

- Raises:
**RuntimeError**– If the buffer has been deregistered or the handle is invalid.


-
*property*size*: int*[](https://docs.nvidia.com#nccl.core.RegisteredBufferHandle.size) Size of the registered buffer in bytes.


-
close() None
[](https://docs.nvidia.com#nccl.core.RegisteredBufferHandle.close) Explicitly deallocates the resource.

Idempotent: safe to call multiple times.


-
*property*is_valid*: bool*[](https://docs.nvidia.com#nccl.core.RegisteredBufferHandle.is_valid) Whether the resource has been initialized and is still valid (not closed).


-

## RegisteredWindowHandle[](https://docs.nvidia.com#registeredwindowhandle)

-
*class*nccl.core.RegisteredWindowHandle(*comm: nccl.bindings.nccl.Comm*,*buffer_ptr: int*,*size: int*,*flags:*)[WindowFlag](https://docs.nvidia.com/communicator/registration.html#nccl.core.WindowFlag)| None = None[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle) Bases:

`CommResource`

NCCL registered window handle for Remote Memory Access (RMA) operations.

Registers a memory window with the communicator for one-sided communication patterns. Created by

. Registration is collective: all ranks must call`Communicator.register_window()`

. Deregistration is local. The window handle can be released explicitly via`Communicator.register_window()`

, or automatically when the owning communicator is destroyed or aborted.`close()`

-
*property*is_valid*: bool*[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.is_valid) Whether the window is still registered (not closed, handle non-null).


-
*property*handle*: int*[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.handle) Window handle value, or

`0`

while unavailable or after deregistration.

-
*property*size*: int*[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.size) Size of the registered window in bytes.


-
*property*user_ptr*: int*[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.user_ptr) Original user buffer pointer registered with this window.

- Raises:
**RuntimeError**– If the window has been deregistered.


-
get_lsa_multimem_device_pointer(
*offset: int = 0*) int | None[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.get_lsa_multimem_device_pointer) Returns the LSA multicast device pointer for this window.

Returns a device pointer suitable for multicast operations over the LSA (Load/Store Accessible) team. The pointer is valid as long as the window and communicator remain alive.

- Parameters:
**offset**– Byte offset within the window buffer. Defaults to 0.- Returns:
Device pointer as int, or

`None`

if multimem is not supported.- Raises:
**RuntimeError**– If the window has been closed.


-
get_multimem_device_pointer(
*multimem:*,[MultimemHandle](https://docs.nvidia.com#nccl.core.MultimemHandle)*offset: int = 0*) int | None[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.get_multimem_device_pointer) Returns the multicast device pointer for this window and

`multimem`

.Unlike

(which uses the LSA team’s multimem), this resolves the pointer for an explicit multimem handle produced during device communicator creation.`get_lsa_multimem_device_pointer()`

- Parameters:
**multimem**– Areturned by`MultimemHandle`

.`DevCommResource.multimem_handle()`

**offset**– Byte offset within the window buffer. Defaults to 0.

- Returns:
Device pointer as int, or

`None`

if multimem is not supported.- Raises:
**RuntimeError**– If the window has been closed.


-
get_lsa_device_pointer(
*lsa_rank: int*,*offset: int = 0*) int[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.get_lsa_device_pointer) Returns the LSA device pointer for a peer within the LSA team.

Returns a device pointer to the peer’s window buffer addressable from the local GPU via LSA (Load/Store Accessible) mapping.

- Parameters:
**lsa_rank**– Rank within the LSA team (0 to lsa_size - 1).**offset**– Byte offset within the window buffer. Defaults to 0.

- Returns:
Device pointer as int.

- Raises:
**RuntimeError**– If the window has been closed.


-
get_peer_device_pointer(
*peer: int*,*offset: int = 0*) int | None[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.get_peer_device_pointer) Returns a device pointer to a peer’s window buffer by world rank.

If the peer is not reachable via LSA, returns

`None`

.- Parameters:
**peer**– World rank of the peer (0 to nranks - 1).**offset**– Byte offset within the window buffer. Defaults to 0.

- Returns:
Device pointer as int, or

`None`

if the peer is not reachable via LSA.- Raises:
**RuntimeError**– If the window has been closed.


-
get_multimem_le_info(
*offset: int = 0*)[CftLeInfo](https://docs.nvidia.com#nccl.core.CftLeInfo)[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.get_multimem_le_info) Returns the multicast logical endpoint address for this window and offset.

- Parameters:
**offset**– Byte offset within the window buffer. Defaults to 0.- Returns:
The logical endpoint address, as a

.`CftLeInfo`

- Raises:
**RuntimeError**– If the window has been closed.

See also


-
get_cft_le_info(
*peer_cft: int*,*cft_team:*,[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam)*offset: int = 0*)[CftLeInfo](https://docs.nvidia.com#nccl.core.CftLeInfo)[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.get_cft_le_info) Returns the logical endpoint address for a peer within

`cft_team`

.- Parameters:
**peer_cft**– Rank within`cft_team`

.**cft_team**– The CFT team, as returned by.`Communicator.team_cft()`

**offset**– Byte offset within the window buffer. Defaults to 0.

- Returns:
The logical endpoint address, as a

.`CftLeInfo`

- Raises:
**RuntimeError**– If the window has been closed.

See also


-
get_peer_le_info(
*peer: int*,*offset: int = 0*)[CftLeInfo](https://docs.nvidia.com#nccl.core.CftLeInfo)[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.get_peer_le_info) Returns the logical endpoint address for a peer by world rank.

- Parameters:
**peer**– World rank of the peer. Must fall within this rank’s flat CFT team, as returned by; NCCL rejects a peer outside it.`Communicator.team_cft()`

**offset**– Byte offset within the window buffer. Defaults to 0.

- Returns:
The logical endpoint address, as a

.`CftLeInfo`

- Raises:
**RuntimeError**– If the window has been closed.

See also


-
close() None
[](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle.close) Explicitly deallocates the resource.

Idempotent: safe to call multiple times.


-

## CftLeInfo[](https://docs.nvidia.com#cftleinfo)

Returned by the [ RegisteredWindowHandle](https://docs.nvidia.com#nccl.core.RegisteredWindowHandle) logical-endpoint queries.
CFT operations address memory by this pair rather than by pointer.

## CustomRedOp[](https://docs.nvidia.com#customredop)

-
*class*nccl.core.CustomRedOp(*comm: nccl.bindings.nccl.Comm*,*scalar_ptr: int*,*datatype:*,[NcclDataType](https://docs.nvidia.com/types.html#nccl.core.NcclDataType)*residence: nccl.bindings.nccl.ScalarResidence*)[](https://docs.nvidia.com#nccl.core.CustomRedOp) Bases:

`CommResource`

NCCL user-defined custom reduction operator.

Created by

. The PreMulSum operator performs`Communicator.create_pre_mul_sum()`

`output = scalar * sum(inputs)`

, useful for averaging or weighted reductions. The operator can be released explicitly via, or automatically when the owning communicator is destroyed or aborted.`close()`

-
*property*op*: int*[](https://docs.nvidia.com#nccl.core.CustomRedOp.op) Operator handle for use in reduction operations.

- Raises:
**RuntimeError**– If the operator has been destroyed or is invalid.


-
close() None
[](https://docs.nvidia.com#nccl.core.CustomRedOp.close) Explicitly deallocates the resource.

Idempotent: safe to call multiple times.


-
*property*is_valid*: bool*[](https://docs.nvidia.com#nccl.core.CustomRedOp.is_valid) Whether the resource has been initialized and is still valid (not closed).


-

## DevCommResource[](https://docs.nvidia.com#devcommresource)

-
*class*nccl.core.DevCommResource(*comm: _nccl_bindings.Comm*,*reqs_lowpp: _nccl_bindings.DevCommRequirements*,*team_multimem_lowpp: dict[*,[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam), _nccl_bindings.MultimemHandle] | None = None*resource_handle_lowpps: tuple[_nccl_bindings.LsaBarrierHandle | _nccl_bindings.GinBarrierHandle | _nccl_bindings.LLA2AHandle, ...] | None = None*)[](https://docs.nvidia.com#nccl.core.DevCommResource) Bases:

`CommResource`

NCCL device communicator resource for device-side operations.

Owns and manages an

created by`ncclDevComm_t`

. The device communicator is automatically destroyed when the parent communicator is destroyed or aborted.`Communicator.create_dev_comm()`

-
close() None
[](https://docs.nvidia.com#nccl.core.DevCommResource.close) Explicitly deallocates the resource.

Idempotent: safe to call multiple times.


-
*property*is_valid*: bool*[](https://docs.nvidia.com#nccl.core.DevCommResource.is_valid) Whether the resource has been initialized and is still valid (not closed).


-
*property*ptr*: int*[](https://docs.nvidia.com#nccl.core.DevCommResource.ptr) Address of the underlying

object, represented as a Python integer.`ncclDevComm_t`

- Raises:
**RuntimeError**– If the device communicator has been destroyed.


-
multimem_handle(
*team:*)[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam)[MultimemHandle](https://docs.nvidia.com#nccl.core.MultimemHandle)[](https://docs.nvidia.com#nccl.core.DevCommResource.multimem_handle) Returns the multimem handle requested for

`team`

.The returned handle references storage owned by this resource and remains valid until the device communicator is closed.

- Parameters:
**team**– The team the handle was requested for, as an entry of the`teams`

requirement used to create this device communicator.- Returns:
The

NCCL filled in for`MultimemHandle`

`team`

.- Raises:
**RuntimeError**– If the device communicator has been closed.**KeyError**– If`team`

was not requested with`multimem=True`

in the requirements used to create this device communicator.



-
*property*resource_handles*: tuple[*[LsaBarrierHandle](https://docs.nvidia.com#nccl.core.LsaBarrierHandle)|[GinBarrierHandle](https://docs.nvidia.com#nccl.core.GinBarrierHandle)|[LLA2AHandle](https://docs.nvidia.com#nccl.core.LLA2AHandle), ...][](https://docs.nvidia.com#nccl.core.DevCommResource.resource_handles) Finalized resource handles, in the order of

.`resources`

`resource_handles[i]`

corresponds to`requirements.resources[i]`

and is an,`LsaBarrierHandle`

, or`GinBarrierHandle`

depending on the requirement. Each remains backed by this resource until the device communicator is closed.`LLA2AHandle`


-
close() None

## Device resource handles[](https://docs.nvidia.com#device-resource-handles)

Handles returned by [ DevCommResource.resource_handles](https://docs.nvidia.com#nccl.core.DevCommResource.resource_handles) and

[. These are views backed by their owning](https://docs.nvidia.com#nccl.core.DevCommResource.multimem_handle)

`DevCommResource.multimem_handle()`

[, not independently closable resources. They remain valid only while that resource remains open. Pass one to the device-side APIs.](https://docs.nvidia.com#nccl.core.DevCommResource)

`DevCommResource`

### MultimemHandle[](https://docs.nvidia.com#multimemhandle)

-
*class*nccl.core.MultimemHandle(**args: Any*,***kwargs: Any*)[](https://docs.nvidia.com#nccl.core.MultimemHandle) Multimem handle, returned by

for a team requested with`multimem_handle()`

`multimem=True`

. Pass it to device-side multimem operations.

### LsaBarrierHandle[](https://docs.nvidia.com#lsabarrierhandle)

-
*class*nccl.core.LsaBarrierHandle(**args: Any*,***kwargs: Any*)[](https://docs.nvidia.com#nccl.core.LsaBarrierHandle) Load/Store Accessible (LSA) barrier handle, returned by

for each`resource_handles`

. Pass it to device-side barrier sessions.`LsaBarrierRequirement`


### GinBarrierHandle[](https://docs.nvidia.com#ginbarrierhandle)

-
*class*nccl.core.GinBarrierHandle(**args: Any*,***kwargs: Any*)[](https://docs.nvidia.com#nccl.core.GinBarrierHandle) GPU-Initiated Networking (GIN) barrier handle, returned by

for each`resource_handles`

. Pass it to device-side barrier sessions.`GinBarrierRequirement`


### LLA2AHandle[](https://docs.nvidia.com#lla2ahandle)

-
*class*nccl.core.LLA2AHandle(**args: Any*,***kwargs: Any*)[](https://docs.nvidia.com#nccl.core.LLA2AHandle) Low-latency all-to-all (LLA2A) handle, returned by

for each`resource_handles`

. Pass it to device-side all-to-all sessions.`LLA2ARequirement`