source: https://docs.nvidia.com/deploy/cuda-compatibility/forward-compatibility.html

# Forward Compatibility[#](https://docs.nvidia.com#forward-compatibility)

## Forward Compatibility Support Across Major Toolkit Versions[#](https://docs.nvidia.com#forward-compatibility-support-across-major-toolkit-versions)

Increasingly, data centers and enterprises may not want to update the NVIDIA GPU Driver across major release versions due to the rigorous testing and validation that happens before any system level driver installations are done.

To support such scenarios, CUDA introduced a Forward Compatibility Upgrade path in CUDA 10.0.

Warning

Forward Compatibility is applicable only for systems with:

NVIDIA Data Center GPUs.

Select

[NGC Server Ready](https://docs.nvidia.com/certification-programs/ngc-ready-systems/index.html)SKUs of RTX cards.Jetson boards.


It’s mainly intended to support applications built on newer CUDA Toolkits to run on systems installed with an older NVIDIA Linux GPU driver from different major release families. This new forward-compatible upgrade path requires the use of a special package called “CUDA Comaptibility Package”.

## Installing the CUDA Forward Compatibility Package[#](https://docs.nvidia.com#installing-the-cuda-forward-compatibility-package)

### From Network Repositories or Local Installers[#](https://docs.nvidia.com#from-network-repositories-or-local-installers)

The CUDA forward compatibility package is available in the local installers or the CUDA network repositories provided by NVIDIA as `cuda-compat-<cuda_major_version>-<cuda_minor_version>`

.

Each NVIDIA driver is built with an accompanying CUDA supported release; and this package is generated from the NVIDIA driver that matches with the CUDA release for which the compatibility is requested. For example, the `cuda-compat-13-4`

package is built using the NVIDIA driver libraries version 615.

Install the package on the system using the package installer.

**Ubuntu / Debian:**

```
# apt install cuda-compat-13-4
```

**Red Hat Enterprise Linux / Rocky Linux / Oracle Linux / Amazon Linux / Fedora / KylinOS:**

```
# dnf install cuda-compat-13-4
```

**SLES / OpenSUSE:**

```
# zypper install cuda-compat-13-4
```

**Azure Linux:**

```
# tdnf install cuda-compat-13-4
```

The CUDA forward compatibility package will then be installed to the versioned toolkit directory. For example, for the CUDA forward compatibility package of 13.4, the GPU driver libraries of 615 will be installed in `/usr/local/cuda-13.4/compat/`

.

The `cuda-compat-<cuda_major_version>-<cuda_minor_version>`

package consists of the following files:

`libcuda.so.*`

- CUDA driver`libcudadebugger.so.*`

- GPU debugging support for CUDA Driver (CUDA 11.8 and later only)`libnvidia-gpucomp.so.*`

- GPU compiler component shared by the CUDA driver compilers (CUDA 13.4 and later only)`libnvidia-nvvm*.so.*`

- JIT LTO (CUDA 11.5 and later only)`libnvidia-ptxjitcompiler.so.*`

- JIT compiler for PTX files`libnvidia-tileiras.so.*`

- CUDA Tile IR assembler (CUDA 13.4 and later only)`libnvidia-pkcs11*.so.*`

- OpenSSL support for CUDA driver`doc/cuda-compat-13-4/copyright`

- License information`doc/cuda-compat-13-4/changelog.Debian.gz`

- Package changelog (Debian-based systems)

Note

This package only provides the libraries, and does not configure the system to find such libraries.

#### Example installation and configuration[#](https://docs.nvidia.com#example-installation-and-configuration)

In this example, the user sets `LD_LIBRARY_PATH`

to include the files installed by the `cuda-compat-13-4`

package on an Ubuntu system.

Install the package:

```
# apt install -y cuda-compat-13-4
Selecting previously unselected package cuda-compat-13-4.
(Reading database ... 339974 files and directories currently installed.)
Preparing to unpack .../cuda-compat-13-4_615.31-1ubuntu1_amd64.deb ...
Unpacking cuda-compat-13-4 (615.31-1ubuntu1) ...
Setting up cuda-compat-13-4 (615.31-1ubuntu1) ...
Processing triggers for libc-bin (2.31-0ubuntu9.2) ...
```

Check the files installed under `/usr/local/cuda-13.4/compat`

:

```
$ ls -1 /usr/local/cuda-13.4/compat
libcuda.so.615.31
libcudadebugger.so.615.31
libnvidia-gpucomp.so.615.31
libnvidia-nvvm.so.615.31
libnvidia-nvvm70.so.4
libnvidia-ptxjitcompiler.so.615.31
libnvidia-tileiras.so.615.31
libnvidia-pkcs11-openssl3.so.615.31
```

The user can set `LD_LIBRARY_PATH`

to include the files installed before running the CUDA 13.4 application:

```
$ export LD_LIBRARY_PATH=/usr/local/cuda-13.4/compat
$ samples/bin/x86_64/linux/release/deviceQuery
samples/bin/x86_64/linux/release/deviceQuery Starting...
CUDA Device Query (Runtime API) version (CUDART static linking)
Detected 1 CUDA Capable device(s)
Device 0: "Tesla T4"
CUDA Driver Version / Runtime Version 13.4 / 13.4
CUDA Capability Major/Minor version number: 7.5
[...]
deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 13.4, CUDA Runtime Version = 13.4, NumDevs = 1
Result = PASS
```

### Manually Installing from Runfile[#](https://docs.nvidia.com#manually-installing-from-runfile)

The CUDA forward compatibility package files can also be extracted from the appropriate datacenter driver ‘runfile’ installers (`.run`

) available in NVIDIA driver downloads. To do this:

Download the latest NVIDIA Data Center GPU driver, and extract the

`.run`

file using option`-x`

.Copy the CUDA libraries, listed at the start of this section, into a user or

`root`

created directory.Follow your system’s guidelines for making sure that the system linker picks up the new libraries.


## Deployment Considerations for Forward Compatibility[#](https://docs.nvidia.com#deployment-considerations-for-forward-compatibility)

### Use the Right CUDA Forward Compatibility Package[#](https://docs.nvidia.com#use-the-right-cuda-forward-compatibility-package)

The CUDA forward compatibility package should be used only in the following situations when forward compatibility is required across major releases.

The CUDA forward compatibility package is named after the highest toolkit that it can support. If you are on the 535 driver but require 12.5 application support, please install the CUDA compatibility package for 12.5.

Note

When performing a full system upgrade, when choosing to install both the toolkit and the driver, remove any forward compatible packages present in the system.

For example, if you are upgrading the driver to 525.60.13 which is the minimum required driver version for the 12.x toolkits, then the CUDA compatibility package is not required in most cases. 11.x and 12.x applications will be supported due to backward compatibility and future 12.x applications will be supported due to minor-version compatibility.

But there are feature restrictions that may make this option less desirable for your scenario - for example: Applications requiring PTX JIT compilation support. Unlike the minor-version compatibility that is defined between CUDA runtime and CUDA driver, forward compatibility is defined between the kernel driver and the CUDA driver, and hence such restrictions do not apply. In order to circumvent the limitation, a forward compatibility package may be used in such scenarios as well.

CUDA forward compatibility package |
NVIDIA driver |
||||||
|---|---|---|---|---|---|---|---|
535+ (CUDA 12.2) |
570+ (CUDA 12.8) |
580+ (CUDA 13.0) |
590+ (CUDA 13.1) |
595+ (CUDA 13.2) |
610+ (CUDA 13.3) |
615+ (CUDA 13.4) |
|
cuda-compat-13-4 |
C |
C |
C |
C |
C |
C |
N/A |
cuda-compat-13-3 |
C |
C |
C |
C |
C |
N/A |
X |
cuda-compat-13-2 |
C |
C |
C |
C |
N/A |
X |
X |
cuda-compat-13-1 |
C |
C |
C |
N/A |
X |
X |
X |
cuda-compat-13-0 |
C |
C |
N/A |
X |
X |
X |
X |
cuda-compat-12-9 |
C |
C |
X |
X |
X |
X |
X |
cuda-compat-12-8 |
C |
N/A |
X |
X |
X |
X |
X |
cuda-compat-12-6 |
C |
X |
X |
X |
X |
X |
X |
cuda-compat-12-5 |
C |
X |
X |
X |
X |
X |
X |
cuda-compat-12-4 |
C |
X |
X |
X |
X |
X |
X |
cuda-compat-12-3 |
C |
X |
X |
X |
X |
X |
X |
cuda-compat-12-2 |
N/A |
X |
X |
X |
X |
X |
X |

C - Compatible

X - Not compatible

Branches not listed in the table above are end of life and are not supported targets for compatibility.

New Feature Branches are not supported targets for CUDA Forward Compatibility.


Examples of how to read this table:

The CUDA 12.4 forward compatibility package is compatible (C) with driver versions 535. It is not applicatble (N/A) for 550, as 12.4 was paired with 550 and therefore no extra packages are needed.

The CUDA 12.3 forward compatibility package is not-compatible (X) with driver version 550 as it was released prior to the driver. Binaries created in 12.3 are still subject to the backwards compatibility guarantees described in this document.

Please note that this table is in reference to use for the compatibility libraries only. A line indicating “X” does not mean that backward or minor version compatibility do not apply to this release. It means that NVIDIA does not provide a compatibility package for this combination.


### Feature Exceptions[#](https://docs.nvidia.com#feature-exceptions)

There are specific features in the CUDA driver that require kernel-mode support and will only work with a newer kernel mode driver. A few features depend on other user-mode components and are therefore also unsupported.

CUDA forward compatibility package |
CUDA - OpenGL/Vulkan Interop |
cuMemMap* set of functionalities |
|---|---|---|
System Base Installation: >= r580 Driver |
||
cuda-compat-13-x |
No |
Yes [1] |
System Base Installation: >= r525 Driver |
||
cuda-compat-12-x |
No |
Yes [1] |
System Base Installation: >= r450 Driver |
||
cuda-compat-11-x |
No |
Yes [1] |

[1] This relies on `CU_DEVICE_ATTRIBUTE_HANDLE_TYPE_POSIX_FILE_DESCRIPTOR_SUPPORTED`

and `CU_DEVICE_ATTRIBUTE_VIRTUAL_ADDRESS_MANAGEMENT_SUPPORTED`

, which should be queried if you intend to use the full range of this functionality.

[2] Supported on Red Hat Enterprise Linux operating system version 8.1 or higher.

### Check for Compatibility Support[#](https://docs.nvidia.com#check-for-compatibility-support)

In addition to the CUDA driver and certain compiler components, there are other drivers in the system installation stack (for example, OpenCL) that remain on the old version. The forward-compatible upgrade path is for CUDA only.

A well-written application should use following error codes to determine if a CUDA Forward Compatible Upgrade is supported. System administrators should be aware of these error codes to determine if there are errors in the deployment.

`CUDA_ERROR_SYSTEM_DRIVER_MISMATCH = 803`

. This error indicates that there is a mismatch between the versions of the display driver and the CUDA driver.`CUDA_ERROR_COMPAT_NOT_SUPPORTED_ON_DEVICE = 804`

. This error indicates that the system was upgraded to run with forward compatibility but the visible hardware detected by CUDA does not support this configuration.

## Deployment Model for Forward Compatibility[#](https://docs.nvidia.com#deployment-model-for-forward-compatibility)

There are two models of deployment for the CUDA compatibility package. We recommend the use of the ‘shared’ deployment mode.

Shared deployment: Allows sharing the same CUDA compatibility package across installed toolkits in the system. Download and extract the latest forward compatibility package with the highest toolkit version in its name. Set the

`LD_LIBRARY_PATH`

variable or through an automatic loader (for example,`ld.so.conf`

), point to that package. This is the most recommended choice.The user can set

`LD_LIBRARY_PATH`

to include the files installed before running the CUDA application:$ LD_LIBRARY_PATH=/usr/local/cuda-13.4/compat

Per-application deployment: Individual applications can choose a package of their choice and place it as part of the Modules system tied to the toolkit and the libraries. Using the Modules system, the admin, or the user, can set up ‘module’ scripts for each version of each toolkit package, and then load the module script for the toolkit as needed.

$ module load cuda/11.0

There is an important consideration to the per-application deployment approach: older forward compatibility packages are not supported on new driver versions. Therefore the module load scripts should proactively query the system for whether the compatibility package can be used before loading the files. This is especially critical if there was a full system upgrade. In the cases where the module script cannot use CUDA compatible upgrade, a fallback path to the default system’s installed CUDA driver can provide a more consistent experience and this can be achieved using

`RPATH`

.