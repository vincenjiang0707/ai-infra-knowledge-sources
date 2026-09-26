source: https://docs.nvidia.com/gpudirect-storage/cuobject/cuobject-server-release-notes/index.html

# 1. NVIDIA cuObject Server Release Notes[#](https://docs.nvidia.com#nvidia-cuobject-server-release-notes)

Release information for NVIDIA® cuObject server.

# 2. Release information[#](https://docs.nvidia.com#release-information)

Version |
Date |
cuObject server libraries with CUDA Release |
|---|---|---|
v2.0.0 |
Aug 18, 2026 |
13.4 |
v1.2.0 |
May 26, 2026 |
13.3 |
v1.0.0 |
Jan 12, 2026 |
13.1.1 |

# 3. Introduction[#](https://docs.nvidia.com#introduction)

Release information for NVIDIA® cuObject server for developers and users.

cuObject is a high-performance suite of libraries designed to enable direct data transfers between GPU memory or system memory and an object storage (S3-compatible) solution via RDMA. By relying on RDMA operations, rather than TCP transfer methods, cuObject avoids using CPU kernel code for TCP processing and can bypass the CPU for data payloads. cuObject eliminates the traditional bottleneck of staging data in local scratch file systems, enabling high-throughput data ingestion for AI training and inference at scale.

## 3.1. Architecture overview[#](https://docs.nvidia.com#architecture-overview)

cuObject consists of two primary components:

**cuObjClient**: Provides client-side APIs for GET and PUT operations with user-defined callbacks for control path communication, while data path operations leverage RDMA for high-performance transfers.**cuObjServer**: Implements the RDMA-accelerated server side for S3-compatible object storage services, supporting multi-threaded concurrency, automatic connection management, and Dynamically Connected (DC) transport.

Refer to the following guides for more information about cuObject:

# 4. Key features and changes[#](https://docs.nvidia.com#key-features-and-changes)

## 4.1. v2.0.0[#](https://docs.nvidia.com#v2-0-0)

Following features have been added in v2.0.0:

Added an event-driven completion mode that allows applications to wait on completions through a standard file descriptor by using

`poll`

,`epoll`

, or`io_uring`

.Added multi-VIP failover and rotation to keep RDMA data paths available during a VIP swap.


## 4.2. v1.2.0[#](https://docs.nvidia.com#v1-2-0)

Following features have been added in v1.2.0:

IPv6 support

Support max_rd_atomic parameter in the RDMA configuration


## 4.3. v1.0.0[#](https://docs.nvidia.com#v1-0-0)

Following features have been added in v1.0.0:

Multi-threaded, channel-based concurrency

Scatter-gather I/O support (up to 10 entries)

Asynchronous operation and polling


# 5. Known limitations[#](https://docs.nvidia.com#known-limitations)

## 5.1. Memory and size constraints[#](https://docs.nvidia.com#memory-and-size-constraints)

Maximum operation size: 1 GiB per

`handleGetObject()`

or`handlePutObject()`

callMaximum scatter-gather entries: 10 entries per operation

Maximum SGE per operation: configurable via

`max_sge`

parameter (default: 10)Async operations:

`poll()`

caps`max_events`

to`16`

MaxRdAtomic: For optimal PUT performance using

`RDMA_READ`

, set`MaxRdAtomic`

by using`setMaxRdAtomic(16)`

;`0`

enables auto-detection

## 5.2. ABI compatibility[#](https://docs.nvidia.com#abi-compatibility)

The server version has been updated to 2.0.0. Binaries compiled with older versions are not expected to work with this version.


# 6. Getting started[#](https://docs.nvidia.com#getting-started)

## 6.1. Hardware requirements[#](https://docs.nvidia.com#hardware-requirements)

x86_64 or ARM64 CPU architecture

Mellanox ConnectX-5 and above InfiniBand HCA, or RoCE-capable Ethernet adapter

Minimum 16 GB system RAM recommended


## 6.2. Software requirements[#](https://docs.nvidia.com#software-requirements)

Linux operating system (tested on Ubuntu 22.04 and 24.04, RHEL 8, 9, and 10)

InfiniBand and RDMA drivers and libraries (

`libibverbs`

,`librdmacm`

)C++14 or later compatible compiler


## 6.3. Installation[#](https://docs.nvidia.com#installation)

### 6.3.1. Install DOCA and RDMA libraries[#](https://docs.nvidia.com#install-doca-and-rdma-libraries)

Use the DOCA installation guide to install DOCA.

### 6.3.2. Install cuObject server library[#](https://docs.nvidia.com#install-cuobject-server-library)

Follow the instructions from cuObject Server library downloads.

### 6.3.3. Verify installation[#](https://docs.nvidia.com#verify-installation)

```
# Check library presence
ldconfig -p | grep cuobj
# Verify cuObjServer installation
rpm -qa | grep cuobjserver # RHEL/CentOS
dpkg -l | grep cuobjserver # Ubuntu/Debian
```

# 7. Fixed issues[#](https://docs.nvidia.com#fixed-issues)

## 7.1. v1.2.0[#](https://docs.nvidia.com#id8)

Fixed

`app_wr_id_dci`

allocation to use the configured`cq_depth`

instead of a fixed send queue depth.Added

`max_rd_atomic`

handling so that the RDMA READ depth is configurable or auto-detected instead of fixed at`1`

.Improved RDMA error reporting to include actual

`errno`

strings in many failure paths.

## 7.2. v1.0.0[#](https://docs.nvidia.com#id9)

This is the initial release of cuObject server v1.0.0. No prior versions exist.

# 8. Open issues[#](https://docs.nvidia.com#open-issues)

None reported for the v1.0.0 initial release.