source: https://rocm.docs.amd.com/en/latest/install/asan.html

# Install AMD ROCm with ASAN[#](https://rocm.docs.amd.com#install-amd-rocm-with-asan)

ASAN (AddressSanitizer) builds of ROCm are available for specific AMD Instinct GPU architectures and can be installed using the package manager or a tarball.

Important

ASAN builds are only available for

`gfx942`

and`gfx950`

architectures, plus a multiarch build (`all`

, both gfx942 and gfx950).ASAN rpm and debian packages use the naming convention

`amdrocm-asan10.0`

or`amdrocm-asan10.0-gfxXYZ`

.ASAN rpm and debian packages install to

`/opt/rocm/core-asan-10.0`

, separate from regular ROCm installations at`/opt/rocm/core-10.0`

.ASAN packages are approximately 4× larger than a standard ROCm installation due to debug symbols and ASAN instrumentation.


Use the following selector to choose your GPU architecture, operating system, and installation method.

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

Before installing ROCm ASAN, make sure your system meets the ROCm hardware, software, and driver requirements. For more information, see [Install AMD ROCm](https://rocm.docs.amd.com/rocm.html).

For system requirements and support information, see the [Compatibility matrix](https://rocm.docs.amd.com/compatibility/compatibility-matrix.html).

## Install ROCm ASAN[#](https://rocm.docs.amd.com#install-rocm-asan)

Use the following instructions to install ROCm ASAN packages on your system.

### Register ROCm repositories[#](https://rocm.docs.amd.com#register-rocm-repositories-i-pkgman)

Complete the ROCm installation prerequisites to install dependencies and configure GPU access permissions before proceeding.

```
# Download and install GPG key
sudo mkdir --parents --mode=0755 /etc/apt/keyrings
wget https://stable.repo.amd.com/rocm/gpg/packages.gpg -O - | \
gpg --dearmor | sudo tee /etc/apt/keyrings/amdrocm.gpg > /dev/null
sudo tee /etc/apt/sources.list.d/amdrocm-stable-asan.sources << EOF
X-Repo-Id: amdrocm-stable-asan
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages-asan/ubuntu2604/
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
sudo tee /etc/apt/sources.list.d/amdrocm-stable-asan.sources << EOF
X-Repo-Id: amdrocm-stable-asan
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages-asan/ubuntu2404/
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
sudo tee /etc/apt/sources.list.d/amdrocm-stable-asan.sources << EOF
X-Repo-Id: amdrocm-stable-asan
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages-asan/ubuntu2204/
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
sudo tee /etc/apt/sources.list.d/amdrocm-stable-asan.sources << EOF
X-Repo-Id: amdrocm-stable-asan
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages-asan/debian13/
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
sudo tee /etc/apt/sources.list.d/amdrocm-stable-asan.sources << EOF
X-Repo-Id: amdrocm-stable-asan
Types: deb
URIs: https://stable.repo.amd.com/rocm/core/packages-asan/debian12/
Suites: stable
Components: main
Architectures: amd64
Signed-By: /etc/apt/keyrings/amdrocm.gpg
Enabled: yes
EOF
sudo apt update
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/rhel10/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/rhel8/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/rhel10/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/rhel8/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/yum.repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/rhel9/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo dnf clean all
```

```
sudo tee /etc/zypp/repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/sles16/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo zypper --gpg-auto-import-keys refresh
```

```
sudo tee /etc/zypp/repos.d/amdrocm-stable-asan.repo <<EOF
[amdrocm-stable-asan]
name=ROCm 10.0.0 asan
baseurl=https://stable.repo.amd.com/rocm/core/packages-asan/sles15/x86_64
enabled=1
gpgcheck=1
gpgkey=https://stable.repo.amd.com/rocm/gpg/packages.gpg
EOF
sudo zypper --gpg-auto-import-keys refresh
```

### Install ROCm ASAN packages[#](https://rocm.docs.amd.com#install-rocm-asan-packages-i-pkgman-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-ubuntu-ver-22-04-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-rhel-ver-9-rhel-ver-8-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-sles-ver-15-i-pkgman)

After registering the repository, install ROCm ASAN packages for your target
GPU architecture. See [ROCm ASAN meta packages](https://rocm.docs.amd.com#rocm-asan-install-meta-packages) for additional installation options.

```
sudo apt install amdrocm-asan10.0
```

```
sudo apt install amdrocm-asan10.0-gfx942
```

```
sudo apt install amdrocm-asan10.0-gfx950
```

```
sudo dnf install amdrocm-asan10.0
```

```
sudo dnf install amdrocm-asan10.0-gfx942
```

```
sudo dnf install amdrocm-asan10.0-gfx950
```

```
sudo zypper install amdrocm-asan10.0
```

```
sudo zypper install amdrocm-asan10.0-gfx942
```

```
sudo zypper install amdrocm-asan10.0-gfx950
```

#### ROCm ASAN meta packages[#](https://rocm.docs.amd.com#rocm-asan-meta-packages-i-pkgman-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-ubuntu-ver-22-04-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-rhel-ver-9-rhel-ver-8-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-sles-ver-15-i-pkgman-os-ubuntu-os-debian-fam-all-gfx-gfx942-gfx-gfx950-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx942-gfx-gfx950-os-sles-fam-all-gfx-gfx942-gfx-gfx950-i-pkgman)

Meta packages group related components and dependencies together, allowing you to install only what is necessary for your use case. The following table describes available ROCm ASAN meta packages:

Meta package name |
Use case |
Description |
Contents |
|---|---|---|---|
|
ROCm Base |
Core runtime environment. Install this to run ROCm applications with ASAN instrumentation. |
Runtimes, libraries, system control and monitoring tools, and other essential components with ASAN. |
|
ROCm Developer Essentials |
Development environment. Install this to build ROCm applications with ASAN support. |
|
|
ROCm Profiler |
Install this to profile and optimize ROCm applications with ASAN. |
Profilers and related tools with ASAN instrumentation. |
|
ROCm OpenCL |
Install this to run OpenCL applications on ROCm with ASAN. |
Components needed to run OpenCL with ASAN. |
|
ROCm Full Suite |
Install this if you need everything with ASAN. |
The complete ROCm Core SDK including runtimes, compilers, development tools, and dependencies with ASAN. |

Meta package name |
Use case |
Description |
Contents |
|---|---|---|---|
|
ROCm Base |
Core runtime environment. Install this to run ROCm applications with ASAN instrumentation. |
Runtimes, libraries, system control and monitoring tools, and other essential components with ASAN. |
|
ROCm Developer Essentials |
Development environment. Install this to build ROCm applications with ASAN support. |
|
|
ROCm Profiler |
Install this to profile and optimize ROCm applications with ASAN. |
Profilers and related tools with ASAN instrumentation. |
|
ROCm OpenCL |
Install this to run OpenCL applications on ROCm with ASAN. |
Components needed to run OpenCL with ASAN. |
|
ROCm Full Suite |
Install this if you need everything with ASAN. |
The complete ROCm Core SDK including runtimes, compilers, development tools, and dependencies with ASAN. |

Note

All ASAN meta packages follow the naming convention
`amdrocm-<component>-asan10.0`

or `amdrocm-<component>-asan10.0-gfx<XYZ>`

for architecture-specific builds.

### Create the installation directory[#](https://rocm.docs.amd.com#create-the-installation-directory-i-pkgman-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-ubuntu-ver-22-04-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-rhel-ver-9-rhel-ver-8-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-sles-ver-15-i-pkgman-os-ubuntu-os-debian-fam-all-gfx-gfx942-gfx-gfx950-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx942-gfx-gfx950-os-sles-fam-all-gfx-gfx942-gfx-gfx950-i-pkgman-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-ubuntu-os-debian-i-tar)

Run the following command in your desired location to create your installation directory:

```
mkdir therock-tarball-asan && cd therock-tarball-asan
```

Important

Subsequent commands assume you’re working with the `therock-tarball-asan`

directory. If you choose a different directory name, adjust the commands
accordingly.

### Download and unpack the tarball[#](https://rocm.docs.amd.com#download-and-unpack-the-tarball-i-pkgman-os-ubuntu-ubuntu-ver-26-04-ubuntu-ver-24-04-ubuntu-ver-22-04-os-debian-debian-ver-13-debian-ver-12-os-rhel-rhel-ver-10-rhel-ver-9-rhel-ver-8-os-oracle-linux-oracle-linux-ver-10-oracle-linux-ver-9-oracle-linux-ver-8-os-rocky-linux-os-sles-sles-ver-16-sles-ver-15-i-pkgman-os-ubuntu-os-debian-fam-all-gfx-gfx942-gfx-gfx950-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx942-gfx-gfx950-os-sles-fam-all-gfx-gfx942-gfx-gfx950-i-pkgman-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-os-ubuntu-os-debian-i-tar-i-tar)

Use the following commands to download and untar the ROCm ASAN tarball for your target GPU architecture.

```
wget https://stable.repo.amd.com/rocm/core/tarball-asan/therock-dist-linux-multiarch-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

```
wget https://stable.repo.amd.com/rocm/core/tarball-asan/therock-dist-linux-gfx94X-dcgpu-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

```
wget https://stable.repo.amd.com/rocm/core/tarball-asan/therock-dist-linux-gfx950-dcgpu-10.0.0.tar.gz
mkdir install
tar -xf *.tar.gz -C install
```

## Post-installation[#](https://rocm.docs.amd.com#post-installation)

After installing ROCm ASAN 10.0.0, complete these post-installation steps to configure your system and validate the installation.

### Configure your environment[#](https://rocm.docs.amd.com#configure-your-environment-i-pkgman-i-tar)

Configure environment variables so that ROCm ASAN libraries and tools are available either to all users on the system or only to your user account.

Create a profile script so that all users inherit the ROCm ASAN
environment variables when they start a shell session. Make sure
you’re in the `therock-tarball-asan`

directory before proceeding.

```
# Configure ROCM_ASAN_PATH to the ASan install tree (tarball extract path)
ROCM_ASAN_INSTALL_PATH=$(pwd)/install
sudo tee /etc/profile.d/set-rocm-asan-env.sh << EOF
# ROCm ASan Configuration
export ROCM_ASAN_PATH=$ROCM_ASAN_INSTALL_PATH
# Add ROCm bin to PATH
export PATH=\$PATH:\$ROCM_ASAN_PATH/bin
# Enable XNACK for device-side GPU instrumentation
# Without this, only host-side (CPU) errors will be detected
export HSA_XNACK=1
# Locate ASan runtime directory and append instrumented library directories
ASAN_LIB_PATH=\$(amdclang --print-file-name=libclang_rt.asan-x86_64.so 2>/dev/null || echo "")
export LD_LIBRARY_PATH="\$LD_LIBRARY_PATH:\${ASAN_LIB_PATH%/*}:\${ROCM_ASAN_PATH}/lib:\${ROCM_ASAN_PATH}/lib/llvm/lib:\${ROCM_ASAN_PATH}/lib/rocm_sysdeps/lib/"
export ASAN_LIB_NAME=libclang_rt.asan-x86_64.so
export LD_PRELOAD="\${ASAN_LIB_PATH%/*}/\$ASAN_LIB_NAME:\${ROCM_ASAN_PATH}/lib/libamdhip64.so:\${ROCM_ASAN_PATH}/lib/libhsa-runtime64.so"
EOF
sudo chmod +x /etc/profile.d/set-rocm-asan-env.sh
source /etc/profile.d/set-rocm-asan-env.sh
```

Create a profile script so that all users inherit the ROCm ASAN environment variables when they start a shell session.

```
# Configure ROCM_ASAN_PATH to the ASan install tree
sudo tee /etc/profile.d/set-rocm-asan-env.sh << 'EOF'
# ROCm ASan Configuration
export ROCM_ASAN_PATH=/opt/rocm/core-asan-10.0
# Enable XNACK for device-side GPU instrumentation
# Without this, only host-side (CPU) errors will be detected
export HSA_XNACK=1
# Locate ASan runtime directory and append instrumented library directories
ASAN_LIB_PATH=$(amdclang --print-file-name=libclang_rt.asan-x86_64.so 2>/dev/null || echo "")
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${ASAN_LIB_PATH%/*}:${ROCM_ASAN_PATH}/lib:${ROCM_ASAN_PATH}/lib/llvm/lib:${ROCM_ASAN_PATH}/lib/rocm_sysdeps/lib/"
export ASAN_LIB_NAME=libclang_rt.asan-x86_64.so
export LD_PRELOAD="${ASAN_LIB_PATH%/*}/$ASAN_LIB_NAME:${ROCM_ASAN_PATH}/lib/libamdhip64.so:${ROCM_ASAN_PATH}/lib/libhsa-runtime64.so"
EOF
sudo chmod +x /etc/profile.d/set-rocm-asan-env.sh
source /etc/profile.d/set-rocm-asan-env.sh
```

Configure the ROCm ASAN environment for your user by updating your shell startup configuration file.

Use the following commands to update your shell configuration file
(`~/.bashrc`

or `~/.profile`

) and add ROCm ASAN to your PATH.
Before proceeding, make sure you’re in the `therock-tarball-asan`

directory so the install path resolves correctly.

Use the following commands to update your shell configuration file
(`~/.bashrc`

or `~/.profile`

) and add ROCm ASAN to your PATH.

```
# Configure ROCM_ASAN_PATH to the ASan install tree (tarball extract path)
ROCM_ASAN_INSTALL_PATH=$(pwd)/install
tee --append ~/.bashrc << EOF
# BEGIN ROCm ASan Configuration
export ROCM_ASAN_PATH=$ROCM_ASAN_INSTALL_PATH
# Add ROCm bin to PATH
export PATH=\$PATH:\$ROCM_ASAN_PATH/bin
# Enable XNACK for device-side GPU instrumentation
# Without this, only host-side (CPU) errors will be detected
export HSA_XNACK=1
# Locate ASan runtime directory and append instrumented library directories
ASAN_LIB_PATH=\$(amdclang --print-file-name=libclang_rt.asan-x86_64.so 2>/dev/null || echo "")
export LD_LIBRARY_PATH="\$LD_LIBRARY_PATH:\${ASAN_LIB_PATH%/*}:\${ROCM_ASAN_PATH}/lib:\${ROCM_ASAN_PATH}/lib/llvm/lib:\${ROCM_ASAN_PATH}/lib/rocm_sysdeps/lib/"
export ASAN_LIB_NAME=libclang_rt.asan-x86_64.so
export LD_PRELOAD="\${ASAN_LIB_PATH%/*}/\$ASAN_LIB_NAME:\${ROCM_ASAN_PATH}/lib/libamdhip64.so:\${ROCM_ASAN_PATH}/lib/libhsa-runtime64.so"
# END ROCm ASan Configuration
EOF
source ~/.bashrc
```

```
# Configure ROCM_ASAN_PATH to the ASan install tree
tee --append ~/.bashrc << 'EOF'
# BEGIN ROCm ASan Configuration
export ROCM_ASAN_PATH=/opt/rocm/core-asan-10.0
# Enable XNACK for device-side GPU instrumentation
# Without this, only host-side (CPU) errors will be detected
export HSA_XNACK=1
# Locate ASan runtime directory and append instrumented library directories
ASAN_LIB_PATH=$(amdclang --print-file-name=libclang_rt.asan-x86_64.so 2>/dev/null || echo "")
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${ASAN_LIB_PATH%/*}:${ROCM_ASAN_PATH}/lib:${ROCM_ASAN_PATH}/lib/llvm/lib:${ROCM_ASAN_PATH}/lib/rocm_sysdeps/lib/"
export ASAN_LIB_NAME=libclang_rt.asan-x86_64.so
export LD_PRELOAD="${ASAN_LIB_PATH%/*}/$ASAN_LIB_NAME:${ROCM_ASAN_PATH}/lib/libamdhip64.so:${ROCM_ASAN_PATH}/lib/libhsa-runtime64.so"
# END ROCm ASan Configuration
EOF
source ~/.bashrc
```

```
# Configure ROCM_ASAN_PATH to the ASan install tree (tarball extract path)
ROCM_ASAN_INSTALL_PATH=$(pwd)/install
tee --append ~/.profile << EOF
# BEGIN ROCm ASan Configuration
export ROCM_ASAN_PATH=$ROCM_ASAN_INSTALL_PATH
# Add ROCm bin to PATH
export PATH=\$PATH:\$ROCM_ASAN_PATH/bin
# Enable XNACK for device-side GPU instrumentation
# Without this, only host-side (CPU) errors will be detected
export HSA_XNACK=1
# Locate ASan runtime directory and append instrumented library directories
ASAN_LIB_PATH=\$(amdclang --print-file-name=libclang_rt.asan-x86_64.so 2>/dev/null || echo "")
export LD_LIBRARY_PATH="\$LD_LIBRARY_PATH:\${ASAN_LIB_PATH%/*}:\${ROCM_ASAN_PATH}/lib:\${ROCM_ASAN_PATH}/lib/llvm/lib:\${ROCM_ASAN_PATH}/lib/rocm_sysdeps/lib/"
export ASAN_LIB_NAME=libclang_rt.asan-x86_64.so
export LD_PRELOAD="\${ASAN_LIB_PATH%/*}/\$ASAN_LIB_NAME:\${ROCM_ASAN_PATH}/lib/libamdhip64.so:\${ROCM_ASAN_PATH}/lib/libhsa-runtime64.so"
# END ROCm ASan Configuration
EOF
source ~/.profile
```

```
# Configure ROCM_ASAN_PATH to the ASan install tree
tee --append ~/.profile << 'EOF'
# BEGIN ROCm ASan Configuration
export ROCM_ASAN_PATH=/opt/rocm/core-asan-10.0
# Enable XNACK for device-side GPU instrumentation
# Without this, only host-side (CPU) errors will be detected
export HSA_XNACK=1
# Locate ASan runtime directory and append instrumented library directories
ASAN_LIB_PATH=$(amdclang --print-file-name=libclang_rt.asan-x86_64.so 2>/dev/null || echo "")
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${ASAN_LIB_PATH%/*}:${ROCM_ASAN_PATH}/lib:${ROCM_ASAN_PATH}/lib/llvm/lib:${ROCM_ASAN_PATH}/lib/rocm_sysdeps/lib/"
export ASAN_LIB_NAME=libclang_rt.asan-x86_64.so
export LD_PRELOAD="${ASAN_LIB_PATH%/*}/$ASAN_LIB_NAME:${ROCM_ASAN_PATH}/lib/libamdhip64.so:${ROCM_ASAN_PATH}/lib/libhsa-runtime64.so"
# END ROCm ASan Configuration
EOF
source ~/.profile
```

### Verify your installation[#](https://rocm.docs.amd.com#verify-your-installation)

Use the following ROCm tools to verify that ROCm ASAN is correctly installed and that your AMD devices are visible to the system.

Use `rocminfo`

to list detected AMD GPUs and confirm that the ROCm runtimes
and drivers are correctly installed and loaded:

```
rocminfo
```

Use the AMD SMI CLI `amd-smi`

to validate system information:

```
amd-smi version
```

## Uninstall ROCm ASAN[#](https://rocm.docs.amd.com#uninstall-rocm-asan)

### Uninstall ROCm ASAN packages[#](https://rocm.docs.amd.com#uninstall-rocm-asan-packages-i-pkgman)

Use your package manager to remove the installed packages.

sudo apt autoremove amdrocm-asan10.0

sudo apt autoremove amdrocm-asan10.0-gfx942

sudo apt autoremove amdrocm-asan10.0-gfx950

sudo dnf remove amdrocm-asan10.0

sudo dnf remove amdrocm-asan10.0-gfx942

sudo dnf remove amdrocm-asan10.0-gfx950

sudo zypper remove amdrocm-*-asan10.0*

Remove ROCm repositories.

sudo rm -f /etc/apt/sources.list.d/amdrocm-stable-asan.sources # Clear the cache and clean the system sudo rm -rf /var/cache/apt/* sudo apt clean all sudo apt update

sudo rm -f /etc/yum.repos.d/amdrocm-stable-asan.repo* # Clear the cache and clean the system sudo rm -rf /var/cache/dnf sudo dnf clean all

sudo zypper removerepo "amdrocm-stable-asan" # Clear the cache and clean the system sudo zypper clean --all sudo zypper refresh

Remove the ROCm environment variables from your configuration.

sudo rm -f /etc/profile.d/set-rocm-asan-env.sh

Remove the ROCm environment configuration block from your shell configuration file (

`~/.bashrc`

or`~/.profile`

).

### Uninstall the ROCm ASAN tarball[#](https://rocm.docs.amd.com#uninstall-the-rocm-asan-tarball-i-pkgman-os-ubuntu-os-debian-fam-all-gfx-gfx942-gfx-gfx950-os-rhel-os-oracle-linux-os-rocky-linux-fam-all-gfx-gfx942-gfx-gfx950-os-sles-os-ubuntu-os-debian-os-rhel-os-oracle-linux-os-rocky-linux-os-sles-i-tar)

Remove the directory containing the ROCm ASAN installation:

Important

The following command assumes you’re working with the

`therock-tarball-asan`

directory. If you chose a different directory name when[installing ROCm](https://rocm.docs.amd.com#rocm-asan-install-rocm), adjust the command accordingly.rm -rf therock-tarball-asan

Remove the ROCm environment variables from your configuration.

sudo rm -f /etc/profile.d/set-rocm-asan-env.sh

Remove the ROCm environment configuration block from your shell configuration file (

`~/.bashrc`

or`~/.profile`

).

## Next steps[#](https://rocm.docs.amd.com#next-steps)

To run applications with ASAN instrumentation, ensure the following:

Linux kernel ≥ 5.6 with HMM enabled

`HSA_XNACK=1`

`-fsanitize=address`

Instrumented runtimes


For more information, see the [GPU sanitizer guide](https://github.com/ROCm/TheRock/blob/main/docs/development/sanitizers.md#using-asan-instrumented-libraries).