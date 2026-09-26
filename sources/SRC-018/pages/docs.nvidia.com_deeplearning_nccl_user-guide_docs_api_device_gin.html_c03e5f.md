source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/device_gin.html

# Device API – GIN[](https://docs.nvidia.com#device-api-gin)

## GIN[](https://docs.nvidia.com#gin)

**Device functions.** The following are callable from device (GPU) code only. GIN is supported since NCCL 2.28.7.

### ncclGin[](https://docs.nvidia.com#ncclgin)

-
class ncclGin
[](https://docs.nvidia.com#_CPPv47ncclGin) A class encompassing major elements of the GIN support.

-
ncclGin(ncclDevComm const &comm, int contextIndex)
[](https://docs.nvidia.com#_CPPv4N7ncclGin7ncclGinERK11ncclDevCommi) Initializes a new

`ncclGin`

object.*comm*is the device communicator created using.`ncclDevCommCreate()`

*contextIndex*is the index of the GIN context – a network communication channel. Using multiple GIN contexts allows the implementation to spread traffic onto multiple connections, avoiding locking and bottlenecks. Therefore, performance-oriented kernels should cycle among the available contexts to improve resource utilization (the number of available contexts is available via`ginContextCount`

).`ncclGin`

always represents one specific context. To run a barrier whose fence covers every GIN context on the comm (useful when operations have been sharded across multiple contexts – e.g. multi-NIC), pass`ncclGinAllContexts(comm)`

to`ncclGinBarrier()`

in place of an`ncclGin`

.

-
void put(ncclTeam team, int peer, ncclWindow_t dstWnd, size_t dstOffset, ncclWindow_t srcWnd, size_t srcOffset, size_t bytes, RemoteAction remoteAction, LocalAction localAction, Coop coop, DescriptorSmem descriptor, cuda::thread_scope alreadyReleased, cuda::thread_scope expected_scope, SegmentType bufType)
[](https://docs.nvidia.com#_CPPv4N7ncclGin3putE8ncclTeami12ncclWindow_t6size_t12ncclWindow_t6size_t6size_t12RemoteAction11LocalAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE11SegmentType) Schedules a device-initiated, one-sided data transfer operation from a local buffer to a remote buffer on a peer.

*peer*is a rank within*team*(see[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)); it may refer to the local rank (a loopback). The destination and source buffers are each specified using the window (*dstWnd*,*srcWnd*) and a byte-based offset (*dstOffset*,*srcOffset*).*bytes*specifies the data transfer count in bytes. If GIN is initialized with connection type,`NCCL_GIN_CONNECTION_RAIL`

*peer*must be within the same rail team as the local rank.Arguments beyond the first seven are optional.

*remoteAction*and*localAction*specify actions to undertake on the destination peer and on the local rank when the payload has been settled and the input has been consumed (respectively). They default to`ncclGin_None`

(no action); other options include`ncclGin_Signal{Inc|Add}`

(for*remoteAction*) and`ncclGin_CounterInc`

(for*localAction*); see[Signals and Counters](https://docs.nvidia.com#devapi-signals)below for more details.*coop*indicates the set of threads participating in this operation (see[Thread Groups](https://docs.nvidia.com/usage/deviceapi.html#devapi-coops)); it defaults to`ncclCoopThread`

(a single device thread), which is the recommended model.*bufType*specifies the physical memory composition of the source and destination buffers (see[Segment Types](https://docs.nvidia.com/usage/deviceapi.html#devapi-segment-types)); it defaults to`ncclGin_SegmentDevice`

.The visibility of the signal on the destination peer implies the visibility of the put data it is attached to. Depending on the signal type, the visibility of the signal may also imply the visibility of all the preceding puts to the same peer on the same context.

The API also defines an alternative, “convenience” variant of this method that uses

`ncclSymPtr`

types to specify the buffers and expects size to be conveyed in terms of the number of elements instead of the byte count. There are also two`putValue`

variants that take a single element at a time (no greater than eight bytes), passed by value.

-
void get(ncclTeam team, int peer, ncclWindow_t remoteWnd, size_t remoteOffset, ncclWindow_t localWnd, size_t localOffset, size_t bytes, Coop coop = ncclCoopThread{}, DescriptorSmem descriptor = ncclGin_None{}, uint32_t optFlags =
[ncclGinOptFlagsDefault](https://docs.nvidia.com/flags.html#_CPPv422ncclGinOptFlagsDefault), SegmentType bufType = ncclGin_SegmentDevice{})[](https://docs.nvidia.com#_CPPv4N7ncclGin3getE8ncclTeami12ncclWindow_t6size_t12ncclWindow_t6size_t6size_t4Coop14DescriptorSmem8uint32_t11SegmentType) Schedules a device-initiated, one-sided data transfer operation from a remote buffer to a local buffer (available since NCCL 2.30.3).

*peer*is a rank within*team*(see[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)); it may refer to the local rank (a loopback). The remote and local buffers are each specified using the window (*remoteWnd*,*localWnd*) and a byte-based offset (*remoteOffset*,*localOffset*).*bytes*specifies the data transfer count in bytes. If GIN is initialized with connection type,`NCCL_GIN_CONNECTION_RAIL`

*peer*must be within the same rail team as the local rank.*bufType*specifies the physical memory composition of the source and destination buffers (see[Segment Types](https://docs.nvidia.com/usage/deviceapi.html#devapi-segment-types)); it defaults to`ncclGin_SegmentDevice`

.*optFlags*is a bitwise OR of optional flags to the backend (see[GIN Optimization Flags](https://docs.nvidia.com/flags.html#gin-opt-flags)); it defaults to`ncclGinOptFlagsDefault`

.

-
void flush(Coop coop, cuda::memory_order ord = cuda::memory_order_acquire)
[](https://docs.nvidia.com#_CPPv4N7ncclGin5flushE4CoopN4cuda12memory_orderE) Ensures that all the pending transfer operations scheduled by any threads of

*coop*are locally consumed. For put operations, this means that the source buffers are safe to reuse; this makes no claims regarding the completion status on the remote peer(s). For get operations, this means that the data is visible to the local rank.

-
void flushAsync(ncclTeam team, uint32_t peer, ncclGinRequest_t *request, Coop coop = ncclCoopThread{}, uint32_t optFlags =
[ncclGinOptFlagsDefault](https://docs.nvidia.com/flags.html#_CPPv422ncclGinOptFlagsDefault), DescriptorSmem descriptor = ncclGin_None{})[](https://docs.nvidia.com#_CPPv4N7ncclGin10flushAsyncE8ncclTeam8uint32_tP16ncclGinRequest_t4Coop8uint32_t14DescriptorSmem) Initiates a non-blocking flush operation for one peer (see

).`ncclGin::flush()`

*peer*is a rank within*team*(see[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)).*request*is supplied by the caller and initialized by`flushAsync`

. The caller may use*request*to determine when the flush is complete (see). Available since NCCL 2.30.3.`ncclGin::wait()`


-
void wait(ncclGinRequest_t &request, Coop coop = ncclCoopThread{}, DescriptorSmem descriptor = ncclGin_None{}, cuda::memory_order ord = cuda::memory_order_acquire)
[](https://docs.nvidia.com#_CPPv4N7ncclGin4waitER16ncclGinRequest_t4Coop14DescriptorSmemN4cuda12memory_orderE) Blocks until

*request*is complete. Available since NCCL 2.30.3.

-
ncclGin(ncclDevComm const &comm, int contextIndex)

### Signals and Counters[](https://docs.nvidia.com#signals-and-counters)

-
type ncclGinSignal_t
[](https://docs.nvidia.com#_CPPv415ncclGinSignal_t) Signals are used to trigger actions on remote peers, most commonly on the completion of a

operation. They each have a 64-bit integer value associated with them that can be manipulated atomically.`ncclGin::put()`

Since NCCL 2.30.5, there are two types of signals:

*strong*and*weak*. Strong signals imply the visibility of all the preceding puts to the same peer on the same context. Weak signals imply only the visibility of the put data the signal is attached to.

-
struct ncclGin_StrongSignalInc
[](https://docs.nvidia.com#_CPPv423ncclGin_StrongSignalInc) -
[ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal[](https://docs.nvidia.com#_CPPv4N23ncclGin_StrongSignalInc6signalE)

-

-
struct ncclGin_StrongSignalAdd
[](https://docs.nvidia.com#_CPPv423ncclGin_StrongSignalAdd) -
[ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal[](https://docs.nvidia.com#_CPPv4N23ncclGin_StrongSignalAdd6signalE)

-
uint64_t value
[](https://docs.nvidia.com#_CPPv4N23ncclGin_StrongSignalAdd5valueE)

-

-
struct ncclGin_WeakSignalInc
[](https://docs.nvidia.com#_CPPv421ncclGin_WeakSignalInc) -
[ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal[](https://docs.nvidia.com#_CPPv4N21ncclGin_WeakSignalInc6signalE)

-

-
struct ncclGin_WeakSignalAdd
[](https://docs.nvidia.com#_CPPv421ncclGin_WeakSignalAdd) -
[ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal[](https://docs.nvidia.com#_CPPv4N21ncclGin_WeakSignalAdd6signalE)

-
uint64_t value
[](https://docs.nvidia.com#_CPPv4N21ncclGin_WeakSignalAdd5valueE)

-

These objects can be passed as the *remoteAction* arguments of methods such as [ ncclGin::put()](https://docs.nvidia.com#_CPPv4N7ncclGin3putE8ncclTeami12ncclWindow_t6size_t12ncclWindow_t6size_t6size_t12RemoteAction11LocalAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE11SegmentType) and

[to describe the actions to perform on the peer on receipt – in this case, increase the value of a](https://docs.nvidia.com#_CPPv4N7ncclGin6signalE8ncclTeami12RemoteAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE)

`ncclGin::signal()`

*signal*specified by index.

`SignalInc{signalIdx}`

is functionally equivalent to `SignalAdd{signalIdx, 1}`

; however, it
may not be mixed with other signal-modifying operations without an intervening signal reset (see below). Signal values
use “rolling” comparison logic to ensure that an unsigned overflow maintains the property of `x < x + 1`

.These objects represent “VA signals”: signals that are located at an arbitrary VA (window and offset pair) instead
of a pre-allocated signal index. Like the `ncclGin_StrongSignalInc`

and `ncclGin_StrongSignalAdd`

objects,
these objects can be passed as the *remoteAction* arguments of methods such as [ ncclGin::put()](https://docs.nvidia.com#_CPPv4N7ncclGin3putE8ncclTeami12ncclWindow_t6size_t12ncclWindow_t6size_t6size_t12RemoteAction11LocalAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE11SegmentType)
and

[to increment a signal on the peer. To use a VA signal, the window must be registered with flags](https://docs.nvidia.com#_CPPv4N7ncclGin6signalE8ncclTeami12RemoteAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE)

`ncclGin::signal()`

[. When an address is used as a signal, all reads and writes to the address must be issued via GIN (i.e., a](https://docs.nvidia.com/flags.html#c.NCCL_WIN_STRICT_ORDERING)

`NCCL_WIN_STRICT_ORDERING`

`RemoteAction`

or GIN signal method).-
struct ncclGin_VASignalInc
[](https://docs.nvidia.com#_CPPv419ncclGin_VASignalInc) Deprecated since version 2.30.5: Prefer

or`ncclGin_StrongVASignalInc`

instead.`ncclGin_WeakVASignalInc`

-
ncclWindow_t signalWindow
[](https://docs.nvidia.com#_CPPv4N19ncclGin_VASignalInc12signalWindowE)

-
size_t signalOffset
[](https://docs.nvidia.com#_CPPv4N19ncclGin_VASignalInc12signalOffsetE)

-
ncclWindow_t signalWindow

-
struct ncclGin_VASignalAdd
[](https://docs.nvidia.com#_CPPv419ncclGin_VASignalAdd) Deprecated since version 2.30.5: Prefer

or`ncclGin_StrongVASignalAdd`

instead.`ncclGin_WeakVASignalAdd`

-
ncclWindow_t signalWindow
[](https://docs.nvidia.com#_CPPv4N19ncclGin_VASignalAdd12signalWindowE)

-
size_t signalOffset
[](https://docs.nvidia.com#_CPPv4N19ncclGin_VASignalAdd12signalOffsetE)

-
uint64_t value
[](https://docs.nvidia.com#_CPPv4N19ncclGin_VASignalAdd5valueE)

-
ncclWindow_t signalWindow

-
struct ncclGin_SignalInc
[](https://docs.nvidia.com#_CPPv417ncclGin_SignalInc) Deprecated since version 2.30.5: Prefer

or`ncclGin_StrongSignalInc`

instead.`ncclGin_WeakSignalInc`

-
[ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal[](https://docs.nvidia.com#_CPPv4N17ncclGin_SignalInc6signalE)

-

-
struct ncclGin_SignalAdd
[](https://docs.nvidia.com#_CPPv417ncclGin_SignalAdd) Deprecated since version 2.30.5: Prefer

or`ncclGin_StrongSignalAdd`

instead.`ncclGin_WeakSignalAdd`

-
[ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal[](https://docs.nvidia.com#_CPPv4N17ncclGin_SignalAdd6signalE)

-
uint64_t value
[](https://docs.nvidia.com#_CPPv4N17ncclGin_SignalAdd5valueE)

-

Since NCCL 2.30.5, these signal types are deprecated in favor of explicitly strong and weak signal objects.
The strength of these signals is determined by the value of `ginStrongSignalsRequired`

when creating the device communicator.

**Signal methods of ncclGin:**

-
void
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::signal(ncclTeam team, int peer, RemoteAction remoteAction, Coop coop, DescriptorSmem descriptor, cuda::thread_scope alreadyReleased, cuda::thread_scope expected_scope)[](https://docs.nvidia.com#_CPPv4N7ncclGin6signalE8ncclTeami12RemoteAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE)

-
uint64_t
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::readSignal([ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal, int bits = 64, cuda::memory_order ord = cuda::memory_order_acquire)[](https://docs.nvidia.com#_CPPv4N7ncclGin10readSignalE15ncclGinSignal_tiN4cuda12memory_orderE)

-
void
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::waitSignal(Coop coop,[ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal, uint64_t least, int bits = 64, cuda::memory_order ord = cuda::memory_order_acquire)[](https://docs.nvidia.com#_CPPv4N7ncclGin10waitSignalE4Coop15ncclGinSignal_t8uint64_tiN4cuda12memory_orderE)

-
void
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::resetSignal([ncclGinSignal_t](https://docs.nvidia.com#_CPPv415ncclGinSignal_t)signal)[](https://docs.nvidia.com#_CPPv4N7ncclGin11resetSignalE15ncclGinSignal_t)

These are signal-specific methods of [ ncclGin](https://docs.nvidia.com#_CPPv47ncclGin).

[implements an explicit signal notification without an accompanying data transfer operation; it takes a subset of arguments of](https://docs.nvidia.com#_CPPv4N7ncclGin6signalE8ncclTeami12RemoteAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE)

`ncclGin::signal()`

[.](https://docs.nvidia.com#_CPPv4N7ncclGin3putE8ncclTeami12ncclWindow_t6size_t12ncclWindow_t6size_t6size_t12RemoteAction11LocalAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE11SegmentType)

`ncclGin::put()`

[returns the bottom](https://docs.nvidia.com#_CPPv4N7ncclGin10readSignalE15ncclGinSignal_tiN4cuda12memory_orderE)

`ncclGin::readSignal()`

*bits*of the value of the

*signal*.

[waits for the bottom](https://docs.nvidia.com#_CPPv4N7ncclGin10waitSignalE4Coop15ncclGinSignal_t8uint64_tiN4cuda12memory_orderE)

`ncclGin::waitSignal()`

*bits*of the

*signal*value to meet or exceed

*least*. Finally,

[resets the](https://docs.nvidia.com#_CPPv4N7ncclGin11resetSignalE15ncclGinSignal_t)

`ncclGin::resetSignal()`

*signal*value to

`0`

(this method may not race with
concurrent modifications to the signal).-
uint64_t
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::readSignal(ncclWindow_t signalWindow, size_t signalOffset, int bits = 64, cuda::memory_order ord = cuda::memory_order_acquire)[](https://docs.nvidia.com#_CPPv4N7ncclGin10readSignalE12ncclWindow_t6size_tiN4cuda12memory_orderE)

-
void
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::waitSignal(Coop coop, ncclWindow_t signalWindow, size_t signalOffset, uint64_t least, int bits = 64, cuda::memory_order ord = cuda::memory_order_acquire)[](https://docs.nvidia.com#_CPPv4N7ncclGin10waitSignalE4Coop12ncclWindow_t6size_t8uint64_tiN4cuda12memory_orderE)

These are VA signal-specific methods of [ ncclGin](https://docs.nvidia.com#_CPPv47ncclGin).

-
type ncclGinCounter_t
[](https://docs.nvidia.com#_CPPv416ncclGinCounter_t) Counters are used to trigger actions on the local rank; as such, they are complementary to signals, which are meant for remote actions. Like signals, they use “rolling” comparison logic, but they are limited to storing values of at most 56 bits.


-
struct ncclGin_CounterInc
[](https://docs.nvidia.com#_CPPv418ncclGin_CounterInc) -
[ncclGinCounter_t](https://docs.nvidia.com#_CPPv416ncclGinCounter_t)counter[](https://docs.nvidia.com#_CPPv4N18ncclGin_CounterInc7counterE)

-

This object can be passed as the *localAction* argument of methods such as [ ncclGin::put()](https://docs.nvidia.com#_CPPv4N7ncclGin3putE8ncclTeami12ncclWindow_t6size_t12ncclWindow_t6size_t6size_t12RemoteAction11LocalAction4Coop14DescriptorSmemN4cuda12thread_scopeEN4cuda12thread_scopeE11SegmentType). It is the only action
defined for counters.

**Counter methods of ncclGin:**

-
uint64_t
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::readCounter([ncclGinCounter_t](https://docs.nvidia.com#_CPPv416ncclGinCounter_t)counter, int bits = 56, cuda::memory_order ord = cuda::memory_order_acquire)[](https://docs.nvidia.com#_CPPv4N7ncclGin11readCounterE16ncclGinCounter_tiN4cuda12memory_orderE)

-
void
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::waitCounter(Coop coop,[ncclGinCounter_t](https://docs.nvidia.com#_CPPv416ncclGinCounter_t)counter, uint64_t least, int bits = 56, cuda::memory_order ord = cuda::memory_order_acquire)[](https://docs.nvidia.com#_CPPv4N7ncclGin11waitCounterE4Coop16ncclGinCounter_t8uint64_tiN4cuda12memory_orderE)

-
void
[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)::resetCounter([ncclGinCounter_t](https://docs.nvidia.com#_CPPv416ncclGinCounter_t)counter)[](https://docs.nvidia.com#_CPPv4N7ncclGin12resetCounterE16ncclGinCounter_t)

These are counter-specific methods of [ ncclGin](https://docs.nvidia.com#_CPPv47ncclGin) and they are functionally equivalent to their signal
counterparts discussed above.

### ncclGinBarrierSession[](https://docs.nvidia.com#ncclginbarriersession)

-
template<typename Coop>

class ncclGinBarrierSession[](https://docs.nvidia.com#_CPPv4I0E21ncclGinBarrierSession) A class representing a network barrier session.

-
ncclGinBarrierSession(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclGinBarrierSession)coop,[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)gin, ncclTeamTagRail tag, uint32_t index)[](https://docs.nvidia.com#_CPPv4N21ncclGinBarrierSession21ncclGinBarrierSessionE4Coop7ncclGin15ncclTeamTagRail8uint32_t) Initializes a new network barrier session.

*coop*represents a cooperative group (see[Thread Groups](https://docs.nvidia.com/usage/deviceapi.html#devapi-coops)).*gin*is a previously initializedobject.`ncclGin`

*ncclTeamTagRail*indicates that the barrier will apply to all peers on the same rail as the local rank (see[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)).*index*identifies the underlying barrier to use (it should be different for each*coop*; typically set to`blockIdx.x`

to ensure uniqueness between CTAs).

-
ncclGinBarrierSession(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclGinBarrierSession)coop,[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)gin, ncclTeam team, ncclGinBarrierHandle handle, uint32_t index)[](https://docs.nvidia.com#_CPPv4N21ncclGinBarrierSession21ncclGinBarrierSessionE4Coop7ncclGin8ncclTeam20ncclGinBarrierHandle8uint32_t) Initializes a new network barrier session. This is the general-purpose variant to be used, e.g., when communicating with ranks from the world team (see

[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)), whereas the previous variant was specific to the rail team. This variant expects*team*to be passed as an argument, and also takes an extra*handle*argument indicating the location of the underlying barriers (typically set to the`railGinBarrier`

field of the device communicator).

-
void sync(
[Coop](https://docs.nvidia.com#_CPPv4I0E21ncclGinBarrierSession)coop, cuda::memory_order order, ncclGinFenceLevel fence = ncclGinFenceLevel::Put | ncclGinFenceLevel::Get)[](https://docs.nvidia.com#_CPPv4N21ncclGinBarrierSession4syncE4CoopN4cuda12memory_orderE17ncclGinFenceLevel) Synchronizes all threads of all team members that participate in the barrier session. The

*fence*argument is a bit-flag enum selecting which prior network operations must be complete after the barrier returns; if omitted it defaults to`ncclGinFenceLevel::Put | ncclGinFenceLevel::Get`

so callers who do not opt in explicitly get the strongest guarantee:`ncclGinFenceLevel::None`

— pure synchronization, no drain.`ncclGinFenceLevel::Put`

— after the barrier returns, puts issued by other team members targeting the calling rank prior to the barrier are visible in the calling rank’s memory.`ncclGinFenceLevel::Get`

— after the barrier returns, gets issued by the calling rank prior to the barrier have landed in the calling rank’s local memory.

The fence values are bit flags and compose via bitwise OR. To request both

`Put`

and`Get`

semantics, pass`ncclGinFenceLevel::Put | ncclGinFenceLevel::Get`

.`ncclGinFenceLevel::Relaxed`

is preserved as a deprecated alias for`None`

for source-level backward compatibility; new code should use`None`

.

-
ncclGinBarrierSession(

### ncclBarrierSession[](https://docs.nvidia.com#ncclbarriersession)

-
template<typename Coop>

class ncclBarrierSession[](https://docs.nvidia.com#_CPPv4I0E18ncclBarrierSession) A class representing a hybrid barrier session. It combines a memory barrier over the

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)team () with a network barrier (`ncclLsaBarrierSession`

).`ncclGinBarrierSession`

-
ncclBarrierSession(
[Coop](https://docs.nvidia.com#_CPPv4I0E18ncclBarrierSession)coop, ncclTeamTagWorld tag,[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)gin, uint32_t index, bool multimem = false)[](https://docs.nvidia.com#_CPPv4N18ncclBarrierSession18ncclBarrierSessionE4Coop16ncclTeamTagWorld7ncclGin8uint32_tb) Initializes a new hybrid barrier session covering the world team (see

[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)).*coop*represents a cooperative group (see[Thread Groups](https://docs.nvidia.com/usage/deviceapi.html#devapi-coops)).*gin*is a previously initializedobject, used for the network part of the barrier.`ncclGin`

*index*identifies the underlying barrier to use (it should be unique for each*coop*; typically set to`blockIdx.x`

to ensure uniqueness between CTAs).*multimem*requests memory multicast for the LSA part of the barrier.

-
ncclBarrierSession(
[Coop](https://docs.nvidia.com#_CPPv4I0E18ncclBarrierSession)coop, ncclTeamTagRail tag,[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)gin, uint32_t index)[](https://docs.nvidia.com#_CPPv4N18ncclBarrierSession18ncclBarrierSessionE4Coop15ncclTeamTagRail7ncclGin8uint32_t) Initializes a new hybrid barrier session covering the rail team, i.e., all peers on the same rail as the local rank (see

[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)).

-
ncclBarrierSession(
[Coop](https://docs.nvidia.com#_CPPv4I0E18ncclBarrierSession)coop, ncclTeamTagLsa tag, ncclDevComm const &comm, uint32_t index, bool multimem = false)[](https://docs.nvidia.com#_CPPv4N18ncclBarrierSession18ncclBarrierSessionE4Coop14ncclTeamTagLsaRK11ncclDevComm8uint32_tb) Initializes a new hybrid barrier session covering the LSA team. Since no network traffic is involved, this variant takes the device communicator

*comm*(created using) instead of an`ncclDevCommCreate()`

object, and only the LSA barrier takes part in the session.`ncclGin`


-
ncclBarrierSession(
[Coop](https://docs.nvidia.com#_CPPv4I0E18ncclBarrierSession)coop, ncclTeam innerTeam, ncclTeam outerTeam,[ncclGin](https://docs.nvidia.com#_CPPv47ncclGin)gin, ncclLsaBarrierHandle innerBarHandle, ncclGinBarrierHandle outerBarHandle, uint32_t index, bool multimem = false, ncclMultimemHandle innerMmHandle = {})[](https://docs.nvidia.com#_CPPv4N18ncclBarrierSession18ncclBarrierSessionE4Coop8ncclTeam8ncclTeam7ncclGin20ncclLsaBarrierHandle20ncclGinBarrierHandle8uint32_tb18ncclMultimemHandle) Initializes a new hybrid barrier session. This is the general-purpose variant, to be used when the teams and the barrier locations are not the ones baked into the constructors above.

*innerTeam*and*innerBarHandle*describe the memory barrier, while*outerTeam*and*outerBarHandle*describe the network barrier.*innerMmHandle*provides the multicast handle backing the*multimem*implementation of the memory barrier.

-
void sync(
[Coop](https://docs.nvidia.com#_CPPv4I0E18ncclBarrierSession)coop, cuda::memory_order order, ncclGinFenceLevel fence = ncclGinFenceLevel::Put | ncclGinFenceLevel::Get)[](https://docs.nvidia.com#_CPPv4N18ncclBarrierSession4syncE4CoopN4cuda12memory_orderE17ncclGinFenceLevel) Synchronizes all threads of all team members that participate in the barrier session.

*fence*selects which prior network operations must be complete after the barrier returns; it has the same meaning and the same default as in.`ncclGinBarrierSession::sync()`

The selected barrier implementation is decided at run-time from the session’s team, the GIN connectivity of the device communicator (see

`ginConnectionType`

), and*fence*.

-
[ncclLsaBarrierSession](https://docs.nvidia.com/device_memory.html#_CPPv4I0E21ncclLsaBarrierSession)<[Coop](https://docs.nvidia.com#_CPPv4I0E18ncclBarrierSession)> &lsaBarrier()[](https://docs.nvidia.com#_CPPv4N18ncclBarrierSession10lsaBarrierEv)

-
[ncclGinBarrierSession](https://docs.nvidia.com#_CPPv4I0E21ncclGinBarrierSession)<[Coop](https://docs.nvidia.com#_CPPv4I0E18ncclBarrierSession)> &ginBarrier()[](https://docs.nvidia.com#_CPPv4N18ncclBarrierSession10ginBarrierEv) Returns the reference to the memory barrier or the rail network barrier underlying this hybrid session, so that it can be driven individually.


-
ncclBarrierSession(