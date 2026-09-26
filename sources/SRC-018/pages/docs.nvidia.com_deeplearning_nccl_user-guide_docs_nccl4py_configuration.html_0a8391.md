source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/nccl4py/configuration.html

# Configuration[](https://docs.nvidia.com#configuration)

Configuration objects passed to communicator creation methods and to individual collectives, plus the flag enums they consume.

## NCCLConfig[](https://docs.nvidia.com#ncclconfig)

Used by [ Communicator.init()](https://docs.nvidia.com/communicator/lifecycle.html#nccl.core.Communicator.init),

[,](https://docs.nvidia.com/communicator/lifecycle.html#nccl.core.Communicator.initialize)

`Communicator.initialize()`

[,](https://docs.nvidia.com/communicator/lifecycle.html#nccl.core.Communicator.split)

`Communicator.split()`

[, and](https://docs.nvidia.com/communicator/lifecycle.html#nccl.core.Communicator.shrink)

`Communicator.shrink()`

[. Fields left unset (](https://docs.nvidia.com/communicator/lifecycle.html#nccl.core.Communicator.grow)

`Communicator.grow()`

`None`

) remain at NCCL’s
internal default; values are validated by the C library when the config is
consumed.-
*class*nccl.core.NCCLConfig(***,*blocking: bool | None = None*,*cga_cluster_size: int | None = None*,*min_ctas: int | None = None*,*max_ctas: int | None = None*,*net_name: str | None = None*,*split_share: bool | None = None*,*traffic_class: int | None = None*,*comm_name: str | None = None*,*collnet_enable: bool | None = None*,*cta_policy:*,[CTAPolicy](https://docs.nvidia.com#nccl.core.CTAPolicy)| None = None*shrink_share: bool | None = None*,*nvls_ctas: int | None = None*,*n_channels_per_net_peer: int | None = None*,*nvlink_centric_sched: bool | None = None*,*graph_usage_mode: int | None = None*,*num_rma_ctx: int | None = None*,*max_p2p_peers: int | None = None*,*graph_stream_ordering: int | None = None*,*launch_order_implicit: bool | None = None*,*num_rma_sig: int | None = None*,*rma_eager_init: bool | None = None*,*host_cft_mode:*,[NcclHostCftMode](https://docs.nvidia.com#nccl.core.NcclHostCftMode)| None = None*nvls_host_mode:*)[NcclNvlsHostMode](https://docs.nvidia.com#nccl.core.NcclNvlsHostMode)| None = None[](https://docs.nvidia.com#nccl.core.NCCLConfig) Bases:

`LowppSpec`

NCCL configuration for communicator initialization.

Provides configuration options for NCCL communicators, allowing fine-tuning of performance and behavior characteristics. Fields not set in the constructor remain at NCCL’s internal default; values are validated by the C library when the config is consumed.

See also

for the description of each field.`ncclConfig_t`

-
blocking
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.blocking) Blocking (True) or non-blocking (False) communicator behavior. If unset, NCCL uses True.

Available since NCCL 2.14.0.


-
cga_cluster_size
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.cga_cluster_size) Cooperative Group Array (CGA) size for kernels (0-8). If unset, NCCL uses 4 for sm90+, 0 otherwise.

Available since NCCL 2.17.0.


-
min_ctas
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.min_ctas) Minimum number of CTAs per kernel; positive integer up to 32. If unset, NCCL uses 1.

Available since NCCL 2.17.0.


-
max_ctas
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.max_ctas) Maximum number of CTAs per kernel; positive integer up to 32. If unset, NCCL uses 32.

Available since NCCL 2.17.0.


-
net_name
*: str | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.net_name) Network module name (e.g. ‘IB’, ‘Socket’). Case-insensitive. If unset, NCCL auto-selects.

Available since NCCL 2.17.0.


Share resources with the child communicator during split. If unset, NCCL uses False.

Available since NCCL 2.18.0.


-
traffic_class
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.traffic_class) Traffic class (TC) for network operations (>= 0). Network-specific meaning.

Available since NCCL 2.26.0.


-
comm_name
*: str | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.comm_name) User-defined communicator name for logging and profiling.

Available since NCCL 2.27.0.


-
collnet_enable
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.collnet_enable) Enable (True) or disable (False) IB SHARP. If unset, NCCL uses False.

Available since NCCL 2.27.0.


-
cta_policy
*:*[CTAPolicy](https://docs.nvidia.com#nccl.core.CTAPolicy)| None*= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.cta_policy) CTA scheduling policy. If unset, NCCL uses CTAPolicy.DEFAULT.

Available since NCCL 2.27.0.


Share resources with the child communicator during shrink. If unset, NCCL uses False.

Available since NCCL 2.27.0.


-
nvls_ctas
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.nvls_ctas) Total number of CTAs for NVLS kernels (positive integer). If unset, NCCL auto-determines.

Available since NCCL 2.27.1.


-
n_channels_per_net_peer
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.n_channels_per_net_peer) Number of network channels for pairwise communication. Positive integer, rounded up to power of 2. If unset, NCCL uses an AlltoAll-optimized value.

Available since NCCL 2.28.0.


-
nvlink_centric_sched
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.nvlink_centric_sched) Enable NVLink-centric scheduling. If unset, NCCL uses False.

Available since NCCL 2.28.2.


-
graph_usage_mode
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.graph_usage_mode) Graph usage mode. Supported values are 0 (no graphs), 1 (one graph), and 2 (multiple graphs or a mix of graph and non-graph). If unset, NCCL uses 2.

Available since NCCL 2.29.0.


-
num_rma_ctx
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.num_rma_ctx) Number of RMA contexts. Positive integer. If unset, NCCL uses 1.

Available since NCCL 2.29.0.


-
max_p2p_peers
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.max_p2p_peers) Maximum number of peers any rank will concurrently communicate with using P2P. Positive integer. If unset, NCCL uses the communicator size.

Available since NCCL 2.30.0.


-
graph_stream_ordering
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.graph_stream_ordering) Whether NCCL preserves stream-ordering semantics for collectives captured into CUDA graphs. Supported values are 0 (disabled) or 1 (enabled). The value 0 cannot be combined with

`graph_usage_mode=2`

. Also controllable via the`NCCL_GRAPH_STREAM_ORDERING`

environment variable. If unset, NCCL uses 1.Available since NCCL 2.30.5.


-
launch_order_implicit
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.launch_order_implicit) Whether this communicator takes part in implicit launch ordering. Within one CUDA context, operations on communicators that enable it must not overlap with operations on communicators that do not. Also controllable via the

`NCCL_LAUNCH_ORDER_IMPLICIT`

environment variable, which takes precedence. If unset, NCCL uses False.Available since NCCL 2.31.0.


-
num_rma_sig
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.num_rma_sig) Number of one-sided RMA signal indexes available per context. Non-negative integer; bounds the

`signal_index`

accepted by the signal and wait-signal operations. If unset, NCCL uses 1.Available since NCCL 2.31.0.


-
rma_eager_init
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.rma_eager_init) Whether the collective one-sided RMA signal setup is initialized at communicator creation rather than at the first window registration. True is required if the communicator issues signal or wait-signal operations without first registering a symmetric window. Also controllable via the

`NCCL_RMA_EAGER_INIT`

environment variable, which takes precedence. If unset, NCCL uses False.Available since NCCL 2.31.0.


-
host_cft_mode
*:*[NcclHostCftMode](https://docs.nvidia.com#nccl.core.NcclHostCftMode)| None*= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.host_cft_mode) Host-side Compute Fabric Transport mode. Controls whether the communicator creates the CUDA fabric logical endpoints backing the host-side CFT queries. If unset, NCCL uses

.`NcclHostCftMode.DEFAULT`

Available since NCCL 2.31.1.


-
nvls_host_mode
*:*[NcclNvlsHostMode](https://docs.nvidia.com#nccl.core.NcclNvlsHostMode)| None*= None*[](https://docs.nvidia.com#nccl.core.NCCLConfig.nvls_host_mode) Host-side NVLS mode. Selects which host NVLS components the communicator uses. If unset, NCCL uses its library-defined default, which is currently equivalent to

.`NcclNvlsHostMode.ENABLE`

Available since NCCL 2.32.0.


-
blocking

### NcclHostCftMode[](https://docs.nvidia.com#ncclhostcftmode)

Value of [ NCCLConfig.host_cft_mode](https://docs.nvidia.com#nccl.core.NCCLConfig.host_cft_mode).

-
*class*nccl.core.NcclHostCftMode(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclHostCftMode) Bases:

`IntEnum`

Host-side Compute Fabric Transport (CFT) mode, mirroring

.`ncclHostCftMode_t`

Set on

to control whether the communicator creates the CUDA fabric logical endpoints that back the host-side CFT queries.`NCCLConfig.host_cft_mode`

-
DEFAULT
*= -2147483648*[](https://docs.nvidia.com#nccl.core.NcclHostCftMode.DEFAULT) Use the version-specific default.


-
ENABLE
*= 1*[](https://docs.nvidia.com#nccl.core.NcclHostCftMode.ENABLE) Enable host-side CFT support, creating the communicator’s unicast and multicast logical endpoints during the first window registration.


-
DISABLE
*= 2*[](https://docs.nvidia.com#nccl.core.NcclHostCftMode.DISABLE) Disable host-side CFT support.


-
FALLBACK
*= 3*[](https://docs.nvidia.com#nccl.core.NcclHostCftMode.FALLBACK) Try to create the logical endpoints; on error, disable host-side CFT instead of failing.


-
DEFAULT

### NcclNvlsHostMode[](https://docs.nvidia.com#ncclnvlshostmode)

Value of [ NCCLConfig.nvls_host_mode](https://docs.nvidia.com#nccl.core.NCCLConfig.nvls_host_mode).

-
*class*nccl.core.NcclNvlsHostMode(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclNvlsHostMode) Bases:

`IntFlag`

Host-side NVLS mode, mirroring

`ncclNvlsHostMode_t`

.Set on

to select which host NVLS components the communicator uses. The two`NCCLConfig.nvls_host_mode`

`DISABLE_`

members combine; leave the field unset for the library default.-
ENABLE
*= 0*[](https://docs.nvidia.com#nccl.core.NcclNvlsHostMode.ENABLE) Enable all host NVLS components.


-
DISABLE_TRANSPORT
*= 1*[](https://docs.nvidia.com#nccl.core.NcclNvlsHostMode.DISABLE_TRANSPORT) Disable the NVLS transport and the registered-buffer optimization.


-
DISABLE_SYMMETRIC_MULTIMEM
*= 2*[](https://docs.nvidia.com#nccl.core.NcclNvlsHostMode.DISABLE_SYMMETRIC_MULTIMEM) Disable multimem in NCCL’s symmetric kernels and copy-engine paths.


-
DISABLE
*= 2147483647*[](https://docs.nvidia.com#nccl.core.NcclNvlsHostMode.DISABLE) Disable all present and future host NVLS components.


-
ENABLE

## NCCLCollConfig[](https://docs.nvidia.com#ncclcollconfig)

Accepted as the `config`

argument of every collective on
[ Communicator](https://docs.nvidia.com/communicator/class.html#nccl.core.Communicator). See the individual field documentation for unset
behavior and usage requirements.

-
*class*nccl.core.NCCLCollConfig(***,*min_ctas: int | None = None*,*max_ctas: int | None = None*,*nvls_ctas: int | None = None*,*cga_cluster_size: int | None = None*,*alg_selection: str | None = None*,*force_alg_selection: bool | None = None*,*cta_policy:*,[CTAPolicy](https://docs.nvidia.com#nccl.core.CTAPolicy)| None = None*user_profiler_tag: int | None = None*,*launch_completion_event:*,[Event](https://nvidia.github.io/cuda-python/cuda-core/latest/generated/cuda.core.Event.html#cuda.core.Event)| int | None = None*vendor_options: tuple[*)[VendorOption](https://docs.nvidia.com#nccl.core.VendorOption), ...] = ()[](https://docs.nvidia.com#nccl.core.NCCLCollConfig) Bases:

`LowppSpec`

Per-call configuration for a single collective.

Accepted as the

`config`

argument of every collective on, tuning that one call. The same configuration must be set on every rank; NCCL validates it only locally, when the call is issued.`Communicator`

See also

-
min_ctas
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.min_ctas) Lower bound on channels/CTAs for this call. Also set by

`NCCL_MIN_CTAS`

, which takes precedence. If unset, inherits.`NCCLConfig.min_ctas`

Available since NCCL 2.31.0.


-
max_ctas
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.max_ctas) Upper bound on channels/CTAs for this call, clamped to the communicator’s

`max_ctas`

. Also set by`NCCL_MAX_CTAS`

, which takes precedence. If unset, inherits.`NCCLConfig.max_ctas`

Available since NCCL 2.31.0.


-
nvls_ctas
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.nvls_ctas) NVLS-pool-specific channel cap for this call. Also set by

`NCCL_NVLS_NCHANNELS`

, which takes precedence. If unset, inherits.`NCCLConfig.nvls_ctas`

Available since NCCL 2.31.0.


-
cga_cluster_size
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.cga_cluster_size) CUDA thread-block-cluster size (0-8, Hopper+). Inconsistent values within one group are undefined behavior. Also set by

`NCCL_CGA_CLUSTER_SIZE`

, which takes precedence. If unset, inherits.`NCCLConfig.cga_cluster_size`

Available since NCCL 2.31.0.


-
alg_selection
*: str | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.alg_selection) Selection string filtering which algorithms this call may use, e.g.

`"ring"`

,`"tree,ring"`

,`"^symk"`

. If unset or empty, NCCL selects automatically.Available since NCCL 2.31.0.


-
force_alg_selection
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.force_alg_selection) Whether an unsatisfiable

is an error rather than a fallback to automatic selection. If unset, NCCL uses True.`alg_selection`

Available since NCCL 2.31.0.


-
cta_policy
*:*[CTAPolicy](https://docs.nvidia.com#nccl.core.CTAPolicy)| None*= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.cta_policy) CTA scheduling policy for this call. Also set by

`NCCL_CTA_POLICY`

, which takes precedence. If unset, inherits.`NCCLConfig.cta_policy`

Available since NCCL 2.31.0.


-
user_profiler_tag
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.user_profiler_tag) Opaque value delivered verbatim to profiler plugins with this call’s profiler events; does not affect execution. Values with the most-significant bit set are reserved by NCCL. If unset, NCCL uses 0.

Available since NCCL 2.31.0.


-
launch_completion_event
*: NcclEventSpec | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.launch_completion_event) Caller-owned, rank-local CUDA event recorded at collective kernel launch completion. With CUDA versions earlier than 12.3, NCCL records the event before the kernel launch instead. A

`cuda.core.Event`

created by`Device().create_event()`

has the required timing-disabled configuration; events passed as integer handles must likewise have timing disabled. Interprocess and interop events are unsupported. Either every rank passes an event or none does, and at most one per communicator in a group. Keep it alive through all queued waits and captured-graph executions. If unset, NCCL records no event.Available since NCCL 2.32.0.


-
vendor_options
*: tuple[*[VendorOption](https://docs.nvidia.com#nccl.core.VendorOption), ...]*= ()*[](https://docs.nvidia.com#nccl.core.NCCLCollConfig.vendor_options) Vendor-specific options;

`(vendor_id, option_id)`

keys must be unique.Available since NCCL 2.31.0.


-
min_ctas

### VendorOption[](https://docs.nvidia.com#vendoroption)

-
*class*nccl.core.VendorOption(*vendor_id: int*,*option_id: int*,*int_value: int | None = None*,*str_value: str | None = None*,*raw_value: int | None = None*)[](https://docs.nvidia.com#nccl.core.VendorOption) Bases:

`object`

A single vendor-specific option attached to an

.`NCCLCollConfig`

Mirrors one

node. Options are identified by the`ncclConfigExt_t`

`(vendor_id, option_id)`

pair; the official NCCL library ignores every extension, so an option only has an effect on a vendor library that recognizes its`vendor_id`

. Vendors pick a non-zero`vendor_id`

less than 2**24 that is unlikely to collide.Exactly one of the three value fields must be set.

See also

-
vendor_id
*: int*[](https://docs.nvidia.com#nccl.core.VendorOption.vendor_id) Vendor-chosen identifier, unique across vendor libraries.


-
option_id
*: int*[](https://docs.nvidia.com#nccl.core.VendorOption.option_id) Vendor-defined identifier distinguishing options within a vendor.


-
int_value
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.VendorOption.int_value) Integer value (

`val.i`

).

-
str_value
*: str | None**= None*[](https://docs.nvidia.com#nccl.core.VendorOption.str_value) String value (

`val.s`

), encoded to UTF-8.

-
raw_value
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.VendorOption.raw_value) Value of any other type (

`val.raw`

), as an integer. If it is an address, the referent must stay valid for the duration of the call.

-
vendor_id

## CTAPolicy[](https://docs.nvidia.com#ctapolicy)

-
*class*nccl.core.CTAPolicy(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.CTAPolicy) Bases:

`IntFlag`

NCCL performance policy for CTA scheduling, used by

and`NCCLConfig.cta_policy`

.`NCCLCollConfig.cta_policy`

-
DEFAULT
*= 0*[](https://docs.nvidia.com#nccl.core.CTAPolicy.DEFAULT) Default CTA policy.


-
EFFICIENCY
*= 1*[](https://docs.nvidia.com#nccl.core.CTAPolicy.EFFICIENCY) Optimize for efficiency.


-
ZERO
*= 2*[](https://docs.nvidia.com#nccl.core.CTAPolicy.ZERO) Zero-CTA optimization.


-
DEFAULT

## NCCLDevCommRequirements[](https://docs.nvidia.com#nccldevcommrequirements)

Used by [ Communicator.create_dev_comm()](https://docs.nvidia.com/communicator/device_setup.html#nccl.core.Communicator.create_dev_comm). Fields left unset
(

`None`

) remain at NCCL’s internal default.-
*class*nccl.core.NCCLDevCommRequirements(***,*lsa_multimem: bool | None = None*,*barrier_count: int | None = None*,*lsa_barrier_count: int | None = None*,*rail_gin_barrier_count: int | None = None*,*lsa_ll_a2a_block_count: int | None = None*,*lsa_ll_a2a_slot_count: int | None = None*,*gin_force_enable: bool | None = None*,*gin_context_count: int | None = None*,*gin_signal_count: int | None = None*,*gin_counter_count: int | None = None*,*gin_connection_type:*,[NcclGinConnectionType](https://docs.nvidia.com/communicator/device_setup.html#nccl.core.NcclGinConnectionType)| None = None*gin_exclusive_contexts: bool | None = None*,*gin_queue_depth: int | None = None*,*gin_traffic_class: int | None = None*,*world_gin_barrier_count: int | None = None*,*gin_strong_signals_required: bool | None = None*,*gin_va_signals_required: bool | None = None*,*gin_custom_stride: int | None = None*,*gin_type:*,[NcclGinType](https://docs.nvidia.com/communicator/device_setup.html#nccl.core.NcclGinType)| None = None*cft_caps:*,[NcclCftCap](https://docs.nvidia.com#nccl.core.NcclCftCap)| None = None*cft_barrier_count: int | None = None*,*teams: tuple[*,[TeamRequirement](https://docs.nvidia.com#nccl.core.TeamRequirement), ...] = ()*resources: tuple[*)[LsaBarrierRequirement](https://docs.nvidia.com#nccl.core.LsaBarrierRequirement)|[GinBarrierRequirement](https://docs.nvidia.com#nccl.core.GinBarrierRequirement)|[LLA2ARequirement](https://docs.nvidia.com#nccl.core.LLA2ARequirement), ...] = ()[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements) Bases:

`LowppSpec`

NCCL device communicator requirements configuration.

This is a reusable high-level Python request consumed by

. Per-team requirements are declared through the`Communicator.create_dev_comm()`

tuple. Each call snapshots the request into independent low-level`teams`

`ncclDevCommRequirements_t`

and linked`ncclTeamRequirements_t`

storage, including separate multimem output handles. NCCL copies the requirements and linked-list nodes before the call returns; the resultingretains the storage referenced by each`DevCommResource`

`outMultimemHandle`

. This object may therefore be changed between calls without affecting device communicators that were already created. Do not mutate it concurrently with.`Communicator.create_dev_comm()`

See also

for the description of each field.`ncclDevCommRequirements`

-
lsa_multimem
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.lsa_multimem) Enable multimem on the LSA team. If unset, NCCL uses False.


-
barrier_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.barrier_count) Number of barriers required. If unset, NCCL uses 0.


-
lsa_barrier_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.lsa_barrier_count) Number of LSA barriers. If unset, NCCL uses 0.


-
rail_gin_barrier_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.rail_gin_barrier_count) Number of railed GIN barriers. If unset, NCCL uses 0.


-
lsa_ll_a2a_block_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.lsa_ll_a2a_block_count) LSA low-latency all-to-all block count. If unset, NCCL uses 0.


-
lsa_ll_a2a_slot_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.lsa_ll_a2a_slot_count) LSA low-latency all-to-all slot count. If unset, NCCL uses 0.


-
gin_force_enable
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_force_enable) Force-enable GPU-Initiated Networking (GIN). If unset, NCCL uses False.


-
gin_context_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_context_count) Number of GIN contexts (hint; actual count may differ). If unset, NCCL uses 4.


-
gin_signal_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_signal_count) Number of GIN signals (guaranteed to start at id=0). If unset, NCCL uses 0.


-
gin_counter_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_counter_count) Number of GIN counters (guaranteed to start at id=0). If unset, NCCL uses 0.


-
gin_connection_type
*:*[NcclGinConnectionType](https://docs.nvidia.com/communicator/device_setup.html#nccl.core.NcclGinConnectionType)| None*= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_connection_type) GIN connection type. If unset, NCCL uses NcclGinConnectionType.NONE.


-
gin_exclusive_contexts
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_exclusive_contexts) Use exclusive GIN contexts. If unset, NCCL uses False.


-
gin_queue_depth
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_queue_depth) GIN queue depth. If unset, NCCL uses 0.


-
gin_traffic_class
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_traffic_class) GIN traffic class. If unset, NCCL uses its internal default.


-
world_gin_barrier_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.world_gin_barrier_count) Number of world GIN barriers. If unset, NCCL uses 0.


-
gin_strong_signals_required
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_strong_signals_required) Whether GIN strong signals are required by kernels using this devComm. When False, using GIN strong signals results in undefined behavior. If unset, NCCL uses True.


-
gin_va_signals_required
*: bool | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_va_signals_required) Whether GIN VA signals are required by kernels using this devComm. When False, using GIN VA signals results in undefined behavior. If unset, NCCL uses True.


-
gin_custom_stride
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_custom_stride) Stride of ranks to connect for GIN. Only consulted when

is`gin_connection_type`

, and must be a multiple of`NcclGinConnectionType.CUSTOM_STRIDE`

. If unset, NCCL uses 1.`NCCLCommProperties.gin_min_stride`


-
gin_type
*:*[NcclGinType](https://docs.nvidia.com/communicator/device_setup.html#nccl.core.NcclGinType)| None*= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.gin_type) GIN transport to require. If unset, NCCL uses

, accepting any available transport.`NcclGinType.NONE`


-
cft_caps
*:*[NcclCftCap](https://docs.nvidia.com#nccl.core.NcclCftCap)| None*= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.cft_caps) Compute Fabric Transport capabilities to request, as a bitmask of

values. Creation fails if CFT resources are requested on a communicator where not all ranks support CFT. If unset, NCCL uses`NcclCftCap`

.`NcclCftCap.NONE`


-
cft_barrier_count
*: int | None**= None*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.cft_barrier_count) Number of CFT barriers to allocate, one per independently addressed barrier slot the kernel uses (commonly one per CTA). If unset, NCCL uses 0.


-
teams
*: tuple[*[TeamRequirement](https://docs.nvidia.com#nccl.core.TeamRequirement), ...]*= ()*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.teams) Per-team requirements. Entries for the same team (by value) are merged, keeping first-appearance order; multimem is requested for a team if any of its entries sets it. A team requested with

`multimem=True`

yields a multimem handle retrievable via.`multimem_handle()`


-
resources
*: tuple[*[LsaBarrierRequirement](https://docs.nvidia.com#nccl.core.LsaBarrierRequirement)|[GinBarrierRequirement](https://docs.nvidia.com#nccl.core.GinBarrierRequirement)|[LLA2ARequirement](https://docs.nvidia.com#nccl.core.LLA2ARequirement), ...]*= ()*[](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.resources) Device resource requirements (LSA/GIN barriers, low-latency all-to-all). Each entry yields, in order, a handle in

. Entries are kept as-is (not merged): each is a distinct resource.`resource_handles`


-
lsa_multimem

### NcclCftCap[](https://docs.nvidia.com#ncclcftcap)

Bitmask value of [ NCCLDevCommRequirements.cft_caps](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.cft_caps).

-
*class*nccl.core.NcclCftCap(*value*,*names=<not given>*,**values*,*module=None*,*qualname=None*,*type=None*,*start=1*,*boundary=None*)[](https://docs.nvidia.com#nccl.core.NcclCftCap) Bases:

`IntFlag`

Compute Fabric Transport capabilities, mirroring

`ncclCftCap_t`

.Combined as a bitmask on

.`NCCLDevCommRequirements.cft_caps`

-
NONE
*= 0*[](https://docs.nvidia.com#nccl.core.NcclCftCap.NONE) No CFT capability requested.


-
CFT
*= 1*[](https://docs.nvidia.com#nccl.core.NcclCftCap.CFT) Request unicast CFT logical endpoints.


-
MULTIMEM
*= 2*[](https://docs.nvidia.com#nccl.core.NcclCftCap.MULTIMEM) Request multicast CFT operations and multimem CFT barriers.


-
NONE

## Requirement entries[](https://docs.nvidia.com#requirement-entries)

The element types of [ NCCLDevCommRequirements.teams](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.teams) and

[.](https://docs.nvidia.com#nccl.core.NCCLDevCommRequirements.resources)

`NCCLDevCommRequirements.resources`

### TeamRequirement[](https://docs.nvidia.com#teamrequirement)

-
*class*nccl.core.TeamRequirement(*team:*,[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam)*multimem: bool = False*)[](https://docs.nvidia.com#nccl.core.TeamRequirement) Bases:

`object`

A per-team requirement for device communicator creation.

Pass a tuple of these as

. When`NCCLDevCommRequirements.teams`

`multimem`

is True, NCCL allocates a multicast handle for the team, retrievable afterwards via.`multimem_handle()`

-
multimem
*: bool**= False*[](https://docs.nvidia.com#nccl.core.TeamRequirement.multimem)

-
multimem

### LsaBarrierRequirement[](https://docs.nvidia.com#lsabarrierrequirement)

-
*class*nccl.core.LsaBarrierRequirement(*team:*,[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam)*n_barriers: int*)[](https://docs.nvidia.com#nccl.core.LsaBarrierRequirement) Bases:

`object`

Requests an LSA barrier resource on

`team`

with`n_barriers`

barriers.Add to

; the finalized`NCCLDevCommRequirements.resources`

is returned in`LsaBarrierHandle`

.`resource_handles`

-
n_barriers
*: int*[](https://docs.nvidia.com#nccl.core.LsaBarrierRequirement.n_barriers)

-
n_barriers

### GinBarrierRequirement[](https://docs.nvidia.com#ginbarrierrequirement)

-
*class*nccl.core.GinBarrierRequirement(*team:*,[NCCLTeam](https://docs.nvidia.com/types.html#nccl.core.NCCLTeam)*n_barriers: int*)[](https://docs.nvidia.com#nccl.core.GinBarrierRequirement) Bases:

`object`

Requests a GIN barrier resource on

`team`

with`n_barriers`

barriers.Add to

; the finalized`NCCLDevCommRequirements.resources`

is returned in`GinBarrierHandle`

.`resource_handles`

-
n_barriers
*: int*[](https://docs.nvidia.com#nccl.core.GinBarrierRequirement.n_barriers)

-
n_barriers

### LLA2ARequirement[](https://docs.nvidia.com#lla2arequirement)

-
*class*nccl.core.LLA2ARequirement(*n_blocks: int*,*max_elements: int*,*max_element_size: int*)[](https://docs.nvidia.com#nccl.core.LLA2ARequirement) Bases:

`object`

Requests a low-latency all-to-all resource with

`n_blocks`

blocks, sized to hold up to`max_elements`

elements of at most`max_element_size`

bytes each.Add to

; the finalized`NCCLDevCommRequirements.resources`

is returned in`LLA2AHandle`

.`resource_handles`

-
n_blocks
*: int*[](https://docs.nvidia.com#nccl.core.LLA2ARequirement.n_blocks)

-
max_elements
*: int*[](https://docs.nvidia.com#nccl.core.LLA2ARequirement.max_elements)

-
max_element_size
*: int*[](https://docs.nvidia.com#nccl.core.LLA2ARequirement.max_element_size)

-
n_blocks