source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/communicator/class.html

# Communicator Class[](https://docs.nvidia.com#communicator-class)

-
*class*nccl.core.Communicator(*ptr: int | None = None*)[](https://docs.nvidia.com#nccl.core.Communicator) Bases:

`object`

NCCL communicator for collective and point-to-point operations.

A communicator represents a group of participants that perform NCCL operations. Each participant is assigned an integer rank in

`[0, nranks)`

.Most users should create communicators with

or`init()`

. The constructor is a low-level interoperability entry point for wrapping an existing NCCL communicator pointer or creating a null communicator for later initialization.`init_all()`

A communicator instance provides collective and point-to-point operations, lifecycle and resource management, and properties describing its rank, device, topology, and capabilities.

-
__init__(
*ptr: int | None = None*) None[](https://docs.nvidia.com#nccl.core.Communicator.__init__) Wraps an existing NCCL communicator pointer.

This is a low-level interoperability entry point for an NCCL communicator pointer obtained from another library or framework. Most users should create communicators with

or`init()`

instead.`init_all()`

Omitting

`ptr`

or passing 0 creates a null communicator. A null communicator can later be initialized with, or used with`initialize()`

to join an existing communicator.`grow()`

- Parameters:
**ptr**– Address of an existing NCCL communicator, represented as a Python integer.`None`

and 0 create a null communicator. Defaults to`None`

.


-
__init__(

## Properties[](https://docs.nvidia.com#properties)

[ Communicator.properties](https://docs.nvidia.com#nccl.core.Communicator.properties) returns an

[holding the properties NCCL reports for the communicator, including fields that have no dedicated accessor. The groups below provide per-field accessors for the values needed most often.](https://docs.nvidia.com#nccl.core.NCCLCommProperties)

`NCCLCommProperties`

-
Communicator.properties
[](https://docs.nvidia.com#nccl.core.Communicator.properties) All properties NCCL reports for this communicator.

Use this to read several properties at once, or to reach the fields that have no dedicated accessor.

- Returns:
An

holding every field NCCL reports for this communicator.`NCCLCommProperties`

- Raises:
– If the communicator is not initialized.**NcclInvalid**


### Identity[](https://docs.nvidia.com#identity)

-
Communicator.ptr
[](https://docs.nvidia.com#nccl.core.Communicator.ptr) Integer value of the underlying

(0 if destroyed or null).`ncclComm_t`


-
Communicator.is_valid
[](https://docs.nvidia.com#nccl.core.Communicator.is_valid) Whether the communicator is valid (not destroyed or null).


-
Communicator.nranks
[](https://docs.nvidia.com#nccl.core.Communicator.nranks) Total number of ranks in the communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.device
[](https://docs.nvidia.com#nccl.core.Communicator.device) CUDA device associated with this communicator.

Returns a

providing additional functionality such as`cuda.core.Device`

`to_system_device`

for obtaining the NVML device, device properties, and synchronization.- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.rank
[](https://docs.nvidia.com#nccl.core.Communicator.rank) This caller’s rank within the communicator (0 to nranks - 1).

- Raises:
– If the communicator is not initialized.**NcclInvalid**


### Device-API capability[](https://docs.nvidia.com#device-api-capability)

These properties reflect the underlying NCCL [ ncclCommProperties_t](https://docs.nvidia.com/api/device_setup.html#c.ncclCommProperties_t)
structure.

-
Communicator.cuda_dev
[](https://docs.nvidia.com#nccl.core.Communicator.cuda_dev) CUDA device ID associated with this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.nvml_dev
[](https://docs.nvidia.com#nccl.core.Communicator.nvml_dev) NVML device ID for the GPU associated with this communicator.

Uses the NVML indexing space, which may differ from CUDA indexing.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.device_api_support
[](https://docs.nvidia.com#nccl.core.Communicator.device_api_support) Whether device-side NCCL operations are supported on this platform.

If False, a device communicator cannot be created.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.multimem_support
[](https://docs.nvidia.com#nccl.core.Communicator.multimem_support) Whether ranks in the same LSA team can communicate using multimem.

If False, a device communicator cannot be created with multimem resources.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.gin_type
[](https://docs.nvidia.com#nccl.core.Communicator.gin_type) GPU-Initiated Networking (GIN) type reaching every rank.

If equal to

, a device communicator cannot be created with GIN connection type`NcclGinType.NONE`

. A rail-restricted transport may still be available; see`NcclGinConnectionType.FULL`

.`railed_gin_type`

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.n_lsa_teams
[](https://docs.nvidia.com#nccl.core.Communicator.n_lsa_teams) Number of Load/Store Accessible (LSA) teams for this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.host_rma_support
[](https://docs.nvidia.com#nccl.core.Communicator.host_rma_support) Whether host RMA is supported on this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.railed_gin_type
[](https://docs.nvidia.com#nccl.core.Communicator.railed_gin_type) Railed GIN type supported by this communicator.

If equal to

, a device communicator cannot be created with GIN connection type`NcclGinType.NONE`

.`NcclGinConnectionType.RAIL`

- Raises:
– If the communicator is not initialized.**NcclInvalid**


### NCCLCommProperties[](https://docs.nvidia.com#ncclcommproperties)

Covers the accessors in both groups above, plus the fields that have none.

-
*class*nccl.core.NCCLCommProperties(***,*rank: int*,*n_ranks: int*,*cuda_dev: int*,*nvml_dev: int*,*device_api_support: bool*,*multimem_support: bool*,*gin_type:*,[NcclGinType](https://docs.nvidia.com/device_setup.html#nccl.core.NcclGinType)*n_lsa_teams: int*,*host_rma_support: bool*,*railed_gin_type:*,[NcclGinType](https://docs.nvidia.com/device_setup.html#nccl.core.NcclGinType)*comm_hash: int | None = None*,*gin_min_stride: int | None = None*,*gin_connection_type:*,[NcclGinConnectionType](https://docs.nvidia.com/device_setup.html#nccl.core.NcclGinConnectionType)| None = None*available_gin_types: frozenset[*,[NcclGinType](https://docs.nvidia.com/device_setup.html#nccl.core.NcclGinType)] | None = None*dev_comm_runtime_version_size: int | None = None*,*cft_support: bool | None = None*,*cft_multicast_support: bool | None = None*,*cft_counted_support: bool | None = None*)[](https://docs.nvidia.com#nccl.core.NCCLCommProperties) Bases:

`object`

The properties NCCL reports for a communicator.

Returned by

. These values are fixed for the lifetime of the communicator. Version-marked fields are`Communicator.properties`

`None`

when nccl4py was built against an older NCCL.See also

`ncclCommProperties`

for the description of each field.-
rank
*: int*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.rank) This caller’s rank within the communicator.


-
n_ranks
*: int*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.n_ranks) Number of ranks in the communicator.


-
cuda_dev
*: int*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.cuda_dev) CUDA device ID associated with the communicator.


-
nvml_dev
*: int*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.nvml_dev) NVML device ID for the GPU. Uses the NVML indexing space, which may differ from CUDA indexing.


-
device_api_support
*: bool*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.device_api_support) Whether device-side NCCL operations are supported.


-
multimem_support
*: bool*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.multimem_support) Whether ranks in the same LSA team can communicate using multimem.


-
gin_type
*:*[NcclGinType](https://docs.nvidia.com/device_setup.html#nccl.core.NcclGinType)[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.gin_type) GIN transport reaching every rank.

`NONE`

unlessis`gin_connection_type`

`FULL`

, even when a rail-restricted transport is available.

-
n_lsa_teams
*: int*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.n_lsa_teams) Number of LSA teams.


-
host_rma_support
*: bool*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.host_rma_support) Whether host RMA is supported.


-
railed_gin_type
*:*[NcclGinType](https://docs.nvidia.com/device_setup.html#nccl.core.NcclGinType)[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.railed_gin_type) GIN transport reaching ranks within a rail.

`NONE`

only when no GIN transport is available at all.

-
comm_hash
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.comm_hash) Hash identifying the communicator, shared by all its ranks (NCCL 2.31+).


-
gin_min_stride
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.gin_min_stride) Granularity of the GIN rank stride this communicator supports. A stride passed as

must be a multiple of this value, and no larger than the rail team’s stride. It is 1 when`NCCLDevCommRequirements.gin_custom_stride`

is`gin_connection_type`

`FULL`

(NCCL 2.31+).

-
gin_connection_type
*:*[NcclGinConnectionType](https://docs.nvidia.com/device_setup.html#nccl.core.NcclGinConnectionType)| None*= None*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.gin_connection_type) `NONE`

,`RAIL`

or`FULL`

. A device communicator may request this topology or a narrower one via(NCCL 2.31+).`NCCLDevCommRequirements.gin_connection_type`

- Type:
Widest GIN connection topology this communicator supports



-
available_gin_types
*: frozenset[*[NcclGinType](https://docs.nvidia.com/device_setup.html#nccl.core.NcclGinType)] | None*= None*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.available_gin_types) The GIN transports this communicator can use, e.g.

`NcclGinType.GDAKI in props.available_gin_types`

. Empty when GIN is unavailable (NCCL 2.31+).

-
dev_comm_runtime_version_size
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.dev_comm_runtime_version_size) Size, in bytes, of the device communicator structure in the running NCCL library (NCCL 2.31+).


-
cft_support
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.cft_support) Whether every rank in the communicator supports CFT unicast logical endpoints, which requires CUDA and driver 13.3+ on each. NCCL reduces this across ranks, so

`False`

does not mean the local GPU lacks support (NCCL 2.32+).

-
cft_multicast_support
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.cft_multicast_support) Whether every rank in the communicator supports multicast CFT logical endpoints. Independent of

; a GPU may support multicast endpoints without unicast ones (NCCL 2.32+).`cft_support`


-
cft_counted_support
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCommProperties.cft_counted_support) Whether every rank in the communicator supports counted CFT logical-endpoint operations (NCCL 2.32+).


-
rank

## Teams[](https://docs.nvidia.com#teams)

A [ NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam) names a strided subset of the communicator’s ranks.
The members below return the predefined teams; pass one to

[or to the rank converters. See](https://docs.nvidia.com/configuration.html#nccl.core.TeamRequirement)

`TeamRequirement`

[Teams](https://docs.nvidia.com/usage/deviceapi.html#devapi-teams)for team semantics.

-
Communicator.team_world
[](https://docs.nvidia.com#nccl.core.Communicator.team_world) The world team for this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.team_lsa
[](https://docs.nvidia.com#nccl.core.Communicator.team_lsa) The LSA team for this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.team_rail
[](https://docs.nvidia.com#nccl.core.Communicator.team_rail) The rail team for this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.team_cft_multimem
[](https://docs.nvidia.com#nccl.core.Communicator.team_cft_multimem) The CFT multimem team for this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**

See also


-
Communicator.team_cft(
*mode:*)[NcclCftTeamMode](https://docs.nvidia.com#nccl.core.NcclCftTeamMode)= NcclCftTeamMode.FLAT[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam)[](https://docs.nvidia.com#nccl.core.Communicator.team_cft) The CFT team for this communicator, in the requested layout.

- Parameters:
**mode**– Team layout. Defaults to, matching the C default.`NcclCftTeamMode.FLAT`

- Raises:
– If the communicator is not initialized.**NcclInvalid**

See also


-
Communicator.team_rank_to_world(
*team:*,[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam)*team_rank: int*) int[](https://docs.nvidia.com#nccl.core.Communicator.team_rank_to_world) Maps a rank within

`team`

to its rank in this communicator.`team`

is anchored at this rank, so`team.rank`

maps back toand neighbours are offset by`rank`

`team.stride`

.- Parameters:
**team**– The team`team_rank`

is expressed in, as returned by,`team_world`

, or`team_lsa`

.`team_rail`

**team_rank**– Rank within`team`

.

- Returns:
The corresponding rank in this communicator.

- Raises:
– If the communicator is not initialized.**NcclInvalid**


-
Communicator.team_rank_to_lsa(
*team:*,[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam)*team_rank: int*) int[](https://docs.nvidia.com#nccl.core.Communicator.team_rank_to_lsa) Maps a rank within

`team`

to its rank in the LSA team.The LSA-relative counterpart of

:`team_rank_to_world()`

`team.rank`

maps back to this rank’s index in. Only meaningful when`team_lsa`

`team_rank`

names a peer that shares this rank’s LSA team.- Parameters:
**team**– The team`team_rank`

is expressed in, as returned by,`team_world`

, or`team_lsa`

.`team_rail`

**team_rank**– Rank within`team`

.

- Returns:
The corresponding rank in the LSA team, or

`-1`

if the device resource state could not be initialized.- Raises:
– If the communicator is not initialized.**NcclInvalid**


### NcclCftTeamMode[](https://docs.nvidia.com#ncclcftteammode)

-
*class*nccl.core.NcclCftTeamMode(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclCftTeamMode) Bases:

`IntEnum`

CFT team layout, mirroring

.`ncclCftTeamMode_t`

Selects which ranks in the CFT unicast group the CFT team

includes.`Communicator.team_cft()`

-
FLAT
*= 0*[](https://docs.nvidia.com#nccl.core.NcclCftTeamMode.FLAT) Every rank in the CFT unicast group.


-
HIER_MULTIMEM
*= 1*[](https://docs.nvidia.com#nccl.core.NcclCftTeamMode.HIER_MULTIMEM) The ranks of the CFT unicast group sharing the same index across multicast CFT groups.


-
HIER_LSA
*= 2*[](https://docs.nvidia.com#nccl.core.NcclCftTeamMode.HIER_LSA) The ranks of the CFT unicast group sharing the same index across LSA groups.


-
FLAT