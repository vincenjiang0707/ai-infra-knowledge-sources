source: https://docs.nvidia.com/deploy/cuda-compatibility/why-cuda-compatibility.html

# Why CUDA Compatibility[#](https://docs.nvidia.com#why-cuda-compatibility)

The NVIDIA® CUDA® Toolkit enables developers to build NVIDIA GPU accelerated compute applications for desktop computers, enterprise, and data centers to hyperscalers. It consists of the CUDA compiler toolchain including the CUDA runtime (cudart) and various CUDA libraries and tools. To build an application, a developer has to install only the CUDA Toolkit and necessary libraries required for linking.

In order to run a CUDA application, the system should have a CUDA enabled GPU and an NVIDIA driver that is compatible with the CUDA Toolkit that was used to build the application itself. If the application relies on dynamic linking for libraries, then the system should have the right version of such libraries as well.

Prior to CUDA 13.4, every CUDA Toolkit also shipped with an NVIDIA driver package for convenience, and that driver supported all the features introduced in that version of the CUDA Toolkit. Starting with CUDA 13.4, the NVIDIA Linux driver is distributed separately and is no longer bundled with the CUDA Toolkit; the CUDA driver must now be obtained separately. Please check the toolkit and driver version requirements in the applicable [CUDA Toolkit Release Notes](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/). The driver package includes both the user mode CUDA driver (`libcuda.so`

) and kernel mode components necessary to run the application.

Typically, upgrading a CUDA Toolkit involves upgrading both the toolkit and the driver to get up to date toolkit and driver capabilities.

As you can see, when the NVIDIA driver is upgraded along with the CUDA Toolkit, the `CUDA Driver`

and `CUDA Runtime`

versions in the sample output of `deviceQuery`

match perfectly:

```
$ ./deviceQuery
./deviceQuery Starting...
CUDA Device Query (Runtime API) version (CUDART static linking)
Detected 1 CUDA Capable device(s)
Device 0: "NVIDIA GeForce RTX 4070 SUPER"
CUDA Driver Version / Runtime Version 13.4 / 13.4
CUDA Capability Major/Minor version number: 8.9
[...]
deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 13.4, CUDA Runtime Version = 13.4, NumDevs = 1
Result = PASS
```

This is not always required. CUDA Compatibility guarantees allow for upgrading only certain components:

Backwards compatibility ensures that a newer NVIDIA driver can be used with an older CUDA Toolkit. This is implicit and most simple way of doing upgrades.

Minor version and forward compatibility ensure that an older NVIDIA driver can be used with a newer CUDA Toolkit.


Applications that directly rely only on the CUDA runtime can be deployed in the following scenarios:

CUDA driver (libcuda.so) |
Compatibility type |
Requirements |
|---|---|---|
|
Backwards compatibility |
None |
|
No PTX (requires SASS), NVCC target architecture required |
|
|
Extra CUDA compatibility package |