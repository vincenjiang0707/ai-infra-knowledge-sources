source: https://rocm.docs.amd.com/en/docs-7.2.4/reference/glossary/performance.html

# Performance analysis glossary[#](https://rocm.docs.amd.com#performance-analysis-glossary)

2026-02-20

3 min read time

This section provides brief definitions of performance analysis concepts and optimization techniques.

- Active cycle
[#](https://rocm.docs.amd.com#term-Active-cycle) An active cycle is a clock cycle in which a

[compute unit](https://rocm.docs.amd.com/device-hardware.html#term-Compute-units)has at least one active[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/rocPRIM-glossary.html#term-Wavefront)resident. See[Warp (Wavefront) execution states](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#wavefront-execution)for details.- Arithmetic bandwidth
[#](https://rocm.docs.amd.com#term-Arithmetic-bandwidth) Arithmetic bandwidth is the peak rate at which arithmetic work can be performed, defining the compute roof in

[roofline models](https://rocm.docs.amd.com#term-Roofline-model). See[Compute-bound performance](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#compute-bound)for details.- Arithmetic intensity
[#](https://rocm.docs.amd.com#term-Arithmetic-intensity) Arithmetic intensity is the ratio of arithmetic operations to memory operations in a kernel, and determines performance characteristics. See

[Arithmetic intensity](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#arithmetic-intensity)for intensity analysis.- Bank conflict
[#](https://rocm.docs.amd.com#term-Bank-conflict) A bank conflict occurs when multiple threads simultaneously access different addresses in the same

[LDS bank](https://rocm.docs.amd.com/device-hardware.html#term-Local-data-share), serializing accesses. See[Bank conflict theory](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#bank-conflicts-theory)for details.- Branch efficiency
[#](https://rocm.docs.amd.com#term-Branch-efficiency) Branch efficiency measures how often all threads within a

[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/rocPRIM-glossary.html#term-Wavefront)take the same execution path, quantifying control-flow uniformity. See[Branch efficiency](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#branch-efficiency)for branch analysis.- Compute-bound
[#](https://rocm.docs.amd.com#term-Compute-bound) Compute-bound kernels are limited by the

[arithmetic bandwidth](https://rocm.docs.amd.com#term-Arithmetic-bandwidth)of the GPU’s[compute units](https://rocm.docs.amd.com/device-hardware.html#term-Compute-units)rather than[memory bandwidth](https://rocm.docs.amd.com#term-Memory-bandwidth). See[Compute-bound performance](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#compute-bound)for compute-bound analysis.- CU utilization
[#](https://rocm.docs.amd.com#term-CU-utilization) CU utilization measures the percentage of time that

[compute units](https://rocm.docs.amd.com/device-hardware.html#term-Compute-units)are actively executing instructions. See[CU utilization](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#cu-utilization)for utilization analysis.- Issue efficiency
[#](https://rocm.docs.amd.com#term-Issue-efficiency) Issue efficiency measures how effectively the

[wavefront scheduler](https://rocm.docs.amd.com/device-hardware.html#term-Wavefront-scheduler)keeps execution pipelines busy by issuing instructions. See[Issue efficiency](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#issue-efficiency)for efficiency metrics.- Latency hiding
[#](https://rocm.docs.amd.com#term-Latency-hiding) Latency hiding masks long-latency operations by running many concurrent threads, keeping execution pipelines busy. See

[Latency hiding mechanisms](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#latency-hiding)for details.- Little’s Law
[#](https://rocm.docs.amd.com#term-Little-s-Law) Little’s Law relates concurrency, latency, and throughput, determining how much independent work must be in flight to hide latency. See

[Little’s Law](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#littles-law)for latency hiding details.- Memory bandwidth
[#](https://rocm.docs.amd.com#term-Memory-bandwidth) Memory bandwidth is the maximum rate at which data can be transferred between memory hierarchy levels, typically measured in bytes per second. See

[Memory-bound performance](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#memory-bound)for details.- Memory coalescing
[#](https://rocm.docs.amd.com#term-Memory-coalescing) Memory coalescing improves

[memory bandwidth](https://rocm.docs.amd.com#term-Memory-bandwidth)by servicing many logical loads or stores with fewer physical memory transactions. See[Memory coalescing theory](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#memory-coalescing-theory)for coalescing patterns.- Memory-bound
[#](https://rocm.docs.amd.com#term-Memory-bound) Memory-bound kernels are limited by

[memory bandwidth](https://rocm.docs.amd.com#term-Memory-bandwidth)rather than[arithmetic bandwidth](https://rocm.docs.amd.com#term-Arithmetic-bandwidth), typically due to low[arithmetic intensity](https://rocm.docs.amd.com#term-Arithmetic-intensity). See[Memory-bound performance](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#memory-bound)for memory-bound analysis.- Occupancy
[#](https://rocm.docs.amd.com#term-Occupancy) Occupancy is the ratio of active

[wavefronts](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/rocPRIM-glossary.html#term-Wavefront)to the maximum number of wavefronts that can be active on a[compute unit](https://rocm.docs.amd.com/device-hardware.html#term-Compute-units). See[Occupancy theory](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#occupancy)for occupancy analysis.- Overhead
[#](https://rocm.docs.amd.com#term-Overhead) Overhead latency is the time spent with no useful work being done, often due to CPU-side bottlenecks or kernel launch delays. See

[Performance bottlenecks](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#performance-bottlenecks)for details.- Peak rate
[#](https://rocm.docs.amd.com#term-Peak-rate) Peak rate is the theoretical maximum throughput at which a hardware system can complete work under ideal conditions. See

[Theoretical performance limits](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#theoretical-performance-limits)for details.- Pipe utilization
[#](https://rocm.docs.amd.com#term-Pipe-utilization) Pipe utilization measures how effectively a kernel uses the execution pipelines within each

[compute unit](https://rocm.docs.amd.com/device-hardware.html#term-Compute-units). See[Pipe utilization](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#pipe-utilization)for utilization details.- Register pressure
[#](https://rocm.docs.amd.com#term-Register-pressure) Register pressure occurs when excessive register demand limits the number of active

[wavefronts](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/rocPRIM-glossary.html#term-Wavefront)per[compute unit](https://rocm.docs.amd.com/device-hardware.html#term-Compute-units), reducing[occupancy](https://rocm.docs.amd.com#term-Occupancy). See[Register pressure theory](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#register-pressure-theory)for details.- Roofline model
[#](https://rocm.docs.amd.com#term-Roofline-model) The roofline model is a visual performance model that determines whether a program is

[compute-bound](https://rocm.docs.amd.com#term-Compute-bound)or[memory-bound](https://rocm.docs.amd.com#term-Memory-bound). See[Roofline model](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#roofline-model)for roofline analysis.- Wavefront divergence
[#](https://rocm.docs.amd.com#term-Wavefront-divergence) Wavefront divergence occurs when threads within a

[wavefront](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/rocPRIM-glossary.html#term-Wavefront)take different execution paths due to conditional statements. See[Branch efficiency](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#branch-efficiency)for divergence handling details.- Wavefront execution state
[#](https://rocm.docs.amd.com#term-Wavefront-execution-state) Wavefront execution states (

*active*,*stalled*,*eligible*,*selected*) describe the scheduling status of[wavefronts](https://rocm.docs.amd.com/projects/rocPRIM/en/docs-7.2.4/reference/rocPRIM-glossary.html#term-Wavefront)on AMD GPUs. See[Warp (Wavefront) execution states](https://rocm.docs.amd.com/projects/HIP/en/docs-7.2.4/understand/performance_optimization.html#wavefront-execution)for state definitions.