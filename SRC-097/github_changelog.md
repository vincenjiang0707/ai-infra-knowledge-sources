# Changelog (aggregated from releases.body)

> releases: 27

## 0.1.0 (2025-03-18)

**NVIDIA Inference Xfer Library (NIXL)** is targeted for accelerating point to point communications in AI inference frameworks such as NVIDIA Dynamo, while providing an abstraction over various types of memory (e.g., CPU and GPU) and storage (e.g., file, block and object store) through a modular plug-in architecture.

### NIXL features
#### Core Transfer Capabilities
* Accelerated point-to-point communications for AI inference workloads
* Efficient zero-copy memory transfer between CPU and GPU
* Direct GPU-to-GPU transfer with RDMA support via UCX
* Asynchronous transfer operations with completion notifications
#### Memory Abstraction
* Unified interface across heterogeneous memory types (DRAM, VRAM)
* Transparent handling of different storage backends (file, block, object)
* Intelligent buffer management for optimal data placement
#### Metadata Management
* Lightweight serialization system for transfer descriptors
* Cross-platform memory region exchange
* Zero-overhead lookup mechanisms for registered memory
#### Plugin Architecture
* Modular design enabling custom communication backends
* UCX and GPU Direct Storage plugins for high-performance networking and storage
* Extensible framework for various types of backends to perform data transfer

## 0.1.1 (2025-04-11)

## What's Changed

* Auto register-deregister by @mkhazraee in #56 and #55 and #128 
* Multi-Object (MO) UCX backend implementation to support multi-GPU buffers in a single transfer request by @artpol84 in #58 
* Return bytes for notifications in Python API by @tstamler in #109
* Add typing and backend selection to Python API by @tstamler in #86
* Discover plugins in directory by @aranadive in #82
* Allow dynamic linking of plugins in wheel by @tstamler in #94
* Update dockerfiles and use cuda-dl-base image by @aranadive in #106 and @nv-anants in #115
* Add Doxygen for c++ and python APIs by @vvenkates27 in #32 and @tstamler in #127
* Improved examples for GDS by @vvenkates27 in #114, and initial Pytest implementation by @tstamler in #100
* Switch to C++17 by @aranadive in #104
* Add code of conduct for project by @saturley-hall in #102
* Several bug fixes, performance improvements and clarifications in the documentation
* Improved tests throughout, for pytest, agent, and GDS

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.1.0...0.1.1

## 0.2.0 (2025-05-01)

## What's Changed

### New Features
- Metadata exchange APIs
  - API for exchanging metadata through listener thread
  - API for getting/sending partial agent metadata
  - New APIs can exchange metadata in peer-to-peer mode (sockets) or central metadata server (ETCD)
  - See Doxygen documentation for new APIs, and README for ETCD instructions
- Improved transfer preparation backend API for better performance with storage backends
- Basic C and Rust bindings
- Thread safe mode that can be enabled through agent config
- Introducing nixlbench - our NIXL performance benchmarking suite
  - https://github.com/ai-dynamo/nixl/blob/main/benchmark/nixlbench/README.md

### Developer Tools
- Logging infrastructure to enable new developers to use NIXL logging macros
- Debug mode infrastructure to enable new features that will only run in debug mode
- Integrate Abseil for thread and logging features

### Testing and Performance
- AWS EFA Testing with latest version of UCX
- Gtest infrastructure and mock backend for unit testing
- Various Bug fixes, optimizations and documentation clarification

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.1.1...0.2.0

## 0.2.1 (2025-05-22)

## What's Changed

### New Features
- Added **Mooncake backend** to support the Mooncake Transfer Engine.
- **ARM (aarch64)** build support for broader platform compatibility.
- Added **POSIX plugin** with support for both AIO and io_uring.
- Enhanced **NIXLBench** with improved barrier handling, environment persistence, and graceful termination.
- Enabled **multi-threaded test execution** in `nixl_test`.
- Enhanced **UCX backend** with `cuda-ipc` support and optimized request completion notifications.

### Developer Enhancements
- Unified and improved **logging infrastructure** across components.
- Applied modern C++ practices: `using` declarations, smart pointers, and cleaner memory management.
- Improved Python usability: clarified GDS dependencies, updated examples, and streamlined test behavior.
- Documentation updates: plugin requirements, ETCD hostname usage, PyPI references, and ownership metadata.

### Testing & Performance
- Extended unit and integration test coverage using `pytest` and `gtest`.
- Improved CI workflows: system info logging, updated runner labels, and test configuration controls.
- Resolved performance and stability issues:
  - Fixed memory leak in UCX `genNotif()`
  - Addressed descriptor list and statistic calculation bugs in NIXLBench
  - Minor communication reliability fixes in the Agent

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.2.0...0.2.1

## 0.3.0 (2025-06-02)

## What's Changed
### New Features

* **New Backends & Plugins**:

  * Added 3FS backend support
  * Added POSIX plugin support in `nixlbench`

* **Architecture Support**:

  * Enabled ARM (aarch64) build support for `nixl-sys`

* **Cost & Performance Tools**:

  * Implemented cost estimation and exposed a Python API
  * Added NIXL KV Cache Benchmark to simulate KV Cache Transfers through NIXL

* **Synchronization Improvements**:

  * Introduced a new synchronization read-write locking mode
  * UCX\_MO now sends completion notifications in `postXfer`
  * Included missing UCX backend options


### Developer Enhancements

* **UCX Improvements**:

  * Refactored plugin glue logic and removed busy-polling in progress thread
  * Enabled multi-worker support
  * Improved error handling, debug logging, and support for multi-GPU and CUDA IPC
  * Added configuration options for error handling and UCX endpoint estimation
  * Set CUDA context for remote MD operations
  * Improved UCX backend read/write operation handling

* **Build & Packaging**:

  * Added crate metadata and updated Python dependencies
  * Fixed build issues on RedHat8, Manylinux, and 3FS plugin
  * Removed unused packages and improved consistency in naming

* **Code Quality & Maintenance**:

  * Marked internal methods with `const`
  * Updated CODEOWNERS, attribution files, and third-party notices
  * Ignored crate files in pre-commit checks

* **Rust Bindings**:

  * Improved Rust API with missing functions, reordering, and better test coverage
  * Fixed build and example issues

* **Agent & Metadata Handling**:

  * Improved ETCD metadata fetch and invalidation using watchers
  * Updated agent API to require labels
  * Removed unsafe move semantics and applied socket timeout handling


### Testing & Performance

* **CI & Infrastructure**:

  * Added AWS EFA testing infrastructure
  * Enabled container builds with UCX from source

* **Stability & Reliability**:

  * Applied timeout to polling thread and agent socket connections
  * Fixed memory leaks and double-destroy issues in batch I/O
  * Resolved multiple build and runtime bugs for better test coverage and platform support
 
### Known Issues
  * Arm builds for GDS plugin, nixl, nixlbench aren't supported correctly for this release - #273, #414

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.2.1...0.3.0

## 0.3.1 (2025-07-01)

## Summary
NVIDIA® NIXL Release 0.3.1 delivers key improvements in **performance**, **portability**, and **developer experience**.

- **New capabilities**:  
  Introduced GDAKI (GPUDirect Async Kernel-Initiated) transfers using DOCA RDMA (our Data-Center-on-a-Chip framework with Remote Direct Memory Access). We also added smarter runtime defaults and enhanced Python and Rust bindings for streamlined LLM runtime development.

- **Stronger infrastructure**:  
  Refactored the UCX backend for improved performance and clarity, added support for AArch64 and manylinux (Python's portable binary distribution standard), and cleaned up the API structure for better maintainability.

- **Improved testing**:  
  Integrated **Blossom-CI** (our custom continuous integration pipeline), expanded multi-threaded and RDMA test coverage, and enhanced logging and diagnostics for faster issue resolution.

## New Features

- Added GDAKI support integrating DOCA GPUNetIO and RDMA in stream mode  
- Enabled listener-side invalidation messaging and socket-based transfers  
- Expanded `nixlbench` to configure GDS batch and pool sizes  
- Auto-detection of NIXL library path based on host CPU architecture  
- Enabled VMM CUDA memory allocation in `nixlbench`  
- Ensured that CPU is used as default device when CUDA is disabled  
- Improved Python bindings with NumPy array support and performance tuning  
- Enhanced Rust bindings with usability improvements and feature support  

## Developer Enhancements

- Refactored UCX backend including RMA rails configuration and worker logic  
- Improved UCX progress engine granularity for better performance  
- Fixed memory registration checks in UCX memory operations  
- Simplified and corrected UCP AM header usage  
- Optimized backend serialization to include only supported options  
- Introduced `Dockerfile.manylinux` for Python packaging compatibility  
- Added build and containerization support for AArch64  
- Cleaned up UCX plugin notification list handling  
- Updated Rust and C++ APIs for better structure and public access clarity  
- Fixed missing headers in 3fs plugin and ensured build consistency  
- Standardized naming conventions in benchmarking tools  
- Expanded contributor roles and ownership metadata  
- Streamlined dependencies and build options for GDS and IB devices  

## Testing & Performance

- Enabled multi-threaded GTest transfers for concurrency testing  
- Integrated `blossom-ci` for more robust CI builds and EFA test debugging  
- Increased CI timeouts and polling intervals for more reliable AWS tests  
- Improved logging in plugin tests for better visibility and debugging  
- Added support for ARM builds and cross-platform validation  
- Fixed UCX build issues with IB dependencies and container options  
- Ensured accurate attribution updates and release version tagging 

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.3.0...0.3.1

## 0.4.0 (2025-07-10)

## Summary
NVIDIA® NIXL Release 0.4.0 delivers key improvements in performance, portability, and developer experience.
* New capabilities:
Introduced two new storage plugins. GDS (GPUDirect Storage) multi-threaded and AWS S3 (Amazon Simple Storage Service). We also integrated Custom Traffic Performance Test (CTPerf) into our benchmarks to measure KV Cache Transfers over network.

* Stronger infrastructure:
Improved the existing backends UCX, GDS, POSIX, GPUNetIO, boosting performance and extending functionality. Enhanced python wheels adding ARM 64 support, enabling compression.

* Improved testing:
Expanded `nixlbench` to support Mooncake and HF3FS backends. Integrated clang-format stage into CI, enhanced logging in various CI stages.

## New Features
* Added GDS multi-threaded storage plugin
* Added OBJ storage plugin for AWS S3 generic objects
* Integrated CTPerf into `kvbench`
* Expanded `nixlbench` to support Mooncake and HF3FS backends

## Developer Enhancements
* Improved performance of UCX plugin for EFA
* Fixed Dockerfile to support setups with different versions of CUDA drivers
* Added missing UCX plugins to enable CUDA and RDMACM support in UCX backend
* Compressed wheels after patching to reduce the size of the wheels
* Added support for building python wheels on ARM 64
* Decreased the default number of GDS batches created to facilitate creating multiple NIXL agents
* Fixed GPUNetIO plugin usage by `nixlbench`
* Improved memory type detection in UCX backend
* Enabled reposting requests using POSIX backend
* Added support for self notification in UCX backend
* Upgraded ssl dependency for wheel
* Fixed python bindings to handle unsorted descriptor lists
* Improved NIXL logging for better debugging
* Enhanced resource management and error handling in UCX backend
 
## Testing
* Added clang-format CI stage to improve the quality of the code
* Removes automatic retry on AWS job failures, adds GitHub metadata tags for traceability and better debugging
* Renamed CI Docker images to explicitly show OS coverage in our test matrix
* Improved logging in AWS EFA tests for better visibility and debugging
* Added Jenkins job for `nixlbench` container builds
* Reduced gtest wall time improving error handling tests
* Fixed multi-threaded gtest output
* Enabled building with stub API in Rust bindings
* Fixed C++ examples to enable cmake build

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.3.1...0.4.0

## 0.4.1 (2025-07-24)

## Summary
NVIDIA® NIXL Release 0.4.1 delivers improvements in resiliency, and developer experience.
* Improved resiliency:
Advanced error handling is enabled in the UCX backend, ensuring that send requests are always completed even in case of remote failure.
* Stronger infrastructure:
Added NIXL plugins into the packaged python wheel, and improved NIXL plugins loader, to facilitate usage of NIXL installed as a Python package.

## Developer Enhancements
* Enabled advanced error handling in UCX backend
* Added NIXL plugins to the wheel
* Improved NIXL plugins loader
* Enhanced resource management in UCX backend
* Extended contributing and coding style guidelines

## Testing
* Enabled CI running on GPU
* Extended gtest covering Agent class functionality

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.4.0...0.4.1

## 0.5.0 (2025-08-06)

## Summary
NVIDIA® NIXL Release 0.5.0 introduces new API capabilities, major improvements to the build, performance infrastructure and several bug fixes.

*   **New Capabilities:**
    New `queryMem` API for inspecting memory registrations. New Telemetry API for tracking transfer time. Updated H3FS backend to support zero-copy using shared memory to improve performance.

*   **Stronger Infrastructure:**
    Significantly improved the build and testing infrastructure. Build portability was increased with fixes for RHEL8, and CI stability has been hardened. Smaller wheels and robust plugin dependency loading improve deployment.

## New Features
*  Added `queryMem` API to query properties of registered memory
*  Added telemetry infrastructure that is used to track transfer time for performance analysis. 
*  Added a configurable checksum toggle for the Object (S3) plugin
*  Expanded `nixlbench` to support the Object (S3) storage plugin

## Infrastructure and Performance Improvements
*  The HF3FS backend now uses shared memory to significantly improve performance by avoiding memory copy.
*  Added a comprehensive Backend Developer Guide to the documentation
*  Improved `nixlbench` with page-aligned memory allocation for better performance
*  Enabled running `nixlbench` tests in parallel using a shared etcd server
*  Unified and simplified the Python wheel building process
*  Improved python logging project-wide
*  Reduced the size of Python wheels
*  Added `etcd` gtests to the CI pipeline
*  Added gtest infrastructure for plugins
*  Fixed various build issues for `etcd-cpp-api`, Meson, and RHEL8 environments
*  Fixed an issue in `registerMem` for the Object plugin
*  Fixed the Rust cargo package definition

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.4.1...0.5.0

## 0.5.1 (2025-08-28)

## Summary
NVIDIA® NIXL Release 0.5.1 delivers major improvements in performance and scalability, enhances Rust language support, and rolls out key infrastructure for performance analysis. This release successfully delivers on roadmap items including a new core threadpool and telemetry export capabilities.

*   **Performance and Scalability:**
    Introduces the UCX backend threadpool for parallel posting of large requests, reducing latency by up to 30-87% in production workloads.
*   **Telemetry Infrastructure:**
    Introduces a telemetry framework that records and exports detailed transfer metrics, providing insights for performance analysis.
*   **Enhanced Rust Integration:**
    Rust support has been significantly expanded with full build and CI integration using Meson, CI-based testing, and the addition of new API bindings.
*   **Stability and Resiliency:**
    Fixes multiple critical stability issues that may cause crashes, and improves error handling and cleanup.

## New Features
*   Added a telemetry framework to track and export detailed transfer data (#562).
*   The `queryMem` API is now available in the Rust bindings (#620).
*   The Mooncake plugin now supports the `notify` operation (#493, #696).
*   Added `nixlbench` support for the GDS_MT backend (#671).

## Performance
*   Introduced a threadpool to the UCX backend for parallel posting of large requests, significantly improving performance and scalability (#573, #606).

## Observability
*   Improved logging throughout the Python codebase (#633).
*   `nixlbench` now measures tail latency and latency breakdown for performance analysis (#591).

## Bugfixes
*   Reworked metadata listener connection logic to fix a stack corruption bug (#681).
*   Fixed a race condition in notification handling (#649).
*   Improved error handling for canceled transfers (#677) and agent metadata cleanup on failure (#509).
*   Fixed a bug in the GDS plugin related to `CUfileDescr_t` initialization (#721).
*   Corrected `nixlbench` implementation for `--num_files` and `READ` mode (#635).
*   Resolved a build regression in the Mooncake plugin (#710).

## Dependencies
*   UCX dependency upgraded to 1.19.0 (#673).
*   GDRCopy dependency upgraded to 2.5.1 (#712).

## Build and Test Infrastructure
*   Enabled the build, installation, and testing of Rust bindings with Meson and CI (#290).
*   Added a new CI check to detect excessively large pull requests (#627).
*   Unified the container builder to support both `NIXL` and `NIXLBench` (#567).
*   Implemented timeouts for CI test steps to prevent hangs (#660).
*   Improved CI test scripting to avoid TCP port collisions (#568).
*   Simplified the project's Docker build process (#604) and fixed build failures on Ubuntu 22.04 (#653).

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.5.0...0.5.1

## 0.6.0 (2025-09-18)

## Summary
NVIDIA® NIXL Release 0.6.0 introduces preview API support for the powerful new Device API for GPU-initiated operations, extends telemetry with per-request metrics, and improves language binding support. This release delivers key roadmap items for GPU-native workflows and enhances observability, performance, and stability.

*   **Device API for GPU-centric Workflows:**
    Introduces preview API support for the GPU-side Device API, enabling applications to initiate data transfers directly from GPU kernels. This significantly reduces host-GPU synchronization overhead for GPU-native workloads.
*   **Granular Performance Telemetry:**
    The telemetry framework is extended with a new API to retrieve detailed performance metrics on a per-request basis directly from the client applications, enabling finer-grained performance analysis and easier debugging.
*   **Expanded Language Bindings:**
    Python and Rust bindings have been substantially enhanced, adding support for new core APIs and introducing more idiomatic object-oriented constructs in Python.
*   **Performance and Stability:**
    Delivers performance improvements for descriptor list handling, enhances plugin performance, and addresses several stability issues to improve overall robustness.

## New Features
*   Introduced preview API support for the NIXL Device API, enabling transfer requests to be created and signaled directly from GPU kernels (#704, #705, #749, #720).
*   Added the `getXferTelemetry` API to retrieve detailed metrics for individual transfers (#702).

## Performance
*   Improved the performance of the `populate` method for descriptor lists that are not fully sorted (#729).
*   Added mempool support to the HF3FS plugin for improved performance (#695).

## Bugfixes
*   [Core] Fixed crash triggered by use-after-free where requests were deleted without ownership (#782, #783).
*   [Core] Workaround for meson CUDA detection failure on ARM builds, resulting in incomplete CUDA support (#743)
*   [UCX] Corrected error-handling logic in the `checkXfer` function (#690).
*   [Bindings] Python wheel packaging now excludes `libcuda*` and `libcufile` to avoid bundling system libraries (#745).
*   [Mooncake Plugin] Fixed an issue where `DOWN` network interfaces were not correctly filtered (#406).
*   [Mooncake Plugin] Fixed the destruction of notification messages (#739).

## API Changes
*   Removed the `progress` method and its indicator from the Storage Backend API (#701).
*   Removed the `sorted` flag from the user-facing `nixlDescList` (#731).
*   Removed unused `has_overlaps` and `overlaps` methods from `nixlDescList` (#718).
*   Enhanced the plugin manager to reduce boilerplate needed to create new plugins (#622).

## Bindings
*   Rust bindings now include `get_local_partial_md`, `send_local_partial_md`, `query_xfer_backend`, `make_xfer_req`, and `prepare_xfer_dlist` (#684, #693).
*   Added idiomatic Python objects for transfer and descriptor list handles (#737).
*   Enabled packaging of the Object storage plugin in the Python wheel (#755).

## Dependencies
*   DOCA dependency upgraded to 3.1 (#753).

## Benchmarks
*   Added bandwidth reporting to `kvbench` (#670).
*   `kvbench` now supports all available plugins (#754).
*   Enabled passing `num_workers` to the UCX backend from `nixlbench` (#708).
*   Improved error handling in `nixlbench` and `kvbench` (#740, #757).
*   Added error logging throughout the `nixl_agent` Python code (#738).
*   Fixed `nixlbench` container builds by ensuring PyTorch is installed with CUDA support (#758, #769).
*   Fixed an error in the communication barrier when testing with block sizes larger than 1MB (#722).

## Build and Test Infrastructure
*   Added a fallback to manual CUDA detection in Meson and build scripts when auto-detection fails (#743, #777, #778).
*   Improved reliability of Rustup installation in CI (#725).
*   Used standard signal names in Python test scripts for better portability (#717).
*   Fixed various CI image build and trigger issues (#744, #748).

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.5.1...0.6.0

## 0.6.1 (2025-10-09)

## Summary
NVIDIA® NIXL Release 0.6.1 introduces a new Libfabric plugin for high-performance networking on AWS, expands language binding support and improves stability.

*   **Libfabric Networking for AWS:**
    Introduces a new Libfabric plugin to leverage AWS Elastic Fabric Adapter (EFA) for high-performance, low-latency communication.
*   **Language Bindings:**
    Rust bindings now include support for agent configuration and the `getXferTelemetry` API, improving integration and observability for Rust applications.
*   **Performance and Stability:**
    Resolves several critical stability issues to enhance robustness.

## New Features
*   Introduced a new Libfabric plugin with topology-aware support for AWS EFA devices (#784, #801, #802, #809, #817, #826, #831, #833, #850, #852, #866, #867, #868).
*   Added an agent configuration flag to enable or disable telemetry capture on a per-agent basis (#764).
*   Made the ETCD watch timeout configurable in the metadata listener, to avoid timeouts under heavy load conditions (#766).
*   Added a `ca_bundle` option to the Object Storage plugin for compatibility with S3-compatible storage using self-signed certificates (#806).

## Bugfixes
*   [Core] Fixed a critical use-after-free error on disconnect where requests could be deleted without proper ownership (#782).
*   [Listener] Prevented a crash in the etcd client on multiple metadata updates received in rapid succession (#765).
*   [Telemetry] Addressed minor issues in the telemetry framework (#750).

## Bindings
*   [Rust] Added bindings for ThreadSync and AgentConfig (#824).
*   [Rust] Exposed the `getXferTelemetry` API in the Rust bindings for retrieving per-request performance metrics (#823).

## Dependencies
*   The UCX dependency is now optional, allowing NIXL to be built without UCX (#825).
*   Upgraded the DOCA dependency to 3.1 in the `nixlbench` container (#760).

## Benchmarks
*   Fixed the `nixlbench` container runtime by ensuring the Python virtual environment is activated correctly (#848).
*   Fixed a function signature mismatch in the NVSHMEM worker (#786).

## Build and Test Infrastructure
*   Improved CUDA detection in `nixlbench` build scripts with a fallback mechanism (#777).

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.6.0...0.6.1


## 0.7.0 (2025-10-24)

## Summary
NVIDIA® NIXL Release 0.7.0 introduces the new GUSLI storage plugin, adds build support for the CUDA 13.0 toolkit, and delivers key improvements to the Libfabric, UCX and GPUNetIO backends.

*   **GUSLI Storage Plugin:**
    Introduces a new storage backend based on [NVIDIA GUSLI](https://github.com/NVIDIA/GUSLI) for high-performance access to flash storage.
*   **CUDA 13 Build Support:**
    Enables NIXL and the `nixlbench` suite to be built from source with CUDA 13.0, ensuring compatibility with the latest drivers and libraries. Official binary packages with CUDA 13.0 support are planned for a future release.

## New Features
*   Introduced the GUSLI storage plugin for high-throughput, low-latency I/O (#887).

## Improvements
*   [Build] Added support for building NIXL and `nixlbench` from source with CUDA 13 (#820).
*   [Libfabric] Added support for non-GDR instances on AWS and resolved python wheel compatibility issues (#901, #937).
*   [Device API] Improved support for GPU-initiated UCX transfers in MoE workloads with easier to use APIs and lower latency (#815).

## Bugfixes
*   [Libfabric] Addressed several stability issues, including double-free errors in topology initialization, resource cleanup on disconnect, and handling of asymmetrical rail configurations in heterogeneous nodes (#839, #860, #926).
*   [Libfabric] Improved resilience by manually progressing the completion queue when resources are unavailable and adding retry logic for failed operations (#856, #859).
*   [Libfabric] Fixed EFA device discovery to correctly identify device IDs (#876).

## Dependencies
*   [GPUNetIO] Upgraded the GPUNetIO backend to the DOCA 3.1 Verbs library (#733).

## Bindings
*   The Python wheel no longer bundles `libfabric`, `libefa`, and `libhwloc`, as the libraries are available in many base images for AWS and this prevents version mismatch. (#937).
*   Added a new Python example for remote storage operations (#841).

## Benchmarks
*   Added `nixlbench` support for the new GUSLI backend (#897, #929).
*   Improved `nixlbench` flexibility by making `etcd` optional for storage backends and fixing logic for key collisions (#862, #878).
*   Fixed an API parameter mismatch in the `nixlbench` POSIX benchmark (#880).

## Build and Test Infrastructure
*   Expanded CI coverage by enabling tests on DGX systems and adding GPU-specific tests for `nixlbench` (#834, #780).
*   Resolved a package installation failure for `libibverbs-dev` on the CUDA 13 base container image (#889).
*   Improved the build system to avoid building gtest when CUDA or UCX dependencies are not found (#925).
*   Added a backend selection option for easier debugging of different transfer backends (#822).
*   Refined release build packaging to correctly manage the inclusion of tests and examples (#872, #896).

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.6.1...0.7.0

## 0.7.1 (2025-11-06)

## Summary
NVIDIA® NIXL Release 0.7.1 is a maintenance release that introduces Python packaging support for CUDA 13.0, improves the interface of the Device API, and resolves critical issues in the Libfabric backend.

*   **CUDA 12 and CUDA 13 Python Wheels:**
    This release provides officially supported CUDA 13 Python wheels, splitting the packaging into a `nixl` meta-package and the platform-specific packages `nixl-cu12` and `nixl-cu13`. More information below under `Python packaging changes`.
*   **Device API: Single-thread Support for Multiple Queue Pairs:**
    Single-threaded applications can now drive multiple QPs from a single thread, for higher performance without the overhead of creating multiple agents or multiple threads.
*   **Device API: Improved Asynchronous API Handling:**
    The Device API plugin's `post` functions were changed to return `NIXL_IN_PROG` to signal that an operation has been submitted but is not yet complete, improving the predictability and performance of asynchronous calls.

## Python packaging changes
NIXL is now packaged using a `nixl` PyPI meta-package and CUDA platform-specific wheels for CUDA 12 (`nixl-cuda12`) and CUDA 13 (`nixl-cuda13`). (#915, #954, #956, #966).

### PyPi users

The desired wheel can now be installed from PyPi with `pip install nixl[cu12]` or `pip install nixl[cu13]`.

For backwards compatibility, `pip install nixl` installs automatically `nixl[cu12]`, continuing to work seamlessly for CUDA 12 users without requiring changes to downstream project dependencies.

CUDA 13 users must use `pip install nixl[cu13]` to install NIXL.

If both `nixl-cu12` and `nixl-cu13` are installed at the same time in an environment, `nixl-cu13` takes precedence.

### Python installation from source

Pip installations from source code through `pip install .` now require additional steps to build and install the `nixl` meta-package:

On CUDA 12:

```
pip install .
pip install meson meson-python pybind11 tomlkit
meson setup build
ninja -C build
pip install build/src/bindings/python/nixl-meta/nixl-*-py3-none-any.whl
```

On CUDA 13:

```
pip install .
pip install meson meson-python pybind11 tomlkit
./contrib/tomlutil.py --wheel-name nixl-cu13 pyproject.toml
meson setup build
ninja -C build
pip install build/src/bindings/python/nixl-meta/nixl-*-py3-none-any.whl
```

See also [this](https://github.com/ai-dynamo/nixl/blob/4d6cdcd203aae581030b2908140ad966b7a5d4b5/benchmark/nixlbench/contrib/Dockerfile#L208) for a full example in docker.

## API changes
*   [Device API] Asynchronous `post` functions now return `NIXL_IN_PROG` to signal that an operation is in flight, providing a clearer status for non-blocking calls (#911).
*   [Device API] Added support for `worker_id` selection in the backend, allowing for more granular performance tuning with multiple QPs driven by a single thread (#938).

## Bugfixes
*   [Libfabric] Corrected an issue with offset calculations that could cause data corruption in certain transfer scenarios (#883).
*   [Libfabric] Fixed a bug in handling asymmetrical rail configurations on heterogeneous nodes (#908).
*   [Libfabric] Addressed issues with metadata handling for partial and multi-load transfers (#976, #986).
*   [Bindings] Fixed an error in the Python API when `NIXL_LOG_LEVEL` was set to TRACE (#890).
*   [Plugins] Reduced logging noise by changing messages for plugins with missing external dependencies from `ERROR` to `INFO` (#967).

## Known issues
*   [GPUNETIO] The GPUNETIO plugin is not available in CUDA 13 environments. This will be addressed in a future release.

## Benchmarks
*   `nixlbench` now allows compilation even if the `etcd` development libraries are not found on the system (#959).
*   The `PostXferReq` timer in `nixlbench` was changed to provide more accurate latency measurements (#944).
*   For CUDA 13, the `nixlbench` PyTorch dependency is now installed from the stable channel (#943).

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.7.0...0.7.1

## 0.8.0 (2025-11-20)

## Summary

NVIDIA® NIXL Release 0.8.0 delivers significant performance improvements, major new capabilities, and important dependency updates. Key highlights include a massive optimization for large-batch workloads in the UCX backend, the introduction of a new POSIX backend using Linux AIO for high-performance storage I/O, and direct CUDA memory registration support for the Libfabric backend.

This version contains breaking changes, including the removal of the legacy Multi-Object UCX backend and an update to the minimum required Libfabric version. It also introduces support for Python 3.13 and changes the default build type to `Release` for optimized performance out of the box.

### Major Features & Improvements

*   **UCX Performance for Large-Batch Workloads:** The request handling mechanism in the UCX backend has been overhauled to reduce overheads. For workloads with large batches (~64k) of small messages (<1KB), as in `sglang` and other LLM inference engines that use paged attention, this change significantly reduces latency and improves time-to-first-token (TTFT). Internal benchmarks show a **~50% performance increase** in `nixlbench` and a **~20% TTFT reduction** in `sglang` for these scenarios. (#982)
*   **Linux AIO plugin for the POSIX backend:** The POSIX backend now leverages the Linux Asynchronous I/O (`AIO`) API where available. This provides a high-performance, asynchronous interface for data transfers to and from local storage. Internal benchmarks show an increase in read throughput for read sizes above 100 kB (#885)
*   **Libfabric CUDA Memory Registration:** The Libfabric backend can now directly register CUDA memory regions using `fi_mr_regattr`. Thus adds support for extended memory registration attributes and optimized RDMA behavior. (#960)
*   **Python:** Added support for Python 3.13. (#994)

### Breaking Changes

*   **UCX Multi-Object Backend Removed:** The legacy Multi-Object (UCX_MO) backend has been removed. Users should migrate to the primary UCX backend, which now incorporates multi-device support. (#898)
*   **Libfabric Minimum Version Increased:** The minimum required version of Libfabric has been raised to **v1.21.0** to support new features. (#961)
*   **Default Build Type is now `Release`:** When building from source, the default build type is now `Release` instead of `Debug`. This ensures that default builds are optimized for performance. (#869)

### API Changes

*   **[Rust]** New `RegDescList` and `XferDescList` APIs have been added to the Rust interface for descriptor management. (#828)
*   **[Python]** Obsolete and unused code from the Python API has been removed. (#985)

### Enhancements

*   **[Build]** The build system now searches for libraries in paths specified by the `NIXL_PREFIX` environment variable, making it easier to link against custom builds. (#998)

### Bugfixes

*   **[Core]** Metadata exchanges over sockets have been improved with better error handling. (#999)
*   **[Core]** The metadata exchange over sockets communication queue is now fully flushed before stopping the listener thread, preventing potential data loss during shutdown. (#830)
*   **[Libfabric]** Fixed multiple issues with metadata handling for partial loads and offset calculations that could lead to data corruption. (#969, #978)
*   **[Bindings]** Resolved a crash in Python examples that occurred when the `NIXL_PLUGIN_DIR` environment variable was not set. (#963)
*   **[Rust]** Fixed an issue that prevented Rust stubs from building correctly. (#1001)

### Benchmarks & Test Infrastructure

*   **[nixlbench]** Fixed a memory management bug related to `cudaFree`. (#965)
*   **[nixlbench]** The tool will now correctly exit with a failure code if an I/O vector consistency check fails. (#992)
*   **[CI]** Switched CI jobs from PyTorch-based images to `cuda-dl-base` images for better unification and consistency. (#924)

### Known Issues

* **[GPUNETIO]** The GPUNETIO plugin is not available in CUDA 13 environments. This will be addressed in a future release.

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.7.1...0.8.0

## 0.9.0 (2026-01-21)

## Summary
NVIDIA® NIXL Release 0.9.0 delivers significant new capabilities and performance improvements. Key highlights include the introduction of the **UCCL backend** for optimized collective communication, a new **Telemetry Plugin infrastructure** with Prometheus support, and the **NIXL-EP** example demonstrating expert-parallel dispatch. This release also adds support for **Python 3.14**, enables **Shared Memory for Libfabric** intra-node transfers, and includes important performance optimizations for core request handling.

This version contains breaking changes, specifically the removal of support for Python 3.9.

### Major Features
*   **UCCL Backend Integration:** Added support for the UCCL P2P backend, enabling efficient GPU memory transfers over RDMA. (#895)
* **Telemetry Plugin Infrastructure:** A new extensible telemetry plugin system has been introduced, allowing for custom metric exporters.
* **Prometheus Exporter:** A new plugin to export metrics to Prometheus. (#1091)
* **Cyclic Buffer Exporter:** A plugin for high-performance cyclic buffer telemetry. (#1088)
* **Plugin Manager:** Infrastructure to support loading and managing telemetry plugins. (#1070)
* **NIXL-EP (Elasticity Example):** Introduced `examples/device/ep`, a comprehensive example demonstrating expert-parallel dispatch and combine operations using the NIXL device API. This includes improved metadata fetching and CI integration. (#1043, #1132, #1104, #1077)
  * **Enable CUDA IPC NVLINK backend:** NIXL-EP now enables the CUDA IPC NVLINK backend for improved intra-node GPU communication. (#1099)
* **Libfabric Shared Memory Support:** Enabled the shared memory provider (`shm`) for NVLink intra-node transfers in the Libfabric backend. This improves performance for local GPU-to-GPU communication by leveraging NVLink without requiring network transport. (#1076)

### Breaking Changes
* **Python 3.9 Support Removed:** Support for Python 3.9 has been removed. The supported Python versions are now 3.10 through 3.14. (#1071)

### API Changes
* **[Python] Python 3.14 Support:** Added official support for Python 3.14. (#1071)
* **[Python] Explicit API Exports:** Python APIs are now explicitly exported using `__all__` to control the public namespace and cleaner imports. (#1062)
* **[Rust] Custom Backend Parameters:** Added support for passing custom backend parameters in Rust bindings. (#900)
* **[Rust] Descriptor Serialization:** Added `Serde` serialization support for `RegDescList` and `XferDescList`. (#829)
* **[Rust] Indexing Support:** Added `Index`/`IndexMut` and `get`/`get_mut` methods for descriptor lists. (#1003)

### Enhancements
**Performance**
* **[Core] Request Handling Optimization:** Implemented request handling optimizations to reduce overhead for large batches of small messages. (#1009)
* **[UCX] Relaxed Ordering:** Set `UCX_IB_PCI_RELAXED_ORDERING=try` by default to improve PCI performance where supported. (#1012)
* **[Libfabric] EFA Unsolicited Write Recv:** Added `FI_OPT_EFA_USE_UNSOLICITED_WRITE_RECV` option to disable unsolicited write receives on EFA RDM, reducing CQ overflows under high load. (#1084)
* **[Libfabric] Large Message Notifications:** Implemented notification fragmentation for large messages to better support large transfers (e.g., TensorRT-LLM disaggregated workloads). (#1182)
* **[NIXL-EP] Parallel Metadata Fetch:** Optimized connection establishment in NIXL-EP by parallelizing metadata fetches. (#1132)

**Build & CI**
* **Selective Plugin Building:** Added Meson options to selectively enable or disable specific plugins during build (`-Denable_plugins=...`). (#951)
* **CUDA 13 Support:** Updated CI infrastructure to support CUDA 13 for GPU tests. (#996)
* **POSIX Plugin Dependencies:** Fixed POSIX plugin dependency handling in Meson to resolve build issues with TRTLLM. (#1086)
* **Python License:** Fixed license identifier in Python packages to match the LICENSE file. (#1119)
* **manylinux wheel packaging:** Added the `uring` library to the manylinux 0.9.0 Docker image so it’s included with wheels (enables POSIX plugin access to performant async I/O options). (#1185)

**Documentation**
* **Libfabric Guide:** Improved clarity and grammar in the Libfabric README. (#1007)
* **Examples:** Enhanced the basic Python examples and `nixl_ep` documentation. (#1078, #1093)

### Bugfixes
* **[POSIX] AIO Resubmission:** Fixed a bug where the Linux AIO plugin could not correctly resubmit I/O requests. (#1020)
* **[Libfabric] Sockets Deadlock:** Fixed a connection deadlock with the sockets provider by reducing the CQ read timeout. (#1080)
* **[Libfabric] Topology Grouping:** Fixed GPU NIC grouping logic in `libfabric_topology` when multiple GPUs share a NIC. (#1024)
* **[Libfabric] GPU-to-EFA mapping:** Fixed GPU-to-EFA mapping by using PCI bus IDs instead of GPU IDs, ensuring correct device association. (#1184)
* **[Core] Metadata Crash:** Fixed a crash that occurred if a peer closed the connection during metadata exchange. (#854)
* **[Telemetry] Dangling Pointer:** Resolved a dangling pointer issue in `getName`/`getVersion` in the telemetry plugin. (#1148)
* **[Benchmark] nixlbench Memory:** `nixlbench` now allocates page-aligned memory by default to ensure consistency. (#1060)
* **[Python] venv Support:** Fixed Python test scripts to work correctly inside `uv` virtual environments. (#1106)
* **[UCX] Device API Detection:** Fixed detection logic for UCX GPU device API support. (#990)

### Benchmarks & Test Infrastructure
* **[kvbench] FLOPs Estimation:** Added Tensor Parallel (TP) scaling and MLP FLOPs to compute time estimates in `kvbench`. (#1083)
* **[nixlbench] Consistency Check:** Added data validation consistency checks to `nixlbench`. (#1103)

### Known Issues

**Full Changelog**: https://github.com/ai-dynamo/nixl/compare/0.8.0...0.9.0
```

## 0.10.0 (2026-02-18)

## Summary

The NVIDIA® NIXL Release 0.10.0 delivers major advancements in cloud storage, networking, and device integration, reinforcing NIXL’s hardware‑agnostic design. This release introduces full AWS Neuron device support, enabling developers to leverage heterogeneous compute environments with consistent performance and unified APIs. Alongside this, NIXL 0.10.0 expands storage capabilities with a new Azure Blob Storage plugin, S3 CRT client integration, and a hierarchical object storage architecture designed to support upcoming S3 RDMA acceleration.

The release also debuts the comprehensive Device API V2, extending across host-side, backend, and device-side implementations to simplify integration and improve portability. Networking enhancements include support for Slingshot/CXI providers and multiple Libfabric performance optimizations, such as CQ batch reads and an improved threading model for higher concurrency and throughput.

## Major Features

- **Azure Blob Storage Plugin:** Introduce the initial implementation of Azure Blob Storage support as another cloud object storage backend for NIXL. This plugin uses the Azure SDK for C++ to provide object segment storage and OAuth-based authentication through Microsoft Entra ID. It serves as a functional alternative to the existing S3 backend and includes integration tests, nixlbench benchmarking support, and CI infrastructure for validation. (#1233)
- **S3 CRT Client Support:** Added support for the AWS Common Runtime (CRT) S3 client, enabling higher throughput S3 transfers with automatic multipart upload/download parallelism. (#1127)
- **Hierarchical Object Storage Architecture:** Refactored the object storage plugin into a modular, inheritance-based client and engine architecture. This introduces a clean separation of concerns with support for standard S3, CRT-based S3, and a placeholder for future accelerated (RDMA) S3 backends with vendor-specific extensions. (#1247)
- **Device API V2:** A comprehensive redesign of the NIXL Device API, delivering a new programming model across the full stack:
 - API definition and interface updates. (#1229)
 - Core host-side implementation. (#1230)
 - UCX backend implementation. (#1245)
 - GPU and UCX device-side implementation. (#1255)
- **Libfabric Slingshot/CXI Support:** Added support for the HPE Slingshot/CXI provider in Libfabric, including `FI_MR_ENDPOINT` memory registration mode handling. This enables NIXL to run on Slingshot interconnect fabrics commonly found in HPC environments. (#1242)
- **AWS Neuron Device Support:** Added OFI (OpenFabrics Interfaces) support for AWS Neuron devices (Trainium/Inferentia), enabling NIXL networking over Neuron-based accelerators. (#1258)
- **Dual License Updates:** Updated licensing information in the GitHub repository to reflect dual licensing (Apache 2.0 + MIT for DeepEP-derived code).

## API Changes

- **[Device] Device API V2:** The Device API has been redesigned with new interfaces for host-side and device-side operations, along with a memory view API that simplifies device initialization. This is a significant API change from the v1 Device API. (#1229, #1230, #1245, #1255)

## Enhancements

### Performance

- **[Python] GIL Release:** Released the Python Global Interpreter Lock (GIL) in time-consuming NIXL functions, improving concurrency for multi-threaded Python applications. (#1232)
- **[Libfabric] CQ Batch Reads & Threading Model:** Implemented batch completion queue reads (16 entries per read) and changed the threading model from `FI_THREAD_SAFE` to `FI_THREAD_COMPLETION` for improved Libfabric performance. (#1272)
- **[Libfabric] Remove CM Thread:** Removed the connection management thread as the Libfabric plugin moves to the EFA protocol, simplifying the connection flow and reducing overhead. (#1251)
- **[Libfabric] EFA Infinite RNR Retry:** Enabled infinite Receiver Not Ready (RNR) retry at the EFA firmware level (`FI_OPT_EFA_RNR_RETRY=7`), improving reliability by preventing RNR timeout failures. (#1207)
- **[Libfabric] Notification Fragmentation:** Implemented notification fragmentation for large messages in the Libfabric backend, enabling reliable transfer of messages that exceed single-notification size limits. (#1142)
- **[Libfabric] Disable Unsolicited Write Recv:** Disabled unsolicited write receive for EFA RDM endpoints, reducing completion queue overflow under high write loads. (#1084)
- **[UCX] RC GDA Multi-Channel Config:** Added configuration support for RC GDA (GPU Direct Access) number of channels, allowing tuning of GPU-Direct RDMA transport parallelism. (#1206)

### NIXL-EP example Improvements

- **Memory View API Migration:** Migrated NIXL-EP example to the new Device API V2 memory view interface, greatly simplifying device and host initialization code. (#1256)
- **Unified Data and Counter Buffers:** Consolidated data and counter buffer management for cleaner resource handling. (#1186)
- **Channels Modulo Elimination:** Removed channels modulo logic for simplified channel management. (#1200)
- **UCX Multi-Channel API:** Migrated to the UCX multi-channel API for improved transfer parallelism. (#1175)
- **TCPStore Migration:** Migrated metadata exchange and elastic coordination from etcd to PyTorch TCPStore for simplified deployment. (#1144, #1155)

### Networking & Backend

- **[UCX] Plugin Reorganization:** Moved UCX utilities from `src/utils/ucx/` to `src/plugins/ucx/` for improved code organization and maintainability. (#1005, #1254, #1234)
- **[UCX] Removed CUDA Context Management:** Removed manual CUDA context management from the UCX plugin, simplifying the backend. (#946)
- **[UCX] Hardware Warning Improvements:** Added warnings when hardware is not supported by UCX, improving user feedback during initialization. (#1241)
- **[Core] Plugin Manager Refactor:** Refactored the plugin manager for improved memory safety and string handling. (#1209)

### Build & CI

- **CI: Azure Infrastructure:** Added Azurite (Azure Storage emulator), Azure SDK, and Azure CLI to CI for Azure Blob Storage plugin testing. (#1263)
- **CI Build Speed:** Improved speed of building NIXL in CI pipelines. (#1139)
- **Build Instructions:** Added missing ninja install step and detailed build instructions for first-time users. (#1181)
- **Telemetry Metrics Description:** Updated metrics types and descriptions for the telemetry system. (#1280)
- **External Plugin Headers:** Installed missing headers required by external plugin builds. (#1135)

### Benchmarks

- **[nixlbench] Config File Support:** Added `--config_file` parameter support to nixlbench, enabling benchmark configuration via external files. (#989)
- **[kvbench] New Models:** Added GPT-OSS and Qwen3 model support to kvbench for expanded LLM benchmarking. (#1108)
- **[nixlbench] Neuron Device Support:** Added support for AWS Neuron devices with VRAM segment type in nixlbench, using dynamic library loading to avoid hard dependency on libnrt. (#1265)
- **[nixlbench] Filenames Parameter:** Added `--filenames` parameter for specifying storage object names. (#1192)
- **[nixlbench] GUSLI Auto-Generated Config:** nixlbench now automatically generates GUSLI configuration. (#1193)
- **[nixlbench] Backward Compatibility:** Restored gflags-based flag parsing for backward compatibility. (#1289)

### Documentation

- **Supported Platforms:** Clarified supported platforms and Linux build prerequisites in the documentation. (#1211)
- **Build Directory Reference:** Updated build directory references in README. (#1246)
- **Typo Fixes:** Fixed typos across documentation files. (#1260)

## Bugfixes

- **[GUSLI] Incorrect Offset:** Fixed an incorrect offset calculation in the GUSLI plugin. (#1244)
- **[GPUNetIO] Build Fix:** Fixed the GPUNetIO plugin build. (#1266)
- **[UCX] Config Parsing:** Fixed UCX configuration parsing issues. (#1201)
- **[UCX] Memory Leak:** Configured a sane value for the rcache unreleased threshold, fixing a memory leak in the UCX backend. (#1210)
- **[UCX] Plugin Bug:** Fixed a bug in the UCX plugin. (#1082)
- **[UCCL] Consistency Checks:** Fixed consistency check logic in the UCCL backend. (#1151)
- **[OBJ/S3] Virtual Addressing:** Set `useVirtualAddressing` for S3CRTClient to work around an AWS SDK bug. (#1283)
- **[Prometheus] CMake Build:** Fixed Prometheus telemetry plugin build with newer CMake versions. (#1196)
- **[Prometheus] Security Patch:** Applied a security patch for a dependency of the Prometheus plugin. (#1204)
- **[Core] Role Validation:** Fixed role parameter validation logic error. (#1237)
- **[Core] HW Detection Logging:** Replaced error/exception with warning log messages in hardware detection support to avoid false alarm error messages. (#1273)
- **[Telemetry] Dangling Pointer:** Fixed a dangling pointer in the telemetry plugin `getName`/`getVersion` methods that could cause crashes. (#1148)
- **[Libfabric] GPU-to-EFA Mapping:** Fixed GPU-to-EFA NIC mapping to use PCI bus IDs instead of device indices, correcting topology-aware routing on multi-GPU/multi-NIC systems. (#1149)
- **[Build] AWS Dependencies:** Fixed AWS build dependencies. (#1262)
- **[CI] etcd Process Kill:** Fixed `pkill etcd` from accidentally killing other containers' processes. (#1227)

## Test Infrastructure

- **[Rust] Sync Manager Tests:** Added test coverage for the Rust sync_manager. (#1006)
- **Debugging:** Added descriptor list dump on posting with debug logging enabled for improved troubleshooting. (#1243)

## Known Issues
Full Changelog: [0.9.0...0.10.0](https://github.com/ai-dynamo/nixl/compare/0.9.0...0.10.0)

## 0.10.1 (2026-03-03)

# 0.10.1

## Summary
NVIDIA® NIXL Release 0.10.1 is a targeted maintenance release focusing on improvements to Rust bindings, Python packaging, and testing infrastructure.

## Rust Bindings
- **Runtime Library Resolution**: Introduced `libnixl_capi.so`, a shared library that exports `nixl_capi_*` C symbols. This allows downstream consumers of the `nixl-sys` Rust crate to load NIXL at runtime without requiring build-time linking. The NIXL stubs have been rewritten from abort-on-call to use `dlopen`/`dlsym` for lazy forwarding to the real implementation (#1358).
- **Build Checks**: Added a `libnixl.so` existence check in `build.rs` before attempting to link. This ensures the fallback to stubs works correctly when `nixl-sys` is used as a git dependency where headers are available but libraries are not installed (#1358).

## Python Packaging & Testing
- **Exact Version Pinning**: Pinned the Python CUDA-specific dependencies (`nixl-cu12` and `nixl-cu13`) to exact versions in the `nixl` meta-package. This prevents version mismatches and ensures consistent environments when installing the meta-package (#1354).
- **Testing Infrastructure**: Added support for running Python tests with a pre-created virtual environment (with support for both standard `pip` and `uv pip`), improving CI flexibility and local development workflows (#1353).

Full Changelog: [0.10.0...0.10.1](https://github.com/ai-dynamo/nixl/compare/0.10.0...0.10.1)


## v1.0.0 (2026-03-13)

# 1.0.0

## Summary

The NVIDIA® NIXL Release 1.0.0 marks a major milestone in API stability and production readiness. This release finalizes the Device API V2 transition by removing the legacy V1 implementation and normalizing naming conventions, establishing a clean and stable 1.0 API surface. A new two-phase configuration framework replaces ad-hoc environment and API configuration handling, providing a consistent and extensible runtime configuration model across all NIXL components.

NIXL 1.0.0 also delivers significant improvements to networking, storage, and backend infrastructure. The Libfabric backend gains NUMA-aware rail selection for topology-optimized transport on multi-socket systems, while the POSIX plugin introduces per-engine IO queuing for higher filesystem concurrency. Cloud storage maturity advances with Azure Blob connection string and CA bundle support, S3 CRT multipart threshold corrections, and expanded object storage functional testing. Across core transfer paths, descriptor iteration and transfer request creation have been optimized, telemetry overhead reduced, and UCCL batch transfer handling simplified, contributing to improved throughput and lower latency in production deployments.

## Major Features

- **Device API V2 Finalization:** Removed the legacy Device API V1 implementation and completed all V2-oriented cleanups, including normalizing `MemoryView` to `MemView` across the codebase. This establishes Device API V2 as the sole, stable device programming interface for NIXL 1.0. (#1342, #1337, #1376)
- **Configuration Framework:** Introduced a comprehensive two-phase configuration system spanning environment-driven (Part 1) and API-driven (Part 2) settings. This replaces the previous ad-hoc configuration approach with a structured, extensible model for runtime configuration management. (#1301, #1346)
- **Libfabric NUMA-Aware Rail Selection:** Added a NUMA-aware rail selection policy for `DRAM_SEG` memory types in the Libfabric backend. This enables topology-optimized transport selection on multi-socket systems by aligning memory access with the closest available network rail. (#1302)
- **Libfabric Control Rail Removal:** Removed the legacy control rail from the Libfabric backend, simplifying the rail management architecture and reducing resource overhead. (#1386)
- **POSIX Per-Engine IO Queue:** Added per-engine IO queue support in the POSIX plugin, improving concurrency and scheduling behavior for filesystem-backed storage workflows. (#1051)
- **Azure Blob Storage Enhancements:** Extended the Azure Blob Storage plugin with connection string authentication support and configurable CA bundle settings, improving deployment flexibility in enterprise and air-gapped environments. (#1351, #1329)
- **Rust Runtime Library Resolution:** Introduced `dlopen`-based `nixl-sys` stubs via `libnixl_capi.so`, enabling Rust consumers to resolve NIXL at runtime without build-time linking. Stubs use `dlopen`/`dlsym` for lazy forwarding to the real implementation. (#1358)
- **UCCL Batch Transfer Optimization:** Simplified and optimized UCCL handling for batch transfer workflows, reducing overhead in multi-transfer scenarios. (#1271)

## API Changes

- **[Device] API V1 Removal:** The Device API V1 has been fully removed. Device API V2 is now the only supported device API path. Applications still using V1 interfaces must migrate to V2. (#1342)
- **[Device] MemoryView to MemView Rename:** Device API V2 naming has been normalized from `MemoryView` to `MemView` across all interfaces. Downstream code should update symbol references accordingly. (#1337)
- **[Config] New Configuration Model:** Runtime configuration now follows the new two-phase environment/API configuration framework. Existing environment variable and API-based configuration patterns should be reviewed against the new model. (#1301, #1346)

## Enhancements

### Performance

- **[Core] Transfer Request Optimization:** Optimized `createXferReq` performance to reduce overhead in the hot transfer request creation path. (#1338)
- **[Core] Descriptor List Iteration:** Optimized `nixlDescList` iteration for faster descriptor traversal during transfer operations. (#1322)
- **[Telemetry] Reduced Runtime Overhead:** Optimized `nixlTelemetry::addXferTime` for lower per-transfer telemetry cost. (#1365)
- **[Telemetry] Remove Backend Export:** Removed backend telemetry export to eliminate unnecessary overhead in the telemetry pipeline. (#1364)
- **[UCCL] Batch Transfer Simplification:** Simplified and optimized UCCL for batch transfer workflows, reducing per-transfer overhead. (#1271)
- **[UCX] Removed Extra Copy:** Eliminated an unnecessary data copy from `prepMemoryView` in the UCX plugin, reducing memory transfer overhead. (#1261)
- **[Core] Serialization Optimizations:** Added validation checks and small optimizations to serialization/deserialization utilities. (#1277)

### Networking & Backend

- **[Libfabric] Remove Post-Operation Retry Delay:** Removed the delay between post-operation retries in the Libfabric backend, reducing latency for retry-sensitive workloads. (#1335)
- **[Libfabric] TCP Provider Fix:** Fixed TCP provider behavior in the Libfabric backend for correct operation on TCP-based fabrics. (#1348)
- **[Libfabric] EFA Hardware Warning:** Added a warning when EFA hardware is present but the Libfabric backend is not selected, improving user guidance during initialization. (#1287)
- **[UCX] VRAM Memory-Type Validation:** NIXL now raises an error when UCX incorrectly reports VRAM memory as host memory, preventing silent misclassification that could cause data corruption. (#1385, #1393)
- **[UCX] Targeted GDA Configuration:** RC GDA configuration is now applied only when relevant UCX transports are active, avoiding unnecessary configuration side-effects. (#1347)
- **[UCX] Utils Refactoring:** Minor refactoring of UCX backend utility code for improved maintainability. (#1291)
- **[Core] Memory Handling Refactor Preparation:** Refactored internal core/agent memory handling structures in preparation for follow-on memory management improvements. (#1361, #1370)
- **[Core] Listener Error Reporting:** Fixed incorrect error reporting in the core metadata listener. (#1345)

### NIXL-EP Example Improvements

- **Release Build Tuning:** Disabled fast fault detection for release builds to reduce overhead in production deployments. (#1275)

### Build & CI

- **CI: GPU Test Migration to Slurm:** Moved GPU tests to Slurm-based scheduling with improved allocation timeouts and test timeout handling for more reliable GPU CI execution. (#1250, #1366, #1336, #1318)
- **CI: Build Abort Logic:** Improved abort logic for obsolete builds and added automatic cancellation of previous dispatcher builds for the same PR. (#1317, #1281)
- **CI: Mooncake Non-Interactive Build:** Configured Mooncake builds to run without interactive prompts. (#1290)
- **CI: GHA Runner Pinning:** Pinned GitHub Actions runner versions and kubectl for improved CI stability. (#804)
- **CI: Demo Pinning:** Pinned ci-demo to the `stable_nixl` tag for reproducible demo builds. (#1343)
- **CI: UCX Bug Workaround:** Added a workaround for a UCX bug affecting CI test runs. (#1310)
- **Build: Wheel Environment Updates:** Upgraded hwloc in the wheel build environment, disabled nvlm in manylinux Dockerfile, and updated S3 SDK version. (#1396, #1403, #1387)
- **Build: Meson Device API V2 Fix:** Fixed the `ucx_gpu_device_api_v2_available` detection in `meson.build`. (#1316)
- **Code Quality Automation:** Added CodeRabbit configuration for AI-assisted code reviews and expanded the code style guide for contributor consistency. (#1293, #1143)

### Benchmarks

- **[nixlbench] Aggregate BW Fix:** Fixed aggregate bandwidth calculation in pairwise single-group mode. (#1299)
- **[nixlbench] SHA256 Checksum:** Switched to SHA256 checksum algorithm when uploading test objects for READ tests. (#1286)
- **[nixlbench] GUSLI READ Fix:** Fixed GUSLI READ consistency check failure and cleanup crash. (#1300)
- **[nixlbench] CLI Simplification:** Reduced the number of CLI argument combinations in benchmark test matrix. (#1363)

### Documentation

- **Code Style Guide:** Expanded the code style guide with additional guidance for contributors. (#1143)

## Bugfixes

- **[OBJ/S3 CRT] Multipart Sizing:** Aligned CRT `partSize` and multipart upload threshold with the CRT minimum part size limit, preventing invalid multipart configurations. (#1368)
- **[Libfabric] Unit Test Regression:** Fixed a regression in Libfabric unit tests and updated related README and comments. (#1394)
- **[Libfabric] TCP Provider:** Fixed TCP provider behavior for correct operation on TCP-based fabrics. (#1348)
- **[Core] Worker File Offset:** Fixed `file_offset` calculation in `nixl_worker`. (#1399)
- **[Core] Listener Error Reporting:** Fixed wrong error reporting in the core metadata listener. (#1345)
- **[Core] Metadata Listener Setup:** Fixed silent failure on metadata listener socket setup, improving error visibility. (#1371)
- **[Core] Metadata Test Coverage:** Handled all error message cases in metadata test for complete error path coverage. (#1372)
- **[UCX] VRAM Misclassification:** Fixed silent VRAM-as-host-memory misclassification by raising an explicit error when UCX reports incorrect memory types. (#1385, #1393)
- **[UCX] Worker Test:** Fixed `ucx_worker_test` for the `USE_VRAM` case. (#1373)
- **[POSIX] Naming:** Fixed POSIX plugin naming conventions. (#1296)
- **[Core] String Utility Cleanup:** Removed deprecated `strEqual` and cleaned up common string utility tools. (#1391, #1309)
- **[Core] CUDA Memory Init:** Fixed CUDA memory initialization ordering. (#1360)

## Test Infrastructure

- **Stricter Test Failures:** Updated Google Test harness to fail on unexpected error or warning log messages, improving detection of regressions. (#1288)
- **Reliable Failure Detection:** Improved test reliability with better failure assertion patterns. (#1323)
- **Binary Data Output:** Removed printing of binary data from test output to reduce noise in CI logs. (#1276, #1409)
- **CRT Test Improvements:** Fixed CRT multi-buffer test timeout reporting and reduced poll spin overhead. (#1404)
- **Telemetry Test Simplification:** Simplified the telemetry test for easier maintenance. (#1362)
- **CPP Test Script:** Updated CI scripts to fail if either `nixl_test` binary fails. (#1294)
- **Object Plugin Functional Tests:** Added functional test coverage for the NIXL object storage plugin. (#1284)
- **Hardware Warning Test Scoping:** Skipped hardware warning tests in non-GPU CI flows and excluded `rc_gda` transport from hardware warning test scope. (#1334, #1292)
- **S3 CRT Test Fix:** Fixed the agent name for S3 CRT tests. (#1314)

## Known Issues

Full Changelog: [0.10.1...1.0.0](https://github.com/ai-dynamo/nixl/compare/0.10.1...1.0.0)



## v1.0.1 (2026-04-14)

# 1.0.1

## Summary
NVIDIA® NIXL Release 1.0.1 is a targeted maintenance release focusing on NIXL-EP stability fixes, libfabric transport reliability improvements, and build/packaging improvements across UCX, Python wheel, and Docker environments.

## NIXL-EP Fixes
- **Fix Destruction Flows**: Fixed resource cleanup and destruction ordering in NIXL-EP to prevent crashes and resource leaks during shutdown (#1452).
- **Fix Signaling Buffer Corruption During Elastic Scale-Up**: Fixed a signaling buffer corruption issue in NIXL-EP that could occur when new nodes join during elastic scale-up, ensuring correct buffer state across topology changes (#1453).

## Libfabric Fixes
- **Fix Notification Override on Transfer Handle Repost**: Fixed an issue in the libfabric backend where updated notification messages were ignored when transfer handles were reposted, causing reposted transfers to always use the original notification from initial preparation time (#1482, #1433).
- **Fix Endpoint Thread Safety**: Added proper mutex locking for all endpoint access in the libfabric backend to satisfy `FI_THREAD_COMPLETION` thread-safety requirements, preventing potential race conditions during concurrent I/O operations (#1483, #1457).

## Build & Packaging
- **Enable UCX EP Support in Python Wheel Build**: Added UCX endpoint support to the Python wheel build, enabling NIXL-EP functionality for pip-installed deployments (#1440).
- **Disable gdrcopy in UCX Build**: Disabled gdrcopy in the UCX build to avoid linkage conflicts in environments where gdrcopy is not available or not needed (#1436).
- **Fix Abseil Version Conflicts**: Resolved Abseil version conflicts in NIXL builds and Docker images that could cause linker errors or runtime symbol mismatches (#1432).
- **Bump RDMA Memory Check UCX Version**: Updated the UCX version used for RDMA memory checks to align with the latest supported UCX release (#1445).
- **Pin Torch Version to 2.11**: Pinned the PyTorch dependency to version 2.11 for reproducible builds and compatibility (#1471).
- **Add pkg-config Install**: Added missing `pkg-config` installation to the build environment, fixing build failures in minimal container images (#1450).
- **Fix Dependency Issues**: Removed strict PyTorch version check during module initialization to allow broader compatibility, and unified UCX checkout behavior to consistently use the configured UCX reference (#1488).

Full Changelog: [1.0.0...1.0.1](https://github.com/ai-dynamo/nixl/compare/1.0.0...1.0.1)




## v1.1.0 (2026-05-12)

# 1.1.0

## Summary

The NVIDIA® NIXL Release 1.1.0 introduces a high-throughput dispatch/combine kernel path for the NIXL-EP example program and modernizes the telemetry data model for production-scale deployments. A new dedicated `nixl_ep_ht.cu` kernel set ships alongside the renamed low-latency `nixl_ep_ll.cu`, paired with a VMM-based device memory allocator and elastic-scaling fixes covering destruction flows, non-consecutive rank topologies, and signaling-buffer corruption during scale-up, while the core plugin manager now defers backend loading until first use to reduce agent startup cost. Telemetry consumers must adopt two breaking changes -- the public event signature drops its `timestamp` field, and the Prometheus exporter migrates `agent_xfer_time` / `agent_xfer_post_time` from `Gauge` to `Counter`, suffixes counters with `_total`, and removes the per-backend metric category in favor of standardized transfer, performance, and memory categories. **Downstream consumers should also switch their `requirements.txt` from `nixl[cu12]` / `nixl[cu13]` to plain `nixl`** -- the meta wheel now bundles both CUDA backends and auto-selects at runtime based on `torch.version.cuda` (see [API Changes]).

NIXL 1.1.0 also delivers significant networking, storage, and backend improvements. The Libfabric backend extends NUMA-aware rail selection to additional EC2 instance topologies, adds completion-queue locking for `FI_THREAD_COMPLETION` semantics, and resolves multi-GPU memory registration and notification-override regressions on transfer-handle repost. A new Dell ObjectScale S3-over-RDMA accelerated engine joins the OBJ plugin for high-bandwidth object storage, UCX now raises an explicit error when VRAM is misclassified as host memory, and `nixlbench` adds Neuron (Trainium/Inferentia) device support. Across core transfer paths, batched insertion of sorted descriptor lists and a bounded in-memory telemetry buffer contribute to lower per-request overhead and predictable memory behavior in long-running agents.

## Major Features

- **NIXL-EP High-Throughput Kernels:** Added a new high-throughput dispatch/combine kernel path (`examples/device/ep/csrc/kernels/nixl_ep_ht.cu`) alongside the renamed low-latency `nixl_ep_ll.cu`, with matching `test_ht.py` coverage and configurable GPU timeouts so the example can be tuned for production-scale runs. (#1341, #1503, #1520)
- **Plugin Manager: Deferred Plugin Loading:** Plugins are now loaded the first time they are actually used instead of at agent construction. Reduces agent startup cost when only a subset of plugins is exercised and removes dead code from the telemetry path. (#1546, #1564)
- **Dell ObjectScale S3-over-RDMA Engine:** New accelerated S3 engine under `src/plugins/obj/s3_accel/dell/` (with tests) that talks to Dell ObjectScale over RDMA via a dedicated client. Wired into `obj_backend.cpp` and exercised through `test/gtest/unit/obj/`. (#1327)

## API Changes

- **[Telemetry] Prometheus Exporter Migration:** Removed the `NIXL_TELEMETRY_BACKEND` event category and `createOrUpdateBackendEvent()`. Counters are now registered with a `_total` suffix to match Prometheus naming conventions, and the `agent_xfer_time` / `agent_xfer_post_time` metrics moved from `Gauge` to `Counter`. (#1308)
- **[Telemetry] Event Signature Cleanup:** Removed the public `timestamp` field from `nixlTelemetryEvent`, simplified `backend_engine.h` and `telemetry_plugin.h` signatures, and tightened the `buffer_plugin` API. Downstream consumers must update event-construction sites. (#1522)
- **[Packaging] Switch downstream installs from `nixl[cu12]` / `nixl[cu13]` to plain `nixl`:** **Action required: update your `requirements.txt` (or `pyproject.toml` / `setup.py`) to depend on `nixl` instead of `nixl[cu12]` or `nixl[cu13]`.** The `nixl` meta wheel on PyPI now installs both `nixl-cu12` and `nixl-cu13` backends in a single step and selects the correct one at runtime from `torch.version.cuda`. The `[cu12]` / `[cu13]` extras are still accepted as no-op aliases so existing pins keep working, but new installs should drop the extra.

  **`torch` is a mandatory runtime dependency and must be installed from the PyTorch index matching your CUDA driver, either before `nixl` or in the same `pip install` invocation.** nixl declares torch as a dependency, but the default PyPI torch is CPU-only; pass `--index-url https://download.pytorch.org/whl/cu130` (or the appropriate CUDA variant) so pip resolves a CUDA-enabled build. At import nixl time the meta package reads `torch.version.cuda` to select between the bundled `nixl-cu12` and `nixl-cu13` backends. (#1574, #1578)


## Enhancements

### Performance

- **[Core] Batch Insertion for Sorted Descriptor Lists:** Added a batched insert path in `nixl_descriptors.cpp` / `nixl_memory_section.cpp` so registering large descriptor lists no longer pays the per-element ordered-insert cost. New `sec_desc_list` gtest covers the path. (#1479)
- **[Core] Deferred Plugin Loading:** See Major Features. Avoids parsing/loading unused backends at agent startup. (#1546, #1564)

### Networking & Backend

- **[Libfabric] NUMA-Aware Rail Selection on Additional Instance Types:** Extended the rail-manager / topology code paths to recognize more EC2 instance topologies (including `c5n.18xlarge`), warn cleanly when no policy applies, and keep the NUMA-aware policy from regressing on hardware it has not been tuned for. (#1461)
- **[Libfabric] Endpoint Locking for `FI_THREAD_COMPLETION`:** Expanded the CQ mutex to cover endpoint-bound posting operations, and skip in-line CQ progress when the dedicated progress thread is enabled. (#1457)
- **[Libfabric] Active Rail Tracking:** Reworked `libfabric_rail_manager` reference counting and added a sizable mock/unit-test harness (`libfabric_mock_stubs.h`, `rail_active_refcount_test.cpp`) so rail activation/deactivation is now covered by tests. (#1510)
- **[Libfabric] Multi-GPU Memory Registration:** Restored the original two-`if` registration pattern in `libfabric_backend.cpp` and downgraded the multi-GPU detection log from WARN to INFO. Validated end-to-end with `nixlbench --scheme tp --mode MG`. (#1506)
- **[Libfabric] EFA Hardware Warning:** Emit a clear warning when EFA hardware is present but the LIBFABRIC backend is not in use, plus new `hw_warning_test` coverage. (#1287)
- **[Libfabric] Log-Level Cleanup in EFA Path:** Reclassified noisy WARN messages and added an `Accelerator-PCI` prefix to topology-mapping INFO logs for context. (#1462)
- **[UCX] Disable Emulated RMA Protocols:** On UCX >= 1.21, force `PROTO_EMULATION_ENABLE=n` and pin `IB_TX_INLINE_RESP=0` in `ucx_utils.cpp` so the backend refuses to fall back to software-emulated RMA -- transfers either run over true RDMA or fail fast instead of silently degrading. (#1611)
- **[UCX] Timeout Warning on Device Memory List Creation:** Added a configurable timeout warning in `mem_list.cpp` so slow VRAM registrations surface visibly instead of hanging silently. (#1410)
- **[UCX] Plugin Cleanup:** Removed an unused `ucx_backend` class field. (#1512)
- **[Mooncake] Dependency Bump:** Updated the Mooncake submodule/build to v0.3.9, including matching CI matrix entries. (#1448)

### NIXL Expert Parallelism (EP)

- **VMM API for Device Memory Allocation:** Added a new `vmm.cpp` / `vmm.hpp` layer so the NIXL-EP example uses the CUDA VMM API instead of plain `cudaMalloc` for its device buffers. (#1415)
- **CUDA Graph Reuse Across Elastic Scaling:** The low-latency dispatch/combine kernel path now reuses its CUDA graphs across elastic scale up/down instead of rebuilding them on every rank change. `Buffer.connect_ranks` gains an `activate=False` option (LL mode only) so newly connected ranks can be staged masked and activated later via `update_mask_buffer`. (#1584)
- **High-Throughput Follow-Up Fixes:** Removed a redundant count buffer, fixed internode destruction flows, re-guarded `p2p_ptr_get` with `is_rank_masked`, and merged duplicated `!low_latency_mode` blocks. (#1503)
- **Robust Destruction Flows:** Deregister buffers before `cudaFree`, fix disconnect rank ordering, skip remote `prepMemView` when there are no peers, and warn (rather than throw) on destructor failures. (#1430)
- **Non-Consecutive Rank Support:** Move `p2p_ptr_get` calls inside the rank-mask guard so configurations like ranks `[0, 2]` no longer dereference uninitialized P2P mappings. (#1478)
- **Signaling Buffer Corruption on Elastic Scale-Up:** Size the signaling region for the maximum expert count so growing `num_experts` no longer overlaps with send/recv data. (#1451)
- **Planned-SIGTERM Handling in Elastic Test:** `elastic.py` now recognizes the intentional SIGTERM injected to simulate rank failure and does not flag those workers as errors. (#1500)
- **GCC `maybe-uninitialized` Fix in `ht_dispatch`:** Switched to raw pointers in ternary expressions matching the existing `recv_topk_*` pattern so `-Werror=maybe-uninitialized` no longer fails the example build. (#1525)
- **Cleanup:** Removed an unused variable in the EP CSRS kernels. (#1508)
#### Limitations
- **Cross-NVL-domain runs are not supported in this release.** Launching NIXL EP across nodes that belong to different NVLink domains (for example, with SLURM `--segment 1`, or any allocation that spans NVL blocks) will fail during connection setup.



### Packaging & Distribution

- **Unified Meta Wheel + CUDA-Matched Torch:** Implementation side of the `pip install nixl` simplification described under API Changes. Adds a `-Drelease_wheel=true` meson option (`meson_options.txt`, `nixl-meta/meson.build`, `pyproject.toml.in`) that toggles the unified meta wheel for release builds vs. a single-backend wheel for source builds; the manylinux Dockerfile emits the meta wheel only on the cu12 pass since it is identical for cu12/cu13; the vLLM and SGLang Dockerfiles drop their per-CUDA wheel-selection logic; and `.gitlab/build.sh` installs the CUDA-matched PyTorch wheel instead of whatever default `torch` shipped with the other dev dependencies. (#1574)
- **Inference Image Dockerfiles:** Added `contrib/Dockerfile.vllm` and `contrib/Dockerfile.sglang` for downstream inference-stack consumers. (#1477)
- **Enable UCX-EP Support in Python Wheel:** Wire UCX-EP into the wheel build and meson configuration so the published Python wheel ships with EP support. (#1440)
- **Disable `gdrcopy` in UCX Build:** Drop `gdrcopy` from the UCX build dependency set across `contrib/Dockerfile`, `contrib/Dockerfile.manylinux`, and the nixlbench builder. (#1436)

### Benchmarks

- **[nixlbench] Neuron Support:** `nixlbench` now allocates, deallocates, and consistency-checks VRAM segments on Neuron (Trainium/Inferentia) devices when CUDA is unavailable. (#1454)
- **[nixlbench] Pairwise SG Stats Scaling Fix:** Skip the per-device-count multiplication of B/W in multi-rank single-group mode, so 8-device runs no longer report inflated throughput. (#1495)
- **[nixlbench] Worker Cleanup:** Removed unused parameters across workers and the `worker.h` interface. (#1426)
- **[nixlbench] Pairwise Single-Group Stats Extension:** Extend the statistics calculation condition to handle multiple initiator devices in pairwise single-group mode. (#1407)

## Bugfixes

- **[Core] Agent etcd Metadata Synchronization:** Fixed incorrect synchronization with the etcd metadata communication thread (`agent_data.h`, `nixl_agent.cpp`, `nixl_listener.cpp`) so concurrent metadata exchange no longer races. (#1559, #1563)
- **[Core] `nixl_worker` File Offset Calculation:** Restored the correct `file_offset += block_size` accounting for non-GUSLI plugins after the regression introduced by `62a5b3e`. (#1399)
- **[Telemetry] Bounded In-Memory Event Buffer:** Fixed unbounded growth of the in-memory telemetry buffer by capping it to `getMaxEventsBuffered()` instead of growing indefinitely. (#1516)
- **[Libfabric] Active Rail Tracking:** See Networking & Backend; the same change is also a bugfix on rail activation accounting. (#1510)
- **[Libfabric] Notification Override on Repost:** `postXfer()` now reads the updated notification fields from `opt_args` so reposted transfers send the new notification instead of the original `prepXfer()` value. (#1433)
- **[Libfabric] Multi-GPU Memory Registration:** See Networking & Backend; restoring the two-if pattern fixed the multi-GPU registration regression. (#1506)
- **[Libfabric] Improved Log Levels:** Reduce noisy WARNs and clarify topology-mapping INFO logs (also accept `SIZE_MAX` as a valid `size_t` boundary). (#1462)
- **[UCX] Reject VRAM Reported as Host Memory:** Raise an explicit error when UCX detects a VRAM allocation as host memory instead of silently transferring it as host data. (#1393)
- **[UCX (bundled)] dma-buf Offset for Interior CUDA Addresses:** The wheel's bundled UCX (pinned to `v1.21.x` in `.gitlab/build.sh`) picks up an upstream fix that restores the queried-address delta in `uct_cuda_copy_md_mem_query`'s dma-buf offset. Without it, registering an interior CUDA buffer produces a remote key whose zero point is shifted to the allocation base, so RDMA writes can land on neighboring memory -- observed sporadically in production. Regression originally introduced by `openucx/ucx#11055`. (openucx/ucx#11419)
- **[Rust] Agent Deadlocks and C-String Handling:** Fix agent deadlocks and C-string lifetimes in the Rust bindings (`bindings/rust/src/agent.rs`) and add the matching Rust integration test that mirrors the C++ test. (#1367)
- **[Python] IDE / Linter / Static-Analysis Resolution:** Fix `nixl-meta` static-analysis resolution for `nixl_agent` and `nixl_logger`, including the example `basic_two_peers.py`. (#1402)
- **[nixlbench] Pairwise SG Stats Scaling on Multi-Rank:** Same change as the Benchmarks entry; included here as a bugfix for the originally reported issue #1463. (#1495)
- **[nixlbench] Poll Shutdown:** Fix shutdown of `nixlbench` so the etcd runtime and worker poll loops actually exit cleanly when the test ends. (#1421)
- **[nixlbench] `file_offset` Regression:** See `[Core] nixl_worker File Offset Calculation` -- this lived under `benchmark/nixlbench/` and is dual-listed for traceability. (#1399)

## Known Issues

Full Changelog: [1.0.0...1.1.0](https://github.com/ai-dynamo/nixl/compare/1.0.0...1.1.0)






## v1.2.0 (2026-05-30)

# 1.2.0

## Summary

The NVIDIA® NIXL Release 1.2.0 adds OS-assigned port support to the metadata listener so multi-peer agents can bind to port `0` and discover the kernel-chosen port at runtime instead of statically reserving one, and tightens the Libfabric backend's EFA write path with `FI_MORE`\-based descriptor batching pinned to a single endpoint per rail. The Libfabric change groups up to 16 consecutive write descriptors before flushing the doorbell to the device, reducing PCIe round trips for small-message high-descriptor-count transfers while keeping a standard round-robin read path so reads do not regress.

NIXL 1.2.0 also tightens the build and packaging story for downstream consumers. UCX now configures `UCX_MAX_HCA_PER_GPU=auto` on UCX `>= 1.21`, NIXL gains a `nixl_cuda_arch_list` meson option to compile against a user-selected SM list instead of the full datacenter default sweep, and `liburing` is sourced from a meson wrap pinned to WrapDB `liburing_2.14-1` so the POSIX backend's `io_uring` support is available out of the box from a source build and from every shipping container. The Rust bindings stop silently swallowing backend registration failures and now surface the C API status from `register_memory` directly to the caller.

## Major Features

- **OS-Assigned Port Support for Metadata Listener:** Added support for binding the metadata listener to port `0` so the OS picks an available port; the bound port is retrieved via `getsockname()` and emitted on `NIXL_INFO`. The Python multi-peer test helpers in `.gitlab/test_python.sh` now exercise this path so concurrent examples no longer collide on a hard-coded port. (\#1439)

## API Changes

- **\[Core\] Metadata Listener Port Type Migration:** Upgraded the default listener-port variables and structure fields (`listenPort`, `listen_port`) in `src/api/cpp/nixl_params.h`, `src/api/cpp/nixl_types.h`, and `src/utils/stream/metadata_stream.{h,cpp}` from `int` to `uint16_t` to match standard socket definitions. The Rust bindings (`src/bindings/rust/wrapper.{h,cpp}`, `src/bindings/rust/src/agent.rs`) gain a `DEFAULT_COMM_PORT` constant mirroring the C++ `default_comm_port`. (\#1439)

## Enhancements

### Performance

- **\[Libfabric\] EFA Doorbell Batching via `FI_MORE`:** `libfabric_backend.cpp` now batches up to 16 consecutive write descriptors on the same EP-pinned rail and submits them through `fi_writemsg()` with the `FI_MORE` flag, draining via a flushing `fi_writemsg()` on batch close. A stable per-transfer `base_offset` is reserved once in `postXfer()` (instead of per-descriptor) so every descriptor in a transfer sees the same rail assignment. Delivers a **30%–58% write bandwidth improvement** for small-message high-descriptor-count transfers; the read path keeps the existing round-robin layout to avoid regressing reads. (\#1626)

### Networking & Backend

- **\[UCX\] Auto-Selected `MAX_HCA_PER_GPU` on UCX `>= 1.21`:** `src/plugins/ucx/ucx_utils.cpp` now sets `UCX_MAX_HCA_PER_GPU=auto` when the linked UCX is `>= 1.21`, letting UCX pick the right HCA-to-GPU mapping on modern multi-HCA hosts instead of relying on the historical default. (\#1637)

### Packaging & Distribution

- **Configurable CUDA Target Selection (`nixl_cuda_arch_list`):** Added a `nixl_cuda_arch_list` meson option (`meson.build`, `meson_options.txt`, `contrib/build-wheel.sh`) defaulting to `sm_80, sm_86, sm_89, sm_90, sm_100, sm_103, sm_120` for full datacenter coverage. Users compiling for a single architecture can pass e.g. `-Dnixl_cuda_arch_list=90,100` for materially faster builds; when `nixl_ep` is enabled, the `sm_8x` entries are dropped automatically since the EP example only supports newer architectures. (\#1639)  
- **`liburing` via meson Wrap:** Replaced the per-container `liburing` install paths (apt `liburing-dev` on Ubuntu, `git clone` \+ `make` on manylinux, `git clone` \+ `make` in nixlbench builder, `.gitlab/build.sh`) with a single meson wrap pinned to WrapDB `liburing_2.14-1`. POSIX backend `io_uring` support is now always available when building from source and identical across `contrib/Dockerfile`, `contrib/Dockerfile.manylinux`, and `nixlbench/contrib/Dockerfile`. `ATTRIBUTIONS-CPP.md` bumped to `liburing 2.14`. (\#1577)

## Bugfixes

- **\[Rust\] Surface `register_memory` Errors:** `src/bindings/rust/src/agent.rs` now returns the C API status from `register_memory` instead of constructing a `RegistrationHandle` after a failed registration; the Rust integration tests in `src/bindings/rust/tests/tests.rs` are updated to create a backend and pass opt args so backend registration failures are exercised and no longer silently ignored. (\#1632)

## Known Issues

Full Changelog: [1.1.0...1.2.0](https://github.com/ai-dynamo/nixl/compare/1.1.0...1.2.0)  


## v1.3.0 (2026-06-15)

# 1.3.0

## Summary

NIXL 1.3.0 expands platform reach and backend capabilities. It adds AMD ROCm/HIP support for AMD Instinct GPUs (MI300X, MI325X, MI350X, MI355X), including `nixlbench`. The core build now targets C++20 to enable modern C++ features and provides a stronger foundation for future development for anyone compiling NIXL or its plugins from source. NIXL 1.3.0 also broadens the storage ecosystem: a new DDN Infinia backend joins the object-storage family, the `obj` plugin can now auto-register vendor backends without factory changes, and path-based file registration is now supported across all file-based backends.

Secondary updates focus on performance and reliability. Azure Blob Storage paths get faster through parallel memory queries, releasing the python global lock during transfer-request creation reduces multi-threaded contention, and using a pre-allocated telemetry buffer improves hot path performance. The telemetry schema is simplified, descriptor-list paths gain batched bulk removal and an empty-section leak fix, and the benchmark tools (`nixlbench`/`kvbench`) include several correctness improvements.

## Major Features

- **AMD ROCm/HIP support:** Added AMD ROCm/HIP build support for AMD Instinct GPUs (gfx942 - MI300X, MI325X; gfx950-MI350X, MI355X), including hardware-info detection plumbing and a follow-up enabling the same support for `nixlbench`. (#1642, #1647)
- **Move to C++20:** Switched the core and plugins to the C++20 standard and updated the plugin READMEs accordingly. Downstream builds-from-source now require a C++20-capable toolchain. (#1571)
- **DDN Infinia backend plugin:** Added a new NIXL backend plugin for DDN Infinia storage. (#1569)
- **Path-based file registration for all `FILE_SEG` backends:** Callers can now declare files by path in `nixlBlobDesc::metaInfo` (`<modes>:<path>` with `ro`/`rw` access and `direct`/`sync`/`noatime`/`create` flags); backends open the file in `registerMem` and close it in `deregisterMem`. Wired through a shared `src/utils/file/file_path_mode` helper into POSIX, HF3FS, CUDA_GDS, and GDS_MT. Strictly additive — unknown tokens fall back to the existing fd-in-`devId` mode. (#1635)
- **Object plugin vendor backend registry:** Replaced the `#ifdef` ladder in `obj_backend.cpp` with a self-registration pattern so accelerated/vendor engines register themselves via `objAccelEngineRegistrar`, making it trivial to add new object-storage engines without modifying the factory. (#1550)


## API Changes

- **[Telemetry] Slimmed telemetry event schema:** Removed the redundant `category` field from telemetry events, simplifying `telemetry_event.h` and the backend telemetry surface. Consumers parsing telemetry events should drop the `category` field. (#1649)
- **[NIXL EP] Refactor rank and expert semantics:** Added new fields, public mask-update capability and host-side tracking of active ranks for elastic rank handling. Dispatch/combine now accept an active-rank bound + experts-per-rank parameterization; internal buffer/layouts updated to use the active-range model. Removed the legacy mask-clean API. (#1693)


## Enhancements

### Performance

- **[Azure] Parallelized memory query for the `AZURE_BLOB` plugin:** Batched memory queries now issue HEAD requests in parallel (mirroring the OBJ plugin), improving initial blob-existence checks for integrations such as KV-cache lookups in LMCache. (#1721)
- **[Python] Release the GIL during `makeXferReq`:** The Python binding now releases the GIL while building transfer requests, reducing contention for multithreaded callers. (#1712)
- **[Telemetry] Pre-allocate the event buffer:** The telemetry event buffer is pre-allocated to avoid reallocation on the hot path. (#1719)
- **[Core] Batched descriptor-list removal:** `remDescList` and `removeLocalData` now remove descriptors in bulk instead of one-at-a-time, eliminating the previous O(N*M) per-deregister cost. (#1597)
- **[Core] Use C++20 `[[likely]]`/`[[unlikely]]`:** Replaced `__builtin_expect` with the standard C++20 branch-prediction attributes across the core, UCX backend, and `nixlbench`. (#1714)

### Networking & Backend

- **[Azure] Updated CA certificate discovery:** Expanded the list of CA certificate file paths the Azure Blob client checks, improving TLS trust-store discovery across environments. (#1694)

### NIXL-EP

- **Removed a declared-but-undefined method:** Cleaned up a method without a definition in the device/EP example. (#1684)

### Packaging & Distribution

- **`nixl_ep` wheel packs CUDA in a separate namespace:** The `nixl_ep` wheel now packages the bundled CUDA libraries under a distinct namespace (with a load fallback), avoiding collisions with other CUDA installations. (#1727)
- **Wheel build excludes DDN partner libraries:** Extended the `auditwheel --exclude` list in `build-wheel.sh` so DDN partner libraries are not vendored into the wheel. (#1733)

### Benchmarks

- **[nixlbench] AMD ROCm/HIP build support:** Enabled building `nixlbench` for AMD ROCm/HIP as a follow-up to the core AMD support. (#1647)
- **[nixlbench] Use `max_block_size` for object-storage buffer size:** Sized the object-storage buffer from `max_block_size`. (#1636)
- **[nixlbench] Fixed object-storage device-ID collisions across threads:** Resolved colliding device IDs when multiple threads target object storage. (#1638)
- **[nixlbench] Fixed deallocation memory ordering:** Corrected the order in which memory is deallocated. (#1590)
- **[nixlbench] Fixed a missing closing bracket in print output:** Repaired malformed benchmark print output. (#1725)
- **[kvbench] Fixed OBJ backend configuration and buffer-size setup:** Corrected the OBJ backend configuration and buffer-size initialization in `kvbench`. (#1549)

## Bugfixes

- **[Core] Fixed `addElement` using a hardcoded `VRAM_SEG` lookup:** `mem_section` no longer assumes `VRAM_SEG` when adding an element. (#1634)
- **[Core] Erase empty sections in `removeLocalData`:** Empty section map entries are now removed, preventing `sectionMap`/`memToBackend` from growing without bound in long-running register/deregister workloads. (#1597)
- **[Core] Fixed `remDescList` returning `NIXL_ERR_NOT_FOUND` when `len=0`:** Zero-length descriptor lists are handled correctly. (#1551)
- **[POSIX] Fixed backend queue fallback handling:** Corrected fallback handling in the POSIX backend transfer queue. (#1605)
- **[Telemetry] Fixed DOCA exporter build:** Added `nixl_common_dep` so `tomlplusplus` resolves for the DOCA telemetry plugin, which otherwise failed to compile after `common/configuration.h` began including `toml++/toml.hpp` directly. (#1640)

## Known Issues

- **[POSIX]** File-path Mode has a double-free issue (#1766)

Full Changelog: [1.2.0...1.3.0](https://github.com/ai-dynamo/nixl/compare/1.2.0...1.3.0)


## v1.3.1 (2026-07-08)

# 1.3.1

## Summary

NIXL 1.3.1 is a focused patch release. It closes the path-mode file-registration gap introduced in 1.3.0: reusing the same `devId` across distinct path-mode `FILE_SEG` registrations could leave transfers ambiguous and trigger a double-free on deregister, so all four path-mode file backends now reserve and enforce a unique path-mode `devId` per registered file. (\#1790)

The release also improves wheel packaging. The `nixl_ep` wheel can now be built against multiple PyTorch versions, producing per-`(Python, Torch)` extension artifacts that are merged into a single distribution and loaded by ABI/Torch version at runtime. In addition, the published manylinux wheels now bundle the DDN INFINIA backend plugin by default, so the INFINIA storage backend is available out of the box. (\#1775, \#1866, \#1832)

## API Changes

- **\[POSIX/CUDA GDS/GDS MT/HF3FS\] Unique `devId` required for path-mode `FILE_SEG`:** Path-mode registrations that reuse an in-use `devId` are now rejected with `NIXL_ERR_INVALID_PARAM`. Fd-in-`devId` mode (non-path `metaInfo`) is unchanged — one file descriptor may still back multiple descriptors at different offsets. (\#1790)

## Enhancements

### NIXL-EP Example Improvements

- **Multi-PyTorch `nixl_ep` wheels:** The `nixl_ep` wheel can now be built and packaged for multiple PyTorch versions at once. The build produces per-`(Python, Torch)` extension artifacts (with Torch-version-aware extension names) and merges them into a single wheel via a new `contrib/wheel_merge.py`; at import time the correct PyTorch/ABI extension is selected based on the installed Torch version. (\#1775)

### Packaging & Distribution

- **DDN INFINIA plugin bundled in manylinux wheels:** The published manylinux wheels are built on the public PyPA `manylinux_2_28` base and now bundle the DDN INFINIA plugin (`libplugin_INFINIA.so`) by default — meson auto-detects the DDN `red_client` libraries at `/opt/ddn/red` and compiles the plugin into the wheel. The proprietary DDN `libred_*` runtime libraries are intentionally **not** vendored (they remain `auditwheel --exclude`d) and are loaded at runtime from the customer's DDN install. (\#1832)  
- **Wire `--torch-versions` through the container build:** `contrib/Dockerfile` gained a `WHL_TORCH_VERSIONS` build arg (default `2.11,2.12,2.13`) that is forwarded to `contrib/build-wheel.sh` via `--torch-versions` when `BUILD_NIXL_EP=true`, fixing EP container builds that previously failed with `--build-nixl-ep requires --torch-versions`. The EP meson target's `override_options` were also extended to `['buildtype=release', 'optimization=3', 'debug=false']` so a global `--buildtype=debug` no longer leaks `-G` onto the EP `nvcc` compiles. (\#1866)

## Bugfixes

- **\[POSIX/CUDA GDS/GDS MT/HF3FS\] Fixed path-mode double-free and leak on deregister:** Introduced a shared `nixl::PathModeDevIdRegistry` with RAII reserve/commit/release semantics so each path-mode file's `devId` is tracked from `registerMem` through `deregisterMem`, eliminating the ambiguous section-key collision that could free the same backend metadata twice when distinct path-mode files shared a `devId`. Fixes \#1766. (\#1790)

## Known Issues

Full Changelog: [1.3.0...1.3.1](https://github.com/ai-dynamo/nixl/compare/1.3.0...1.3.1)  


## v1.3.2 (2026-07-24)

# 1.3.2

## Summary

NIXL 1.3.2 is a targeted patch release that fixes a cross-node EFA transfer hang introduced in 1.3.1. When the progress thread is enabled, NIXL posts each WRITE descriptor under a separate endpoint lock while using `FI_MORE` to keep a 16-descriptor batch open; on `efa`/`efa-direct` providers, CQ progress can acquire that same endpoint lock before the closing post, leaving the batch permanently open and stalling the transfer. An initial fix disabling `FI_MORE` on EFA (\#1924) was replaced by a more targeted per-rail flush strategy (\#1989) that preserves batching throughput on all providers.

The fix introduces per-rail flush tracking: a precompute pass identifies the last descriptor on each rail before posting begins, and `FI_MORE` is cleared only at that descriptor (or when the per-rail batch reaches `NIXL_LIBFABRIC_FI_MORE_BATCH_SIZE`). This guarantees every rail's batch closes without a fixed-width group boundary assumption and without disabling batching globally.

## Bugfixes

- **\[Libfabric\] Fix cross-node EFA transfer hang with progress thread:** On `efa` and `efa-direct` providers, CQ progress can acquire the endpoint lock between a batch's first and closing `FI_MORE` post, preventing the batch from ever being flushed. NIXL 1.3.1 users with the progress thread enabled would see decode workers stuck in `KVPoll.WaitingForInput` returning empty responses. An intermediate fix that disabled `FI_MORE` entirely on EFA (\#1924) was reverted (\#1984) in favour of the per-rail flush in \#1989, which closes each rail's batch correctly without giving up batching throughput on non-EFA providers. (\#1924, \#1984, \#1989)

## Known Issues

Full Changelog: [1.3.1...75ead3d7](https://github.com/ai-dynamo/nixl/compare/1.3.1...75ead3d7)  


## v1.4.0 (2026-08-14)

# 1.4.0

## Summary

NIXL 1.4.0 centers on performance, observability, and LIBFABRIC correctness. Stride (compressed) descriptors cut prepared-handle memory by orders of magnitude — a 1.4M-descriptor set for DeepSeek-R1-Distill-Qwen-32B shrinks from ~44 MB to ~7 KB — and `make_prepped_xfer` latency drops up to 5.4× in SGLang workloads. 

A new `nixl::trace` tracing framework with an NVTX backend (`libtrace_backend_nvtx.so`) surfaces NIXL operations on Nsight Systems timelines; the telemetry layer gains unified Prometheus/DOCA exporters, 60% lower per-transfer overhead, and new dropped-event, error-count, and byte-gauge metrics. 

The LIBFABRIC backend receives two critical fixes: a pre-connection handshake that prevents transfer-ID collisions across sender processes, and a `FI_MORE` rail-flush correction that eliminates transfer hangs in multi-DRAM-registration workloads. Seven concurrency and correctness fixes land across the core agent and file-seg backends, NIXL-EP wheels now bundle extensions for multiple PyTorch versions in a single distribution, and UCX is updated to v1.22.x to unlock rendezvous PUT/GET protocols.

## Major Features

- **Stride (compressed) descriptors for prep+make:** The prep+make API now encodes prepared handles as stride (run-length) descriptors, collapsing contiguous memory runs into a compact form. A 1,387,520-descriptor set for DeepSeek-R1-Distill-Qwen-32B shrinks from ~44 MB to ~7 KB; `make_prepped_xfer` is up to 5.4× faster in SGLang merge micro-benchmarks and `Avg Prep` time drops from 34 µs to 21 µs in nixlbench. The merge algorithm is also accelerated and uses reserve-instead-of-resize for the internal descriptor vector. (#1756)
- **`nixl::trace` pluggable tracing framework + NVTX backend:** A new internal `nixl::trace` API instruments NIXL operations at one set of call sites and fans out to loadable `.so` backend plugins. NVTX ships as the first backend (`libtrace_backend_nvtx.so`), making NIXL transfer operations, notifications, and lifecycle events appear as colored NVTX ranges on an Nsight Systems timeline (`--trace=cuda,nvtx`). The backend is auto-enabled when the process runs under Nsight Systems, requires only the CUDA toolkit's header-only `nvtx3` to build, and adds near-zero overhead when no profiler is attached. (#1765, #1845, #1867)
- **Multi-PyTorch-version NIXL-EP wheels:** The NIXL-EP wheel build now compiles separate per-PyTorch-version C++ extensions in isolated environments and merges them into a single distribution via a new `contrib/wheel_merge.py` step. The correct ABI extension is selected at import time based on the installed PyTorch version, so one wheel works across PyTorch versions without reinstallation. (#1775)

## API Changes

- **[Telemetry] Prometheus and DOCA metric series renamed to the `*_last_bytes` convention:** The `agent_memory_registered` / `agent_memory_deregistered` gauges are renamed to `agent_memory_registered_last_bytes` / `agent_memory_deregistered_last_bytes`. Prometheus/DOCA scrape configurations referencing the old names must be updated. (#1850)

## Enhancements

### Performance

- **[UCX] Avoid zero-initializing the full `ucp_request_param_t` on each operation:** A recent UCX SGL patch grew `ucp_request_param_t`; zero-initializing the whole struct on every PUT/GET/AM call was measurable — ~2% throughput regression in nixlbench (512B × 64000 ops, 8 threads). Changed to explicitly set only the needed `op_attr_mask`, `memh`, and `flags` fields, dropping the blanket `= {0}` init. (#2022)
- **[Core] Lazy `torch` import cuts NIXL Python startup time:** `torch` is now imported only on demand rather than at `import nixl`, eliminating the ~1 s startup cost for callers that do not use PyTorch. A `TYPE_CHECKING` guard preserves IDE autocompletion; CUDA version detection falls back through CUDA bindings, CuPy, and a lightweight probe when PyTorch is absent. Duplicate logic between the `nixl` and `nixl.ep` modules is consolidated into `nixl_meta_utils.py`. (#1895)
- **[Telemetry] Cut per-transfer telemetry overhead 60% with CPU-counter stopwatch, batched stats, and enum-keyed Prometheus maps:** `nixlDuration` (`nixl_duration.h`) measures post and transfer durations using the invariant TSC (`rdtsc` on x86_64, `cntvct_el0` on aarch64), reducing the per-transfer telemetry cost from ~79 ns to ~32 ns while keeping the exposed `startTime` on a drift-free `CLOCK_MONOTONIC_COARSE` clock. The four xfer-stat events (`agent_xfer_time`, `agent_tx/rx_bytes`, `agent_tx/rx_requests_num`, `agent_xfer_post_time`) are now written under one mutex lock in `addXferStats`, halving lock round-trips on the hot path. The Prometheus exporter's `counters_`/`gauges_` maps are re-keyed on the `nixl_telemetry_event_type_t` enum, eliminating the per-event `std::string` allocation in `exportEvent()`. (#1890, #1844, #1878)

### Networking & Backend

- **[OBJ/S3 CRT] Configurable `throughput_target_gbps` for the S3 CRT client:** Exposes the CRT connection-count target as the optional backend parameter `throughput_target_gbps` (integer Gbps; default remains 10). In testing against a Cloudian HyperStore system, raising this limit raised sustained throughput from 10 GiB/s to 18.13 GiB/s. (#1769)
- **[UCX] Enable rendezvous PUT/GET protocol on UCX ≥ 1.22:** Sets `RNDV_PIPELINE_ERROR_HANDLING=y` at context creation when the runtime UCX version is 1.22 or newer, enabling the rendezvous-based PUT and GET transfer protocols. (#1854)
- **[Libfabric] Add pre-connection handshake to convey sender agent index:** Before the first transfer the LIBFABRIC backend now sends a handshake message carrying the local agent index assigned to the peer. The peer stores this index and uses it as immediate data on all subsequent WRITE and notification posts, allowing the receiver to distinguish transfers from different sender processes that share the same transfer ID. Calling `connect()` before the first transfer avoids any first-transfer stall. Validated with no throughput regression on AWS p5en nodes. (#1736)
- **[Libfabric] Fix `FI_MORE` flush granularity to per-rail instead of per-group:** The prior `FI_MORE` WRITE batching flushed doorbells positionally (last of each 16-descriptor group), which is only correct when every descriptor in a group maps to the same physical rail. Transfers spanning buffers with different rail assignments — e.g. many DRAM registrations in Dynamo — would alternate rails within a group, leaving one rail's batch unsubmitted and causing the transfer to hang. Fixed by precomputing a per-rail flush map in `postXfer` (walking descriptors in reverse to find each rail's last post) and passing an explicit `apply_fi_more` flag into `prepareAndSubmitTransfer`. The new `NIXL_LIBFABRIC_FI_MORE_BATCH_SIZE` env var (default 16) caps consecutive `FI_MORE`-eligible descriptors before an unconditional flush. nixlbench was unaffected (one buffer per device = one rail). (#1966)

### NIXL-EP Example Improvements

- **Dropped-events counter for telemetry loss detection:** Adds a new `agent_telemetry_events_dropped` cumulative counter emitted by both Prometheus (`_total` suffix) and DOCA exporters. When the staging queue is full, drops are accumulated in `droppedEvents_` and flushed as a synthetic event bypassing the queue on the next periodic drain — ensuring the counter itself can never be lost. Bumps `TELEMETRY_VERSION` 3 → 4; `examples/python/telemetry_reader.py` is updated accordingly. (#1887)
- **Private UCX loading via SONAME suffix and `RTLD_DEEPBIND`:** The UCX backend plugin is now loaded with `RTLD_DEEPBIND` by default (opt-out via `NIXL_UCX_DEEPBIND=0`), preventing the bundled UCX from binding to a globally loaded UCX in HPC-X/OpenMPI environments. The container build supports `--ucx-soname-suffix` and `--private-ucx` flags to compile UCX with a private SONAME, and `auditwheel` handling is updated to correctly map the renamed libraries. Set `NIXL_UCX_EXPECTED_SONAME` to fail fast if an unexpected UCX library is bound. (#1673)
- **NVLink low-latency path optimization:** Caches P2P GPU pointers in a per-context GPU-side array (`p2p_ptrs`) instead of calling `nixlGetPtr` on every low-latency send, eliminating redundant pointer resolution. Also reduces the TOPK index width from 64-bit to 32-bit. On the TRT-LLM MoE dispatch benchmark (8×H100, NVLink), NIXL-EP dispatch reaches parity with DeepEP low latency (e.g., 32.55 µs vs. 32.06 µs at batch size 16). (#1751)

### Packaging & Distribution

- **Bump UCX dependency to v1.22.x:** Build tooling, CI matrices, and wheel builds are updated to use UCX v1.22.x, required to enable the rendezvous PUT/GET protocol and the UCX private SONAME extension. (#1868)
- **UCX SPCx and Infinia plugin now bundled in the manylinux wheel:** The manylinux wheel for 1.4.0 includes the UCX SPCx and DDN Infinia storage plugins, making them available without a separate install. (#1968)
- **Install Python bindings from source in the container image:** The reference container `Dockerfile` now builds and installs the `nixl` Python meta-package from source rather than from a pre-built wheel, ensuring installed bindings always match the container's native NIXL build. (#1896)
- **Add NVIDIA Proprietary License to wheel distribution:** The Python wheel now includes `licenses/NVIDIA-proprietary-LICENSE.txt` covering bundled proprietary dependencies. (#1972)

### Benchmarks

- **[LIBFABRIC] Configurable `postXfer` thread pool:** The LIBFABRIC backend now supports a configurable descriptor-posting thread pool for `postXfer()`, controlled by the `num_threads` and `split_batch_size` backend parameters (exposed in the Python config and nixlbench). Validated on two GB200/EFA nodes running LIBFABRIC 1.21.0 with cross-node DRAM WRITE at batch size 2048. (#1581)

### Documentation

- **Unified Prometheus and DOCA/CollectX exporter metric output:** The native Prometheus and DOCA exporters now share a single `constexpr` metric descriptor, ending drift between the two hand-written metric policies. Both exporters emit identical `agent_*` series names, labels, and help text from one source of truth. (#1894)
- **Error counts in telemetry exporters:** Both Prometheus and DOCA exporters now export per-error-type counters, making transfer-error rates visible without parsing NIXL logs. (#1851)
- **Last-operation byte gauges in telemetry exporters:** Adds `agent_memory_registered_last_bytes` / `agent_memory_deregistered_last_bytes` gauges to both exporters, exposing the byte size of the most-recent memory registration and deregistration events. (#1824)
- **Telemetry NOP collector fallback when no sink is attached:** When telemetry is configured but no sink is active, NIXL now falls back to a no-op collector rather than failing or asserting, simplifying telemetry-optional deployments. (#1779)

## Bugfixes

- **[UCX] Fixed infinite loop hanging thread teardown on dedicated-thread exit:** The pending-request drop loop in `nixlUcxDedicatedThread::run()` used a manual iterator but never advanced it, causing the thread to spin indefinitely whenever it exited with queued requests (confirmed by the sibling drain loop's explicit `erase` after `complete()`). Changed to a range-for followed by `clear()`. (#1880)
- **[Core] Fixed shared-lock misuse in `prepMemView` and `releaseMemView`:** Both methods modify `nixlAgentData::mvhToEngine` and therefore require an exclusive lock; they were guarded with `NIXL_SHARED_LOCK_GUARD`, allowing concurrent writers. Replaced with `std::lock_guard`. (#1865)
- **[Core] Fixed race conditions in remote-section invalidation under concurrent disconnect:** In error-handling paths, the agent called `invalidateRemoteData` while holding only a reader lock, enabling data-race corruption. The fix upgrades to an exclusive lock before invalidation and passes a generation token so only the correct stale section is invalidated, preventing spurious removals of concurrently reconnected remotes. (#1811)
- **[Core] Fixed potentially dangling `const char *` pointers in backend plugin metadata:** `nixlBackendPlugin` stored raw pointers to `name` and `version` string arguments that could go out of scope after the factory call; changed to `std::string` copies in `backend_plugin.h`. (#1853)
- **[CUDA_GDS] Enforce unique `devId` per path-mode file across all FILE_SEG backends:** Path-mode registrations in POSIX, CUDA_GDS, GDS_MT, and HF3FS now use a per-engine `PathModeDevIdRegistry` (`src/utils/file/file_path_mode.h`) with RAII `reserve()`/`commit()` semantics, rejecting duplicate path-mode devIds with `NIXL_ERR_INVALID_PARAM`. This eliminates the double-free and ambiguous file-selection bug from #1766. (#1790)
- **[Libfabric] Fixed `FI_MORE` flush grouping causing transfers to hang:** Positional doorbell flushing incorrectly rang only one physical rail's doorbell when descriptors in a batch mapped to different rails; the other rail's batch was never submitted. (See Networking & Backend for the full description of the fix.) (#1966)
- **[nixlbench] Fixed race condition with ASIO runtime on shutdown:** After the final benchmark barrier completes, the ASIO runtime could still receive data and throw an exception, crashing the benchmark process. Fixed by passing a `finishing` flag through the barrier call chain that suppresses further `recvHead()` posts once the last collective is done. (#1963)

## Known Issues

Full Changelog: [v1.3.0...v1.4.0](https://github.com/ai-dynamo/nixl/compare/v1.3.0...v1.4.0)

## v1.4.1 (2026-09-01)

# 1.4.1

## Summary

NIXL 1.4.1 is a focused patch release that closes a use-after-free window in the transfer-request path. `postXferReq`/`estimateXferCost` previously validated a remote xfer handle by name only, so a handle created before a peer disconnect/re-register cycle could still be posted against the new (freed-then-reallocated) generation's metadata, segfaulting in the UCX send path. (#2027)

The release also restores the `num_experts` parameter to the `nixl_ep` example's low-latency `dispatch`/`combine` path, so callers can pin dispatch/combine tensor shapes to a fixed expert capacity instead of having them shift with the active rank mask — letting captured CUDA graphs be reused safely across rank changes. (#2095)

## Enhancements

### NIXL-EP

- **`nixl_ep`: CUDA graph reuse across rank changes:** `dispatch()` regains an optional `num_experts` parameter (previously deprecated in #1693) that fixes the dispatch/combine layout to a caller-supplied expert capacity instead of deriving it from the currently active `active_rank_bound`. Masking or unmasking ranks no longer changes tensor shapes, buffer offsets, or kernel launch parameters when `num_experts` is set, so CUDA graphs captured against `dispatch`/`combine`/`get_next_combine_buffer` remain valid across rank changes. `combine()` and `get_next_combine_buffer()` now derive their rank bound from `layout_range`/an explicit parameter rather than the live `active_rank_bound`, with added shape validation. (#2095)

### Packaging & Distribution

- **`nixl_ep` preview support for PyTorch 2.14:** The manylinux wheel build's `WHL_TORCH_VERSIONS` now includes `2.14`, so published `nixl_ep` wheels add a preview PyTorch 2.14 extension alongside 2.11-2.13. (#2157)

## Bugfixes

- **[Core] Fixed use-after-free on stale-generation transfer handles:** `postXferReq` and `estimateXferCost` now track a per-remote-agent generation counter and reject request handles created against a since-invalidated (freed and re-registered) remote agent with `NIXL_ERR_NOT_FOUND`, instead of dereferencing the freed `nixlUcxPublicMetadata`. Previously, a disconnect that invalidated a peer's metadata followed by re-registration could leave in-flight handles pointing at freed memory, segfaulting in `sendXferRangeBatch`/`ucp_put_nbx`. Follow-up to #1811/#1987. (#2027)

## Known Issues

Full Changelog: [v1.4.0...v1.4.1](https://github.com/ai-dynamo/nixl/compare/v1.4.0...v1.4.1)

