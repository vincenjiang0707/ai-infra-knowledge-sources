source: https://rocm.docs.amd.com/en/latest/install/build-from-source.html

# Build the ROCm Core SDK from source[#](https://rocm.docs.amd.com#build-the-rocm-core-sdk-from-source)

You can build the ROCm Core SDK from source using the open-source unified build
system [TheRock](https://github.com/ROCm/TheRock). To learn more about the
motivation and architecture behind this system, see [ROCm Technology Preview:
ROCm Core SDK and TheRock Build System](https://rocm.blogs.amd.com/software-tools-optimization/therock/README.html).

This page consists mainly of references to [TheRock’s README](https://github.com/ROCm/TheRock?tab=readme-ov-file#building-from-source)
and [supporting development manuals](https://github.com/ROCm/TheRock/blob/main/README.md#development-manuals),
which provide up-to-date build instructions and guidance for supported
platforms. See [TheRock Development Guide](https://github.com/ROCm/TheRock/blob/main/docs/development/development_guide.md#therock-development-guide)
to learn about the overall build architecture.

Tip

Building from source is recommended only if you need custom builds or are
contributing to ROCm development.
For most users, installing from official AMD releases is faster and easier.
See [Install AMD ROCm 10.0.0](https://rocm.docs.amd.com/rocm.html) for installation instructions.

## Prerequisites[#](https://rocm.docs.amd.com#prerequisites)

A successful build depends on a correctly configured environment. Before you begin, ensure your system meets all hardware and software requirements. Review the following resources:

## High-level build process[#](https://rocm.docs.amd.com#high-level-build-process)

For an overview of the build architecture, start with TheRock’s [development guide](https://github.com/ROCm/TheRock/blob/main/docs/development/development_guide.md).
While specific commands vary by platform, the general workflow for building
from source involves these stages:

Clone the repository and install build dependencies. See

[Platform-specific setup](https://rocm.docs.amd.com#build-from-src-plat-setup).Configure the build: Use CMake feature flags to configure the build. This step allows you to target specific platforms, build subsets of ROCm Core SDK components, and toggle component features. See

[Build configuration](https://github.com/ROCm/TheRock/blob/main/README.md#build-configuration)for optional and required build flags.Execute the build: Run the build command to compile the source code. This can be a time- and resource-intensive process. See

[CMake build usage](https://github.com/ROCm/TheRock/blob/main/README.md#cmake-build-usage).After a successful build, the outputs are available for use in downstream tasks. To learn more about build outputs, see the relevant

[TheRock documentation](https://github.com/ROCm/TheRock/blob/main/docs/development/artifacts.md). Common post-build tasks include:Using

`build/dist/rocm`

: When the build completes, you should have a build of ROCm in the`build/dist/rocm/`

directory. See[Using installed tarballs](https://github.com/ROCm/TheRock/blob/main/RELEASES.md#using-installed-tarballs)for more information.Building Python packages: Prepare the build artifacts for distribution as Python packages. See

[Building Python packages](https://github.com/ROCm/TheRock/blob/main/docs/packaging/python_packaging.md#building-packages).Building PyTorch: Build a compatible PyTorch version against ROCm wheels. See the

[PyTorch build instructions](https://github.com/ROCm/TheRock/tree/main/external-builds/pytorch#build-instructions).


## Platform-specific setup[#](https://rocm.docs.amd.com#platform-specific-setup)

### ManyLinux[#](https://rocm.docs.amd.com#manylinux)

On Linux, it’s recommended to build with ManyLinux to produce binaries that are
portable across Ubuntu and other Linux distributions. To learn more about what
a ROCm ManyLinux build entails, see [ManyLinux builds](https://github.com/ROCm/TheRock/blob/main/docs/design/manylinux_builds.md).
Refer to [ManyLinux x86_64](https://github.com/ROCm/TheRock/blob/main/docs/environment_setup_guide.md#manylinux-x86-64)
in the environment setup guide.

### Ubuntu 24.04[#](https://rocm.docs.amd.com#ubuntu-24-04)

TheRock provides detailed instructions and scripts for preparing an Ubuntu
24.04 system, including installing necessary packages via apt.
Refer to [Setup — Ubuntu 24.04](https://github.com/ROCm/TheRock?tab=readme-ov-file#setup---ubuntu-2404)
in the TheRock repository for guidance.

### Windows 11[#](https://rocm.docs.amd.com#windows-11)

For setup instructions on Windows 11 using Visual Studio 2022, see
[Setup — Windows 11](https://github.com/ROCm/TheRock?tab=readme-ov-file#setup---windows-11-vs-2022)
in the TheRock repository.

See also

For details on supported configurations, known issues, and other
Windows-specific considerations, review the [Windows support](https://github.com/ROCm/TheRock/blob/main/docs/development/windows_support.md)
documentation.