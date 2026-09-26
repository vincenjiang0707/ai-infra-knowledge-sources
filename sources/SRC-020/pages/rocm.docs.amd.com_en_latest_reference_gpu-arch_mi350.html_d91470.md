source: https://rocm.docs.amd.com/en/latest/reference/gpu-arch/mi350.html

# AMD Instinct MI350 Series microarchitecture[#](https://rocm.docs.amd.com#amd-instinct-mi350-series-microarchitecture)

The AMD Instinct™ MI350 Series GPUs are based on the AMD CDNA4 architecture, and are designed for AI, HPC, and machine learning workloads. The series includes the MI350X (1000W, air-cooled) and the MI355X (1400W, direct liquid-cooled), both in the OAM form factor, and the MI350P, a PCIe card (600W, configurable to 450W) for deployment in mainstream servers.

Each MI350X and MI355X GPU integrates eight vertically stacked accelerator complex dies (XCDs) and two I/O dies (IODs) tied together with AMD Infinity Fabric™ technology on-package, connecting to eight stacks of 12-Hi HBM3E memory. The MI350P is a smaller configuration, integrating four XCDs and a single IOD connected to four HBM3E stacks.

## Chiplet architecture[#](https://rocm.docs.amd.com#chiplet-architecture)

The CDNA4 architecture uses a chiplet-based, heterogeneous design in which each chiplet uses a manufacturing process suited to its function.

The accelerator complex dies (XCDs) house the computational portion of the processor and the lowest levels of the cache hierarchy. They are built on TSMC’s N3P process to take advantage of improved logic density and performance. The I/O dies (IODs) contain the AMD Infinity Cache™, memory controllers, and interconnects. These functions do not benefit from the latest process technology and are implemented on TSMC’s N6 process.

The CDNA4 architecture consolidates the IOD functions into two larger dies rather than the four smaller IODs of the prior generation. The direct connection between the two IODs reduces latency and power consumption compared to the previous generation.

## Compute units[#](https://rocm.docs.amd.com#compute-units)

Each XCD comprises 36 AMD CDNA4 compute units (CUs) organized as four arrays of nine CUs, of which 32 are active. On the MI350X and MI355X, the processor spans eight XCDs for up to 256 CUs total. The MI350P spans four XCDs for up to 128 CUs total.

Each CU instantiates a full processor pipeline with highly threaded and parallel execution of scalar, vector, and matrix instructions, along with a memory pipeline with an L1 data cache and a Local Data Share (LDS). The 64 KB, 8-way set-associative instruction cache is shared between two adjacent CUs.

The LDS in each CDNA4 CU is 160 KB with doubled read bandwidth compared to the prior generation, which improves the utilization of the vector and matrix execution resources for matrix multiply routines.

### Matrix cores and precision support[#](https://rocm.docs.amd.com#matrix-cores-and-precision-support)

The CDNA4 Matrix Cores add hardware support for industry-standard micro-scaling (OCP MX) formats including MXFP8, MXFP6, and MXFP4, alongside existing formats such as FP16, BF16, FP8, and INT8. Execution resources for 16-bit and smaller data types are twice as many as in the prior generation.

## Memory hierarchy[#](https://rocm.docs.amd.com#memory-hierarchy)

The L1 vector data cache in each CU is 32KB with 128B cache lines and 64-way associativity. Each XCD shares a 4MB, 16-way set-associative L2 cache with 16 parallel channels.

On the MI350X and MI355X, the AMD Infinity Cache™ is a shared 256MB memory-side cache in the IODs. The HBM3E memory interfaces operate at 8 Gbps, providing up to 8 TB/s of peak theoretical memory bandwidth and 288GB of total capacity (36GB per stack). The MI350P provides a 128MB Infinity Cache in its single IOD, up to 4 TB/s of peak theoretical memory bandwidth, and 144GB of total capacity across four HBM3E stacks.

## Performance[#](https://rocm.docs.amd.com#performance)

The following table lists the peak theoretical performance of the MI350 Series GPUs for different data types. The MI350P figures reflect its four-XCD configuration.

Computation and data type |
MI350X peak theoretical |
MI355X peak theoretical |
MI350P peak theoretical |
|---|---|---|---|
Matrix FP64 |
72.1 TF |
78.6 TF |
36 TF |
Vector FP64 |
72.1 TF |
78.6 TF |
36 TF |
Matrix FP32 |
144.2 TF |
157.3 TF |
72 TF |
Vector FP32 |
144.2 TF |
157.3 TF |
72 TF |
Matrix FP16 | FP16 Sparsity |
2.3 PF | 4.6 PF |
2.5 PF | 5.0 PF |
1.15 PF | 2.3 PF |
Vector FP16 |
144.2 TF |
157.3 TF |
72 TF |
Matrix BF16 | BF16 Sparsity |
2.3 PF | 4.6 PF |
2.5 PF | 5.0 PF |
1.15 PF | 2.3 PF |
Matrix OCP-FP8 | OCP-FP8 Sparsity |
4.6 PF | 9.2 PF |
5.0 PF | 10 PF |
2.3 PF | 4.6 PF |
Matrix MXFP8 |
4.6 PF |
5.0 PF |
2.3 PF |
Matrix MXFP6 / MXFP4 |
9.2 PF |
10 PF |
4.6 PF |
Matrix INT8 | INT8 Sparsity |
4.6 POPs | 9.2 POPs |
5.0 POPs | 10 POPs |
2.3 POPs | 4.6 POPs |

## Node-level architecture[#](https://rocm.docs.amd.com#node-level-architecture)

The MI350X and MI355X use a fully connected 8-GPU node topology, identical to the prior generation. Each GPU connects to the host via one PCIe Gen 5 x16 link and communicates with other GPUs through 7 AMD Infinity Fabric links operating at 38.4 Gbps, providing over 1 TB/s of aggregate communication bandwidth per GPU.

The MI350X uses the OAM form factor on a UBB8 baseboard compatible with prior generation AMD Instinct MI325X platform designs. The MI355X uses the same form factor but targets direct liquid-cooled infrastructure.

The MI350P is a full-height, full-length, dual-slot PCIe card that connects to the host via one PCIe Gen 5 x16 link. It is designed for air-cooled servers, with up to eight cards per server.

## Compute and memory partitioning[#](https://rocm.docs.amd.com#compute-and-memory-partitioning)

The MI350 Series supports spatial partitioning along XCD boundaries. On the MI350X and MI355X, the GPU can be divided into 1, 2, 4, or 8 compute partitions with full isolation between partitions. Memory can be configured in NPS1 mode, interleaving across all 8 HBM stacks, or NPS2 mode, which partitions the 288GB into two 144GB pools, one per IOD, to reduce cross-IOD Infinity Fabric traffic and improve latency and efficiency. Because the MI350P has a single IOD, it supports up to four compute partitions and a single (NPS1) memory partition across its 144GB.