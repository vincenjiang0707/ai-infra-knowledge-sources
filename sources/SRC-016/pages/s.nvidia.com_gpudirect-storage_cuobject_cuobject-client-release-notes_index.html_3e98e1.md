source: https://docs.nvidia.com/gpudirect-storage/cuobject/cuobject-client-release-notes/index.html

# 1. NVIDIA cuObject client Release Notes[#](https://docs.nvidia.com#nvidia-cuobject-client-release-notes)

Release information for NVIDIA® cuObject client.

Version |
Date |
cuObject client libraries with CUDA Release |
|---|---|---|
v1.3.0 |
Aug 18, 2026 |
13.4 |
v1.2.0 |
May 26, 2026 |
13.3 |
v1.0.0 |
Jan 12, 2026 |
13.1.1 |

## 1.1. 1. Introduction[#](https://docs.nvidia.com#introduction)

Release information for NVIDIA® cuObject client for developers and users.

cuObject is a high-performance suite of libraries designed to enable direct data transfers between GPU memory or system memory and object storage (S3-compatible) solution via RDMA. By relying on RDMA operations, rather than TCP transfer methods, cuObject both avoids using CPU kernel code for TCP processing and can bypass the CPU for data payloads. cuObject eliminates the traditional bottleneck of staging data in local scratch file systems, enabling high-throughput data ingestion for AI training and inference at scale.

### 1.1.1. Architecture Overview[#](https://docs.nvidia.com#architecture-overview)

cuObject consists of two primary components:

**cuObjClient**: Provides client-side APIs for GET and PUT operations with user-defined callbacks for control path communication, while data path operations leverage RDMA for high-performance transfers.**cuObjServer**: Implements the RDMA-accelerated server side for S3-compatible object storage services, supporting multi-threaded concurrency, automatic connection management, and Dynamically Connected (DC) transport.

Refer to the following guides for more information about cuObject:

## 1.2. 2. Key Features and Changes[#](https://docs.nvidia.com#key-features-and-changes)

## 1.3. v1.3.0[#](https://docs.nvidia.com#v1-3-0)

Following features have been added in v1.3.0:

**RDMA Token Reset**: Support for resetting an RDMA token when required. This allows the system to invalidate stale RDMA tokens, which prevents unauthorized access from server nodes and improves the security of RDMA-based communication.

## 1.4. v1.2.0[#](https://docs.nvidia.com#v1-2-0)

Following features have been added in v1.2.0:

**Multipath Failover/Failback**: Support for failover and failback across multiple InfiniBand or RoCE NICs.**IPv6 Support**: Support for IPv6-based network configurations.

## 1.5. v1.0.0[#](https://docs.nvidia.com#v1-0-0)

Following features have been added in v1.0.0:

**Zero-Copy Data Path**: Direct RDMA transfers between client and server memory, eliminating CPU involvement in data movement.**GPUDirect RDMA Support**: Native support for CUDA device memory and system memory.**Callback-Based Architecture**: User-defined GET and PUT callbacks for control path communication.**Memory Registration APIs**:`cuMemObjGetDescriptor()`

and`cuMemObjPutDescriptor()`

.**RDMA Token Management**:`cuMemObjGetRDMAToken()`

and`cuMemObjPutRDMAToken()`

for manual descriptor control.**Context Management**:`getCtx()`

utility for extracting user context from callbacks.**Thread-Safe Operations**: Concurrent GET and PUT operations on different registered buffers.

## 1.6. 3. Known Limitations[#](https://docs.nvidia.com#known-limitations)

### 1.6.1. Memory and Size Constraints[#](https://docs.nvidia.com#memory-and-size-constraints)

Maximum memory registration: (4GiB - 64K) per

`cuMemObjGetDescriptor()`

call.`buffer_offset`

is ignored and defaults to 0 in the GET and PUT API calls.Concurrent GET and PUT operations on a single RDMA buffer are not supported.

GET and PUT for GPU unregistered buffers is limited to the

`per_buffer_cache_size_kb`

configuration value specified in the`cufile.json`

configuration.GET and PUT for host memory is not supported for unregistered buffers.

The

`execution`

section in`cufile.json`

does not apply for cuObject, which means cuObject does not use a threadpool for issuing IOs.The memory key can be reused after a deregister followed by a re-registration. For server error handling scenarios, either the server should guarantee that all outstanding IOs are drained or the client should call

`cuFileDriverClose()`

to reject any stale RDMA IO requests from corrupting newer registrations.For unregistered CUDA managed memory,

`cuMemObjGetMaxRequestCallbackSize()`

currently returns`-1`

.RDMA multipathing requires at least two active RDMA devices during driver initialization to support failover and failback.


## 1.7. 4. Getting Started[#](https://docs.nvidia.com#getting-started)

### 1.7.1. Hardware Requirements[#](https://docs.nvidia.com#hardware-requirements)

x86_64 or ARM64 (Grace CPU only) CPU architecture

Mellanox ConnectX-5 and above InfiniBand HCA or RoCE-capable Ethernet adapter

NVIDIA GPU with CUDA Compute Capability 6.0 or higher (for GPU memory operations)

Minimum 16 GB system RAM recommended


### 1.7.2. Software Requirements[#](https://docs.nvidia.com#software-requirements)

Linux operating system (tested on Ubuntu 22.04 and 24.04, RHEL 9 and 10)

CUDA Toolkit 13.1.1 or later

NVIDIA GPU Driver compatible with CUDA 13.1.1

InfiniBand and RDMA drivers and libraries (

`libibverbs`

,`librdmacm`

)CUDA runtime libraries for GPU memory support

GPUDirect Storage (GDS) libraries (for GPU and system memory support)

C++14 or later compatible compiler


### 1.7.3. Installation[#](https://docs.nvidia.com#installation)

#### 1.7.3.1. Install DOCA and RDMA Libraries[#](https://docs.nvidia.com#install-doca-and-rdma-libraries)

Use the [DOCA Installation Guide for Linux](https://docs.nvidia.com/doca/sdk/DOCA-Installation-Guide-for-Linux/index.html) to install DOCA.

#### 1.7.3.2. Install cuObject client Libraries[#](https://docs.nvidia.com#install-cuobject-client-libraries)

cuObject client libraries are part of CUDA Toolkit. Follow the instructions from cuObject client library downloads.

### 1.7.4. Verify Installation[#](https://docs.nvidia.com#verify-installation)

```
# Check library presence
$ ldconfig -p | grep cuobj
$ ldconfig -p | grep cufile
# Verify cuObjClient installation
$ rpm -qa | grep cuobjclient # RHEL/CentOS
$ dpkg -l | grep cuobjclient # Ubuntu/Debian
# Verify GDS support
$ /usr/local/cuda/gds/tools/gdscheck -p
```

## 1.8. 5. Fixed Issues[#](https://docs.nvidia.com#fixed-issues)

## 1.9. v1.2.0[#](https://docs.nvidia.com#id1)

Fixed

`cuMemObjGetMaxRequestCallbackSize()`

behavior for unregistered CUDA device memory to return the configured GPU bounce-buffer capacity, including larger bounce-buffer configurations.Fixed

`cuMemObjGetMaxRequestCallbackSize()`

so that it does not advertise a callback size larger than`CUOBJ_MAX_MEMORY_REG_SIZE`

.Reduced the maximum registration size from 4 GiB to 4 GiB - 64 KiB to stay within descriptor size limits.

Fixed support for RDMA device and interface names in

`rdma_dev_addr_list`

.Fixed an issue where the maximum log file size could not be configured. Use

`logging.max_file_size_mb`

to configure the maximum log file size.

### 1.9.1. v1.0.0[#](https://docs.nvidia.com#id2)

This is the initial release of cuObject v1.0.0. No prior versions exist.

## 1.10. 6. Open Issues[#](https://docs.nvidia.com#open-issues)

None reported for v1.0.0 initial release.