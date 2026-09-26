source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/types.html

# Types[](https://docs.nvidia.com#types)

The following types are used by the NCCL library.

## ncclComm_t[](https://docs.nvidia.com#ncclcomm-t)

-
type ncclComm_t
[](https://docs.nvidia.com#c.ncclComm_t) NCCL communicator. Points to an opaque structure inside NCCL.


## ncclResult_t[](https://docs.nvidia.com#ncclresult-t)

-
type ncclResult_t
[](https://docs.nvidia.com#c.ncclResult_t) Return values for all NCCL functions. Possible values are:

-
ncclSuccess
[](https://docs.nvidia.com#c.ncclResult_t.ncclSuccess) (

`0`

) Function succeeded.

-
ncclUnhandledCudaError
[](https://docs.nvidia.com#c.ncclResult_t.ncclUnhandledCudaError) (

`1`

) A call to a CUDA function failed.

-
ncclSystemError
[](https://docs.nvidia.com#c.ncclResult_t.ncclSystemError) (

`2`

) A call to the system failed.

-
ncclInternalError
[](https://docs.nvidia.com#c.ncclResult_t.ncclInternalError) (

`3`

) An internal check failed. This is due to either a bug in NCCL or a memory corruption.

-
ncclInvalidArgument
[](https://docs.nvidia.com#c.ncclResult_t.ncclInvalidArgument) (

`4`

) An argument has an invalid value.

-
ncclInvalidUsage
[](https://docs.nvidia.com#c.ncclResult_t.ncclInvalidUsage) (

`5`

) The call to NCCL is incorrect. This is usually reflecting a programming error.

-
ncclRemoteError
[](https://docs.nvidia.com#c.ncclResult_t.ncclRemoteError) (

`6`

) A call failed possibly due to a network error or a remote process exiting prematurely.

-
ncclInProgress
[](https://docs.nvidia.com#c.ncclResult_t.ncclInProgress) (

`7`

) A NCCL operation on the communicator is being enqueued and is being progressed in the background.

Whenever a function returns an error (neither ncclSuccess nor ncclInProgress), NCCL should print a more detailed message when the environment variable

[NCCL_DEBUG](https://docs.nvidia.com/env.html#nccl-debug)is set to “WARN”.-
ncclSuccess

## ncclDataType_t[](https://docs.nvidia.com#nccldatatype-t)

-
type ncclDataType_t
[](https://docs.nvidia.com#c.ncclDataType_t) NCCL defines the following integral and floating data-types.

-
ncclInt8
[](https://docs.nvidia.com#c.ncclDataType_t.ncclInt8) Signed 8-bits integer


-
ncclChar
[](https://docs.nvidia.com#c.ncclDataType_t.ncclChar) Signed 8-bits integer


-
ncclUint8
[](https://docs.nvidia.com#c.ncclDataType_t.ncclUint8) Unsigned 8-bits integer


-
ncclInt32
[](https://docs.nvidia.com#c.ncclDataType_t.ncclInt32) Signed 32-bits integer


-
ncclInt
[](https://docs.nvidia.com#c.ncclDataType_t.ncclInt) Signed 32-bits integer


-
ncclUint32
[](https://docs.nvidia.com#c.ncclDataType_t.ncclUint32) Unsigned 32-bits integer


-
ncclInt64
[](https://docs.nvidia.com#c.ncclDataType_t.ncclInt64) Signed 64-bits integer


-
ncclUint64
[](https://docs.nvidia.com#c.ncclDataType_t.ncclUint64) Unsigned 64-bits integer


-
ncclFloat16
[](https://docs.nvidia.com#c.ncclDataType_t.ncclFloat16) 16-bits floating point number (half precision)


-
ncclHalf
[](https://docs.nvidia.com#c.ncclDataType_t.ncclHalf) 16-bits floating point number (half precision)


-
ncclFloat32
[](https://docs.nvidia.com#c.ncclDataType_t.ncclFloat32) 32-bits floating point number (single precision)


-
ncclFloat
[](https://docs.nvidia.com#c.ncclDataType_t.ncclFloat) 32-bits floating point number (single precision)


-
ncclFloat64
[](https://docs.nvidia.com#c.ncclDataType_t.ncclFloat64) 64-bits floating point number (double precision)


-
ncclDouble
[](https://docs.nvidia.com#c.ncclDataType_t.ncclDouble) 64-bits floating point number (double precision)


-
ncclBfloat16
[](https://docs.nvidia.com#c.ncclDataType_t.ncclBfloat16) 16-bits floating point number (truncated precision in bfloat16 format, CUDA 11 or later)


-
ncclFloat8e4m3
[](https://docs.nvidia.com#c.ncclDataType_t.ncclFloat8e4m3) 8-bits floating point number, 4 exponent bits, 3 mantissa bits (CUDA >= 11.8 and SM >= 90)


-
ncclFloat8e5m2
[](https://docs.nvidia.com#c.ncclDataType_t.ncclFloat8e5m2) 8-bits floating point number, 5 exponent bits, 2 mantissa bits (CUDA >= 11.8 and SM >= 90)


-
ncclInt8

## ncclRedOp_t[](https://docs.nvidia.com#ncclredop-t)

## ncclScalarResidence_t[](https://docs.nvidia.com#ncclscalarresidence-t)

-
type ncclScalarResidence_t
[](https://docs.nvidia.com#c.ncclScalarResidence_t) Indicates where (memory space) scalar arguments reside and when they can be dereferenced.

-
ncclScalarHostImmediate
[](https://docs.nvidia.com#c.ncclScalarResidence_t.ncclScalarHostImmediate) The scalar resides in host memory and should be dereferenced in the most immediate way.


-
ncclScalarDevice
[](https://docs.nvidia.com#c.ncclScalarResidence_t.ncclScalarDevice) The scalar resides on device visible memory and should be dereferenced once needed.


-
ncclScalarHostImmediate

## ncclConfig_t[](https://docs.nvidia.com#ncclconfig-t)

-
type ncclHostCftMode_t
[](https://docs.nvidia.com#c.ncclHostCftMode_t) Values for the

`hostCftMode`

communicator configuration.-
ncclHostCftDefault
[](https://docs.nvidia.com#c.ncclHostCftMode_t.ncclHostCftDefault) Use the version-specific default.


-
ncclHostCftEnable
[](https://docs.nvidia.com#c.ncclHostCftMode_t.ncclHostCftEnable) Enable host-side CFT support.


-
ncclHostCftDisable
[](https://docs.nvidia.com#c.ncclHostCftMode_t.ncclHostCftDisable) Disable host-side CFT support.


-
ncclHostCftFallback
[](https://docs.nvidia.com#c.ncclHostCftMode_t.ncclHostCftFallback) Try to create CFT logical endpoints. In case of an error, host-side CFT will be disabled.


-
ncclHostCftDefault

-
type ncclConfig_t
[](https://docs.nvidia.com#c.ncclConfig_t) A structure-based configuration users can set to initialize a communicator; a newly created configuration must be initialized by NCCL_CONFIG_INITIALIZER.

-
NCCL_CONFIG_INITIALIZER
[](https://docs.nvidia.com#c.ncclConfig_t.NCCL_CONFIG_INITIALIZER) A configuration macro initializer which must be assigned to a newly created configuration.


-
blocking
[](https://docs.nvidia.com#c.ncclConfig_t.blocking) This attribute can be set as integer 0 or 1 to indicate nonblocking or blocking communicator behavior correspondingly. Blocking is the default behavior.


-
cgaClusterSize
[](https://docs.nvidia.com#c.ncclConfig_t.cgaClusterSize) Set Cooperative Group Array (CGA) size of kernels launched by NCCL. This attribute can be set between 0 and 8, and the default value is 4 since sm90 architecture and 0 for older architectures.


-
minCTAs
[](https://docs.nvidia.com#c.ncclConfig_t.minCTAs) Set the minimal number of CTAs NCCL should use for each kernel. Set to a positive integer value, up to 32. The default value is 1.


-
maxCTAs
[](https://docs.nvidia.com#c.ncclConfig_t.maxCTAs) Set the maximal number of CTAs NCCL should use for each kernel. Set to a positive integer value, up to 32. The default value is 32.


-
netName
[](https://docs.nvidia.com#c.ncclConfig_t.netName) Specify the network module name NCCL should use for network communication. The value of netName must match exactly the name of the network module (case-insensitive). NCCL internal network module names are “IB” (generic IB verbs) and “Socket” (TCP/IP sockets). External network plugins define their own names. The default value is undefined, and NCCL will choose the network module automatically.


Specify whether to share resources with child communicator during communicator split. Set the value of splitShare to 0 or 1. The default value is 0. When the parent communicator is created with splitShare=1 during ncclCommInitRankConfig, the child communicator can share internal resources of the parent during communicator split. Split communicators are in the same family. When resources are shared, aborting any communicator can result in other communicators in the same family becoming unusable. Irrespective of whether sharing resources or not, users should always abort/destroy all no longer needed communicators to free up resources. Note: when the parent communicator has been revoked, resource sharing during split is disabled regardless of this flag.


Specify whether to share resources with child communicator during communicator shrink. Set the value of shrinkShare to 0 or 1. The default value is 0. Note: when shrink is used with NCCL_SHRINK_ABORT, the value of shrinkShare is ignored and no resources are shared. When the parent communicator has been revoked, resource sharing is also disabled. The behavior of this flag is similar to splitShare, see above.


-
trafficClass
[](https://docs.nvidia.com#c.ncclConfig_t.trafficClass) Set the traffic class (TC) to use for network operations on the communicator. The meaning of TC is specific to the network plugin in use by the communicator (e.g. IB networks use service level, RoCE networks use type of service). Assigning different TCs to each communicator can benefit workloads which overlap communication. TCs are defined by the system configuration and should be greater than or equal to 0. Note that environment variables, such as NCCL_IB_SL and NCCL_IB_TC, take precedence over user-specified TC values. To utilize user-defined TCs, ensure that these environment variables are unset.


-
collnetEnable
[](https://docs.nvidia.com#c.ncclConfig_t.collnetEnable) Set 1/0 to enable/disable IB SHARP on the communicator. The default value is 0 (disabled).


-
CTAPolicy
[](https://docs.nvidia.com#c.ncclConfig_t.CTAPolicy) Set the policy for the communicator. The full list of supported policies can be found in

[NCCL Communicator CTA Policy Flags](https://docs.nvidia.com/flags.html#cta-policy-flags). The default value is NCCL_CTA_POLICY_DEFAULT.

-
nvlsCTAs
[](https://docs.nvidia.com#c.ncclConfig_t.nvlsCTAs) Set the total number of CTAs NCCL should use for NVLS kernels. Set to a positive integer value. By default, NCCL will automatically determine the best number of CTAs based on the system configuration.


-
commName
[](https://docs.nvidia.com#c.ncclConfig_t.commName) Specify the user defined name for the communicator. The communicator name can be used by NCCL to enrich logging and profiling.


-
nChannelsPerNetPeer
[](https://docs.nvidia.com#c.ncclConfig_t.nChannelsPerNetPeer) Set the number of network channels to be used for pairwise communication. The value must be a positive integer and will be round up to the next power of 2. The default value is optimized for the AlltoAll communication pattern. Consider increasing the value to increase the bandwidth for send/recv communication.


-
graphUsageMode
[](https://docs.nvidia.com#c.ncclConfig_t.graphUsageMode) Set the graph usage mode for the communicator. It support three possible values: 0 (no graphs), 1 (one graph) and 2 (either multiple graphs or mix of graph and non-graph). The default value is 2. If

[NCCL_GRAPH_STREAM_ORDERING](https://docs.nvidia.com/env.html#nccl-graph-stream-ordering)ordisables capture-time stream ordering (`graphStreamOrdering`

`0`

),**graph mixing must be off**—use`graphUsageMode`

`0`

or`1`

only;`graphUsageMode=2`

must not be combined with ordering`0`

(see[NCCL_GRAPH_STREAM_ORDERING](https://docs.nvidia.com/env.html#nccl-graph-stream-ordering)).

-
graphStreamOrdering
[](https://docs.nvidia.com#c.ncclConfig_t.graphStreamOrdering) (since 2.30)

Per-communicator override of

[NCCL_GRAPH_STREAM_ORDERING](https://docs.nvidia.com/env.html#nccl-graph-stream-ordering).`1`

keeps NCCL’s default capture-time serialization of communication kernels.`0`

disables it for this communicator—kernels are placed on the capture stream and the application must guarantee correct ordering (see[NCCL_GRAPH_STREAM_ORDERING](https://docs.nvidia.com/env.html#nccl-graph-stream-ordering)).Defaults to

`NCCL_CONFIG_UNDEF_INT`

(inherits[NCCL_GRAPH_STREAM_ORDERING](https://docs.nvidia.com/env.html#nccl-graph-stream-ordering)).`0`

or`1`

overrides the env var for this communicator.`graphStreamOrdering=0`

requires`graphUsageMode`

`0`

or`1`

(mixing**off**). Combining it with`graphUsageMode=2`

is**not supported**; see[NCCL_GRAPH_STREAM_ORDERING](https://docs.nvidia.com/env.html#nccl-graph-stream-ordering).**Mixed values on one GPU:**A communicator set to`1`

still receives NCCL’s internal serialization for its own kernels, but NCCL does**not**insert cross-communicator ordering with a peer set to`0`

—its kernels may overlap in situations NCCL would have serialized. Use`0`

only when the application guarantees ordering of**all**NCCL communication kernels that may run concurrently on the GPU.

-
launchOrderImplicit
[](https://docs.nvidia.com#c.ncclConfig_t.launchOrderImplicit) (since 2.31)

Per-communicator request for

[NCCL_LAUNCH_ORDER_IMPLICIT](https://docs.nvidia.com/env.html#nccl-launch-order-implicit).`1`

enables implicit launch ordering for this communicator;`0`

disables it.`NCCL_CONFIG_UNDEF_INT`

is the default and has the same effective behavior as`0`

.Communicators with different effective values can coexist. Overlap safety is about communication operations that may run concurrently on the same GPU:

Operations on disabled/default communicators retain the existing multiple-communicator ordering guarantees.

Operations on enabled communicators may overlap with operations on other enabled communicators if the application follows the host-side ordering requirements described for

[NCCL_LAUNCH_ORDER_IMPLICIT](https://docs.nvidia.com/env.html#nccl-launch-order-implicit).Operations on enabled communicators must not overlap with operations on disabled/default communicators. The application must order or synchronize those operations so they do not overlap, or configure the communicators consistently.


NCCL logs an

`INFO`

message if a CUDA context has used both enabled and disabled/default effective values, but it still initializes the communicator.If

[NCCL_LAUNCH_ORDER_IMPLICIT](https://docs.nvidia.com/env.html#nccl-launch-order-implicit)is set in the environment, it overrides this field before initialization.

-
maxP2pPeers
[](https://docs.nvidia.com#c.ncclConfig_t.maxP2pPeers) Set the maximum number of peers any rank will concurrently communicate with using P2P communication. Setting this value will influence all send/recv and send/recv-based collectives (all-to-all, scatter, gather). Values less than one or greater than the number of ranks will default to the number of ranks in the communicator.


-
numRmaCtx
[](https://docs.nvidia.com#c.ncclConfig_t.numRmaCtx) (since 2.31)

Number of one-sided RMA communication contexts to provision on the communicator. The

`ctx`

argument of,`ncclPutSignal()`

, and`ncclSignal()`

must lie in`ncclWaitSignal()`

`[0, numRmaCtx)`

. The default value is 1.

-
numRmaSig
[](https://docs.nvidia.com#c.ncclConfig_t.numRmaSig) (since 2.31)

Set the number of one-sided RMA signal indexes available per context. The default value is

`1`

. Host one-sided RMA operations such as,`ncclPutSignal()`

, and`ncclSignal()`

use`ncclWaitSignal()`

`sigIdx`

values in the range`[0, numRmaSig)`

.

-
rmaEagerInit
[](https://docs.nvidia.com#c.ncclConfig_t.rmaEagerInit) (since 2.31)

Controls when the collective one-sided RMA signal setup is initialized. With

`0`

(default), it is initialized during the first window registration (), a collective point. Use`ncclCommWindowRegister()`

`1`

to initialize it at communicator-init time instead; this is required if a communicator issuesor`ncclSignal()`

without first registering a window, which otherwise returns`ncclWaitSignal()`

`ncclInvalidUsage`

.If

[NCCL_RMA_EAGER_INIT](https://docs.nvidia.com/env.html#nccl-rma-eager-init)is set in the environment, it overrides this field before initialization.

-
hostCftMode
[](https://docs.nvidia.com#c.ncclConfig_t.hostCftMode) (since 2.31)

Controls support for host-side Compute Fabric Transport (CFT) queries.

`ncclHostCftEnable`

creates the communicator’s unicast and multicast logical endpoints during the firstcall on a CFT-capable communicator.`ncclCommWindowRegister()`

`ncclHostCftDisable`

disables support, and`ncclHostCftFallback`

tries to create logical endpoints and disables host-side CFT in case of error.`ncclHostCftDefault`

selects the library-defined default behavior.

-
nvlsHostMode
[](https://docs.nvidia.com#c.ncclConfig_t.nvlsHostMode) (since 2.31)

Controls host-side use of NVLink SHARP (NVLS) for a single communicator. The value is a bitmask that can independently disable the NVLS collective transport and multimem use by NCCL’s internal symmetric kernels and Copy Engine (CE) collectives. Explicit Device API multimem requests remain available. Selectively disabling host NVLS components on small or infrequently used communicators can preserve limited hardware multicast resources for other communicators that can utilize them more effectively.

Supported values (

`ncclNvlsHostMode_t`

):`ncclNvlsHostModeDefault`

— Library-defined default. Currently equivalent to`ncclNvlsHostModeEnable`

.`ncclNvlsHostModeEnable`

— Enable all host NVLS components.`ncclNvlsHostModeDisableTransport`

— Disable the NVLS collective transport and its registered-buffer optimization. The NVLS, NVLS_TREE, and multi-RPN PAT algorithms will be disabled.`ncclNvlsHostModeDisableSymmetricMultimem`

— Disable multimem use by NCCL’s internal symmetric kernels and CE collectives. UC symmetric kernels and CE fallbacks remain available.`ncclNvlsHostModeDisable`

— Disable all present and future host NVLS components. This value sets all non-reserved bits for forward compatibility.

The component flags can be combined with the bitwise OR operator. These flags do not affect the communicator’s reported Device API multimem capability and do not prevent explicit Device API calls from allocating multimem resources.


-
NCCL_CONFIG_INITIALIZER

## ncclEncryptionConfig_t[](https://docs.nvidia.com#ncclencryptionconfig-t)

-
type ncclEncryptionConfig_t
[](https://docs.nvidia.com#c.ncclEncryptionConfig_t) A structure-based configuration used by

; a newly created configuration must be initialized by`ncclSetEncryption()`

`NCCL_ENCRYPTION_CONFIG_INITIALIZER`

.-
NCCL_ENCRYPTION_CONFIG_INITIALIZER
[](https://docs.nvidia.com#c.ncclEncryptionConfig_t.NCCL_ENCRYPTION_CONFIG_INITIALIZER) A configuration macro initializer which must be assigned to a newly created encryption configuration.


-
NCCL_ENCRYPTION_MODE_PSK
[](https://docs.nvidia.com#c.ncclEncryptionConfig_t.NCCL_ENCRYPTION_MODE_PSK) Request TLS encryption for NCCL-owned TCP sockets using a pre-shared key.


-
mode
[](https://docs.nvidia.com#c.ncclEncryptionConfig_t.mode) The encryption mode. Use

to request TLS encryption for NCCL-owned TCP sockets.`NCCL_ENCRYPTION_MODE_PSK`


-
psk
[](https://docs.nvidia.com#c.ncclEncryptionConfig_t.psk) Null-terminated pre-shared key string used when

`mode`

is. The key must contain at least 32 bytes.`NCCL_ENCRYPTION_MODE_PSK`


-
NCCL_ENCRYPTION_CONFIG_INITIALIZER

## ncclCollConfig_t[](https://docs.nvidia.com#ncclcollconfig-t)

-
type ncclCollConfig_t
[](https://docs.nvidia.com#c.ncclCollConfig_t) Per-collective configuration passed through an

`nccl*Config`

collective API. Everymust be initialized with`ncclCollConfig_t`

before any member is set. Passing`NCCL_COLLCONFIG_INITIALIZER`

`NULL`

to a config-taking collective is equivalent to calling the corresponding collective without a configuration.The application owns the configuration and any storage it references, and must keep them valid for the duration of each call that uses them. Set the same configuration on every rank unless a member is documented otherwise.

For options that also have environment-variable and communicator-level forms, NCCL applies values in the following order: environment variable, per-collective configuration, communicator configuration, and library default. Leave resource and CTA-policy members at

`NCCL_CONFIG_UNDEF_INT`

to fall through to the next source in this list.-
NCCL_COLLCONFIG_INITIALIZER
[](https://docs.nvidia.com#c.ncclCollConfig_t.NCCL_COLLCONFIG_INITIALIZER) (since 2.31)

Initializes a new

with default values.`ncclCollConfig_t`


-
[ncclConfigExt_t](https://docs.nvidia.com#c.ncclConfigExt_t)*ext[](https://docs.nvidia.com#c.ncclCollConfig_t.ext) (since 2.31)

Head of a linked list of vendor-specific

options, or`ncclConfigExt_t`

`NULL`

. The official NCCL library does not read this member; it exists for vendor libraries layered on top of NCCL to forward their own vendor-defined options through the same call.

-
int minCTAs
[](https://docs.nvidia.com#c.ncclCollConfig_t.minCTAs) (since 2.31)

Per-collective override of

`minCTAs`

in[ncclConfig_t](https://docs.nvidia.com#ncclconfig). Accepts the same value range as[NCCL_MIN_CTAS](https://docs.nvidia.com/env.html#nccl-min-ctas); an out-of-range value is ignored and NCCL falls through to the next priority source. If the resolved value exceeds the resolved`maxCTAs`

, NCCL resets`minCTAs`

to`1`

.

-
int maxCTAs
[](https://docs.nvidia.com#c.ncclCollConfig_t.maxCTAs) (since 2.31)

Per-collective override of

`maxCTAs`

in[ncclConfig_t](https://docs.nvidia.com#ncclconfig). Accepts the same value range as[NCCL_MAX_CTAS](https://docs.nvidia.com/env.html#nccl-max-ctas); an out-of-range value is ignored and NCCL falls through to the next priority source. The resolved value is further clamped to the communicator’s`maxCTAs`

and applies only to this collective, including when calls are grouped.

-
int nvlsCTAs
[](https://docs.nvidia.com#c.ncclCollConfig_t.nvlsCTAs) (since 2.31)

Per-collective override of

`nvlsCTAs`

in[ncclConfig_t](https://docs.nvidia.com#ncclconfig). This setting applies only to NVLS algorithms.

-
int cgaClusterSize
[](https://docs.nvidia.com#c.ncclCollConfig_t.cgaClusterSize) (since 2.31)

Per-collective override of

`cgaClusterSize`

in[ncclConfig_t](https://docs.nvidia.com#ncclconfig). Accepts the same value range as[NCCL_CGA_CLUSTER_SIZE](https://docs.nvidia.com/env.html#nccl-cga-cluster-size); an out-of-range value is ignored and NCCL falls through to the next priority source. All collectives in a group must use the same value; inconsistent values result in undefined behavior.

-
const char *algSelection
[](https://docs.nvidia.com#c.ncclCollConfig_t.algSelection) (since 2.31)

A case-insensitive expression that filters the algorithms and kernels NCCL may use for this call.

`NULL`

or an empty string requests automatic selection.Each name is matched as a prefix from the start of a known name. For example,

`ring`

selects`RING_LL`

,`RING_LL128`

, and`RING_SIMPLE`

, but does not select`SYMK_RailRing_LsaSTMC`

; similarly,`nvls`

selects both`NVLS_SIMPLE`

and`NVLSTREE_SIMPLE`

. The supported operators are`+`

(AND),`,`

(OR), and`^`

(NOT); parentheses are not supported. For example,`tree,ring`

permits either family,`ring + ^RING_LL128`

permits Ring except LL128, and`^symk`

excludes symmetric kernels.The selectable built-in names and the collectives for which they are valid are:

AllReduce:

`TREE_LL`

,`TREE_LL128`

,`TREE_SIMPLE`

,`RING_LL`

,`RING_LL128`

,`RING_SIMPLE`

,`COLLNET_DIRECT_SIMPLE`

,`COLLNET_CHAIN_SIMPLE`

,`NVLS_SIMPLE`

,`NVLSTREE_SIMPLE`

,`SYMK_AGxLL_R`

,`SYMK_AGxLLMC_R`

,`SYMK_RSxTmaLD_AGxTmaST`

,`SYMK_RSxLD_AGxST`

, and`SYMK_RSxLDMC_AGxSTMC`

.AllGather:

`RING_LL`

,`RING_LL128`

,`RING_SIMPLE`

,`COLLNET_DIRECT_SIMPLE`

,`NVLS_SIMPLE`

,`PAT_SIMPLE`

,`SYMK_LL`

,`SYMK_LLMC`

,`SYMK_TmaST`

,`SYMK_ST`

,`SYMK_TmaSTMC`

,`SYMK_STMC`

, and`SYMK_RailRing_LsaSTMC`

.ReduceScatter:

`RING_LL`

,`RING_LL128`

,`RING_SIMPLE`

,`COLLNET_DIRECT_SIMPLE`

,`NVLS_SIMPLE`

,`PAT_SIMPLE`

,`SYMK_LL`

,`SYMK_TmaLD`

,`SYMK_LD`

,`SYMK_LDMC`

,`SYMK_RailA2A_LsaLD`

, and`SYMK_RailA2A_LsaLDMC`

.Broadcast and Reduce:

`RING_LL`

,`RING_LL128`

, and`RING_SIMPLE`

.

The

`SYMK_*`

names refer to symmetric-memory kernels built on the NCCL Device API.`LL`

is a low-latency protocol that tags data with an inline flag instead of a separate synchronization step;`LD`

/`ST`

are ordinary load/store data movement and`TmaLD`

/`TmaST`

use the Tensor Memory Accelerator for bulk asynchronous copies; the`MC`

suffix (as in`LLMC`

,`LDMC`

,`STMC`

) means the load, store, or reduction is done through NVLink SHARP multimem (multicast) instead of per-peer accesses; and`Rail`

/`Lsa`

names are multi-node kernels that combine a local NVLink-domain (`Lsa`

) step with a network exchange between same-rail ranks across nodes.Algorithm names are implementation details and may evolve. AllToAll, Gather, and Scatter lower to point-to-point sends and receives and expose no selectable names; Copy Engine paths are likewise not selectable here. Request a Copy Engine path with

`CTAPolicy`

instead.

-
int forceAlgSelection
[](https://docs.nvidia.com#c.ncclCollConfig_t.forceAlgSelection) (since 2.31)

Controls what happens when

`algSelection`

is invalid or cannot be honored. With the default value,`1`

, NCCL returns an error. Set it to`0`

to fall back to automatic selection instead.

-
int CTAPolicy
[](https://docs.nvidia.com#c.ncclCollConfig_t.CTAPolicy) (since 2.31)

Per-collective override of the communicator’s CTA policy. A set value replaces the communicator value; see

[NCCL Communicator CTA Policy Flags](https://docs.nvidia.com/flags.html#cta-policy-flags). If both`NCCL_CTA_POLICY_ZERO`

and`NCCL_CTA_POLICY_EFFICIENCY`

are set, Zero-CTA takes precedence. Copy Engine paths are selected through this policy, not`algSelection`

.

-
uint64_t userProfilerTag
[](https://docs.nvidia.com#c.ncclCollConfig_t.userProfilerTag) (since 2.31)

An opaque value delivered with the call’s events to profiler plugins that support profiler interface v7. Zero denotes an untagged call; older profiler interfaces ignore the tag.

The tag does not affect execution. NCCL reserves values with the most-significant bit set for possible future use; applications should use values with that bit clear.


-
cudaEvent_t launchCompletionEvent
[](https://docs.nvidia.com#c.ncclCollConfig_t.launchCompletionEvent) (since 2.32)

A caller-owned CUDA event that NCCL records at the collective kernel-launch completion boundary. Create the event with

[cudaEventCreateWithFlags and cudaEventDisableTiming](https://docs.nvidia.com/cuda/cuda-runtime-api/group__CUDART__EVENT.html). It must not be an interprocess or interop event.A NULL event requests no update. Event presence must match across ranks: every rank in the corresponding collective must provide a rank-local non-NULL event, or every rank must provide NULL. A group supports at most one non-NULL event per communicator.

Keep the event alive through all queued waits and graph executions that use it. For a grouped collective, enqueue a dependent

`cudaStreamWaitEvent`

only after`ncclGroupEnd`

returns`ncclSuccess`

. With a nonblocking communicator, first poll`ncclCommGetAsyncError`

until it returns`ncclSuccess`

; do not enqueue the wait after an error.NCCL records the event only for kernel launches; Copy Engine and RMA work do not record it.

CUDA 12.3 or newer provides launch-completion semantics. On older CUDA platforms, NCCL emits a warning and records the event before the kernel launch; this fallback does not provide a launch-completion guarantee. CUDA launch completion is best effort and does not guarantee that dependent work overlaps the collective. Graph capture is supported with a capture-compatible event; sharing a recorded event across graphs is not supported.


-
NCCL_COLLCONFIG_INITIALIZER

-
type ncclConfigExt_t
[](https://docs.nvidia.com#c.ncclConfigExt_t) A vendor-specific key-value option that can be linked through its

`next`

member and attached to. Each option has a key consisting of`ncclCollConfig_t.ext`

`key.vendorId`

and`key.optionId`

and one value in the`val.i`

,`val.s`

, or`val.raw`

union member. The list is unordered and must not contain duplicate keys.Vendors should choose a non-zero

`vendorId`

under`2^24`

that is unlikely to collide with other vendor libraries, for example by picking a random number;`optionId`

then distinguishes options within that vendor’s own namespace.

## ncclSimInfo_t[](https://docs.nvidia.com#ncclsiminfo-t)

-
type ncclSimInfo_t
[](https://docs.nvidia.com#c.ncclSimInfo_t) This struct will be used by ncclGroupSimulateEnd() to return information about the calls.

-
NCCL_SIM_INFO_INITIALIZER
[](https://docs.nvidia.com#c.ncclSimInfo_t.NCCL_SIM_INFO_INITIALIZER)

NCCL_SIM_INFO_INITIALIZER is a configuration macro initializer which must be assigned to a newly created ncclSimInfo_t struct.

-
estimatedTime
[](https://docs.nvidia.com#c.ncclSimInfo_t.estimatedTime)

Estimated time for the operation(s) in the group call will be returned in this attribute.

-
NCCL_SIM_INFO_INITIALIZER

## ncclCommMemStat_t[](https://docs.nvidia.com#ncclcommmemstat-t)

-
type ncclCommMemStat_t
[](https://docs.nvidia.com#c.ncclCommMemStat_t) Memory statistic selectors for

.`ncclCommMemStats()`

-
ncclStatGpuMemSuspend
[](https://docs.nvidia.com#c.ncclCommMemStat_t.ncclStatGpuMemSuspend) Communicator allocated GPU memory that can be released via suspend (bytes).


-
ncclStatGpuMemSuspended
[](https://docs.nvidia.com#c.ncclCommMemStat_t.ncclStatGpuMemSuspended) Whether communicator allocated GPU memory is currently suspended (

`0`

= active,`1`

= suspended).

-
ncclStatGpuMemPersist
[](https://docs.nvidia.com#c.ncclCommMemStat_t.ncclStatGpuMemPersist) Communicator allocated GPU memory that cannot be suspended (bytes).


-
ncclStatGpuMemTotal
[](https://docs.nvidia.com#c.ncclCommMemStat_t.ncclStatGpuMemTotal) Total communicator allocated GPU memory that is tracked by NCCL (bytes).


-
ncclStatGpuMemSuspend

## ncclWindow_t[](https://docs.nvidia.com#ncclwindow-t)

-
type ncclWindow_t
[](https://docs.nvidia.com#c.ncclWindow_t) NCCL window object for window registration and deregistration.