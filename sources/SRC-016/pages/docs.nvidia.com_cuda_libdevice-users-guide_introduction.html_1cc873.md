source: https://docs.nvidia.com/cuda/libdevice-users-guide/introduction.html

#
1. Introduction[](https://docs.nvidia.com#introduction)

##
1.1. What Is libdevice?[](https://docs.nvidia.com#what-is-libdevice)

The libdevice library is a collection of NVVM bitcode functions that implement common functions for NVIDIA GPU devices, including math primitives and bit-manipulation functions. These functions are optimized for particular GPU architectures, and are intended to be linked with an NVVM IR module during compilation to PTX.

This guide documents both the functions available in libdevice and the basic usage of the library from a compiler writer’s perspective.