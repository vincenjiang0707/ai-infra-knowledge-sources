source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/communicator/device_setup.html

# Device Communicator Setup[](https://docs.nvidia.com#device-communicator-setup)

Host-side methods and resources for creating an NCCL device communicator.
The device-side communication primitives themselves are available only
from CUDA kernels and are documented under the C device API
([Device API](https://docs.nvidia.com/api/device.html)); this page covers what the Python (host) side
exposes for bootstrapping them. The configuration object passed to
[ Communicator.create_dev_comm()](https://docs.nvidia.com#nccl.core.Communicator.create_dev_comm) is documented in

[Configuration](https://docs.nvidia.com/configuration.html).

## create_dev_comm[](https://docs.nvidia.com#create-dev-comm)

-
Communicator.create_dev_comm(
*requirements:*)[NCCLDevCommRequirements](https://docs.nvidia.com/configuration.html#nccl.core.NCCLDevCommRequirements)| None = None[DevCommResource](https://docs.nvidia.com/resources.html#nccl.core.DevCommResource)[](https://docs.nvidia.com#nccl.core.Communicator.create_dev_comm) Creates a device communicator for device-side NCCL operations.

This is a collective call: every rank in the communicator must participate. When called inside a group, the result may not be filled in until the group completes.

Device communicators enable direct GPU kernel access to NCCL communication primitives. Multiple device communicators can be created from one host communicator. The returned

is tracked by the communicator and may be released explicitly via its`DevCommResource`

method, or automatically when the communicator is destroyed or aborted. Access the device communicator pointer via`close()`

or`DevCommResource.ptr`

`resource.dev_comm.ptr`

.- Parameters:
**requirements**– Configuration for device communicator resource allocation. If`None`

, a defaultis used. Defaults to`NCCLDevCommRequirements`

`None`

.- Returns:
for the device communicator.`DevCommResource`

- Raises:
– If the communicator is not initialized.**NcclInvalid**

See also


## GIN type enums[](https://docs.nvidia.com#gin-type-enums)

GPU-Initiated Networking (GIN) enums describing what device-side network transport is available on a communicator and which connection topology the user requires.

### NcclGinType[](https://docs.nvidia.com#ncclgintype)

-
*class*nccl.core.NcclGinType(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclGinType) Bases:

`IntEnum`

GIN transport type, mirroring

.`ncclGinType_t`

Reported by

and`Communicator.gin_type`

to indicate which device-side network transport, if any, is available on the communicator, and accepted by`Communicator.railed_gin_type`

to request one.`NCCLDevCommRequirements.gin_type`

-
NONE
*= 0*[](https://docs.nvidia.com#nccl.core.NcclGinType.NONE) No GIN transport. When reported, none is available; when set on

it instead means any available transport is acceptable.`NCCLDevCommRequirements.gin_type`


-
PROXY
*= 2*[](https://docs.nvidia.com#nccl.core.NcclGinType.PROXY) Proxy-based GIN. Network operations issued from a device kernel are relayed through a CPU proxy thread.


-
GDAKI
*= 3*[](https://docs.nvidia.com#nccl.core.NcclGinType.GDAKI) GPUDirect Async Kernel-Initiated (GDA-KI). The kernel directly issues network operations to the NIC, bypassing the CPU proxy.


-
GPI
*= 4*[](https://docs.nvidia.com#nccl.core.NcclGinType.GPI) GPU-Push Interface. GPU threads push network descriptors directly to a NIC-visible MMIO queue, with no CPU involvement and no memory barriers.


-
EFA_GDA
*= 5*[](https://docs.nvidia.com#nccl.core.NcclGinType.EFA_GDA) EFA GPUDirect Async. Kernel-initiated network operations on AWS Elastic Fabric Adapter NICs.


-
NONE

### NcclGinConnectionType[](https://docs.nvidia.com#ncclginconnectiontype)

-
*class*nccl.core.NcclGinConnectionType(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclGinConnectionType) Bases:

`IntEnum`

GIN connection topology, mirroring

.`ncclGinConnectionType_t`

Set on the

`gin_connection_type`

field ofbefore calling`NCCLDevCommRequirements`

to declare which peers must be reachable via GIN from device code.`Communicator.create_dev_comm()`

-
NONE
*= 0*[](https://docs.nvidia.com#nccl.core.NcclGinConnectionType.NONE) No GIN connection requested.


-
FULL
*= 1*[](https://docs.nvidia.com#nccl.core.NcclGinConnectionType.FULL) Fully connected. Every rank in the communicator must be reachable from every other rank via GIN.


-
RAIL
*= 2*[](https://docs.nvidia.com#nccl.core.NcclGinConnectionType.RAIL) Rail-restricted. Ranks must be reachable via GIN only within the same rail (network plane).


-
CUSTOM_STRIDE
*= 3*[](https://docs.nvidia.com#nccl.core.NcclGinConnectionType.CUSTOM_STRIDE) Strided. Ranks must be reachable via GIN at the stride given by

.`NCCLDevCommRequirements.gin_custom_stride`


-
NONE