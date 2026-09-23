# hipkittens-gemm-ladder

source: https://rocm.blogs.amd.com/software-tools-optimization/hipkittens-gemm-ladder/README.html

# An Educational GEMM Ladder for Helios GPUs[#](https://rocm.blogs.amd.com#an-educational-gemm-ladder-for-helios-gpus)

AMD Helios will be an important platform for AI. Helios offers 432 GB of HBM4,
23 TB/s of HBM bandwidth per GPU, and 40 PFLOPs of FP4 compute
[AMD Instinct™ MI455X GPU](https://www.amd.com/content/dam/amd/en/documents/products/accelerators/instinct/amd-instinct-mi455x_brochure.pdf).
These capabilities will be especially valuable for large frontier models and long-context
agentic workloads.

In this blog post, we highlight several features of the Helios architecture and build an
educational ladder of BF16 general matrix multiplication (GEMM) kernels that progressively
takes advantage of them. The ladder is inspired by Simon Boehm’s CUDA GEMM worklog
[How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance: a Worklog](https://siboehm.com/articles/22/CUDA-MMM)
and is intended to help kernel developers understand how Helios’s new hardware features
affect kernel design.

## A HipKittens Refresher[#](https://rocm.blogs.amd.com#a-hipkittens-refresher)

Both the kernel implementations and optimization ladder in this post use HipKittens, so we
collect the main references here before diving in. The framework is introduced in
[HipKittens: Fast and Furious AMD Kernels](https://arxiv.org/abs/2511.08083), and the
[HipKittens repository](https://github.com/HazyResearch/HipKittens) contains its source and
kernel examples.

## Helios Feature Overview[#](https://rocm.blogs.amd.com#helios-feature-overview)

A Helios GPU contains 256 workgroup processors (WGPs), organized into eight Accelerator Complex Dies (XCDs). Each WGP has 320 KB of local data share (LDS) and 1024 32-bit registers per wave. The GPU has 432 GB of HBM4 with 23 TB/s of peak bandwidth. The Helios scale-up domain includes 72 GPUs per rack with 3.6 TB/s of bandwidth and a unified virtual-memory abstraction that simplifies intra-node memory access.

Hardware unit |
Description |
|---|---|
Single Instruction Multiple Data processor (SIMD) |
A group of 32 lanes with its own set of vector general-purpose registers (VGPRs). |
Workgroup processor (WGP) |
One of the GPU’s 256 processors. Previously referred to as a compute unit (CU) on earlier AMD GPU generations. A WGP contains two SIMD pairs, or four SIMDs in total. |
Shader Engine (SE) |
A collection of 16 physically co-located WGPs. |
Accelerator Complex Die (XCD) |
A collection of 32 physically co-located WGPs on a chiplet. |
I/O Die (IOD) |
A base die with four XCDs stacked on top. Each IOD contains 96 MiB of coherent L2 cache. |
GPU |
One AMD Instinct™ MI455X GPU consists of two IODs. |

Table 1. Physical compute hierarchy of a CDNA™ 5 Helios GPU.

Execution unit |
Description |
|---|---|
Thread |
The smallest unit of execution on the GPU. |
Wave |
A collection of 32 threads that executes in lockstep. Earlier AMD GPUs used 64 threads per wave. |
Workgroup |
A collection of waves co-scheduled on a WGP. |
Workgroup cluster |
A collection of workgroups running concurrently on a Shader Engine. |
Grid |
The complete collection of workgroups, or workgroup clusters, launched by one kernel. |

Table 2. Logical HIP execution hierarchy on CDNA™ 5.

Memory |
Description |
|---|---|
VGPR |
The SIMD-scoped vector register file: 1024 registers, each with 32 lanes of 32-bit values. |
LDS/L1 |
Each WGP has six 64 KB hardware partitions. Up to five (320 KB) can be allocated to LDS, with at least one retained for L1. |
L2 |
Two coherent 96 MB halves, one per IOD, totaling 192 MB per device. |
High-Bandwidth Memory (HBM) |
Eight 54 GB HBM4 stacks, totaling 432 GB. |

Table 3. Physical memory hierarchy of a CDNA™ 5 Helios GPU.

The key changes at each level of the memory hierarchy include:

**Partitioned LDS.**Each WGP has five 64 KB LDS partitions. LDS remains banked, so layouts must avoid bank conflicts. Two 256-byte-per-cycle paths, one per SIMD pair, serve LDS. Concurrent accesses to the same partition can cause partition conflicts, so high-bandwidth kernels must consider both bank placement within a partition and placement across partitions. A single 256-byte-per-cycle path is already sufficient to saturate the matrix core units.**Cache structure, NUMA effects, and memory prefetching.**Earlier AMD GPUs used both a per-XCD L2 cache and a global last-level cache (LLC). Helios simplifies this hierarchy to a single L2 cache, physically implemented as two coherent 96 MB halves per GPU. The half closer to a given processor provides substantially higher bandwidth than the remote half (more than 40 TB/s for near L2 versus approximately 20 TB/s for remote L2). Across the GPU’s eight XCDs, four XCDs reside in each local L2 NUMA domain. Cache hints let kernel developers manage L2 behavior, including prefetching global memory into L2 from either the device or the host.**Tensor Data Movement (TDM) for global HBM.**TDM provides a DMA-style path between HBM and LDS. It supports scatter-gather access patterns and exposes its descriptor architecture in the ISA. Unlike a hardware-swizzled load, TDM does not rearrange LDS data on the fly, so padding or layout design is still required to avoid bank conflicts.

The key changes to the execution model include:

**Wave size.**Helios uses 32 threads per wave, compared with 64 threads per wave on previous AMD GPUs. On earlier generations, a 64-thread wave executed across 16 physical SIMD lanes, creating less regular lane ownership and memory-access patterns that kernel programmers had to account for when optimizing memory layouts[AMD GPUs go brrr](https://hazyresearch.stanford.edu/blog/2025-11-09-amd-brr).[[1]](https://rocm.blogs.amd.com#id2)Helios pairs 32-thread waves with 32 physical SIMD lanes, enabling more regular lane ownership and simplifying memory-layout optimization.**Workgroup-cluster launch and multicast.**Helios can guarantee that groups of up to 16 workgroups are co-located across nearby WGPs, enabling data sharing and synchronization across the cluster. Instead of having every workgroup independently request the same data, one load can be multicast to multiple WGPs, increasing effective bandwidth through cache reuse.

Now let’s put these features into action.

## Educational GEMM Ladder[#](https://rocm.blogs.amd.com#educational-gemm-ladder)

Inspired by Simon Boehm’s GEMM worklog, we present an educational GEMM ladder for Helios GPUs. Figure 1 introduces the MI455X hardware hierarchy and shows how GEMM tiles map onto it:



Figure 1: The MI455X hierarchy narrows from the GPU to XCDs, WGPs, SIMDs, waves, and threads (top). GEMM maps A and B tiles to WGPs that accumulate C output tiles (bottom).

For a large GEMM, the output matrix is divided into tiles that can be computed independently. Each workgroup, a collection of waves co-scheduled on a WGP, computes one output tile. Every WGP has its own register file and LDS, as well as circuitry for matrix multiplication, exponentials, and other arithmetic in data types including BF16, FP8, FP6, and FP4. All WGPs can also access the GPU’s shared cache hierarchy and HBM. Figure 2 summarizes the measured performance across the optimization ladder:

Even a kernel midway through the ladder outperforms the well-optimized MI355X GEMM kernel, and the final Helios kernels approach twice its performance. These tests were run on early-access GPUs, which continue to receive substantial firmware and software improvements.

Each rung computes [HipKittens: Fast and Furious AMD Kernels](https://github.com/HazyResearch/HipKittens).
For each kernel, we report the
PFLOP/s attained for

For each rung, we also show the kernel’s hot loop—that is, its iteration over the GEMM
K dimension—captured with AMD Advanced Thread Trace (ATT) using the profiling tools in the
[ROCm Systems repository](https://github.com/ROCm/rocm-systems). In these visualizations,
each row depicts one wave’s instruction execution over time, and a group of rows shows
execution on one or more of the WGP’s four SIMDs.

### Level 0: Naive Baseline ([gemm_naive.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/00_gemm_naive.cpp#L58-L82))[#](https://rocm.blogs.amd.com#level-0-naive-baseline-gemm-naive-cpp)

Each workgroup computes a

This baseline uses one LDS buffer for A and B and does not overlap data movement with compute. Every K iteration therefore proceeds serially: load A and B from global memory into LDS, synchronize, load from LDS into registers and compute, synchronize again, and only then begin loading the next K tile. The second synchronization is required because the same LDS buffer is reused in every iteration. As a result, the matrix units are idle during memory movement, and the memory pipeline is underutilized during computation. The figure below shows the resulting serialized schedule:

#### Level 0 APIs[#](https://rocm.blogs.amd.com#level-0-apis)

API |
Purpose |
|---|---|
Uses vector lanes to copy a global tile through registers into LDS. |
|
Loads one wave’s LDS fragment into registers. |
|
Drains memory traffic before LDS is published or reused. |
|
Waits for every wave at the workgroup barrier. |
|
Accumulates a BF16 |
|
Converts and writes the FP32 accumulator directly to the global C tile. |

#### Level 0 Pseudocode[#](https://rocm.blogs.amd.com#level-0-pseudocode)

```
for each K tile:
load(A_LDS, A_global); // A: global -> staging registers -> LDS
load(B_LDS, B_global); // B: global -> staging registers -> LDS
sync::fence(); // Wait for global-to-LDS traffic
sync::sync(); // Wait for peer waves to publish LDS
load(A_reg, A_LDS); // A: LDS -> registers
load(B_reg, B_LDS); // B: LDS -> registers
mma_ABt(C, A_reg, B_reg); // Accumulate C += A * B^T
sync::fence(); // Wait for LDS reads
sync::sync(); // Wait before reusing LDS
```

The trace in Figure 4 shows one SIMD with 12 resident wave tracks from different workgroups; the scheduler switches among them automatically to maximize resource utilization:

On SIMD0 wave slot 0, early green VALU instructions come from register-mediated A/B fills
and address calculations. Four purple WMMA instructions at cycles 1,218–1,620 map to
`mma_ABt`

. The long yellow intervals are consistent with publish and reuse synchronization,
although the color alone does not identify a specific barrier.

### Level 1: Double-Buffered in LDS ([gemm_double_buf.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/01_gemm_double_buf.cpp#L65-L89))[#](https://rocm.blogs.amd.com#level-1-double-buffered-in-lds-gemm-double-buf-cpp)

**Performance:**Less than 1% faster than Level 0 (25.3% to 25.4% of the MI355X baseline in Figure 2).

The previous kernel severely underutilizes the 320 KB of LDS available per WGP. At a
`BLOCK_K=32`

, Level 0 uses one 8.5 KB stage—only 2.7% of
the budget. Two stages require 17 KB, or 5.3%, so double buffering is a natural next step.

This kernel allocates two LDS buffer sets for A and B and turns the K loop into a two-stage software pipeline. Initially, a prologue loads and publishes the first A/B tiles; then, each iteration issues HBM loads into the inactive buffer while WMMA consumes the current one. A workgroup barrier at the end ensures the next buffer is ready to read and the current buffer is safe to overwrite before swapping.

**Why it helps:** Double buffering overlaps memory loads with computation, increasing
instruction-level parallelism. The measured performance step stays small here because fills are still
register-mediated and each K block drains fully before handoff. Level 2 keeps the same
staging; with async direct-to-LDS copies, that is when the benefits of this buffering are
realized. The figure below illustrates the double-buffered schedule:

#### Level 1 APIs[#](https://rocm.blogs.amd.com#level-1-apis)

API |
Purpose |
|---|---|
Reserves two tightly packed LDS slots for the current and next operand tiles. |
|
Drains the final LDS reads before the kernel exits. |

#### Level 1 Pseudocode[#](https://rocm.blogs.amd.com#level-1-pseudocode)

```
A_LDS[2];
B_LDS[2];
load(A_LDS[current], A_global);
load(B_LDS[current], B_global);
sync::fence();
sync::arrive();
sync::wait(); // Publish the first LDS stage
for each K tile:
load(A_LDS[next], A_global_clamped);
load(B_LDS[next], B_global_clamped);
load(A_reg, A_LDS[current]);
load(B_reg, B_LDS[current]);
mma_ABt(C, A_reg, B_reg);
sync::fence(); // Wait for fills and reads
sync::arrive();
sync::wait(); // Hand off one workgroup barrier
swap(current, next);
```

The trace in Figure 6 shows how the scheduler interleaves the resident waves at this level:

Like the naive kernel, the scheduler switches among 12 waves from different workgroups. Much of the SIMD’s time is still spent on green VALU work because vector lanes both load data from global memory into registers and write those registers to LDS. Matrix work remains sparse.

### Level 2: Asynchronous HBM Loads ([gemm_async.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/02_gemm_async.cpp#L59-L83))[#](https://rocm.blogs.amd.com#level-2-asynchronous-hbm-loads-gemm-async-cpp)

**Performance:**48% faster than Level 1.

The AMD Instinct MI455X GPU can copy global memory directly into LDS without passing the data
through the register file. An asynchronous copy is fire-and-forget and retires on `asynccnt`

.
The wave checks that counter only when the data becomes a dependency, so the fill no longer
has to lead the iteration or end in a blanket drain.

Rung |
Fill path |
Per K block |
|---|---|---|
Naive |
Register-mediated |
Two full barriers, two LDS drains, and two global-load drains |
Double-buffered |
Register-mediated |
One full barrier, one LDS drain, and one global-load drain |
Asynchronous |
Direct to LDS |
One split barrier, one LDS drain, and one asynchronous-copy drain |

Direct-to-LDS loads avoid staging through VGPRs, reducing register pressure and freeing register space for the larger output tiles introduced in later levels. They also eliminate a register store-and-writeback path to LDS.

**Why it helps:** Asynchronous loads move data from global memory directly into LDS, avoiding
a round trip through the vector register file. The figure below illustrates how the direct-to-LDS
copy overlaps the rest of the pipeline:

#### Level 2 APIs[#](https://rocm.blogs.amd.com#level-2-apis)

API |
Purpose |
|---|---|
Starts a direct global-to-LDS copy without using VGPRs. |
|
Drains unordered asynchronous copies before stage handoff. |
|
Separates workgroup-barrier signaling from waiting. |
|
Prevents the compiler from moving work across a handoff. |

#### Level 2 Pseudocode[#](https://rocm.blogs.amd.com#level-2-pseudocode)

```
load_async(A_LDS[current], A_global);
load_async(B_LDS[current], B_global);
sync::wait_async<0>();
sched::compiler_fence();
sync::arrive();
sync::wait(); // Publish the first LDS stage
sched::compiler_fence();
for each K tile:
load(A_reg, A_LDS[current]);
load(B_reg, B_LDS[current]);
load_async(A_LDS[next], A_global_clamped);
load_async(B_LDS[next], B_global_clamped);
sync::wait_ds<0>(); // Wait for current LDS reads
mma_ABt(C, A_reg, B_reg);
sync::wait_async<0>(); // Wait for next global-to-LDS fills
sched::compiler_fence();
sync::arrive();
sync::wait();
sched::compiler_fence();
swap(current, next);
```

The trace in Figure 8 shows nine resident wave tracks. There is significantly less time waiting for vector work than in earlier levels because the vector lane only issues direct-to-LDS loads before consuming larger chunks from LDS.

### Level 3: Increasing Output Tile Size to 128 x 128 ([gemm_128x128.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/03_gemm_128x128.cpp#L58-L82))[#](https://rocm.blogs.amd.com#level-3-increasing-output-tile-size-to-128-x-128-gemm-128x128-cpp)

**Performance:**80% faster than Level 2.

For one output tile, GEMM’s arithmetic intensity is

When

Larger tiles also increase data reuse. Four WGPs independently computing adjacent

Level 3 computes a

**Why it helps:** Increasing the output tile size raises arithmetic intensity and reduces
memory traffic through greater per-WGP data reuse. Figure 9 shows the schedule for the
larger WGP output tile:

The trace in Figure 10 contains more matrix instructions per wave because each WGP is responsible for a larger output tile:

### Level 4: Increasing Output Tile Size to 256 x 256 ([gemm_256x256.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/04_gemm_256x256.cpp#L62-L86))[#](https://rocm.blogs.amd.com#level-4-increasing-output-tile-size-to-256-x-256-gemm-256x256-cpp)

**Performance:**25% faster than Level 3.

This kernel computes a

#### Level 4 Configuration[#](https://rocm.blogs.amd.com#level-4-configuration)

```
BLOCK_M = BLOCK_N = 256;
WARPS_M = WARPS_N = 4;
rt_fl<64, 64> C_acc;
// The asynchronous double-buffered K loop is otherwise unchanged.
```

Figure 11 illustrates the schedule with a

The trace in Figure 12 begins with asynchronous-load issue, followed by large LDS-read blocks and then dense groups of purple WMMA instructions. These groups reflect the increased matrix work per wave:

### Level 5: Deepening the K Stride for WMMA Instructions ([gemm_deepk.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/05_gemm_deepk.cpp#L62-L86))[#](https://rocm.blogs.amd.com#level-5-deepening-the-k-stride-for-wmma-instructions-gemm-deepk-cpp)

**Performance:**19% faster than Level 4.

Level 1 introduced double buffering between HBM and LDS, but a GEMM kernel can also stall
while moving data from LDS to registers. Level 5 adds a two-stage register buffer for that
path. HBM-to-LDS loads now bring in

Within the outer K loop, an inner loop runs four K=32 substeps. In each substep, a wave loads
a

**Why it helps:** A deeper K loop creates finer-grained pipeline stages and more opportunities
to overlap LDS reads with matrix computation. The figure below illustrates the four-substep
register pipeline:

#### Level 5 Pseudocode[#](https://rocm.blogs.amd.com#level-5-pseudocode)

```
load_async(A_LDS[current], A_global);
load_async(B_LDS[current], B_global);
sync::wait_async<0>();
sched::compiler_fence();
sync::arrive();
sync::wait();
sched::compiler_fence();
for each K stage:
load(A_reg[0], A_LDS[current][0]);
load(B_reg[0], B_LDS[current][0]);
load_async(A_LDS[next], A_global_clamped);
load_async(B_LDS[next], B_global_clamped);
for substep = 0 .. 2:
load(A_reg[next_reg], A_LDS[current][substep + 1]);
load(B_reg[next_reg], B_LDS[current][substep + 1]);
sync::wait_ds<DS_SUB>();
mma_ABt(C, A_reg[current_reg], B_reg[current_reg]);
swap(current_reg, next_reg);
sync::wait_ds<0>();
mma_ABt(C, A_reg[current_reg], B_reg[current_reg]);
sync::wait_async<0>();
sched::compiler_fence();
sync::arrive();
sync::wait();
sched::compiler_fence();
swap(current, next);
```

The trace in Figure 14 shows four resident wave tracks. Instead of large, sequential blocks of LDS reads and compute, each substep interleaves non-matrix work for the next substep with matrix work for the current one:

### Level 6: Accounting for Partitioned LDS ([gemm_segment.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/06_gemm_segment.cpp#L64-L88))[#](https://rocm.blogs.amd.com#level-6-accounting-for-partitioned-lds-gemm-segment-cpp)

**Performance:**No measurable change for this benchmark shape.

Bank-conflict-free LDS accesses can still serialize through partition conflicts when warps on different SIMD pairs target the same 64 KB LDS partition. The WGP’s five LDS partitions are served by two 256-byte-per-cycle paths, one per SIMD pair. Level 6 places the A and B rings in different partitions so simultaneous operand reads avoid partition conflicts and can use both paths.

For a detailed treatment of the partitioned LDS organization and its conflict behavior, see
[A Deep Dive into LDS Optimizations on AMD Instinct MI450 GPUs](https://rocm.blogs.amd.com/software-tools-optimization/mi450-lds-optimization/README.html).

Only allocation changes: all A subtiles are placed in one blocked array, followed by all B subtiles in a different partition. The K loop and its one split barrier are unchanged from Level 5. Figure 15 compares the Level 5 and Level 6 LDS allocation orders:

Figure 16 shows that the execution order remains unchanged:

**Why it helps:** Although this rung does not improve the measured

#### Level 6 Pseudocode[#](https://rocm.blogs.amd.com#level-6-pseudocode)

```
// A and B stages are allocated in separate LDS partitions.
load_async(A_LDS[current], A_global);
load_async(B_LDS[current], B_global);
sync::wait_async<0>();
sched::compiler_fence();
sync::arrive();
sync::wait();
sched::compiler_fence();
for each K stage:
load(A_reg[0], A_LDS[current][0]);
load(B_reg[0], B_LDS[current][0]);
load_async(A_LDS[next], A_global_clamped);
load_async(B_LDS[next], B_global_clamped);
for substep = 0 .. 2:
load(A_reg[next_reg], A_LDS[current][substep + 1]);
load(B_reg[next_reg], B_LDS[current][substep + 1]);
sync::wait_ds<DS_SUB>();
mma_ABt(C, A_reg[current_reg], B_reg[current_reg]);
swap(current_reg, next_reg);
sync::wait_ds<0>();
mma_ABt(C, A_reg[current_reg], B_reg[current_reg]);
sync::wait_async<0>();
sched::compiler_fence();
sync::arrive();
sync::wait();
sched::compiler_fence();
swap(current, next);
```

The trace in Figure 17 shows the unchanged four-group WMMA order:

On SIMD0 wave slot 3, the four purple WMMA groups at cycles 2,531–2,941, 3,051–3,642,
3,746–4,293, and 4,385–4,771 match the four `mma_ABt`

substeps from Level 5. Partition-aware
placement changes LDS addresses but not the matrix-operation order. The trace cannot reveal
which 64 KB partition a particular LDS access used.

### Level 7: Using TDM Loads ([gemm_tdm.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/07_gemm_tdm.cpp#L61-L85))[#](https://rocm.blogs.amd.com#level-7-using-tdm-loads-gemm-tdm-cpp)

**Performance:**38% faster than Level 6.

The Tensor Data Mover is an asynchronous data engine available to each WGP. Device-side TDM descriptors describe affine patterns with up to five dimensions and direct the engine to load data into LDS or store it to global memory. This offloads address generation and load instruction issue from the vector lanes.

TDM moves an entire panel from a device-built descriptor. Only two issuer waves post A and B
while the remaining waves continue computing. Wave 0 posts the A descriptor and wave 1 posts
the B descriptor so that the transfers use different engine parities. The register ring is
unchanged, but `tensorcnt`

replaces the asynchronous-copy drain, and one deep panel replaces
four separately filled subtiles. With two LDS stages, `wait_tdm<S-2>`

becomes
`wait_tdm<0>`

, a full drain.

The kernel also uses padded LDS layouts to produce bank-conflict-free accesses instead of spending vector instructions rearranging data during the fill. Most per-lane load, address-generation, and layout work disappears, leaving more issue bandwidth available for matrix instructions while TDM independently fills the next stage.

**Why it helps:**

Only two waves issue tensor loads; the others continue until the data becomes a dependency.

Each wave can request one large two-dimensional transfer instead of many 128-bit global-to-LDS loads.

The engine is launched with only two issue instructions, one from each issuer wave.

Address generation, padding, transposition when needed, and zero filling are offloaded to a dedicated functional unit.

The simpler hazard structure is easier for the compiler to optimize and reduces register pressure.


The figure below illustrates the descriptor-driven TDM pipeline:

#### Level 7 APIs[#](https://rocm.blogs.amd.com#level-7-apis)

API |
Purpose |
|---|---|
Posts one descriptor-driven global-to-LDS panel transfer. |
|
Drains both TDM transfers before the LDS stage is published or reused. |

#### Level 7 Pseudocode[#](https://rocm.blogs.amd.com#level-7-pseudocode)

```
if (wave_id == 0)
tdm::load_async(A_LDS[current], A_global);
if (wave_id == 1)
tdm::load_async(B_LDS[current], B_global);
sync::wait_tdm<0>();
sched::compiler_fence();
sync::arrive();
sync::wait();
sched::compiler_fence();
for each K stage:
load(A_reg[0], A_LDS[current][0]);
load(B_reg[0], B_LDS[current][0]);
if (wave_id == 0)
tdm::load_async(A_LDS[next], A_global, count_or_zero);
if (wave_id == 1)
tdm::load_async(B_LDS[next], B_global, count_or_zero);
for substep = 0 .. 2:
load(A_reg[next_reg], A_LDS[current][substep + 1]);
load(B_reg[next_reg], B_LDS[current][substep + 1]);
sync::wait_ds<DS_SUB>();
mma_ABt(C, A_reg[current_reg], B_reg[current_reg]);
swap(current_reg, next_reg);
sync::wait_ds<0>();
mma_ABt(C, A_reg[current_reg], B_reg[current_reg]);
sync::wait_tdm<0>();
sched::compiler_fence();
sync::arrive();
sync::wait();
sched::compiler_fence();
swap(current, next);
```

The trace in Figure 19 shows the resulting reduction in lane-issued fill work:

On SIMD0 wave slot 0, decoded WMMA groups at cycles 289–533, 638–1,145, and 1,249–1,732
map to the inner loop’s three `mma_ABt`

calls; cycles 1,826–2,192 map to the final call.
The small green prefix is ordinary VALU work used to build TDM descriptors and offsets.
Descriptor-driven panel movement removes broad lane-issued fill work, leaving matrix groups
as the dominant instruction color. Physical slot labels do not identify source `wave_id`

.

### Level 8: Using Split Barriers ([gemm_split_bar.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/08_gemm_split_bar.cpp#L71-L95))[#](https://rocm.blogs.amd.com#level-8-using-split-barriers-gemm-split-bar-cpp)

**Performance:**4% faster than Level 7.

A workgroup barrier often prevents one wave from overwriting an LDS buffer while another wave is still reading it. With a conventional barrier, each wave signals completion and immediately waits, leaving early waves idle until the slowest wave arrives.

A split barrier separates the signal from the wait. After a wave completes its final LDS read, its operands are safely held in registers, so it signals that the LDS buffer can be released. The wave then performs its final register-only WMMA before waiting for its peers. Compiler fences keep the WMMA inside this interval; moving it outside the signal and wait would preserve numerical correctness but lose the intended overlap.

**Why it helps:** Split barriers overlap the final K substep with peer-wave arrival, hiding
some synchronization latency with useful computation. The figure below illustrates the
matrix work placed between barrier arrival and wait:

#### Level 8 Core Scheduling Change[#](https://rocm.blogs.amd.com#level-8-core-scheduling-change)

```
sync::wait_ds<0>();
sync::wait_tdm<0>();
sync::arrive(); // Release the LDS stage
mma_ABt(C, A_reg[final], B_reg[final]);
sync::wait(); // Wait for peer waves
```

The trace in Figure 21 shows that scheduling interval:

On SIMD0 wave slot 0, the barrier signal issues at cycle 1,649, followed by 16 WMMA instructions at cycles 1,653–1,776 and the barrier wait at cycle 1,784. Slot 1 repeats the same signal, WMMA, and wait sequence at cycles 1,923–2,058. The final purple block is matrix work deliberately placed inside the split-barrier window.

### Level 9: Using Workgroup Clusters and Multicast ([gemm_wgc_multicast.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/09_gemm_wgc_multicast.cpp#L80-L109))[#](https://rocm.blogs.amd.com#level-9-using-workgroup-clusters-and-multicast-gemm-wgc-multicast-cpp)

**Performance:**7% faster than Level 8.

Workgroup clusters can contain up to 16 workgroups launched concurrently. Workgroups in a cluster can declare that they will share selected data with other WGPs in that cluster. Repeated L2 requests are then deduplicated through multicast.

This kernel arranges the workgroups in a

One panel consumed by a cluster row |
Panels multicast across rows and columns |
|---|---|

Figure 22: A $4 \times 4$ cluster reuses A panels down columns and B panels across rows, reducing repeated L2 requests.

The stage handoff now uses both workgroup and cluster barriers. The final WMMA remains inside both split-barrier windows: wave 0 signals cluster arrival, and then every wave waits.

**Why it helps:** Workgroup clusters and multicast broadcast shared panels from L2, increasing
effective L2 bandwidth.

The figure below shows the cluster-scoped synchronization in the pipeline:

#### Level 9 APIs[#](https://rocm.blogs.amd.com#level-9-apis)

API |
Purpose |
|---|---|
Declares a |
|
Publishes the prologue and protects later stage handoffs across the cluster. |

#### Level 9 Pseudocode[#](https://rocm.blogs.amd.com#level-9-pseudocode)

```
maskA = cluster::mask(0x1111 << cluster_x);
maskB = cluster::mask(0x000F << (4 * cluster_y));
if (wave_id == 0)
tdm::load_async(A_LDS[current], A_global, maskA);
if (wave_id == 1)
tdm::load_async(B_LDS[current], B_global, maskB);
sync::wait_tdm<0>();
cluster::sync();
for each K stage:
load(A_reg[0], A_LDS[current][0]);
load(B_reg[0], B_LDS[current][0]);
if (wave_id == 0)
tdm::load_async(A_LDS[next], A_global, maskA, count_or_zero);
if (wave_id == 1)
tdm::load_async(B_LDS[next], B_global, maskB, count_or_zero);
for substep = 0 .. 2:
load(A_reg[next_reg], A_LDS[current][substep + 1]);
load(B_reg[next_reg], B_LDS[current][substep + 1]);
sync::wait_ds<DS_SUB>();
mma_ABt(C, A_reg[current_reg], B_reg[current_reg]);
swap(current_reg, next_reg);
sync::wait_ds<0>();
sync::wait_tdm<0>();
sync::arrive(); // Signal the workgroup barrier
if (wave_id == 0)
cluster::arrive(); // Signal the cluster barrier
mma_ABt(C, A_reg[current_reg], B_reg[current_reg]);
sync::wait();
cluster::wait();
swap(current, next);
```

The trace in Figure 24 shows the final WMMA group inside both barrier windows:

SIMD0 wave slot 0 has a royal-blue `TDM_WAIT`

interval around cycles 1,600–2,050. After the
drain, the workgroup signal issues at cycle 2,069, the cluster signal at 2,082, and 16 WMMA
instructions from the final `mma_ABt`

at cycles 2,101–2,221. The purple work after the blue
interval is therefore inside both barrier windows. The physical slot label does not identify
the A issuer; source `wave_id`

, not slot number, selects descriptor posters.

### Level 10: Efficient GEMM Epilogues ([gemm_epilogue.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/10_gemm_epilogue.cpp#L132-L156))[#](https://rocm.blogs.amd.com#level-10-efficient-gemm-epilogues-gemm-epilogue-cpp)

**Performance:**8% faster than Level 9.

Level 10 stages the C tile through LDS before writing it to global memory. LDS transforms the wave-local, column-major accumulator layout into a row-major tile and enables wider, coalesced stores.

**Why it helps:** Packing the C tile in LDS produces more efficient global-memory store
patterns at the end of the kernel.

The figure below illustrates the LDS-staged output epilogue:

#### Level 10 APIs[#](https://rocm.blogs.amd.com#level-10-apis)

API |
Purpose |
|---|---|
Keeps a wave issuing back-to-back WMMAs on one SIMD. |
|
Stages scattered accumulator values into LDS. |
|
Writes the assembled C tile as wider, coalesced runs. |

#### Level 10 Pseudocode[#](https://rocm.blogs.amd.com#level-10-pseudocode)

```
sched::lock_simd();
for each K stage:
// Same TDM, multicast, and split-barrier pipeline as Level 9.
sync::wait_ds<0>();
sync::wait_tdm<0>();
sync::arrive();
sync::wait();
store(C_LDS, C_acc); // C: registers -> LDS
sync::wait_ds<0>();
sync::arrive();
sync::wait();
store(C_global, C_LDS); // Coalesced C: LDS -> global
```

Figure 26 compares the two epilogues at the same time scale:

Level 9 direct epilogue |
Level 10 LDS-staged epilogue |
|---|---|
Narrow stores remain as scattered, per-column transactions after the final matrix work. |
Green and orange activity remains interleaved while the waves assemble and stream wider, coalesced stores. |

Figure 26: Direct and LDS-staged GEMM epilogues at the same time scale.

The Level 10 epilogue replaces direct per-wave stores with an explicit register-to-LDS-to-global gather-and-stream path. LDS reorganizes wave-local accumulator fragments before the global write, creating a more regular and wider store stream.

### Level 11: One Wave per SIMD ([gemm_one_wave.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/11_gemm_one_wave.cpp#L90-L114))[#](https://rocm.blogs.amd.com#level-11-one-wave-per-simd-gemm-one-wave-cpp)

**Performance:** 6% faster than Level 10.

Level 11 keeps the

The register-operand pipeline expands from two slots to three. Two K=32 substeps are prefetched before the first WMMA, allowing later LDS loads and matrix operations to be interleaved even though there are no other resident waves to hide latency. For each K block, the wave waits for the current TDM stage, prefetches substeps 0 and 1 into two register slots, executes WMMA for substep 0 while loading a later substep into the free slot, rotates the three-slot ring through all four substeps, signals the barriers around the final WMMA, and then advances to the next stage.

**Why it helps:** The larger wave-local tile increases register- and LDS-level data reuse.
Each substep can issue 64 WMMA instructions while the three-slot pipeline maintains overlap.

The figure below illustrates the one-wave-per-SIMD schedule:

#### Level 11 Pseudocode[#](https://rocm.blogs.amd.com#level-11-pseudocode)

```
sched::lock_simd();
if (wave_id == 0)
tdm::load_async(A_LDS[current], A_global, maskA);
if (wave_id == 1)
tdm::load_async(B_LDS[current], B_global, maskB);
sync::wait_tdm<0>();
cluster::sync();
for each K stage:
load(A_reg[0], A_LDS[current][0]);
load(B_reg[0], B_LDS[current][0]);
load(A_reg[1], A_LDS[current][1]);
load(B_reg[1], B_LDS[current][1]);
if (wave_id == 0)
tdm::load_async(A_LDS[next], A_global, maskA, count_or_zero);
if (wave_id == 1)
tdm::load_async(B_LDS[next], B_global, maskB, count_or_zero);
for substep = 0 .. 2:
if substep + 2 < 4:
load(A_reg[(substep + 2) % 3],
A_LDS[current][substep + 2]);
load(B_reg[(substep + 2) % 3],
B_LDS[current][substep + 2]);
sync::wait_ds<DS_SUB>();
mma_ABt(C, A_reg[substep % 3], B_reg[substep % 3]);
sync::wait_ds<0>();
sync::wait_tdm<0>();
sync::arrive();
if (wave_id == 0)
cluster::arrive();
mma_ABt(C, A_reg[final], B_reg[final]);
sync::wait();
cluster::wait();
swap(current, next);
```

Figure 28 shows how the orange LDS activity near cycles 100–350 primes the register ring. The
three long purple groups at cycles 328–787, 901–1,353, and 1,368–1,865 each contain 64
decoded WMMA instructions from an inner-loop `mma_ABt`

. Royal blue at cycles 1,869–2,100 is
the TDM drain. After the two barrier signals, the final 64-instruction WMMA group runs at
cycles 2,150–2,596 before the waits:

### Level 12: Two Waves per SIMD ([gemm_two_waves.cpp](https://github.com/HazyResearch/HipKittens/blob/1602364f4f40b5caeec0ccbbaf9ca31f784f1599/kernels/cdna5/gemm/bf16fp32/gfx1250/12_gemm_two_waves.cpp#L119-L143))[#](https://rocm.blogs.amd.com#level-12-two-waves-per-simd-gemm-two-waves-cpp)

**Performance:**6% faster than Level 11.

The final rung keeps the

A

The operand feed uses `sched_group_barrier`

instead of `compiler_fence`

. It requests six LDS
reads followed by eight matrix operations, repeated four times to cover the 24 reads and
32 matrix operations in one substep.

**Why it helps:** Two co-resident waves let the hardware scheduler issue work from one wave
while the other is waiting for data, preserving matrix utilization while improving latency
hiding.

The figure below illustrates this schedule:

#### Level 12 Helpers[#](https://rocm.blogs.amd.com#level-12-helpers)

Helper |
Purpose |
|---|---|
|
Computes one output fragment, allowing the final MMA to be split into groups of 12 and 20 instructions. |
|
A kernel helper around |

#### Level 12 Pseudocode[#](https://rocm.blogs.amd.com#level-12-pseudocode)

```
sched::lock_simd();
if (wave_id == 0)
tdm::load_async(A_LDS[current], A_global, maskA);
if (wave_id == 1)
tdm::load_async(B_LDS[current], B_global, maskB);
sync::wait_tdm<0>();
cluster::sync();
load(A_reg[0], A_LDS[current][0]);
load(B_reg[0], B_LDS[current][0]);
for each K stage:
if (wave_id == 0)
tdm::load_async(A_LDS[next], A_global, maskA, count_or_zero);
if (wave_id == 1)
tdm::load_async(B_LDS[next], B_global, maskB, count_or_zero);
for substep = 0 .. 2:
load(A_reg[(substep + 1) % 2],
A_LDS[current][substep + 1]);
load(B_reg[(substep + 1) % 2],
B_LDS[current][substep + 1]);
mma_ABt(C, A_reg[substep % 2], B_reg[substep % 2]);
pin_interleave();
mma_ABt_base(...) x 12;
sync::wait_ds<0>();
sync::wait_tdm<0>();
sync::arrive();
if (wave_id == 0)
cluster::arrive();
sync::wait();
load(A_reg[0], A_LDS[next][0]);
load(B_reg[0], B_LDS[next][0]);
mma_ABt_base(...) x 20;
pin_interleave<5, 6>();
cluster::wait();
swap(current, next);
```

The trace in Figure 30 shows the WGP cleanly interleaving instructions from the two waves resident on the SIMD. It begins with interleaved TDM descriptor setup and issue, followed by a long sequence of WMMA and LDS operations alternating between the waves. This maintains the strong WMMA utilization of Level 11 while providing more opportunities to hide latency by switching waves:

## Summary[#](https://rocm.blogs.amd.com#summary)

Many kernel-scheduling patterns that delivered high performance on the AMD Instinct MI350 and MI355X GPUs—including four-wave interleaving and eight- or sixteen-wave ping-pong schedules—translate directly to Helios. Despite the architectural changes described here, kernel developers can retain the core scheduling ideas from earlier AMD GPU generations while taking advantage of partitioned LDS, TDM, and workgroup multicast.

We plan to continue updating [HipKittens](https://github.com/HazyResearch/HipKittens) with
additional Helios kernels, optimizations, and technical discussions. Testing was performed by the authors on early-access hardware. Results may vary based on
configuration, usage, software version, firmware, and optimizations.

## Test Configuration[#](https://rocm.blogs.amd.com#test-configuration)

GPU: AMD Instinct™ MI455X GPU

Workload: BF16 GEMM with

Methodology: 500 warm-up iterations and 100 measured iterations, with L2 cache flush

Kernel implementation: HipKittens HIP/C++

Profiling: AMD Advanced Thread Trace with the ROCm Systems Profiler


## Acknowledgements[#](https://rocm.blogs.amd.com#acknowledgements)

Finally, we thank the AMD University Partnerships team for supporting this work, including Hugo Andrade, Preethi Jayadev, and Tom Papatheodore, and AMD’s Triton and HipBLASLt/TensileLite teams. We also thank our AMD colleagues Lei Zhang, Stanley Winata, Xiaohu Guo, Kumar Deepak, Bryant Nelson, Alex Brown, Brad Nemanich, Brian Shi, Majed Sujon, Ahmed Eltantawy, and Kyle Wang for their feedback and support on this work.

## Disclaimers[#](https://rocm.blogs.amd.com#disclaimers)

The information presented in this document is for informational purposes only and may contain technical inaccuracies, omissions, and typographical errors. The information contained herein is subject to change and may be rendered inaccurate for many reasons, including but not limited to product and roadmap changes, component and motherboard version changes, new model and/or product releases, product differences between differing manufacturers, software changes, BIOS flashes, firmware upgrades, or the like. Any computer system has risks of security vulnerabilities that cannot be completely prevented or mitigated. AMD assumes no obligation to update or otherwise correct or revise this information. However, AMD reserves the right to revise this information and to make changes from time to time to the content hereof without obligation of AMD to notify any person of such revisions or changes. THIS INFORMATION IS PROVIDED ‘AS IS.” AMD MAKES NO REPRESENTATIONS OR WARRANTIES WITH RESPECT TO THE CONTENTS HEREOF AND ASSUMES NO RESPONSIBILITY FOR ANY INACCURACIES, ERRORS, OR OMISSIONS THAT MAY APPEAR IN THIS INFORMATION. AMD SPECIFICALLY DISCLAIMS ANY IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, OR FITNESS FOR ANY PARTICULAR PURPOSE. IN NO EVENT WILL AMD BE LIABLE TO ANY PERSON FOR ANY RELIANCE, DIRECT, INDIRECT, SPECIAL, OR OTHER CONSEQUENTIAL DAMAGES ARISING FROM THE USE OF ANY INFORMATION CONTAINED HEREIN, EVEN IF AMD IS EXPRESSLY ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. AMD, the AMD Arrow logo, and combinations thereof are trademarks of Advanced Micro Devices, Inc. Other product names used in this publication are for identification purposes only and may be trademarks of their respective companies. © 2026 Advanced Micro Devices, Inc. All rights reserved

Third-party content is licensed to you directly by the third party that owns the content and is not licensed to you by AMD. ALL LINKED THIRD-PARTY CONTENT IS PROVIDED “AS IS” WITHOUT A WARRANTY OF ANY KIND. USE OF SUCH THIRD-PARTY CONTENT IS DONE AT YOUR SOLE DISCRETION AND UNDER NO CIRCUMSTANCES WILL AMD BE LIABLE TO YOU FOR ANY THIRD-PARTY CONTENT. YOU ASSUME ALL RISK AND ARE SOLELY RESPONSIBLE FOR ANY DAMAGES THAT MAY ARISE FROM YOUR USE OF THIRD-PARTY CONTENT.
