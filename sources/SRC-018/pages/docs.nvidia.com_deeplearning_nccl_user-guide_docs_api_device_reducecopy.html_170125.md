source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/device_reducecopy.html

# Device API – Remote Reduce and Copy: Building Blocks for Custom Communication Kernels[](https://docs.nvidia.com#device-api-remote-reduce-and-copy-building-blocks-for-custom-communication-kernels)

**Device functions.** All functions on this page are callable from device (GPU) code only. They are **building blocks
for computation-fused kernels**: they implement reduce, copy (broadcast), and fused reduce-then-copy operations, keeping
communication and computation in a single kernel.

Key points:

**Communication patterns:**Sources and destinations can be on remote ranks (usingas input and output of the API), enabling direct implementation of patterns such as`ncclWindow_t`

[AllReduce](https://docs.nvidia.com/usage/collectives.html#allreduce),[AllGather](https://docs.nvidia.com/usage/collectives.html#allgather), and[ReduceScatter](https://docs.nvidia.com/usage/collectives.html#reducescatter).**Building blocks:**Each function implements one peak-bandwidth**communication building block**, not a full algorithm. You can combine these blocks (and your own computation) in tandem to implement custom communication patterns. The three building blocks are:[ReduceSum](https://docs.nvidia.com#device-api-reducecopy-reducesum)—*reduce*; e.g. reduce phase of AllReduce or ReduceScatter[Copy](https://docs.nvidia.com#device-api-reducecopy-copy)—*broadcast/copy*; e.g. broadcast phase of AllReduce or copy in AllGather[ReduceSumCopy](https://docs.nvidia.com#device-api-reducecopy-reducesumcopy)—*fused reduce-then-copy*; e.g. one-step AllReduce or reduce-to-chunks for ReduceScatter

For non-sum reductions, see

[Custom Reduction Operators](https://docs.nvidia.com#device-api-reducecopy-custom-redop).**API forms:**All functions are device-only (callable from`__device__`

code) and come in two forms:**high-level convenience overloads**(the direct summation overloads described in the sections below; they work with NCCL windows, teams, and device communicators) and**lambda-based overloads**, which offer more flexibility for custom layouts (see[Lambda-Based (Custom Layouts)](https://docs.nvidia.com#device-api-reducecopy-lambda)).**GIN:**This API does not support[GIN](https://docs.nvidia.com/device_gin.html#device-api-gin)(GPU-Initiated Networking) implicitly; use this API within the[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)domain and implement an explicit hierarchical design with NCCL GIN to exchange data between LSA domains.**Invocation model (not rank-collective):**These functions are not rank-collective (unlike host API such as). For a given memory region (e.g. a`ncclAllReduce()`

, offset, and count), only a single rank must issue the API call that uses that region. The per-operation sections specify whether each role is multi-rank (each rank issues for its own region) or single-rank (one rank issues for that region).`ncclWindow_t`

**Memory:**Source and destination regions must not overlap (except when exactly in-place: same buffer and same offset); otherwise behavior is undefined. The caller must ensure all arguments and buffer layouts meet the documented requirements; the API does not perform runtime checks.**Alignment:**For best performance, use 16-byte aligned source and destination pointers.

## Compile-Time Requirements[](https://docs.nvidia.com#compile-time-requirements)

`NCCL_DEVICE_PERMIT_EXPERIMENTAL_CODE`

must be defined to `1`

before including the NCCL device headers so that all
block sizes and type combinations are supported for **multimem** operations (see
[multimem reduce](https://docs.nvidia.com#ncclmultimemreducesum-symptr), [multimem copy](https://docs.nvidia.com#ncclmultimemcopy-symptr), and related
multimem APIs below). Without it, certain combinations of low-precision types, *count*, and pointer alignment
in multimem operations may hit runtime asserts. Because only one rank might trigger an assert, this can also lead to
hangs. Defining it means the user acknowledges that they are willing to use cutting-edge APIs that might change between
releases.

**Lambda-based overloads** The API uses device-side C++ lambda functions for overloads that take callables
(e.g. lambdas) to describe source or destination layouts. The API also offers user-facing lambda-based overloads; see
[Lambda-Based (Custom Layouts)](https://docs.nvidia.com#device-api-reducecopy-lambda). Code that includes the NCCL device headers for
this API must always be compiled with CUDA extended lambdas enabled (e.g. `--extended-lambda`

with nvcc); otherwise
you may get a compile-time static assert. See the
[CUDA documentation for extended lambdas](https://docs.nvidia.com/cuda/cuda-programming-guide/05-appendices/cpp-language-support.html#extended-lambdas).

## API Overview[](https://docs.nvidia.com#api-overview)

[ReduceSum](https://docs.nvidia.com#device-api-reducecopy-reducesum)— Reduce building block.[Copy](https://docs.nvidia.com#device-api-reducecopy-copy)— Broadcast/copy building block.[ReduceSumCopy](https://docs.nvidia.com#device-api-reducecopy-reducesumcopy)— Fused reduce-then-copy building block.

**Common template parameters**


TElement type. Supported types are:

`float`

,`double`

,`half`

,`int8`

,`int16`

,`int32`

,`int64`

; and, when available, the following low-precision types:`__nv_bfloat16`

,`__nv_fp8_e4m3`

, and`__nv_fp8_e5m2`

. For low-precision types, sum reduction is accumulated in a wider type:


T

Accumulation type

`half`


`float`


`__nv_bfloat16`


`float`


`__nv_fp8_e4m3`


`half`


`__nv_fp8_e5m2`


`half`

For multimem reduce, this wider accumulation is performed on the NVLink Switch.

CoopCooperation level (see

[Thread Groups]), e.g.`ncclCoopCta`

or`ncclCoopThread`

. All threads in the cooperative group defined byCoopmust participate in the call.IntCountType for the element count. The user can choose a 32-bit integer type (e.g.

`unsigned int`

) or a 64-bit integer type (e.g.`size_t`

) depending on the size of the block region the API operates on.UNROLLOptional; default

`4*16/sizeof(T)`

. UNROLL represents the tradeoff between register usage and achievable peak bandwidth; the optimal value depends on the register usage of the surrounding kernel. HigherUNROLLallows vectorized load/store and more loop unrolling, which helps achieve peak bandwidth. High register usage can lower occupancy and may lead to register spilling; see the[CUDA Programming Guide section on kernel launch and occupancy]. The default is chosen to make good performance possible on most systems.Example (ReduceSumCopy with

T=`float`

,Coop=`ncclCoopCta`

,IntCount=`size_t`

, andUNROLLset to the default for float,`4*16/sizeof(float)`

= 16):size_t srcOffset = [...]; // byte offset into symmetric send buffer on each peer size_t dstOffset = [...]; // byte offset into symmetric recv buffer on each peer ncclLsaReduceSumCopy<float, ncclCoopCta, size_t, 16>(ctaCoop, sendwin, srcOffset, recvwin, dstOffset, count, team);

## ReduceSum — N Sources to One Destination[](https://docs.nvidia.com#reducesum-n-sources-to-one-destination)

All ReduceSum variants reduce from N sources to one destination using sum. See [common template parameters](https://docs.nvidia.com#device-api-reducecopy-common-params) (*T*, *Coop*, *IntCount*, *UNROLL*).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSum([Coop](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount13ncclDevComm_t)coop, ncclWindow_t window, size_t offset,[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount13ncclDevComm_t)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount13ncclDevComm_t)count, ncclDevComm_t devComm)[](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount13ncclDevComm_t) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Reduces from the symmetric buffer at

*window*+*offset*on all[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)peers into local*dstPtr*. The reduction is over all LSA ranks in the communicator; pass*devComm*(the device communicator).*coop*is the cooperative group (see[Thread Groups](https://docs.nvidia.com/usage/deviceapi.html#devapi-coops)).*window*is the window handle from a prior host-side`ncclCommWindowRegister`

and must be the same window (and communicator) as*devComm*; the buffer region must remain registered for the duration of the call.*offset*is the byte offset into*window*where the source buffer starts on each peer;*offset*+*count*×`sizeof(T)`

must not exceed the size of the registered window.*dstPtr*is the local device pointer to the destination buffer; it must point to at least*count*elements of type*T*and must be accessible by all participating threads according to*coop*.*count*is the number of elements to reduce; it must be the same on all[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)ranks, non-negative, and consistent with*IntCount*.*devComm*is the device communicator.**Barrier usage:**When using remote memory, synchronize before and after the call (see example below).Example:

ncclCoopCta ctaCoop; ncclLsaBarrierSession<ncclCoopCta> bar { ctaCoop, devComm, ncclTeamLsa(devComm), devComm.lsaBarrier, blockIdx.x }; bar.sync(ctaCoop, cuda::memory_order_acquire); size_t srcOffset = [...]; // byte offset into symmetric send buffer on each peer size_t dstOffset = [...]; // byte offset into symmetric recv buffer on each peer T* dstPtr = (T*)ncclGetLocalPointer(recvwin, dstOffset); ncclLsaReduceSum<T, ncclCoopCta, size_t>(ctaCoop, sendwin, srcOffset, dstPtr, count, devComm); bar.sync(ctaCoop, cuda::memory_order_release);


-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSum([Coop](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount8ncclTeam)coop, ncclWindow_t window, size_t offset,[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount8ncclTeam)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount8ncclTeam)count, ncclTeam team)[](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount8ncclTeam) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsareducesum-window-devcomm), except the user passes*team*explicitly (e.g.`ncclTeamLsa(devComm)`

) instead of*devComm*. All other parameters, invocation, and barrier usage are as documented for the overload above.*team*is the team of[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)ranks (see[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)).Example:

ncclTeam team = ncclTeamLsa(devComm); ncclLsaReduceSum<T, ncclCoopCta, size_t>(ctaCoop, sendwin, srcOffset, dstPtr, count, team);


-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSum([Coop](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount13ncclDevComm_t)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount13ncclDevComm_t)> src,[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount13ncclDevComm_t)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount13ncclDevComm_t)count, ncclDevComm_t devComm)[](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount13ncclDevComm_t) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsareducesum-window-devcomm), but the source is given by symmetric pointer*src*instead of (window, offset).*dstPtr*,*count*, and*devComm*are as for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm). With`ncclSymPtr`

you can construct with 0 offset and use`src + elementOffset`

(offset in elements, no`sizeof(T)`

).Example:

ncclSymPtr<float> src{sendwin, 0}; ncclLsaReduceSum<float, ncclCoopCta, size_t>(ctaCoop, src + elementOffset, dstPtr, count, devComm);


-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSum([Coop](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount8ncclTeam)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount8ncclTeam)> src,[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount8ncclTeam)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount8ncclTeam)count, ncclTeam team)[](https://docs.nvidia.com#_CPPv4I000_iE16ncclLsaReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount8ncclTeam) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsareducesum-symptr-devcomm), except the user passes*team*explicitly instead of*devComm*. The team is derived from the device communicator (e.g.`ncclTeamLsa(devComm)`

).Example:

ncclSymPtr<float> src{sendwin, 0}; ncclTeam team = ncclTeamLsa(devComm); ncclLsaReduceSum<float, ncclCoopCta, size_t>(ctaCoop, src + elementOffset, dstPtr, count, team);


-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLocalReduceSum([Coop](https://docs.nvidia.com#_CPPv4I000_iE18ncclLocalReduceSumv4CoopiP1T6size_tP1T8IntCount)coop, int nSrc,[T](https://docs.nvidia.com#_CPPv4I000_iE18ncclLocalReduceSumv4CoopiP1T6size_tP1T8IntCount)*basePtr, size_t displ,[T](https://docs.nvidia.com#_CPPv4I000_iE18ncclLocalReduceSumv4CoopiP1T6size_tP1T8IntCount)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE18ncclLocalReduceSumv4CoopiP1T6size_tP1T8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE18ncclLocalReduceSumv4CoopiP1T6size_tP1T8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-team), but over**local**sources only (no other ranks, no remote memory). Sources are strided: the*i*-th source is at`basePtr + i*displ`

for*i*= 0…*nSrc*− 1.*basePtr*is the base pointer,*displ*is the stride in bytes;*dstPtr*and*count*are as for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-team).

**Multimem reduce (ncclMultimemReduceSum)** — Multimem reduce uses NVLink SHARP (NVLS) multicast; the NVLink
Switch performs the reduction from multimem sources. To query NVLS/multimem capability from the host, call
[ ncclCommQueryProperties()](https://docs.nvidia.com/device_setup.html#c.ncclCommQueryProperties) and check the

`multimemSupport`

field of [.](https://docs.nvidia.com/device_setup.html#c.ncclCommProperties_t)

`ncclCommProperties_t`

**Multimem restriction:**The local rank (self) must always be part of the multimem reduction or store; the multimem source or destination logically includes the calling rank. For multimem reduce, supported element types are

`float`

, `double`

, `half`

; the low-precision types when available: `__nv_bfloat16`

, `__nv_fp8_e4m3`

,
`__nv_fp8_e5m2`

; and `int32`

, `uint32`

, `int64`

, `uint64`

. The
define described above (e.g. `NCCL_DEVICE_PERMIT_EXPERIMENTAL_CODE=1`

) may need to be set for all type
and block-size combinations.-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemReduceSum([Coop](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount18ncclMultimemHandle)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount18ncclMultimemHandle)> src,[T](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount18ncclMultimemHandle)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount18ncclMultimemHandle)count, ncclMultimemHandle multimemHandle)[](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop10ncclSymPtrI1TEP1T8IntCount18ncclMultimemHandle) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Reduces from the multimem source

*src*(one logical buffer maps to all participating ranks) into local*dstPtr*. Invocation as for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm).*src*is the symmetric pointer to the multimem source;*dstPtr*is the local destination;*count*is the number of elements;*multimemHandle*identifies the multimem context. To obtain it, set`lsaMultimem`

to true inwhen calling`ncclDevCommRequirements`

; the handle is then available from the device communicator in device code.`ncclDevCommCreate()`


-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemReduceSum([Coop](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4CoopP1TP1T8IntCount)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4CoopP1TP1T8IntCount)*mcSrcPtr,[T](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4CoopP1TP1T8IntCount)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4CoopP1TP1T8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4CoopP1TP1T8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#ncclmultimemreducesum-symptr), but the source is given by raw multimem pointer*mcSrcPtr*instead of`ncclSymPtr`

+ handle (e.g. from host-side).`ncclGetLsaMultimemDevicePointer()`

*dstPtr*and*count*are as for[ncclMultimemReduceSum](https://docs.nvidia.com#ncclmultimemreducesum-symptr).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemReduceSum([Coop](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount18ncclMultimemHandle)coop, ncclWindow_t window, size_t offset,[T](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount18ncclMultimemHandle)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount18ncclMultimemHandle)count, ncclMultimemHandle multimemHandle)[](https://docs.nvidia.com#_CPPv4I000_iE21ncclMultimemReduceSumv4Coop12ncclWindow_t6size_tP1T8IntCount18ncclMultimemHandle) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#ncclmultimemreducesum-symptr), but the source is given by*window*+*offset*(byte offset) and*multimemHandle*, analogous to the window-based LSA overload.*dstPtr*and*count*are as for[ncclMultimemReduceSum](https://docs.nvidia.com#ncclmultimemreducesum-symptr).

## Copy (Broadcast) — One Source to N Destinations[](https://docs.nvidia.com#copy-broadcast-one-source-to-n-destinations)

All Copy variants copy from one source to N destinations. See [common template parameters](https://docs.nvidia.com#device-api-reducecopy-common-params). Invocation as for
[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm); for Copy, the source is local to the invoking rank.

On SM 10.0 and later (Blackwell), [ncclLsaCopyTma](https://docs.nvidia.com#nccllsacopytma-window-devcomm) is a Tensor Memory Accelerator
(TMA) implementation of the same LSA copy. It stages user data through a caller-provided shared memory buffer.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T12ncclWindow_t6size_t8IntCount13ncclDevComm_t)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T12ncclWindow_t6size_t8IntCount13ncclDevComm_t)*srcPtr, ncclWindow_t window, size_t offset,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T12ncclWindow_t6size_t8IntCount13ncclDevComm_t)count, ncclDevComm_t devComm)[](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T12ncclWindow_t6size_t8IntCount13ncclDevComm_t) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Copies from local

*srcPtr*into the symmetric buffer at*window*+*offset*on all[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)peers. Pass*devComm*(the device communicator).*srcPtr*is the local source;*window*and*offset*define the destination region on each peer;*count*is the number of elements. Barrier usage: synchronize before and after when using remote memory (see[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm)).Example (e.g. broadcast phase of AllGather):

ncclCoopCta ctaCoop; ncclLsaBarrierSession<ncclCoopCta> bar { ctaCoop, devComm, ncclTeamLsa(devComm), devComm.lsaBarrier, blockIdx.x }; bar.sync(ctaCoop, cuda::memory_order_acquire); size_t srcOffset = [...]; // byte offset into symmetric send buffer on each peer size_t dstOffset = [...]; // byte offset into symmetric recv buffer on each peer T* srcPtr = (T*)ncclGetLocalPointer(sendwin, srcOffset); ncclLsaCopy<T, ncclCoopCta, size_t>(ctaCoop, srcPtr, recvwin, dstOffset, count, devComm); bar.sync(ctaCoop, cuda::memory_order_release);


-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T12ncclWindow_t6size_t8IntCount8ncclTeam)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T12ncclWindow_t6size_t8IntCount8ncclTeam)*srcPtr, ncclWindow_t window, size_t offset,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T12ncclWindow_t6size_t8IntCount8ncclTeam)count, ncclTeam team)[](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T12ncclWindow_t6size_t8IntCount8ncclTeam) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsacopy-window-devcomm), except the user passes*team*explicitly (e.g.`ncclTeamLsa(devComm)`

) instead of*devComm*.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_t)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_t)*srcPtr, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_t)> dst,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_t)count, ncclDevComm_t devComm)[](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_t) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsacopy-window-devcomm), but the destination is given by symmetric pointer*dst*instead of (window, offset).*srcPtr*,*count*, and*devComm*are as for[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm). You can construct*dst*with 0 offset and use`dst + elementOffset`

for element-based indexing.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeam)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeam)*srcPtr, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeam)> dst,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeam)count, ncclTeam team)[](https://docs.nvidia.com#_CPPv4I000_iE11ncclLsaCopyv4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeam) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsacopy-symptr-devcomm), except the user passes*team*explicitly instead of*devComm*.

**TMA copy (ncclLsaCopyTma)** — Same LSA copy as [ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm), implemented with
the Tensor Memory Accelerator. Compile and launch the kernel for SM 10.0+ (`__CUDA_ARCH__ >= 1000`

). Pass a
compile time staging-buffer size of *SmemBytesTotal* and a pointer to that buffer.

**Requirements (caller must guarantee).** Violating these is undefined behavior.

**Architecture:**Device code must be compiled and the kernel launched on SM 10.0 or later. On older architectures the call is a no op.**Coop:***Coop*must be`ncclCoopThread`

,`ncclCoopWarp`

, or`ncclCoopCta`

.**Element type:**`sizeof(T)`

must divide 16 (the TMA transfer unit). This holds for the types listed under[common template parameters](https://docs.nvidia.com#device-api-reducecopy-common-params).**Count:**`count * sizeof(T)`

must be a multiple of 16.**Alignment:***srcPtr*, every destination, and*smemPtr*must be 16-byte aligned. Window and`ncclSymPtr`

destinations satisfy this for all peers at once, since a window offset has the same alignment on every LSA peer. For a custom destination lambda there is no such guarantee — each pointer it returns must be 16-byte aligned on its own.**Shared memory:***SmemBytesTotal*must be at least 32 bytes (16 bytes of staging data plus a 16-byte mbarrier) and must not exceed the number of shared-memory bytes the kernel actually provides at*smemPtr*. The launch must reserve at least*SmemBytesTotal*bytes of dynamic shared memory when*smemPtr*is dynamic`__shared__`

.

-
template<typename T, typename Coop, typename IntCount, int SmemBytesTotal>

void ncclLsaCopyTma([Coop](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T12ncclWindow_t6size_t8IntCount13ncclDevComm_tPc)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T12ncclWindow_t6size_t8IntCount13ncclDevComm_tPc)*srcPtr, ncclWindow_t window, size_t offset,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T12ncclWindow_t6size_t8IntCount13ncclDevComm_tPc)count, ncclDevComm_t devComm, char *smemPtr)[](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T12ncclWindow_t6size_t8IntCount13ncclDevComm_tPc) For shared requirements (invocation model, memory), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy). For TMA architecture, coop, alignment, count, and shared-memory requirements, see[above](https://docs.nvidia.com#device-api-reducecopy-tma-requirements).Copies from local

*srcPtr*into the symmetric buffer at*window*+*offset*on all[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)peers, staging through*smemPtr*. Pass*devComm*(the device communicator).*srcPtr*,*window*,*offset*, and*count*are as for[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm).*smemPtr*is the start of*SmemBytesTotal*bytes of 16-byte-aligned shared memory owned by the caller. Barrier usage: synchronize before and after when using remote memory (see[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm)).Example — differs from

[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm)only in the staging buffer. Device side:constexpr int smemBytes = 16 << 10; // 16 KiB staging for the whole CTA extern __shared__ char smemScratch[]; ncclLsaCopyTma<T, ncclCoopCta, size_t, smemBytes>(ctaCoop, srcPtr, recvwin, dstOffset, count, devComm, smemScratch);

Host side, which must reserve the same byte count:

cudaFuncSetAttribute(kernel, cudaFuncAttributeMaxDynamicSharedMemorySize, smemBytes); kernel<<<grid, block, smemBytes, stream>>>(...);


-
template<typename T, typename Coop, typename IntCount, int SmemBytesTotal>

void ncclLsaCopyTma([Coop](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T12ncclWindow_t6size_t8IntCount8ncclTeamPc)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T12ncclWindow_t6size_t8IntCount8ncclTeamPc)*srcPtr, ncclWindow_t window, size_t offset,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T12ncclWindow_t6size_t8IntCount8ncclTeamPc)count, ncclTeam team, char *smemPtr)[](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T12ncclWindow_t6size_t8IntCount8ncclTeamPc) For shared requirements (invocation model, memory), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy). For TMA requirements, see[above](https://docs.nvidia.com#device-api-reducecopy-tma-requirements).Same as

[above](https://docs.nvidia.com#nccllsacopytma-window-devcomm), except the user passes*team*explicitly (e.g.`ncclTeamLsa(devComm)`

) instead of*devComm*.

-
template<typename T, typename Coop, typename IntCount, int SmemBytesTotal>

void ncclLsaCopyTma([Coop](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_tPc)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_tPc)*srcPtr, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_tPc)> dst,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_tPc)count, ncclDevComm_t devComm, char *smemPtr)[](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount13ncclDevComm_tPc) For shared requirements (invocation model, memory), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy). For TMA requirements, see[above](https://docs.nvidia.com#device-api-reducecopy-tma-requirements).Same as

[above](https://docs.nvidia.com#nccllsacopytma-window-devcomm), but the destination is given by symmetric pointer*dst*instead of (window, offset).*srcPtr*,*count*,*devComm*, and*smemPtr*are as for[ncclLsaCopyTma](https://docs.nvidia.com#nccllsacopytma-window-devcomm). You can construct*dst*with 0 offset and use`dst + elementOffset`

for element-based indexing.

-
template<typename T, typename Coop, typename IntCount, int SmemBytesTotal>

void ncclLsaCopyTma([Coop](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeamPc)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeamPc)*srcPtr, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeamPc)> dst,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeamPc)count, ncclTeam team, char *smemPtr)[](https://docs.nvidia.com#_CPPv4I000_iE14ncclLsaCopyTmav4CoopP1T10ncclSymPtrI1TE8IntCount8ncclTeamPc) For shared requirements (invocation model, memory), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy). For TMA requirements, see[above](https://docs.nvidia.com#device-api-reducecopy-tma-requirements).Same as

[above](https://docs.nvidia.com#nccllsacopytma-symptr-devcomm), except the user passes*team*explicitly instead of*devComm*.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLocalCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE13ncclLocalCopyv4CoopP1TiP1T6size_t8IntCount)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE13ncclLocalCopyv4CoopP1TiP1T6size_t8IntCount)*srcPtr, int nDst,[T](https://docs.nvidia.com#_CPPv4I000_iE13ncclLocalCopyv4CoopP1TiP1T6size_t8IntCount)*basePtr, size_t displ,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE13ncclLocalCopyv4CoopP1TiP1T6size_t8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE13ncclLocalCopyv4CoopP1TiP1T6size_t8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-team)for thread-cooperation behavior, but**local**only (no other ranks, no remote memory): copies from single source*srcPtr*to*nDst*strided destinations at`basePtr + i*displ`

for*i*= 0…*nDst*− 1.*displ*is the stride in bytes;*count*is the number of elements copied to each destination.

**Multimem copy (ncclMultimemCopy)** — Copies from one local source to one multimem destination (one logical buffer
over all ranks). Uses NVLink SHARP (NVLS) multicast. Query `multimemSupport`

for capability; *multimemHandle*
as for [multimem reduce](https://docs.nvidia.com#ncclmultimemreducesum-symptr). All element types are supported; for types less than
32 bits wide, the define described above (e.g. `NCCL_DEVICE_PERMIT_EXPERIMENTAL_CODE=1`

) must be set for some
count and pointer combinations.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T10ncclSymPtrI1TE8IntCount18ncclMultimemHandle)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T10ncclSymPtrI1TE8IntCount18ncclMultimemHandle)*srcPtr, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T10ncclSymPtrI1TE8IntCount18ncclMultimemHandle)> dst,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T10ncclSymPtrI1TE8IntCount18ncclMultimemHandle)count, ncclMultimemHandle multimemHandle)[](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T10ncclSymPtrI1TE8IntCount18ncclMultimemHandle) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Copies from local

*srcPtr*into the multimem destination*dst*(one logical buffer maps to all participating ranks). Invocation as for[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm).*multimemHandle*as for[ncclMultimemReduceSum](https://docs.nvidia.com#ncclmultimemreducesum-symptr).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1TP1T8IntCount)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1TP1T8IntCount)*srcPtr,[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1TP1T8IntCount)*mcDstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1TP1T8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1TP1T8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#ncclmultimemcopy-symptr), but the destination is given by raw multimem pointer*mcDstPtr*(e.g. from).`ncclGetLsaMultimemDevicePointer()`

*srcPtr*and*count*are as for[ncclMultimemCopy](https://docs.nvidia.com#ncclmultimemcopy-symptr).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T12ncclWindow_t6size_t8IntCount18ncclMultimemHandle)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T12ncclWindow_t6size_t8IntCount18ncclMultimemHandle)*srcPtr, ncclWindow_t window, size_t offset,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T12ncclWindow_t6size_t8IntCount18ncclMultimemHandle)count, ncclMultimemHandle multimemHandle)[](https://docs.nvidia.com#_CPPv4I000_iE16ncclMultimemCopyv4CoopP1T12ncclWindow_t6size_t8IntCount18ncclMultimemHandle) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#ncclmultimemcopy-symptr), but the destination is given by*window*+*offset*(byte offset) and*multimemHandle*.*srcPtr*and*count*are as for[ncclMultimemCopy](https://docs.nvidia.com#ncclmultimemcopy-symptr).

## ReduceSumCopy[](https://docs.nvidia.com#reducesumcopy)

ReduceSumCopy combines reduction and copy into a single call. See [common template parameters](https://docs.nvidia.com#device-api-reducecopy-common-params). Invocation as documented for the
[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm) and
[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm) overloads above.

### LSA ReduceSumCopy (ncclLsaReduceSumCopy)[](https://docs.nvidia.com#lsa-reducesumcopy-nccllsareducesumcopy)

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop12ncclWindow_t6size_t12ncclWindow_t6size_t8IntCount13ncclDevComm_t)coop, ncclWindow_t srcWindow, size_t srcOffset, ncclWindow_t dstWindow, size_t dstOffset,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop12ncclWindow_t6size_t12ncclWindow_t6size_t8IntCount13ncclDevComm_t)count, ncclDevComm_t devComm)[](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop12ncclWindow_t6size_t12ncclWindow_t6size_t8IntCount13ncclDevComm_t) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Reduces from the

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)source at*srcWindow*+*srcOffset*(all LSA peers) and copies the result to the LSA destination at*dstWindow*+*dstOffset*(all LSA peers) in one call. Pass*devComm*(the device communicator).*srcOffset*and*dstOffset*are byte offsets;*count*is the number of elements. When using remote memory, barrier usage is the same as for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm)and[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm): synchronize before and after the call (see the examples there).Example (e.g. LSA AllReduce; see

`test/perf/all_reduce.cu`

for block-parallel chunking):ncclCoopCta ctaCoop; ncclLsaBarrierSession<ncclCoopCta> bar { ctaCoop, devComm, ncclTeamLsa(devComm), devComm.lsaBarrier, blockIdx.x }; bar.sync(ctaCoop, cuda::memory_order_acquire); size_t srcOffset = [...]; // byte offset into symmetric send buffer on each peer size_t dstOffset = [...]; // byte offset into symmetric recv buffer on each peer ncclLsaReduceSumCopy<T, ncclCoopCta, size_t>(ctaCoop, sendwin, srcOffset, recvwin, dstOffset, count, devComm); bar.sync(ctaCoop, cuda::memory_order_release);


-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop12ncclWindow_t6size_t12ncclWindow_t6size_t8IntCount8ncclTeam)coop, ncclWindow_t srcWindow, size_t srcOffset, ncclWindow_t dstWindow, size_t dstOffset,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop12ncclWindow_t6size_t12ncclWindow_t6size_t8IntCount8ncclTeam)count, ncclTeam team)[](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop12ncclWindow_t6size_t12ncclWindow_t6size_t8IntCount8ncclTeam) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsareducesumcopy-window-devcomm), except the user passes*team*explicitly (e.g.`ncclTeamLsa(devComm)`

) instead of*devComm*.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount13ncclDevComm_t)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount13ncclDevComm_t)> src, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount13ncclDevComm_t)> dst,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount13ncclDevComm_t)count, ncclDevComm_t devComm)[](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount13ncclDevComm_t) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsareducesumcopy-window-devcomm), but the source is given by symmetric pointer*src*and the destination by symmetric pointer*dst*instead of (window, offset).*count*and*devComm*are as for[ncclLsaReduceSumCopy](https://docs.nvidia.com#nccllsareducesumcopy-window-devcomm).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount8ncclTeam)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount8ncclTeam)> src, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount8ncclTeam)> dst,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount8ncclTeam)count, ncclTeam team)[](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE10ncclSymPtrI1TE8IntCount8ncclTeam) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsareducesumcopy-symptr-devcomm), except the user passes*team*explicitly instead of*devComm*.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE8ncclTeam8IntCount)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE8ncclTeam8IntCount)> src, ncclTeam srcTeam, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE8ncclTeam8IntCount)> dst, ncclTeam dstTeam,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE8ncclTeam8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE20ncclLsaReduceSumCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE8ncclTeam8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaReduceSumCopy](https://docs.nvidia.com#nccllsareducesumcopy-window-team), but source and destination use different teams (*srcTeam*and*dstTeam*). Ranks in one team must still be load-store accessible (LSA) from ranks in the other (same LSA communicator; involved ranks must be able to access each other’s registered memory).*src*is the source symmetric pointer over*srcTeam*;*dst*is the destination symmetric pointer over*dstTeam*.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLocalReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE22ncclLocalReduceSumCopyv4CoopiP1T6size_tiP1T6size_t8IntCount)coop, int nSrc,[T](https://docs.nvidia.com#_CPPv4I000_iE22ncclLocalReduceSumCopyv4CoopiP1T6size_tiP1T6size_t8IntCount)*srcBasePtr, size_t srcDispl, int nDst,[T](https://docs.nvidia.com#_CPPv4I000_iE22ncclLocalReduceSumCopyv4CoopiP1T6size_tiP1T6size_t8IntCount)*dstBasePtr, size_t dstDispl,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE22ncclLocalReduceSumCopyv4CoopiP1T6size_tiP1T6size_t8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE22ncclLocalReduceSumCopyv4CoopiP1T6size_tiP1T6size_t8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaReduceSumCopy](https://docs.nvidia.com#nccllsareducesumcopy-window-team)for thread-cooperation behavior, but**local**only (no other ranks, no remote memory). Reduces from*nSrc*strided sources at`srcBasePtr + i*srcDispl`

(i = 0…*nSrc*− 1) and copies the result to*nDst*strided destinations at`dstBasePtr + j*dstDispl`

(j = 0…*nDst*− 1).*srcDispl*and*dstDispl*are strides in bytes;*count*is the number of elements per source/destination.

### Multimem ReduceSumCopy (ncclMultimemReduceSumCopy)[](https://docs.nvidia.com#multimem-reducesumcopy-ncclmultimemreducesumcopy)

Reduces from one multimem source and copies to one multimem destination (each one logical buffer maps to all
participating ranks) in one call. To query multimem capability from the host, call [ ncclCommQueryProperties()](https://docs.nvidia.com/device_setup.html#c.ncclCommQueryProperties)
and check the

`multimemSupport`

field of [. The multimem handle is obtained by setting](https://docs.nvidia.com/device_setup.html#c.ncclCommProperties_t)

`ncclCommProperties_t`

`lsaMultimem`

to true in [when calling](https://docs.nvidia.com/device_setup.html#c.ncclDevCommRequirements)

`ncclDevCommRequirements`

[; it is then available from the device communicator in device code.](https://docs.nvidia.com/device_setup.html#c.ncclDevCommCreate)

`ncclDevCommCreate()`

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4Coop12ncclWindow_t6size_t18ncclMultimemHandle12ncclWindow_t6size_t18ncclMultimemHandle8IntCount)coop, ncclWindow_t srcWindow, size_t srcOffset, ncclMultimemHandle srcHandle, ncclWindow_t dstWindow, size_t dstOffset, ncclMultimemHandle dstHandle,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4Coop12ncclWindow_t6size_t18ncclMultimemHandle12ncclWindow_t6size_t18ncclMultimemHandle8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4Coop12ncclWindow_t6size_t18ncclMultimemHandle12ncclWindow_t6size_t18ncclMultimemHandle8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Reduces from the multimem source at

*srcWindow*+*srcOffset*and copies to the multimem destination at*dstWindow*+*dstOffset*in one call.*srcHandle*and*dstHandle*identify the multimem contexts (may be the same or different). Invocation as documented for the[overload above](https://docs.nvidia.com#nccllsareducesum-window-team).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE18ncclMultimemHandle8IntCount)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE18ncclMultimemHandle8IntCount)> src, ncclMultimemHandle srcHandle, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE18ncclMultimemHandle8IntCount)> dst, ncclMultimemHandle dstHandle,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE18ncclMultimemHandle8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE18ncclMultimemHandle8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#ncclmultimemreducesumcopy-window), but the source is given by symmetric pointer*src*and the destination by symmetric pointer*dst*instead of (window, offset).*srcHandle*and*dstHandle*are as for[ncclMultimemReduceSumCopy](https://docs.nvidia.com#ncclmultimemreducesumcopy-window).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemReduceSumCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4CoopP1TP1T8IntCount)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4CoopP1TP1T8IntCount)*mcSrcPtr,[T](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4CoopP1TP1T8IntCount)*mcDstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4CoopP1TP1T8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE25ncclMultimemReduceSumCopyv4CoopP1TP1T8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#ncclmultimemreducesumcopy-symptr), but source and destination are given by raw multimem pointers*mcSrcPtr*and*mcDstPtr*(e.g. from).`ncclGetLsaMultimemDevicePointer()`


### Mixed LSA and Multimem ReduceSumCopy[](https://docs.nvidia.com#mixed-lsa-and-multimem-reducesumcopy)

Reduce from [LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa) and write to multimem, or reduce from multimem and write to LSA, in one call.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSumMultimemCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE18ncclMultimemHandle8IntCount)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE18ncclMultimemHandle8IntCount)> src, ncclTeam srcTeam, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE18ncclMultimemHandle8IntCount)> dst, ncclMultimemHandle dstHandle,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE18ncclMultimemHandle8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeam10ncclSymPtrI1TE18ncclMultimemHandle8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Reduces from

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)source*src*over*srcTeam*and copies to multimem destination*dst*(one logical buffer maps to all participating ranks).*dstHandle*as for[ncclMultimemCopy](https://docs.nvidia.com#ncclmultimemcopy-symptr). Invocation as documented for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm)and[ncclMultimemCopy](https://docs.nvidia.com#ncclmultimemcopy-symptr).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclLsaReduceSumMultimemCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeamP1T8IntCount)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeamP1T8IntCount)> src, ncclTeam srcTeam,[T](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeamP1T8IntCount)*mcDstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeamP1T8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE28ncclLsaReduceSumMultimemCopyv4Coop10ncclSymPtrI1TE8ncclTeamP1T8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#nccllsareducesummultimemcopy-symptr), but the multimem destination is given by raw pointer*mcDstPtr*instead of`ncclSymPtr`

+ handle.

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemReduceSumLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE8ncclTeam8IntCount)coop, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE8ncclTeam8IntCount)> src, ncclMultimemHandle srcHandle, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE8ncclTeam8IntCount)> dst, ncclTeam dstTeam,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE8ncclTeam8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4Coop10ncclSymPtrI1TE18ncclMultimemHandle10ncclSymPtrI1TE8ncclTeam8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Reduces from multimem source

*src*and copies to[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)destination*dst*over*dstTeam*.*srcHandle*as for[ncclMultimemReduceSum](https://docs.nvidia.com#ncclmultimemreducesum-symptr). Invocation as documented for[ncclMultimemReduceSum](https://docs.nvidia.com#ncclmultimemreducesum-symptr)and[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm).

-
template<typename T, typename Coop, typename IntCount, int UNROLL>

void ncclMultimemReduceSumLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4CoopP1T10ncclSymPtrI1TE8ncclTeam8IntCount)coop,[T](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4CoopP1T10ncclSymPtrI1TE8ncclTeam8IntCount)*mcSrcPtr, ncclSymPtr<[T](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4CoopP1T10ncclSymPtrI1TE8ncclTeam8IntCount)> dst, ncclTeam dstTeam,[IntCount](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4CoopP1T10ncclSymPtrI1TE8ncclTeam8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000_iE28ncclMultimemReduceSumLsaCopyv4CoopP1T10ncclSymPtrI1TE8ncclTeam8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[above](https://docs.nvidia.com#ncclmultimemreducesumlsacopy-symptr), but the multimem source is given by raw pointer*mcSrcPtr*instead of`ncclSymPtr`

+ handle.

## Lambda-Based (Custom Layouts)[](https://docs.nvidia.com#lambda-based-custom-layouts)

Lambda-based overloads give more flexibility and allow custom memory layouts for reduce and/or copy. They can mix
local and [LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)-remote sources or destinations (e.g. one source from local memory, others from
LSA windows), and can express non-contiguous or index-dependent addressing that the fixed window/symptr overloads do
not support.

**Conditions for the lambda.** The callable (e.g. lambda) must return `T*`

and be invocable from device code with
a single index argument. When the callable is a lambda, it must be qualified with `__device__`

and the build must
have CUDA extended lambdas enabled (see [Compile-Time Requirements](https://docs.nvidia.com#device-api-reducecopy-compile)). Let *n* be
the associated count (*nSrc* or *nDst* depending on the API).

*n*> 0. Otherwise behavior is undefined.For every index

*i*in [0,*n*), the call*lambda*(*i*) must return a pointer to the start of a valid region of at least*count*contiguous elements of type*T*. The same restrictions apply as for the corresponding non-lambda API: e.g. for[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)sources/destinations the region must be in registered LSA memory and remain valid for the duration of the call; for local pointers they must be accessible to all threads in*coop*.When the API designates source or destination as

**multimem**, every pointer returned by the lambda for that side must be a**multimem pointer**(e.g. from). Using LSA or local pointers for the multimem side is undefined behavior. Conversely, multimem pointers cannot be used where LSA or local pointers are accepted.`ncclGetLsaMultimemDevicePointer()`

The relationship between

*n*and the logical set of sources or destinations is as documented for each API (e.g.*nSrc*sources meaning*nSrc*distinct source regions, or*nDst*destinations meaning*nDst*distinct destination regions).

Violating any of these conditions is undefined behavior; the API does not perform runtime checks.

Example: reduce from a window over a team, but **exclude the local rank** (e.g. reduce only from remote peers).
Use a source lambda that maps index *i* to the *i*-th *other* rank and pass *nSrc* = *team*`.nRanks`

− 1:

```
size_t srcOffset = [...]; // byte offset into symmetric send buffer on each peer
ncclTeam team = ncclTeamLsa(devComm);
int myRank = devComm.rank;
int nSrc = team.nRanks - 1; // all ranks except this one
auto srcLambda = [=] __device__ (int i) -> T* {
int peer = (i < myRank) ? i : i + 1; // skip myRank
return (T*)ncclGetLsaPointer(sendwin, srcOffset, peer);
};
ncclLsaReduceSum<T, ncclCoopCta, size_t>(ctaCoop, srcLambda, nSrc, dstPtr, count);
```

-
template<typename T, typename Coop, typename SrcLambda, typename IntCount, int UNROLL>

void ncclLsaReduceSum([Coop](https://docs.nvidia.com#_CPPv4I0000_iE16ncclLsaReduceSumv4Coop9SrcLambdaiP1T8IntCount)coop,[SrcLambda](https://docs.nvidia.com#_CPPv4I0000_iE16ncclLsaReduceSumv4Coop9SrcLambdaiP1T8IntCount)srcLambda, int nSrc,[T](https://docs.nvidia.com#_CPPv4I0000_iE16ncclLsaReduceSumv4Coop9SrcLambdaiP1T8IntCount)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I0000_iE16ncclLsaReduceSumv4Coop9SrcLambdaiP1T8IntCount)count)[](https://docs.nvidia.com#_CPPv4I0000_iE16ncclLsaReduceSumv4Coop9SrcLambdaiP1T8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-team), but the source layout is given by*srcLambda*(index) returning ``T*`` for each of *nSrc*sources; result to local*dstPtr*.*coop*and*count*as for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-team).*srcLambda*is called with indices 0 to*nSrc*− 1.

-
template<typename T, typename Coop, typename SrcLambda, typename IntCount, int UNROLL>

void ncclLocalReduceSum([Coop](https://docs.nvidia.com#_CPPv4I0000_iE18ncclLocalReduceSumv4Coop9SrcLambdaiP1T8IntCount)coop,[SrcLambda](https://docs.nvidia.com#_CPPv4I0000_iE18ncclLocalReduceSumv4Coop9SrcLambdaiP1T8IntCount)srcLambda, int nSrc,[T](https://docs.nvidia.com#_CPPv4I0000_iE18ncclLocalReduceSumv4Coop9SrcLambdaiP1T8IntCount)*dstPtr,[IntCount](https://docs.nvidia.com#_CPPv4I0000_iE18ncclLocalReduceSumv4Coop9SrcLambdaiP1T8IntCount)count)[](https://docs.nvidia.com#_CPPv4I0000_iE18ncclLocalReduceSumv4Coop9SrcLambdaiP1T8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-team), but over**local**sources only (no other ranks, no remote memory).*srcLambda*(index) returns ``T*`` for each of *nSrc*sources; result to*dstPtr*.*coop*and*count*as for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-team).*srcLambda*is called with indices 0 to*nSrc*− 1.

-
template<typename T, typename Coop, typename DstLambda, typename IntCount, int UNROLL>

void ncclLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I0000_iE11ncclLsaCopyv4CoopP1T9DstLambdai8IntCount)coop,[T](https://docs.nvidia.com#_CPPv4I0000_iE11ncclLsaCopyv4CoopP1T9DstLambdai8IntCount)*srcPtr,[DstLambda](https://docs.nvidia.com#_CPPv4I0000_iE11ncclLsaCopyv4CoopP1T9DstLambdai8IntCount)dstLambda, int nDst,[IntCount](https://docs.nvidia.com#_CPPv4I0000_iE11ncclLsaCopyv4CoopP1T9DstLambdai8IntCount)count)[](https://docs.nvidia.com#_CPPv4I0000_iE11ncclLsaCopyv4CoopP1T9DstLambdai8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-team), but the destination layout is given by*dstLambda*(index) returning ``T*`` for each of *nDst*destinations.*srcPtr*is the local source;*coop*and*count*as for[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-team).*dstLambda*is called with indices 0 to*nDst*− 1.

-
template<typename T, typename Coop, typename DstLambda, typename IntCount, int SmemBytesTotal>

void ncclLsaCopyTma([Coop](https://docs.nvidia.com#_CPPv4I0000_iE14ncclLsaCopyTmav4CoopP1T9DstLambdai8IntCountPc)coop,[T](https://docs.nvidia.com#_CPPv4I0000_iE14ncclLsaCopyTmav4CoopP1T9DstLambdai8IntCountPc)*srcPtr,[DstLambda](https://docs.nvidia.com#_CPPv4I0000_iE14ncclLsaCopyTmav4CoopP1T9DstLambdai8IntCountPc)dstLambda, int nDst,[IntCount](https://docs.nvidia.com#_CPPv4I0000_iE14ncclLsaCopyTmav4CoopP1T9DstLambdai8IntCountPc)count, char *smemPtr)[](https://docs.nvidia.com#_CPPv4I0000_iE14ncclLsaCopyTmav4CoopP1T9DstLambdai8IntCountPc) For shared requirements (invocation model, memory), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy). For TMA architecture, coop, alignment, count, and shared-memory requirements, see[TMA copy requirements](https://docs.nvidia.com#device-api-reducecopy-tma-requirements). For the lambda itself, see[Conditions for the lambda](https://docs.nvidia.com#device-api-reducecopy-lambda).Same as

[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-lambda)for the destination layout, but implemented with TMA as[ncclLsaCopyTma](https://docs.nvidia.com#nccllsacopytma-window-team).*dstLambda*(index) returns ``T*`` for each of *nDst*destinations. Each destination pointer is independent and must itself be 16-byte aligned.*srcPtr*is the local source;*smemPtr*is the staging buffer;*coop*and*count*are as for[ncclLsaCopyTma](https://docs.nvidia.com#nccllsacopytma-window-team).*dstLambda*is called with indices 0 to*nDst*− 1.Example:

ncclTeam team = ncclTeamLsa(devComm); auto dstLambda = [=] __device__ (int i) -> T* { return (T*)ncclGetLsaPointer(recvwin, dstOffset, i); }; ncclLsaCopyTma<T, ncclCoopCta, decltype(dstLambda), size_t, smemBytes>( ctaCoop, srcPtr, dstLambda, team.nRanks, count, smemScratch);


-
template<typename T, typename Coop, typename DstLambda, typename IntCount, int UNROLL>

void ncclLocalCopy([Coop](https://docs.nvidia.com#_CPPv4I0000_iE13ncclLocalCopyv4CoopP1T9DstLambdai8IntCount)coop,[T](https://docs.nvidia.com#_CPPv4I0000_iE13ncclLocalCopyv4CoopP1T9DstLambdai8IntCount)*srcPtr,[DstLambda](https://docs.nvidia.com#_CPPv4I0000_iE13ncclLocalCopyv4CoopP1T9DstLambdai8IntCount)dstLambda, int nDst,[IntCount](https://docs.nvidia.com#_CPPv4I0000_iE13ncclLocalCopyv4CoopP1T9DstLambdai8IntCount)count)[](https://docs.nvidia.com#_CPPv4I0000_iE13ncclLocalCopyv4CoopP1T9DstLambdai8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-team), but**local**only (no other ranks, no remote memory).*dstLambda*(index) returns ``T*`` for each of *nDst*destinations;*srcPtr*,*coop*, and*count*as for[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-team).*dstLambda*is called with indices 0 to*nDst*− 1.

The following four overloads are the lambda-based forms of ReduceSumCopy. They differ by whether the **source** and
**destination** are **:ref:`LSA <device_api_lsa>`** or **multimem**. For any **multimem** side, the common case is a
single multimem pointer (one already represents multiple remote spaces). Multiple multimem pointers are also
supported; the API then
initiates multicast to or from all of them.

Warning

Multicast always includes the self rank. With more than one multimem source or destination, this creates overlapping ranks. The user must ensure correctness.

-
template<typename T, typename Coop, typename SrcLambda, typename DstLambda, typename IntCount, int UNROLL>

void ncclLsaReduceSumLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I00000_iE23ncclLsaReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount)coop,[SrcLambda](https://docs.nvidia.com#_CPPv4I00000_iE23ncclLsaReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount)srcLambda, int nSrc,[DstLambda](https://docs.nvidia.com#_CPPv4I00000_iE23ncclLsaReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount)dstLambda, int nDst,[IntCount](https://docs.nvidia.com#_CPPv4I00000_iE23ncclLsaReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount)count)[](https://docs.nvidia.com#_CPPv4I00000_iE23ncclLsaReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).**Source: :ref:`LSA <device_api_lsa>`. Destination: LSA.**Same as[ncclLsaReduceSumCopy](https://docs.nvidia.com#nccllsareducesumcopy-window-team), but the source layout is given by*srcLambda*(*i*) returning`T*`

for each of*nSrc*sources (*i*= 0 to*nSrc*− 1) and the destination layout by*dstLambda*(*j*) for each of*nDst*destinations (*j*= 0 to*nDst*− 1).*coop*and*count*as for[ncclLsaReduceSumCopy](https://docs.nvidia.com#nccllsareducesumcopy-window-team). When using remote memory, barrier usage is as for[ncclLsaReduceSumCopy](https://docs.nvidia.com#nccllsareducesumcopy-window-devcomm).

-
template<typename T, typename Coop, typename SrcLambda, typename DstLambda, typename IntCount, int UNROLL>

void ncclLsaReduceSumMultimemCopy([Coop](https://docs.nvidia.com#_CPPv4I00000_iE28ncclLsaReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount)coop,[SrcLambda](https://docs.nvidia.com#_CPPv4I00000_iE28ncclLsaReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount)srcLambda, int nSrc,[DstLambda](https://docs.nvidia.com#_CPPv4I00000_iE28ncclLsaReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount)dstLambda, int nDst,[IntCount](https://docs.nvidia.com#_CPPv4I00000_iE28ncclLsaReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount)count)[](https://docs.nvidia.com#_CPPv4I00000_iE28ncclLsaReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).**Source: :ref:`LSA <device_api_lsa>`. Destination: multimem.**Same as[ncclLsaReduceSumMultimemCopy](https://docs.nvidia.com#nccllsareducesummultimemcopy-symptr), but the source layout is given by*srcLambda*(*i*) for*i*= 0 to*nSrc*− 1 and the destination layout by*dstLambda*(*j*) for*j*= 0 to*nDst*− 1.*srcLambda*returns[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)pointers;*dstLambda*must return multimem pointers (e.g. from). The common case is`ncclGetLsaMultimemDevicePointer()`

*nDst*= 1.*coop*and*count*as for[ncclLsaReduceSumCopy](https://docs.nvidia.com#nccllsareducesumcopy-window-team). Invocation as documented for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm)and[ncclMultimemCopy](https://docs.nvidia.com#ncclmultimemcopy-symptr).

-
template<typename T, typename Coop, typename SrcLambda, typename DstLambda, typename IntCount, int UNROLL>

void ncclMultimemReduceSumLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I00000_iE28ncclMultimemReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount)coop,[SrcLambda](https://docs.nvidia.com#_CPPv4I00000_iE28ncclMultimemReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount)srcLambda, int nSrc,[DstLambda](https://docs.nvidia.com#_CPPv4I00000_iE28ncclMultimemReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount)dstLambda, int nDst,[IntCount](https://docs.nvidia.com#_CPPv4I00000_iE28ncclMultimemReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount)count)[](https://docs.nvidia.com#_CPPv4I00000_iE28ncclMultimemReduceSumLsaCopyv4Coop9SrcLambdai9DstLambdai8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).**Source: multimem. Destination: :ref:`LSA <device_api_lsa>`.**Same as[ncclMultimemReduceSumLsaCopy](https://docs.nvidia.com#ncclmultimemreducesumlsacopy-symptr), but the source layout is given by*srcLambda*(*i*) for*i*= 0 to*nSrc*− 1 and the destination layout by*dstLambda*(*j*) for*j*= 0 to*nDst*− 1.*srcLambda*must return multimem pointers (e.g. from);`ncclGetLsaMultimemDevicePointer()`

*dstLambda*returns[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)pointers. The common case is*nSrc*= 1.*coop*and*count*as for[ncclMultimemReduceSumLsaCopy](https://docs.nvidia.com#ncclmultimemreducesumlsacopy-symptr). Invocation as documented for[ncclMultimemReduceSum](https://docs.nvidia.com#ncclmultimemreducesum-symptr)and[ncclLsaCopy](https://docs.nvidia.com#nccllsacopy-window-devcomm).

-
template<typename T, typename Coop, typename SrcLambda, typename DstLambda, typename IntCount, int UNROLL>

void ncclMultimemReduceSumMultimemCopy([Coop](https://docs.nvidia.com#_CPPv4I00000_iE33ncclMultimemReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount)coop,[SrcLambda](https://docs.nvidia.com#_CPPv4I00000_iE33ncclMultimemReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount)srcLambda, int nSrc,[DstLambda](https://docs.nvidia.com#_CPPv4I00000_iE33ncclMultimemReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount)dstLambda, int nDst,[IntCount](https://docs.nvidia.com#_CPPv4I00000_iE33ncclMultimemReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount)count)[](https://docs.nvidia.com#_CPPv4I00000_iE33ncclMultimemReduceSumMultimemCopyv4Coop9SrcLambdai9DstLambdai8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).**Source: multimem. Destination: multimem.**Same as[ncclMultimemReduceSumCopy](https://docs.nvidia.com#ncclmultimemreducesumcopy-window), but the source layout is given by*srcLambda*(*i*) for*i*= 0 to*nSrc*− 1 and the destination layout by*dstLambda*(*j*) for*j*= 0 to*nDst*− 1.*srcLambda*and*dstLambda*must each return multimem pointers (e.g. from). The common case is a single multimem source and a single multimem destination.`ncclGetLsaMultimemDevicePointer()`

*coop*and*count*as for[ncclMultimemReduceSumCopy](https://docs.nvidia.com#ncclmultimemreducesumcopy-window). Invocation as documented for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-team).

## Custom Reduction Operators[](https://docs.nvidia.com#custom-reduction-operators)

The APIs below take an explicit reduction operator (*redOp*) instead of a fixed sum, enabling custom reductions
(e.g. min, max, product). **Restrictions for *redOp*:**

*redOp*is a callable (e.g. functor or lambda) that takes two arguments of type*T*(or`const T&`

) and returns*T*(the combined value).No order is guaranteed in which elements are combined; the reduction may be applied in any order across the sources.

The callable must be

**const**: it must not modify internal state. If*redOp*is a functor, its`operator()`

must be`const`

; stateless lambdas satisfy this by default. Violating this is undefined behavior.

-
template<typename T, typename Coop, typename SrcLambda, typename DstLambda, typename RedOp, typename IntCount, int UNROLL>

void ncclLsaReduceLsaCopy([Coop](https://docs.nvidia.com#_CPPv4I000000_iE20ncclLsaReduceLsaCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)coop,[SrcLambda](https://docs.nvidia.com#_CPPv4I000000_iE20ncclLsaReduceLsaCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)srcLambda, int nSrc,[DstLambda](https://docs.nvidia.com#_CPPv4I000000_iE20ncclLsaReduceLsaCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)dstLambda, int nDst,[RedOp](https://docs.nvidia.com#_CPPv4I000000_iE20ncclLsaReduceLsaCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)const &redOp,[IntCount](https://docs.nvidia.com#_CPPv4I000000_iE20ncclLsaReduceLsaCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000000_iE20ncclLsaReduceLsaCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaReduceSumLsaCopy](https://docs.nvidia.com#nccllsareducesumlsacopy-lambda), but the reduction is performed with the explicit*redOp*callable instead of sum.*redOp*must satisfy the restrictions above. Sources and destinations are[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa).*srcLambda*and*dstLambda*are as for the[lambda-based ReduceSumCopy APIs](https://docs.nvidia.com#nccllsareducesumlsacopy-lambda);*coop*,*count*, and barrier usage as for[ncclLsaReduceSumCopy](https://docs.nvidia.com#nccllsareducesumcopy-window-team).

-
template<typename T, typename Coop, typename SrcLambda, typename DstLambda, typename RedOp, typename IntCount, int UNROLL>

void ncclLsaReduceMultimemCopy([Coop](https://docs.nvidia.com#_CPPv4I000000_iE25ncclLsaReduceMultimemCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)coop,[SrcLambda](https://docs.nvidia.com#_CPPv4I000000_iE25ncclLsaReduceMultimemCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)srcLambda, int nSrc,[DstLambda](https://docs.nvidia.com#_CPPv4I000000_iE25ncclLsaReduceMultimemCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)dstLambda, int nDst,[RedOp](https://docs.nvidia.com#_CPPv4I000000_iE25ncclLsaReduceMultimemCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)const &redOp,[IntCount](https://docs.nvidia.com#_CPPv4I000000_iE25ncclLsaReduceMultimemCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount)count)[](https://docs.nvidia.com#_CPPv4I000000_iE25ncclLsaReduceMultimemCopyv4Coop9SrcLambdai9DstLambdaiRK5RedOp8IntCount) For shared requirements (invocation model, memory, alignment), see the

[introduction](https://docs.nvidia.com#device-api-reducecopy).Same as

[ncclLsaReduceSumMultimemCopy](https://docs.nvidia.com#nccllsareducesummultimemcopy-lambda), but the reduction is performed with the explicit*redOp*callable instead of sum.*redOp*must satisfy the restrictions above. Sources are[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa); destinations are multimem (one logical buffer maps to all participating ranks).*dstLambda*must return multimem pointers (e.g. from). For custom reduction operators, use this API with`ncclGetLsaMultimemDevicePointer()`

[LSA](https://docs.nvidia.com/usage/bufferreg.html#device-api-lsa)sources and multimem destinations; the multimem hardware path supports only sum.*coop*and*count*as for[ncclLsaReduceSumMultimemCopy](https://docs.nvidia.com#nccllsareducesummultimemcopy-lambda). Invocation as documented for[ncclLsaReduceSum](https://docs.nvidia.com#nccllsareducesum-window-devcomm)and[ncclMultimemCopy](https://docs.nvidia.com#ncclmultimemcopy-symptr).