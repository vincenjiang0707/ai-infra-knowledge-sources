source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/api/flags.html

# NCCL API Supported Flags[](https://docs.nvidia.com#nccl-api-supported-flags)

The following show all flags which are supported by NCCL APIs.

## Window Registration Flags[](https://docs.nvidia.com#window-registration-flags)

-
NCCL_WIN_DEFAULT
[](https://docs.nvidia.com#c.NCCL_WIN_DEFAULT) Register buffer into NCCL window with default behavior. The default behavior allows users to pass any offset to the buffer head address as the input of NCCL collective operations. However, this behavior can cause suboptimal performance in NCCL due to the asymmetric buffer usage.


-
NCCL_WIN_COLL_SYMMETRIC
[](https://docs.nvidia.com#c.NCCL_WIN_COLL_SYMMETRIC) Register buffer into NCCL window, and users need to guarantee the offset to the buffer head address from all ranks must be equal when calling NCCL collective operations. It allows NCCL to operate buffer in a symmetric way and provide the best performance.


-
NCCL_WIN_STRICT_ORDERING
[](https://docs.nvidia.com#c.NCCL_WIN_STRICT_ORDERING) Register buffer into NCCL window while ensuring strict ordering for window operations using the IB Verbs transport. This flag is mostly intended for buffers used for GIN VA Signals (see

[Signals and Counters](https://docs.nvidia.com/device_gin.html#devapi-signals)).

## NCCL Communicator CTA Policy Flags[](https://docs.nvidia.com#nccl-communicator-cta-policy-flags)

-
NCCL_CTA_POLICY_DEFAULT
[](https://docs.nvidia.com#c.NCCL_CTA_POLICY_DEFAULT) Use the default CTA policy for NCCL communicator. In this policy, NCCL will automatically adjust resource usage and achieve maximal performance. This policy is suitable for most applications.


-
NCCL_CTA_POLICY_EFFICIENCY
[](https://docs.nvidia.com#c.NCCL_CTA_POLICY_EFFICIENCY) Use the CTA efficiency policy for NCCL communicator. In this policy, NCCL will optimize CTA usage and use minimal number of CTAs to achieve the decent performance when possible. This policy is suitable for applications which require better compute and communication overlap.


-
NCCL_CTA_POLICY_ZERO
[](https://docs.nvidia.com#c.NCCL_CTA_POLICY_ZERO) Use the Zero-CTA policy for NCCL communicator. In this policy, NCCL will use zero CTA whenever it can, even when that choice may sacrifice some performance. Select this mode when your application must preserve the maximum number of CTAs for compute kernels.


## Communicator Shrink Flags[](https://docs.nvidia.com#communicator-shrink-flags)

These flags modify the behavior of the `ncclCommShrink`

operation.

-
NCCL_SHRINK_DEFAULT
[](https://docs.nvidia.com#c.NCCL_SHRINK_DEFAULT) Default behavior. Shrink the parent communicator without affecting ongoing operations. Value:

`0x00`

.

-
NCCL_SHRINK_ABORT
[](https://docs.nvidia.com#c.NCCL_SHRINK_ABORT) First, terminate ongoing parent communicator operations, and then proceed with shrinking the communicator. This is used for error recovery scenarios where the parent communicator might be in a hung state. Resources of parent comm are still not freed, users should decide whether to call ncclCommAbort on the parent communicator after shrink. Value:

`0x01`

.

## GIN Optimization Flags[](https://docs.nvidia.com#gin-optimization-flags)

These flags modify the behavior of GIN Device API operations (see [Device API – GIN](https://docs.nvidia.com/device_gin.html#device-api-gin)).
Flags may be combined with a bitwise OR.

-
enumerator ncclGinOptFlagsDefault
[](https://docs.nvidia.com#_CPPv422ncclGinOptFlagsDefault) Default behavior; no optional flags are given to the backend.


-
enumerator ncclGinOptFlagsAggregateRequests
[](https://docs.nvidia.com#_CPPv432ncclGinOptFlagsAggregateRequests) A user can specify this flag if more requests are expected in the near future. Implementations can reduce overhead by delaying some logic until after the batch is complete. For example, if a user posts N requests, this flag can be used for (N - 1) requests. However, the Nth request must not use this flag to ensure correctness.