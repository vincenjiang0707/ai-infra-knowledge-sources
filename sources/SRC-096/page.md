source: https://github.com/openucx/ucx/releases

# Releases: openucx/ucx

Releases · openucx/ucx

## Release list

## v1.22.0

## 1.22.0 (August 2, 2026)

### Features:

#### UCP

- Added SGL datatype support for non-blocking PUT operations
- Added GET and PUT rendezvous protocols for RMA operations
- Added fault-tolerance recovery foundation
- Added AM, zcopy, multi, and PSN protocol failover support
- Added endpoint flush failover and first-fragment retransmission support
- Added multi-lane support for device operations
- Added memory registration flags to UCP/UCT/UCS APIs
- Enabled v2 operations on proxy and wireup endpoints
- Added transport and wireup debugging table dumps during context and endpoint creation
- Set four rails by default for Vera platforms

#### UCT

- Added UCT v2 capability flags for SGL zcopy operations
- Enhanced endpoint connectivity checks

#### RDMA CORE (IB, ROCE, etc.)

- Added plugin infrastructure for IB token query and plugin-provided RC extended operations
- Added per-endpoint RC transmit queue reservation for resource checks
- Added IB/MLX5 initiator small-fence WQE control flag
- Applied ECE returned by ibv_query_ece by default
- Enabled relaxed ordering by default for Vera CPU platforms

#### CUDA

- Added GDRCopy PCIe BAR1 export option
- Added POSIX file descriptor handle support for same-machine CUDA VMM IPC
- Added support for CUDA device aliasing with MPS MLOPart

#### UCS

- Added table builder debug API
- Added ucs_string_buffer_vappendf utility
- Added numeric range support for device configuration
- Added Vera CPU support

#### UCM

- Propagated memory attributes in allocation events

#### Tools

- Added software GET responder progress support in perftest

#### Build

- Added PR build modes
- Added Ubuntu 26.04, TencentOS 4.4, and GCC 15.2 build coverage
- Added GB300/aarch64 DL cluster test pipeline coverage
- Added parallel static checks
- Enabled on-demand DRP testing for release pipelines
- Added configure option to append a SONAME suffix

### Bugfixes:

#### UCP

- Fixed endpoint fault-tolerance discard and failover flows
- Fixed fallback handling when no more lanes are available
- Fixed AM reply endpoint lookup during initialization
- Fixed memory release crash in active-message path
- Fixed rcache validity check before memory handle invalidation
- Fixed context creation when only accelerator devices are available
- Fixed error reporting when the transport/device resource limit is exceeded
- Fixed RMA rendezvous rkey size assertion
- Fixed bandwidth formatting macros
- Fixed single network-device filtering to use minimum distance
- Fixed protocol assertions and short selection diagnostics
- Fixed zero-length memory handle packing in trace logging
- Fixed rendezvous remote-memory flag estimation from rkey memory-domain maps
- Disabled RMA rendezvous protocols on non-Vera platforms
- Fixed active-message lane selection to preserve latency priority
- Fixed rendezvous multi-lane protocol selection to preserve combined minimum sizes
- Fixed unnecessary rendezvous PUT fences on ordered transports

#### ZE

- Fixed ZE driver enumeration, PCI fallback, IOV bounds, and DMA-BUF memory query semantics
- Fixed ZE memory query system-device detection

#### CUDA

- Fixed CUDA managed-memory Valgrind failures
- Fixed CUDA IPC remote-cache destruction during endpoint destroy
- Fixed CUDA cleanup for destroyed contexts
- Fixed CUDA IPC single-process unmap checks
- Fixed CUDA NVLink detection
- Fixed CUDA IPC remote-cache handling for GET and PUT paths
- Fixed CUDA IPC reachability for same-process interfaces
- Fixed CUDA copy memory-flag detection with active CUDA contexts

#### RDMA CORE (IB, ROCE, etc.)

- Fixed GGA GET zcopy purge completion
- Fixed GDA DMA-BUF offsets and on-demand DMA-BUF checks
- Fixed GDAKI Direct NIC matrix selection
- Fixed IB DEVX handling for UARs without WC support
- Fixed RoCE reachability for RTN_LOCAL routes
- Reverted ARM Neon BlueFlame writes in IB transport
- Fixed MLX5 DDP PUT fencing
- Fixed IB port-speed query logging for unsupported devices
- Fixed Direct NIC sibling matching when HCAs have no active ports
- Fixed DONT_FORK handling for kernels that support RDMA copy-on-fork
- Fixed GGA MMO fence ordering
- Restricted EMR relaxed ordering to device memory

#### Shared Memory

- Fixed POSIX reachability failure logging in containers

#### TCP

- Fixed TCP negative connect-test timeout

#### Packaging

- Fixed GDA RPM/DEB packaging and RPM development package builds

#### UCS

- Fixed stale async file descriptor event filtering
- Fixed IPv6 scope formatting
- Fixed time initialization to be multi-thread safe
- Fixed namespace identifier sizing for portability
- Fixed portability issues for non-glibc and clang environments

#### Tools

- Fixed perftest ZE allocator thread safety and device routing
- Fixed I/O demo data-size range parsing

#### Build

- Fixed GPUNetIO update failure reporting
- Fixed CMake policy version for examples tests
- Replaced ofed_info usage with native package-manager queries
- Fixed CI build result reporting on exceptions
- Excluded .ci/ changes from PR pipeline triggers

### Known issues:

- JUCX package for this release was renamed to

`1.22.0-1`

, please avoid using`1.22.0`

.

## v1.22.0-rc3

## 1.22.0-rc3 (July 26, 2026)

### Bugfixes:

#### UCP

- Fixed rendezvous multi-lane protocol selection to preserve combined minimum sizes
- Fixed unnecessary rendezvous PUT fences on ordered transports

## v1.22.0-rc2

## 1.22.0-rc2 (July 16, 2026)

### Features:

#### UCP

- Added transport and wireup debugging table dumps during context and endpoint creation
- Set four rails by default for Vera platforms

#### CUDA

- Added POSIX file descriptor handle support for same-machine CUDA VMM IPC
- Added support for CUDA device aliasing with MPS MLOPart

#### RDMA CORE (IB, ROCE, etc.)

- Enabled relaxed ordering by default for Vera CPU platforms

#### UCM

- Propagated memory attributes in allocation events

#### Build

- Added configure option to append a SONAME suffix

### Bugfixes:

#### UCP

- Fixed rendezvous remote-memory flag estimation from rkey memory-domain maps
- Disabled RMA rendezvous protocols on non-Vera platforms
- Fixed active-message lane selection to preserve latency priority

#### CUDA

- Fixed CUDA copy memory-flag detection with active CUDA contexts

#### RDMA CORE (IB, ROCE, etc.)

- Fixed Direct NIC sibling matching when HCAs have no active ports
- Fixed DONT_FORK handling for kernels that support RDMA copy-on-fork
- Fixed GGA MMO fence ordering
- Restricted EMR relaxed ordering to device memory

## v1.22.0-rc1

## 1.22.0-rc1 (June 29, 2026)

### Features:

#### UCP

- Added SGL datatype support for non-blocking PUT operations
- Added GET and PUT rendezvous protocols for RMA operations
- Added fault-tolerance recovery foundation
- Added AM, zcopy, multi, and PSN protocol failover support
- Added endpoint flush failover and first-fragment retransmission support
- Added multi-lane support for device operations
- Added memory registration flags to UCP/UCT/UCS APIs
- Enabled v2 operations on proxy and wireup endpoints

#### UCT

- Added UCT v2 capability flags for SGL zcopy operations
- Enhanced endpoint connectivity checks

#### RDMA CORE (IB, ROCE, etc.)

- Added plugin infrastructure for IB token query and plugin-provided RC extended operations
- Added per-endpoint RC transmit queue reservation for resource checks
- Added IB/MLX5 initiator small-fence WQE control flag
- Applied ECE returned by ibv_query_ece by default

#### CUDA

- Added GDRCopy PCIe BAR1 export option

#### UCS

- Added table builder debug API
- Added ucs_string_buffer_vappendf utility
- Added numeric range support for device configuration
- Added Vera CPU support

#### Tools

- Added software GET responder progress support in perftest

#### Build

- Added PR build modes
- Added Ubuntu 26.04, TencentOS 4.4, and GCC 15.2 build coverage
- Added GB300/aarch64 DL cluster test pipeline coverage
- Added parallel static checks
- Enabled on-demand DRP testing for release pipelines

### Bugfixes:

#### UCP

- Fixed endpoint fault-tolerance discard and failover flows
- Fixed fallback handling when no more lanes are available
- Fixed AM reply endpoint lookup during initialization
- Fixed memory release crash in active-message path
- Fixed rcache validity check before memory handle invalidation
- Fixed context creation when only accelerator devices are available
- Fixed error reporting when the transport/device resource limit is exceeded
- Fixed RMA rendezvous rkey size assertion
- Fixed bandwidth formatting macros
- Fixed single network-device filtering to use minimum distance
- Fixed protocol assertions and short selection diagnostics
- Fixed zero-length memory handle packing in trace logging

#### ZE

- Fixed ZE driver enumeration, PCI fallback, IOV bounds, and DMA-BUF memory query semantics
- Fixed ZE memory query system-device detection

#### CUDA

- Fixed CUDA managed-memory Valgrind failures
- Fixed CUDA IPC remote-cache destruction during endpoint destroy
- Fixed CUDA cleanup for destroyed contexts
- Fixed CUDA IPC single-process unmap checks
- Fixed CUDA NVLink detection
- Fixed CUDA IPC remote-cache handling for GET and PUT paths
- Fixed CUDA IPC reachability for same-process interfaces

#### RDMA CORE (IB, ROCE, etc.)

- Fixed GGA GET zcopy purge completion
- Fixed GDA DMA-BUF offsets and on-demand DMA-BUF checks
- Fixed GDAKI Direct NIC matrix selection
- Fixed IB DEVX handling for UARs without WC support
- Fixed RoCE reachability for RTN_LOCAL routes
- Reverted ARM Neon BlueFlame writes in IB transport
- Fixed MLX5 DDP PUT fencing
- Fixed IB port-speed query logging for unsupported devices

#### Shared Memory

- Fixed POSIX reachability failure logging in containers

#### TCP

- Fixed TCP negative connect-test timeout

#### Packaging

- Fixed GDA RPM/DEB packaging and RPM development package builds

#### UCS

- Fixed stale async file descriptor event filtering
- Fixed IPv6 scope formatting
- Fixed time initialization to be multi-thread safe
- Fixed namespace identifier sizing for portability
- Fixed portability issues for non-glibc and clang environments

#### Tools

- Fixed perftest ZE allocator thread safety and device routing
- Fixed I/O demo data-size range parsing

#### Build

- Fixed GPUNetIO update failure reporting
- Fixed CMake policy version for examples tests
- Replaced ofed_info usage with native package-manager queries
- Fixed CI build result reporting on exceptions
- Excluded .ci/ changes from PR pipeline triggers

## v1.21.0

## 1.21.0 (June 24, 2026)

### Features:

#### UCP

- Added UCX_PROTO_EMULATION_ENABLE option to force zero-copy RMA protocol selection
- Added UCX_MAX_HCA_PER_GPU policy to limit GPU memory registrations to nearest HCAs
- Added device lanes that can access host memory for GPU transfer fallback
- Enabled gdr_copy for memtype endpoint transport

#### UCT

- Added device channel pool support
- Added CPU memory usage as AMO local buffer for device operations

#### RDMA CORE (IB, ROCE, etc.)

- Added UCX_IB_GDA_RETAIN_INACTIVE_CTX option to control inactive CUDA context retention in GDAKI
- Added configure option to enable or disable GGA transport

#### Build

- Added --without-gda configure option
- Made cuRAND an optional dependency for perftest CUDA kernels

#### CI/Testing

- Added dry-run package installation checks to the release package build

### Bugfixes:

#### Build

- Fixed support for -Og by disabling always-inline attributes

#### UCP

- Fixed progress counter to return the actual operation status
- Fixed multi protocol minimum size handling for 1-byte operations
- Fixed endpoint finalization when no P2P or connection-manager lane is available

#### UCT

- Fixed notify callback handling by adding a NULL check

#### CUDA

- Fixed CUDA IPC accessibility cache separation for local and remote rkeys
- Fixed CUDA IPC cache/LRU invariant for referenced regions
- Fixed DMA-BUF offsets for interior CUDA addresses

#### ROCM

- Fixed hangs in HIP MPI and OMB tests
- Fixed endpoint flush for in-flight ROCm operations

#### RDMA CORE (IB, ROCE, etc.)

- Fixed GDA DMA-BUF offset handling
- Fixed GDA WQE ordering by using CAS-based readiness marking
- Fixed GDAKI CUDA context handling during endpoint creation
- Fixed GDAKI NIC/GPU mapping when CUDA_VISIBLE_DEVICES hides physical GPUs

### TCP

- Fixed interface selection by skipping IPv4 link-local addresses

#### UCS

- Reverted dynamically loaded external module/plugin support

#### Packaging

- Fixed Debian maintainer field
- Fixed GDA RPM build
- Fixed GDA RPM/devel package layout for CUDA/GDA subpackages
- Fixed RPM/DEB handling when GDA is disabled

## v1.21.0-rc2

## v1.21.0-rc2 (June 8, 2026)

### Features:

#### RDMA CORE (IB, ROCE, etc.)

- Added configure option to enable or disable GGA transport

### Bugfixes:

#### RDMA CORE (IB, ROCE, etc.)

- Fixed GDAKI CUDA context handling during endpoint creation
- Fixed GDAKI NIC/GPU mapping when CUDA_VISIBLE_DEVICES hides physical GPUs

#### TCP

- Fixed interface selection by skipping IPv4 link-local addresses

## v1.21.0-rc1

## 1.21.0-rc1 (May 24, 2026)

### Features:

#### UCP

- Added UCX_PROTO_EMULATION_ENABLE option to force zero-copy RMA protocol selection
- Added UCX_MAX_HCA_PER_GPU policy to limit GPU memory registrations to nearest HCAs
- Added device lanes that can access host memory for GPU transfer fallback
- Enabled gdr_copy for memtype endpoint transport

#### UCT

- Added device channel pool support
- Added CPU memory usage as AMO local buffer for device operations

#### RDMA CORE (IB, ROCE, etc.)

- Added UCX_IB_GDA_RETAIN_INACTIVE_CTX option to control inactive CUDA context retention in GDAKI

#### Build

- Added --without-gda configure option
- Made cuRAND an optional dependency for perftest CUDA kernels

#### CI/Testing

- Added dry-run package installation checks to the release package build

### Bugfixes:

#### Build

- Fixed support for -Og by disabling always-inline attributes

#### UCP

- Fixed progress counter to return the actual operation status
- Fixed multi-protocol minimum size handling for 1-byte operations
- Fixed endpoint finalization when no P2P or connection-manager lane is available

#### UCT

- Fixed notify callback handling by adding a NULL check

#### CUDA

- Fixed CUDA IPC accessibility cache separation for local and remote rkeys
- Fixed CUDA IPC cache/LRU invariant for referenced regions
- Fixed DMA-BUF offsets for interior CUDA addresses

#### ROCM

- Fixed hangs in HIP MPI and OMB tests

#### RDMA CORE (IB, ROCE, etc.)

- Fixed GDA DMA-BUF offset handling
- Fixed GDA WQE ordering by using CAS-based readiness marking

#### UCS

- Reverted dynamically loaded external module/plugin support

#### Packaging

- Fixed Debian maintainer field
- Fixed GDA RPM build
- Fixed GDA RPM/devel package layout for CUDA/GDA subpackages
- Fixed RPM/DEB handling when GDA is disabled

## v1.20.1

## 1.20.1 (May 6, 2026)

### Features:

#### RDMA CORE (IB, ROCE, etc.)

- Added 'auto' option for UCX_IB_MLX5_DEVX_OBJECTS which disables DevX when ODP is available (for Grace)
- Prioritize routes with longer subnet masks for improved reachability check accuracy

#### Documentation

- Clarified that user buffer can be modified after calling ucp_atomic_op_nbx

### Bugfixes:

#### Build

- Fixed IB configuration const correctness for strchr() to allow compilation with GCC 15.2.1

#### UCP

- Increased TLS info buffer size in transport selection to prevent potential truncation
- Fixed incorrect warning about valid environment variable names
- Fixed ucp_config_modify not reporting an error when no matching modifiable configuration exists.

#### RDMA CORE (IB, ROCE, etc.)

- Fixed DevX objects flag handling
- Fixed device memory allocation alignment in MLX5 DevX
- Fixed IB memory handle flags enum order
- Disabled indirect atomic registration for Direct NIC
- Fixed stale destination endpoint ID and acks from before connection reset in UD transport
- Fix RoCE reachable route check when node_guuid is not unique among HCAs

#### CUDA

- Fixed CUDA context handling for system device during rkey unpack

#### ROCM

- Fixed HSA memory type check for newer ROCm releases

#### UCS

- Fixed rcache locking for GDR copy

#### Packaging

- Fix libnvidia-compute removal from ucx-cuda debian package dependencies, breaking existing installation
- Obsoleted KNEM sub-package
- Fix maintainer field in debian packaging

## v1.20.1-rc2

## 1.20.1-rc2 (April 6, 2026)

### Bugfixes:

#### Build

- Fixed IB configuration const correctness for strchr() to allow compilation with GCC 15.2.1

## v1.20.1-rc1

## 1.20.1-rc1 (March 18, 2026)

### Features:

#### RDMA CORE (IB, ROCE, etc.)

- Added 'auto' option for UCX_IB_MLX5_DEVX_OBJECTS which disables DevX when ODP is available (for Grace)
- Prioritize routes with longer subnet masks for improved reachability check accuracy

#### Documentation

- Clarified that user buffer can be modified after calling ucp_atomic_op_nbx

### Bugfixes:

#### UCP

- Increased TLS info buffer size in transport selection to prevent potential truncation
- Fixed incorrect warning about valid environment variable names
- Fixed ucp_config_modify not reporting an error when no matching modifiable configuration exists.

#### RDMA CORE (IB, ROCE, etc.)

- Fixed DevX objects flag handling
- Fixed device memory allocation alignment in MLX5 DevX
- Fixed IB memory handle flags enum order
- Disabled indirect atomic registration for Direct NIC
- Fixed stale destination endpoint ID and acks from before connection reset in UD transport
- Fix RoCE reachable route check when node_guuid is not unique among HCAs

#### CUDA

- Fixed CUDA context handling for system device during rkey unpack

#### ROCM

- Fixed HSA memory type check for newer ROCm releases

#### UCS

- Fixed rcache locking for GDR copy

#### Packaging

- Fix libnvidia-compute removal from ucx-cuda debian package dependencies, breaking existing installation
- Obsoleted KNEM sub-package