source: https://rocm.docs.amd.com/projects/ROCgdb/en/latest

# ROCgdb documentation[#](https://rocm.docs.amd.com#rocgdb-documentation)

This is the documentation for AMD ROCm Debugger (ROCgdb) for Linux, which is the AMD source-level debugger based on the [GNU Debugger (GDB)](https://www.sourceware.org/gdb/documentation/). For documentation on ROCgdb for Windows, see [AMD ROCm debugger for Windows](https://rocm.docs.amd.com/projects/install-on-windows/en/latest/how-to/debugger-windows.html). ROCgdb enables heterogeneous debugging on the ROCm software that consists of an x86-based host architecture along with
commercially available AMD GPU architectures supported by the [AMD Debugger API
Library (ROCdbgapi)](https://rocm.docs.amd.com/projects/ROCdbgapi/en/latest/index.html). ROCdbgapi is included with ROCm.

ROCgdb provides the following features:

Debugs ROCm applications running on AMD GPU-supported hardware.

Debugs applications without the potential variations introduced by simulation and emulation environments.

Offers a seamless debugging environment that allows simultaneous GPU and CPU code debugging within the same application, just like programming in

[HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html), which is a seamless extension of C++ programming.Additional features to support debugging ROCm device code on top of the existing GDB debugging features, which are inherently present for debugging the host code.

Supports

[HIP](https://rocm.docs.amd.com/projects/HIP/en/latest/index.html)kernel debugging.Allows you to set breakpoints, single-step ROCm applications, and inspect and modify the memory and variables of any given thread running on the hardware.


The code is open source and hosted at: [ROCm/ROCgdb](https://github.com/ROCm/ROCgdb)

To contribute to the documentation, refer to
[Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

You can find licensing information on the [Licensing](https://rocm.docs.amd.com/en/latest/about/license.html) page.