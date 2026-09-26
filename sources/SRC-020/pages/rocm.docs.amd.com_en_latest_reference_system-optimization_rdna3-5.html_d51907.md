source: https://rocm.docs.amd.com/en/latest/reference/system-optimization/rdna3-5.html

# AMD RDNA3.5 system optimization[#](https://rocm.docs.amd.com#amd-rdna3-5-system-optimization)

This topic describes how to optimize systems powered by AMD Ryzen APUs with RDNA3.5 architecture. These APUs combine high-performance CPU cores with integrated RDNA3.5 graphics, and support LPDDR5X-8000 or DDR5 memory, making them particularly well-suited for:

LLM development and inference systems

High-performance workstations

Virtualization hosts running multiple VMs

GPU compute and parallel processing

Gaming systems

Home servers and AI development platforms


## Memory settings[#](https://rocm.docs.amd.com#memory-settings)

AMD Ryzen APUs with RDNA3.5 architecture (gfx1150, gfx1151, and gfx1152 LLVM targets) handle memory access through GPU Virtual Memory (GPUVM), which provides per-process GPU virtual address spaces (VMIDs) rather than a separate, discrete VRAM pool.

As a result, memory on RDNA3.5 APUs is mapped rather than physically partitioned. The terms Graphics Address Remapping Table (GART) and Graphics Translation Table (GTT) describe limits on how much system memory can be mapped into GPU address spaces and who can use it, rather than distinct types of physical memory.

**GART**Defines the amount of platform address space (system RAM or Memory-Mapped I/O) that can be mapped into the GPU virtual address space used by the kernel driver. On systems with physically shared CPU and GPU memory, such as RDNA3.5-based systems, this mapped system memory effectively serves as VRAM for the GPU. GART is typically kept relatively small to limit GPU page-table size and is primarily used for driver-internal operations.

**GTT**Defines the amount of system RAM that can be mapped into GPU virtual address spaces for user processes. This is the memory pool used by applications such as PyTorch and other AI/compute workloads. GTT allocations are dynamic and not permanently reserved, allowing the operating system to reclaim memory when the GPU isn’t actively using it. By default, the GTT limit is set to approximately 50 percent of total system RAM.


Note

On systems with physically shared CPU and GPU memory, such as RDNA3.5-based systems, several terms are often used interchangeably in firmware menus, documentation, and community discussions:

VRAM

Carve-out

GART

Dedicated GPU memory

Firmware-reserved GPU memory


In this topic, VRAM will be used going forward.

You can adjust the amount of memory available to the GPU by:

Increasing the VRAM in BIOS, or

Reducing the configured GTT size to be smaller than the reserved amount.


If the GTT size is larger than the VRAM, the AMD GPU driver performs VRAM
allocations using GTT (GTT-backed allocations), as described in the
[torvalds/linux@759e764](https://github.com/torvalds/linux/commit/759e764f7d587283b4e0b01ff930faca64370e59)
GitHub commit.

Because memory is physically shared, there’s no performance distinction like that of discrete GPUs, where dedicated VRAM is significantly faster than system memory. Firmware may optionally reserve some memory exclusively for GPU use, but this provides little benefit for most workloads while permanently reducing available system memory.

For this reason, AI frameworks work more efficiently with GTT-backed allocations. GTT allows large, flexible mappings without permanently reserving memory, resulting in better overall system utilization on unified memory systems.

## Operating system support[#](https://rocm.docs.amd.com#operating-system-support)

The ROCm operating system requirements are available in
[Operating system support](https://rocm.docs.amd.com/about/release-notes.html#release-supported-os).

AMD Ryzen AI Max series APUs (gfx1151) have additional kernel version requirements, as described in the following section.

### Required Linux kernel version[#](https://rocm.docs.amd.com#required-linux-kernel-version)

Support for AMD Ryzen AI Max series APUs requires specific Linux kernel fixes that update internal limits in the AMD KFD driver to ensure correct queue creation and memory availability checks. Without these updates, GPU compute workloads might fail to initialize or exhibit unpredictable behavior.

The following commits are required for AMD Ryzen AI Max series support:

These patches are available in the following minimum kernel versions:

Ubuntu 24.04 Hardware Enablement (HWE):

`6.17.0-19.19~24.04.2`

or laterUbuntu 24.04 Original Equipment Manufacturer (OEM):

`6.14.0-1018`

or laterAll other distributions: Linux kernel

`6.18.4`

or later

The table below reflects compatibility for AMD-released pre-built ROCm binaries only. Distributions that ship native ROCm packaging might provide different support levels.

❌ |
Unsupported combination |
⚠️ |
Unstable/experimental combination |
✅ |
Stable and supported combination |

ROCm Release |
Ubuntu 24.04 HWE (>= 6.17.0-19.19~24.04.2),
Ubuntu 24.04 OEM (>= 6.14.0-1018) or
Ubuntu 26.04 Generic
|
Other distributions >= 6.18.4 |
Other distributions < 6.18.4 |
|---|---|---|---|
7.11.0 or 7.12.0 |
✅ |
✅ |
⚠️ |
7.9.0 or 7.10.0 |
❌ |
❌ |
⚠️ |
7.2.1, 7.2.2 or 7.2.3 |
✅ |
✅ |
⚠️ |
7.2.0 |
✅ |
✅ |
❌ |
7.1.x |
❌ |
❌ |
⚠️ |
6.4.x |
❌ |
❌ |
⚠️ |

Note

Ubuntu 24.04 HWE kernels earlier than `6.17.0-19.19~24.04.2`

and Ubuntu
24.04 OEM kernels earlier than `6.14.0-1018`

are not supported for
RDNA3.5 APUs.

The following distributions include the required fixes in their native packaging, independent of AMD pre-built binaries:

Fedora 43

Ubuntu 26.04

Arch Linux 2026.02.01