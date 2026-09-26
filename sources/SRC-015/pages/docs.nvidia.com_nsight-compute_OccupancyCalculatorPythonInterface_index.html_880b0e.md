source: https://docs.nvidia.com/nsight-compute/OccupancyCalculatorPythonInterface/index.html

# 4. Occupancy Calculator Python Interface[#](https://docs.nvidia.com#occupancy-calculator-python-interface)

## 4.1. Introduction[#](https://docs.nvidia.com#introduction)

NVIDIA Nsight Compute features a Python-based interface for performing occupancy calculations and analysis for kernels on NVIDIA GPUs. These APIs are designed to help developers understand and optimize the utilization of GPU resources to achieve better performance for their kernel.

The module is called [ ncu_occupancy](https://docs.nvidia.com#module-ncu_occupancy) and works on any Python version from 3.7

[[1]](https://docs.nvidia.com#fn1). It can be found in the

`extras/python`

directory of your NVIDIA
Nsight Compute package.## 4.2. API Reference[#](https://docs.nvidia.com#api-reference)

This documents the content of the [ ncu_occupancy](https://docs.nvidia.com#module-ncu_occupancy) package which can be found
in the

`extras/python`

directory of your NVIDIA Nsight Compute installation.-
*class*ncu_occupancy.OccupancyCalculator[#](https://docs.nvidia.com#ncu_occupancy.OccupancyCalculator) Provide methods to calculate occupancy and analyze ways to improve it, for a given GPU.

- Parameters:
- Returns:
An instance of the occupancy calculator.

- Return type:

- get_occupancy_limiters(
*occupancy_parameters:*,[OccupancyParameters](https://docs.nvidia.com#ncu_occupancy.OccupancyParameters)Get the occupancy limiters for the given occupancy parameters.

- Parameters:
**occupancy_parameters**() – The input parameters for the occupancy calculation.`OccupancyParameters`

- Returns:


[list](https://docs.python.org/3/library/stdtypes.html#list)[#](https://docs.nvidia.com#ncu_occupancy.OccupancyCalculator.get_occupancy_limiters)- get_optimal_occupancy(
*occupancy_parameters:*,[OccupancyParameters](https://docs.nvidia.com#ncu_occupancy.OccupancyParameters)*occupancy_variable_list:*,[list](https://docs.python.org/3/library/stdtypes.html#list)= [OccupancyVariable.THREADS_PER_BLOCK]Get the optimal occupancy configuration.

Optimal occupancy is calculated by varying input occupancy variable values while keeping other occupancy variable values constant. If no input occupancy variable list provided then

will be considered by default.`OccupancyVariable.THREADS_PER_BLOCK`

- Parameters:
**occupancy_parameters**() – The input parameters for the occupancy calculation.`OccupancyParameters`

**occupancy_variable_list**(of`list`

, optional) – The list of occupancy variables to consider for optimal occupancy calculation. Only up to two occupancy variables can be specified. (default:`OccupancyVariable`

)`OccupancyVariable.THREADS_PER_BLOCK`


- Returns:
- The optimal occupancy configuration. The dictionary contains the following key-value pairs:
’optimal_occupancy’: (

) The optimal occupancy.`float`



- Return type:


[dict](https://docs.python.org/3/library/stdtypes.html#dict)[#](https://docs.nvidia.com#ncu_occupancy.OccupancyCalculator.get_optimal_occupancy)- get_resource_utilization(
*occupancy_parameters:*,[OccupancyParameters](https://docs.nvidia.com#ncu_occupancy.OccupancyParameters)Get the resource utilization for the given occupancy parameters.

- Parameters:
**occupancy_parameters**() – The input parameters for the occupancy calculation.`OccupancyParameters`

- Returns:
- Resource utilization. The dictionary contains the following key-value pairs:
’sm_occupancy’ : (

) The occupancy of the SMs.`float`

’allocated_blocks’ : (

) The number of allocated blocks out of the total possible blocks per SM.`int`

- ’resource_utilization’(
) The resource utilization for each resource i.e. threads, registers, shared memory. The resource utilization dictionary contains the following key-value pairs:`dict`

- ’<resource name>’: (
) The resource utilization for the resource. The resource utilization dictionary contains the following key-value pairs:`dict`


- ’<resource name>’: (


- ’resource_utilization’(


- Return type:


[dict](https://docs.python.org/3/library/stdtypes.html#dict)[#](https://docs.nvidia.com#ncu_occupancy.OccupancyCalculator.get_resource_utilization)- get_sm_occupancy(
*occupancy_parameters:*,[OccupancyParameters](https://docs.nvidia.com#ncu_occupancy.OccupancyParameters)Calculate the occupancy of the SMs for the given occupancy parameters.

- Parameters:
**occupancy_parameters**() – The input parameters for the occupancy calculation.`OccupancyParameters`

- Returns:
The occupancy of the SMs.

- Return type:


[float](https://docs.python.org/3/library/functions.html#float)[#](https://docs.nvidia.com#ncu_occupancy.OccupancyCalculator.get_sm_occupancy)

-
*class*ncu_occupancy.OccupancyLimiter[#](https://docs.nvidia.com#ncu_occupancy.OccupancyLimiter) Enum representing the occupancy limiters.

-
REGISTERS
[#](https://docs.nvidia.com#ncu_occupancy.OccupancyLimiter.REGISTERS) Register usage is the occupancy limiter.


-
SHARED_MEMORY
[#](https://docs.nvidia.com#ncu_occupancy.OccupancyLimiter.SHARED_MEMORY) Shared memory usage is the occupancy limiter.


-
BLOCKS
[#](https://docs.nvidia.com#ncu_occupancy.OccupancyLimiter.BLOCKS) Block size is the occupancy limiter.


-
BARRIERS
[#](https://docs.nvidia.com#ncu_occupancy.OccupancyLimiter.BARRIERS) Barrier usage is the occupancy limiter.


-
__new__(
*value*)[#](https://docs.nvidia.com#ncu_occupancy.OccupancyLimiter.__new__)

-
REGISTERS

-
*class*ncu_occupancy.OccupancyParameters[#](https://docs.nvidia.com#ncu_occupancy.OccupancyParameters) OccupancyParameters is a

`dataclass`

that holds configuration parameters for occupancy calculations.Shared memory size configuration (bytes). (default: 0)

- Type:


Shared memory (bytes) per block. (default: 2048)

- Type:



-
*class*ncu_occupancy.OccupancyVariable[#](https://docs.nvidia.com#ncu_occupancy.OccupancyVariable) Enum representing the occupancy variables.

-
THREADS_PER_BLOCK
[#](https://docs.nvidia.com#ncu_occupancy.OccupancyVariable.THREADS_PER_BLOCK) Threads per block.


-
REGISTERS_PER_THREAD
[#](https://docs.nvidia.com#ncu_occupancy.OccupancyVariable.REGISTERS_PER_THREAD) Registers per thread.


-
SHARED_MEMORY_PER_BLOCK
[#](https://docs.nvidia.com#ncu_occupancy.OccupancyVariable.SHARED_MEMORY_PER_BLOCK) Shared memory per block.


-
BLOCK_BARRIERS
[#](https://docs.nvidia.com#ncu_occupancy.OccupancyVariable.BLOCK_BARRIERS) Block barriers.


-
__new__(
*value*)[#](https://docs.nvidia.com#ncu_occupancy.OccupancyVariable.__new__)

-
THREADS_PER_BLOCK

-
ncu_occupancy.get_gpu_data(
*major:*,[int](https://docs.python.org/3/library/functions.html#int)*minor:*)[int](https://docs.python.org/3/library/functions.html#int)[dict](https://docs.python.org/3/library/stdtypes.html#dict)[#](https://docs.nvidia.com#ncu_occupancy.get_gpu_data) Get the GPU data for the given compute capability version.

- Parameters:
- Returns:
- The GPU data for the given compute capability version. The dictionary contains the following key-value pairs:
’cc_major’: (

) The major compute capability version of the GPU.`int`

’cc_minor’: (

) The minor compute capability version of the GPU.`int`

’sm_version’: (

) The SM version of the GPU.`str`

’chip_family’: (

) The chip family of the GPU.`str`

’threads_per_warp’: (

) The number of threads per warp.`int`

’max_warps_per_sm’: (

) The number of warps per SM.`int`

’max_threads_per_sm’: (

) The number of threads per SM.`int`

’max_thread_blocks_per_sm’: (

) The number of thread blocks per SM.`int`

’block_barriers_per_sm’: (

) The number of block barriers per SM.`int`

’smem_per_sm’: (

) The shared memory (bytes) per SM.`int`

’max_shared_mem_per_block’: (

) The maximum shared memory (bytes) per block.`int`

’registers_per_sm’: (

) The registers per SM.`int`

’max_regs_per_block’: (

) The maximum registers per block.`int`

’max_regs_per_thread’: (

) The maximum registers per thread.`int`

’reg_allocation_unit_size’: (

) The register allocation unit size.`int`

’reg_allocation_granularity’: (

) The register allocation granularity.`str`

’shared_mem_allocation_unit_size’: (

) The shared memory allocation unit size.`int`

’warps_allocation_granularity’: (

) The warp allocation granularity.`str`

’max_thread_block_size’: (

) The maximum thread block size.`int`

’shared_mem_size_configs’: (

of`list`

) The shared memory size configurations (bytes).`int`

’warp_reg_allocation_granularities’: (

of`list`

) The warp register allocation granularities.`int`



- Return type: