# Changelog (aggregated from releases.body)

> releases: 17

## v2.28.3-1 (2025-10-06)

See the [NCCL 2.28.3 Release Notes](https://docs.nvidia.com/deeplearning/nccl/release-notes/rel_2-28-3.html#rel_2-28-3) for more information

## Device API (Experimental)
 * Introduces device-side APIs to integrate NCCL communication directly into application kernels.
 * Supports LSA (Load/Store Access) for CUDA P2P communication over NVLink and some PCIe platforms.
 * Supports Multimem for hardware multicast using NVLink SHARP.
 * Adds initial framework for GIN (GPU-Initiated Networking), currently under development.
 * Introduces device communicators created using ncclDevCommCreate.
 * Enables device-side communication operations with synchronization (ncclLsaBarrierSession) and memory accessors (ncclGetLsaPointer, ncclGetLsaMultimemPointer).
 * Experimental APIs - signatures and functionality may evolve in future releases.
 * No ABI compatibility is guaranteed — applications must be recompiled with each new NCCL release.

## Symmetric memory improvements
 * Support for aggregating symmetric operations using ncclGroupStart/End APIs.
 * Reimplement symmetric kernels using device API.

## New Host APIs
 * Introduce new host collective APIs: ncclAlltoAll, ncclScatter, ncclGather.

## CE (Copy Engine) Collectives
 * Reduce SM utilization for alltoall, scatter, gather, and allgather within a single (MN)NVL domain.
 * Free up SM capacity for the application to do computation at the same time.
 * To enable the feature for ncclAllGather, ncclAlltoAll, ncclGather, ncclScatter, register buffers into symmetric windows and use the NCCL_CTA_POLICY_ZERO flag in the communicator config_t.

## NCCL Inspector Plugin
 * Introduces an Inspector plugin for always-on performance monitoring.
 * Produces structured JSON output with metadata, execution time, bandwidth, and optional event traces for each NCCL operation.
 * Enables integration with analysis tools such as Performance Exporter to visualize NCCL performance bottlenecks.
 * Lightweight to enable via environment variables NCCL_PROFILER_PLUGIN and NCCL_INSPECTOR_ENABLE.

## CMake support (Experiemental)
 * Adds a CMake build system as an alternative to existing Makefiles.
 * Known issues: pkg.build and Device API currently do not work with CMake.
 * The known issues will be addressed in a future release.

## Decreased max CTA count from 32 to 16 on Blackwell
 * SM overhead is decreased by 50% with this improvement.
 * This may cause some perf drop on Blackwell because of the reduced SM usage.
 * If the extra SM capacity is not desired, two options are available to restore to previous behavior: 1) Setting NCCL_MIN_CTAS=32 NCCL_MAX_CTAS=32 environment variables; 2) setting communicator config to over-write max CTA count to 32.
 * Based on community feedback, future versions may consider different trade-offs between performance and SM overhead.

## Plugins
 * Network
   * App-aware Network plugin. NCCL passes information about communication operations to be executed on the network end point. This allows for better tuning of network end points and their use in the plugins.
   * Improve handling of physical and virtual network devices and load/unload.
   * Network plugin version 11 - add explicit context and communication ID support for per communicator init/finalize.
   * Add Multi-Request Net API. Using this will help NCCL to anticipate multiple send/recv requests and optimize for it. See maxMultiRequestSize field in ncclNetProperties_v11_t.
 * Profiler
   * Add support for API events (group, collective, and p2p) and for tracking kernel launches in the profiler plugin.
   * Add Inspector Profiler Plugin (see section above).
   * Add a hook to Google’s CoMMA profiler on github.
 * Tuner
   * Expose NCCL tuning constants at tuner initialization via ncclTunerConstants_v5_t.
   * Add NVL Domain Information API.
 * Support multiple plugin types from a single shared object.

## New Parameterization and ncclConfig changes:
 * Add new option NCCL_MNNVL_CLIQUE_ID=-2 which will use rack serial number to partition the MNNVL clique. This will limit NVLink domains to GPUs within a single rack.
 * Add NCCL_NETDEVS_POLICY to control how NET devices are assigned to GPUs. The default (AUTO) is the policy used in previous versions.
 * Add NCCL_SINGLE_PROC_MEM_REG_ENABLE control variable to enable NVLS UB registration in the “one process, multiple ranks” case as opt in.
 * Move nChannelsPerNetPeer into ncclConfig. NCCL_NCHANNELS_PER_NET_PEER can override the value in ncclConfig.
 * Enable PxN over C2C by default
   * PxN over C2C will improve performance for Grace-Blackwell platforms by allowing NCCL to leverage the NIC attached to a peer GPU over NVLINK, C2C, and PCIe.
   * This behavior can be overridden by setting NCCL_PXN_C2C=0.

## Other Improvements:
 * Allow FP8 support for non-reductive operations on pre sm90 devices. (See https://github.com/pytorch/pytorch/pull/151594#discussion_r2135777776)
 * Fix NVLS+CollNet and temporarily disables COLLNET_CHAIN for >8 GPUs.
 * Only consider running interfaces for socket traffic. NCCL will not attempt to use interfaces that do not have the IFF_RUNNING bit. (https://github.com/NVIDIA/nccl/issues/1798)
 * Modernize mutex management. Convert to std::mutex and std::lock_guard.
 * Remove sm35 and sm50 GENCODE targets which have long been deprecated and were causing issues with the latest NCCL release builds.
 * Improved NVLS/NVLSTree tuning prediction to improve algorithm and protocol selection.
 * NVLSTree Tuning Fixes. Update tuning data for H100, GB200-NV72.
 * Respond better to RoCE link flaps. Instead of reporting an “unknown event” it will now report “GID table changed”.
 * Move libvirt bridge interface to the end of possible interfaces so that they are considered last. These interfaces are usually virtual bridges to relay traffic to containers running on the host and cannot be used for traffic to a remote node and are therefore unsuitable.

## v2.28.7-1 (2025-10-18)

## GPU-Initiated Networking (GIN)
 * Provides device-side API for integrating GPU-Initiated Networking
   capability into application kernels.
 * New transport layer called DOCA GPUNetIO.
 * New ncclGin construct to create, destroy and manipulate GIN contexts.
 * New ncclGinBarrierSession to provide synchronization functionality.
 * New put, signal, counter operations for data movement and signaling.
 * GIN API signatures and functionalities are subject to change.
 * GIN Support Requirements
   * CUDA 12.2 or later when compiling the GPU code
   * NVIDIA GPUs: Volta or newer. NVIDIA GPU drivers >= 510.40.3
   * NVIDIA NICs: CX4 or newer. rdma-core >= 44.0
   * Requires nvidia-peermem or DMABUF support. When using DMABUF, linux
     kernel >= 6.1 is required.

## New ncclCommRevoke API for fault tolerance
 * Introduces ncclCommRevoke to quiesce ongoing NCCL work on a
   communicator without freeing resources.
 * This answers the need for a lightweight way to cancel in-flight
   collectives and bring a communicator to a safe state before
   split/shrink/finalize/destroy.
 * Includes optional cross-rank coordination (global barrier) and
   supports blocking/non-blocking usage.

## New NCCL Environment Plugin
 * The env plugin allows users to set NCCL environment variables, for
   example, after loading them from a centralized database.
 * The NCCL_ENV_PLUGIN variable can be used to let NCCL load an external
   environment plugin.

## New NCCL Examples on GitHub
 * The NCCL examples directory provides users and developers with
   practical code samples that highlight NCCL’s core features.
 * It covers basic operations like communicator initialization,
   point-to-point communication, and collective operations, as well as
   advanced features such as user buffer registration, symmetric memory,
   and the device API.

## Device API improvements
 * Adds ncclFindWindow API.
 * Adds new ncclBarrierSession to provide hybrid synchronization
   functionality.
 * Makes multimem available with as few as two ranks.
 * Removes distance (NCCL_P2P_LEVEL) considerations from determining the
   availability of symmetric memory.

## Enhanced NCCL RAS output
 * Extends RAS subsystem with JSON format to support machine-parsable
   metrics collection.
 * Enables structured data export for monitoring tools, dashboards, and
   automated analysis systems.

## Github Pull Requests resolved
 * Fast Init - CPU Optimizations for NCCL Initialization Large Scale.
   (PR https://github.com/NVIDIA/nccl/pull/1789)
 * Fast Init - Improve Bootstrap AllGather by 2x at large scale by
   sending bootstrap information bidirectionally. (PR https://github.com/NVIDIA/nccl/pull/1791)
 * Fixes spurious failures when PyTorch is statically linked with
   NCCL-2.28.3 because error is not drained, but rather gets propagated
   into the next CUDA kernel invocation. (PR https://github.com/NVIDIA/nccl/pull/1864)

## Other notable improvements
 * Fixes multicast object leaks in case of failed NVLS user buffer
   registrations, which could lead to crashes. Avoids such registration
   attempts in case of the use of incompatible memory allocators.
 * Fixes potential data corruption with built-in symmetric kernels for
   small messages with size granularity under 8 bytes or when multiple
   symmetric operations were aggregated in a group.
 * Generalizes the existing point-to-point scheduling to the case of
   un-even GPU count per node.
 * Fixes a crash when network plugin assignment fails.
 * Fixes a large performance issue with NCCL_CROSS_NIC=0 and certain
   split mask settings, where NCCL cannot find a viable ring.
 * Fixes crash when NCCL is compiled with recent CUDA versions but
   running on hosts with certain specific older CUDA drivers.

## v2.28.9-1 (2025-11-10)

## NCCL v2.28 Update 2 -

- Fix operation ordering between main thread and proxy thread to prevent hangs at large scale.
- Fix Issue https://github.com/NVIDIA/nccl/issues/1893, a bug fix in GIN.

## v2.29.2-1 (2025-12-24)

## Device API Improvements
 * Supports Device API struct versioning for backwards compatibility with future versions.
 * Adds ncclCommQueryProperties to allow Device API users to check supported features before creating a DevComm.
 * Adds host-accessible device pointer functions from symmetric registered ncclWindows.
 * Adds improved GIN documentation to clarify the support matrix.

## New One-Sided Host APIs
 * Adds new host APIs (ncclPutSignal, ncclWaitSignal, etc) for both network and NVL using zero-SM.
 * One-sided communication operation writes data from the local buffer to a remote peer’s registered memory window without explicit participation from the target process.
 * Utilizes CopyEngine for NVL transfer and CPU proxy for network. 
 * Requires CUDA 12.5 or greater.

## New Experimental Python language binding (NCCL4Py)
 * Pythonic NCCL API for Python applications - native collectives, P2P and other NCCL operations.
 * Interoperable with CUDA Python ecosystem: DLPack/CUDA Array Interface, and special support for PyTorch and CuPy.
 * Automatic cleanup of NCCL-managed resources (GPU buffers, registered buffers/windows, custom reduction operations).

## New LLVM intermediate representation (IR) support
 * Exposes NCCL Device APIs through LLVM IR to enable consumption by diverse code generation systems. 
 * Example usages include high-level languages, Just-In-Time (JIT) compilers, and domain-specific languages (DSL).
 * Build with EMIT_LLVM_IR=1 to generate LLVM IR bitcode.
 * Requires CUDA 12 and Clang 21.

## Built-in hybrid (LSA+GIN) symmetric kernel for AllGather
 * Adds a new hierarchical kernel using MCRing (NVLS multicast + Ring) to improve performance and scalability of AllGather.
 * Requires symmetric memory registration and GIN.

## New ncclCommGrow API
 * Adds the ability to dynamically and efficiently add ranks to an existing NCCL communicator.
 * Use ncclCommGrow with ncclCommShrink to adjust membership of communicators in response to failing and recovering nodes. 
 * Also addresses the need for elastic applications to expand a running job by integrating new ranks.

## Multi-segment registration
 * Expands buffer registration to support multiple segments of physical memory mapped to one contiguous VA space for the p2p, ib and nvls transports.
 * Enables support for expandable segments in PyTorch.

## Improves scalability of AllGatherV pattern
 * Adds support for a scalable allgatherv pattern (group of broadcasts).
 * Adds new scheduler path and new kernels to improve performance at large scale.

## Debuggability & Observability Improvements
 * RAS supports realtime monitoring to continuously track peer status changes.
 * Inspector adds support for Prometheus format output (with NCCL_INSPECTOR_PROM_DUMP=1), in addition to the existing JSON format.
 * Adds profiler support for CopyEngine(CE) based collectives.

## Community Engagement
 * Adds contribution guide: https://github.com/NVIDIA/nccl/blob/master/CONTRIBUTING.md
 * Adds NCCL_SOCKET_POLL_TIMEOUT_MSEC which allows waiting instead of spinning during bootstrap in order to reduce CPU usage. (Github PR #1759)
 * Fixes segfault in ncclGin initialization that can happen if ncclGinIbGdaki.devices() fails after init() succeeds. (Github PR #1881)
 * Fixes crash that can happen when calling p2p and then collectives while using the same user buffer. (Github Issue #1859)
 * Fixes bug that was lowering performance on some sm80 or earlier machines with one NIC per GPU. (Github Issue #1876)
 * Clears non-fatal CUDA errors so they do not propagate. ([Pytorch Issue #164402](https://github.com/pytorch/pytorch/issues/164402))

## Other Improvements
 * Improves performance of large-size AllGather operations using symmetric memory buffers on Blackwell by transparently switching to CE collectives.
 * Improves the default number of channels per net peer for all-to-all, send, and recv to achieve better performance.
 * Improves performance tuning of 256M-512M message sizes on Blackwell for AllReduce.
 * Enables built-in symmetric kernels only on fully connected nvlink systems, as PCIE systems do not perform as well.
 * Prints git branch and commit checksum at the INFO level during NCCL initialization.
 * Improves support for symmetric window registrations on CUDA versions prior to 12.1.
 * Relaxes symmetric buffer registration requirements for collectives so that users can leverage the symmetric kernels with only one of the buffers being registered, when possible.
 * All2all, send, recv now obey NCCL_NETDEVS_POLICY. For these operations, NCCL will now by default use a subset of available network devices as dictated by the Network Device Policy. 
 * Fixes a hang on GB200/300 + CX8 when the user disables GDR.
 * Fixes a bug that could cause AllReduce on ncclFloat8e4m3 to yield “no algorithm/protocol available”.
 * ncclCommWindowRegister will now return a NULL window if the system does not support window registration. 
 * More prominent error when cuMulticastBind fails and NCCL_NVLS_ENABLE=2.
 * Upgrades to doca gpunetio v1.1.

## Known Limitations
 * Since Device API was experimental in 2.28.x, applications that use the Device API in v2.28 may need modifications to work with v2.29. 
 * One-sided host APIs (e.g. ncclPutSignal) currently do not support graph capture. Future releases will add cuda graph support.
 * The improved AllGatherV support breaks the NCCL profiler support for ncclBroadcast operations, limiting visibility to API events. NCCL_ALLGATHERV_ENABLE=0 can be used as a workaround until it is fixed in a future release.
 * NCCL4Py (experimental) has a known issue with cuda.core 0.5.0. We currently recommend using cuda.core 0.4.1 with nccl4py.

## v2.29.3-1 (2026-02-03)

Fixes CAS usage in case of weak failure which was causing a hang on ARM. The issue affects NCCL when compiled with gcc versions prior to 10.

## v2.29.7-1 (2026-02-27)

## Device API & GIN Enhancements
 * Adds multi-context support for GIN with the option to request for exclusive GIN contexts.
 * Adds VA-based GIN signals plus strict window ordering.
 * Adds advanced queue control for GIN, including queue depth, manual credit management and aggregation.
 * Adds GIN support for platforms with no cross rail connectivity.
 * Adds nLsaTeams to ncclCommQueryProperties.
 * Decouples GIN from NET plugin and topology.

## New device APIs for convenience
 * Adds new device APIs for various device side operations.
 * Introduces Copy, ReduceCopy, ReduceSum with various data types and ops.

## Dynamic Memory Offload
 * Adds ncclCommSuspend() / ncclCommResume() for releasing/restoring communicator memory.
 * Adds basic memory overhead tracking infrastructure. 

## Built-in hybrid (LSA+GIN) symmetric kernel for ReduceScatter:
 * Adds new hierarchical kernels to improve performance and scalability of ReduceScatter.
 * Requires symmetric memory registration and GIN support.
 * Symmetric GIN kernels can be disabled with NCCL_SYM_GIN_KERNELS_ENABLE=0.

## Add support for Port Failover
 * Allows internal IB/RoCE plugin to continue working transparently when network errors occur.
 * Adds automatic port failover for GPUs having multiple local IB/RoCE ports/devices.
 * Can be enabled by setting NCCL_IB_RESILIENCY_PORT_FAILOVER=1.

## Symmetric memory improvements
 * Adds support for abort in symmetric kernels.
 * Adds NCCL_CHECK_MODE=DEBUG to validate symmetric buffers registration.

## Project layout reorganization
 * The `ext-*` directories are moved to `plugins` (e.g. `ext-net` → `plugins/net`).
 * `ir` and `nccl4py` are now under `bindings`.
 * `examples` is now `docs/examples`.

## Other Improvements
 * Uses different signals for different peers in the GIN barrier.
 * Adds NCCL_NO_CACHE to force NCCL to always re-read selected env vars.
 * Adds CMake install and find_package support.
 * Adds CMake for NCCL4Py build and updates Cybind integration.
 * Adds preliminary backwards compatibility support to enable running LSA kernels compiled with NCCL 2.29.2/3 on NCCL 2.29.7. This is not supported for GIN yet.

## Bug fixes
 * Fix problems related to the introduction of git_version.h. (Github Issue #1960)
 * Fix oneRankReduce when the number of elements is not a multiple of block number. (Github Issue #1950)
 * Improve GIN handling in ncclCommGetAsyncError. (Github Issue #2019)
 * Fix memory initialization in P2P transport. (Github Issue #1962)
 * Fix hang issue in send/receive scheduling of repeated sparse patterns. 
 * Fall back to cudaMemcpyAsync API when null/default stream is used for CE-based collective operations.
 * Free symmetric window objects automatically during commFree. 
 * Fix a 16-bit overflow of signal and counter ids with GIN proxy.
 * Reset GIN counters and signals upon ncclDevCommDestroy.
 * Fix local data calculation during ncclGinIbP2PBarrier.


## Other
 * Update license to Apache 2.0.

## Known Limitations
 * Applications that use GIN APIs need to be recompiled with 2.29.7 to work with 2.29.7 runtime. 
 * The Profiler Inspector example does not currently compile under CMake. This will be fixed soon.

## Acknowledgments
We thank the following contributors for their work on this release:
- @sphish, @LyricZhao for their contribution on improving the NCCL device API.
- @ruizhang1230, @Zhaojp-Frank, @guoyuhong, @argentea and the Amem project (https://github.com/inclusionAI/asystem-amem) for their contribution on dynamic memory offload.

We also thank the community for issue reports, testing, and feedback.

## v2.30.3-1 (2026-04-15)

## Device API and GIN Enhancements
* GIN contexts are no longer shared between device communicators backed by the same host communicator.
* Adds per-context resource sharing modes for GIN, allowing GPU-scope or CTA-scoped resource sharing.
* Adds TrafficClass support to device communicator. 
* Adds versioning to ncclDevComm.
* Adds timeout support to the device APIs.
* Adds max_rd_atomic and max_dest_rd_atomic support in GIN.
* Upgrades doca-gpunetio to v2.0.2-rc1

## Elastic Buffers (LSA support)
* Support new use cases where large tensors are split into multi-segment windows, with the active region in GPU memory and the remainder in host memory.
* Enables larger effective models and reduces memory pressure during spilling.
* Elastic buffers will support GIN in a future release. 

## gin.get with Nonblocking Flush (Experimental)
* Support GPU‑initiated gets and check completion without stalling.
* It currently only works with GDAKI (not with CPU proxy) and doesn't work on directNIC and Ampere. 

## Symmetric Memory Improvements
* Adds AVG operator to ReduceScatter Symmetric kernels.
* Enable dynamic memory offload with group support for single-process, multi-GPU scenarios.
* Adds support for GPU-only multi-segment registration for symmetric windows.
* Adds CUDA graph capture and replay support for ncclPutSignal and ncclWaitSignal APIs.
* One-sided RMA can now use an external network plugin.

## Tensor Memory Accelerator (TMA) Support
* Adds TMA support in select built-in symmetric kernels to offload bulk peer‑to‑peer copies and reductions, improving NVLink bandwidth and latency.
* Can be enabled with NCCL_SYM_TMA_ENABLE=1.

## DDP Support
* Enables Dynamic Direct Path (DDP) so that NCCL can take advantage of hardware multipath and out‑of‑order receive for higher network performance on supported systems.
* Can be enabled with NCCL_IB_OOO_RQ=1.

## Port Recovery
* Adds support for IB port recovery in NCCL.
* Improves NCCL’s ability to recover from transient network issues so communicators can continue operating without full re‑initialization.
* Can be enabled with NCCL_IB_RESILIENCY_PORT_RECOVERY=1.

## Cross Clique Support
* Add support for treating multiple cliques as the same NVLINK domain.
* Can be enabled with NCCL_MNNVL_CROSS_CLIQUE=1

## NCCL Parameter Infrastructure
* Adds new C APIs to support querying NCCL parameters. 
* Introduces ncclParamGetAllParameterKeys,ncclParamDumpAll, ncclParamGet and ncclParamGetParameter APIs. 

## NCCL4PY v0.2.0
* Adds new APIs from NCCL 2.29 release.
* Add devcomm create/destroy APIs to prepare for device API.
* Enables Freethreading support.

## Other Improvements
* Adds NCCL Inspector P2P event support.
* ncclGinBarrierSession can now be created directly for the world team without manual resource allocation.
* GIN proxy GFD size increased to 128 bytes with version field added.
* GIN proxy CQ polling (ginProgress) moved to per-context to improve performance.
* ncclBarrierSession no longer shares resources with ncclLsaBarrierSession or ncclGinBarrierSession.
* Redundant NCCL_DEBUG=INFO log volume reduced significantly.
* NVLSTree tuning that improves performance for various Blackwell systems.
* Adds p2pMaxPeers to communicator to achieve better tuning for send/recv vs. all2all.
* Enables LL128 protocol in heterogeneous scenarios for Hopper and later GPUs.
* Adds checks for mismatched Net and CollNet counts across communicators.
* Adds Graphana template for NCCL inspector dashboard rendering using Prometheus data.
* Removes unused members nccl_id, comm, nccl_unique_id, and thread_ranks in the examples (Github PR #1989).
* Adds NCCL_LIBIBVERBS_SO environment variable to specify an absolute path for libibverbs (Github PR #2043).
* Extends suspend memory offload to channel device allocations (Github PR #2060).

## Bug Fixes
* Fixes implicit CUDA synchronization in `putSignal` and `CE collectives` caused by pageable CPU stack memcpy. 
* Fixes a hang when using CE collectives and cuda graph under an edge case. 
* Fixes NULL access issue during finalize when RMA and GIN plugins are both initialized.  
* Fixes race conditions in all2all GIN/Hybrid examples with more than one CTA.
* Fixes `ncclGinType_t` uint8_t enum compatibility issue in nccl4py.
* Fixes several memory leaks in communicator create/destroy code paths. 
* Fixes a bug in plugin compat layer for v11 related to lazy initialization.
* Fixes data corruption in symmetric LL kernels with unaligned buffer.
* Fixes plugin name being cleared after communicator destroy (Github Issue #1978).
* Fixes deadlock and use-after-free in the inspector plugin (Github Issue #2000).
* Fixes incorrect network interface selection caused by inverted boolean logic in matchSubnet (Github PR #2047).
* Fixes regression from 2.29.2 where CPU affinity mask is not restored in initTransportsRank (Github issue #2033)

## Known Limitations
* Applications that use GIN APIs need to be recompiled with 2.30.3 to work with 2.30.3 runtime. 
* gin.get requires GDAKI and is not supported on Ampere or directNIC platforms.

## Acknowledgments
We thank the following contributors for their work on this release:

- @chenhengqi, @liangxs, @phu0ngng, @SreevatsaAnantharamu, @SongXiaoXi for your PRs. 
- @sphish, @LyricZhao for continued contribution on improving the NCCL device API.

We also thank the community for issue reports, testing, and feedback.


## v2.30.4-1 (2026-04-22)

Fixes the issue with extra headers for nccl_param feature. Github issue #2105
Added support for elastic buffer with GIN. 

## nccl4py-v0.2.0 (2026-04-24)

# Release Notes — nccl4py 0.2.0

This release adds Python bindings for the new NCCL 2.30 one-sided RMA, Device API (GIN), and elastic communicator features, along with substantially more control over communicator configuration.

## Highlights

- **One-sided RMA (point-to-point)** — New `Communicator.put_signal()`, `Communicator.signal()`, and `Communicator.wait_signal()` methods, plus a `WaitSignalDesc` helper for describing signal values and match operations.
- **NCCL Device API host side setup** — New `Communicator.create_dev_comm()` that produces a `DevCommResource` for use with device-side NCCL kernels. Configure the device communicator through the new `NCCLDevCommRequirements` class, and introspect support via `device_api_support`, `gin_type`, `railed_gin_type`, `host_rma_support`, and `n_lsa_teams` properties.
- **Device pointer access for registered windows** — `RegisteredWindowHandle` now exposes `user_ptr`, `get_lsa_device_pointer()`, `get_lsa_multimem_device_pointer()`, and `get_peer_device_pointer()` for direct access to LSA, multimem, and peer mappings.
- **Elastic and fault-tolerant communicators** — New `Communicator.grow()`, `revoke()`, `suspend()`, and `resume()` methods to support elastic topology changes and error-handling flows. `CommSuspendFlag` added alongside existing `CommShrinkFlag`.
- **More flexible construction** — In addition to `init()`, communicators can now be created with class method `init_all()` and instance method `initialize()`. `Communicator.get_mem_stat()` reports per-communicator memory statistics.

## Configuration

New tuning knobs on `NCCLConfig`:

- `graph_usage_mode`, `num_rma_ctx`, `max_p2p_peers`.

`NCCLDevCommRequirements` — passed to `Communicator.create_dev_comm()` to describe the resources and capabilities a device communicator needs:

- LSA: `lsa_multimem`, `barrier_count`, `lsa_barrier_count`, `rail_gin_barrier_count`, `world_gin_barrier_count`, `lsa_ll_a2a_block_count`, `lsa_ll_a2a_slot_count`.
- GIN: `gin_force_enable`, `gin_context_count`, `gin_signal_count`, `gin_counter_count`, `gin_queue_depth`, `gin_connection_type`, `gin_exclusive_contexts`.

## Device / topology introspection

New `Communicator` properties: `cuda_dev`, `nvml_dev`, `device_api_support`, `multimem_support`, `gin_type`, `railed_gin_type`, `n_lsa_teams`, `host_rma_support`.

## Other changes

- `CTAPolicy` is now an `IntFlag` (was `IntEnum`) so multiple policies can be combined.
- Interop submodules `nccl.core.cupy` and `nccl.core.torch` are now lazy-loaded via `__getattr__` and only imported on first attribute access, so `import nccl.core` no longer pulls in CuPy or PyTorch.


## v2.30.7-1 (2026-06-04)

## Zero-SM Collectives

- Adds hierarchical zero-SM collectives (AllGather and All2all) that use RMA CPU proxy for inter-node communication and Copy Engines for intra-node communication.
- Enables better overlap of compute and communication.
- Enable hierarchical zero-SM collectives with `NCCL_CTA_POLICY_ZERO` flag.

## GIN Enhancements

- Adds new experimental GPU Push Interface (GPI) backend for GIN.
- Adds explicit signal semantics with Strong and Weak signals.
- Adds proper `ncclGinFenceLevel` semantics for barriers.
- Adds separate `NCCL_GIN_IB_TC` toggle to control traffic class used by GIN.
- Adds `NCCL_GIN_RESOURCE_SHARING_THREAD` to enable more optimizations.
- Optimizes QP overhead, including GDAKI mode when counters are not used.
- Ensures GIN is usable when NIC fusion is enabled.
- Adds GIN plugin example in `plugins/gin/example`.

## Symmetric Memory Improvements

- Restructures RMA plugin architecture.
- Adds support for asymmetric buffer sizes during window registration.
- Optimizes ReduceScatter symmetric kernel performance.
- Optimizes performance for RMA operations using CE.
- Adds batched CE operations to improve performance in the RMA CE put/wait path.
- Adds support for window registration during CUDA graph capture.

## MPS with MLOPart Support (Experimental)

- NCCL now leverages CUDA feature Memory Locality Optimized Partition (MLOPart).
- Supports up to 2 ranks per physical GPU with MPS+mlopart.

## Other Improvements

- Adds support for IB ports that require global route headers (GRH).
- Adds logic to `gin.flush` to ensure all prior gets are visible.
- Adds makefile support to compile python wheels from source.
- Adds `NCCL_RMA_DISABLE` env to enable/disable RMA (Github PR #2151).
- Implements reset-without-zeroing for signals and counters in GIN (Github PR #2155).
- Pins GIN proxy thread to NUMA-local CPU set (Github PR #2182).
- Adds optimized weight transfer APIs in `contrib/nccl_xfer`.
- Adds custom kernels in `contrib/custom_algos` for alltoall and allreduce using NCCL Device API.
- Adds examples of Root Mean Square Normalization (RMSNorm), demonstrating the fusion of computation and communication using the device API.
- Unifies coding style by using clang-format. Please see `docs/dev_guide/nccl_coding_style.md` for more details.
- Drops support for v11 and v12 GIN plugin APIs.

## Bug Fixes

- Fixes a deadlock caused by cuda stream allocation under PXN when memseting a buffer at runtime.
- Reintroduce `cudaGridDependencySynchronize` in built-in symmetric kernels, ensuring that newly launched kernels cannot access memory modified by prior kernels before it reaches point of coherency.
- Ignores system headers in include/header processing, thereby avoiding excessive realpath calls in some builds (Github PR #1806).
- Improves QP load balancing on systems configured with RoCE LAG with the round-robin queue affinity policy (Github PR #2150).
- Fixes issue when receiving an external TCP request causes the proxy thread's `ncclProxyService` to hang (Github PR #1834).
- Fixes `rma_proxy` MR registration type for host-NUMA `cpuAccessSignals`, which ensures that the net plugin does not reject the registration due to wrong memory type (Github PR #2187).
- Fixes GIN init context leak (Github PR #2179).
- Fixes issue with one-sided host APIs when a custom GIN plugin is used.
- Fixes one-sided host API issue where requests are dropped at a high message rate (Github Issue #2119).

## Acknowledgements

We thank the following contributors for their work on this release:

@andrewjcg, @baymaxhuang, @bhasunit, @fishautumn, @mozarhua, @ngoyal2707, @wanglei875 for your PRs.

We also thank the community for issue reports, testing, and feedback.

## Known Issues

- NCCL one-sided host RMA APIs, e.g., `ncclPutSignal`, require every rank to call the API as a one-time initialization warm-up. This has been fixed on dev branch: https://github.com/NVIDIA/nccl/commit/e12963e1c7994e054c29df0994e8675ff4749875
- NCCL one-sided RMA operations have a possible corruption issue when multiple symmetric windows are carved from the same backing memory allocation. See https://github.com/NVIDIA/nccl/issues/2198. This has been fixed on dev branch. 
- Hang is possible when specific workload uses PXN (e.g. ncclSend/ncclRecv/All2all) and calls ncclCommDestroy() without waiting for all ranks to complete. This has been fixed on dev branch: https://github.com/NVIDIA/nccl/commit/08b3662c2181d55551d76f97caca497a467d1e84
- Hang is possible when workload uses 2-rank communicator and uses CE collectives. This has been fixed on dev branch: https://github.com/NVIDIA/nccl/commit/430afbcef0d0dbe4bac8de317cf4cedd50ffefa2

## nccl-ep-v0.1.0 (2026-06-08)

NCCL EP is a high-performance NCCL API extension for efficient Mixture-of-Experts (MoE) communication. It provides optimized dispatch and combine primitives for Expert Parallelism (EP) across distributed GPU systems implemented on top of NCCL Device API: Load-Store Accessible (LSA) and GPU-Initiated Networking (GIN) operations.

## API Improvements and Extensions

- Refactor the API signatures to improve user experience and support backward compatibility.
- Change the device memory ownership for EP Tensor data. The user is now responsible for device memory allocations for EP Tensors.
- Refactor the EP tensor data structure management for the host-side NCCL EP Tensor object. EP tensor now supports both dynamic allocation for long-term storage and static on-stack allocation for malloc-free usage on the data path.
- Add lightweight and CUDA Graph-compatible EP Handle management on the data path. `ncclEpCreateHandle` is split into `ncclEpInitHandle`, which is a control-path operation that may allocate device memory and may be collective, and `ncclEpUpdateHandle`, which updates the Handle's routing information before calling the Dispatch operation.
- Allow users to set the number of SMs used by NCCL EP.
- Extend the API to associate an NCCL EP Tensor with an NCCL Window to enable zero-copy optimizations.
- Add flexible Dispatch output layout configurations:
  - HT mode supports Flat and Expert-major layouts.
  - Enable users to provide expert padding to align with GEMM requirements.
  - LL mode supports Expert- and Rank-major layouts.
- Add active rank mask support to identify failed ranks and exclude them from future communication, allowing operation to continue instead of aborting the process.
- Introduce an explicit Forward/Backward pass selector in Dispatch and Combine operations.
- Drop top-K indices from the Dispatch operation signature and use the tensor provided to the Handle update.

## Implementation Improvements

- Migrate to Just-In-Time (JIT) compilation for HT mode. This addresses performance issues and a number of limitations. LL migration to JIT is planned in the next release.
- Add full Multi-node-NVLINK (MNNVL) support.
- Remove limitations on the number of ranks in an LSA team. This has been tested on NVLink72.
- Fully migrate to NCCL infrastructure. All CUDA IPC references are removed and the code only depends on NCCL.
- Enable CUDA Graph support through EP handle management API changes and implementation changes.
- Support MoE and prefill workloads by enabling a variable number of tokens per sender on Dispatch.

## Performance Optimizations

- Improve the performance of Dispatch for HT mode by leveraging NCCL Device API extensions available starting from NCCL v2.30.
- Improve the performance of the Combine operation in HT mode by leveraging JIT compilation.
- Enable zero-copy flows for HT mode.
- Optimize LL performance for NVLink-only configurations by avoiding the send-side staging buffer.
- Update `ep_bench` to measure kernel-only performance.
- Introduce `ncclTeamRail` in HT mode instead of a split communicator.
- Improve Dispatch/recv and Combine/send parallelization in LL mode.

## Memory Footprint Optimizations

- Optimize the Dispatch staging buffer in LL mode. Use per-rank token deduplication and rank-major layout to reduce the staging buffer size by a factor of experts per rank.
- Expose rank-major layout at the API level in LL mode. Rank-major mode reduces the memory footprint by a factor of the number of experts per rank.
- Optimize HT mode handle memory usage by moving the global routing map buffer from the handle to the group scope. This allows different handles to share the buffer.

## Python Bindings

- Expose NCCL EP through `nccl4py`.
- Make Python bindings more pythonic compared to the original 1-to-1 C-Python mapping.

## Performance Benchmark (`ep_bench`)

- Report kernel-only performance metrics through CUPTI, if available.
- Extend the number of settings: number of SMs, number of experts, and layout selection.
- Add sophisticated validation for Dispatch and Combine phases to detect memory corruption and routing issues.

## Bug Fixes

- Fix the bug in HT mode preventing launches on more than 8 nodes.
- Fix HT mode inter-node flags sizing that would cause overflow for 9 or more nodes.
- Clean the API and tools from quantization-related code. Quantization support is planned to be re-enabled in the following release.
- Fix memory ordering in Dispatch/Combine grid barriers.
- Fix a bug causing crashes in LL mode for batch sizes.
- Fix integer overflow in inter-node N2N warp at 8 or more nodes. Thanks to Mozar Huang.

## Known Issues and Limitations

- The number of RDMA domains, or NCCL LSA Teams, in HT mode is limited to 32 due to algorithmic limitations.
- `nccl4py` 0.3 wheel is shipped with `libnccl_ep.so` built with CUDA 13. To use CUDA 12, users have to build `libnccl_ep.so` from source and specify the `.so` file path using `LD_PRELOAD` or `LD_LIBRARY_PATH`. In addition, `NCCL_EP_HOME` needs to be set to point to the corresponding `nccl_ep` installation directory.
- NCCL EP v0.1 does not support quantization. While the API has appearances of quantization-related parameters, such as the scales tensor, the implementation was not tested and is not guaranteed to work. Elements of quantization support are expected to be introduced in the next release.
- The Dispatch operation has resource limitations associated with the amount of available shared on-chip memory. Consumption is impacted by two factors:
  - The hidden dimension of the token.
  - LSA team size, which is the size of the NVLink domain.
- If a job launch is aborted due to shared memory overflow, try to reduce the current stage or pipeline settings. In v0.1, this can only be done statically at build time: reduce the `HYBRIDEP_DISPATCH_NUM_OF_STAGES` and/or `HYBRIDEP_DISPATCH_NUM_OF_PIPELINES_PER_BLOCK` macro values in `hybridep_configs.cuh`, rebuild, and retry.

### LL Mode Limitations

- Maximum top-K: 9.
- Hidden dimensions: 2048, 2560, 4096, 5120, 6144, 7168, and 8192.

## Known Bugs

- In LL mode, `ep_bench` reports Combine verification failure when a batch size of 1 token is used.
- In LL mode, `ep_bench` reports Combine verification failures on 16 nodes and 64 GPUs for the batch size of 8K tokens.

## nccl4py-v0.3.1 (2026-06-11)

## Highlights

- Added `nccl.ep`, a Pythonic interface to `libnccl_ep.so` for expert
  parallel dispatch/combine workflows. The package exposes `Group`, `Handle`,
  `Tensor`, typed config dataclasses, `Algorithm`, `Layout`, `PassDir`, and the
  named input/output structs used by the NCCL EP API.
- Added `nccl.core.device.cute`, enabling CuTeDSL kernels to call NCCL device
  APIs.
- Added top-level stack diagnostics with `nccl.get_version()` and
  `nccl.show_versions()`, reporting `nccl4py`, `libnccl.so`, and
  `libnccl_ep.so` versions, CUDA build variants, and loaded shared-library
  paths.
- Added free-threaded CPython support.

## New Features

### NCCL EP Python API

- New `nccl.ep` package provides Pythonic access to the NCCL EP extension
  library.
- `Group.create()` creates EP groups from a `Communicator` and `GroupConfig`;
  `Group.create_handle()` creates handles with an explicit `Layout`.
- `Handle` supports `update()`, `dispatch()`, `combine()`, `complete()`, and
  `destroy()`.
- `DispatchInputs`, `DispatchOutputs`, `CombineInputs`, `CombineOutputs`, and
  `LayoutInfo` provide named containers for the tensors and metadata used by
  dispatch, combine, and handle setup.
- `Tensor` resolves Python buffers into `ncclEpTensor_t` descriptors.
- `GroupConfig`, `HandleConfig`, `DispatchConfig`, `CombineConfig`, and
  `AllocConfig` expose typed configuration objects.
- `AllocFn` and `FreeFn` expose caller-controlled EP allocation hooks.
- `nccl.ep.interop.torch.get_nccl_comm_from_group()` provides PyTorch interop
  for creating an NCCL communicator from a PyTorch process group's rank and
  world-size information.
- Importing `nccl.ep` sets default `NCCL_EP_HOME` when bundled EP JIT headers
  are present, and `NCCL_HOME` when NCCL public headers are available from the
  installed `nvidia.nccl` package.
- `nccl.ep` checks that the loaded `libnccl.so` and `libnccl_ep.so` were built
  with the same CUDA major version. CUDA minor differences are accepted.

### Communicator Configuration

- Added `graph_stream_ordering` to `NCCLConfig`.

### Device API and CuTe DSL

- New `nccl.core.device.cute` module exposes the NCCL device API to CuTeDSL
  kernels, including communicator/window access, GIN primitives, barrier
  operations, and typed structs.
- Added `bindings/nccl4py/examples/cute/main.py`, a GIN put/wait example with
  host-side validation.
- Added `gin_strong_signals_required` and `gin_va_signals_required` to
  `NCCLDevCommRequirements` for configuring device communicator requirements.
- Added `NcclGinType.GPI` for the GPU-Push Interface transport.

### Version and Diagnostics API

- Top-level `nccl.get_version()` returns a `VersionInfo` dataclass containing
  the `nccl4py` package version plus `LibraryInfo` entries for the loaded
  `libnccl.so` and, when available, `libnccl_ep.so`.
- Top-level `nccl.show_versions()` prints the same stack information in a
  human-readable version block.
- Direct library probes are available for each native library:
  `nccl.core.get_lib_version()` and `nccl.core.get_lib_path()` report the
  loaded `libnccl.so`; `nccl.ep.get_lib_version()` and
  `nccl.ep.get_lib_path()` report the loaded `libnccl_ep.so`.
- Each `LibraryInfo` includes release version, CUDA build variant, and loaded
  shared-library path.

### Installation and Packaging

- CuTeDSL support can be installed through the CUDA-specific extras:
  `nccl4py[cu12]` installs `nvidia-cutlass-dsl>=4.5.2,<5.0`, and
  `nccl4py[cu13]` installs `nvidia-cutlass-dsl[cu13]>=4.5.2,<5.0`.
- Wheels include package data for `nccl/ep/lib/libnccl_ep.so` plus EP JIT
  headers. The bundled `libnccl_ep.so` is built with CUDA 13, regardless of
  whether the `cu12` or `cu13` extra is installed. Users who want to use a
  CUDA 12 build of `libnccl_ep.so` must provide that library themselves, for
  example through `LD_PRELOAD` or `LD_LIBRARY_PATH`.
- Wheels are available for free-threaded CPython 3.14t.

### Examples and Documentation

- Added Python examples for:
  - multiple devices in one process:
    `docs/examples/01_communicators/01_multiple_devices_single_process/python/`;
  - one device per MPI process:
    `docs/examples/01_communicators/03_one_device_per_process_mpi/python/`;
  - point-to-point ring pattern:
    `docs/examples/02_point_to_point/01_ring_pattern/python/`;
  - allreduce: `docs/examples/03_collectives/01_allreduce/python/`;
  - user-buffer allreduce:
    `docs/examples/04_user_buffer_registration/01_allreduce/python/`;
  - symmetric-memory allreduce:
    `docs/examples/05_symmetric_memory/01_allreduce/python/`;
  - symmetric-memory allgather:
    `docs/examples/05_symmetric_memory/02_allgather/python/`.
- Added nccl4py documentation under `docs/userguide/source/nccl4py/`, with the
  main entry point at `docs/userguide/source/nccl4py.rst`.

## Breaking Changes

### Removed APIs

- `nccl.core.group_simulate_end()` has been removed. Use
  `nccl.core.group_end(simulate=True)`:

  ```python
  from nccl.core import group_end, group_start

  group_start()
  # enqueue operations
  info = group_end(simulate=True)
  ```

- `NCCL_SPLIT_NOCOLOR` has been removed from the public constants. Use
  `color=None` when a rank should opt out of `Communicator.split()`.

### Deprecated APIs

- `nccl.core.get_version()` remains available, but is deprecated. Use top-level
  `nccl.get_version()` for structured version information, or
  `nccl.show_versions()` for human-readable output.

### Other Compatibility Notes

- Public NCCL enum wrappers are pure-Python `IntEnum` or `IntFlag` classes.
  Integer compatibility is preserved, and dtype conversion remains supported.
  Code that depends on binding-backed enum class identity from earlier releases
  may need updates.
- Enum members now follow the Python enum convention of `UPPER_SNAKE_CASE`
  names, such as `CTAPolicy.DEFAULT`, `CommShrinkFlag.ABORT`,
  `WindowFlag.COLL_SYMMETRIC`, and `NcclCommMemStat.GPU_MEM_TOTAL`. The
  previous PascalCase/camelCase aliases, such as `CTAPolicy.Default` and
  `NcclCommMemStat.GpuMemTotal`, still work in 0.3.1 for compatibility, but
  will be removed in a future release. New code should use the uppercase names.

## Fixes and Enhancements

- Fixed pointer lifetime handling for non-blocking communicator and window
  initialization.
- Torch interop covers `torch.uint32` and `torch.uint64` when those dtypes are
  available.

## API Stability

- `nccl.ep` and `nccl.core.device.cute` are initial API support. Their public
  interfaces may change in future releases as the NCCL EP and CuTeDSL device
  API integration matures.

## nccl4py-v0.4.1 (2026-08-11)

## Highlights

- Added host APIs for NCCL teams, rank translation, and device resource configuration.
- Expanded the experimental CuTe DSL device API with additional GIN operations, resource addressing, and direct support for host-created resources.
- Added live NCCL parameter access and improved version reporting.

## New Features

### Teams and Device Resources

- Added APIs for inspecting communicator teams, translating ranks, and configuring resources for device-side communication.

  **APIs:**
  - `NCCLTeam`
  - `Communicator.team_world`, `Communicator.team_lsa`, `Communicator.team_rail`
  - `Communicator.team_rank_to_world()`, `Communicator.team_rank_to_lsa()`
  - `NCCLDevCommRequirements.teams`, `NCCLDevCommRequirements.resources`
  - `NCCLDevCommRequirements.gin_traffic_class`
  - `TeamRequirement`
  - `LsaBarrierRequirement`, `GinBarrierRequirement`, `LLA2ARequirement`
  - `MultimemHandle`, `LsaBarrierHandle`, `GinBarrierHandle`, `LLA2AHandle`
  - `DevCommResource.multimem_handle()`, `DevCommResource.resource_handles`
  - `RegisteredWindowHandle.get_multimem_device_pointer()`

### CuTe DSL Device API

- Added device-side rank translation, resource addressing, and additional GIN operations.

  **APIs:**
  - `DevComm.team_rank_to_world()`, `DevComm.team_rank_to_lsa()`
  - `DevComm.resource_buffer_local_pointer()`
  - `DevComm.resource_buffer_lsa_pointer()`
  - `DevComm.resource_buffer_peer_pointer()`
  - `DevComm.resource_buffer_multimem_pointer()`
  - `DevComm.resource_buffer_lsa_multimem_pointer()`
  - `Window.multimem_pointer()`, `Window.lsa_multimem_pointer()`
  - `Gin.put_value()`, `Gin.get()`, `Gin.signal()`, `Gin.flush()`
  - `Gin.read_signal()`, `Gin.reset_signal()`, `Gin.signal_shadow_pointer()`
  - `Gin.read_counter()`, `Gin.wait_counter()`, `Gin.reset_counter()`
  - `GIN_ALL_CONTEXTS`
  - `ThreadScope`, `GinResourceSharingMode`
  - `DevComm.gin(..., resource_sharing_mode=...)`
  - `opt_flags` support for `Gin.put()`, `Gin.put_value()`, `Gin.get()`, and `Gin.signal()`

- Host-created device communicators, registered windows, multimem handles, and LSA/GIN barrier handles can now be passed directly as arguments to `@cute.jit` functions.

### Runtime Inspection

- Added live NCCL parameter access and consolidated version reporting under `nccl.core`.

  **APIs:**
  - `nccl.core.params`
  - `nccl.core.dump_params()`
  - `nccl.core.get_version()`
  - `nccl.core.show_versions()`

## Examples and Documentation

- Added [CuTe DSL examples](https://github.com/NVIDIA/nccl/tree/nccl4py-v0.4.1/bindings/nccl4py/examples/cute) covering teams, LSA all-reduce, multimem, GIN operations, barriers, and resource buffers.

## Breaking Changes

- `nccl.ep` is no longer included in nccl4py. The NCCL EP Python bindings are now distributed separately from the [NVIDIA/nccl-extensions](https://github.com/NVIDIA/nccl-extensions) repository.
- Version helpers are no longer exported from the `nccl` namespace. Import them from `nccl.core`.
- Version reporting was consolidated:
  - `nccl.core.get_version()` now returns `VersionInfo`.
  - `nccl.core.Version`, `get_lib_version()`, and `get_lib_path()` were removed.
  - `VersionInfo.nccl` was renamed to `VersionInfo.libnccl`.
  - `VersionInfo.nccl_ep` was removed.
  - `VersionInfo.nccl_bindings` was added.

## Fixes and Enhancements

- Fixed the default release semantics of `Gin.put()`.
- Improved NCCL parameter error handling and string decoding.

## Compatibility Notes

- The top-level `nccl` Python package is now a PEP 420 namespace package.
- The CuTe DSL device API remains experimental.
- The selected `libnccl_device.bc` must exactly match the NCCL version used by the bindings; nccl4py does not perform this check automatically.
- When one thread manages multiple local ranks, call `Communicator.finalize()` within `nccl.core.group()`.

## Known Issues

- The following CuTe DSL APIs require NCCL 2.31:
  - `Gin.get()`
  - `gin_session()`, `world_gin()`, `rail_gin()`, `hybrid_session()`, `world_hybrid()`
- CuTe DSL JIT compilation with CUDA 12 fails for kernels using the following APIs. CUDA 13 is not affected.

  **Affected APIs:**
  - `Gin.put()`, `Gin.put_value()`, `Gin.get()`, `Gin.signal()`, `Gin.flush()`
  - `GinBarrierSession.sync()`, `BarrierSession.sync()`

## v2.31.2-1 (2026-08-11)

## Compute Fabric Transport (CFT)

- Adds CFT host and device APIs for registering window memory with CUDA logical endpoints and issuing device-side Put, Get, Red and NVLS operations.
- CFT is supported on Blackwell GPUs with CUDA toolkit 13.3 or later.

## Per-Collective Configuration and Tuning

- Adds new `ncclCollConfig_t` and `nccl*Config` APIs for all collectives, with a vendor-defined field to make it easier for custom forks to integrate.
- Supports per-collective algorithm selection, CTA/CGA size and CTA policy overrides.
- Leverages `collConfig` to add `userTag` in profiler API. Motivated by community RFE https://github.com/NVIDIA/nccl/issues/1916.

## GIN Enhancements

- AWS-EFA team contributed the EFA GDA backend for GIN Put, Signal, and Flush operations (Github PR #2273).
- Adds per-DevComm GIN backend selection, allowing users to create multiple DevComms with different backends.
- Supports connecting GIN with custom strides.
- Adds device-side timeouts to blocking GIN APIs such as Flush, Wait, WaitSignal, and WaitCounter operations.
- Reduces QP usage when using railed GIN.
- Reduces file-descriptor consumption in GDAKI when using many QPs.
- Optimizes error reporting in GDAKI via event-based CQ error reporting.
- Add support for out-of-order delivery (DDP) in GDAKI on SPCX, improving performance without impacting GIN correctness guarantees.
- Adds GRH support and automatic path-MTU discovery to the GIN GDAKI backend.

## Parallel Aggregated Tree (PAT) Enhancements

- Enhances the PAT algorithm for ReduceScatter/AllGather by adding hierarchical kernels that use NVLS within the node and PAT across nodes.
- Enables better small/medium message performance.
- Disabled by default. Use `NCCL_ALGO=PAT`, or the `collConfig` API to enable.

## One-Sided RMA and Copy Engine Collectives

- Adds support for multiple contexts and multiple signals to one-sided RMA operations, allowing one-sided RMA traffic from a single rank to use multiple NICs.
- Leverage multiple contexts and signals for hierarchical 0-SM AllGather and AllToAll.
- Optimizes small message latency by using NVLink multicast for AllGather.

## Tuning and Cost Model

- Introduces a new unified cost model interface for querying the cost estimate for both legacy and device-API-based kernels.
- On Blackwell, TMA kernels are now enabled by default and integrated in the cost model for symmetric registered memory.

## Diagnostics and Profiling

- Adds NCCL RAS Diagnostics checks through `NCCL_RUN_RAS_DIAGNOSTICS=1` or RAS client, including GPU inventory, CUDA driver versions, ECC errors, NVLink state, and `NCCL_*` environment consistency checks.
- Adds NCCL Diagnostics through `NCCL_RUN_DIAGNOSTICS=1`, including active P2P connectivity check and actionable P2P remediation guidance.
- Kerne-channel profiling moved to a dedicated per-communicator thread, extending kernel timing to proxy-less NVLink/SHM and graph-captured collectives.
- Profiler V7 exposes per-kernel `initial_sync`, `compute` and `final_sync` phase events and symmetric-kernel variant metadata.
- Adds per-QP CPU WQE post-to-poll latency monitoring for the IB transport.

## Other Improvements

- Adds backward compatibility support for applications that JIT-compile NCCL Device API code.
- Adds support for LTO IR for NCCL device API.
- Reduces communicator host-memory use and topology initialization time on large systems by allocating topology paths according to their actual lengths.
- Adds multiple GIN proxy progress threads with per-thread endpoint assignment through `GIN_PROXY_NTHREADS` (Github PR #2279).
- Improves GIN host-proxy throughput by processing multiple GIN operations per progress iteration (Github PR #2232) and adding hints to the RMA plugin to aggregate requests (Github PR #2254).
- Adds CuTeDSL bindings for GIN Get, Flush, Signal, ReadSignal, and PutValue operations (Github PR #2266).
- Adds an internal CUDA 13.3 DMA-BUF mmap backend for GDRCopy.
- Adds event-based load balancing for the `net_ib` transport.
- Refreshes local GIDs after `IBV_EVENT_GID_CHANGE` events during IB port recovery.
- Updates the RMA plugin interface to v15 (Github PR #2254).
- Improves AMD EPYC topology modeling (Github PR #2036).
- Improves algorithm selection on newer Intel CPUs.
- Makes `nccl_device.h` compatible with C99 host translation units.

## Bug Fixes

- Fixes a hang when PXN connection initialization races with communicator teardown.
- Fixes data corruption when multiple symmetric windows are carved from the same backing memory allocation (Github Issue #2198).
- Fixes a hang during the first Copy Engine collective on a two-rank communicator (Github Issue #2241).
- Fixes NIC/GPU assignment perf regressions by limiting consistent start-NIC selection to Blackwell systems with ConnectX-8.
- Fixes missing GIN signal and counter requirements when Device API communicators are created asynchronously (Github PR #2208).
- Fixes a memory leak when Device API communicator creation fails (Github PR #2225).
- Fixes an incorrect GIN context count reported to applications when the allocated context count is rounded up (Github PR #2301).
- Fixes a resource leak when GIN connection setup fails (Github PR #2206).
- Fixes the CUDA thread capture mode remaining changed when GIN setup fails (Github PR #2229).
- Fixes inconsistent NVLS enablement when multiple ranks share a GPU (Github PR #2257).
- Fixes valid communicator configurations being rejected when only one of `minCTAs` or `maxCTAs` is set (Github PR #2256).
- Fixes communicator initialization failures on multi-system and MNNVL topologies when `NCCL_P2P_PXN_LEVEL=1` (Github PR #2258).
- Fixes a Device API `loadConst` performance regression caused by `__ldg`.
- Fixes CuTeDSL GIN barrier initialization failures caused by under-aligned by-value arguments (Github PR #2243, Issue #2242).

## Contrib/ Updates

- Adds PACE, a parallelism-aware collective engine that fuses layout conversion, data-type conversion, and scatter/gather operations into collective kernels (Github PR #2319).
- Adds experimental `nccl4rust` host and Device API bindings using LTO IR.
- Adds NIIN, a header-only NVSHMEM-compatible interface implemented with NCCL Device API primitives.
- Adds community-contributed architecture learning guides for communicator initialization, topology, tuning, transports, and collective execution (Github PR #2081).
- Adds a community-contributed analysis of DeepEPv2.

## Acknowledgements

We thank the following contributors for their work on this release:

@akkart-aws, @alpha-baby, @anshumang, @baymaxhuang, @bhasunit, @dboyan, @EylonKrause, @Gaojiaqi, @hershys-aws, @mozarhua, @rauteric, @tianhao909, @voipmonitor, @wanglei875, @Xuan-1998, @yongxiangren for your PRs.

We thank the AWS EFA team for their optimizations to GIN CPU Proxy and for adding EFA GDA backend in GIN.

We also thank the community for issue reports, testing, and feedback.

## Known Issues

- PAT + NVLS has performance regressions on H100 platforms. This will be fixed in the next release.
- B40 symmetric TMA kernels: On B40 GPUs, TMA-based symmetric kernels can exceed available shared memory and fail with an illegal memory access. Set `NCCL_SYM_TMA_ENABLE=0` to disable these kernels.
- B100 PCIe MLoPart: Multi-rank-per-GPU workloads using MPS MLoPart on B100 PCIe systems can fail during memory allocation with CUDA error 101 (`invalid device ordinal`). Set `NCCL_CUMEM_ENABLE=0` as a workaround.

## nccl4py-v0.5.0 (2026-09-01)

## Highlights

- Added host and CuTe DSL APIs for CFT setup and logical-endpoint addressing.
- Added per-collective configuration for algorithm selection, CTA tuning, profiler tags, and vendor options.
- Added communicator capability inspection and support for new NCCL 2.31.2 GIN features.
- Added compile-only CuTe DSL arguments for compiling kernels before creating NCCL resources.

## New Features

### Per-Collective Configuration

- Added per-call configuration to all collective operations.

  **APIs:**
  - `NCCLCollConfig`
  - `VendorOption`
  - The `config` argument on `Communicator.allreduce()`, `broadcast()`, `reduce()`, `allgather()`, `reduce_scatter()`, `alltoall()`, `gather()`, and `scatter()`

### Compute Fabric Transport Setup

- Added APIs for configuring CFT resources, querying CFT teams, and resolving logical endpoint addresses. CFT communication and barrier operations are not yet exposed.

  **Host APIs:**
  - `NcclHostCftMode`, `NcclCftTeamMode`, `NcclCftCap`
  - `NCCLConfig.host_cft_mode`
  - `NCCLDevCommRequirements.cft_caps`, `NCCLDevCommRequirements.cft_barrier_count`
  - `Communicator.team_cft()`, `Communicator.team_cft_multimem`
  - `CftLeInfo`
  - `RegisteredWindowHandle.get_cft_le_info()`
  - `RegisteredWindowHandle.get_peer_le_info()`
  - `RegisteredWindowHandle.get_multimem_le_info()`

  **CuTe DSL APIs:**
  - `CftTeamMode`, `CftLeInfo`
  - `DevComm.team_cft()`, `DevComm.team_cft_multimem`
  - `Window.cft_le_info()`, `Window.peer_le_info()`, `Window.multimem_le_info()`
  - `DevComm.resource_buffer_cft_le_info()`
  - `DevComm.resource_buffer_peer_le_info()`
  - `DevComm.resource_buffer_multimem_le_info()`

### Communicator and GIN Capabilities

- Added consolidated communicator property inspection and support for new NCCL 2.31.2 configuration and GIN capabilities.

  **APIs:**
  - `NCCLCommProperties`, `Communicator.properties`
  - `NCCLConfig.launch_order_implicit`
  - `NCCLConfig.num_rma_sig`
  - `NCCLConfig.rma_eager_init`
  - `NCCLDevCommRequirements.gin_type`
  - `NCCLDevCommRequirements.gin_custom_stride`
  - `NcclGinType.EFA_GDA`
  - `NcclGinConnectionType.CUSTOM_STRIDE`
  - `GinBackendMask.EFA_GDA`

### Compile Before Creating NCCL Resources

- Added type-only arguments for compiling CuTe DSL kernels before communicators, windows, or device resources are created.

  **APIs:**
  - `nccl.core.device.cute.runtime.make_fake_dev_comm()`
  - `nccl.core.device.cute.runtime.make_fake_window()`
  - `nccl.core.device.cute.runtime.make_fake_multimem_handle()`
  - `nccl.core.device.cute.runtime.make_fake_lsa_barrier_handle()`
  - `nccl.core.device.cute.runtime.make_fake_gin_barrier_handle()`

## Examples and Documentation

- Added a [compile-before-resource-creation example](https://github.com/NVIDIA/nccl/blob/nccl4py-v0.5.0/bindings/nccl4py/examples/cute/07_compile_with_fake_args.py) and renamed the introductory CuTe DSL example to `00_basic.py`.
- See the complete [CuTe DSL example suite](https://github.com/NVIDIA/nccl/tree/nccl4py-v0.5.0/bindings/nccl4py/examples/cute).

## Fixes and Enhancements

- Registered window handles created within `nccl.core.group()` are now updated correctly after the group completes.

## Compatibility Notes

- The nccl4py 0.5.0 host-side bindings and CuTe DSL API are generated from NCCL 2.31.2 headers.
- When using the CuTe DSL API, use the matching NCCL 2.31.2 `libnccl.so` and `libnccl_device.bc`; nccl4py does not verify this automatically.
- The CuTe DSL device API remains experimental.

## Known Issues

- The NCCL 2.31.2 device IR may fail to JIT-compile `Gin.put()` when EFA GDA is enabled. Apply [this patch](https://github.com/NVIDIA/nccl/commit/60ffa5cdd047b517e1818e0d011e48a52fd43c7e) to NCCL 2.31.2 and rebuild `libnccl_device.bc`.

## nccl4py-v0.6.0 (2026-09-23)

## Highlights

- Added experimental CuTe DSL ReduceCopy APIs for LSA, multimem, and local memory operations.
- Added NCCL 2.32 host APIs for collective launch completion events, NVLS configuration, CFT capability inspection, and window registration.
- Added explicit CuTe DSL barrier-session teardown and corrected `ThreadScope.THREAD` to match libcu++.

## New Features

### Collective Launch Completion Events

- Added per-collective CUDA launch completion events through `NCCLCollConfig`.

  **APIs:**
  - `NCCLCollConfig.launch_completion_event`
  - `NcclEventSpec`

### NCCL 2.32 Configuration and Capability Inspection

- Added host-side NVLS configuration, CFT capability reporting, and specialized window registration flags.

  **APIs:**
  - `NCCLConfig.nvls_host_mode`
  - `NcclNvlsHostMode`
  - `NCCLCommProperties.cft_support`
  - `NCCLCommProperties.cft_multicast_support`
  - `NCCLCommProperties.cft_counted_support`
  - `WindowFlag.GIN_ONLY`
  - `WindowFlag.CFT_COUNTED`

### CuTe DSL ReduceCopy

- Added device APIs for reduction and copy operations across LSA windows, multimem pointers, and local tensors.

  **APIs:**
  - `lsa_reduce_sum()`, `multimem_reduce_sum()`
  - `lsa_copy()`, `multimem_copy()`
  - `lsa_reduce_sum_copy()`, `multimem_reduce_sum_copy()`
  - `local_reduce_sum_copy()`

### CuTe DSL Barrier Lifecycle

- Added explicit session destruction so barrier handles and indexes can be safely reused.

  **APIs:**
  - `LsaBarrierSession.destroy()`
  - `GinBarrierSession.destroy()`
  - `BarrierSession.destroy()`

## Examples and Documentation

- Added [`08_reduce_copy.py`](https://github.com/NVIDIA/nccl/blob/nccl4py-v0.6.0/bindings/nccl4py/examples/cute/08_reduce_copy.py), demonstrating an LSA reduction across registered windows.

## Breaking Changes

- `ThreadScope.THREAD` now has the libcu++ numeric value `10` instead of `3`. Code using the enum member requires no changes; code storing or passing its raw integer value must be updated.
- CuTe DSL barrier sessions must call `destroy()` exactly once after their final operation. Every thread in the session’s cooperative group must call it from uniform control flow.

## Fixes and Enhancements

- The NCCL 2.31.2 device IR issue reported in nccl4py v0.5.0, which could prevent `Gin.put()` from JIT-compiling with EFA GDA enabled, is resolved in the matching NCCL 2.32.3 IR.
- Added a `py.typed` marker so compatible static type checkers can use `nccl.core` annotations.

## Compatibility Notes

- The nccl4py 0.6.0 host-side bindings and CuTe DSL API are generated from NCCL 2.32.3 headers.
- When using the CuTe DSL API, use matching NCCL 2.32.3 `libnccl.so` and `libnccl_device.bc`; nccl4py does not verify this automatically.
- `NCCLCollConfig.launch_completion_event` requires a timing-disabled, non-interprocess CUDA event. Every rank must either provide an event or omit it. CUDA 12.3 or later is required for post-launch recording semantics.
- The CuTe DSL device API remains experimental.

## v2.32.3-1 (2026-09-17)

 ## Vera Rubin Support

  - Adds initial Rubin platform support including support for sm107, CX9 rail and plane detection, and MPS+MLoPart.
  - 2.32.3 focuses on new functionalities and does not contain performance model tuning for Rubin. This will be part of the next release to improve out-of-box experience for Rubin users.

  ## Device API Enhancements

  - Adds Compute Fabric Transport (CFT) counted-write and wait support.
  - Adds socket-based GIN support, enabling custom kernel development with TCP sockets.
  - Adds support in GDAKI for LAG-aware QP assignment based on the context ID. ([Github PR #2315](https://github.com/NVIDIA/nccl/pull/2315))
  - Adds NCCL_WIN_GIN_ONLY so users can register a window only for GIN usage.
  - Optimize GIN performance by skipping mcst operation when possible.

  ## Collectives and Runtime Enhancements

  - Adds a ring-based hierarchical copy-engine AllGather implementation selectable with NCCL_HIER_CE_COLL_AG_RAIL_RING_ENABLE. ([Github PR #2299](https://github.com/NVIDIA/nccl/pull/2299))
  - Improves Blackwell symmetric AllGather performance, resource overhead modeling and kernel selection with a new cost model.
  - Adds optional TLS encryption for NCCL-owned socket traffic when NCCL is built with OpenSSL3, configured through the ncclSetEncryption API.
  - Adds ncclCollConfig_t::launchCompletionEvent, allowing callers to observe kernel-launch completion.
  - Adds ncclNvlsHostMode_t to ncclConfig_t so applications can disable host NVLS collectives per communicator.
  - Optimizes NVLS slot consumption to avoid resource exhaustion issues when using multiple communicators with NVLS.

  ## Diagnostics and Profiling

  - Adds the ATTN log level for important non-fatal conditions, such as configuration fallbacks and plugin initialization failures.
  - Expands RAS capability with GPU-resident progress counters and a watchdog DMA mirror for diagnosing stalled collective kernels.
  - Adds additional RAS diagnostics functionalities for NVLink/NIC state and speed, PCI and GDR configuration, Xid/SXid events and others.
  - Reports degraded NVLink fabric bandwidth with an ATTN message during communicator initialization.
  - Reports mismatched NCCL Git revisions across communicator ranks during initialization.

  ## Other Improvements

  - Fixes PAT+NVLS performance drops on H100 platforms.
  - Avoid address space exhaustion when repeatedly registering symmetric windows backed by a single physical memory allocation.
  - Reduces communicator initialization overhead at large scale by avoiding scans of inactive proxy poll descriptors.
  - Adds an experimental built-in NetworkDirect transport on Windows, with automatic socket fallback.
  - EFA team improved EFA GDA support with gin.get API and others. ([Github PR #2382](https://github.com/NVIDIA/nccl/pull/2382))([Github PR #2398](https://github.com/NVIDIA/nccl/pull/2398))([Github PR #2405](https://github.com/NVIDIA/nccl/pull/2405))
  - Reports Inspector ring-buffer drops and operation counts in JSON. ([Github PR #2304](https://github.com/NVIDIA/nccl/pull/2304))
  - NCCL now supports communicators using multiple MIG instances.
  - Generates  llms.txt for agents to better read NCCL documentation.

  ## Bug Fixes

  - Fixes profiler overhead when no profiler plugin is loaded. ([Github Issue #2355](https://github.com/NVIDIA/nccl/issues/2355))
  - Fixes P2P IPC registration reuse producing out-of-bounds remote addresses when a registered allocation spans multiple cuMem segments. ([Github PR #2362](https://github.com/NVIDIA/nccl/pull/2362))
  - Fixes PAT connection-setup deadlocks when runtime connection is disabled and nodes have uneven local-rank counts. ([Github Issue #2385](https://github.com/NVIDIA/nccl/issues/2385))
  - Fixes non-thread-safe token parsing that could corrupt concurrent configuration parsing. ([Github Issue #2361](https://github.com/NVIDIA/nccl/issues/2361))
  - Fixes B40 TMA symmetric kernels crash due to insufficient shared memory.
  - Fix GIN GDAKI bug related to hop limit when using DOCA SDK.
  - Fixes GIN Proxy and GPI descriptor shared-memory sizing and alignment.
  - Fixed CFT window registration performed before ncclDevCommCreate.
  - Fixes profiler API events reporting rank 0 instead of the originating communicator rank. ([Github Issue #2300](https://github.com/NVIDIA/nccl/issues/2300))
  - Fixes tuner plugins receiving uninitialized cost-model constants after the tuning rework.

  ## Contrib/ Updates

  - Adds more functionality in NiiN.
  - Fixes contrib/nccl_checkpoint rejecting otherwise compatible NCCL versions. ([Github Issue #2347](https://github.com/NVIDIA/nccl/issues/2347))

  ## Acknowledgements

  We thank the following contributors for their work on this release:

  [@madeleineth](https://github.com/madeleineth), [@alpha-baby](https://github.com/alpha-baby), [@akkart-aws](https://github.com/akkart-aws), [@anshumang](https://github.com/anshumang), [@cesar-stuardo-bd](https://github.com/cesar-stuardo-bd), [@hexagonal-banana](https://github.com/hexagonal-banana),
  [@rauteric](https://github.com/rauteric), [@shaq918](https://github.com/shaq918), [@yshalabi](https://github.com/yshalabi), [@zrss](https://github.com/zrss) for your contributions.

  We also thank the community for issue reports, testing, and feedback.

  ## Known Issues

  - Rubin performance model has not been optimized with 2.32.3. Users can observe better performance on Rubin by increasing the number of CTAs NCCL uses. Automatic tuning will be improved in the next release.
  - Socket GIN currently requires users to opt-in to enable GDRCopy.
  - B100 PCIe MLoPart workloads can fail during memory allocation with CUDA error 101 (invalid device ordinal). Set NCCL_CUMEM_ENABLE=0 as a workaround.

