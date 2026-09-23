# NIXL

source: https://github.com/ai-dynamo/nixl/releases

# Releases: ai-dynamo/nixl

## Release list

## v1.4.1

# 1.4.1

## Summary

NIXL 1.4.1 is a focused patch release that closes a use-after-free window in the transfer-request path. `postXferReq`

/`estimateXferCost`

previously validated a remote xfer handle by name only, so a handle created before a peer disconnect/re-register cycle could still be posted against the new (freed-then-reallocated) generation's metadata, segfaulting in the UCX send path. ([#2027](https://github.com/ai-dynamo/nixl/pull/2027))

The release also restores the `num_experts`

parameter to the `nixl_ep`

example's low-latency `dispatch`

/`combine`

path, so callers can pin dispatch/combine tensor shapes to a fixed expert capacity instead of having them shift with the active rank mask — letting captured CUDA graphs be reused safely across rank changes. ([#2095](https://github.com/ai-dynamo/nixl/pull/2095))

## Enhancements

### NIXL-EP

`nixl_ep`

: CUDA graph reuse across rank changes:`dispatch()`

regains an optional`num_experts`

parameter (previously deprecated in[#1693](https://github.com/ai-dynamo/nixl/pull/1693)) that fixes the dispatch/combine layout to a caller-supplied expert capacity instead of deriving it from the currently active`active_rank_bound`

. Masking or unmasking ranks no longer changes tensor shapes, buffer offsets, or kernel launch parameters when`num_experts`

is set, so CUDA graphs captured against`dispatch`

/`combine`

/`get_next_combine_buffer`

remain valid across rank changes.`combine()`

and`get_next_combine_buffer()`

now derive their rank bound from`layout_range`

/an explicit parameter rather than the live`active_rank_bound`

, with added shape validation. ([#2095](https://github.com/ai-dynamo/nixl/pull/2095))

### Packaging & Distribution

The manylinux wheel build's`nixl_ep`

preview support for PyTorch 2.14:`WHL_TORCH_VERSIONS`

now includes`2.14`

, so published`nixl_ep`

wheels add a preview PyTorch 2.14 extension alongside 2.11-2.13. ([#2157](https://github.com/ai-dynamo/nixl/pull/2157))

## Bugfixes

**[Core] Fixed use-after-free on stale-generation transfer handles:**`postXferReq`

and`estimateXferCost`

now track a per-remote-agent generation counter and reject request handles created against a since-invalidated (freed and re-registered) remote agent with`NIXL_ERR_NOT_FOUND`

, instead of dereferencing the freed`nixlUcxPublicMetadata`

. Previously, a disconnect that invalidated a peer's metadata followed by re-registration could leave in-flight handles pointing at freed memory, segfaulting in`sendXferRangeBatch`

/`ucp_put_nbx`

. Follow-up to[#1811](https://github.com/ai-dynamo/nixl/pull/1811)/[#1987](https://github.com/ai-dynamo/nixl/pull/1987). ([#2027](https://github.com/ai-dynamo/nixl/pull/2027))

## Known Issues

Full Changelog: [v1.4.0...v1.4.1](https://github.com/ai-dynamo/nixl/compare/v1.4.0...v1.4.1)

## v1.4.0

# 1.4.0

## Summary

NIXL 1.4.0 centers on performance, observability, and LIBFABRIC correctness. Stride (compressed) descriptors cut prepared-handle memory by orders of magnitude — a 1.4M-descriptor set for DeepSeek-R1-Distill-Qwen-32B shrinks from ~44 MB to ~7 KB — and `make_prepped_xfer`

latency drops up to 5.4× in SGLang workloads.

A new `nixl::trace`

tracing framework with an NVTX backend (`libtrace_backend_nvtx.so`

) surfaces NIXL operations on Nsight Systems timelines; the telemetry layer gains unified Prometheus/DOCA exporters, 60% lower per-transfer overhead, and new dropped-event, error-count, and byte-gauge metrics.

The LIBFABRIC backend receives two critical fixes: a pre-connection handshake that prevents transfer-ID collisions across sender processes, and a `FI_MORE`

rail-flush correction that eliminates transfer hangs in multi-DRAM-registration workloads. Seven concurrency and correctness fixes land across the core agent and file-seg backends, NIXL-EP wheels now bundle extensions for multiple PyTorch versions in a single distribution, and UCX is updated to v1.22.x to unlock rendezvous PUT/GET protocols.

## Major Features

**Stride (compressed) descriptors for prep+make:**The prep+make API now encodes prepared handles as stride (run-length) descriptors, collapsing contiguous memory runs into a compact form. A 1,387,520-descriptor set for DeepSeek-R1-Distill-Qwen-32B shrinks from ~44 MB to ~7 KB;`make_prepped_xfer`

is up to 5.4× faster in SGLang merge micro-benchmarks and`Avg Prep`

time drops from 34 µs to 21 µs in nixlbench. The merge algorithm is also accelerated and uses reserve-instead-of-resize for the internal descriptor vector. ([#1756](https://github.com/ai-dynamo/nixl/pull/1756))A new internal`nixl::trace`

pluggable tracing framework + NVTX backend:`nixl::trace`

API instruments NIXL operations at one set of call sites and fans out to loadable`.so`

backend plugins. NVTX ships as the first backend (`libtrace_backend_nvtx.so`

), making NIXL transfer operations, notifications, and lifecycle events appear as colored NVTX ranges on an Nsight Systems timeline (`--trace=cuda,nvtx`

). The backend is auto-enabled when the process runs under Nsight Systems, requires only the CUDA toolkit's header-only`nvtx3`

to build, and adds near-zero overhead when no profiler is attached. ([#1765](https://github.com/ai-dynamo/nixl/pull/1765),[#1845](https://github.com/ai-dynamo/nixl/pull/1845),[#1867](https://github.com/ai-dynamo/nixl/pull/1867))**Multi-PyTorch-version NIXL-EP wheels:**The NIXL-EP wheel build now compiles separate per-PyTorch-version C++ extensions in isolated environments and merges them into a single distribution via a new`contrib/wheel_merge.py`

step. The correct ABI extension is selected at import time based on the installed PyTorch version, so one wheel works across PyTorch versions without reinstallation. ([#1775](https://github.com/ai-dynamo/nixl/pull/1775))

## API Changes

**[Telemetry] Prometheus and DOCA metric series renamed to the**The`*_last_bytes`

convention:`agent_memory_registered`

/`agent_memory_deregistered`

gauges are renamed to`agent_memory_registered_last_bytes`

/`agent_memory_deregistered_last_bytes`

. Prometheus/DOCA scrape configurations referencing the old names must be updated. ([#1850](https://github.com/ai-dynamo/nixl/pull/1850))

## Enhancements

### Performance

**[UCX] Avoid zero-initializing the full**A recent UCX SGL patch grew`ucp_request_param_t`

on each operation:`ucp_request_param_t`

; zero-initializing the whole struct on every PUT/GET/AM call was measurable — ~2% throughput regression in nixlbench (512B × 64000 ops, 8 threads). Changed to explicitly set only the needed`op_attr_mask`

,`memh`

, and`flags`

fields, dropping the blanket`= {0}`

init. ([#2022](https://github.com/ai-dynamo/nixl/pull/2022))**[Core] Lazy**`torch`

import cuts NIXL Python startup time:`torch`

is now imported only on demand rather than at`import nixl`

, eliminating the ~1 s startup cost for callers that do not use PyTorch. A`TYPE_CHECKING`

guard preserves IDE autocompletion; CUDA version detection falls back through CUDA bindings, CuPy, and a lightweight probe when PyTorch is absent. Duplicate logic between the`nixl`

and`nixl.ep`

modules is consolidated into`nixl_meta_utils.py`

. ([#1895](https://github.com/ai-dynamo/nixl/pull/1895))**[Telemetry] Cut per-transfer telemetry overhead 60% with CPU-counter stopwatch, batched stats, and enum-keyed Prometheus maps:**`nixlDuration`

(`nixl_duration.h`

) measures post and transfer durations using the invariant TSC (`rdtsc`

on x86_64,`cntvct_el0`

on aarch64), reducing the per-transfer telemetry cost from ~79 ns to ~32 ns while keeping the exposed`startTime`

on a drift-free`CLOCK_MONOTONIC_COARSE`

clock. The four xfer-stat events (`agent_xfer_time`

,`agent_tx/rx_bytes`

,`agent_tx/rx_requests_num`

,`agent_xfer_post_time`

) are now written under one mutex lock in`addXferStats`

, halving lock round-trips on the hot path. The Prometheus exporter's`counters_`

/`gauges_`

maps are re-keyed on the`nixl_telemetry_event_type_t`

enum, eliminating the per-event`std::string`

allocation in`exportEvent()`

. ([#1890](https://github.com/ai-dynamo/nixl/pull/1890),[#1844](https://github.com/ai-dynamo/nixl/pull/1844),[#1878](https://github.com/ai-dynamo/nixl/pull/1878))

### Networking & Backend

**[OBJ/S3 CRT] Configurable**Exposes the CRT connection-count target as the optional backend parameter`throughput_target_gbps`

for the S3 CRT client:`throughput_target_gbps`

(integer Gbps; default remains 10). In testing against a Cloudian HyperStore system, raising this limit raised sustained throughput from 10 GiB/s to 18.13 GiB/s. ([#1769](https://github.com/ai-dynamo/nixl/pull/1769))**[UCX] Enable rendezvous PUT/GET protocol on UCX ≥ 1.22:**Sets`RNDV_PIPELINE_ERROR_HANDLING=y`

at context creation when the runtime UCX version is 1.22 or newer, enabling the rendezvous-based PUT and GET transfer protocols. ([#1854](https://github.com/ai-dynamo/nixl/pull/1854))**[Libfabric] Add pre-connection handshake to convey sender agent index:**Before the first transfer the LIBFABRIC backend now sends a handshake message carrying the local agent index assigned to the peer. The peer stores this index and uses it as immediate data on all subsequent WRITE and notification posts, allowing the receiver to distinguish transfers from different sender processes that share the same transfer ID. Calling`connect()`

before the first transfer avoids any first-transfer stall. Validated with no throughput regression on AWS p5en nodes. ([#1736](https://github.com/ai-dynamo/nixl/pull/1736))**[Libfabric] Fix**The prior`FI_MORE`

flush granularity to per-rail instead of per-group:`FI_MORE`

WRITE batching flushed doorbells positionally (last of each 16-descriptor group), which is only correct when every descriptor in a group maps to the same physical rail. Transfers spanning buffers with different rail assignments — e.g. many DRAM registrations in Dynamo — would alternate rails within a group, leaving one rail's batch unsubmitted and causing the transfer to hang. Fixed by precomputing a per-rail flush map in`postXfer`

(walking descriptors in reverse to find each rail's last post) and passing an explicit`apply_fi_more`

flag into`prepareAndSubmitTransfer`

. The new`NIXL_LIBFABRIC_FI_MORE_BATCH_SIZE`

env var (default 16) caps consecutive`FI_MORE`

-eligible descriptors before an unconditional flush. nixlbench was unaffected (one buffer per device = one rail). ([#1966](https://github.com/ai-dynamo/nixl/pull/1966))

### NIXL-EP Example Improvements

**Dropped-events counter for telemetry loss detection:**Adds a new`agent_telemetry_events_dropped`

cumulative counter emitted by both Prometheus (`_total`

suffix) and DOCA exporters. When the staging queue is full, drops are accumulated in`droppedEvents_`

and flushed as a synthetic event bypassing the queue on the next periodic drain — ensuring the counter itself can never be lost. Bumps`TELEMETRY_VERSION`

3 → 4;`examples/python/telemetry_reader.py`

is updated accordingly. ([#1887](https://github.com/ai-dynamo/nixl/pull/1887))**Private UCX loading via SONAME suffix and**The UCX backend plugin is now loaded with`RTLD_DEEPBIND`

:`RTLD_DEEPBIND`

by default (opt-out via`NIXL_UCX_DEEPBIND=0`

), preventing the bundled UCX from binding to a globally loaded UCX in HPC-X/OpenMPI environments. The container build supports`--ucx-soname-suffix`

and`--private-ucx`

flags to compile UCX with a private SONAME, and`auditwheel`

handling is updated to correctly map the renamed libraries. Set`NIXL_UCX_EXPECTED_SONAME`

to fail fast if an unexpected UCX library is bound. ([#1673](https://github.com/ai-dynamo/nixl/pull/1673))**NVLink low-latency path optimization:**Caches P2P GPU pointers in a per-context GPU-side array (`p2p_ptrs`

) instead of calling`nixlGetPtr`

on every low-latency send, eliminating redundant pointer resolution. Also reduces the TOPK index width from 64-bit to 32-bit. On the TRT-LLM MoE dispatch benchmark (8×H100, NVLink), NIXL-EP dispatch reaches parity with DeepEP low latency (e.g., 32.55 µs vs. 32.06 µs at batch size 16). ([#1751](https://github.com/ai-dynamo/nixl/pull/1751))

### Packaging & Distribution

**Bump UCX dependency to v1.22.x:**Build tooling, CI matrices, and wheel builds are updated to use UCX v1.22.x, required to enable the rendezvous PUT/GET protocol and the UCX private SONAME extension. ([#1868](https://github.com/ai-dynamo/nixl/pull/1868))**UCX SPCx and Infinia plugin now bundled in the manylinux wheel:**The manylinux wheel for 1.4.0 includes the UCX SPCx and DDN Infinia storage plugins, making them available without a separate install. ([#1968](https://github.com/ai-dynamo/nixl/pull/1968))**Install Python bindings from source in the container image:**The reference container`Dockerfile`

now builds and installs the`nixl`

Python meta-package from source rather than from a pre-built wheel, ensuring installed bindings always match the container's native NIXL build. ([#1896](https://github.com/ai-dynamo/nixl/pull/1896))**Add NVIDIA Proprietary License to wheel distribution:**The Python wheel now includes`licenses/NVIDIA-proprietary-LICENSE.txt`

covering bundled proprietary dependencies. ([#1972](https://github.com/ai-dynamo/nixl/pull/1972))

### Benchmarks

**[LIBFABRIC] Configurable**The LIBFABRIC backend now supports a configurable descriptor-posting thread pool for`postXfer`

thread pool:`postXfer()`

, controlled by the`num_threads`

and`split_batch_size`

backend parameters (exposed in the Python config and nixlbench). Validated on two GB200/EFA nodes running LIBFABRIC 1.21.0 with cross-node DRAM WRITE at batch size 2048. ([#1581](https://github.com/ai-dynamo/nixl/pull/1581))

### Documentation

**Unified Prometheus and DOCA/CollectX exporter metric output:**The native Prometheus and DOCA exporters now share a single`constexpr`

metri...

[Read more](https://github.com/ai-dynamo/nixl/releases/tag/v1.4.0)

## v1.3.2

# 1.3.2

## Summary

NIXL 1.3.2 is a targeted patch release that fixes a cross-node EFA transfer hang introduced in 1.3.1. When the progress thread is enabled, NIXL posts each WRITE descriptor under a separate endpoint lock while using `FI_MORE`

to keep a 16-descriptor batch open; on `efa`

/`efa-direct`

providers, CQ progress can acquire that same endpoint lock before the closing post, leaving the batch permanently open and stalling the transfer. An initial fix disabling `FI_MORE`

on EFA ([#1924](https://github.com/ai-dynamo/nixl/pull/1924)) was replaced by a more targeted per-rail flush strategy ([#1989](https://github.com/ai-dynamo/nixl/pull/1989)) that preserves batching throughput on all providers.

The fix introduces per-rail flush tracking: a precompute pass identifies the last descriptor on each rail before posting begins, and `FI_MORE`

is cleared only at that descriptor (or when the per-rail batch reaches `NIXL_LIBFABRIC_FI_MORE_BATCH_SIZE`

). This guarantees every rail's batch closes without a fixed-width group boundary assumption and without disabling batching globally.

## Bugfixes

**[Libfabric] Fix cross-node EFA transfer hang with progress thread:**On`efa`

and`efa-direct`

providers, CQ progress can acquire the endpoint lock between a batch's first and closing`FI_MORE`

post, preventing the batch from ever being flushed. NIXL 1.3.1 users with the progress thread enabled would see decode workers stuck in`KVPoll.WaitingForInput`

returning empty responses. An intermediate fix that disabled`FI_MORE`

entirely on EFA ([#1924](https://github.com/ai-dynamo/nixl/pull/1924)) was reverted ([#1984](https://github.com/ai-dynamo/nixl/pull/1984)) in favour of the per-rail flush in[#1989](https://github.com/ai-dynamo/nixl/pull/1989), which closes each rail's batch correctly without giving up batching throughput on non-EFA providers. ([#1924](https://github.com/ai-dynamo/nixl/pull/1924),[#1984](https://github.com/ai-dynamo/nixl/pull/1984),[#1989](https://github.com/ai-dynamo/nixl/pull/1989))

## Known Issues

Full Changelog: [1.3.1...75ead3d7](https://github.com/ai-dynamo/nixl/compare/1.3.1...75ead3d7)

## v1.3.1

# 1.3.1

## Summary

NIXL 1.3.1 is a focused patch release. It closes the path-mode file-registration gap introduced in 1.3.0: reusing the same `devId`

across distinct path-mode `FILE_SEG`

registrations could leave transfers ambiguous and trigger a double-free on deregister, so all four path-mode file backends now reserve and enforce a unique path-mode `devId`

per registered file. ([#1790](https://github.com/ai-dynamo/nixl/pull/1790))

The release also improves wheel packaging. The `nixl_ep`

wheel can now be built against multiple PyTorch versions, producing per-`(Python, Torch)`

extension artifacts that are merged into a single distribution and loaded by ABI/Torch version at runtime. In addition, the published manylinux wheels now bundle the DDN INFINIA backend plugin by default, so the INFINIA storage backend is available out of the box. ([#1775](https://github.com/ai-dynamo/nixl/pull/1775), [#1866](https://github.com/ai-dynamo/nixl/pull/1866), [#1832](https://github.com/ai-dynamo/nixl/pull/1832))

## API Changes

**[POSIX/CUDA GDS/GDS MT/HF3FS] Unique**Path-mode registrations that reuse an in-use`devId`

required for path-mode`FILE_SEG`

:`devId`

are now rejected with`NIXL_ERR_INVALID_PARAM`

. Fd-in-`devId`

mode (non-path`metaInfo`

) is unchanged — one file descriptor may still back multiple descriptors at different offsets. ([#1790](https://github.com/ai-dynamo/nixl/pull/1790))

## Enhancements

### NIXL-EP Example Improvements

**Multi-PyTorch**The`nixl_ep`

wheels:`nixl_ep`

wheel can now be built and packaged for multiple PyTorch versions at once. The build produces per-`(Python, Torch)`

extension artifacts (with Torch-version-aware extension names) and merges them into a single wheel via a new`contrib/wheel_merge.py`

; at import time the correct PyTorch/ABI extension is selected based on the installed Torch version. ([#1775](https://github.com/ai-dynamo/nixl/pull/1775))

### Packaging & Distribution

**DDN INFINIA plugin bundled in manylinux wheels:**The published manylinux wheels are built on the public PyPA`manylinux_2_28`

base and now bundle the DDN INFINIA plugin (`libplugin_INFINIA.so`

) by default — meson auto-detects the DDN`red_client`

libraries at`/opt/ddn/red`

and compiles the plugin into the wheel. The proprietary DDN`libred_*`

runtime libraries are intentionally**not**vendored (they remain`auditwheel --exclude`

d) and are loaded at runtime from the customer's DDN install. ([#1832](https://github.com/ai-dynamo/nixl/pull/1832))**Wire**`--torch-versions`

through the container build:`contrib/Dockerfile`

gained a`WHL_TORCH_VERSIONS`

build arg (default`2.11,2.12,2.13`

) that is forwarded to`contrib/build-wheel.sh`

via`--torch-versions`

when`BUILD_NIXL_EP=true`

, fixing EP container builds that previously failed with`--build-nixl-ep requires --torch-versions`

. The EP meson target's`override_options`

were also extended to`['buildtype=release', 'optimization=3', 'debug=false']`

so a global`--buildtype=debug`

no longer leaks`-G`

onto the EP`nvcc`

compiles. ([#1866](https://github.com/ai-dynamo/nixl/pull/1866))

## Bugfixes

**[POSIX/CUDA GDS/GDS MT/HF3FS] Fixed path-mode double-free and leak on deregister:**Introduced a shared`nixl::PathModeDevIdRegistry`

with RAII reserve/commit/release semantics so each path-mode file's`devId`

is tracked from`registerMem`

through`deregisterMem`

, eliminating the ambiguous section-key collision that could free the same backend metadata twice when distinct path-mode files shared a`devId`

. Fixes[#1766](https://github.com/ai-dynamo/nixl/issues/1766). ([#1790](https://github.com/ai-dynamo/nixl/pull/1790))

## Known Issues

Full Changelog: [1.3.0...1.3.1](https://github.com/ai-dynamo/nixl/compare/1.3.0...1.3.1)

## v1.3.0

# 1.3.0

## Summary

NIXL 1.3.0 expands platform reach and backend capabilities. It adds AMD ROCm/HIP support for AMD Instinct GPUs (MI300X, MI325X, MI350X, MI355X), including `nixlbench`

. The core build now targets C++20 to enable modern C++ features and provides a stronger foundation for future development for anyone compiling NIXL or its plugins from source. NIXL 1.3.0 also broadens the storage ecosystem: a new DDN Infinia backend joins the object-storage family, the `obj`

plugin can now auto-register vendor backends without factory changes, and path-based file registration is now supported across all file-based backends.

Secondary updates focus on performance and reliability. Azure Blob Storage paths get faster through parallel memory queries, releasing the python global lock during transfer-request creation reduces multi-threaded contention, and using a pre-allocated telemetry buffer improves hot path performance. The telemetry schema is simplified, descriptor-list paths gain batched bulk removal and an empty-section leak fix, and the benchmark tools (`nixlbench`

/`kvbench`

) include several correctness improvements.

## Major Features

**AMD ROCm/HIP support:**Added AMD ROCm/HIP build support for AMD Instinct GPUs (gfx942 - MI300X, MI325X; gfx950-MI350X, MI355X), including hardware-info detection plumbing and a follow-up enabling the same support for`nixlbench`

. ([#1642](https://github.com/ai-dynamo/nixl/pull/1642),[#1647](https://github.com/ai-dynamo/nixl/pull/1647))**Move to C++20:**Switched the core and plugins to the C++20 standard and updated the plugin READMEs accordingly. Downstream builds-from-source now require a C++20-capable toolchain. ([#1571](https://github.com/ai-dynamo/nixl/pull/1571))**DDN Infinia backend plugin:**Added a new NIXL backend plugin for DDN Infinia storage. ([#1569](https://github.com/ai-dynamo/nixl/pull/1569))**Path-based file registration for all**Callers can now declare files by path in`FILE_SEG`

backends:`nixlBlobDesc::metaInfo`

(`<modes>:<path>`

with`ro`

/`rw`

access and`direct`

/`sync`

/`noatime`

/`create`

flags); backends open the file in`registerMem`

and close it in`deregisterMem`

. Wired through a shared`src/utils/file/file_path_mode`

helper into POSIX, HF3FS, CUDA_GDS, and GDS_MT. Strictly additive — unknown tokens fall back to the existing fd-in-`devId`

mode. ([#1635](https://github.com/ai-dynamo/nixl/pull/1635))**Object plugin vendor backend registry:**Replaced the`#ifdef`

ladder in`obj_backend.cpp`

with a self-registration pattern so accelerated/vendor engines register themselves via`objAccelEngineRegistrar`

, making it trivial to add new object-storage engines without modifying the factory. ([#1550](https://github.com/ai-dynamo/nixl/pull/1550))

## API Changes

**[Telemetry] Slimmed telemetry event schema:**Removed the redundant`category`

field from telemetry events, simplifying`telemetry_event.h`

and the backend telemetry surface. Consumers parsing telemetry events should drop the`category`

field. ([#1649](https://github.com/ai-dynamo/nixl/pull/1649))**[NIXL EP] Refactor rank and expert semantics:**Added new fields, public mask-update capability and host-side tracking of active ranks for elastic rank handling. Dispatch/combine now accept an active-rank bound + experts-per-rank parameterization; internal buffer/layouts updated to use the active-range model. Removed the legacy mask-clean API. ([#1693](https://github.com/ai-dynamo/nixl/pull/1693))

## Enhancements

### Performance

**[Azure] Parallelized memory query for the**Batched memory queries now issue HEAD requests in parallel (mirroring the OBJ plugin), improving initial blob-existence checks for integrations such as KV-cache lookups in LMCache. (`AZURE_BLOB`

plugin:[#1721](https://github.com/ai-dynamo/nixl/pull/1721))**[Python] Release the GIL during**The Python binding now releases the GIL while building transfer requests, reducing contention for multithreaded callers. (`makeXferReq`

:[#1712](https://github.com/ai-dynamo/nixl/pull/1712))**[Telemetry] Pre-allocate the event buffer:**The telemetry event buffer is pre-allocated to avoid reallocation on the hot path. ([#1719](https://github.com/ai-dynamo/nixl/pull/1719))**[Core] Batched descriptor-list removal:**`remDescList`

and`removeLocalData`

now remove descriptors in bulk instead of one-at-a-time, eliminating the previous O(N*M) per-deregister cost. ([#1597](https://github.com/ai-dynamo/nixl/pull/1597))**[Core] Use C++20**Replaced`[[likely]]`

/`[[unlikely]]`

:`__builtin_expect`

with the standard C++20 branch-prediction attributes across the core, UCX backend, and`nixlbench`

. ([#1714](https://github.com/ai-dynamo/nixl/pull/1714))

### Networking & Backend

**[Azure] Updated CA certificate discovery:**Expanded the list of CA certificate file paths the Azure Blob client checks, improving TLS trust-store discovery across environments. ([#1694](https://github.com/ai-dynamo/nixl/pull/1694))

### NIXL-EP

**Removed a declared-but-undefined method:**Cleaned up a method without a definition in the device/EP example. ([#1684](https://github.com/ai-dynamo/nixl/pull/1684))

### Packaging & Distribution

The`nixl_ep`

wheel packs CUDA in a separate namespace:`nixl_ep`

wheel now packages the bundled CUDA libraries under a distinct namespace (with a load fallback), avoiding collisions with other CUDA installations. ([#1727](https://github.com/ai-dynamo/nixl/pull/1727))**Wheel build excludes DDN partner libraries:**Extended the`auditwheel --exclude`

list in`build-wheel.sh`

so DDN partner libraries are not vendored into the wheel. ([#1733](https://github.com/ai-dynamo/nixl/pull/1733))

### Benchmarks

**[nixlbench] AMD ROCm/HIP build support:**Enabled building`nixlbench`

for AMD ROCm/HIP as a follow-up to the core AMD support. ([#1647](https://github.com/ai-dynamo/nixl/pull/1647))**[nixlbench] Use**Sized the object-storage buffer from`max_block_size`

for object-storage buffer size:`max_block_size`

. ([#1636](https://github.com/ai-dynamo/nixl/pull/1636))**[nixlbench] Fixed object-storage device-ID collisions across threads:**Resolved colliding device IDs when multiple threads target object storage. ([#1638](https://github.com/ai-dynamo/nixl/pull/1638))**[nixlbench] Fixed deallocation memory ordering:**Corrected the order in which memory is deallocated. ([#1590](https://github.com/ai-dynamo/nixl/pull/1590))**[nixlbench] Fixed a missing closing bracket in print output:**Repaired malformed benchmark print output. ([#1725](https://github.com/ai-dynamo/nixl/pull/1725))**[kvbench] Fixed OBJ backend configuration and buffer-size setup:**Corrected the OBJ backend configuration and buffer-size initialization in`kvbench`

. ([#1549](https://github.com/ai-dynamo/nixl/pull/1549))

## Bugfixes

**[Core] Fixed**`addElement`

using a hardcoded`VRAM_SEG`

lookup:`mem_section`

no longer assumes`VRAM_SEG`

when adding an element. ([#1634](https://github.com/ai-dynamo/nixl/pull/1634))**[Core] Erase empty sections in**Empty section map entries are now removed, preventing`removeLocalData`

:`sectionMap`

/`memToBackend`

from growing without bound in long-running register/deregister workloads. ([#1597](https://github.com/ai-dynamo/nixl/pull/1597))**[Core] Fixed**Zero-length descriptor lists are handled correctly. (`remDescList`

returning`NIXL_ERR_NOT_FOUND`

when`len=0`

:[#1551](https://github.com/ai-dynamo/nixl/pull/1551))**[POSIX] Fixed backend queue fallback handling:**Corrected fallback handling in the POSIX backend transfer queue. ([#1605](https://github.com/ai-dynamo/nixl/pull/1605))**[Telemetry] Fixed DOCA exporter build:**Added`nixl_common_dep`

so`tomlplusplus`

resolves for the DOCA telemetry plugin, which otherwise failed to compile after`common/configuration.h`

began including`toml++/toml.hpp`

directly. ([#1640](https://github.com/ai-dynamo/nixl/pull/1640))

## Known Issues

**[POSIX]**File-path Mode has a double-free issue ([#1766](https://github.com/ai-dynamo/nixl/issues/1766))

Full Changelog: [1.2.0...1.3.0](https://github.com/ai-dynamo/nixl/compare/1.2.0...1.3.0)

## v1.2.0

# 1.2.0

## Summary

The NVIDIA® NIXL Release 1.2.0 adds OS-assigned port support to the metadata listener so multi-peer agents can bind to port `0`

and discover the kernel-chosen port at runtime instead of statically reserving one, and tightens the Libfabric backend's EFA write path with `FI_MORE`

-based descriptor batching pinned to a single endpoint per rail. The Libfabric change groups up to 16 consecutive write descriptors before flushing the doorbell to the device, reducing PCIe round trips for small-message high-descriptor-count transfers while keeping a standard round-robin read path so reads do not regress.

NIXL 1.2.0 also tightens the build and packaging story for downstream consumers. UCX now configures `UCX_MAX_HCA_PER_GPU=auto`

on UCX `>= 1.21`

, NIXL gains a `nixl_cuda_arch_list`

meson option to compile against a user-selected SM list instead of the full datacenter default sweep, and `liburing`

is sourced from a meson wrap pinned to WrapDB `liburing_2.14-1`

so the POSIX backend's `io_uring`

support is available out of the box from a source build and from every shipping container. The Rust bindings stop silently swallowing backend registration failures and now surface the C API status from `register_memory`

directly to the caller.

## Major Features

**OS-Assigned Port Support for Metadata Listener:**Added support for binding the metadata listener to port`0`

so the OS picks an available port; the bound port is retrieved via`getsockname()`

and emitted on`NIXL_INFO`

. The Python multi-peer test helpers in`.gitlab/test_python.sh`

now exercise this path so concurrent examples no longer collide on a hard-coded port. ([#1439](https://github.com/ai-dynamo/nixl/pull/1439))

## API Changes

**[Core] Metadata Listener Port Type Migration:**Upgraded the default listener-port variables and structure fields (`listenPort`

,`listen_port`

) in`src/api/cpp/nixl_params.h`

,`src/api/cpp/nixl_types.h`

, and`src/utils/stream/metadata_stream.{h,cpp}`

from`int`

to`uint16_t`

to match standard socket definitions. The Rust bindings (`src/bindings/rust/wrapper.{h,cpp}`

,`src/bindings/rust/src/agent.rs`

) gain a`DEFAULT_COMM_PORT`

constant mirroring the C++`default_comm_port`

. ([#1439](https://github.com/ai-dynamo/nixl/pull/1439))

## Enhancements

### Performance

**[Libfabric] EFA Doorbell Batching via**`FI_MORE`

:`libfabric_backend.cpp`

now batches up to 16 consecutive write descriptors on the same EP-pinned rail and submits them through`fi_writemsg()`

with the`FI_MORE`

flag, draining via a flushing`fi_writemsg()`

on batch close. A stable per-transfer`base_offset`

is reserved once in`postXfer()`

(instead of per-descriptor) so every descriptor in a transfer sees the same rail assignment. Delivers a**30%–58% write bandwidth improvement**for small-message high-descriptor-count transfers; the read path keeps the existing round-robin layout to avoid regressing reads. ([#1626](https://github.com/ai-dynamo/nixl/pull/1626))

### Networking & Backend

**[UCX] Auto-Selected**`MAX_HCA_PER_GPU`

on UCX`>= 1.21`

:`src/plugins/ucx/ucx_utils.cpp`

now sets`UCX_MAX_HCA_PER_GPU=auto`

when the linked UCX is`>= 1.21`

, letting UCX pick the right HCA-to-GPU mapping on modern multi-HCA hosts instead of relying on the historical default. ([#1637](https://github.com/ai-dynamo/nixl/pull/1637))

### Packaging & Distribution

**Configurable CUDA Target Selection (**Added a`nixl_cuda_arch_list`

):`nixl_cuda_arch_list`

meson option (`meson.build`

,`meson_options.txt`

,`contrib/build-wheel.sh`

) defaulting to`sm_80, sm_86, sm_89, sm_90, sm_100, sm_103, sm_120`

for full datacenter coverage. Users compiling for a single architecture can pass e.g.`-Dnixl_cuda_arch_list=90,100`

for materially faster builds; when`nixl_ep`

is enabled, the`sm_8x`

entries are dropped automatically since the EP example only supports newer architectures. ([#1639](https://github.com/ai-dynamo/nixl/pull/1639))Replaced the per-container`liburing`

via meson Wrap:`liburing`

install paths (apt`liburing-dev`

on Ubuntu,`git clone`

+`make`

on manylinux,`git clone`

+`make`

in nixlbench builder,`.gitlab/build.sh`

) with a single meson wrap pinned to WrapDB`liburing_2.14-1`

. POSIX backend`io_uring`

support is now always available when building from source and identical across`contrib/Dockerfile`

,`contrib/Dockerfile.manylinux`

, and`nixlbench/contrib/Dockerfile`

.`ATTRIBUTIONS-CPP.md`

bumped to`liburing 2.14`

. ([#1577](https://github.com/ai-dynamo/nixl/pull/1577))

## Bugfixes

**[Rust] Surface**`register_memory`

Errors:`src/bindings/rust/src/agent.rs`

now returns the C API status from`register_memory`

instead of constructing a`RegistrationHandle`

after a failed registration; the Rust integration tests in`src/bindings/rust/tests/tests.rs`

are updated to create a backend and pass opt args so backend registration failures are exercised and no longer silently ignored. ([#1632](https://github.com/ai-dynamo/nixl/pull/1632))

## Known Issues

Full Changelog: [1.1.0...1.2.0](https://github.com/ai-dynamo/nixl/compare/1.1.0...1.2.0)

## v1.1.0

# 1.1.0

## Summary

The NVIDIA® NIXL Release 1.1.0 introduces a high-throughput dispatch/combine kernel path for the NIXL-EP example program and modernizes the telemetry data model for production-scale deployments. A new dedicated `nixl_ep_ht.cu`

kernel set ships alongside the renamed low-latency `nixl_ep_ll.cu`

, paired with a VMM-based device memory allocator and elastic-scaling fixes covering destruction flows, non-consecutive rank topologies, and signaling-buffer corruption during scale-up, while the core plugin manager now defers backend loading until first use to reduce agent startup cost. Telemetry consumers must adopt two breaking changes -- the public event signature drops its `timestamp`

field, and the Prometheus exporter migrates `agent_xfer_time`

/ `agent_xfer_post_time`

from `Gauge`

to `Counter`

, suffixes counters with `_total`

, and removes the per-backend metric category in favor of standardized transfer, performance, and memory categories. **Downstream consumers should also switch their requirements.txt from nixl[cu12] / nixl[cu13] to plain nixl** -- the meta wheel now bundles both CUDA backends and auto-selects at runtime based on




`torch.version.cuda`

(see [API Changes]).NIXL 1.1.0 also delivers significant networking, storage, and backend improvements. The Libfabric backend extends NUMA-aware rail selection to additional EC2 instance topologies, adds completion-queue locking for `FI_THREAD_COMPLETION`

semantics, and resolves multi-GPU memory registration and notification-override regressions on transfer-handle repost. A new Dell ObjectScale S3-over-RDMA accelerated engine joins the OBJ plugin for high-bandwidth object storage, UCX now raises an explicit error when VRAM is misclassified as host memory, and `nixlbench`

adds Neuron (Trainium/Inferentia) device support. Across core transfer paths, batched insertion of sorted descriptor lists and a bounded in-memory telemetry buffer contribute to lower per-request overhead and predictable memory behavior in long-running agents.

## Major Features

**NIXL-EP High-Throughput Kernels:**Added a new high-throughput dispatch/combine kernel path (`examples/device/ep/csrc/kernels/nixl_ep_ht.cu`

) alongside the renamed low-latency`nixl_ep_ll.cu`

, with matching`test_ht.py`

coverage and configurable GPU timeouts so the example can be tuned for production-scale runs. ([#1341](https://github.com/ai-dynamo/nixl/pull/1341),[#1503](https://github.com/ai-dynamo/nixl/pull/1503),[#1520](https://github.com/ai-dynamo/nixl/pull/1520))**Plugin Manager: Deferred Plugin Loading:**Plugins are now loaded the first time they are actually used instead of at agent construction. Reduces agent startup cost when only a subset of plugins is exercised and removes dead code from the telemetry path. ([#1546](https://github.com/ai-dynamo/nixl/pull/1546),[#1564](https://github.com/ai-dynamo/nixl/pull/1564))**Dell ObjectScale S3-over-RDMA Engine:**New accelerated S3 engine under`src/plugins/obj/s3_accel/dell/`

(with tests) that talks to Dell ObjectScale over RDMA via a dedicated client. Wired into`obj_backend.cpp`

and exercised through`test/gtest/unit/obj/`

. ([#1327](https://github.com/ai-dynamo/nixl/pull/1327))

## API Changes

-
**[Telemetry] Prometheus Exporter Migration:**Removed the`NIXL_TELEMETRY_BACKEND`

event category and`createOrUpdateBackendEvent()`

. Counters are now registered with a`_total`

suffix to match Prometheus naming conventions, and the`agent_xfer_time`

/`agent_xfer_post_time`

metrics moved from`Gauge`

to`Counter`

. ([#1308](https://github.com/ai-dynamo/nixl/pull/1308)) -
**[Telemetry] Event Signature Cleanup:**Removed the public`timestamp`

field from`nixlTelemetryEvent`

, simplified`backend_engine.h`

and`telemetry_plugin.h`

signatures, and tightened the`buffer_plugin`

API. Downstream consumers must update event-construction sites. ([#1522](https://github.com/ai-dynamo/nixl/pull/1522)) -
**[Packaging] Switch downstream installs from**`nixl[cu12]`

/`nixl[cu13]`

to plain`nixl`

:**Action required: update your**The`requirements.txt`

(or`pyproject.toml`

/`setup.py`

) to depend on`nixl`

instead of`nixl[cu12]`

or`nixl[cu13]`

.`nixl`

meta wheel on PyPI now installs both`nixl-cu12`

and`nixl-cu13`

backends in a single step and selects the correct one at runtime from`torch.version.cuda`

. The`[cu12]`

/`[cu13]`

extras are still accepted as no-op aliases so existing pins keep working, but new installs should drop the extra.nixl declares torch as a dependency, but the default PyPI torch is CPU-only; pass`torch`

is a mandatory runtime dependency and must be installed from the PyTorch index matching your CUDA driver, either before`nixl`

or in the same`pip install`

invocation.`--index-url https://download.pytorch.org/whl/cu130`

(or the appropriate CUDA variant) so pip resolves a CUDA-enabled build. At import nixl time the meta package reads`torch.version.cuda`

to select between the bundled`nixl-cu12`

and`nixl-cu13`

backends. ([#1574](https://github.com/ai-dynamo/nixl/pull/1574),[#1578](https://github.com/ai-dynamo/nixl/pull/1578))

## Enhancements

### Performance

**[Core] Batch Insertion for Sorted Descriptor Lists:**Added a batched insert path in`nixl_descriptors.cpp`

/`nixl_memory_section.cpp`

so registering large descriptor lists no longer pays the per-element ordered-insert cost. New`sec_desc_list`

gtest covers the path. ([#1479](https://github.com/ai-dynamo/nixl/pull/1479))**[Core] Deferred Plugin Loading:**See Major Features. Avoids parsing/loading unused backends at agent startup. ([#1546](https://github.com/ai-dynamo/nixl/pull/1546),[#1564](https://github.com/ai-dynamo/nixl/pull/1564))

### Networking & Backend

**[Libfabric] NUMA-Aware Rail Selection on Additional Instance Types:**Extended the rail-manager / topology code paths to recognize more EC2 instance topologies (including`c5n.18xlarge`

), warn cleanly when no policy applies, and keep the NUMA-aware policy from regressing on hardware it has not been tuned for. ([#1461](https://github.com/ai-dynamo/nixl/pull/1461))**[Libfabric] Endpoint Locking for**Expanded the CQ mutex to cover endpoint-bound posting operations, and skip in-line CQ progress when the dedicated progress thread is enabled. (`FI_THREAD_COMPLETION`

:[#1457](https://github.com/ai-dynamo/nixl/pull/1457))**[Libfabric] Active Rail Tracking:**Reworked`libfabric_rail_manager`

reference counting and added a sizable mock/unit-test harness (`libfabric_mock_stubs.h`

,`rail_active_refcount_test.cpp`

) so rail activation/deactivation is now covered by tests. ([#1510](https://github.com/ai-dynamo/nixl/pull/1510))**[Libfabric] Multi-GPU Memory Registration:**Restored the original two-`if`

registration pattern in`libfabric_backend.cpp`

and downgraded the multi-GPU detection log from WARN to INFO. Validated end-to-end with`nixlbench --scheme tp --mode MG`

. ([#1506](https://github.com/ai-dynamo/nixl/pull/1506))**[Libfabric] EFA Hardware Warning:**Emit a clear warning when EFA hardware is present but the LIBFABRIC backend is not in use, plus new`hw_warning_test`

coverage. ([#1287](https://github.com/ai-dynamo/nixl/pull/1287))**[Libfabric] Log-Level Cleanup in EFA Path:**Reclassified noisy WARN messages and added an`Accelerator-PCI`

prefix to topology-mapping INFO logs for context. ([#1462](https://github.com/ai-dynamo/nixl/pull/1462))**[UCX] Disable Emulated RMA Protocols:**On UCX >= 1.21, force`PROTO_EMULATION_ENABLE=n`

and pin`IB_TX_INLINE_RESP=0`

in`ucx_utils.cpp`

so the backend refuses to fall back to software-emulated RMA -- transfers either run over true RDMA or fail fast instead of silently degrading. ([#1611](https://github.com/ai-dynamo/nixl/pull/1611))**[UCX] Timeout Warning on Device Memory List Creation:**Added a configurable timeout warning in`mem_list.cpp`

so slow VRAM registrations surface visibly instead of hanging silently. ([#1410](https://github.com/ai-dynamo/nixl/pull/1410))**[UCX] Plugin Cleanup:**Removed an unused`ucx_backend`

class field. ([#1512](https://github.com/ai-dynamo/nixl/pull/1512))**[Mooncake] Dependency Bump:**Updated the Mooncake submodule/build to v0.3.9, including matching CI matrix entries. ([#1448](https://github.com/ai-dynamo/nixl/pull/1448))

### NIXL Expert Parallelism (EP)

**VMM API for Device Memory Allocation:**Added a new`vmm.cpp`

/`vmm.hpp`

layer so the NIXL-EP example uses the CUDA VMM API instead of plain`cudaMalloc`

for its device buffers. ([#1415](https://github.com/ai-dynamo/nixl/pull/1415))**CUDA Graph Reuse Across Elastic Scaling:**The low-latency dispatch/combine kernel path now reuses its CUDA graphs across elastic scale up/down instead of rebuilding them on every rank change.`Buffer.connect_ranks`

gains an`activate=False`

option (LL mode only) so newly connected ranks can be staged masked and activated later via`update_mask_buffer`

. ([#1584](https://github.com/ai-dynamo/nixl/pull/1584))**High-Throughput Follow-Up Fixes:**Removed a redundant count buffer, fixed internode destruction flows, re-guarded`p2p_ptr_get`

with`is_rank_masked`

, and merged duplicated`!low_latency_mode`

blocks. ([#1503](https://github.com/ai-dynamo/nixl/pull/1503))**Robust Destruction Flows:**Deregister buffers before`cudaFree`

, fix disconnect rank ordering, skip remote`prepMemView`

when there are no peers, and warn (rather than throw) on destructor failures. ([#1430](https://github.com/ai-dynamo/nixl/pull/1430))**Non-Consecutive Rank Support:**Move`p2p_ptr_get`

calls inside the rank-mask guard so configurations like ranks`[0, 2]`

no longer dereference uninitialized P2P mappings. ([#1478](https://github.com/ai-dynamo/nixl/pull/1478))**Signaling Buffer Corruption on Elastic Scale-Up:**Size the signaling region for the maximum expert count so growing`num_experts`

no longer overlaps with send/recv data. ([#1451](https://github.com/ai-dynamo/nixl/pull/1451))**Planned-SIGTERM Handling in Elastic Test:**`elastic.py`

now recognizes the intentional SIGTERM injected to simulate rank failure and does not flag those workers as errors. ([#1500](https://github.com/ai-dynamo/nixl/pull/1500))**GCC**Switched to raw pointers in ternary expressions matching the existing`maybe-uninitialized`

Fix in`ht_dispatch`

:`recv_topk_*`

pattern so`-Werror=maybe-uninitialized`

no longer fails the example build. ([#1525](https://github.com/ai-dynamo/nixl/pull/1525))**Cleanup:**Removed an unused variable in the EP CSRS kernels. ([#1508](https://github.com/ai-dynamo/nixl/pull/1508))

#### Limitations

**Cross-NVL-domain runs are not supported in this release.**Launching NIXL EP across nodes that belong to different NVLink domains (for example, with SLURM`--segment 1`

, or any allocation that spans NVL blocks) will fail during connection setup.

### Packaging & Distribution

**Unified Meta Wheel + CUDA-Matched Torch:**Implementation side of the`pip install nixl`

simplification described under API Changes. Adds a`-Drelease_wheel=true`

meson option (`meson_options.txt`

,`nixl-meta/meson.build`

,`pyproject.toml.in`

) that toggles the unified meta wheel for release builds vs. a single-backend wheel for source builds; the manylinux Dockerfile emits the meta wheel only on the cu12 pass since it is identical for cu12/cu13; the vLLM and SGLang Dockerfiles drop their per-CUDA wheel-selection logic; and `.gitlab/b...

[Read more](https://github.com/ai-dynamo/nixl/releases/tag/v1.1.0)

## v1.0.1

# 1.0.1

## Summary

NVIDIA® NIXL Release 1.0.1 is a targeted maintenance release focusing on NIXL-EP stability fixes, libfabric transport reliability improvements, and build/packaging improvements across UCX, Python wheel, and Docker environments.

## NIXL-EP Fixes

**Fix Destruction Flows**: Fixed resource cleanup and destruction ordering in NIXL-EP to prevent crashes and resource leaks during shutdown ([#1452](https://github.com/ai-dynamo/nixl/pull/1452)).**Fix Signaling Buffer Corruption During Elastic Scale-Up**: Fixed a signaling buffer corruption issue in NIXL-EP that could occur when new nodes join during elastic scale-up, ensuring correct buffer state across topology changes ([#1453](https://github.com/ai-dynamo/nixl/pull/1453)).

## Libfabric Fixes

**Fix Notification Override on Transfer Handle Repost**: Fixed an issue in the libfabric backend where updated notification messages were ignored when transfer handles were reposted, causing reposted transfers to always use the original notification from initial preparation time ([#1482](https://github.com/ai-dynamo/nixl/pull/1482),[#1433](https://github.com/ai-dynamo/nixl/pull/1433)).**Fix Endpoint Thread Safety**: Added proper mutex locking for all endpoint access in the libfabric backend to satisfy`FI_THREAD_COMPLETION`

thread-safety requirements, preventing potential race conditions during concurrent I/O operations ([#1483](https://github.com/ai-dynamo/nixl/pull/1483),[#1457](https://github.com/ai-dynamo/nixl/pull/1457)).

## Build & Packaging

**Enable UCX EP Support in Python Wheel Build**: Added UCX endpoint support to the Python wheel build, enabling NIXL-EP functionality for pip-installed deployments ([#1440](https://github.com/ai-dynamo/nixl/pull/1440)).**Disable gdrcopy in UCX Build**: Disabled gdrcopy in the UCX build to avoid linkage conflicts in environments where gdrcopy is not available or not needed ([#1436](https://github.com/ai-dynamo/nixl/pull/1436)).**Fix Abseil Version Conflicts**: Resolved Abseil version conflicts in NIXL builds and Docker images that could cause linker errors or runtime symbol mismatches ([#1432](https://github.com/ai-dynamo/nixl/pull/1432)).**Bump RDMA Memory Check UCX Version**: Updated the UCX version used for RDMA memory checks to align with the latest supported UCX release ([#1445](https://github.com/ai-dynamo/nixl/pull/1445)).**Pin Torch Version to 2.11**: Pinned the PyTorch dependency to version 2.11 for reproducible builds and compatibility ([#1471](https://github.com/ai-dynamo/nixl/pull/1471)).**Add pkg-config Install**: Added missing`pkg-config`

installation to the build environment, fixing build failures in minimal container images ([#1450](https://github.com/ai-dynamo/nixl/pull/1450)).**Fix Dependency Issues**: Removed strict PyTorch version check during module initialization to allow broader compatibility, and unified UCX checkout behavior to consistently use the configured UCX reference ([#1488](https://github.com/ai-dynamo/nixl/pull/1488)).

Full Changelog: [1.0.0...1.0.1](https://github.com/ai-dynamo/nixl/compare/1.0.0...1.0.1)

## v1.0.0

# 1.0.0

## Summary

The NVIDIA® NIXL Release 1.0.0 marks a major milestone in API stability and production readiness. This release finalizes the Device API V2 transition by removing the legacy V1 implementation and normalizing naming conventions, establishing a clean and stable 1.0 API surface. A new two-phase configuration framework replaces ad-hoc environment and API configuration handling, providing a consistent and extensible runtime configuration model across all NIXL components.

NIXL 1.0.0 also delivers significant improvements to networking, storage, and backend infrastructure. The Libfabric backend gains NUMA-aware rail selection for topology-optimized transport on multi-socket systems, while the POSIX plugin introduces per-engine IO queuing for higher filesystem concurrency. Cloud storage maturity advances with Azure Blob connection string and CA bundle support, S3 CRT multipart threshold corrections, and expanded object storage functional testing. Across core transfer paths, descriptor iteration and transfer request creation have been optimized, telemetry overhead reduced, and UCCL batch transfer handling simplified, contributing to improved throughput and lower latency in production deployments.

## Major Features

**Device API V2 Finalization:**Removed the legacy Device API V1 implementation and completed all V2-oriented cleanups, including normalizing`MemoryView`

to`MemView`

across the codebase. This establishes Device API V2 as the sole, stable device programming interface for NIXL 1.0. ([#1342](https://github.com/ai-dynamo/nixl/pull/1342),[#1337](https://github.com/ai-dynamo/nixl/pull/1337),[#1376](https://github.com/ai-dynamo/nixl/pull/1376))**Configuration Framework:**Introduced a comprehensive two-phase configuration system spanning environment-driven (Part 1) and API-driven (Part 2) settings. This replaces the previous ad-hoc configuration approach with a structured, extensible model for runtime configuration management. ([#1301](https://github.com/ai-dynamo/nixl/pull/1301),[#1346](https://github.com/ai-dynamo/nixl/pull/1346))**Libfabric NUMA-Aware Rail Selection:**Added a NUMA-aware rail selection policy for`DRAM_SEG`

memory types in the Libfabric backend. This enables topology-optimized transport selection on multi-socket systems by aligning memory access with the closest available network rail. ([#1302](https://github.com/ai-dynamo/nixl/pull/1302))**Libfabric Control Rail Removal:**Removed the legacy control rail from the Libfabric backend, simplifying the rail management architecture and reducing resource overhead. ([#1386](https://github.com/ai-dynamo/nixl/pull/1386))**POSIX Per-Engine IO Queue:**Added per-engine IO queue support in the POSIX plugin, improving concurrency and scheduling behavior for filesystem-backed storage workflows. ([#1051](https://github.com/ai-dynamo/nixl/pull/1051))**Azure Blob Storage Enhancements:**Extended the Azure Blob Storage plugin with connection string authentication support and configurable CA bundle settings, improving deployment flexibility in enterprise and air-gapped environments. ([#1351](https://github.com/ai-dynamo/nixl/pull/1351),[#1329](https://github.com/ai-dynamo/nixl/pull/1329))**Rust Runtime Library Resolution:**Introduced`dlopen`

-based`nixl-sys`

stubs via`libnixl_capi.so`

, enabling Rust consumers to resolve NIXL at runtime without build-time linking. Stubs use`dlopen`

/`dlsym`

for lazy forwarding to the real implementation. ([#1358](https://github.com/ai-dynamo/nixl/pull/1358))**UCCL Batch Transfer Optimization:**Simplified and optimized UCCL handling for batch transfer workflows, reducing overhead in multi-transfer scenarios. ([#1271](https://github.com/ai-dynamo/nixl/pull/1271))

## API Changes

**[Device] API V1 Removal:**The Device API V1 has been fully removed. Device API V2 is now the only supported device API path. Applications still using V1 interfaces must migrate to V2. ([#1342](https://github.com/ai-dynamo/nixl/pull/1342))**[Device] MemoryView to MemView Rename:**Device API V2 naming has been normalized from`MemoryView`

to`MemView`

across all interfaces. Downstream code should update symbol references accordingly. ([#1337](https://github.com/ai-dynamo/nixl/pull/1337))**[Config] New Configuration Model:**Runtime configuration now follows the new two-phase environment/API configuration framework. Existing environment variable and API-based configuration patterns should be reviewed against the new model. ([#1301](https://github.com/ai-dynamo/nixl/pull/1301),[#1346](https://github.com/ai-dynamo/nixl/pull/1346))

## Enhancements

### Performance

**[Core] Transfer Request Optimization:**Optimized`createXferReq`

performance to reduce overhead in the hot transfer request creation path. ([#1338](https://github.com/ai-dynamo/nixl/pull/1338))**[Core] Descriptor List Iteration:**Optimized`nixlDescList`

iteration for faster descriptor traversal during transfer operations. ([#1322](https://github.com/ai-dynamo/nixl/pull/1322))**[Telemetry] Reduced Runtime Overhead:**Optimized`nixlTelemetry::addXferTime`

for lower per-transfer telemetry cost. ([#1365](https://github.com/ai-dynamo/nixl/pull/1365))**[Telemetry] Remove Backend Export:**Removed backend telemetry export to eliminate unnecessary overhead in the telemetry pipeline. ([#1364](https://github.com/ai-dynamo/nixl/pull/1364))**[UCCL] Batch Transfer Simplification:**Simplified and optimized UCCL for batch transfer workflows, reducing per-transfer overhead. ([#1271](https://github.com/ai-dynamo/nixl/pull/1271))**[UCX] Removed Extra Copy:**Eliminated an unnecessary data copy from`prepMemoryView`

in the UCX plugin, reducing memory transfer overhead. ([#1261](https://github.com/ai-dynamo/nixl/pull/1261))**[Core] Serialization Optimizations:**Added validation checks and small optimizations to serialization/deserialization utilities. ([#1277](https://github.com/ai-dynamo/nixl/pull/1277))

### Networking & Backend

**[Libfabric] Remove Post-Operation Retry Delay:**Removed the delay between post-operation retries in the Libfabric backend, reducing latency for retry-sensitive workloads. ([#1335](https://github.com/ai-dynamo/nixl/pull/1335))**[Libfabric] TCP Provider Fix:**Fixed TCP provider behavior in the Libfabric backend for correct operation on TCP-based fabrics. ([#1348](https://github.com/ai-dynamo/nixl/pull/1348))**[Libfabric] EFA Hardware Warning:**Added a warning when EFA hardware is present but the Libfabric backend is not selected, improving user guidance during initialization. ([#1287](https://github.com/ai-dynamo/nixl/pull/1287))**[UCX] VRAM Memory-Type Validation:**NIXL now raises an error when UCX incorrectly reports VRAM memory as host memory, preventing silent misclassification that could cause data corruption. ([#1385](https://github.com/ai-dynamo/nixl/pull/1385),[#1393](https://github.com/ai-dynamo/nixl/pull/1393))**[UCX] Targeted GDA Configuration:**RC GDA configuration is now applied only when relevant UCX transports are active, avoiding unnecessary configuration side-effects. ([#1347](https://github.com/ai-dynamo/nixl/pull/1347))**[UCX] Utils Refactoring:**Minor refactoring of UCX backend utility code for improved maintainability. ([#1291](https://github.com/ai-dynamo/nixl/pull/1291))**[Core] Memory Handling Refactor Preparation:**Refactored internal core/agent memory handling structures in preparation for follow-on memory management improvements. ([#1361](https://github.com/ai-dynamo/nixl/pull/1361),[#1370](https://github.com/ai-dynamo/nixl/pull/1370))**[Core] Listener Error Reporting:**Fixed incorrect error reporting in the core metadata listener. ([#1345](https://github.com/ai-dynamo/nixl/pull/1345))

### NIXL-EP Example Improvements

**Release Build Tuning:**Disabled fast fault detection for release builds to reduce overhead in production deployments. ([#1275](https://github.com/ai-dynamo/nixl/pull/1275))

### Build & CI

**CI: GPU Test Migration to Slurm:**Moved GPU tests to Slurm-based scheduling with improved allocation timeouts and test timeout handling for more reliable GPU CI execution. ([#1250](https://github.com/ai-dynamo/nixl/pull/1250),[#1366](https://github.com/ai-dynamo/nixl/pull/1366),[#1336](https://github.com/ai-dynamo/nixl/pull/1336),[#1318](https://github.com/ai-dynamo/nixl/pull/1318))**CI: Build Abort Logic:**Improved abort logic for obsolete builds and added automatic cancellation of previous dispatcher builds for the same PR. ([#1317](https://github.com/ai-dynamo/nixl/pull/1317),[#1281](https://github.com/ai-dynamo/nixl/pull/1281))**CI: Mooncake Non-Interactive Build:**Configured Mooncake builds to run without interactive prompts. ([#1290](https://github.com/ai-dynamo/nixl/pull/1290))**CI: GHA Runner Pinning:**Pinned GitHub Actions runner versions and kubectl for improved CI stability. ([#804](https://github.com/ai-dynamo/nixl/pull/804))**CI: Demo Pinning:**Pinned ci-demo to the`stable_nixl`

tag for reproducible demo builds. ([#1343](https://github.com/ai-dynamo/nixl/pull/1343))**CI: UCX Bug Workaround:**Added a workaround for a UCX bug affecting CI test runs. ([#1310](https://github.com/ai-dynamo/nixl/pull/1310))**Build: Wheel Environment Updates:**Upgraded hwloc in the wheel build environment, disabled nvlm in manylinux Dockerfile, and updated S3 SDK version. ([#1396](https://github.com/ai-dynamo/nixl/pull/1396),[#1403](https://github.com/ai-dynamo/nixl/pull/1403),[#1387](https://github.com/ai-dynamo/nixl/pull/1387))**Build: Meson Device API V2 Fix:**Fixed the`ucx_gpu_device_api_v2_available`

detection in`meson.build`

. ([#1316](https://github.com/ai-dynamo/nixl/pull/1316))**Code Quality Automation:**Added CodeRabbit configuration for AI-assisted code reviews and expanded the code style guide for contributor consistency. ([#1293](https://github.com/ai-dynamo/nixl/pull/1293),[#1143](https://github.com/ai-dynamo/nixl/pull/1143))

### Benchmarks

**[nixlbench] Aggregate BW Fix:**Fixed aggregate bandwidth calculation in pairwise single-group mode. ([#1299](https://github.com/ai-dynamo/nixl/pull/1299))**[nixlbench] SHA256 Checksum:**Switched to SHA256 checksum algorithm when uploading test objects for READ tests. ([#1286](https://github.com/ai-dynamo/nixl/pull/1286))**[nixlbench] GUSLI READ Fix:**Fixed GUSLI READ consistency check failure and cleanup crash. ([#1300](https://github.com/ai-dynamo/nixl/pull/1300))**[nixlbench] CLI Simplification:**Reduced the number of CLI argument combinations in benchmark test matrix. ([#1363](https://github.com/ai-dynamo/nixl/pull/1363))

### Documentation

**Code Style Guide:**Expanded the code style guide with additional guidance for contributors. ([#1143](https://github.com/ai-dynamo/nixl/pull/1143))

## Bugfixes

**[OBJ/S3 CRT] Multipart Sizing:**Aligned CRT`partSize`

and multipart upload threshold with the CRT minimum part size limit, preventing invalid multipart configurations. ([#1368](https://github.com/ai-dynamo/nixl/pull/1368))**[Libfabric] Unit Test Regression:**Fixed a regression in Libfabric unit tests and updated related README and comments. ([#1394](https://github.com/ai-dynamo/nixl/pull/1394))**[Libfabric] TCP Provider:**Fixed TCP provider behavior for correct operation on TCP-based fabrics. ([#1348](https://github.com/ai-dynamo/nixl/pull/1348))**[Core] Worker File Offset:**Fixed`file_offset`

calculation in`nixl_worker`

. ([#1399](https://github.com/ai-dynamo/nixl/pull/1399))**[Core] Listener Error Reporting:**Fixed wrong error reporting in the core metadata listener. ([#1345](https://github.com/ai-dynamo/nixl/pull/1345))**[Core] Metadata Listener Setup:**Fixed silent failure on metadata listener socket setup, improving error visibility. ([#1371](https://github.com/ai-dynamo/nixl/pull/1371))**[Core] Metadata Test Coverage:**Handled all error message cases in metadata test for complete error path coverage. ([#1372](https://github.com/ai-dynamo/nixl/pull/1372))**[UCX] VRAM Misclassification:**Fixed silent VRAM-as-host-memory misclassification by raising an explicit error when UCX reports incorrect memory types. ([#1385](https://github.com/ai-dynamo/nixl/pull/1385),[#1393](https://github.com/ai-dynamo/nixl/pull/1393))**[UCX] Worker Test:**Fixed`ucx_worker_test`

for the`USE_VRAM`

case. ([#1373](https://github.com/ai-dynamo/nixl/pull/1373))**[POSIX] Naming:**Fixed POSIX plugin naming conventions. ([#1296](https://github.com/ai-dynamo/nixl/pull/1296))**[Core] String Utility Cleanup:**Removed deprecated`strEqual`

and cleaned up common string utility tools. ([#1391](https://github.com/ai-dynamo/nixl/pull/1391),[#1309](https://github.com/ai-dynamo/nixl/pull/1309))**[Core] CUDA Memory Init:**Fixed CUDA memory initialization ordering. ([#1360](https://github.com/ai-dynamo/nixl/pull/1360))

## Test Infrastructure

**Stricter Test Failures:**Updated Google Test harness to fail on unexpected error or warning log messages, improving detection of regressions. ([#1288](https://github.com/ai-dynamo/nixl/pull/1288))

-...

[Read more](https://github.com/ai-dynamo/nixl/releases/tag/v1.0.0)

## 0.10.1

# 0.10.1

## Summary

NVIDIA® NIXL Release 0.10.1 is a targeted maintenance release focusing on improvements to Rust bindings, Python packaging, and testing infrastructure.

## Rust Bindings

**Runtime Library Resolution**: Introduced`libnixl_capi.so`

, a shared library that exports`nixl_capi_*`

C symbols. This allows downstream consumers of the`nixl-sys`

Rust crate to load NIXL at runtime without requiring build-time linking. The NIXL stubs have been rewritten from abort-on-call to use`dlopen`

/`dlsym`

for lazy forwarding to the real implementation ([#1358](https://github.com/ai-dynamo/nixl/pull/1358)).**Build Checks**: Added a`libnixl.so`

existence check in`build.rs`

before attempting to link. This ensures the fallback to stubs works correctly when`nixl-sys`

is used as a git dependency where headers are available but libraries are not installed ([#1358](https://github.com/ai-dynamo/nixl/pull/1358)).

## Python Packaging & Testing

**Exact Version Pinning**: Pinned the Python CUDA-specific dependencies (`nixl-cu12`

and`nixl-cu13`

) to exact versions in the`nixl`

meta-package. This prevents version mismatches and ensures consistent environments when installing the meta-package ([#1354](https://github.com/ai-dynamo/nixl/pull/1354)).**Testing Infrastructure**: Added support for running Python tests with a pre-created virtual environment (with support for both standard`pip`

and`uv pip`

), improving CI flexibility and local development workflows ([#1353](https://github.com/ai-dynamo/nixl/pull/1353)).

Full Changelog: [0.10.0...0.10.1](https://github.com/ai-dynamo/nixl/compare/0.10.0...0.10.1)