source: https://rocm.docs.amd.com/projects/MIOpen/en/latest

# MIOpen documentation[#](https://rocm.docs.amd.com#miopen-documentation)

MIOpen is the AMD open-source, deep-learning primitives library for GPUs. It implements fusion to optimize for memory bandwidth and GPU launch overheads, providing an auto-tuning infrastructure to overcome the large design space of problem configurations. It also implements different algorithms to optimize convolutions for different filter and input sizes.

MIOpen is one of the first libraries to publicly support the `bfloat16`

data type for convolutions, which
allows for efficient training at lower precision without loss of accuracy.

The MIOpen public repository is located at
[ROCm/rocm-libraries](https://github.com/ROCm/rocm-libraries/tree/develop/projects/miopen).

Note

The MIOpen repository for ROCm 6.4.3 and earlier is located at [ROCm/MIOpen](https://github.com/ROCm/MIOpen).

For information on contributing to the MIOpen code base, see
[Contributing to ROCm](https://rocm.docs.amd.com/en/latest/contribute/contributing.html).

For licensing information for all ROCm components, see
[ROCm licensing](https://rocm.docs.amd.com/en/latest/about/license.html).