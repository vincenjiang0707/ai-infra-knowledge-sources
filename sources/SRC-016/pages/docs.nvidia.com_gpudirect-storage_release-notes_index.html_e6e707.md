source: https://docs.nvidia.com/gpudirect-storage/release-notes/index.html

# 1. NVIDIA GPUDirect Storage Release Notes[#](https://docs.nvidia.com#nvidia-gpudirect-storage-release-notes)

Release information for NVIDIA® Magnum IO GPUDirect® Storage.

# 2. Introduction[#](https://docs.nvidia.com#introduction)

Release information for NVIDIA® GPUDirect® Storage (GDS) for developers and users.

NVIDIA Magnum IO GPUDirect Storage (GDS) is one of the members of the GPUDirect family of technologies. GDS enables a direct data path for direct memory access (DMA) transfers between GPU memory and storage. This direct path increases IO bandwidth, decreases IO latency and reduces the utilization load on the host CPU.

GDS is generally available on third party storage solutions such as DDN EXAScaler, Dell EMC Isilon, IBM Spectrum Scale,
NetApp ONTAP and BeeGFS, WekaFS, VAST NFS, Dell Isilon, and Micron. See the [Support Matrix](https://docs.nvidia.com#support-matrix) for the complete list.
GDS documents and online resources provide additional context for the optimal use of and understanding of GPUDirect Storage.

Refer to the following guides for more information about GDS:

To learn more about GDS, refer to the following posts:

[GPUDirect Storage: A Direct Path Between Storage and GPU Memory](https://devblogs.nvidia.com/gpudirect-storage/)The

[Magnum IO](https://developer.nvidia.com/blog/tag/magnum-io/)blog series.

# 3. New Features and Changes[#](https://docs.nvidia.com#new-features-and-changes)

v1.19.1

Added support for VDURA PanFS.

Fixed assorted bugs.


v1.19

Added cuFile APIs to perform scatter-gather I/O across multiple buffers.

Added

`vanilla_posix_mode`

, which performs POSIX-mode I/O when any of the libraries required by cuFile are missing.Improved sparse-file read performance with P2P DMA on EXT4 and XFS by automatically using a more efficient data path when sparse regions are detected. This optimization is enabled by default for larger reads (16 KiB and above) and helps avoid performance degradation when accessing sparse files. To disable it, set the following in

`/etc/cufile.json`

:"sparse": { "p2p_compat_enable": false }

Added support for RAID1 and RAID10 on NVMe drives in the following configurations:

**x86 platforms**: Supported with`nvidia-fs`

.**Grace-based platforms**: Supported with`nvidia-fs`

and C2C mode.**x86 P2PDMA mode**: Supported starting with kernel 7.2 and later.

To enable C2C/P2PDMA mode for RAID1 and RAID10, configure the following settings in

`/etc/cufile.json`

:"block": { "nvme": { "use_pci_p2pdma": true }, "raid1": { "use_pci_p2pdma": true }, "raid10": { "use_pci_p2pdma": true } }


v1.18.1

Improved multithreaded I/O performance for access sizes larger than 8 MiB on distributed file systems


V1.18

Enhanced the accuracy of byte-count reporting during file writes to provide consistent progress information.

Removed the batch I/O size limitation for GDS mode that was caused by the bounce buffer size.

Added support for Linux kernel 7.0 to

`nvidia-fs`

.Improved multithreading performance on Grace-based platforms.

Fixed assorted bugs.


V1.17

Reduced buffer management overhead through DMA-Buf interoperability.

Added tunable bounce buffer sizing for each mode to better match application and topology behavior.

Added deterministic routing and visibility control for multi-GPU and multi-path environments.

Added a structured JSON-based API to simplify integration and automation.

Integrated support for user-defined system topologies.

Updated the compatibility path to support ZFS and BTRFS across all I/O APIs.

Added support for specifying GPU bounce buffer configuration by using

`gpu_bounce_buffer_slab_config`

in`cufile.json`

, similar to POSIX slab properties.Added deprecation warnings for uniform bounce buffer configuration parameters and APIs.

Included assorted bug fixes.


V1.16

Update

`gdscheck`

output to specify the modes (`p2pdma`

,`nvfs`

,`compat`

) supported by`libcufile`

.Added P2P configuration APIs:

`cuFileDriverSetP2PFlags()`

: Configure P2P transfer flags for specific filesystem or device types.`cuFileDriverGetP2PFlags()`

: Query current P2P flag settings.

Removed batch io size limitation due to the bounce buffer size. For any batch I/Os larger than the bounce buffer size, it would now perform a posix I/O.

Added support for Amazon FSx for Lustre with GPUDirect Storage. GPUDirect Storage now interoperates with Amazon FSx for Lustre on Amazon EC2, enabling a direct data path between Lustre and NVIDIA GPUs. This reduces CPU utilization and can increase throughput for data-intensive GPU workloads. See the GPUDirect Storage Overview for supported file systems and configuration notes.

SLES distro supports GDS in P2PDMA mode.

Assorted bug fixes


v1.15.1

Assorted bug fixes.


V1.15

After a reboot, the first time an application launches,

`cuFileStatsStart`

may fail when called after`cuFileStatsStop`

. This issue is not observed in subsequent application launches.Statistics collection API routines for

`cuFile`

operationsRemoved support for NVIDIA Pascal and Volta architectures

Assorted bug fixes


v1.14

Added support for NEC ScaTeFS.

Updated GDS user level stats to show P2PDMA stats

Updated nvidia-fs.ko to support 6.12 kernel

Introduced

`Get/Put`

API interfaces for GDS Parameters, enabling retrieval and modification of parameter values for`size_t`

,`bool`

, and`string`

types.Assorted bug fixes


**Features introduced in previous releases:**

v1.13

Improved unregistered buffer IO performance for larger IO size using threadpool.

Improved unregistered buffer IO performance by increasing the internal bounce buffer size. The size can be configured up to a max of 16MiB using the JSON parameter

`per_buffer_cache_size_kb`

.On Grace+Hopper systems, DDN Exascaler GDS p2p mode is supported with 64K kernel PAGE SIZE for transfer sizes that are 4KB aligned but not 64K aligned.

Updated nvidia-fs.ko to support more PCIe Devices, to support Amazon Fsx for Lustre.

Stability fixes during driver close and batch close operations.

Added support for new “NVME P2PDMA” feature for GDS. This mode supports GDS with NVMe linux upstream drivers, minimum kernel version >= 6.2 (Ubuntu 22.04) and 5.14 (RHEL 9.4) on x86_64 based platforms. This feature will eliminate the need for custom MOFED NVMe patches and nvidia-fs.ko to support GDS with Ext4 and XFS with NVMe drives.


v1.11.1

Assorted bug fixes.


v1.11

Added support for RHEL 8.10, RHEL 9.4 and UB 24.04.

Assorted bug fixes.


v1.10.1

Assorted bug fixes.


v1.10

Assorted bug fixes.


v1.9.1

Assorted bug fixes.


v1.9

Added support for RHEL 9.3 and UB 22.04.3.


v1.8.1

Added support for RHEL 9.2 on Grace Hopper platform with 64K host OS page size for EXT4 filesystems with Local NVMe.

Improved the IO throughput performance for applications by adding topology awareness in compatibility mode.


v1.8

Assorted bug fixes.


v1.7.2

Added Grace Hopper platform Support with 64K host OS page size for EXT4 filesystems with Local NVMe on Ubuntu 22.04 with HWE kernels.

Proprietary NVIDIA kernel module is not supported. Only the NVIDIA

[open kernel](https://us.download.nvidia.com/XFree86/Linux-x86_64/535.104.05/README/kernel_open.html)module will be supported.cuFile APIs can be used in Cloud-service-providers environments in compatibility mode.


v1.7

Support for APIs

`cuFileStreamRegister`

,`cuFileStreamDeregister`

,`cuFileReadAsync`

, and`cuFileWriteAsync`

is complete. This enables use of CUDA Streams with cuFile APIs.cuFile APIs can be used with system memory.

cuFile APIs can now be used with non-O_DIRECT file descriptors.

Threadpool support is enabled by default and is required for cuFile APIs supporting CUDA streams.


v1.6.1

Improved batch API performance.

Implemented threadpool in the cuFile library to enable parallelism and improve throughput of a large IO request using a single user thread.


v1.5.1

Assorted bug fixes.


v1.5:

Added support for

`cuMem*`

memory allocations with cuFile APIs.

v1.4:

Hopper PCIe support.

RHEL 9.0 and Ubuntu 22.04 support.


v1.3.1:

GDS can be now installed through CUDA

`.run`

files.Support for Ubuntu 22.04 and RHEL9.

Improvements to NIC to GPU affinity for userspace RDMA file systems.


v1.3

Initial support for Linux dma-buf.


v1.2.1

GDS now supports vGPU in VMware context. Refer to

[https://docs.nvidia.com/grid/latest/grid-vgpu-release-notes-generic-linux-kvm/index.html#gpudirect-technology-support](https://docs.nvidia.com/grid/latest/grid-vgpu-release-notes-generic-linux-kvm/index.html#gpudirect-technology-support)and[https://docs.nvidia.com/grid/latest/grid-vgpu-user-guide/index.html#cuda-open-cl-support-vgpu](https://docs.nvidia.com/grid/latest/grid-vgpu-user-guide/index.html#cuda-open-cl-support-vgpu)for more information.

v1.2

Support for BeeGFS.

Support for XFS.

Batch APIs available for use (Alpha level support).


v1.1.1:

Use

`nvidia_peermem`

default for userspace RDMA filesystems (GPFS, WekaFS). In order to use`nvidia_peermem`

, load it using:`# modprobe nvidia_peermem`

Added support for BeeGFS (preview).


v1.1:

The XFS file system has been added to the list of supported file systems at a a beta support level.

Improved support for unregistered buffers.

Added options

`start_offset`

and`io_size`

to gdsio config file per job options.Improved performance of 4K and 8K IO sizes for local file systems.

Added user-configurable priority for internal cuFile CUDA streams.


v1.0:

New configuration and environment variables for the cuFile library.

Fixed error handling behavior for Weka retriable and unsupported errors.

Removed hard dependency on

`librcu-bp`

.Added read support for IBM Spectrum Scale.


v0.95:

Compatibility with POSIX IO is enabled by default.

Alpha level support for RHEL 8.3.

GDS is available as Technical preview for DGX OS.

Support for MLNX_OFED 5.3 for NVMe and NVMeOF.

Support for Excelero NVMesh devices.

Support for ScaleFlux computational storage.

Integration with DALI® and PyTorch.

Experimental RAPIDS integration for cuDF, unoptimized, reads only.


# 4. MLNX_OFED/DOCA and File System Requirements[#](https://docs.nvidia.com#mlnx-ofed-doca-and-file-system-requirements)

The following are the MLNX_OFED/DOCA and file system requirements for GDS:

MLNX_OFED/DOCA must be installed

**before**installing GDS. Refer to[Installing GPUDirect Storage](https://docs.nvidia.com/gpudirect-storage/troubleshooting-guide/index.html#gds-installing)for more information about installing MLNX_OFED.`nvidia-fs.ko`

requires Linux kernels 4.15.x and above.Ubuntu 22.04.3 is not supported with any publicly available MLNX_OFED versions at this time.

For NVMe drives accessed through

`nvidia-fs`

, DOCA version compatibility also depends on your Linux kernel version. See[Known Limitations](https://docs.nvidia.com#known-limitations)for details.

MLNX_OFED/DOCA version |
Distros supported |
Notes |
|---|---|---|
5.4-x (LTS) |
Ubuntu 18.04, 20.04,22.04, RHEL 8.x (>8.4), RHEL 9 |
|
5.5-x |
Ubuntu 18.04, 20.04, RHEL 8.4, RHEL 8.6 |
|
5.6-x |
Ubuntu 18.04, 20.04, RHEL 8.4, RHEL 8.6 |
|
5.7-x |
Ubuntu 18.04, 20.04, RHEL 8.4, RHEL 8.6 |
Does not support RHEL9 and UB22.04 |
5.8-x (LTS) |
Ubuntu 18.04, 20.04,22.04, RHEL 8.x (>8.4), RHEL 9, Rocky Linux 9.x, RockyLinux 8.x |
|
5.9-x |
UB22.04 and RHEL 9.1, 8.7 |
NVMeOF is not functional. |
23.04-x |
UB22.04 and RHEL 9.2, 8.8 |
NVMeOF is not functional. |
23.07-x |
UB22.04 and RHEL 9.2, 8.8 |
NVMeOF is not functional |
23.10 |
UB22.04 and RHEL 9.2 |
|
24.04-x |
UB24.04 and RHEL 9.4 |
|
DOCA 3.1-x |
UB24.04 and RHEL 9.6, 9.7, 10 |
|
DOCA 3.4.1 |
UB26.04 and RHEL 10.2 |
RHEL 10.2 support is enabled with DOCA 3.4.1 |

# 5. Support Matrix[#](https://docs.nvidia.com#support-matrix)

Supported GPUs: Data Center and Quadro (desktop) cards with compute capability > 6 listed [here](https://developer.nvidia.com/cuda-gpus#compute)
are supported in GDS mode. All other cards are supported only in compatibility mode.

**Partner/Distributed File Systems**

Partner Company |
Partner Product Version |
Compatible GDS Version |
Date |
|---|---|---|---|
Amazon Web Services (AWS) |
FSx for Lustre, Lustre 2.15 clients on Ubuntu 22.04 (kernel 6.8 or higher) |
1.13.1 |
November 2024 |
DDN |
EXAScaler 5.2 and newer EXAScaler 6.0 and newer |
1.1 and higher |
November 2021 |
DellEMC |
PowerScale 9.2.0.0 |
1.0 |
October 2021 |
Hammerspace |
Hammerspace 5.0 |
1.8 |
January 2024 |
Hitachi Vantara |
HCSF |
1.0 |
October 2021 |
HPE Data Fabric |
7.2 and newer |
1.3 and higher |
July 2025 |
HPE Cray ClusterStor |
Neo 4.2 and newer |
1.0 and higher |
September 2021 |
HPE GreenLake File Storage |
3.0 |
1.10 |
June 2024 |
IBM |
Spectrum Scale 5.1.2 and newer |
1.1 and higher |
November 2021 |
NetApp |
ONTAP 9.10.1 |
1.0 and higher |
January 2022 |
NetApp ThinkParQ System Fabrics Works |
7.3.0 |
1.1.1 and higher |
March 2022 |
Pure Storage |
FlashBlade |
1.7 and higher |
December 2023 |
VAST |
Universal Storage 4.1 |
1.1 and higher |
November 2021 |
VDURA |
PanFS |
1.19.1 and higher |
September 2026 |
WekaIO |
WekaFS 3.13 |
1.0 |
June 2021 |

# 6. GDS Enabled Libraries/Frameworks[#](https://docs.nvidia.com#gds-enabled-libraries-frameworks)

GDS has been enabled in the following libraries and frameworks:

RAPIDS cuDF:

[More details](https://docs.rapids.ai/api)CLARA cuCIM:

[More details](https://github.com/rapidsai/cucim/blob/9e346db3a2c9f3a5be931b614f16d31d0bd88cc6/notebooks/Accessing_File_with_GDS.ipynb)DALI: Python frameworks such as PyTorch are enabled to use DALI, which is in turn enabled with GDS:

[More details](https://docs.nvidia.com/deeplearning/dali/main-user-guide/docs/examples/general/data_loading/numpy_reader.html#GPUDirect-Storage-Support)MONAI: Python Framework for Medical Imaging and Deep learning:

[More details](https://github.com/Project-MONAI/tutorials/blob/main/modules/GDS_dataset.ipynb)Clara Parabricks:

[More details](https://docs.nvidia.com/clara/parabricks/latest/bestperformance.html#gds-support)NIXL IO Backend:

[More details](https://github.com/ai-dynamo/nixl/blob/main/src/plugins/cuda_gds/README.md)

# 7. Filesystem Classification Matrix[#](https://docs.nvidia.com#filesystem-classification-matrix)

Filesystems that are designed for data center and HPC cluster deployments with GDS support are classified as enterprise/deployment ready. Developer-friendly filesystems that do not provide native GDS support, but can be used with compatibility mode, are more suited for local development and testing.

Filesystem |
Classification |
|---|---|
EXT4 |
Enterprise/Deployment |
XFS |
Enterprise/Deployment |
DDN EXAScaler |
Enterprise/Deployment |
IBM Spectrum Scale |
Enterprise/Deployment |
WekaFS |
Enterprise/Deployment |
BeeGFS |
Enterprise/Deployment |
NFS |
Enterprise/Deployment |
ScaTeFS |
Enterprise/Deployment |
VirtioFS |
Enterprise/Deployment |
TMPFS |
Developer Friendly |
OverlayFS |
Developer Friendly |
ZFS |
Developer Friendly |
BTRFS |
Developer Friendly |

Note

Filesystems such as TMPFS do not support `O_DIRECT`

mode.

# 8. Included Packages[#](https://docs.nvidia.com#included-packages)

The GDS package contains the following Debian packages:

`gds-tools-13-4_*.deb`

`libcufile-13-4_*.deb`

`libcufile-dev-13-4_*.deb`

`nvidia-fs.*.deb`

`nvidia-fs-dkms.*.deb`

`nvidia-gds-13-4_*.deb`


Note

Each component has a README file. For example, for `gds-tools`

, the README file is in the `/usr/local/cuda-13.4/gds/tools/`

directory.

# 9. Minor Updates and Bug Fixes[#](https://docs.nvidia.com#minor-updates-and-bug-fixes)

The following minor updates and bug fixes were made in version **1.14**:

Fix to

`nvidia-fs.ko`

to support PCIe devices with the same BDF across two different PCIe domains.Minor bug fixes.


# 10. Known Issues[#](https://docs.nvidia.com#known-issues)

GDS does not work on OpenShift with NW Operator version 24.

When using NW Operator 25.1.0 on OpenShift with

`ENABLE_NFSRDMA`

and`UNLOAD_STORAGE_DRIVERS`

set to`true`

, the OpenShift installation might get corrupted. This issue is resolved in NW Operator 25.7 and above.Using

`nvidia-fs`

version 2.25.6 may cause cuFile APIs to fail when using GDS P2P mode with the`nvidia-fs`

kernel driver. We recommend using`nvidia-fs`

version 2.25.7 or newer from the GitHub release:[nvidia-fs v2.25.7](https://github.com/NVIDIA/gds-nvidia-fs/releases/tag/v2.25.7).`NVME P2PDMA`

mode is currently not supported on RHEL 9.5 for x86.`NVME P2PDMA`

can fail on x86_64 platforms when KASLR is enabled in the linux kernel. The feature can be disabled by specifying the`nokaslr`

kernel parameter.Without nvidia-persistenced enabled,

`NVME P2PDMA`

can increase the time taken to start the driver initialization for B200 platforms.Sparse file IO performance on Ext4 with

`NVME P2PDMA`

is slower on x86_64 platforms compared to GDS P2PDMA with`nvidia-fs.ko`

.When installing via .run file, the installation of GPUDirect Storage components fails if MLNX_OFED is not installed.

The cuFile library may fail to load GPU topology information properly when udev information is not accessible to the application. Ensure the correct udev library is installed.

`nvidia-fs`

can deadlock in`nv_p2p_dma_map_pages`

and`nv_p2p_mem_info_free_callback`

functions when the user frees the CUDA memory without calling`cuFileBufDeregister`

on registered buffers.On DDN EXAScaler file systems:

With stripe count > 1,

`cuFileRead`

and`cuFileWrite`

do not work with poll mode enabled for versions older than 2.12.5_ddn10.With 2.12.5_ddn10, any reads beyond EOF causes a BUG_ON inside

`nvidia-fs`

.

The

`cuFileRead`

and`cuFileWrite`

APIs fail when working on`cuMemMap`

allocations with multiple GPUs, when the IO request to a GPU buffer is not 4K aligned and spans across multiple GPUs.When the

`cufile_stats`

JSON parameter is set to a non-zero value, the cuFile library may crash during program exit if opened or closed through the dl interface. Workaround: Explicitly call`cuFileDriverClose`

API before closing the library.Prior to CUDA 13.1, enabling stats with verbose logging may cause a race condition during shutdown that can trigger a segmentation fault.

The

`nvidia.ko`

kernel P2P interface version has changed to`0x00020000`

starting from NVIDIA driver version`R580.82.05`

. The`nvidia-fs.ko`

module must be rebuilt against the new symbols after the`nvidia.ko`

driver installation. Remove the existing`nvidia-fs-dkms`

driver manually and reinstall the`nvidia-fs.ko`

driver after the`nvidia.ko`

driver installation by running:sudo apt install -y --reinstall nvidia-fs-dkms

For GPFS, in the case of asynchronous I/O, only I/Os that fail with

`-EOPNOTSUPP`

at submission time are retried via the compat path by`libcufile`

. I/Os that fail with this error during execution time are not retried via the compat path.With

`libcufile`

version`1.16.0`

, when`nvidia-fs`

is loaded but the NVMe/NVMeoF driver is not patched for GDS support, I/O operations on block devices may incorrectly attempt to use the GDS path and fail. This issue only affects file descriptors registered after the first one on the same block device. As a workaround, unload the`nvidia-fs`

module when operating on block devices with an unpatched NVMe/NVMeoF driver, for example:modprobe -r nvidia-fs

Due to a change in

`pin_user_pages_fast`

, upstream kernels 6.11 and later, as well as corresponding recent RHEL kernels, exhibit a performance regression for small I/O sizes up to 128 KB. This regression affects both the NVMe`nvidia-fs`

path and the`p2pdma`

path.For large system deployments on Ubuntu 26.04 and later, it is advisable to use static topology in the

`cufile`

configuration to reduce startup time for short-running applications.To retain the previous 16 MiB maximum direct I/O chunk size, set

`max_direct_io_size_kb`

to`16384`

in`cufile.json`

.

# 11. Known Limitations[#](https://docs.nvidia.com#known-limitations)

This section provides information about the known limitations in this release of GDS.

GPUDirect Storage with

`NVME P2PDMA`

feature is not supported with RAID0 and multipath NVMe support.vGPU supports the latest GPUs with OpenRM; that is, GPUs with Ada Lovelace, Hopper and later are supported. A100 and earlier GPUs are not supported with OpenRM.

All OS (BaseOS/RHEL/SLES ) for Grace-Hopper need persistence enabled.

CUDA streams based APIs:

CUDA graphs are not supported with cuFile Stream APIs.

cuFile Stream APIs for GPFS and WekaFS are supported in compatibility mode only.

cuFile Stream APIs are not supported when cuFile configuration parameter

`execution.parallel_io`

is false or`execution.max_io_threads`

is set to 0.`CU_FILE_STREAMS_SUPPORTED`

bit is not set in`Props.fflags`

when queried with`cuFileDriverGetProperties`

.

Available BAR1 memory reported by the

`nvidia-smi`

utility is not accurate due to some internal overhead of the CUDA toolkit. Therefore, a huge allocation of BAR1 memory by any GDS application can run into ENOMEM errors, even when`nvidia-smi`

utility shows there is available BAR1 memory.GPUDirect storage in P2P mode does not support NVMe end-to-end data protection features. To support GDS in p2p mode, the NVMe must be formatted with Protection Information where

`Metadata Size`

is set to zero bytes.CentOS 7.x is no longer supported.

Checksums on the client-side of file systems must be disabled for GDS.

cuFile APIs are not supported with applications that use the

`fork()`

system call.GDS Compatibility mode is only tested on GDS qualified file systems: ext4, EXAScaler, Amazon FSx for Lustre, XFS, WekaFS, IBM Spectrum Scale, VAST, and BeeGFS.

On x86-64 platforms, GDS with “IOMMU=on” or ACS enabled are not guaranteed to work functionally or in a performant way.

Refer to the following documentation for IBM Spectrum Scale Limitations with GDS:

[https://www.ibm.com/docs/en/spectrum-scale/5.1.5?topic=architecture-gpudirect-storage-support-spectrum-scale](https://www.ibm.com/docs/en/spectrum-scale/5.1.5?topic=architecture-gpudirect-storage-support-spectrum-scale)Upgrading of Linux Kernel version and

`nv_peer_mem`

:WekaFS does not support newer MLNX_OFED versions 5.3.x and above with GDS.

`nvidia-peer-memory-dkms=1.1-0-nvidia2`

is required for GDS support with WekaFS. Please follow the instructions in section 2.2 of the*GDS Troubleshooting and Installation Guide*.RHEL 8.3 or later does not have default udev rules for detecting RAID members, which disables GDS on RAID volumes. Refer to the section “Adding udev Rules for RAID Volumes” in

*GDS Installation and Troubleshooting Guide*.Sparse file read performance can be slow with the “NVME P2PDMA” feature.

WekaFS is not supported with CUDA 13.1 because of a regression in file handle parsing. This issue causes GPUDirect Storage read and write operations to fail with

`EBADF`

(`-9`

). If you use WekaFS, upgrade to CUDA 13.3 or later.On DGX Spark, GPUDirect Storage is supported only in compatibility mode. Do not load

`nvidia-fs`

, because doing so can result in errors.On Linux 6.17 and later with

`nvidia-fs`

mode enabled, the NVMe patch has a known issue with drives that support scatter-gather lists (SGLs). When the driver uses the SGL path, I/O failures and kernel-level hangs can occur. As a workaround, use the`p2pdma`

path on these kernels.If you plan to use

`nvidia-fs`

to access local NVMe drives, DOCA version compatibility depends on your Linux kernel version:On Linux kernel 6.17 or newer, DOCA 3.3.0 or newer is required. This guidance may also apply to older kernels on Linux distributions that have backported the iterative block-layer mapping API; check for it by running

`grep -w blk_rq_dma_map_iter_start /proc/kallsyms`

.On Linux kernel 6.16 or older, any DOCA version except 3.3.0 can be used.

If you cannot install a DOCA version that is compatible with your kernel as described above, use the

`p2pdma`

path as a workaround. Refer to the*GDS Installation and Troubleshooting Guide*.


# 12. Notice[#](https://docs.nvidia.com#notice)

This document is provided for information purposes only and shall not be regarded as a warranty of a certain functionality, condition, or quality of a product. NVIDIA Corporation (“NVIDIA”) makes no representations or warranties, expressed or implied, as to the accuracy or completeness of the information contained in this document and assumes no responsibility for any errors contained herein. NVIDIA shall have no liability for the consequences or use of such information or for any infringement of patents or other rights of third parties that may result from its use. This document is not a commitment to develop, release, or deliver any Material (defined below), code, or functionality.

NVIDIA reserves the right to make corrections, modifications, enhancements, improvements, and any other changes to this document, at any time without notice.

Customer should obtain the latest relevant information before placing orders and should verify that such information is current and complete.

NVIDIA products are sold subject to the NVIDIA standard terms and conditions of sale supplied at the time of order acknowledgement, unless otherwise agreed in an individual sales agreement signed by authorized representatives of NVIDIA and customer (“Terms of Sale”). NVIDIA hereby expressly objects to applying any customer general terms and conditions with regards to the purchase of the NVIDIA product referenced in this document. No contractual obligations are formed either directly or indirectly by this document.

NVIDIA products are not designed, authorized, or warranted to be suitable for use in medical, military, aircraft, space, or life support equipment, nor in applications where failure or malfunction of the NVIDIA product can reasonably be expected to result in personal injury, death, or property or environmental damage. NVIDIA accepts no liability for inclusion and/or use of NVIDIA products in such equipment or applications and therefore such inclusion and/or use is at customer’s own risk.

NVIDIA makes no representation or warranty that products based on this document will be suitable for any specified use. Testing of all parameters of each product is not necessarily performed by NVIDIA. It is customer’s sole responsibility to evaluate and determine the applicability of any information contained in this document, ensure the product is suitable and fit for the application planned by customer, and perform the necessary testing for the application in order to avoid a default of the application or the product. Weaknesses in customer’s product designs may affect the quality and reliability of the NVIDIA product and may result in additional or different conditions and/or requirements beyond those contained in this document. NVIDIA accepts no liability related to any default, damage, costs, or problem which may be based on or attributable to: (i) the use of the NVIDIA product in any manner that is contrary to this document or (ii) customer product designs.

No license, either expressed or implied, is granted under any NVIDIA patent right, copyright, or other NVIDIA intellectual property right under this document. Information published by NVIDIA regarding third-party products or services does not constitute a license from NVIDIA to use such products or services or a warranty or endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual property rights of the third party, or a license from NVIDIA under the patents or other intellectual property rights of NVIDIA.

Reproduction of information in this document is permissible only if approved in advance by NVIDIA in writing, reproduced without alteration and in full compliance with all applicable export laws and regulations, and accompanied by all associated conditions, limitations, and notices.

THIS DOCUMENT AND ALL NVIDIA DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESSED, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND EXPRESSLY DISCLAIMS ALL IMPLIED WARRANTIES OF NONINFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A PARTICULAR PURPOSE. TO THE EXTENT NOT PROHIBITED BY LAW, IN NO EVENT WILL NVIDIA BE LIABLE FOR ANY DAMAGES, INCLUDING WITHOUT LIMITATION ANY DIRECT, INDIRECT, SPECIAL, INCIDENTAL, PUNITIVE, OR CONSEQUENTIAL DAMAGES, HOWEVER CAUSED AND REGARDLESS OF THE THEORY OF LIABILITY, ARISING OUT OF ANY USE OF THIS DOCUMENT, EVEN IF NVIDIA HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. Notwithstanding any damages that customer might incur for any reason whatsoever, NVIDIA’s aggregate and cumulative liability towards customer for the products described herein shall be limited in accordance with the Terms of Sale for the product.

# 13. OpenCL[#](https://docs.nvidia.com#opencl)

OpenCL is a trademark of Apple Inc. used under license to the Khronos Group Inc.

# 14. Trademarks[#](https://docs.nvidia.com#trademarks)

NVIDIA, the NVIDIA logo, CUDA, DGX, DGX-1, DGX-2, DGX-A100, Tesla, and Quadro are trademarks and/or registered trademarks of NVIDIA Corporation in the United States and other countries. Other company and product names may be trademarks of the respective companies with which they are associated.