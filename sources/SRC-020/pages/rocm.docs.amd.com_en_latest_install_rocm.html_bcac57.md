source: https://rocm.docs.amd.com/en/latest/install/rocm.html

# Install AMD ROCm 10.0.0[#](https://rocm.docs.amd.com#install-amd-rocm-rocm-version)

## Compare installation methods

ROCm offers five installation methods. If you’re unsure, start with package manager on Linux or tarball on Windows.

Install method |
Platform |
Best for |
Install scope |
|---|---|---|---|
Package manager (apt/dnf/zypper) |
|
|
|
amdgpu-install |
|
|
|
pip |
|
|
|
Tarball |
|
|
|
Runfile |
|
|
|

Use the following selector to choose your installation method for your
supported AMD GPU or APU and operating system. For system requirements and
support information, see the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html). To learn more about changes introduced
in ROCm 10.0.0, see the [Release notes](https://rocm.docs.amd.com/about/release-notes.html).

Note

If your GPU is not listed, it might be community-enabled through TheRock
nightly builds. For more information, see [TheRock supported GPUs](https://github.com/ROCm/TheRock/blob/main/SUPPORTED_GPUS.md). For
installation guidance, see [TheRock releases](https://github.com/ROCm/TheRock/blob/main/RELEASES.md).

This installation method uses Ubuntu’s native package manager `apt`

to install ROCm. This method suits standard system-wide installations
where ROCm packages should be tracked, updated, and removed through
system package workflows.

This installation method uses Debian’s native package manager `apt`

to install ROCm. This method suits standard system-wide installations
where ROCm packages should be tracked, updated, and removed through
system package workflows.

This installation method uses RHEL’s native package manager `dnf`

to
install ROCm. This method suits standard system-wide installations where
ROCm packages should be tracked, updated, and removed through system
package workflows.

This installation method uses Oracle Linux’s native package manager
`dnf`

to install ROCm. This method suits standard system-wide
installations where ROCm packages should be tracked, updated, and removed
through system package workflows.

This installation method uses Rocky Linux’s native package manager
`dnf`

to install ROCm. This method suits standard system-wide
installations where ROCm packages should be tracked, updated, and removed
through system package workflows.

This installation method uses SLES’s native package manager `zypper`

to install ROCm. This method suits standard system-wide installations
where ROCm packages should be tracked, updated, and removed through
system package workflows.

The pip installation method provides ROCm components as Python wheel packages in a virtual environment. This method suits Python-focused development workflows that use an isolated, per-project ROCm environment managed with standard Python packaging tools.

The tarball installation method provides ROCm as a self-contained installation from a pre-built archive. This method suits controlled or restricted environments requiring manual placement, updates, and removal outside the system package manager.

The ROCm Runfile Installer can install ROCm and/or the AMD GPU Driver (amdgpu) without using a native Linux package management system, making it ideal for systems with policy constraints or restricted environments. Network access is not needed for install as long as dependencies for ROCm and/or AMD GPU driver (amdgpu) are met. A single installer supports all GFX architectures, automates post-installation configuration, and offers an interactive command line TUI for guided setup.

Note

For detailed installation options and configuration, see
[ROCm Runfile Installer](https://rocm.docs.amd.com/rocm-runfile-installer.html).

Use the `amdgpu-install`

script to install ROCm, the AMD GPU driver,
graphics components, and other packages. It simplifies installation by
automating GPU-specific and distro-specific package selection. The script
also runs post-installation checks and installs an uninstallation script,
allowing you to remove the entire ROCm stack with a single command.

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

Before installing ROCm 10.0.0, ensure your system meets
all prerequisites. This includes installing the required dependencies and
configuring permissions for GPU access. To confirm that your system is
supported, see the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html).

Before installing ROCm 10.0.0, ensure your system meets
all prerequisites. This includes installing the required dependencies.
To confirm that your system is supported, see the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html).

Before installing ROCm 10.0.0, ensure your system meets
all prerequisites. To confirm that your system is supported, see the
[Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html).

## Install essential packages for Docker containers

Docker images often include only a minimal set of installations, so some essential packages might be missing. When installing ROCm within a Docker container, you might need to install additional packages for a successful installation.

If applicable, run the following command to install essential packages:

```
apt update
apt install sudo wget gpg perl
```

```
apt update
apt install sudo cmake libgfortran5 perl
```

```
apt update
apt install sudo wget python3 perl
```

```
apt update
apt install sudo wget curl python3 rsync perl
```

```
dnf install sudo wget perl
```

```
dnf install sudo wget perl python3
```

```
dnf install sudo wget perl
```

```
dnf install sudo wget perl python3
```

```
dnf install sudo wget perl
```

```
dnf install sudo wget perl
```

```
dnf install sudo wget rsync perl
```

```
zypper install sudo wget SUSEConnect perl
```

```
zypper install sudo wget cmake libgfortran5 perl
```

```
zypper install sudo wget perl python3
```

```
zypper install sudo wget rsync perl
```

See [Run ROCm Docker containers](https://rocm.docs.amd.com/docker-containers.html) for Docker-related guidance.

### Prepare Windows for ROCm installation[#](https://rocm.docs.amd.com#prepare-windows-for-rocm-installation-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-i-amdgpu-install-i-runfile-os-windows-os-ubuntu-os-debian-os-rhel-os-rocky-linux-os-oracle-linux-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-ubuntu-os-debian-i-pkgman-i-pip-i-tar-i-runfile-os-rhel-os-rocky-linux-os-oracle-linux-i-pkgman-i-pip-i-tar-os-rhel-rhel-ver-8-10-rhel-ver-9-4-rhel-ver-9-6-rhel-ver-9-8-rhel-ver-10-0-rhel-ver-10-2-os-oracle-linux-oracle-linux-ver-8-oracle-linux-ver-9-oracle-linux-ver-10-os-rocky-linux-i-runfile-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-windows)

Remove any existing HIP SDK for Windows installations and other conflicting AMD graphics software. To uninstall the HIP SDK using the GUI, navigate to the following screen:

Control Panel > Programs > Uninstall a program


Disable the following Windows security features as they can interfere with ROCm functionality:

Turn off WDAG (Windows Defender Application Guard)

Control Panel > Programs > Programs and Features > Turn Windows features on or off >

**Clear**“Microsoft Defender Application Guard”

Turn off SAC (Smart App Control)

Settings > Privacy & security > Windows Security > App & browser control > Smart App Control settings >

**Off**



### Install WSL2 and Ubuntu 26.04[#](https://rocm.docs.amd.com#install-wsl2-and-ubuntu-26-04-os-wsl-ubuntu-ver-26-04)

Install WSL2 and Ubuntu 26.04 on your Windows system. See [How to install Linux on Windows
with WSL2 (Microsoft Learn)](https://learn.microsoft.com/en-us/windows/wsl/install) for instructions.

Complete the following instructions in your WSL2 environment.

### Install WSL2 and Ubuntu 24.04[#](https://rocm.docs.amd.com#install-wsl2-and-ubuntu-24-04-os-wsl-ubuntu-ver-26-04-ubuntu-ver-24-04-4)

Install WSL2 and Ubuntu 24.04 on your Windows system. See [How to install Linux on Windows
with WSL2 (Microsoft Learn)](https://learn.microsoft.com/en-us/windows/wsl/install) for instructions.

Complete the following instructions in your WSL2 environment.

### Install WSL2 and Ubuntu 22.04[#](https://rocm.docs.amd.com#install-wsl2-and-ubuntu-22-04-os-wsl-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5)

Install WSL2 and Ubuntu 22.04 on your Windows system. See [How to install Linux on Windows
with WSL2 (Microsoft Learn)](https://learn.microsoft.com/en-us/windows/wsl/install) for instructions.

Complete the following instructions in your WSL2 environment.

### Install the OEM kernel[#](https://rocm.docs.amd.com#install-the-oem-kernel-os-ubuntu-os-wsl-ubuntu-ver-24-04-4)

Ryzen APUs (gfx1150, gfx1151, gfx1152, gfx1153, and gfx1103) require the OEM
kernel 6.14 for Ubuntu 24.04. Use the following command to install it
using `apt`

.

```
sudo apt update && sudo apt install linux-oem-24.04d
```

Reboot your system after installing the OEM kernel.

### Install the OEM kernel[#](https://rocm.docs.amd.com#install-the-oem-kernel-os-ubuntu-ubuntu-ver-24-04-4)

Ryzen APUs require the OEM kernel 6.14 or newer for Ubuntu 24.04. Use the
following command to install it using `apt`

.

```
sudo apt update && sudo apt install linux-oem-24.04d
```

Reboot your system after installing the OEM kernel.

### Register your Red Hat Enterprise Linux system[#](https://rocm.docs.amd.com#register-your-red-hat-enterprise-linux-system-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-i-amdgpu-install-i-runfile-os-windows-os-ubuntu-os-debian-os-rhel-os-rocky-linux-os-oracle-linux-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-ubuntu-os-debian-i-pkgman-i-pip-i-tar-i-runfile-os-rhel-os-rocky-linux-os-oracle-linux-i-pkgman-i-pip-i-tar-os-rhel-rhel-ver-8-10-rhel-ver-9-4-rhel-ver-9-6-rhel-ver-9-8-rhel-ver-10-0-rhel-ver-10-2-os-oracle-linux-oracle-linux-ver-8-oracle-linux-ver-9-oracle-linux-ver-10-os-rocky-linux-i-runfile-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-windows-os-wsl-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-fam-ryzen-i-pkgman-i-pip-i-tar-os-ubuntu-os-wsl-ubuntu-ver-24-04-4-i-amdgpu-install-os-ubuntu-ubuntu-ver-24-04-4-os-rhel)

Register your Red Hat Enterprise Linux (RHEL) system to enable access to Red Hat repositories and ensure you’re able to download and install packages.

Run the following command to register your system:

```
subscription-manager register --username <username> --password <password>
```

```
subscription-manager register --username <username> --password <password>
subscription-manager attach --auto
```

### Register your SUSE Linux Enterprise Server system[#](https://rocm.docs.amd.com#register-your-suse-linux-enterprise-server-system-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-i-amdgpu-install-i-runfile-os-windows-os-ubuntu-os-debian-os-rhel-os-rocky-linux-os-oracle-linux-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-ubuntu-os-debian-i-pkgman-i-pip-i-tar-i-runfile-os-rhel-os-rocky-linux-os-oracle-linux-i-pkgman-i-pip-i-tar-os-rhel-rhel-ver-8-10-rhel-ver-9-4-rhel-ver-9-6-rhel-ver-9-8-rhel-ver-10-0-rhel-ver-10-2-os-oracle-linux-oracle-linux-ver-8-oracle-linux-ver-9-oracle-linux-ver-10-os-rocky-linux-i-runfile-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-windows-os-wsl-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-fam-ryzen-i-pkgman-i-pip-i-tar-os-ubuntu-os-wsl-ubuntu-ver-24-04-4-i-amdgpu-install-os-ubuntu-ubuntu-ver-24-04-4-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-sles)

Register your SUSE Linux Enterprise Server (SLES) system to enable access to SUSE repositories and ensure you’re able to download and install packages.

Run the following command to register your system:

```
sudo SUSEConnect -r <REGCODE>
```

### Update your system[#](https://rocm.docs.amd.com#update-your-system-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-i-amdgpu-install-i-runfile-os-windows-os-ubuntu-os-debian-os-rhel-os-rocky-linux-os-oracle-linux-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-ubuntu-os-debian-i-pkgman-i-pip-i-tar-i-runfile-os-rhel-os-rocky-linux-os-oracle-linux-i-pkgman-i-pip-i-tar-os-rhel-rhel-ver-8-10-rhel-ver-9-4-rhel-ver-9-6-rhel-ver-9-8-rhel-ver-10-0-rhel-ver-10-2-os-oracle-linux-oracle-linux-ver-8-oracle-linux-ver-9-oracle-linux-ver-10-os-rocky-linux-i-runfile-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-windows-os-wsl-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-fam-ryzen-i-pkgman-i-pip-i-tar-os-ubuntu-os-wsl-ubuntu-ver-24-04-4-i-amdgpu-install-os-ubuntu-ubuntu-ver-24-04-4-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-sles-os-rhel)

After registering your system, update RHEL to the latest packages. This is particularly important for newer hardware on older versions of RHEL.

Run the following command to update your system:

```
sudo dnf update --releasever=10.2 --exclude=\*release\*
```

```
sudo dnf update --releasever=10.0 --exclude=\*release\*
```

```
sudo dnf update --releasever=9.8 --exclude=\*release\*
```

```
sudo dnf update --releasever=9.6 --exclude=\*release\*
```

```
sudo dnf update --releasever=9.4 --exclude=\*release\*
```

```
sudo dnf update --releasever=8.10 --exclude=\*release\*
```

### Update your system[#](https://rocm.docs.amd.com#update-your-system-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-i-amdgpu-install-i-runfile-os-windows-os-ubuntu-os-debian-os-rhel-os-rocky-linux-os-oracle-linux-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-ubuntu-os-debian-i-pkgman-i-pip-i-tar-i-runfile-os-rhel-os-rocky-linux-os-oracle-linux-i-pkgman-i-pip-i-tar-os-rhel-rhel-ver-8-10-rhel-ver-9-4-rhel-ver-9-6-rhel-ver-9-8-rhel-ver-10-0-rhel-ver-10-2-os-oracle-linux-oracle-linux-ver-8-oracle-linux-ver-9-oracle-linux-ver-10-os-rocky-linux-i-runfile-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-windows-os-wsl-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-fam-ryzen-i-pkgman-i-pip-i-tar-os-ubuntu-os-wsl-ubuntu-ver-24-04-4-i-amdgpu-install-os-ubuntu-ubuntu-ver-24-04-4-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-sles-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-sles)

After registering your system, update SLES to the latest available packages. This is particularly important for newer hardware on older versions of SLES.

Run the following command to update your system:

```
sudo zypper update
```

### Add additional package repositories[#](https://rocm.docs.amd.com#add-additional-package-repositories-i-amdgpu-install-os-rhel)

ROCm installation packages depend on packages that aren’t included in the default package repositories. Use the following command to add the necessary repositories.

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
sudo rpm -ivh epel-release-latest-10.noarch.rpm
sudo dnf config-manager --enable codeready-builder-for-rhel-10-x86_64-rpms
```

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
```

```
sudo dnf config-manager --enable codeready-builder-for-rhel-9-x86_64-rpms
```

### Update your system[#](https://rocm.docs.amd.com#update-your-system-i-pkgman-os-oracle-linux)

Update Oracle Linux to the latest available packages.

Run the following command to update your system:

```
sudo dnf update --releasever=10.2 --exclude=\*release\*
```

```
sudo dnf update --releasever=9.8 --exclude=\*release\*
```

```
sudo dnf update --releasever=8.10 --exclude=\*release\*
```

### Add additional package repositories[#](https://rocm.docs.amd.com#add-additional-package-repositories-i-pkgman-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rhel)

ROCm installation packages depend on packages that aren’t included in the default package repositories. Use the following command to add the necessary repositories.

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
sudo rpm -ivh epel-release-latest-10.noarch.rpm
sudo dnf config-manager --enable codeready-builder-for-rhel-10-x86_64-rpms
```

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
```

```
sudo dnf config-manager --enable codeready-builder-for-rhel-9-x86_64-rpms
```

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo rpm -ivh epel-release-latest-8.noarch.rpm
```

```
sudo dnf config-manager --enable codeready-builder-for-rhel-8-x86_64-rpms
```

### Add additional package repositories[#](https://rocm.docs.amd.com#add-additional-package-repositories-i-pkgman-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux)

ROCm installation packages depend on packages that aren’t included in the default package repositories. Use the following command to add the necessary repositories.

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-10.noarch.rpm
sudo rpm -ivh epel-release-latest-10.noarch.rpm
sudo crb enable
```

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
sudo crb enable
```

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
sudo rpm -ivh epel-release-latest-8.noarch.rpm
sudo crb enable
```

### Add additional package repositories[#](https://rocm.docs.amd.com#add-additional-package-repositories-i-pkgman-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux)

ROCm installation packages depend on packages that aren’t included in the default package repositories. Use the following command to add the necessary repositories.

```
wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm
sudo rpm -ivh epel-release-latest-9.noarch.rpm
sudo crb enable
```

### Install additional packages[#](https://rocm.docs.amd.com#install-additional-packages-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-wsl-i-amdgpu-install)

Some ROCm tools require the `libatomic`

and `libquadmath`

libraries to run correctly. Install
them using your distribution’s package manager.

```
sudo apt install libatomic1 libquadmath0
```

```
sudo dnf install libatomic libquadmath
```

### Install additional packages[#](https://rocm.docs.amd.com#install-additional-packages-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-wsl-i-amdgpu-install-os-ubuntu-os-rhel-i-pkgman-i-pip-i-tar)

Some ROCm tools require the `libatomic`

and `libquadmath`

libraries to run correctly. Install
them using your distribution’s package manager.

```
sudo apt install libatomic1 libquadmath0
```

## Install the OEM kernel for Ryzen APUs

Ryzen APUs require the OEM kernel 6.14 or newer for Ubuntu 24.04. Use the
following command to install it using `apt`

.

```
sudo apt update && sudo apt install linux-oem-24.04d
```

Reboot your system after installing the OEM kernel.

To build the ROCDXG library for WSL2, you’ll need GCC 11.4 or later and CMake 3.15 or later.

```
sudo apt install libatomic1 libquadmath0 gcc g++ cmake
```

```
sudo dnf install libatomic libquadmath
```

```
sudo zypper install libatomic1 libquadmath0
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-ubuntu-ubuntu-ver-26-04)

Install a supported Python version. For example, to install Python 3.14, run the following command:

```
sudo apt install python3.14 python3.14-venv
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4)

Install a supported Python version. For example, to install Python 3.12, run the following command:

```
sudo apt install python3.12 python3.12-venv
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5)

Install a supported Python version. For example, to install Python 3.11, run the following command:

```
sudo apt install python3.11 python3.11-venv
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-debian-debian-ver-13)

Install a supported Python version. For example, to install Python 3.13, run the following command:

```
sudo apt install python3.13 python3.13-venv
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-debian-debian-ver-13-debian-ver-12)

Install a supported Python version. For example, to install Python 3.11, run the following command:

```
sudo apt install python3.11 python3.11-venv
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-rhel-rhel-ver-10-2-rhel-ver-10-0)

Install a supported Python version. For example, to install Python 3.12, run the following command:

```
sudo dnf install python3.12 python3.12-pip
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-9-rhel-ver-8-10)

Install a supported Python version. For example, to install Python 3.11, run the following command:

```
sudo dnf install python3.11 python3.11-pip
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-oracle-linux-oracle-linux-ver-10)

Install a supported Python version. For example, to install Python 3.12, run the following command:

```
sudo dnf install python3.12 python3.12-pip
```

### Install Python[#](https://rocm.docs.amd.com#install-python-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8)

Install a supported Python version. For example, to install Python 3.11, run the following command:

```
sudo dnf install python3.11 python3.11-pip
```

### Install Python[#](https://rocm.docs.amd.com#install-python-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-9-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux)

Install a supported Python version. For example, to install Python 3.11, run the following command:

```
sudo dnf install python3.11 python3.11-pip
```

### Install Python[#](https://rocm.docs.amd.com#install-python-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-9-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles)

Install a supported Python version. For example, to install Python 3.13, run the following command:

```
sudo zypper install python313 python313-pip
```

Install a supported Python version. For example, to install Python 3.11, run the following command:

```
sudo zypper install python311 python311-pip
```

### Install Python[#](https://rocm.docs.amd.com#install-python-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-9-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-0-sles-ver-15-7-os-windows)

Install a supported Python version: 3.11, 3.12, 3.13, or 3.14. See [Python
Releases for Windows](https://www.python.org/downloads/windows/) for
installation details.

### Configure permissions for GPU access[#](https://rocm.docs.amd.com#configure-permissions-for-gpu-access-i-pkgman-i-pip-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-wsl)

There are two primary methods for configuring GPU access for ROCm: group membership or udev rules. Each method has its own advantages. The choice depends on your specific requirements and system management preferences. If you’re working in a containerized environment, do this step on the host system, outside of the container.

By default, GPU access is controlled by membership in the `video`

and
`render`

Linux system groups. The `video`

group traditionally handles
video device access, while the `render`

group manages GPU rendering
through DRM render nodes.

```
# Add the current user to the render and video groups
sudo usermod -a -G render,video $LOGNAME
```

udev rules are a flexible, system-wide approach for managing device permissions, eliminating the need for user group management while allowing granular GPU access. To enable them and grant GPU access to all users, run the following command:

```
sudo tee /etc/udev/rules.d/70-amdgpu.rules << EOF
KERNEL=="kfd", GROUP="render", MODE="0666"
SUBSYSTEM=="drm", KERNEL=="renderD*", GROUP="render", MODE="0666"
EOF
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Note

To apply all settings, reboot your system.

### Configure permissions for GPU access[#](https://rocm.docs.amd.com#configure-permissions-for-gpu-access-i-amdgpu-install-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles)

There are two primary methods for configuring GPU access for ROCm: group membership or udev rules. Each method has its own advantages. The choice depends on your specific requirements and system management preferences.

By default, GPU access is controlled by membership in the `video`

and
`render`

Linux system groups. The `video`

group traditionally handles
video device access, while the `render`

group manages GPU rendering
through DRM render nodes.

```
# Add the current user to the render and video groups
sudo usermod -a -G render,video $LOGNAME
```

udev rules are a flexible, system-wide approach for managing device permissions, eliminating the need for user group management while allowing granular GPU access. To enable them and grant GPU access to all users, run the following command:

```
sudo tee /etc/udev/rules.d/70-amdgpu.rules << EOF
KERNEL=="kfd", GROUP="render", MODE="0666"
SUBSYSTEM=="drm", KERNEL=="renderD*", GROUP="render", MODE="0666"
EOF
sudo udevadm control --reload-rules
sudo udevadm trigger
```

Note

To apply all settings, reboot your system.

## Quick start[#](https://rocm.docs.amd.com#quick-start-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-i-amdgpu-install-i-runfile-os-windows-os-ubuntu-os-debian-os-rhel-os-rocky-linux-os-oracle-linux-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-ubuntu-os-debian-i-pkgman-i-pip-i-tar-i-runfile-os-rhel-os-rocky-linux-os-oracle-linux-i-pkgman-i-pip-i-tar-os-rhel-rhel-ver-8-10-rhel-ver-9-4-rhel-ver-9-6-rhel-ver-9-8-rhel-ver-10-0-rhel-ver-10-2-os-oracle-linux-oracle-linux-ver-8-oracle-linux-ver-9-oracle-linux-ver-10-os-rocky-linux-i-runfile-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-windows-os-wsl-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-fam-ryzen-i-pkgman-i-pip-i-tar-os-ubuntu-os-wsl-ubuntu-ver-24-04-4-i-amdgpu-install-os-ubuntu-ubuntu-ver-24-04-4-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-sles-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-sles-i-amdgpu-install-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-i-pkgman-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-rocky-linux-ver-9-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-wsl-i-amdgpu-install-os-ubuntu-os-rhel-i-pkgman-i-pip-i-tar-os-ubuntu-os-debian-fam-all-ubuntu-ver-24-04-4-os-wsl-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-9-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-0-sles-ver-15-7-os-windows-i-pkgman-i-pip-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-wsl-i-amdgpu-install-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-runfile)

Download and launch the interactive installer to set up ROCm and/or the AMD GPU Driver with guided, step-by-step configuration.

```
curl -fsSLO https://repo.radeon.com/rocm/installer/rocm-runfile-installer/rocm-rel-10.0/rocm-installer-10.0.0-4.run && bash rocm-installer-10.0.0-4.run
```

## Configuration options[#](https://rocm.docs.amd.com#configuration-options-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-i-amdgpu-install-i-runfile-os-windows-os-ubuntu-os-debian-os-rhel-os-rocky-linux-os-oracle-linux-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-ubuntu-os-debian-i-pkgman-i-pip-i-tar-i-runfile-os-rhel-os-rocky-linux-os-oracle-linux-i-pkgman-i-pip-i-tar-os-rhel-rhel-ver-8-10-rhel-ver-9-4-rhel-ver-9-6-rhel-ver-9-8-rhel-ver-10-0-rhel-ver-10-2-os-oracle-linux-oracle-linux-ver-8-oracle-linux-ver-9-oracle-linux-ver-10-os-rocky-linux-i-runfile-os-sles-i-pkgman-i-pip-i-tar-i-runfile-os-windows-os-wsl-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-fam-ryzen-i-pkgman-i-pip-i-tar-os-ubuntu-os-wsl-ubuntu-ver-24-04-4-i-amdgpu-install-os-ubuntu-ubuntu-ver-24-04-4-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-sles-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-sles-i-amdgpu-install-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-i-pkgman-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-rocky-linux-ver-9-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-wsl-i-amdgpu-install-os-ubuntu-os-rhel-i-pkgman-i-pip-i-tar-os-ubuntu-os-debian-fam-all-ubuntu-ver-24-04-4-os-wsl-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-9-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-0-sles-ver-15-7-os-windows-i-pkgman-i-pip-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-wsl-i-amdgpu-install-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-runfile-i-runfile)

The following command line options are used to customize the runfile
installer, including dependency handling and GPU access configuration. For
recommended usage, go to [Installation](https://rocm.docs.amd.com#rocm-install).

### Dependencies[#](https://rocm.docs.amd.com#dependencies-i-runfile-i-runfile)

The runfile installer controls dependency installation via the `deps=`

argument.

| Command | Description |
|---|---|
| Installs all required packages |
| Lists all required packages |
| Validates which required packages are installed |

Specify the target after the dependency argument; for example: `deps=install rocm`

.

Note

It is recommended to include `deps=install`

if you’re not sure what
dependencies are installed on your system.

### GPU access[#](https://rocm.docs.amd.com#gpu-access-i-runfile-i-runfile-i-runfile)

There are two primary methods of configuring GPU access for ROCm: group membership or udev rules. The choice depends on your specific requirements and system management preferences.

The runfile installer sets GPU access at install time using the `gpu-access=`

argument.

| Argument | Method |
|---|---|
| Group membership (adds the current user to the render and video groups) |
| udev rules (configures system-wide GPU access) |

## Installation[#](https://rocm.docs.amd.com#installation)

Note

If you have ROCm 7.2.4 or older installed, please uninstall it before proceeding.

Note

If you have ROCm 7.2.4 or older installed, please uninstall it before proceeding.

Note

If you have ROCm 7.2.4 or older installed, please uninstall it before proceeding.

Note

If you have ROCm 7.2.4 or older installed, please uninstall it before proceeding.

Before getting started, make sure you’ve completed the [Prerequisites](https://rocm.docs.amd.com#rocm-prerequisites).
For information about supported operating systems and compatible AMD devices,
see the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html).

Caution

Do not replace or copy the ROCm compiler and runtime DLLs to System32 as this can cause conflicts.

### Download the runfile installer[#](https://rocm.docs.amd.com#download-the-runfile-installer-os-ubuntu-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-i-pkgman-i-runfile-os-rhel-rhel-ver-10-0-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-i-pkgman-i-runfile-os-sles-sles-ver-15-7-i-pkgman-i-runfile-os-debian-os-oracle-linux-os-rocky-linux-os-windows-i-pkgman-i-runfile-os-windows-i-runfile)

Use the following command to download the ROCm Runfile Installer.

```
wget https://repo.radeon.com/rocm/installer/rocm-runfile-installer/rocm-rel-10.0/rocm-installer-10.0.0-4.run
```

### Install the amdgpu-install script[#](https://rocm.docs.amd.com#install-the-amdgpu-install-script-i-amdgpu-install-os-ubuntu-os-rhel)

Use the following commands to download and install the `amdgpu-install`

script.

```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/31.50/ubuntu/resolute/amdgpu-install_31.50.315000-1_all.deb
sudo apt install ./amdgpu-install_31.50.315000-1_all.deb
```

```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/31.50/ubuntu/noble/amdgpu-install_31.50.315000-1_all.deb
sudo apt install ./amdgpu-install_31.50.315000-1_all.deb
```

```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/31.50/ubuntu/jammy/amdgpu-install_31.50.315000-1_all.deb
sudo apt install ./amdgpu-install_31.50.315000-1_all.deb
```

```
wget https://repo.radeon.com/amdgpu-install/31.50/rhel/10.2/amdgpu-install-31.50.315000-1.el10.noarch.rpm
sudo dnf install ./amdgpu-install-31.50.315000-1.el10.noarch.rpm
```

```
wget https://repo.radeon.com/amdgpu-install/31.50/rhel/10.0/amdgpu-install-31.50.315000-1.el10.noarch.rpm
sudo dnf install ./amdgpu-install-31.50.315000-1.el10.noarch.rpm
```

```
wget https://repo.radeon.com/amdgpu-install/31.50/rhel/9.8/amdgpu-install-31.50.315000-1.el9.noarch.rpm
sudo dnf install ./amdgpu-install-31.50.315000-1.el9.noarch.rpm
```

```
wget https://repo.radeon.com/amdgpu-install/31.50/rhel/9.6/amdgpu-install-31.50.315000-1.el9.noarch.rpm
sudo dnf install ./amdgpu-install-31.50.315000-1.el9.noarch.rpm
```

```
wget https://repo.radeon.com/amdgpu-install/31.50/rhel/9.4/amdgpu-install-31.50.315000-1.el9.noarch.rpm
sudo dnf install ./amdgpu-install-31.50.315000-1.el9.noarch.rpm
```

```
wget https://repo.radeon.com/amdgpu-install/31.50/rhel/8.10/amdgpu-install-31.50.315000-1.el8.noarch.rpm
sudo dnf install ./amdgpu-install-31.50.315000-1.el8.noarch.rpm
```

### Install the kernel driver[#](https://rocm.docs.amd.com#install-the-kernel-driver-i-pkgman-i-pip-i-tar-fam-all)

For information about AMD GPU Driver (amdgpu) compatibility, see the
[Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html).

For Instinct and Radeon devices, install the AMD GPU Driver (amdgpu).
See [Ubuntu native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-ubuntu.html)
in the AMD Instinct Data Center GPU Documentation.

Supported Ryzen APUs require the inbox kernel driver included with Ubuntu 26.04.

Supported Ryzen APUs require the inbox kernel driver included with Ubuntu 24.04.4.

For Instinct and Radeon devices, install the AMD GPU Driver (amdgpu).
See [Debian native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-debian.html)
in the AMD Instinct Data Center GPU Documentation.

For Instinct and Radeon devices, install the AMD GPU Driver (amdgpu).
See [RHEL native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-rhel.html)
in the AMD Instinct Data Center GPU Documentation.

For Instinct and Radeon devices, install the AMD GPU Driver (amdgpu).
See [Oracle Linux native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-ol.html)
in the AMD Instinct Data Center GPU Documentation.

For Instinct and Radeon devices, install the AMD GPU Driver (amdgpu).
See [Rocky Linux native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-rl.html)
in the AMD Instinct Data Center GPU Documentation.

For Instinct and Radeon devices, install the AMD GPU Driver (amdgpu).
See [SLES native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-sles.html)
in the AMD Instinct Data Center GPU Documentation.

### Install the kernel driver[#](https://rocm.docs.amd.com#install-the-kernel-driver-i-pkgman-i-pip-i-tar-fam-all-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-fam-instinct-fam-radeon)

For information about AMD GPU Driver (amdgpu) compatibility, see the
[Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html).

For instructions on installing the AMD GPU Driver (amdgpu), see [Ubuntu native
installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-ubuntu.html)
in the AMD Instinct Data Center GPU Documentation.

For instructions on installing the AMD GPU Driver (amdgpu), see [Debian native
installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-debian.html)
in the AMD Instinct Data Center GPU Documentation.

For instructions on installing the AMD GPU Driver (amdgpu), see [RHEL native
installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-rhel.html)
in the AMD Instinct Data Center GPU Documentation.

For instructions on installing the AMD GPU Driver (amdgpu), see [Oracle Linux native
installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-ol.html)
in the AMD Instinct Data Center GPU Documentation.

For instructions on installing the AMD GPU Driver (amdgpu), see [Rocky Linux native
installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-rl.html)
in the AMD Instinct Data Center GPU Documentation.

For instructions on installing the AMD GPU Driver (amdgpu), see [SLES
native installation](https://instinct.docs.amd.com/projects/amdgpu-docs/en/docs-31.50.0/install/detailed-install/package-manager/package-manager-sles.html)
in the AMD Instinct Data Center GPU Documentation.

### About the kernel driver[#](https://rocm.docs.amd.com#about-the-kernel-driver-fam-ryzen-os-ubuntu)

Supported Ryzen APUs require the inbox kernel driver included with Ubuntu 26.04.

Supported Ryzen APUs require the inbox kernel driver included with Ubuntu 24.04.4.

### Install the kernel driver[#](https://rocm.docs.amd.com#install-the-kernel-driver-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-fam-all-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-fam-instinct-fam-radeon-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-fam-ryzen-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-i-runfile)

For information about AMD GPU Driver (amdgpu) compatibility, see the
[Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html).

```
bash rocm-installer-10.0.0-4.run deps=install amdgpu
```

Note

Reboot your system after installing the AMD GPU Driver.

### Install AMD Software: Adrenalin Edition[#](https://rocm.docs.amd.com#install-amd-software-adrenalin-edition-os-ubuntu-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-i-pkgman-i-runfile-os-rhel-rhel-ver-10-0-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-i-pkgman-i-runfile-os-sles-sles-ver-15-7-i-pkgman-i-runfile-os-debian-os-oracle-linux-os-rocky-linux-os-windows-i-pkgman-i-runfile-os-windows-i-runfile-i-amdgpu-install-os-ubuntu-os-rhel-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pkgman-i-pip-i-tar-fam-all-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-fam-instinct-fam-radeon-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-fam-ryzen-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-i-runfile-os-windows-os-wsl)

For details and the download link, see [https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-26-8-1.html#Downloads](https://www.amd.com/en/resources/support-articles/release-notes/RN-RAD-WIN-26-8-1.html#Downloads).

### Install ROCm[#](https://rocm.docs.amd.com#install-rocm)

Use the following instructions to install ROCm packages on your system.

#### Register ROCm repositories[#](https://rocm.docs.amd.com#register-rocm-repositories-i-pkgman)

Register the ROCm repository with your system’s package manager. This lets you install and update
ROCm packages using `apt`

.

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/ubuntu2604/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
# ROCm release signing key
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/ubuntu2604/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/ubuntu2404/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
# ROCm release signing key
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/ubuntu2404/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/ubuntu2204/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
# ROCm release signing key
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/ubuntu2204/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

Register the ROCm repository with your system’s package manager. This enables
you to install and update ROCm packages using `apt`

.

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/debian13/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/debian13/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/debian12/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable.sources << EOF
X-Repo-Id: amdrocm-stable
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages/debian12/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

Register the ROCm repository with your system’s package manager. This enables
you to install and update ROCm packages using `dnf`

.

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel10/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel10/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel8/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel8/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

Register the ROCm repository with your system’s package manager. This enables
you to install and update ROCm packages using `dnf`

.

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel10/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel10/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel8/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel8/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

Register the ROCm repository with your system’s package manager. This enables
you to install and update ROCm packages using `dnf`

.

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

Register the ROCm repository with your system’s package manager. This enables
you to install and update ROCm packages using `zypper`

.

```
sudo tee /etc/zypp/repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/sles16/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo zypper --gpg-auto-import-keys refresh
```

```
sudo tee /etc/zypp/repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/sles16/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo zypper --gpg-auto-import-keys refresh
```

```
sudo tee /etc/zypp/repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/sles15/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo zypper --gpg-auto-import-keys refresh
```

```
sudo tee /etc/zypp/repos.d/amdrocm-stable.repo <<EOF
[amdrocm-stable]
name=ROCm 10.0.0
baseurl=https://stable.repo.amd.com/rocm/core/packages/sles15/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo zypper --gpg-auto-import-keys refresh
```

#### Install ROCm packages[#](https://rocm.docs.amd.com#install-rocm-packages-i-pkgman-os-ubuntu-os-wsl-ubuntu-ver-26-04-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-24-04-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-22-04-5-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-debian-debian-ver-13-fam-all-fam-instinct-fam-radeon-fam-ryzen-debian-ver-12-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rhel-rhel-ver-10-2-rhel-ver-10-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-8-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-oracle-linux-oracle-linux-ver-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-9-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-8-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rocky-linux-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-sles-sles-ver-16-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-sles-ver-15-7-fam-all-fam-instinct-fam-radeon-fam-ryzen-i-pkgman)

Use `apt`

to install the core ROCm packages. See [ROCm meta
packages](https://rocm.docs.amd.com#rocm-install-meta-packages) for additional installation
options.

```
sudo apt install amdrocm10.0
```

```
sudo apt install amdrocm10.0-gfx950
```

```
sudo apt install amdrocm10.0-gfx942
```

```
sudo apt install amdrocm10.0-gfx90a
```

```
sudo apt install amdrocm10.0-gfx908
```

```
sudo apt install amdrocm10.0-gfx1201
```

```
sudo apt install amdrocm10.0-gfx1200
```

```
sudo apt install amdrocm10.0-gfx1100
```

```
sudo apt install amdrocm10.0-gfx1101
```

```
sudo apt install amdrocm10.0-gfx1102
```

```
sudo apt install amdrocm10.0-gfx1103
```

```
sudo apt install amdrocm10.0-gfx1030
```

```
sudo apt install amdrocm10.0-gfx1151
```

```
sudo apt install amdrocm10.0-gfx1150
```

```
sudo apt install amdrocm10.0-gfx1152
```

```
sudo apt install amdrocm10.0-gfx1153
```

Use `dnf`

to install the core ROCm packages. See [ROCm meta
packages](https://rocm.docs.amd.com#rocm-install-meta-packages) for additional installation
options.

```
sudo dnf install amdrocm10.0
```

```
sudo dnf install amdrocm10.0-gfx950
```

```
sudo dnf install amdrocm10.0-gfx942
```

```
sudo dnf install amdrocm10.0-gfx90a
```

```
sudo dnf install amdrocm10.0-gfx908
```

```
sudo dnf install amdrocm10.0-gfx1201
```

```
sudo dnf install amdrocm10.0-gfx1200
```

```
sudo dnf install amdrocm10.0-gfx1100
```

```
sudo dnf install amdrocm10.0-gfx1101
```

```
sudo dnf install amdrocm10.0-gfx1102
```

```
sudo dnf install amdrocm10.0-gfx1103
```

```
sudo dnf install amdrocm10.0-gfx1030
```

```
sudo dnf install amdrocm10.0-gfx1151
```

```
sudo dnf install amdrocm10.0-gfx1150
```

```
sudo dnf install amdrocm10.0-gfx1152
```

```
sudo dnf install amdrocm10.0-gfx1153
```

Use `zypper`

to install the core ROCm packages. See [ROCm meta
packages](https://rocm.docs.amd.com#rocm-install-meta-packages) for additional installation
options.

```
sudo zypper install amdrocm10.0
```

```
sudo zypper install amdrocm10.0-gfx950
```

```
sudo zypper install amdrocm10.0-gfx942
```

```
sudo zypper install amdrocm10.0-gfx90a
```

```
sudo zypper install amdrocm10.0-gfx908
```

##### ROCm meta packages[#](https://rocm.docs.amd.com#rocm-meta-packages-i-pkgman-os-ubuntu-os-wsl-ubuntu-ver-26-04-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-24-04-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-22-04-5-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-debian-debian-ver-13-fam-all-fam-instinct-fam-radeon-fam-ryzen-debian-ver-12-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rhel-rhel-ver-10-2-rhel-ver-10-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-8-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-oracle-linux-oracle-linux-ver-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-9-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-8-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rocky-linux-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-sles-sles-ver-16-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-sles-ver-15-7-fam-all-fam-instinct-fam-radeon-fam-ryzen-i-pkgman-os-ubuntu-os-debian-os-wsl-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-i-pkgman)

Meta packages group related components and dependencies together, allowing you to install only what is necessary for your use case. The following table describes available ROCm meta packages:

| Meta package name | Use case | Description | Contents | ||||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| ROCm Base | Core runtime environment. Install this to run ROCm applications. | Runtimes, libraries, system control and monitoring tools, and other essential components. | |
|
| ROCm Developer Essentials | Development environment. Install this to build ROCm applications. |
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| ROCm Profiler | Install this to profile and optimize ROCm applications. | Profilers and related tools. | ||||||||||||||||
| ROCm OpenCL | Install this to run OpenCL applications on ROCm. | Components needed to run OpenCL. | ||||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| ROCm Full Suite | Install this if you need everything. | The complete ROCm Core SDK including runtimes, compilers, development tools, and dependencies. |

Warning

Before proceeding, please enable “Above 4G Decoding” in your BIOS settings.

Run the `amdgpu-install`

script with the following `--usecase`

arguments
to install ROCm, graphics and amdgpu driver packages.

```
sudo amdgpu-install --usecase=rocm,graphics --gfxversion=auto
```

Run the `amdgpu-install`

script with the following `--usecase`

arguments to install ROCm packages. Ryzen APUs require the inbox
kernel driver included with Ubuntu – to skip installing the AMD GPU
driver, add `--no-dkms`

.

```
sudo amdgpu-install --usecase=rocm --gfxversion=auto --no-dkms
```

Run the `amdgpu-install`

script with the following `--usecase`

arguments
to install ROCm and graphics packages.

```
sudo amdgpu-install --usecase=rocm,graphics --gfxversion=all
```

Reboot your system after installing.

#### Set up your Python virtual environment[#](https://rocm.docs.amd.com#set-up-your-python-virtual-environment-i-pkgman-os-ubuntu-os-wsl-ubuntu-ver-26-04-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-24-04-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-22-04-5-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-debian-debian-ver-13-fam-all-fam-instinct-fam-radeon-fam-ryzen-debian-ver-12-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rhel-rhel-ver-10-2-rhel-ver-10-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-8-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-oracle-linux-oracle-linux-ver-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-9-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-8-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rocky-linux-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-sles-sles-ver-16-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-sles-ver-15-7-fam-all-fam-instinct-fam-radeon-fam-ryzen-i-pkgman-os-ubuntu-os-debian-os-wsl-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-i-pkgman-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-i-amdgpu-install-os-ubuntu-os-rhel-fam-radeon-fam-ryzen-fam-all-i-pip)

Create and activate the Python virtual environment where you’ll install ROCm packages.

For example, to create and activate a Python 3.14 virtual environment, run the following command:

```
python3.14 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.12 virtual environment, run the following command:

```
python3.12 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.11 virtual environment, run the following command:

```
python3.11 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.13 virtual environment, run the following command:

```
python3.13 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.11 virtual environment, run the following command:

```
python3.11 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.12 virtual environment, run the following command:

```
python3.12 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.11 virtual environment, run the following command:

```
python3.11 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.12 virtual environment, run the following command:

```
python3.12 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.11 virtual environment, run the following command:

```
python3.11 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.11 virtual environment, run the following command:

```
python3.11 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.11 virtual environment, run the following command:

```
python3.11 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.13 virtual environment, run the following command:

```
python3.13 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.11 virtual environment, run the following command:

```
python3.11 -m venv .venv
source .venv/bin/activate
```

For example, to create and activate a Python 3.12 virtual environment, run the following command:

```
py -3.12 -m venv .venv
.venv\Scripts\activate
```

#### Install ROCm wheel packages[#](https://rocm.docs.amd.com#install-rocm-wheel-packages-i-pkgman-os-ubuntu-os-wsl-ubuntu-ver-26-04-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-24-04-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-22-04-5-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-debian-debian-ver-13-fam-all-fam-instinct-fam-radeon-fam-ryzen-debian-ver-12-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rhel-rhel-ver-10-2-rhel-ver-10-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-8-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-oracle-linux-oracle-linux-ver-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-9-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-8-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rocky-linux-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-sles-sles-ver-16-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-sles-ver-15-7-fam-all-fam-instinct-fam-radeon-fam-ryzen-i-pkgman-os-ubuntu-os-debian-os-wsl-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-i-pkgman-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-i-amdgpu-install-os-ubuntu-os-rhel-fam-radeon-fam-ryzen-fam-all-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-0-sles-ver-15-7-os-windows-i-pip)

Use pip to install the ROCm libraries and development tools.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-all]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools for
your `gfx950`

GPU.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx950]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools for
your `gfx942`

device.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx942]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx90a]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx908]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools for
your `gfx1201`

GPU.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1201]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools for
your `gfx1200`

GPU.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1200]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1100]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1101]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1102]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1103]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1030]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools for
your `gfx1151`

Ryzen APU.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1151]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools for
your `gfx1150`

Ryzen APU.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1150]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

Use pip to install the ROCm libraries and development tools for
your `gfx1152`

Ryzen APU.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1152]==10.0.0"
```

Use pip to install the ROCm libraries and development tools for
your `gfx1153`

Ryzen APU.

Run the following command:

```
python -m pip install --index-url https://stable.repo.amd.com/rocm/whl-next/ "rocm[libraries,device-gfx1153]==10.0.0"
```

The table below lists the available packages. Each bracketed name is an
optional *extra* of the `rocm`

meta package — combine the ones you need
as a comma-separated list (for example, `rocm[libraries,devel]`

).

| Package | Contents | Use case | ||||||||||||||
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Core SDK: runtime, HIP, compiler, utility tools, and profiling SDK (rocprofiler-sdk, rocprofv3, roctx). | Required by all ROCm users. | ||||||||||||||
| Pre-built math and ML host libraries. | Required for ML frameworks such as PyTorch and JAX. | ||||||||||||||
| Compilers, CMake configuration, headers, and static libraries. | Building ROCm applications. | ||||||||||||||
|
|
|
|
|
|
|
|
|
|
|
|
|
|
| Pre-compiled GPU kernels for the specified target. | Required to run GPU workloads; installed alongside |
| Profiling tools: rocprofiler-systems and rocprofiler-compute. | Optional; analyzing and optimizing ROCm applications. |

#### Create the installation directory[#](https://rocm.docs.amd.com#create-the-installation-directory-i-pkgman-os-ubuntu-os-wsl-ubuntu-ver-26-04-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-24-04-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-22-04-5-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-debian-debian-ver-13-fam-all-fam-instinct-fam-radeon-fam-ryzen-debian-ver-12-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rhel-rhel-ver-10-2-rhel-ver-10-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-8-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-oracle-linux-oracle-linux-ver-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-9-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-8-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rocky-linux-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-sles-sles-ver-16-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-sles-ver-15-7-fam-all-fam-instinct-fam-radeon-fam-ryzen-i-pkgman-os-ubuntu-os-debian-os-wsl-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-i-pkgman-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-i-amdgpu-install-os-ubuntu-os-rhel-fam-radeon-fam-ryzen-fam-all-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-0-sles-ver-15-7-os-windows-i-pip-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-i-tar)

Run the following command in your desired location to create your installation directory:

```
mkdir therock-tarball && cd therock-tarball
```

Important

Subsequent commands assume you’re working with the `therock-tarball`

directory. If you choose a different directory name, adjust the
commands accordingly.

Create the installation directory in `C:\TheRock\build`

. For example,
use the following command in your command prompt:

```
mkdir C:\TheRock\build
```

Important

Subsequent commands assume you’re working with the
`C:\TheRock\build`

directory. If you choose a different directory
name, adjust the commands accordingly.

#### Download and unpack the tarball[#](https://rocm.docs.amd.com#download-and-unpack-the-tarball-i-pkgman-os-ubuntu-os-wsl-ubuntu-ver-26-04-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-24-04-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-22-04-5-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-debian-debian-ver-13-fam-all-fam-instinct-fam-radeon-fam-ryzen-debian-ver-12-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rhel-rhel-ver-10-2-rhel-ver-10-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-8-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-oracle-linux-oracle-linux-ver-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-9-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-8-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rocky-linux-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-sles-sles-ver-16-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-sles-ver-15-7-fam-all-fam-instinct-fam-radeon-fam-ryzen-i-pkgman-os-ubuntu-os-debian-os-wsl-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-i-pkgman-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-i-amdgpu-install-os-ubuntu-os-rhel-fam-radeon-fam-ryzen-fam-all-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-0-sles-ver-15-7-os-windows-i-pip-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-windows-i-tar)

Use the following commands to download and untar the ROCm tarball.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-multiarch-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball for
your `gfx950`

GPU.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx950-dcgpu-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball for
your `gfx942`

GPU.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx94X-dcgpu-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx90a-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx908-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx120X-all-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx110X-all-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx103X-all-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball for
your `gfx1151`

GPU.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx1151-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball for
your `gfx1150`

GPU.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx1150-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball for
your `gfx1152`

GPU.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx1152-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Use the following commands to download and untar the ROCm tarball for
your `gfx1153`

GPU.

```
wget https://stable.repo.amd.com/rocm/core/tarball/therock-dist-linux-gfx1153-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

Download the tarball and extract the contents to `C:\TheRock\build`

.
Run the following commands in your command prompt:

```
cd C:\TheRock
curl -o therock-dist-windows-multiarch-10.0.0.tar.gz https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-multiarch-10.0.0.tar.gz
tar -xzf therock-dist-windows-multiarch-10.0.0.tar.gz -C build --strip-components=1
```

Download link:

[therock-dist-windows-multiarch-10.0.0.tar.gz](https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-multiarch-10.0.0.tar.gz)

```
cd C:\TheRock
curl -o therock-dist-windows-gfx120X-all-10.0.0.tar.gz https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx120X-all-10.0.0.tar.gz
tar -xzf therock-dist-windows-gfx120X-all-10.0.0.tar.gz -C build --strip-components=1
```

Download link:

[therock-dist-windows-gfx120X-all-10.0.0.tar.gz](https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx120X-all-10.0.0.tar.gz)

```
cd C:\TheRock
curl -o therock-dist-windows-gfx110X-all-10.0.0.tar.gz https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx110X-all-10.0.0.tar.gz
tar -xzf therock-dist-windows-gfx110X-all-10.0.0.tar.gz -C build --strip-components=1
```

Download link:

[therock-dist-windows-gfx110X-all-10.0.0.tar.gz](https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx110X-all-10.0.0.tar.gz)

```
cd C:\TheRock
curl -o therock-dist-windows-gfx103X-all-10.0.0.tar.gz https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx103X-all-10.0.0.tar.gz
tar -xzf therock-dist-windows-gfx103X-all-10.0.0.tar.gz -C build --strip-components=1
```

Download link:

[therock-dist-windows-gfx103X-all-10.0.0.tar.gz](https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx103X-all-10.0.0.tar.gz)

```
cd C:\TheRock
curl -o therock-dist-windows-gfx1151-10.0.0.tar.gz https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx1151-10.0.0.tar.gz
tar -xzf therock-dist-windows-gfx1151-10.0.0.tar.gz -C build --strip-components=1
```

Download link:

[therock-dist-windows-gfx1151-10.0.0.tar.gz](https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx1151-10.0.0.tar.gz)

```
cd C:\TheRock
curl -o therock-dist-windows-gfx1150-10.0.0.tar.gz https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx1150-10.0.0.tar.gz
tar -xzf therock-dist-windows-gfx1150-10.0.0.tar.gz -C build --strip-components=1
```

Download link:

[therock-dist-windows-gfx1150-10.0.0.tar.gz](https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx1150-10.0.0.tar.gz)

```
cd C:\TheRock
curl -o therock-dist-windows-gfx1152-10.0.0.tar.gz https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx1152-10.0.0.tar.gz
tar -xzf therock-dist-windows-gfx1152-10.0.0.tar.gz -C build --strip-components=1
```

Download link:

[therock-dist-windows-gfx1152-10.0.0.tar.gz](https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx1152-10.0.0.tar.gz)

```
cd C:\TheRock
curl -o therock-dist-windows-gfx1153-10.0.0.tar.gz https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx1153-10.0.0.tar.gz
tar -xzf therock-dist-windows-gfx1153-10.0.0.tar.gz -C build --strip-components=1
```

Download link:

[therock-dist-windows-gfx1153-10.0.0.tar.gz](https://stable.repo.amd.com/rocm/core/tarball/therock-dist-windows-gfx1153-10.0.0.tar.gz)

Install the `core`

ROCm components. See [ROCm meta components](https://rocm.docs.amd.com#rocm-install-runfile-meta-components) for additional installation options.

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=all gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx950 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx942 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx90a gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx908 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1201 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1200 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1100 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1101 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1102 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1103 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1030 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1151 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1150 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1152 gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1153 gpu-access=user
```

#### ROCm meta components[#](https://rocm.docs.amd.com#rocm-meta-components-i-pkgman-os-ubuntu-os-wsl-ubuntu-ver-26-04-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-24-04-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-22-04-5-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-debian-debian-ver-13-fam-all-fam-instinct-fam-radeon-fam-ryzen-debian-ver-12-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rhel-rhel-ver-10-2-rhel-ver-10-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-8-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-oracle-linux-oracle-linux-ver-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-9-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-8-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rocky-linux-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-sles-sles-ver-16-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-sles-ver-15-7-fam-all-fam-instinct-fam-radeon-fam-ryzen-i-pkgman-os-ubuntu-os-debian-os-wsl-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-i-pkgman-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-i-amdgpu-install-os-ubuntu-os-rhel-fam-radeon-fam-ryzen-fam-all-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-0-sles-ver-15-7-os-windows-i-pip-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-windows-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-windows-fam-all-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-i-runfile-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-i-runfile)

Meta components are similar to the meta packages used in the package manager installation method. They group related components and dependencies together, allowing you to install only what is necessary for your use case. The following table describes available ROCm meta components:

| Meta component name | Use case | Description | Contents |
|---|---|---|---|
| ROCm Base | Core runtime environment. Install this to run ROCm applications. | Runtimes, libraries, system control and monitoring tools, and other essential components. |
| ROCm Developer Essentials | Development environment. Install this to build ROCm applications. |
|
| ROCm Profiler | Install this to profile and optimize ROCm applications. | Profilers and related tools. |
| ROCm OpenCL | Install this to run OpenCL applications on ROCm. | Components needed to run OpenCL. |
| ROCm Full Suite | Install this if you need everything. | The complete ROCm Core SDK including runtimes, compilers, development tools, and dependencies. |

The default installation uses the core meta component. To select other
components, add the `compo=`

argument. For example, to install both `core`

and
`core-dev`

:

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx950 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx942 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx90a compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx908 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1201 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1200 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1100 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1101 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1102 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1103 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1030 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1151 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1150 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1152 compo=core,core-dev gpu-access=user
```

```
bash rocm-installer-10.0.0-4.run deps=install rocm gfx=gfx1153 compo=core,core-dev gpu-access=user
```

### Install ROCDXG and AMD SMI for WSL[#](https://rocm.docs.amd.com#install-rocdxg-and-amd-smi-for-wsl-i-pkgman-os-ubuntu-os-wsl-ubuntu-ver-26-04-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-24-04-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-ubuntu-ver-22-04-5-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-debian-debian-ver-13-fam-all-fam-instinct-fam-radeon-fam-ryzen-debian-ver-12-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rhel-rhel-ver-10-2-rhel-ver-10-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-fam-all-fam-instinct-fam-radeon-fam-ryzen-rhel-ver-8-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-oracle-linux-oracle-linux-ver-10-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-9-fam-all-fam-instinct-fam-radeon-fam-ryzen-oracle-linux-ver-8-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-rocky-linux-fam-all-fam-instinct-fam-radeon-fam-ryzen-os-sles-sles-ver-16-0-fam-all-fam-instinct-fam-radeon-fam-ryzen-sles-ver-15-7-fam-all-fam-instinct-fam-radeon-fam-ryzen-i-pkgman-os-ubuntu-os-debian-os-wsl-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-i-pkgman-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-fam-all-i-amdgpu-install-os-ubuntu-os-rhel-fam-radeon-fam-ryzen-fam-all-i-pip-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-4-ubuntu-ver-22-04-5-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-2-rhel-ver-10-0-rhel-ver-9-8-rhel-ver-9-6-rhel-ver-9-4-rhel-ver-8-10-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-0-sles-ver-15-7-os-windows-i-pip-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-windows-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-windows-fam-all-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-i-runfile-fam-all-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-i-runfile-gfx-gfx950-gfx-gfx942-gfx-gfx90a-gfx-gfx908-gfx-gfx1201-gfx-gfx1200-gfx-gfx1100-gfx-gfx1101-gfx-gfx1102-gfx-gfx1103-gfx-gfx1030-gfx-gfx1151-gfx-gfx1150-gfx-gfx1152-gfx-gfx1153-os-wsl)

Download and install ROCDXG Library.

wget https://github.com/ROCm/librocdxg/releases/download/v1.2.2/rocdxg-roct_1.2.2_amd64.deb sudo apt install ./rocdxg-roct_1.2.2_amd64.deb

Download and install AMD SMI Library for WSL.

sudo apt install python3-pip python3-wheel python3-argcomplete wget https://github.com/ROCm/librocdxg/releases/download/v1.2.2/rocdxg-amd-smi-lib_1.2.2_amd64.deb sudo apt install ./rocdxg-amd-smi-lib_1.2.2_amd64.deb source /etc/profile.d/rocdxg-amd-smi-lib.sh


In your host Windows environment, download and install the

[Windows SDK](https://learn.microsoft.com/en-us/windows/apps/windows-sdk/)for Windows 11. Make sure you have the necessary permissions to access the Windows SDK installation files from your WSL2 environment.In your WSL2 environment, clone the ROCDXG library.

git clone https://github.com/ROCm/librocdxg.git

Set

`WIN_SDK_PATH`

to the Windows SDK include directory for your installed version.# Set the Windows SDK path (adjust version number if different) export WIN_SDK_PATH="/mnt/c/Program Files (x86)/Windows Kits/10/Include/10.0.28000.0"

Build the ROCDXG Library using CMake.

cd librocdxg mkdir -p build cd build cmake .. -DWIN_SDK="${WIN_SDK_PATH}/shared" make sudo make install

Build the AMD SMI Library for WSL using CMake.

# Before proceeding, cd /path/to/librocdxg/ cd amdsmi cmake -B build -DWIN_SDK="${WIN_SDK_PATH}/shared" . cmake --build build sudo cmake --install build source /etc/profile.d/rocdxg-amd-smi-lib.sh


## Post-installation[#](https://rocm.docs.amd.com#post-installation)

After installing ROCm 10.0.0, complete these post-installation steps to complete your system configuration and validate the installation.

### Configure your environment[#](https://rocm.docs.amd.com#configure-your-environment-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-tar)

Configure environment variables so that ROCm libraries and tools are available either to all users on the system or only to your user account.

Create a profile script so that all users inherit the ROCm
environment variables when they start a shell session. Make sure
you’re in the `therock-tarball`

directory before proceeding.

```
# Configure ROCm PATH. Make sure you're in the therock-tarball directory before proceeding.
ROCM_INSTALL_PATH=$(pwd)/install
sudo tee /etc/profile.d/set-rocm-env.sh << EOF
export ROCM_PATH=$ROCM_INSTALL_PATH
export PATH=\$PATH:\$ROCM_PATH/bin
export LD_LIBRARY_PATH=\$ROCM_PATH/lib
EOF
sudo chmod +x /etc/profile.d/set-rocm-env.sh
source /etc/profile.d/set-rocm-env.sh
```

Configure the ROCm environment for your user by updating your shell startup configuration file.

Use the following commands to update your shell configuration file
(`~/.bashrc`

or `~/.profile`

) and add ROCm to your PATH. Before proceeding, make sure you’re in the
`therock-tarball`

directory so the install path resolves correctly.

```
# Configure ROCm PATH. Make sure you're in the therock-tarball directory before proceeding.
ROCM_INSTALL_PATH=$(pwd)/install
tee --append ~/.bashrc << EOF
# BEGIN ROCm environment configuration
export ROCM_PATH=$ROCM_INSTALL_PATH
export PATH=\$PATH:\$ROCM_PATH/bin
export LD_LIBRARY_PATH=\$ROCM_PATH/lib
# END ROCm environment configuration
EOF
source ~/.bashrc
```

```
# Configure ROCm PATH. Make sure you're in the therock-tarball directory before proceeding.
ROCM_INSTALL_PATH=$(pwd)/install
tee --append ~/.profile << EOF
# BEGIN ROCm environment configuration
export ROCM_PATH=$ROCM_INSTALL_PATH
export PATH=\$PATH:\$ROCM_PATH/bin
export LD_LIBRARY_PATH=\$ROCM_PATH/lib
# END ROCm environment configuration
EOF
source ~/.profile
```

### Configure your environment[#](https://rocm.docs.amd.com#configure-your-environment-os-windows-i-tar)

Configure environment variables so that ROCm libraries and tools are available on your Windows system.

**Run command prompt as an administrator**and set the following environment variables.setx HIP_DEVICE_LIB_PATH "C:\TheRock\build\lib\llvm\amdgcn\bitcode" /M setx HIP_PATH "C:\TheRock\build" /M setx HIP_PLATFORM "amd" /M setx LLVM_PATH "C:\TheRock\build\lib\llvm" /M

Add the following paths into the PATH environment variable.

setx PATH "%PATH%;C:\TheRock\build\bin;C:\TheRock\build\lib\llvm\bin" /M

Open a new command prompt window for the environment variables to take effect. Run

`set`

to see the list of active variables.`set`


### Verify your installation[#](https://rocm.docs.amd.com#verify-your-installation-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-tar-os-windows-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles)

Use the following ROCm tools to verify that ROCm is correctly installed and that your AMD devices are visible to the system.

Use

`rocminfo`

to list detected AMD GPUs and confirm that the ROCm runtimes and drivers are correctly installed and loaded.rocminfo

## Example output of

`rocminfo`

ROCk module version 6.16.6 is loaded ===================== HSA System Attributes ===================== Runtime Version: 1.21 Runtime Ext Version: 1.21 System Timestamp Freq.: 1000.000000MHz Sig. Max Wait Duration: 18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count) Machine Model: LARGE System Endianness: LITTLE Mwaitx: ENABLED XNACK enabled: NO DMAbuf Support: YES VMM Support: YES ========== HSA Agents ========== ******* Agent 1 ******* Name: gfx950 Uuid: GPU-5b920922d0067ea9 Marketing Name: AMD Instinct MI350X Vendor Name: AMD ... [output truncated]

Use the AMD SMI CLI

`amd-smi`

to validate system information.`amd-smi version`

## Example output of

`amd-smi version`

`AMDSMI Tool: 27.0.0+6b0e43f3 | AMDSMI Library version: 27.0.0 | ROCm version: 10.0.0 | amdgpu version: 7.1.3.31500000 | ionic version: N/A`


Inspect your installation in your Python environment and confirm that ROCm packages, including the

`rocm-sdk`

CLI, are available.pip freeze | grep rocm which rocm-sdk ls .venv/bin


### Verify your installation[#](https://rocm.docs.amd.com#verify-your-installation-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-tar-os-windows-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pip-os-windows)

Use the following ROCm tools to verify that ROCm is correctly installed and that your AMD devices are visible to the system.

Use

`hipinfo`

to list detected AMD GPUs and confirm that the ROCm runtimes and drivers are correctly installed and loaded.hipinfo

## Example output of

`hipinfo`

-------------------------------------------------------------------------------- device# 0 Name: AMD Radeon(TM) 8060S Graphics pciBusID: 197 pciDeviceID: 0 pciDomainID: 0 multiProcessorCount: 20 ... [output truncated]

Inspect your installation in your Python environment and confirm that ROCm packages, including the

`rocm-sdk`

CLI, are available.pip freeze where rocm-sdk dir .venv\Scripts


Use `hipinfo`

to list detected AMD GPUs and confirm that the ROCm
runtimes and drivers are correctly installed and loaded.

```
hipinfo
```

##
Example output of `hipinfo`


```
--------------------------------------------------------------------------------
device# 0
Name: AMD Radeon(TM) 8060S Graphics
pciBusID: 197
pciDeviceID: 0
pciDomainID: 0
multiProcessorCount: 20
... [output truncated]
```

### Verify your installation[#](https://rocm.docs.amd.com#verify-your-installation-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-tar-os-windows-i-tar-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pip-os-windows-i-pip-i-tar-os-wsl)

Use `rocminfo`

to verify that ROCm is correctly
installed and that your AMD devices are visible to the system.

```
rocminfo
```

##
Example output of `rocminfo`


```
WSL2 environment detected.
=====================
HSA System Attributes
=====================
Runtime Version: 1.21
Runtime Ext Version: 1.21
System Timestamp Freq.: 1000.000000MHz
Sig. Max Wait Duration: 18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model: LARGE
System Endianness: LITTLE
Mwaitx: DISABLED
XNACK enabled: NO
DMAbuf Support: YES
VMM Support: YES
==========
HSA Agents
==========
*******
Agent 1
*******
Name: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
Uuid: CPU-XX
Marketing Name: AMD RYZEN AI MAX+ 395 w/ Radeon 8060S
Vendor Name: CPU
Feature: None specified
Profile: FULL_PROFILE
Float Round Mode: NEAR
Max Queue Number: 0(0x0)
Queue Min Size: 0(0x0)
Queue Max Size: 0(0x0)
Queue Type: MULTI
Node: 0
Device Type: CPU
Cache Info:
L1: 49152(0xc000) KB
Chip ID: 0(0x0)
Cacheline Size: 64(0x40)
BDFID: 0
Internal Node ID: 0
Compute Unit: 32
SIMDs per CU: 0
Shader Engines: 0
Shader Arrs. per Eng.: 0
Memory Properties:
Features: None
Pool Info:
Pool 1
Segment: GLOBAL; FLAGS: FINE GRAINED
Size: 14123020(0xd7800c) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
Pool 2
Segment: GLOBAL; FLAGS: EXTENDED FINE GRAINED
Size: 14123020(0xd7800c) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
Pool 3
Segment: GLOBAL; FLAGS: KERNARG, FINE GRAINED
Size: 14123020(0xd7800c) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
Pool 4
Segment: GLOBAL; FLAGS: COARSE GRAINED
Size: 14123020(0xd7800c) KB
Allocatable: TRUE
Alloc Granule: 4KB
Alloc Recommended Granule:4KB
Alloc Alignment: 4KB
Accessible by all: TRUE
ISA Info:
*******
Agent 2
*******
Name: gfx1151
Uuid: GPU-ffffffffffffffff
Marketing Name: AMD Radeon(TM) 8060S Graphics
Vendor Name: AMD
... [output truncated]
```

### Configure your environment[#](https://rocm.docs.amd.com#configure-your-environment-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pip)

Note

Follow this step only if you installed the `devel`

package.

Initialize the ROCm SDK.

```
rocm-sdk init
```

### Test your installation[#](https://rocm.docs.amd.com#test-your-installation-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-pip-i-pip)

Run the following commands from your Python virtual environment to confirm that the ROCm SDK is correctly configured and that basic checks complete successfully.

```
rocm-sdk targets
rocm-sdk test
```

To learn more about the `rocm-sdk`

tool and to see example
outputs, see [Using ROCm Python packages (TheRock)](https://github.com/ROCm/TheRock/blob/main/RELEASES.md#using-rocm-python-packages).

### Test your installation[#](https://rocm.docs.amd.com#test-your-installation-os-windows-i-pip)

Run the following commands from your Python virtual environment to confirm that the ROCm SDK is correctly configured and that basic checks complete successfully.

```
rocm-sdk test
```

To learn more about the `rocm-sdk`

tool and to see example
outputs, see [Using ROCm Python packages (TheRock)](https://github.com/ROCm/TheRock/blob/main/RELEASES.md#using-rocm-python-packages).

Tip

If you need to deactivate your Python virtual environment when finished, run:

```
deactivate
```

See also

To install deep learning frameworks, including [PyTorch](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/pytorch/install.html)
and [JAX](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/jax/install.html),
and get started with AI training and inference, see the [AI Ecosystem](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/)
documentation portal.

To install deep learning frameworks, including [PyTorch](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/frameworks/pytorch/install.html),
and get started with AI training and inference, see the [AI Ecosystem](https://rocm.docs.amd.com/projects/ai-ecosystem/en/latest/)
documentation portal.

To learn about HPC libraries and applications, see
[ROCm HPC SDK](https://rocm.docs.amd.com/components/hpc-sdk/index.html).

To learn about ROCm Extras, which include supplementary tools for
benchmarking and validating, see [ROCm Extras](https://rocm.docs.amd.com/components/extras.html).

## Uninstalling[#](https://rocm.docs.amd.com#uninstalling)

Uninstall the librocdxg packages.

sudo apt purge rocdxg-amd-smi-lib rocdxg-roct sudo apt autoremove

Remove leftover librocdxg files.

sudo rm -rf /opt/rocm/core-10.0/lib/librocdxg.so* \ /opt/rocm/core-10.0/share/rocdxg \ /opt/rocm/core-10.0/share/doc/rocdxg

Use your package manager to remove the

[installed packages](https://rocm.docs.amd.com#rocm-install-rocm).sudo apt autoremove amdrocm10.0

sudo apt autoremove amdrocm10.0-gfx950

sudo apt autoremove amdrocm10.0-gfx942

sudo apt autoremove amdrocm10.0-gfx90a

sudo apt autoremove amdrocm10.0-gfx908

sudo apt autoremove amdrocm10.0-gfx1201

sudo apt autoremove amdrocm10.0-gfx1200

sudo apt autoremove amdrocm10.0-gfx1100

sudo apt autoremove amdrocm10.0-gfx1101

sudo apt autoremove amdrocm10.0-gfx1102

sudo apt autoremove amdrocm10.0-gfx1103

sudo apt autoremove amdrocm10.0-gfx1030

sudo apt autoremove amdrocm10.0-gfx1151

sudo apt autoremove amdrocm10.0-gfx1150

sudo apt autoremove amdrocm10.0-gfx1152

sudo apt autoremove amdrocm10.0-gfx1153

Remove ROCm repositories.

# Remove ROCm repositories sudo rm /etc/apt/sources.list.d/amdrocm-stable.sources # Clear the cache and clean the system sudo rm -rf /var/cache/apt/* sudo apt clean all sudo apt update


Use your package manager to remove the

[installed packages](https://rocm.docs.amd.com#rocm-install-rocm).sudo apt autoremove amdrocm10.0

sudo apt autoremove amdrocm10.0-gfx950

sudo apt autoremove amdrocm10.0-gfx942

sudo apt autoremove amdrocm10.0-gfx90a

sudo apt autoremove amdrocm10.0-gfx908

sudo apt autoremove amdrocm10.0-gfx1201

sudo apt autoremove amdrocm10.0-gfx1200

sudo apt autoremove amdrocm10.0-gfx1100

sudo apt autoremove amdrocm10.0-gfx1101

sudo apt autoremove amdrocm10.0-gfx1102

sudo apt autoremove amdrocm10.0-gfx1103

sudo apt autoremove amdrocm10.0-gfx1030

sudo apt autoremove amdrocm10.0-gfx1151

sudo apt autoremove amdrocm10.0-gfx1150

sudo apt autoremove amdrocm10.0-gfx1152

sudo apt autoremove amdrocm10.0-gfx1153

sudo dnf remove amdrocm10.0

sudo dnf remove amdrocm10.0-gfx950

sudo dnf remove amdrocm10.0-gfx94x

sudo dnf remove amdrocm10.0-gfx90a

sudo dnf remove amdrocm10.0-gfx908

sudo dnf remove amdrocm10.0-gfx120x

sudo dnf remove amdrocm10.0-gfx110x

sudo dnf remove amdrocm10.0-gfx103x

sudo dnf remove amdrocm10.0-gfx1151

sudo dnf remove amdrocm10.0-gfx1150

sudo dnf remove amdrocm10.0-gfx1152

sudo dnf remove amdrocm10.0-gfx1153

sudo zypper remove amdrocm*

Remove ROCm repositories.

# Remove ROCm repositories sudo rm -f /etc/apt/sources.list.d/amdrocm-stable.sources # Clear the cache and clean the system sudo rm -rf /var/cache/apt/* sudo apt clean all sudo apt update

# Remove ROCm repositories sudo rm -f /etc/yum.repos.d/amdrocm-stable.repo* # Clear the cache and clean the system sudo rm -rf /var/cache/dnf sudo dnf clean all

# Remove ROCm repositories sudo zypper removerepo "amdrocm-stable" # Clear the cache and clean the system sudo zypper clean --all sudo zypper refresh


Clear the pip cache.

rm -rf ~/.cache/pip

pip cache purge

Remove your local Python virtual environment.

rm -rf .venv

`rmdir /s /q .venv`


To uninstall ROCm, remove your installation directory.

Important

The following command assumes you’re working with the

`therock-tarball`

directory. If you chose a different directory name when[installing ROCm](https://rocm.docs.amd.com#rocm-install), adjust the command accordingly.sudo rm -rf therock-tarball

Remove your ROCm environment configuration from your system.

If you opted for a

[system-wide setup](https://rocm.docs.amd.com#rocm-post-install-env)during the installation process, remove the ROCm environment variables.sudo rm -f /etc/profile.d/set-rocm-env.sh

If you opted for a

[user-specific setup](https://rocm.docs.amd.com#rocm-post-install-env)during the installation process, remove the ROCm environment configuration block from your shell configuration file (`~/.bashrc`

or`~/.profile`

).

To uninstall ROCm, remove your installation directory.

`rmdir /s /q C:\TheRock`

Important

This step assumes you’re working with the

`C:\TheRock\build`

directory. If you chose a different directory name when[installing ROCm](https://rocm.docs.amd.com#rocm-install), adjust this step accordingly.**Run command prompt as an administrator**and delete the following environment variables.setx HIP_DEVICE_LIB_PATH "" /M setx HIP_PATH "" /M setx HIP_PLATFORM "" /M setx LLVM_PATH "" /M

Remove the following paths from your PATH environment variable using your system settings GUI. Navigate to the following screen:

Control Panel > System and Security > Edit environment variables


Edit the PATH variable and delete the following paths:

`C:\TheRock\build\bin`

`C:\TheRock\build\lib\llvm\bin`


To uninstall the Adrenalin Driver, see

[Uninstall AMD Software](https://www.amd.com/en/resources/support-articles/faqs/RSX2-UNINSTALL.html).

Use the following command to uninstall ROCm.

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=all

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx950

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx942

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx90a

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx908

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1201

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1200

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1100

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1101

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1102

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1103

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1030

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1151

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1150

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1152

bash rocm-installer-10.0.0-4.run uninstall-rocm gfx=gfx1153

Use the following command to uninstall the AMD GPU Driver (amdgpu).

bash rocm-installer-10.0.0-4.run uninstall-amdgpu


Use

`amdgpu-uninstall`

to remove the[installed packages](https://rocm.docs.amd.com#rocm-install-rocm).`sudo amdgpu-uninstall`


Use

`amdgpu-uninstall`

to remove the[installed packages](https://rocm.docs.amd.com#rocm-install-rocm).`sudo amdgpu-uninstall`


Use

`amdgpu-uninstall`

to remove the[installed packages](https://rocm.docs.amd.com#rocm-install-rocm).`sudo amdgpu-uninstall`


Remove ROCm repositories.

sudo apt purge amdgpu-install sudo apt autoremove # Clear the cache and clean the system sudo rm -rf /var/cache/apt/* sudo apt clean all sudo apt update

sudo dnf remove amdgpu-install # Clear the cache and clean the system sudo rm -rf /var/cache/dnf sudo dnf clean all