source: https://rocm.docs.amd.com/projects/hipFile/en/latest

# hipFile documentation[#](https://rocm.docs.amd.com#hipfile-documentation)

hipFile is AMD’s Infinity Storage library that provides direct-to-GPU I/O without requiring a host-side buffer. The library provides C and Python APIs for synchronous, asynchronous, and batch I/O operations. hipFile automatically falls back to POSIX I/O when operations are unable to use the direct-to-GPU path.

hipFile is delivered as part of [TheRock](https://github.com/ROCm/TheRock). The hipFile source code is located at [ROCm/rocm-systems](https://github.com/ROCm/rocm-systems/tree/develop/projects/hipfile).

Troubleshooting

Licensing information is in the [LICENSE.md](https://github.com/ROCm/rocm-systems/blob/develop/projects/hipfile/LICENSE.md) file in the repository.