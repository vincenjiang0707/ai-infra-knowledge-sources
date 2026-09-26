source: https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/genindex.html

NCCL
2.32
Overview of NCCL
Setup
Building with TLS support
Configuring TCP encryption
Using NCCL
Creating a Communicator
Using MIG instances
Creating a communicator with options
Creating a communicator using multiple ncclUniqueIds
Shrinking a communicator
Growing a communicator
Creating more communicators
Using multiple NCCL communicators concurrently
Finalizing a communicator
Destroying a communicator
Error handling and communicator abort
Asynchronous errors and error handling
Fault Tolerance
Quality of Service
Collective Operations
AllReduce
Broadcast
Reduce
AllGather
ReduceScatter
AlltoAll
Gather
Scatter
Data Pointers
CUDA Stream Semantics
Mixing Multiple Streams within the same ncclGroupStart/End() group
Group Calls
Management Of Multiple GPUs From One Thread
Aggregated Operations (2.2 and later)
Group Operation Ordering Semantics
Nonblocking Group Operation
Point-to-point communication
Two-sided communication
Sendrecv
One-to-all (scatter)
All-to-one (gather)
All-to-all
Neighbor exchange
One-sided communication
PutSignal and WaitSignal
Barrier
All-to-all
Thread Safety
In-place Operations
Using NCCL with CUDA Graphs
Requirements and Limitations
User Buffer Registration
NVLink Sharp Buffer Registration
IB Sharp Buffer Registration
General Buffer Registration
Buffer Registration, GPU Direct RDMA, and MPS with MLOPart
Buffer Registration and PXN
Memory Allocator
Window Registration
Zero-CTA Optimization
Device-Initiated Communication
Device API
Requirements
Cross-Version Compatibility
Host-Side Setup
Simple LSA Kernel
Multimem Device Kernel
Thread Groups
Teams
Segment Types
Host-Accessible Device Pointer Functions
GIN Device Kernel
Compatibility adjustments
Compute Fabric Transport
Requirements
Device Communicator Setup
Teams and Endpoints
CFT Operations
CFT Barriers
Examples
Cross-proxy Fences
NCCL API
Communicator Creation and Management Functions
ncclGetLastError
ncclGetErrorString
ncclGetVersion
ncclGetUniqueId
ncclSetEncryption
ncclCommInitRank
ncclCommInitAll
ncclCommInitRankConfig
ncclCommInitRankScalable
ncclCommSplit
ncclCommShrink
ncclCommGetUniqueId
ncclCommGrow
ncclCommRevoke
ncclCommFinalize
ncclCommDestroy
ncclCommAbort
ncclCommGetAsyncError
ncclCommCount
ncclCommCuDevice
ncclCommUserRank
ncclCommRegister
ncclCommDeregister
ncclCommWindowRegister
ncclCommWindowDeregister
ncclMemAlloc
ncclMemFree
ncclCommSuspend
ncclCommResume
ncclCommMemStats
Collective Communication Functions
ncclAllReduce
ncclBroadcast
ncclReduce
ncclAllGather
ncclReduceScatter
ncclAlltoAll
ncclGather
ncclScatter
Per-Collective Configuration Variants
Group Calls
ncclGroupStart
ncclGroupEnd
ncclGroupSimulateEnd
Point To Point Communication Functions
Two-Sided Point-to-Point Operations
ncclSend
ncclRecv
One-Sided Point-to-Point Operations (RMA)
ncclPutSignal
ncclSignal
ncclWaitSignal
Types
ncclComm_t
ncclResult_t
ncclDataType_t
ncclRedOp_t
ncclScalarResidence_t
ncclConfig_t
ncclEncryptionConfig_t
ncclCollConfig_t
ncclSimInfo_t
ncclCommMemStat_t
ncclWindow_t
User Defined Reduction Operators
ncclRedOpCreatePreMulSum
ncclRedOpDestroy
NCCL API Supported Flags
Window Registration Flags
NCCL Communicator CTA Policy Flags
Communicator Shrink Flags
GIN Optimization Flags
Device API
Device API – Host-Side Setup
Host-Side Setup
Host-Accessible Device Pointer Functions
Device API – Memory and LSA
LSA
Multimem
Device API – GIN
GIN
Device API - CFT
Compute Fabric Transport
CFT Communicator Requirements
CFT Teams
Logical Endpoint Queries
CFT Operations
Reduction Operations
CFT Barriers
Device API – Remote Reduce and Copy: Building Blocks for Custom Communication Kernels
Compile-Time Requirements
API Overview
ReduceSum — N Sources to One Destination
Copy (Broadcast) — One Source to N Destinations
ReduceSumCopy
Lambda-Based (Custom Layouts)
Custom Reduction Operators
NCCL Parameter API
Types
Handle-Based API
ncclParamBind
Accessor Family of Functions - ncclResult_t ncclParamGet*(ncclParamHandle_t h, T* out)
ncclParamGetStr
ncclParamGet
Key-Based API
ncclParamGetParameter
ncclParamGetAllParameterKeys
ncclParamDumpAll
Language Bindings
Python Bindings (NCCL4Py)
Communicator
Communicator Class
Creation and Lifecycle Methods
Collective Communication Methods
Point-to-Point and Signal Methods
Memory Registration Methods
Device Communicator Setup
Status and Utility Methods
Configuration
NCCLConfig
NCCLCollConfig
CTAPolicy
NCCLDevCommRequirements
Requirement entries
Group Operations
group
group_start
group_end
GroupSimInfo
Memory Management
mem_alloc
mem_free
Communicator Resources
CommResource
RegisteredBufferHandle
RegisteredWindowHandle
CftLeInfo
CustomRedOp
DevCommResource
Device resource handles
Types and Constants
Data type
Reduction operator
Team
Type aliases
Exceptions
Parameters
params
dump_params
Versions
show_versions
get_version
VersionInfo
LibraryInfo
Framework Interop
CuPy
PyTorch
Migrating from NCCL 1 to NCCL 2
Initialization
Communication
Counts
In-place usage for AllGather and ReduceScatter
AllGather arguments order
Datatypes
Error codes
Examples
Communicator Creation and Destruction Examples
Example 1: Single Process, Single Thread, Multiple Devices
Example 2: One Device per Process or Thread
Example 3: Multiple Devices per Thread
Example 4: Multiple communicators per device
Communication Examples
Example 1: One Device per Process or Thread
Example 2: Multiple Devices per Thread
NCCL and MPI
API
Using multiple devices per process
ReduceScatter operation
Send and Receive counts
Other collectives and point-to-point operations
In-place operations
Using NCCL within an MPI Program
MPI Progress
Inter-GPU Communication with CUDA-aware MPI
Environment Variables
System configuration
NCCL_SOCKET_IFNAME
Values accepted
NCCL_SOCKET_FAMILY
Values accepted
NCCL_SOCKET_MAGIC
Values accepted
NCCL_SOCKET_RETRY_CNT
Values accepted
NCCL_SOCKET_RETRY_SLEEP_MSEC
Values accepted
NCCL_SOCKET_POLL_TIMEOUT_MSEC
Values accepted
NCCL_SOCKET_NTHREADS
Values accepted
NCCL_NSOCKS_PERTHREAD
Values accepted
NCCL_CROSS_NIC
Values accepted
NCCL_IB_HCA
Values accepted
NCCL_IB_RAIL_POLICY
Values accepted
NCCL_IB_TIMEOUT
Values accepted
NCCL_IB_RETRY_CNT
Values accepted
NCCL_IB_GID_INDEX
Values accepted
NCCL_IB_ADDR_FAMILY
Values accepted
NCCL_IB_ADDR_RANGE
Values accepted
NCCL_IB_ROCE_VERSION_NUM
Values accepted
NCCL_IB_PKEY
Values accepted
NCCL_IB_PKEY_VALUE
Values accepted
NCCL_IB_SL
Values accepted
NCCL_IB_TC
Values accepted
NCCL_IB_FIFO_TC
Values accepted
NCCL_IB_RETURN_ASYNC_EVENTS
Values accepted
NCCL_IB_EVENT_BASED_LB
Values accepted
NCCL_OOB_NET_ENABLE
Values accepted
NCCL_OOB_NET_IFNAME
Values accepted
NCCL_UID_STAGGER_THRESHOLD
Values accepted
NCCL_UID_STAGGER_RATE
Values accepted
NCCL_NET
Values accepted
NCCL_NET_PLUGIN
Values accepted
NCCL_GIN_PLUGIN
Values accepted
NCCL_RMA_PLUGIN
Values accepted
NCCL_TUNER_PLUGIN
Values accepted
NCCL_PROFILER_PLUGIN
Values accepted
NCCL_ENV_PLUGIN
Values accepted
NCCL_IGNORE_CPU_AFFINITY
Values accepted
NCCL_CONF_FILE
Values accepted
NCCL_DEBUG
Values accepted
NCCL_DEBUG_LEVELS
NCCL_DEBUG_FILE
Values accepted
NCCL_DEBUG_SUBSYS
Values accepted
NCCL_DEBUG_TIMESTAMP_FORMAT
Value accepted
NCCL_DEBUG_TIMESTAMP_LEVELS
Value accepted
NCCL_COLLNET_ENABLE
Value accepted
NCCL_COLLNET_NODE_THRESHOLD
Value accepted
NCCL_CTA_POLICY
Value accepted
NCCL_NETDEVS_POLICY
Value accepted
NCCL_MULTI_RANK_GPU_ENABLE
Values accepted
NCCL_TOPO_FILE
Value accepted
NCCL_TOPO_DUMP_FILE
Value accepted
NCCL_SET_THREAD_NAME
Value accepted
Debugging
NCCL_P2P_DISABLE
Values accepted
NCCL_P2P_LEVEL
Values accepted
Integer Values (Legacy)
NCCL_P2P_DIRECT_DISABLE
Values accepted
NCCL_SHM_DISABLE
Values accepted
NCCL_BUFFSIZE
Values accepted
NCCL_NTHREADS
Values accepted
NCCL_MAX_NCHANNELS
Values accepted
NCCL_MIN_NCHANNELS
Values accepted
NCCL_CHECKS_DISABLE
Values accepted
NCCL_CHECK_POINTERS
Values accepted
NCCL_CHECK_MODE
Values accepted
NCCL_LAUNCH_MODE
Values accepted
NCCL_IB_DISABLE
Values accepted
NCCL_IB_AR_THRESHOLD
Values accepted
NCCL_IB_OOO_RQ
Values accepted
NCCL_IB_QPS_PER_CONNECTION
Values accepted
NCCL_IB_SPLIT_DATA_ON_QPS
Values accepted
NCCL_IB_CUDA_SUPPORT
Values accepted
NCCL_IB_PCI_RELAXED_ORDERING
Values accepted
NCCL_IB_ADAPTIVE_ROUTING
Values accepted
NCCL_IB_ECE_ENABLE
Values accepted
NCCL_MEM_SYNC_DOMAIN
Values accepted
NCCL_CUMEM_ENABLE
Values accepted
NCCL_CUMEM_HOST_ENABLE
Values accepted
NCCL_NET_GDR_LEVEL (formerly NCCL_IB_GDR_LEVEL)
Values accepted
Integer Values (Legacy)
NCCL_NET_GDR_C2C
Values accepted
NCCL_NET_GDR_READ
Values accepted
NCCL_GDRCOPY_ENABLE
Values accepted
NCCL_GDRCOPY_FIFO_ENABLE
Values accepted
NCCL_GDRCOPY_SYNC_ENABLE
Values accepted
NCCL_GDRCOPY_FLUSH_ENABLE
Values accepted
NCCL_NET_SHARED_BUFFERS
Value accepted
NCCL_NET_SHARED_COMMS
Value accepted
NCCL_IGNORE_NET_MISMATCH
Values accepted
NCCL_IGNORE_COLLNET_MISMATCH
Values accepted
NCCL_SINGLE_RING_THRESHOLD
Values accepted
NCCL_LL_THRESHOLD
Values accepted
NCCL_TREE_THRESHOLD
Values accepted
NCCL_ALGO
Values accepted
NCCL_PROTO
Values accepted
NCCL_NVB_DISABLE
Value accepted
NCCL_PXN_DISABLE
Value accepted
NCCL_P2P_PXN_LEVEL
Value accepted
NCCL_PXN_C2C
Value accepted
NCCL_RUNTIME_CONNECT
Value accepted
NCCL_GRAPH_REGISTER
Value accepted
NCCL_LOCAL_REGISTER
Value accepted
NCCL_LEGACY_CUDA_REGISTER
Value accepted
NCCL_WIN_ENABLE
Value accepted
NCCL_SET_STACK_SIZE
Value accepted
NCCL_GRAPH_MIXING_SUPPORT
Value accepted
NCCL_GRAPH_STREAM_ORDERING
Value accepted
NCCL_RMA_EAGER_INIT
Value accepted
NCCL_DMABUF_ENABLE
Value accepted
NCCL_P2P_NET_CHUNKSIZE
Values accepted
NCCL_P2P_LL_THRESHOLD
Values accepted
NCCL_ALLOC_P2P_NET_LL_BUFFERS
Values accepted
NCCL_COMM_BLOCKING
Values accepted
NCCL_CGA_CLUSTER_SIZE
Values accepted
NCCL_MAX_CTAS
Values accepted
NCCL_MIN_CTAS
Values accepted
NCCL_NVLS_ENABLE
Values accepted
NCCL_IB_MERGE_NICS
Values accepted
NCCL_NET_MERGE_POLICY
Values accepted
NCCL_MNNVL_ENABLE
Values accepted
NCCL_MNNVL_UUID
Values accepted
NCCL_MNNVL_CLIQUE_ID
Values accepted
NCCL_RAS_ENABLE
Values accepted
NCCL_RAS_ADDR
Values accepted
NCCL_RAS_TIMEOUT_FACTOR
Values accepted
NCCL_LAUNCH_ORDER_IMPLICIT
Values accepted
NCCL_LAUNCH_RACE_FATAL
Values accepted
NCCL_IPC_USE_ABSTRACT_SOCKET
Values accepted
NCCL_SYM_GIN_KERNELS_ENABLE
Values accepted
Troubleshooting
Diagnostics
RAS Diagnostics
Active Diagnostics
Running Active Diagnostics
Available Checks
GPU troubleshooting
GPU Direct
GPU-to-GPU communication
Linux bare-metal IOMMU and PCIe peer-to-peer
GPU-to-NIC communication
PCI Access Control Services (ACS)
Topology detection
Networking Troubleshooting
Networking issues
IP network interfaces
IP ports
NIC-level diagnostics
InfiniBand
RDMA over Converged Ethernet (RoCE)
Runtime and MPI issues
Errors
Memory issues
Shared memory
Stack size
Unified Memory (UVM)
File Descriptors
MPI
Open MPI based MPIs (e.g. NVIDIA HPC-X)
Performance and tuning
Performance issues
Intra-node communication
Inter-node communication
Multi-node NVLink (MNNVL) issues
Tuning NCCL configuration
CPU and memory affinity
Logging
Logging Environment Variables
Logging Levels
Setting the Logging Level
Adding Logging Levels
Example Output
Filtering by Subsystem
Basic Usage
Available Subsystems
Example Output by Subsystem
Logging to Files
Timestamp Configuration
Timestamp Format
Timestamp Levels
Common Debugging Scenarios
Diagnosing Initialization Hangs
Investigating Network Issues
Understanding Topology Detection
Debugging Performance Issues
Tracing NCCL API Calls
Full Debugging Session
RAS
Principle of Operation
RAS Queries
Sample Output
JSON Output
Monitoring Mode
Control Commands
RAS Diagnostics
Available Checks
Prerequisites
Running During Communicator Initialization
Running On Demand
Output Format
Concurrent Requests
NCCL
Index
Index
_
|
A
|
B
|
C
|
D
|
E
|
F
|
G
|
H
|
I
|
L
|
M
|
N
|
O
|
P
|
R
|
S
|
T
|
U
|
V
|
W
|
Z
_
__init__() (nccl.core.Communicator method)
A
ABORT (nccl.core.CommShrinkFlag attribute)
abort() (nccl.core.Communicator method)
alg_selection (nccl.core.NCCLCollConfig attribute)
allgather() (nccl.core.Communicator method)
allreduce() (nccl.core.Communicator method)
alltoall() (nccl.core.Communicator method)
as_bytes (nccl.core.UniqueId property)
as_ndarray (nccl.core.UniqueId property)
available_gin_types (nccl.core.NCCLCommProperties attribute)
AVG (nccl.core.NcclRedOp attribute)
B
barrier_count (nccl.core.NCCLDevCommRequirements attribute)
BFLOAT16 (nccl.core.NcclDataType attribute)
blocking (nccl.core.NCCLConfig attribute)
broadcast() (nccl.core.Communicator method)
C
CFT (nccl.core.NcclCftCap attribute)
cft_barrier_count (nccl.core.NCCLDevCommRequirements attribute)
cft_caps (nccl.core.NCCLDevCommRequirements attribute)
CFT_COUNTED (nccl.core.WindowFlag attribute)
cft_counted_support (nccl.core.NCCLCommProperties attribute)
cft_multicast_support (nccl.core.NCCLCommProperties attribute)
cft_support (nccl.core.NCCLCommProperties attribute)
CftLeInfo (class in nccl.core)
cga_cluster_size (nccl.core.NCCLCollConfig attribute)
(nccl.core.NCCLConfig attribute)
CHAR (nccl.core.NcclDataType attribute)
close() (nccl.core.CustomRedOp method)
(nccl.core.DevCommResource method)
(nccl.core.RegisteredBufferHandle method)
(nccl.core.RegisteredWindowHandle method)
(nccl.core.resources.CommResource method)
close_all_resources() (nccl.core.Communicator method)
COLL_SYMMETRIC (nccl.core.WindowFlag attribute)
collnet_enable (nccl.core.NCCLConfig attribute)
comm_hash (nccl.core.NCCLCommProperties attribute)
comm_name (nccl.core.NCCLConfig attribute)
CommResource (class in nccl.core.resources)
CommShrinkFlag (class in nccl.core)
CommSuspendFlag (class in nccl.core)
Communicator (class in nccl.core)
context (nccl.core.WaitSignalDesc attribute)
create_dev_comm() (nccl.core.Communicator method)
create_pre_mul_sum() (nccl.core.Communicator method)
cta_policy (nccl.core.NCCLCollConfig attribute)
(nccl.core.NCCLConfig attribute)
CTAPolicy (class in nccl.core)
cuda_dev (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
cuda_variant (nccl.core.LibraryInfo attribute)
CUSTOM_STRIDE (nccl.core.NcclGinConnectionType attribute)
CustomRedOp (class in nccl.core)
D
DEFAULT (nccl.core.CommShrinkFlag attribute)
(nccl.core.CTAPolicy attribute)
(nccl.core.NcclHostCftMode attribute)
(nccl.core.WindowFlag attribute)
destroy() (nccl.core.Communicator method)
dev_comm_runtime_version_size (nccl.core.NCCLCommProperties attribute)
DevCommResource (class in nccl.core)
device (nccl.core.Communicator attribute)
device_api_support (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
DISABLE (nccl.core.NcclHostCftMode attribute)
(nccl.core.NcclNvlsHostMode attribute)
DISABLE_SYMMETRIC_MULTIMEM (nccl.core.NcclNvlsHostMode attribute)
DISABLE_TRANSPORT (nccl.core.NcclNvlsHostMode attribute)
DOUBLE (nccl.core.NcclDataType attribute)
dump_params() (in module nccl.core)
E
EFA_GDA (nccl.core.NcclGinType attribute)
EFFICIENCY (nccl.core.CTAPolicy attribute)
empty() (in module nccl.core.interop.cupy)
(in module nccl.core.interop.torch)
ENABLE (nccl.core.NcclHostCftMode attribute)
(nccl.core.NcclNvlsHostMode attribute)
estimated_time (nccl.core.GroupSimInfo attribute)
F
FALLBACK (nccl.core.NcclHostCftMode attribute)
finalize() (nccl.core.Communicator method)
FLAT (nccl.core.NcclCftTeamMode attribute)
FLOAT (nccl.core.NcclDataType attribute)
FLOAT16 (nccl.core.NcclDataType attribute)
FLOAT32 (nccl.core.NcclDataType attribute)
FLOAT64 (nccl.core.NcclDataType attribute)
FLOAT8E4M3 (nccl.core.NcclDataType attribute)
FLOAT8E5M2 (nccl.core.NcclDataType attribute)
force_alg_selection (nccl.core.NCCLCollConfig attribute)
from_bytes() (nccl.core.UniqueId static method)
from_numpy_dtype() (nccl.core.NcclDataType class method)
FULL (nccl.core.NcclGinConnectionType attribute)
G
gather() (nccl.core.Communicator method)
GDAKI (nccl.core.NcclGinType attribute)
get_async_error() (nccl.core.Communicator method)
get_cft_le_info() (nccl.core.RegisteredWindowHandle method)
get_error_string() (in module nccl.core)
get_last_error() (nccl.core.Communicator method)
get_lsa_device_pointer() (nccl.core.RegisteredWindowHandle method)
get_lsa_multimem_device_pointer() (nccl.core.RegisteredWindowHandle method)
get_mem_stat() (nccl.core.Communicator method)
get_multimem_device_pointer() (nccl.core.RegisteredWindowHandle method)
get_multimem_le_info() (nccl.core.RegisteredWindowHandle method)
get_peer_device_pointer() (nccl.core.RegisteredWindowHandle method)
get_peer_le_info() (nccl.core.RegisteredWindowHandle method)
get_unique_id() (in module nccl.core)
(nccl.core.Communicator method)
get_version() (in module nccl.core)
gin_connection_type (nccl.core.NCCLCommProperties attribute)
(nccl.core.NCCLDevCommRequirements attribute)
gin_context_count (nccl.core.NCCLDevCommRequirements attribute)
gin_counter_count (nccl.core.NCCLDevCommRequirements attribute)
gin_custom_stride (nccl.core.NCCLDevCommRequirements attribute)
gin_exclusive_contexts (nccl.core.NCCLDevCommRequirements attribute)
gin_force_enable (nccl.core.NCCLDevCommRequirements attribute)
gin_min_stride (nccl.core.NCCLCommProperties attribute)
GIN_ONLY (nccl.core.WindowFlag attribute)
gin_queue_depth (nccl.core.NCCLDevCommRequirements attribute)
gin_signal_count (nccl.core.NCCLDevCommRequirements attribute)
gin_strong_signals_required (nccl.core.NCCLDevCommRequirements attribute)
gin_traffic_class (nccl.core.NCCLDevCommRequirements attribute)
gin_type (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
(nccl.core.NCCLDevCommRequirements attribute)
gin_va_signals_required (nccl.core.NCCLDevCommRequirements attribute)
GinBarrierHandle (class in nccl.core)
GinBarrierRequirement (class in nccl.core)
GPI (nccl.core.NcclGinType attribute)
GPU_MEM_PERSIST (nccl.core.NcclCommMemStat attribute)
GPU_MEM_SUSPEND (nccl.core.NcclCommMemStat attribute)
GPU_MEM_SUSPENDED (nccl.core.NcclCommMemStat attribute)
GPU_MEM_TOTAL (nccl.core.NcclCommMemStat attribute)
graph_stream_ordering (nccl.core.NCCLConfig attribute)
graph_usage_mode (nccl.core.NCCLConfig attribute)
group() (in module nccl.core)
group_end() (in module nccl.core)
group_start() (in module nccl.core)
GroupSimInfo (class in nccl.core)
grow() (nccl.core.Communicator method)
H
HALF (nccl.core.NcclDataType attribute)
handle (nccl.core.RegisteredBufferHandle property)
(nccl.core.RegisteredWindowHandle property)
HIER_LSA (nccl.core.NcclCftTeamMode attribute)
HIER_MULTIMEM (nccl.core.NcclCftTeamMode attribute)
host_cft_mode (nccl.core.NCCLConfig attribute)
host_rma_support (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
I
init() (nccl.core.Communicator class method)
init_all() (nccl.core.Communicator class method)
initialize() (nccl.core.Communicator method)
INT (nccl.core.NcclDataType attribute)
INT32 (nccl.core.NcclDataType attribute)
INT64 (nccl.core.NcclDataType attribute)
INT8 (nccl.core.NcclDataType attribute)
int_value (nccl.core.VendorOption attribute)
is_valid (nccl.core.Communicator attribute)
(nccl.core.CustomRedOp property)
(nccl.core.DevCommResource property)
(nccl.core.RegisteredBufferHandle property)
(nccl.core.RegisteredWindowHandle property)
(nccl.core.resources.CommResource property)
itemsize (nccl.core.NcclDataType property)
L
launch_completion_event (nccl.core.NCCLCollConfig attribute)
launch_order_implicit (nccl.core.NCCLConfig attribute)
le_id (nccl.core.CftLeInfo attribute)
le_offset (nccl.core.CftLeInfo attribute)
libnccl (nccl.core.VersionInfo attribute)
LibraryInfo (class in nccl.core)
LLA2AHandle (class in nccl.core)
LLA2ARequirement (class in nccl.core)
lsa_barrier_count (nccl.core.NCCLDevCommRequirements attribute)
lsa_ll_a2a_block_count (nccl.core.NCCLDevCommRequirements attribute)
lsa_ll_a2a_slot_count (nccl.core.NCCLDevCommRequirements attribute)
lsa_multimem (nccl.core.NCCLDevCommRequirements attribute)
LsaBarrierHandle (class in nccl.core)
LsaBarrierRequirement (class in nccl.core)
M
MAX (nccl.core.NcclRedOp attribute)
max_ctas (nccl.core.NCCLCollConfig attribute)
(nccl.core.NCCLConfig attribute)
max_element_size (nccl.core.LLA2ARequirement attribute)
max_elements (nccl.core.LLA2ARequirement attribute)
max_p2p_peers (nccl.core.NCCLConfig attribute)
MEM (nccl.core.CommSuspendFlag attribute)
mem_alloc() (in module nccl.core)
mem_free() (in module nccl.core)
MIN (nccl.core.NcclRedOp attribute)
min_ctas (nccl.core.NCCLCollConfig attribute)
(nccl.core.NCCLConfig attribute)
MULTIMEM (nccl.core.NcclCftCap attribute)
multimem (nccl.core.TeamRequirement attribute)
multimem_handle() (nccl.core.DevCommResource method)
multimem_support (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
MultimemHandle (class in nccl.core)
N
n_barriers (nccl.core.GinBarrierRequirement attribute)
(nccl.core.LsaBarrierRequirement attribute)
n_blocks (nccl.core.LLA2ARequirement attribute)
n_channels_per_net_peer (nccl.core.NCCLConfig attribute)
n_lsa_teams (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
n_ranks (nccl.core.NCCLCommProperties attribute)
(nccl.core.NCCLTeam attribute)
nccl4py (nccl.core.VersionInfo attribute)
nccl_bindings (nccl.core.VersionInfo attribute)
NCCL_CFT (C macro)
NCCL_CFT_MULTIMEM (C macro)
NCCL_CFT_NONE (C macro)
NCCL_CTA_POLICY_DEFAULT (C macro)
NCCL_CTA_POLICY_EFFICIENCY (C macro)
NCCL_CTA_POLICY_ZERO (C macro)
NCCL_SHRINK_ABORT (C macro)
NCCL_SHRINK_DEFAULT (C macro)
NCCL_WIN_COLL_SYMMETRIC (C macro)
NCCL_WIN_DEFAULT (C macro)
NCCL_WIN_STRICT_ORDERING (C macro)
ncclAllGather (C function)
ncclAllGatherConfig (C function)
ncclAllReduce (C function)
ncclAllReduceConfig (C function)
ncclAlltoAll (C function)
ncclAlltoAllConfig (C function)
ncclBarrierSession (C++ class)
ncclBarrierSession::ginBarrier (C++ function)
ncclBarrierSession::lsaBarrier (C++ function)
ncclBarrierSession::ncclBarrierSession (C++ function)
,
[1]
,
[2]
,
[3]
ncclBarrierSession::sync (C++ function)
ncclBcast (C function)
ncclBroadcast (C function)
ncclBroadcastConfig (C function)
NcclBufferSpec (in module nccl.core)
ncclCft (C++ class)
ncclCft::flush (C++ function)
ncclCft::flushSmem (C++ function)
ncclCft::get (C++ function)
ncclCft::ncclCft (C++ function)
ncclCft::pullRed (C++ function)
ncclCft::put (C++ function)
ncclCft::putCpMask (C++ function)
ncclCft::putMultimem (C++ function)
ncclCft::putMultimemCpMask (C++ function)
ncclCft::red (C++ function)
ncclCft::redMultimem (C++ function)
ncclCft::submit (C++ function)
ncclCftBarrierSession (C++ class)
ncclCftBarrierSession::arrive (C++ function)
ncclCftBarrierSession::ncclCftBarrierSession (C++ function)
ncclCftBarrierSession::sync (C++ function)
,
[1]
ncclCftBarrierSession::wait (C++ function)
,
[1]
NcclCftCap (class in nccl.core)
ncclCftOpAnd (C++ struct)
ncclCftOpMax (C++ struct)
ncclCftOpMin (C++ struct)
ncclCftOpOr (C++ struct)
ncclCftOpSum (C++ struct)
ncclCftOpXor (C++ struct)
ncclCftSmem (C++ struct)
NcclCftTeamMode (class in nccl.core)
ncclCftTeamMode_t (C type)
ncclCftTeamMode_t.NCCL_CFT_TEAM_FLAT (C macro)
ncclCftTeamMode_t.NCCL_CFT_TEAM_HIER_LSA (C macro)
ncclCftTeamMode_t.NCCL_CFT_TEAM_HIER_MULTIMEM (C macro)
NCCLCollConfig (class in nccl.core)
ncclCollConfig_t (C type)
ncclCollConfig_t.algSelection (C member)
ncclCollConfig_t.cgaClusterSize (C member)
ncclCollConfig_t.CTAPolicy (C member)
ncclCollConfig_t.ext (C member)
ncclCollConfig_t.forceAlgSelection (C member)
ncclCollConfig_t.launchCompletionEvent (C member)
ncclCollConfig_t.maxCTAs (C member)
ncclCollConfig_t.minCTAs (C member)
ncclCollConfig_t.NCCL_COLLCONFIG_INITIALIZER (C macro)
ncclCollConfig_t.nvlsCTAs (C member)
ncclCollConfig_t.userProfilerTag (C member)
ncclComm_t (C type)
ncclCommAbort (C function)
ncclCommCount (C function)
ncclCommCuDevice (C function)
ncclCommDeregister (C function)
ncclCommDestroy (C function)
ncclCommFinalize (C function)
ncclCommGetAsyncError (C function)
ncclCommGetUniqueId (C function)
ncclCommGrow (C function)
ncclCommInitAll (C function)
ncclCommInitRank (C function)
ncclCommInitRankConfig (C function)
ncclCommInitRankScalable (C function)
NcclCommMemStat (class in nccl.core)
ncclCommMemStat_t (C type)
ncclCommMemStat_t.ncclStatGpuMemPersist (C macro)
ncclCommMemStat_t.ncclStatGpuMemSuspend (C macro)
ncclCommMemStat_t.ncclStatGpuMemSuspended (C macro)
ncclCommMemStat_t.ncclStatGpuMemTotal (C macro)
ncclCommMemStats (C function)
NCCLCommProperties (class in nccl.core)
ncclCommProperties_t (C type)
ncclCommProperties_t.commHash (C member)
ncclCommProperties_t.cudaDev (C member)
ncclCommProperties_t.deviceApiSupport (C member)
ncclCommProperties_t.ginMinStride (C member)
ncclCommProperties_t.ginType (C member)
ncclCommProperties_t.multimemSupport (C member)
ncclCommProperties_t.nLsaTeams (C member)
ncclCommProperties_t.nRanks (C member)
ncclCommProperties_t.nvmlDev (C member)
ncclCommProperties_t.railedGinType (C member)
ncclCommProperties_t.rank (C member)
ncclCommQueryProperties (C function)
ncclCommRegister (C function)
ncclCommResume (C function)
ncclCommRevoke (C function)
ncclCommShrink (C function)
ncclCommSplit (C function)
ncclCommSuspend (C function)
ncclCommUserRank (C function)
ncclCommWindowDeregister (C function)
ncclCommWindowRegister (C function)
NCCLConfig (class in nccl.core)
ncclConfig_t (C type)
ncclConfig_t.blocking (C macro)
ncclConfig_t.cgaClusterSize (C macro)
ncclConfig_t.collnetEnable (C macro)
ncclConfig_t.commName (C macro)
ncclConfig_t.CTAPolicy (C macro)
ncclConfig_t.graphStreamOrdering (C macro)
ncclConfig_t.graphUsageMode (C macro)
ncclConfig_t.hostCftMode (C macro)
ncclConfig_t.launchOrderImplicit (C macro)
ncclConfig_t.maxCTAs (C macro)
ncclConfig_t.maxP2pPeers (C macro)
ncclConfig_t.minCTAs (C macro)
ncclConfig_t.NCCL_CONFIG_INITIALIZER (C macro)
ncclConfig_t.nChannelsPerNetPeer (C macro)
ncclConfig_t.netName (C macro)
ncclConfig_t.numRmaCtx (C macro)
ncclConfig_t.numRmaSig (C macro)
ncclConfig_t.nvlsCTAs (C macro)
ncclConfig_t.nvlsHostMode (C macro)
ncclConfig_t.rmaEagerInit (C macro)
ncclConfig_t.shrinkShare (C macro)
ncclConfig_t.splitShare (C macro)
ncclConfig_t.trafficClass (C macro)
ncclConfigExt_t (C type)
NcclDataType (class in nccl.core)
ncclDataType_t (C type)
ncclDataType_t.ncclBfloat16 (C macro)
ncclDataType_t.ncclChar (C macro)
ncclDataType_t.ncclDouble (C macro)
ncclDataType_t.ncclFloat (C macro)
ncclDataType_t.ncclFloat16 (C macro)
ncclDataType_t.ncclFloat32 (C macro)
ncclDataType_t.ncclFloat64 (C macro)
ncclDataType_t.ncclFloat8e4m3 (C macro)
ncclDataType_t.ncclFloat8e5m2 (C macro)
ncclDataType_t.ncclHalf (C macro)
ncclDataType_t.ncclInt (C macro)
ncclDataType_t.ncclInt32 (C macro)
ncclDataType_t.ncclInt64 (C macro)
ncclDataType_t.ncclInt8 (C macro)
ncclDataType_t.ncclUint32 (C macro)
ncclDataType_t.ncclUint64 (C macro)
ncclDataType_t.ncclUint8 (C macro)
ncclDevComm (C type)
ncclDevComm.ginContextCount (C member)
ncclDevComm.lsaRank (C member)
ncclDevComm.lsaSize (C member)
ncclDevComm.nRanks (C member)
ncclDevComm.rank (C member)
ncclDevCommCreate (C function)
ncclDevCommDestroy (C function)
ncclDevCommRequirements (C type)
NCCLDevCommRequirements (class in nccl.core)
ncclDevCommRequirements.barrierCount (C member)
ncclDevCommRequirements.cftBarrierCount (C member)
ncclDevCommRequirements.cftCaps (C member)
ncclDevCommRequirements.ginConnectionType (C member)
ncclDevCommRequirements.ginCounterCount (C member)
ncclDevCommRequirements.ginCustomStride (C member)
ncclDevCommRequirements.ginForceEnable (C member)
ncclDevCommRequirements.ginSignalCount (C member)
ncclDevCommRequirements.ginStrongSignalsRequired (C member)
ncclDevCommRequirements.ginTrafficClass (C member)
ncclDevCommRequirements.ginVaSignalsRequired (C member)
ncclDevCommRequirements.lsaBarrierCount (C member)
ncclDevCommRequirements.lsaMultimem (C member)
ncclDevCommRequirements.railGinBarrierCount (C member)
ncclDevCommRequirements.resourceRequirementsList (C member)
ncclDevCommRequirements.teamRequirementsList (C member)
ncclDevCommRequirements.worldGinBarrierCount (C member)
NcclDeviceSpec (in module nccl.core)
ncclEncryptionConfig_t (C type)
ncclEncryptionConfig_t.mode (C macro)
ncclEncryptionConfig_t.NCCL_ENCRYPTION_CONFIG_INITIALIZER (C macro)
ncclEncryptionConfig_t.NCCL_ENCRYPTION_MODE_PSK (C macro)
ncclEncryptionConfig_t.psk (C macro)
NcclEventSpec (in module nccl.core)
ncclGather (C function)
ncclGatherConfig (C function)
ncclGetCftDeviceLeInfo (C function)
ncclGetCftLeInfo (C++ function)
ncclGetErrorString (C function)
ncclGetLastError (C function)
ncclGetLocalPointer (C++ function)
ncclGetLsaDevicePointer (C function)
ncclGetLsaMultimemDevicePointer (C function)
ncclGetLsaMultimemPointer (C++ function)
ncclGetLsaPointer (C++ function)
ncclGetMultimemDeviceLeInfo (C function)
ncclGetMultimemDevicePointer (C function)
ncclGetMultimemLeInfo (C++ function)
ncclGetPeerDeviceLeInfo (C function)
ncclGetPeerDevicePointer (C function)
ncclGetPeerLeInfo (C++ function)
ncclGetPeerPointer (C++ function)
ncclGetUniqueId (C function)
ncclGetVersion (C function)
ncclGin (C++ class)
ncclGin::flush (C++ function)
ncclGin::flushAsync (C++ function)
ncclGin::get (C++ function)
ncclGin::ncclGin (C++ function)
ncclGin::put (C++ function)
ncclGin::readCounter (C++ function)
ncclGin::readSignal (C++ function)
,
[1]
ncclGin::resetCounter (C++ function)
ncclGin::resetSignal (C++ function)
,
[1]
ncclGin::signal (C++ function)
ncclGin::wait (C++ function)
ncclGin::waitCounter (C++ function)
ncclGin::waitSignal (C++ function)
,
[1]
ncclGin_CounterInc (C++ struct)
ncclGin_CounterInc::counter (C++ member)
ncclGin_SignalAdd (C++ struct)
ncclGin_SignalAdd::signal (C++ member)
ncclGin_SignalAdd::value (C++ member)
ncclGin_SignalInc (C++ struct)
ncclGin_SignalInc::signal (C++ member)
ncclGin_StrongSignalAdd (C++ struct)
ncclGin_StrongSignalAdd::signal (C++ member)
ncclGin_StrongSignalAdd::value (C++ member)
ncclGin_StrongSignalInc (C++ struct)
ncclGin_StrongSignalInc::signal (C++ member)
ncclGin_StrongVASignalAdd (C++ struct)
ncclGin_StrongVASignalAdd::signalOffset (C++ member)
ncclGin_StrongVASignalAdd::signalWindow (C++ member)
ncclGin_StrongVASignalAdd::value (C++ member)
ncclGin_StrongVASignalInc (C++ struct)
ncclGin_StrongVASignalInc::signalOffset (C++ member)
ncclGin_StrongVASignalInc::signalWindow (C++ member)
ncclGin_VASignalAdd (C++ struct)
ncclGin_VASignalAdd::signalOffset (C++ member)
ncclGin_VASignalAdd::signalWindow (C++ member)
ncclGin_VASignalAdd::value (C++ member)
ncclGin_VASignalInc (C++ struct)
ncclGin_VASignalInc::signalOffset (C++ member)
ncclGin_VASignalInc::signalWindow (C++ member)
ncclGin_WeakSignalAdd (C++ struct)
ncclGin_WeakSignalAdd::signal (C++ member)
ncclGin_WeakSignalAdd::value (C++ member)
ncclGin_WeakSignalInc (C++ struct)
ncclGin_WeakSignalInc::signal (C++ member)
ncclGin_WeakVASignalAdd (C++ struct)
ncclGin_WeakVASignalAdd::signalOffset (C++ member)
ncclGin_WeakVASignalAdd::signalWindow (C++ member)
ncclGin_WeakVASignalAdd::value (C++ member)
ncclGin_WeakVASignalInc (C++ struct)
ncclGin_WeakVASignalInc::signalOffset (C++ member)
ncclGin_WeakVASignalInc::signalWindow (C++ member)
ncclGinBarrierSession (C++ class)
ncclGinBarrierSession::ncclGinBarrierSession (C++ function)
,
[1]
ncclGinBarrierSession::sync (C++ function)
NcclGinConnectionType (class in nccl.core)
ncclGinConnectionType_t (C enum)
ncclGinConnectionType_t.NCCL_GIN_CONNECTION_CUSTOM_STRIDE (C enumerator)
ncclGinConnectionType_t.NCCL_GIN_CONNECTION_FULL (C enumerator)
ncclGinConnectionType_t.NCCL_GIN_CONNECTION_NONE (C enumerator)
ncclGinConnectionType_t.NCCL_GIN_CONNECTION_RAIL (C enumerator)
ncclGinCounter_t (C++ type)
ncclGinOptFlagsAggregateRequests (C++ enumerator)
ncclGinOptFlagsDefault (C++ enumerator)
ncclGinSignal_t (C++ type)
NcclGinType (class in nccl.core)
ncclGinType_t (C enum)
ncclGinType_t.NCCL_GIN_TYPE_EFA_GDA (C enumerator)
ncclGinType_t.NCCL_GIN_TYPE_GDAKI (C enumerator)
ncclGinType_t.NCCL_GIN_TYPE_GPI (C enumerator)
ncclGinType_t.NCCL_GIN_TYPE_NONE (C enumerator)
ncclGinType_t.NCCL_GIN_TYPE_PROXY (C enumerator)
ncclGroupEnd (C function)
ncclGroupSimulateEnd (C function)
ncclGroupStart (C function)
NcclHostCftMode (class in nccl.core)
ncclHostCftMode_t (C type)
ncclHostCftMode_t.ncclHostCftDefault (C macro)
ncclHostCftMode_t.ncclHostCftDisable (C macro)
ncclHostCftMode_t.ncclHostCftEnable (C macro)
ncclHostCftMode_t.ncclHostCftFallback (C macro)
NcclInvalid
ncclLocalCopy (C++ function)
,
[1]
ncclLocalReduceSum (C++ function)
,
[1]
ncclLocalReduceSumCopy (C++ function)
ncclLsaBarrierSession (C++ class)
ncclLsaBarrierSession::arrive (C++ function)
ncclLsaBarrierSession::ncclLsaBarrierSession (C++ function)
ncclLsaBarrierSession::sync (C++ function)
ncclLsaBarrierSession::wait (C++ function)
ncclLsaCopy (C++ function)
,
[1]
,
[2]
,
[3]
,
[4]
ncclLsaCopyTma (C++ function)
,
[1]
,
[2]
,
[3]
,
[4]
ncclLsaReduceLsaCopy (C++ function)
ncclLsaReduceMultimemCopy (C++ function)
ncclLsaReduceSum (C++ function)
,
[1]
,
[2]
,
[3]
,
[4]
ncclLsaReduceSumCopy (C++ function)
,
[1]
,
[2]
,
[3]
,
[4]
ncclLsaReduceSumLsaCopy (C++ function)
ncclLsaReduceSumMultimemCopy (C++ function)
,
[1]
,
[2]
ncclMemAlloc (C function)
ncclMemFence (C++ function)
ncclMemFenceScope (C++ enum)
ncclMemFenceScope::Cta (C++ enumerator)
ncclMemFenceScope::Sys (C++ enumerator)
ncclMemFree (C function)
ncclMemProxyType (C++ enum)
ncclMemProxyType::Fabric (C++ enumerator)
ncclMemProxyType::Generic (C++ enumerator)
ncclMultimemCopy (C++ function)
,
[1]
,
[2]
ncclMultimemReduceSum (C++ function)
,
[1]
,
[2]
ncclMultimemReduceSumCopy (C++ function)
,
[1]
,
[2]
ncclMultimemReduceSumLsaCopy (C++ function)
,
[1]
,
[2]
ncclMultimemReduceSumMultimemCopy (C++ function)
NcclNvlsHostMode (class in nccl.core)
ncclParamBind (C function)
ncclParamDumpAll (C function)
ncclParamGet (C function)
ncclParamGetAllParameterKeys (C function)
ncclParamGetI16 (C function)
ncclParamGetI32 (C function)
ncclParamGetI64 (C function)
ncclParamGetI8 (C function)
ncclParamGetParameter (C function)
ncclParamGetStr (C function)
ncclParamGetU16 (C function)
ncclParamGetU32 (C function)
ncclParamGetU64 (C function)
ncclParamGetU8 (C function)
ncclParamHandle_t (C type)
ncclPutSignal (C function)
ncclRecv (C function)
NcclRedOp (class in nccl.core)
ncclRedOp_t (C type)
ncclRedOp_t.ncclAvg (C macro)
ncclRedOp_t.ncclMax (C macro)
ncclRedOp_t.ncclMin (C macro)
ncclRedOp_t.ncclProd (C macro)
ncclRedOp_t.ncclSum (C macro)
ncclRedOpCreatePreMulSum (C function)
ncclRedOpDestroy (C function)
ncclReduce (C function)
ncclReduceConfig (C function)
ncclReduceScatter (C function)
ncclReduceScatterConfig (C function)
ncclResult_t (C type)
ncclResult_t.ncclInProgress (C macro)
ncclResult_t.ncclInternalError (C macro)
ncclResult_t.ncclInvalidArgument (C macro)
ncclResult_t.ncclInvalidUsage (C macro)
ncclResult_t.ncclRemoteError (C macro)
ncclResult_t.ncclSuccess (C macro)
ncclResult_t.ncclSystemError (C macro)
ncclResult_t.ncclUnhandledCudaError (C macro)
ncclScalarResidence_t (C type)
ncclScalarResidence_t.ncclScalarDevice (C macro)
ncclScalarResidence_t.ncclScalarHostImmediate (C macro)
NcclScalarSpec (in module nccl.core)
ncclScatter (C function)
ncclScatterConfig (C function)
ncclSend (C function)
ncclSetEncryption (C function)
ncclSignal (C function)
ncclSimInfo_t (C type)
ncclSimInfo_t.estimatedTime (C macro)
ncclSimInfo_t.NCCL_SIM_INFO_INITIALIZER (C macro)
NcclStreamSpec (in module nccl.core)
NCCLTeam (class in nccl.core)
ncclTeamCft (C function)
(C++ function)
ncclTeamCftMultimem (C function)
(C++ function)
ncclWaitSignal (C function)
ncclWaitSignalDesc_t (C type)
ncclWaitSignalDesc_t.ctx (C member)
ncclWaitSignalDesc_t.opCnt (C member)
ncclWaitSignalDesc_t.peer (C member)
ncclWaitSignalDesc_t.sigIdx (C member)
ncclWindow_t (C type)
net_name (nccl.core.NCCLConfig attribute)
NONE (nccl.core.NcclCftCap attribute)
(nccl.core.NcclGinConnectionType attribute)
(nccl.core.NcclGinType attribute)
nranks (nccl.core.Communicator attribute)
num_rma_ctx (nccl.core.NCCLConfig attribute)
num_rma_sig (nccl.core.NCCLConfig attribute)
numpy_dtype (nccl.core.NcclDataType property)
nvlink_centric_sched (nccl.core.NCCLConfig attribute)
nvls_ctas (nccl.core.NCCLCollConfig attribute)
(nccl.core.NCCLConfig attribute)
nvls_host_mode (nccl.core.NCCLConfig attribute)
nvml_dev (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
O
op (nccl.core.CustomRedOp property)
op_count (nccl.core.WaitSignalDesc attribute)
option_id (nccl.core.VendorOption attribute)
P
params (in module nccl.core)
path (nccl.core.LibraryInfo attribute)
peer (nccl.core.WaitSignalDesc attribute)
PROD (nccl.core.NcclRedOp attribute)
properties (nccl.core.Communicator attribute)
PROXY (nccl.core.NcclGinType attribute)
ptr (nccl.core.Communicator attribute)
(nccl.core.DevCommResource property)
put_signal() (nccl.core.Communicator method)
R
RAIL (nccl.core.NcclGinConnectionType attribute)
rail_gin_barrier_count (nccl.core.NCCLDevCommRequirements attribute)
railed_gin_type (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
rank (nccl.core.Communicator attribute)
(nccl.core.NCCLCommProperties attribute)
(nccl.core.NCCLTeam attribute)
raw_value (nccl.core.VendorOption attribute)
recv() (nccl.core.Communicator method)
reduce() (nccl.core.Communicator method)
reduce_scatter() (nccl.core.Communicator method)
register_buffer() (nccl.core.Communicator method)
register_window() (nccl.core.Communicator method)
RegisteredBufferHandle (class in nccl.core)
RegisteredWindowHandle (class in nccl.core)
resolve_array() (in module nccl.core.interop.cupy)
resolve_tensor() (in module nccl.core.interop.torch)
resource_handles (nccl.core.DevCommResource property)
resources (nccl.core.NCCLDevCommRequirements attribute)
resume() (nccl.core.Communicator method)
revoke() (nccl.core.Communicator method)
rma_eager_init (nccl.core.NCCLConfig attribute)
S
scatter() (nccl.core.Communicator method)
send() (nccl.core.Communicator method)
show_versions() (in module nccl.core)
shrink() (nccl.core.Communicator method)
shrink_share (nccl.core.NCCLConfig attribute)
signal() (nccl.core.Communicator method)
signal_index (nccl.core.WaitSignalDesc attribute)
size (nccl.core.RegisteredBufferHandle property)
(nccl.core.RegisteredWindowHandle property)
split() (nccl.core.Communicator method)
split_share (nccl.core.NCCLConfig attribute)
str_value (nccl.core.VendorOption attribute)
STRICT_ORDERING (nccl.core.WindowFlag attribute)
stride (nccl.core.NCCLTeam attribute)
SUM (nccl.core.NcclRedOp attribute)
suspend() (nccl.core.Communicator method)
T
team (nccl.core.GinBarrierRequirement attribute)
(nccl.core.LsaBarrierRequirement attribute)
(nccl.core.TeamRequirement attribute)
team_cft() (nccl.core.Communicator method)
team_cft_multimem (nccl.core.Communicator attribute)
team_lsa (nccl.core.Communicator attribute)
team_rail (nccl.core.Communicator attribute)
team_rank_to_lsa() (nccl.core.Communicator method)
team_rank_to_world() (nccl.core.Communicator method)
team_world (nccl.core.Communicator attribute)
TeamRequirement (class in nccl.core)
teams (nccl.core.NCCLDevCommRequirements attribute)
traffic_class (nccl.core.NCCLConfig attribute)
U
UINT32 (nccl.core.NcclDataType attribute)
UINT64 (nccl.core.NcclDataType attribute)
UINT8 (nccl.core.NcclDataType attribute)
UniqueId (class in nccl.core)
user_profiler_tag (nccl.core.NCCLCollConfig attribute)
user_ptr (nccl.core.RegisteredWindowHandle property)
V
vendor_id (nccl.core.VendorOption attribute)
vendor_options (nccl.core.NCCLCollConfig attribute)
VendorOption (class in nccl.core)
version (nccl.core.LibraryInfo attribute)
VersionInfo (class in nccl.core)
W
wait_signal() (nccl.core.Communicator method)
WaitSignalDesc (class in nccl.core)
WindowFlag (class in nccl.core)
world_gin_barrier_count (nccl.core.NCCLDevCommRequirements attribute)
Z
ZERO (nccl.core.CTAPolicy attribute)