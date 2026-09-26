source: https://docs.nvidia.com/gpudirect-storage/nvidia_fs/index.html

# 1. NVIDIA GPUDirect Storage Filesystem Kernel Driver (nvidia-fs)[#](https://docs.nvidia.com#nvidia-gpudirect-storage-filesystem-kernel-driver-nvidia-fs)

Release and usage information for the NVIDIA® Magnum IO GPUDirect® Storage (GDS) filesystem kernel
driver, `nvidia-fs`

.

# 2. Overview[#](https://docs.nvidia.com#overview)

The GPUDirect Storage kernel driver, `nvidia-fs.ko`

, is a kernel module that orchestrates I/O
directly from DMA/RDMA-capable storage to user-allocated GPU memory on NVIDIA data-center class GPUs.

For more details on using GPUDirect Storage, refer to
[GPUDirect Storage](https://docs.nvidia.com/gpudirect-storage/index.html). The GDS documents and
online resources provide additional context for the optimal use and understanding of GPUDirect Storage.

# 3. Release Information[#](https://docs.nvidia.com#release-information)

This page tracks `nvidia-fs`

driver releases only. The latest published `nvidia-fs`

driver version
is 2.30.

The driver is available through the following official distribution channel:

For the authoritative release history, refer to the
[ChangeLog](https://github.com/NVIDIA/gds-nvidia-fs/blob/master/ChangeLog). Driver releases and
source are available at
[gds-nvidia-fs releases](https://github.com/NVIDIA/gds-nvidia-fs/releases).

# 4. Key Features[#](https://docs.nvidia.com#key-features)

The driver supports the following storage solutions:

NVMe and NVMe over Fabrics (NVMe-oF) block storage

EXT4 in ordered mode on NVMe and NVMe-oF

XFS on NVMe and NVMe-oF

NFS over RDMA with MOFED 5.1 and later

RDMA-capable distributed file systems, including DDN EXAScaler, WekaFS, VAST, IBM Spectrum Scale, and BeeGFS


# 5. Version History[#](https://docs.nvidia.com#version-history)

Refer to the `ChangeLog`

file that is included in the package for more information.

# 6. Known Limitations[#](https://docs.nvidia.com#known-limitations)

The following limitations are specific to the `nvidia-fs`

driver:

Version 2.17.5 and later requires the NVIDIA UNIX Open Kernel Module on x86_64.

Kernel compatibility depends on the

`nvidia-fs`

version.`nvidia-fs`

must be rebuilt or reinstalled after an NVIDIA driver upgrade that changes exported P2P symbols.For NVMe deployments that use

`nvidia-fs`

, DOCA 3.3.x is not supported. Use DOCA 3.2.x or earlier.The module requires a storage or filesystem driver that implements the corresponding

`nvidia-fs`

callback integration.

# 7. Getting Started[#](https://docs.nvidia.com#getting-started)

## 7.1. Hardware Requirements[#](https://docs.nvidia.com#hardware-requirements)

A supported NVIDIA data-center class GPU with compute capability 6.0 or later.

An NVMe or NVMe-oF device, or a supported distributed filesystem with

`nvidia-fs`

integration.

## 7.2. Software Requirements[#](https://docs.nvidia.com#software-requirements)

NVIDIA open kernel driver 535 or later.

CUDA Toolkit 12.2 or later as a packaging and build prerequisite.

DOCA 3.2.x/MOFED 25.10 or later for NVMe, NVMe-oF, and NFS support.


The following table lists the minimum kernel version for each supported operating system distribution.

Operating System Distribution |
Minimum Kernel Version |
|---|---|
Red Hat Enterprise Linux |
4.18.0-477 |
Rocky Linux |
4.18.0-477 |
Ubuntu |
5.15.0-67 |

## 7.3. Installation[#](https://docs.nvidia.com#installation)

### 7.3.1. Install NVIDIA Open Source Driver[#](https://docs.nvidia.com#install-nvidia-open-source-driver)

To install the open kernel module flavor, follow the instructions in the
[NVIDIA Driver Installation Guide](https://docs.nvidia.com/datacenter/tesla/driver-installation-guide/latest/index.html).

Install the NVIDIA driver before you install `nvidia-fs`

. When the NVIDIA driver is subsequently
upgraded, DKMS automatically rebuilds `nvidia-fs`

.

### 7.3.2. Verify NVIDIA Driver[#](https://docs.nvidia.com#verify-nvidia-driver)

To verify that the NVIDIA Open Kernel Module driver is installed and loaded, run the following command:

```
$ cat /proc/driver/nvidia/version
```

On a system with the Open Kernel Module flavor, you should see output that is similar to the following:

```
NVRM version: NVIDIA Open Kernel Module ...
GCC version: gcc version 13.3.0
```

### 7.3.3. Install nvidia-fs[#](https://docs.nvidia.com#install-nvidia-fs)

Follow the instructions on the
[nvidia-fs download page](https://developer.nvidia.com/nvidia-fs-downloads).

### 7.3.4. Verify nvidia-fs[#](https://docs.nvidia.com#verify-nvidia-fs)

After the package is installed, load the driver if it is not already present:

```
$ sudo modprobe nvidia_fs
```

To check that the driver is present, run the following command:

```
$ lsmod | grep nvidia_fs
nvidia_fs 274432 0
nvidia 16388096 8 nvidia_uvm,nvidia_fs,nvidia_modeset
```

To inspect the installed module metadata, run the following command:

```
$ modinfo nvidia_fs
```

Enable the peer-affinity counters only while you diagnose topology, and then inspect the affinity and distance tables:

```
$ echo 1 | sudo tee /sys/module/nvidia_fs/parameters/peer_stats_enabled
$ cat /proc/driver/nvidia-fs/peer_affinity
$ cat /proc/driver/nvidia-fs/peer_distance
```

To reset the driver counters, run the following command:

```
$ echo 1 | sudo tee /proc/driver/nvidia-fs/stats
```

Read and write counters are disabled by default because they can affect small-I/O performance. To check or disable these counters, run the following commands:

```
$ cat /sys/module/nvidia_fs/parameters/rw_stats_enabled
$ echo 0 | sudo tee /sys/module/nvidia_fs/parameters/rw_stats_enabled
```

# 8. Additional Package Availability Notes[#](https://docs.nvidia.com#additional-package-availability-notes)

Starting with CUDA 13.4,

`nvidia-fs`

is released separately and is no longer included in the CUDA runfile or CUDA local repository.In the CUDA network repository,

`nvidia-fs`

remains available as a dependency of the`nvidia-gds`

meta-package. For installs that also use packages.nvidia.com, users can enable multiple repositories; apt, dnf, and zypper resolve dependencies across the union of enabled repos. Until`nvidia-fs`

is backfilled there, keep the CUDA repo enabled alongside packages.nvidia.com when installing`nvidia-gds`

.For local repository, the

`nvidia-fs`

local repository package is provided separately from the CUDA local repository package.**Both repositories must be available for the nvidia-gds meta-package dependencies to be resolved.**