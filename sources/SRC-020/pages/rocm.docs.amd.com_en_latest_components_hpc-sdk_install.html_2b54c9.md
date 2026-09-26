source: https://rocm.docs.amd.com/en/latest/components/hpc-sdk/install.html

# Install ROCm HPC SDK[#](https://rocm.docs.amd.com#install-rocm-hpc-sdk)

AMD ROCm HPC SDK provides high-performance computing libraries and tools for AMD Instinct GPUs. This guide walks you through installing the HPC SDK alongside ROCm installation on a supported Linux distribution.

The ROCm for HPC applications and containers run on a standard ROCm
installation. See the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html#compat-matrix) for details
on supported hardware and operating systems.

The HPC application containers are published through
[AMD InfinityHub-CI](https://github.com/amd/InfinityHub-CI). Each container
provides parameters to specify source code branches and release versions of ROCm,
OpenMPI, UCX, and Ubuntu.

Before installing the HPC SDK, make sure your system meets the ROCm hardware,
software, and driver requirements. For instructions, see [Install AMD ROCm](https://rocm.docs.amd.com/install/rocm.html#rocm-install-selector). Use the
selector panel on that page to view instructions appropriate for your system
environment.

HPC SDK includes [hipTensor](https://github.com/ROCm/rocm-libraries/tree/develop/projects/hiptensor) and [rocALUTION](https://github.com/ROCm/rocm-libraries/tree/develop/projects/rocalution) packaged as part of the installation.

## Install HPC SDK[#](https://rocm.docs.amd.com#install-hpc-sdk)

The standard ROCm tarball installation includes the HPC SDK. No
additional steps are required. For details on ROCm tarball installation,
refer to [Install AMD ROCm 10.0.0](https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html) and
select **Tarball** installation method from installation environment
selector.

[Install ROCm](https://rocm.docs.amd.com/install/rocm.html). Remember to complete the[ROCm installation prerequisites](https://rocm.docs.amd.com/install/rocm.html#rocm-prerequisites)to install dependencies and configure GPU access permissions.

Use the following command to install HPC SDK for all GPU architectures:

sudo apt install amdrocm-hpc10.0 amdrocm-hpc-sdk10.0

sudo dnf install amdrocm-hpc10.0 amdrocm-hpc-sdk10.0

sudo zypper install amdrocm-hpc10.0 amdrocm-hpc-sdk10.0


Use the following command to install HPC SDK for your

`gfx950`

GPU:sudo apt install amdrocm-hpc10.0-gfx950 amdrocm-hpc-sdk10.0-gfx950

sudo dnf install amdrocm-hpc10.0-gfx950 amdrocm-hpc-sdk10.0-gfx950

sudo zypper install amdrocm-hpc10.0-gfx950 amdrocm-hpc-sdk10.0-gfx950


Use the following command to install HPC SDK for your

`gfx942`

GPU:sudo apt install amdrocm-hpc10.0-gfx942 amdrocm-hpc-sdk10.0-gfx942

sudo dnf install amdrocm-hpc10.0-gfx942 amdrocm-hpc-sdk10.0-gfx942

sudo zypper install amdrocm-hpc10.0-gfx942 amdrocm-hpc-sdk10.0-gfx942


Use the following command to install HPC SDK for your

`gfx90a`

GPU:sudo apt install amdrocm-hpc10.0-gfx90a amdrocm-hpc-sdk10.0-gfx90a

sudo dnf install amdrocm-hpc10.0-gfx90a amdrocm-hpc-sdk10.0-gfx90a

sudo zypper install amdrocm-hpc10.0-gfx90a amdrocm-hpc-sdk10.0-gfx90a


Use the following command to install HPC SDK for your

`gfx908`

GPU:sudo apt install amdrocm-hpc10.0-gfx908 amdrocm-hpc-sdk10.0-gfx908

sudo dnf install amdrocm-hpc10.0-gfx908 amdrocm-hpc-sdk10.0-gfx908

sudo zypper install amdrocm-hpc10.0-gfx908 amdrocm-hpc-sdk10.0-gfx908


Use the following command to install HPC SDK for your

`gfx1200`

GPU:sudo apt install amdrocm-hpc10.0-gfx1200 amdrocm-hpc-sdk10.0-gfx1200

sudo dnf install amdrocm-hpc10.0-gfx1200 amdrocm-hpc-sdk10.0-gfx1200

sudo zypper install amdrocm-hpc10.0-gfx1200 amdrocm-hpc-sdk10.0-gfx1200


Use the following command to install HPC SDK for your

`gfx1201`

GPU:sudo apt install amdrocm-hpc10.0-gfx1201 amdrocm-hpc-sdk10.0-gfx1201

sudo dnf install amdrocm-hpc10.0-gfx1201 amdrocm-hpc-sdk10.0-gfx1201

sudo zypper install amdrocm-hpc10.0-gfx1201 amdrocm-hpc-sdk10.0-gfx1201


Use the following command to install HPC SDK for your

`gfx1100`

GPU:sudo apt install amdrocm-hpc10.0-gfx1100 amdrocm-hpc-sdk10.0-gfx1100

sudo dnf install amdrocm-hpc10.0-gfx1100 amdrocm-hpc-sdk10.0-gfx1100

sudo zypper install amdrocm-hpc10.0-gfx1100 amdrocm-hpc-sdk10.0-gfx1100


Use the following command to install HPC SDK for your

`gfx1101`

GPU:sudo apt install amdrocm-hpc10.0-gfx1101 amdrocm-hpc-sdk10.0-gfx1101

sudo dnf install amdrocm-hpc10.0-gfx1101 amdrocm-hpc-sdk10.0-gfx1101

sudo zypper install amdrocm-hpc10.0-gfx1101 amdrocm-hpc-sdk10.0-gfx1101


Use the following command to install HPC SDK for your

`gfx1102`

GPU:sudo apt install amdrocm-hpc10.0-gfx1102 amdrocm-hpc-sdk10.0-gfx1102

sudo dnf install amdrocm-hpc10.0-gfx1102 amdrocm-hpc-sdk10.0-gfx1102

sudo zypper install amdrocm-hpc10.0-gfx1102 amdrocm-hpc-sdk10.0-gfx1102


Use the following command to install HPC SDK for your

`gfx1103`

GPU:sudo apt install amdrocm-hpc10.0-gfx1103 amdrocm-hpc-sdk10.0-gfx1103

sudo dnf install amdrocm-hpc10.0-gfx1103 amdrocm-hpc-sdk10.0-gfx1103

sudo zypper install amdrocm-hpc10.0-gfx1103 amdrocm-hpc-sdk10.0-gfx1103


Use the following command to install HPC SDK for your

`gfx1030`

GPU:sudo apt install amdrocm-hpc10.0-gfx1030 amdrocm-hpc-sdk10.0-gfx1030

sudo dnf install amdrocm-hpc10.0-gfx1030 amdrocm-hpc-sdk10.0-gfx1030

sudo zypper install amdrocm-hpc10.0-gfx1030 amdrocm-hpc-sdk10.0-gfx1030


Use the following command to install HPC SDK for your

`gfx1151`

GPU:sudo apt install amdrocm-hpc10.0-gfx1151 amdrocm-hpc-sdk10.0-gfx1151

sudo dnf install amdrocm-hpc10.0-gfx1151 amdrocm-hpc-sdk10.0-gfx1151

sudo zypper install amdrocm-hpc10.0-gfx1151 amdrocm-hpc-sdk10.0-gfx1151


Use the following command to install HPC SDK for your

`gfx1150`

GPU:sudo apt install amdrocm-hpc10.0-gfx1150 amdrocm-hpc-sdk10.0-gfx1150

sudo dnf install amdrocm-hpc10.0-gfx1150 amdrocm-hpc-sdk10.0-gfx1150

sudo zypper install amdrocm-hpc10.0-gfx1150 amdrocm-hpc-sdk10.0-gfx1150


Use the following command to install HPC SDK for your

`gfx1152`

GPU:sudo apt install amdrocm-hpc10.0-gfx1152 amdrocm-hpc-sdk10.0-gfx1152

sudo dnf install amdrocm-hpc10.0-gfx1152 amdrocm-hpc-sdk10.0-gfx1152

sudo zypper install amdrocm-hpc10.0-gfx1152 amdrocm-hpc-sdk10.0-gfx1152


Use the following command to install HPC SDK for your

`gfx1153`

GPU:sudo apt install amdrocm-hpc10.0-gfx1153 amdrocm-hpc-sdk10.0-gfx1153

sudo dnf install amdrocm-hpc10.0-gfx1153 amdrocm-hpc-sdk10.0-gfx1153

sudo zypper install amdrocm-hpc10.0-gfx1153 amdrocm-hpc-sdk10.0-gfx1153


The standard ROCm tarball installation includes the HPC SDK. No
additional steps are required. For details on ROCm tarball installation,
refer to [Install AMD ROCm 7.14.0](https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html) and
select **Tarball** installation method from installation environment
selector.

[Install ROCm](https://rocm.docs.amd.com/install/rocm.html). Remember to complete the[ROCm installation prerequisites](https://rocm.docs.amd.com/install/rocm.html#rocm-prerequisites)to install dependencies and configure GPU access permissions.

Use the following command to install HPC SDK for all GPU architectures:

sudo apt install amdrocm-hpc7.14 amdrocm-hpc-sdk7.14

sudo dnf install amdrocm-hpc7.14 amdrocm-hpc-sdk7.14

sudo zypper install amdrocm-hpc7.14 amdrocm-hpc-sdk7.14


Use the following command to install HPC SDK for your

`gfx950`

GPU:sudo apt install amdrocm-hpc7.14-gfx950 amdrocm-hpc-sdk7.14-gfx950

sudo dnf install amdrocm-hpc7.14-gfx950 amdrocm-hpc-sdk7.14-gfx950

sudo zypper install amdrocm-hpc7.14-gfx950 amdrocm-hpc-sdk7.14-gfx950


Use the following command to install HPC SDK for your

`gfx942`

GPU:sudo apt install amdrocm-hpc7.14-gfx942 amdrocm-hpc-sdk7.14-gfx942

sudo dnf install amdrocm-hpc7.14-gfx942 amdrocm-hpc-sdk7.14-gfx942

sudo zypper install amdrocm-hpc7.14-gfx942 amdrocm-hpc-sdk7.14-gfx942


Use the following command to install HPC SDK for your

`gfx90a`

GPU:sudo apt install amdrocm-hpc7.14-gfx90a amdrocm-hpc-sdk7.14-gfx90a

sudo dnf install amdrocm-hpc7.14-gfx90a amdrocm-hpc-sdk7.14-gfx90a

sudo zypper install amdrocm-hpc7.14-gfx90a amdrocm-hpc-sdk7.14-gfx90a


Use the following command to install HPC SDK for your

`gfx908`

GPU:sudo apt install amdrocm-hpc7.14-gfx908 amdrocm-hpc-sdk7.14-gfx908

sudo dnf install amdrocm-hpc7.14-gfx908 amdrocm-hpc-sdk7.14-gfx908

sudo zypper install amdrocm-hpc7.14-gfx908 amdrocm-hpc-sdk7.14-gfx908


Use the following command to install HPC SDK for your

`gfx1200`

GPU:sudo apt install amdrocm-hpc7.14-gfx1200 amdrocm-hpc-sdk7.14-gfx1200

sudo dnf install amdrocm-hpc7.14-gfx1200 amdrocm-hpc-sdk7.14-gfx1200

sudo zypper install amdrocm-hpc7.14-gfx1200 amdrocm-hpc-sdk7.14-gfx1200


Use the following command to install HPC SDK for your

`gfx1201`

GPU:sudo apt install amdrocm-hpc7.14-gfx1201 amdrocm-hpc-sdk7.14-gfx1201

sudo dnf install amdrocm-hpc7.14-gfx1201 amdrocm-hpc-sdk7.14-gfx1201

sudo zypper install amdrocm-hpc7.14-gfx1201 amdrocm-hpc-sdk7.14-gfx1201


Use the following command to install HPC SDK for your

`gfx1100`

GPU:sudo apt install amdrocm-hpc7.14-gfx1100 amdrocm-hpc-sdk7.14-gfx1100

sudo dnf install amdrocm-hpc7.14-gfx1100 amdrocm-hpc-sdk7.14-gfx1100

sudo zypper install amdrocm-hpc7.14-gfx1100 amdrocm-hpc-sdk7.14-gfx1100


Use the following command to install HPC SDK for your

`gfx1101`

GPU:sudo apt install amdrocm-hpc7.14-gfx1101 amdrocm-hpc-sdk7.14-gfx1101

sudo dnf install amdrocm-hpc7.14-gfx1101 amdrocm-hpc-sdk7.14-gfx1101

sudo zypper install amdrocm-hpc7.14-gfx1101 amdrocm-hpc-sdk7.14-gfx1101


Use the following command to install HPC SDK for your

`gfx1102`

GPU:sudo apt install amdrocm-hpc7.14-gfx1102 amdrocm-hpc-sdk7.14-gfx1102

sudo dnf install amdrocm-hpc7.14-gfx1102 amdrocm-hpc-sdk7.14-gfx1102

sudo zypper install amdrocm-hpc7.14-gfx1102 amdrocm-hpc-sdk7.14-gfx1102


Use the following command to install HPC SDK for your

`gfx1103`

GPU:sudo apt install amdrocm-hpc7.14-gfx1103 amdrocm-hpc-sdk7.14-gfx1103

sudo dnf install amdrocm-hpc7.14-gfx1103 amdrocm-hpc-sdk7.14-gfx1103

sudo zypper install amdrocm-hpc7.14-gfx1103 amdrocm-hpc-sdk7.14-gfx1103


Use the following command to install HPC SDK for your

`gfx1030`

GPU:sudo apt install amdrocm-hpc7.14-gfx1030 amdrocm-hpc-sdk7.14-gfx1030

sudo dnf install amdrocm-hpc7.14-gfx1030 amdrocm-hpc-sdk7.14-gfx1030

sudo zypper install amdrocm-hpc7.14-gfx1030 amdrocm-hpc-sdk7.14-gfx1030


Use the following command to install HPC SDK for your

`gfx1151`

GPU:sudo apt install amdrocm-hpc7.14-gfx1151 amdrocm-hpc-sdk7.14-gfx1151

sudo dnf install amdrocm-hpc7.14-gfx1151 amdrocm-hpc-sdk7.14-gfx1151

sudo zypper install amdrocm-hpc7.14-gfx1151 amdrocm-hpc-sdk7.14-gfx1151


Use the following command to install HPC SDK for your

`gfx1150`

GPU:sudo apt install amdrocm-hpc7.14-gfx1150 amdrocm-hpc-sdk7.14-gfx1150

sudo dnf install amdrocm-hpc7.14-gfx1150 amdrocm-hpc-sdk7.14-gfx1150

sudo zypper install amdrocm-hpc7.14-gfx1150 amdrocm-hpc-sdk7.14-gfx1150


Use the following command to install HPC SDK for your

`gfx1152`

GPU:sudo apt install amdrocm-hpc7.14-gfx1152 amdrocm-hpc-sdk7.14-gfx1152

sudo dnf install amdrocm-hpc7.14-gfx1152 amdrocm-hpc-sdk7.14-gfx1152

sudo zypper install amdrocm-hpc7.14-gfx1152 amdrocm-hpc-sdk7.14-gfx1152


Use the following command to install HPC SDK for your

`gfx1153`

GPU:sudo apt install amdrocm-hpc7.14-gfx1153 amdrocm-hpc-sdk7.14-gfx1153

sudo dnf install amdrocm-hpc7.14-gfx1153 amdrocm-hpc-sdk7.14-gfx1153

sudo zypper install amdrocm-hpc7.14-gfx1153 amdrocm-hpc-sdk7.14-gfx1153


## Uninstall HPC SDK[#](https://rocm.docs.amd.com#uninstall-hpc-sdk)

The standard ROCm uninstallation process can be followed to uninstall HPC
SDK. No additional steps are required to remove the HPC SDK separately.
Refer to [Uninstalling ROCm 10.0.0](https://rocm.docs.amd.com/en/docs-10.0.0/install/rocm.html#uninstalling)
section and select **Tarball** from the installation environment
selector.

Use the following command to uninstall HPC SDK for all GPU architectures:

```
sudo apt autoremove amdrocm-hpc10.0 amdrocm-hpc-sdk10.0
```

```
sudo dnf remove amdrocm-hpc10.0 amdrocm-hpc-sdk10.0
```

```
sudo zypper remove amdrocm-hpc10.0 amdrocm-hpc-sdk10.0
```

Use the following command to uninstall HPC SDK for your `gfx950`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx950 amdrocm-hpc-sdk10.0-gfx950
```

```
sudo dnf remove amdrocm-hpc10.0-gfx950 amdrocm-hpc-sdk10.0-gfx950
```

```
sudo zypper remove amdrocm-hpc10.0-gfx950 amdrocm-hpc-sdk10.0-gfx950
```

Use the following command to uninstall HPC SDK for your `gfx942`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx942 amdrocm-hpc-sdk10.0-gfx942
```

```
sudo dnf remove amdrocm-hpc10.0-gfx942 amdrocm-hpc-sdk10.0-gfx942
```

```
sudo zypper remove amdrocm-hpc10.0-gfx942 amdrocm-hpc-sdk10.0-gfx942
```

Use the following command to uninstall HPC SDK for your `gfx90a`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx90a amdrocm-hpc-sdk10.0-gfx90a
```

```
sudo dnf remove amdrocm-hpc10.0-gfx90a amdrocm-hpc-sdk10.0-gfx90a
```

```
sudo zypper remove amdrocm-hpc10.0-gfx90a amdrocm-hpc-sdk10.0-gfx90a
```

Use the following command to uninstall HPC SDK for your `gfx908`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx908 amdrocm-hpc-sdk10.0-gfx908
```

```
sudo dnf remove amdrocm-hpc10.0-gfx908 amdrocm-hpc-sdk10.0-gfx908
```

```
sudo zypper remove amdrocm-hpc10.0-gfx908 amdrocm-hpc-sdk10.0-gfx908
```

Use the following command to uninstall HPC SDK for your `gfx1200`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1200 amdrocm-hpc-sdk10.0-gfx1200
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1200 amdrocm-hpc-sdk10.0-gfx1200
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1200 amdrocm-hpc-sdk10.0-gfx1200
```

Use the following command to uninstall HPC SDK for your `gfx1201`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1201 amdrocm-hpc-sdk10.0-gfx1201
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1201 amdrocm-hpc-sdk10.0-gfx1201
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1201 amdrocm-hpc-sdk10.0-gfx1201
```

Use the following command to uninstall HPC SDK for your `gfx1100`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1100 amdrocm-hpc-sdk10.0-gfx1100
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1100 amdrocm-hpc-sdk10.0-gfx1100
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1100 amdrocm-hpc-sdk10.0-gfx1100
```

Use the following command to uninstall HPC SDK for your `gfx1101`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1101 amdrocm-hpc-sdk10.0-gfx1101
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1101 amdrocm-hpc-sdk10.0-gfx1101
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1101 amdrocm-hpc-sdk10.0-gfx1101
```

Use the following command to uninstall HPC SDK for your `gfx1102`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1102 amdrocm-hpc-sdk10.0-gfx1102
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1102 amdrocm-hpc-sdk10.0-gfx1102
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1102 amdrocm-hpc-sdk10.0-gfx1102
```

Use the following command to uninstall HPC SDK for your `gfx1103`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1103 amdrocm-hpc-sdk10.0-gfx1103
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1103 amdrocm-hpc-sdk10.0-gfx1103
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1103 amdrocm-hpc-sdk10.0-gfx1103
```

Use the following command to uninstall HPC SDK for your `gfx1030`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1030 amdrocm-hpc-sdk10.0-gfx1030
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1030 amdrocm-hpc-sdk10.0-gfx1030
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1030 amdrocm-hpc-sdk10.0-gfx1030
```

Use the following command to uninstall HPC SDK for your `gfx1151`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1151 amdrocm-hpc-sdk10.0-gfx1151
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1151 amdrocm-hpc-sdk10.0-gfx1151
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1151 amdrocm-hpc-sdk10.0-gfx1151
```

Use the following command to uninstall HPC SDK for your `gfx1150`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1150 amdrocm-hpc-sdk10.0-gfx1150
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1150 amdrocm-hpc-sdk10.0-gfx1150
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1150 amdrocm-hpc-sdk10.0-gfx1150
```

Use the following command to uninstall HPC SDK for your `gfx1152`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1152 amdrocm-hpc-sdk10.0-gfx1152
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1152 amdrocm-hpc-sdk10.0-gfx1152
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1152 amdrocm-hpc-sdk10.0-gfx1152
```

Use the following command to uninstall HPC SDK for your `gfx1153`

GPU:

```
sudo apt autoremove amdrocm-hpc10.0-gfx1153 amdrocm-hpc-sdk10.0-gfx1153
```

```
sudo dnf remove amdrocm-hpc10.0-gfx1153 amdrocm-hpc-sdk10.0-gfx1153
```

```
sudo zypper remove amdrocm-hpc10.0-gfx1153 amdrocm-hpc-sdk10.0-gfx1153
```

The standard ROCm uninstallation process can be followed to uninstall HPC
SDK. No additional steps are required to remove the HPC SDK separately.
Refer to [Uninstalling ROCm 7.14.0](https://rocm.docs.amd.com/en/docs-7.14.0/install/rocm.html#uninstalling)
section and select **Tarball** from the installation environment
selector.

Use the following command to uninstall HPC SDK for all GPU architectures:

```
sudo apt autoremove amdrocm-hpc7.14 amdrocm-hpc-sdk7.14
```

```
sudo dnf remove amdrocm-hpc7.14 amdrocm-hpc-sdk7.14
```

```
sudo zypper remove amdrocm-hpc7.14 amdrocm-hpc-sdk7.14
```

Use the following command to uninstall HPC SDK for your `gfx950`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx950 amdrocm-hpc-sdk7.14-gfx950
```

```
sudo dnf remove amdrocm-hpc7.14-gfx950 amdrocm-hpc-sdk7.14-gfx950
```

```
sudo zypper remove amdrocm-hpc7.14-gfx950 amdrocm-hpc-sdk7.14-gfx950
```

Use the following command to uninstall HPC SDK for your `gfx942`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx942 amdrocm-hpc-sdk7.14-gfx942
```

```
sudo dnf remove amdrocm-hpc7.14-gfx942 amdrocm-hpc-sdk7.14-gfx942
```

```
sudo zypper remove amdrocm-hpc7.14-gfx942 amdrocm-hpc-sdk7.14-gfx942
```

Use the following command to uninstall HPC SDK for your `gfx90a`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx90a amdrocm-hpc-sdk7.14-gfx90a
```

```
sudo dnf remove amdrocm-hpc7.14-gfx90a amdrocm-hpc-sdk7.14-gfx90a
```

```
sudo zypper remove amdrocm-hpc7.14-gfx90a amdrocm-hpc-sdk7.14-gfx90a
```

Use the following command to uninstall HPC SDK for your `gfx908`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx908 amdrocm-hpc-sdk7.14-gfx908
```

```
sudo dnf remove amdrocm-hpc7.14-gfx908 amdrocm-hpc-sdk7.14-gfx908
```

```
sudo zypper remove amdrocm-hpc7.14-gfx908 amdrocm-hpc-sdk7.14-gfx908
```

Use the following command to uninstall HPC SDK for your `gfx1200`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1200 amdrocm-hpc-sdk7.14-gfx1200
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1200 amdrocm-hpc-sdk7.14-gfx1200
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1200 amdrocm-hpc-sdk7.14-gfx1200
```

Use the following command to uninstall HPC SDK for your `gfx1201`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1201 amdrocm-hpc-sdk7.14-gfx1201
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1201 amdrocm-hpc-sdk7.14-gfx1201
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1201 amdrocm-hpc-sdk7.14-gfx1201
```

Use the following command to uninstall HPC SDK for your `gfx1100`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1100 amdrocm-hpc-sdk7.14-gfx1100
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1100 amdrocm-hpc-sdk7.14-gfx1100
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1100 amdrocm-hpc-sdk7.14-gfx1100
```

Use the following command to uninstall HPC SDK for your `gfx1101`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1101 amdrocm-hpc-sdk7.14-gfx1101
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1101 amdrocm-hpc-sdk7.14-gfx1101
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1101 amdrocm-hpc-sdk7.14-gfx1101
```

Use the following command to uninstall HPC SDK for your `gfx1102`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1102 amdrocm-hpc-sdk7.14-gfx1102
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1102 amdrocm-hpc-sdk7.14-gfx1102
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1102 amdrocm-hpc-sdk7.14-gfx1102
```

Use the following command to uninstall HPC SDK for your `gfx1103`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1103 amdrocm-hpc-sdk7.14-gfx1103
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1103 amdrocm-hpc-sdk7.14-gfx1103
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1103 amdrocm-hpc-sdk7.14-gfx1103
```

Use the following command to uninstall HPC SDK for your `gfx1030`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1030 amdrocm-hpc-sdk7.14-gfx1030
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1030 amdrocm-hpc-sdk7.14-gfx1030
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1030 amdrocm-hpc-sdk7.14-gfx1030
```

Use the following command to uninstall HPC SDK for your `gfx1151`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1151 amdrocm-hpc-sdk7.14-gfx1151
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1151 amdrocm-hpc-sdk7.14-gfx1151
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1151 amdrocm-hpc-sdk7.14-gfx1151
```

Use the following command to uninstall HPC SDK for your `gfx1150`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1150 amdrocm-hpc-sdk7.14-gfx1150
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1150 amdrocm-hpc-sdk7.14-gfx1150
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1150 amdrocm-hpc-sdk7.14-gfx1150
```

Use the following command to uninstall HPC SDK for your `gfx1152`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1152 amdrocm-hpc-sdk7.14-gfx1152
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1152 amdrocm-hpc-sdk7.14-gfx1152
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1152 amdrocm-hpc-sdk7.14-gfx1152
```

Use the following command to uninstall HPC SDK for your `gfx1153`

GPU:

```
sudo apt autoremove amdrocm-hpc7.14-gfx1153 amdrocm-hpc-sdk7.14-gfx1153
```

```
sudo dnf remove amdrocm-hpc7.14-gfx1153 amdrocm-hpc-sdk7.14-gfx1153
```

```
sudo zypper remove amdrocm-hpc7.14-gfx1153 amdrocm-hpc-sdk7.14-gfx1153
```