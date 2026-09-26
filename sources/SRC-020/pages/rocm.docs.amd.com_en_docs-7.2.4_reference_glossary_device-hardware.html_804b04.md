source: https://rocm.docs.amd.com/en/docs-7.2.4/reference/glossary/device-hardware.html

# Device hardware glossary[#](https://rocm.docs.amd.com#device-hardware-glossary)

2026-02-20

7 min read time

This section provides concise definitions of hardware components and architectural features of AMD GPUs.

- AccVGPR
[#](https://rocm.docs.amd.com#term-AccVGPR) Accumulation General Purpose Vector Registers (AccVGPRs) are a special type of

[VGPRs](https://rocm.docs.amd.com#term-VGPR)used exclusively for matrix operations.- ALU
[#](https://rocm.docs.amd.com#term-ALU) Arithmetic logic units (ALUs) are the primary arithmetic engines that execute mathematical and logical operations within

[compute units](https://rocm.docs.amd.com#term-Compute-units). See[Vector arithmetic logic unit (VALU)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#valu)for details.- AMD device architecture
[#](https://rocm.docs.amd.com#term-AMD-device-architecture) AMD device architecture is based on unified, programmable compute engines known as

[compute units (CUs)](https://rocm.docs.amd.com#term-Compute-units). See[Hardware implementation](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#hardware-implementation)for details.- Compute unit versioning
[#](https://rocm.docs.amd.com#term-Compute-unit-versioning) [Compute units](https://rocm.docs.amd.com#term-Compute-units)are versioned with[GFX IP](https://rocm.docs.amd.com#term-GFX-IP)identifiers that define their microarchitectural features and instruction set compatibility. See[Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/compilers.html#gfx-ip)for details.- Compute units
[#](https://rocm.docs.amd.com#term-Compute-units) Compute units (CUs) are the fundamental programmable execution engines in AMD GPUs capable of running complex programs. See

[Compute unit architecture](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#compute-unit)for details.- Data movement engine
[#](https://rocm.docs.amd.com#term-Data-movement-engine) Data movement engines (DMEs) are specialized hardware units in AMD Instinct MI300 and MI350 series GPUs that accelerate multi-dimensional tensor data copies between global memory and on-chip memory. See

[Data movement engine (CDNA 3 / CDNA 4)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#dme)for details.- GCD
[#](https://rocm.docs.amd.com#term-GCD) On AMD Instinct MI100 and MI250 series GPUs and AMD Radeon GPUs, the Graphics Compute Die (GCD) contains the GPU’s computational elements and lower levels of the cache hierarchy. See

[AMD Instinct™ MI250 microarchitecture](https://rocm.docs.amd.com/conceptual/gpu-arch/mi250.html)for details.- GFX IP
[#](https://rocm.docs.amd.com#term-GFX-IP) GFX IP (Graphics IP) versions are identifiers that specify which instruction formats, memory models, and compute features are supported by each AMD GPU generation. See

[Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/compilers.html#gfx-ip)for versioning information.- GFX IP major version
[#](https://rocm.docs.amd.com#term-GFX-IP-major-version) The

[GFX IP](https://rocm.docs.amd.com#term-GFX-IP)major version represents the GPU’s core instruction set and architecture. For example, a GFX IP 11 major version corresponds to the RDNA3 architecture, influencing driver support and available compute features. See[Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/compilers.html#gfx-ip)for versioning information.- GFX IP minor version
[#](https://rocm.docs.amd.com#term-GFX-IP-minor-version) The

[GFX IP](https://rocm.docs.amd.com#term-GFX-IP)minor version represents specific variations within a[GFX IP](https://rocm.docs.amd.com#term-GFX-IP)major version and affects feature sets, optimizations, and driver behavior. Different GPU models within the same major version can have unique capabilities, impacting performance and supported instructions. See[Target GPU architectures (GFX IP)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/compilers.html#gfx-ip)for versioning information.- GPU RAM (VRAM)
[#](https://rocm.docs.amd.com#term-GPU-RAM-VRAM) GPU RAM, also known as

[global memory](https://rocm.docs.amd.com/device-software.html#term-Global-memory)in the HIP programming model, is the large, high-capacity off-chip memory subsystem accessible by all[compute units](https://rocm.docs.amd.com#term-Compute-units), forming the foundation of the device’s[memory hierarchy](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#hbm).- Graphics L1 cache
[#](https://rocm.docs.amd.com#term-Graphics-L1-cache) On AMD Radeon GPUs, the read-only graphics level 1 (L1) cache is local to groups of

[WGPs](https://rocm.docs.amd.com#term-WGP)called shader arrays, providing fast access to recently used data. AMD Instinct GPUs do not feature the graphics L1 cache.- Infinity Cache (L3 cache)
[#](https://rocm.docs.amd.com#term-Infinity-Cache-L3-cache) On AMD Instinct MI300 and MI350 series GPUs and AMD Radeon GPUs, the Infinity Cache is the last level cache of the cache hierarchy. It is shared by all

[compute units](https://rocm.docs.amd.com#term-Compute-units)and[WGPs](https://rocm.docs.amd.com#term-WGP)on the GPU.- L0 instruction cache
[#](https://rocm.docs.amd.com#term-L0-instruction-cache) On AMD Radeon GPUs, the level 0 (L0) instruction cache is local to each

[WGP](https://rocm.docs.amd.com#term-WGP)and thus shared between the WGP’s[compute units](https://rocm.docs.amd.com#term-Compute-units).- L0 scalar cache
[#](https://rocm.docs.amd.com#term-L0-scalar-cache) On AMD Radeon GPUs, the level 0 (L0) scalar data cache is local to each

[WGP](https://rocm.docs.amd.com#term-WGP)and thus shared between the WGP’s[compute units](https://rocm.docs.amd.com#term-Compute-units). It provides the[scalar ALU](https://rocm.docs.amd.com#term-SALU)with fast access to recently used data.- L0 vector cache
[#](https://rocm.docs.amd.com#term-L0-vector-cache) On AMD Radeon GPUs, the level 0 (L0) vector data cache is local to each

[WGP](https://rocm.docs.amd.com#term-WGP)and thus shared between the WGP’s[compute units](https://rocm.docs.amd.com#term-Compute-units). It provides the[vector ALU](https://rocm.docs.amd.com#term-VALU)with fast access to recently used data.- L1 instruction cache
[#](https://rocm.docs.amd.com#term-L1-instruction-cache) On AMD Instinct GPUs, the level 1 (L1) instruction cache is local to each

[compute unit](https://rocm.docs.amd.com#term-Compute-units). On AMD Radeon GPUs, the L1 instruction cache does not exist as a separate cache level, and instructions are stored in the[L0 instruction cache](https://rocm.docs.amd.com#term-L0-instruction-cache).- L1 scalar cache
[#](https://rocm.docs.amd.com#term-L1-scalar-cache) On AMD Instinct GPUs, the level 1 (L1) scalar data cache is local to each

[compute unit](https://rocm.docs.amd.com#term-Compute-units), providing the[scalar ALU](https://rocm.docs.amd.com#term-SALU)with fast access to recently used data. On AMD Radeon GPUs, the L1 scalar cache does not exist as a separate cache level, and recently used scalar data is stored in the[L0 scalar cache](https://rocm.docs.amd.com#term-L0-scalar-cache).- L1 vector cache
[#](https://rocm.docs.amd.com#term-L1-vector-cache) On AMD Instinct GPUs, the level 1 (L1) vector data cache is local to each

[compute unit](https://rocm.docs.amd.com#term-Compute-units), providing the[vector ALU](https://rocm.docs.amd.com#term-VALU)with fast access to recently used data. On AMD Radeon GPUs, the L1 vector cache does not exist as a separate cache level, and recently used vector data is stored in the[L0 vector cache](https://rocm.docs.amd.com#term-L0-vector-cache).- L2 cache
[#](https://rocm.docs.amd.com#term-L2-cache) On AMD Instinct MI100 series GPUs, the L2 cache is shared across the entire chip, while for all other AMD GPUs the L2 caches are shared by the

[compute units](https://rocm.docs.amd.com#term-Compute-units)on the same[GCD](https://rocm.docs.amd.com#term-GCD)or[XCD](https://rocm.docs.amd.com#term-XCD).- Load/store unit
[#](https://rocm.docs.amd.com#term-Load-store-unit) Load/store units (LSUs) handle data transfer between

[compute units](https://rocm.docs.amd.com#term-Compute-units)and the GPU’s memory subsystems, managing thousands of concurrent memory operations. See[Load/store unit (LSU)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#lsu)for details.Local data share (LDS) is fast on-chip memory local to each

[compute unit](https://rocm.docs.amd.com#term-Compute-units)and shared among[work-items](https://rocm.docs.amd.com#term-Work-item-Thread)in a[work-group](https://rocm.docs.amd.com#term-Work-group-Block), enabling efficient coordination and data reuse. In the HIP programming model, the LDS is known as shared memory. See[Local data share (LDS)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#lds)for LDS programming details.- Matrix cores (MFMA units)
[#](https://rocm.docs.amd.com#term-Matrix-cores-MFMA-units) Matrix cores (MFMA units) are specialized execution units that perform large-scale matrix operations in a single instruction, delivering high throughput for AI and HPC workloads. See

[Matrix fused multiply-add (MFMA)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#mfma-units)for details.- Register file
[#](https://rocm.docs.amd.com#term-Register-file) The register file is the primary on-chip memory store in each

[compute unit](https://rocm.docs.amd.com#term-Compute-units), holding data between arithmetic and memory operations. See[Memory model](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/programming_model.html#memory-hierarchy)for details.- Registers
[#](https://rocm.docs.amd.com#term-Registers) Registers are the lowest level of the memory hierarchy, storing per-thread temporary variables and intermediate results. See

[Memory model](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/programming_model.html#memory-hierarchy)for register usage details.- SALU
[#](https://rocm.docs.amd.com#term-SALU) Scalar

[ALUs](https://rocm.docs.amd.com#term-ALU)(SALUs) operate on a single value per[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/rocPRIM-glossary.html#term-Wavefront)and manage all control flow.- SGPR
[#](https://rocm.docs.amd.com#term-SGPR) Scalar general-purpose

[registers](https://rocm.docs.amd.com#term-Registers)(SGPRs) hold data produced and consumed by a[compute unit](https://rocm.docs.amd.com#term-Compute-units)’s[scalar ALU](https://rocm.docs.amd.com#term-SALU).- SGPR file
[#](https://rocm.docs.amd.com#term-SGPR-file) The

[SGPR](https://rocm.docs.amd.com#term-SGPR)file is the[register file](https://rocm.docs.amd.com#term-Register-file)that holds data used by the[scalar ALU](https://rocm.docs.amd.com#term-SALU).- SIMD core
[#](https://rocm.docs.amd.com#term-SIMD-core) SIMD cores are execution lanes that perform scalar and vector arithmetic operations inside each

[compute unit](https://rocm.docs.amd.com/projects/composable_kernel/en/docs-7.2.4/reference/Composable-Kernel-Glossary.html#term-compute-unit). See[CDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#cdna-architecture)and[RDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#rdna-architecture)for details.- Special function unit
[#](https://rocm.docs.amd.com#term-Special-function-unit) Special function units (SFUs) accelerate transcendental and reciprocal mathematical functions such as

`exp`

,`log`

,`sin`

, and`cos`

. See[Special function unit (SFU)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#sfu)for details.- VALU
[#](https://rocm.docs.amd.com#term-VALU) Vector

[ALUs](https://rocm.docs.amd.com#term-ALU)(VALUs) perform an arithmetic or logical operation on data for each[work-item](https://rocm.docs.amd.com#term-Work-item-Thread)in a[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/rocPRIM-glossary.html#term-Wavefront), enabling data-parallel execution.- VGPR
[#](https://rocm.docs.amd.com#term-VGPR) Vector general-purpose

[registers](https://rocm.docs.amd.com#term-Registers)(VGPRs) hold data produced and consumed by a[compute unit](https://rocm.docs.amd.com#term-Compute-units)’s[vector ALU](https://rocm.docs.amd.com#term-VALU).- VGPR file
[#](https://rocm.docs.amd.com#term-VGPR-file) The

[VGPR](https://rocm.docs.amd.com#term-VGPR)file is the[register file](https://rocm.docs.amd.com#term-Register-file)that holds data used by the[vector ALU](https://rocm.docs.amd.com#term-VALU). GPUs with[matrix cores](https://rocm.docs.amd.com#term-Matrix-cores-MFMA-units)also have[AccVGPR](https://rocm.docs.amd.com#term-AccVGPR)files, used specifically for matrix instructions.- Wavefront (Warp)
[#](https://rocm.docs.amd.com#term-Wavefront-Warp) A wavefront (also called a warp) is a group of

[work-items](https://rocm.docs.amd.com#term-Work-item-Thread)that execute in parallel on a single[compute unit](https://rocm.docs.amd.com#term-Compute-units), sharing one instruction stream. See[Warp (or Wavefront)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/programming_model.html#wavefront)for execution details.- Wavefront scheduler
[#](https://rocm.docs.amd.com#term-Wavefront-scheduler) The wavefront scheduler in each

[compute unit](https://rocm.docs.amd.com#term-Compute-units)decides which[wavefront](https://rocm.docs.amd.com/projects/composable_kernel/en/docs-7.2.4/reference/Composable-Kernel-Glossary.html#term-wavefront)to execute each clock cycle, enabling rapid context switching for latency hiding. See[Sequencer and scheduling](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#wave-scheduling)for details.- Wavefront size
[#](https://rocm.docs.amd.com#term-Wavefront-size) The wavefront size is the number of

[work-items](https://rocm.docs.amd.com#term-Work-item-Thread)that execute together in a single[wavefront](https://rocm.docs.amd.com#term-Wavefront-Warp). For AMD Instinct GPUs, the wavefront size is 64 threads, while AMD Radeon GPUs have a wavefront size of 32 threads. See[Warp (or Wavefront)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/programming_model.html#wavefront)for details.- WGP
[#](https://rocm.docs.amd.com#term-WGP) A Workgroup Processor (WGP) is a hardware unit on AMD Radeon GPUs that contains two

[compute units](https://rocm.docs.amd.com#term-Compute-units)and their associated resources, enabling efficient scheduling and execution of[wavefronts](https://rocm.docs.amd.com/projects/composable_kernel/en/docs-7.2.4/reference/Composable-Kernel-Glossary.html#term-wavefront). See[RDNA architecture](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/hardware_implementation.html#rdna-architecture)for details.- Work-group (Block)
[#](https://rocm.docs.amd.com#term-Work-group-Block) A work-group (also called a block) is a collection of

[wavefronts](https://rocm.docs.amd.com#term-Wavefront-Warp)scheduled together on a single[compute unit](https://rocm.docs.amd.com#term-Compute-units)that can coordinate through[Local data share](https://rocm.docs.amd.com#term-Local-data-share)memory. See[Block (Work-group)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/programming_model.html#inherent-thread-hierarchy-block)for work-group details.- Work-item (Thread)
[#](https://rocm.docs.amd.com#term-Work-item-Thread) A work-item (also called a thread) is the smallest unit of execution on an AMD GPU and represents a single element of work. See

[Thread (Work-item)](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/programming_model.html#work-item)for thread hierarchy details.- XCD
[#](https://rocm.docs.amd.com#term-XCD) On AMD Instinct MI300 and MI350 series GPUs, the Accelerator Complex Die (XCD) contains the GPU’s computational elements and lower levels of the cache hierarchy. See

[AMD Instinct™ MI300 Series microarchitecture](https://rocm.docs.amd.com/conceptual/gpu-arch/mi300.html)for details.