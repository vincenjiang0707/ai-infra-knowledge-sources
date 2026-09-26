source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__runtime__ocl__gpu__prop__cpp__api.html
lastmod: 

# Group Intel GPU OpenCL specific properties[#](https://docs.openvino.ai#group-intel-gpu-opencl-specific-properties)

-
*group*Intel GPU OpenCL specific properties Set of Intel GPU OpenCL specific properties.

Typedefs

-
using ThrottleLevel =
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[hint](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hintE)::[Priority](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint8PriorityE)[#](https://docs.openvino.ai#_CPPv413ThrottleLevel) This enum represents the possible value of

[ov::intel_gpu::hint::queue_throttle](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__ocl__gpu__prop__cpp__api_1gace6031a0761c1917aa84135fe2163d56)property:LOW is used for CL_QUEUE_THROTTLE_LOW_KHR OpenCL throttle hint

MEDIUM (DEFAULT) is used for CL_QUEUE_THROTTLE_MED_KHR OpenCL throttle hint

HIGH is used for CL_QUEUE_THROTTLE_HIGH_KHR OpenCL throttle hint



Variables

-
static constexpr Property<uint64_t, PropertyMutability::RO> device_total_mem_size = {"GPU_DEVICE_TOTAL_MEM_SIZE"}
Read-only property which defines size of memory in bytes available for the device. For iGPU it returns host memory size, for dGPU - dedicated gpu memory size.


-
static constexpr Property<uint64_t, PropertyMutability::RO> device_max_alloc_mem_size = {"GPU_DEVICE_MAX_ALLOC_MEM_SIZE"}
[#](https://docs.openvino.ai#_CPPv425device_max_alloc_mem_size) Read-only property which defines max size of memory object allocation in bytes.


-
static constexpr Property<std::string, PropertyMutability::RO> uarch_version = {"GPU_UARCH_VERSION"}
[#](https://docs.openvino.ai#_CPPv413uarch_version) Read-only property to get microarchitecture identifier in major.minor.revision format.


-
static constexpr Property<int32_t, PropertyMutability::RO> execution_units_count = {"GPU_EXECUTION_UNITS_COUNT"}
[#](https://docs.openvino.ai#_CPPv421execution_units_count) Read-only property to get count of execution units for current GPU.


-
static constexpr Property<std::map<std::string, uint64_t>, PropertyMutability::RO> memory_statistics{"GPU_MEMORY_STATISTICS"}
[#](https://docs.openvino.ai#_CPPv417memory_statistics) Read-only property to get statistics of GPU memory allocated by engine for each allocation type It contains information about current memory usage.


-
static constexpr Property<bool> enable_loop_unrolling = {"GPU_ENABLE_LOOP_UNROLLING"}
[#](https://docs.openvino.ai#_CPPv421enable_loop_unrolling) Turning on this key enables to unroll recurrent layers such as TensorIterator or Loop with fixed iteration count. This key is turned on by default. Turning this key on will achieve better inference performance for loops with not too many iteration counts (less than 16, as a rule of thumb). Turning this key off will achieve better performance for both graph loading time and inference time with many iteration counts (greater than 16). Note that turning this key on will increase the graph loading time in proportion to the iteration counts. Thus, this key should be turned off if graph loading time is considered to be most important target to optimize.


-
static constexpr Property<bool> disable_winograd_convolution = {"GPU_DISABLE_WINOGRAD_CONVOLUTION"}
[#](https://docs.openvino.ai#_CPPv428disable_winograd_convolution) Turning on this key disables winograd convolution. Winograd convolution has different characteristics for accuracy and performance compared to other convolution implementations.


-
static constexpr Property<
[ThrottleLevel](https://docs.openvino.ai#_CPPv413ThrottleLevel)> queue_throttle = {"GPU_QUEUE_THROTTLE"}[#](https://docs.openvino.ai#_CPPv414queue_throttle) This key instructs the GPU plugin to use OpenCL queue throttle hints as defined in

[https://www.khronos.org/registry/OpenCL/specs/opencl-2.1-extensions.pdf](https://www.khronos.org/registry/OpenCL/specs/opencl-2.1-extensions.pdf), chapter 9.19. This option should be used with[ov::intel_gpu::hint::ThrottleLevel](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__ocl__gpu__prop__cpp__api_1gabeb80bf9522a2518878afb54e3fd2204)values.

-
static constexpr Property<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[hint](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hintE)::[Priority](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint8PriorityE)> queue_priority = {"GPU_QUEUE_PRIORITY"}[#](https://docs.openvino.ai#_CPPv414queue_priority) This key instructs the GPU plugin to use the OpenCL queue priority hint as defined in

[https://www.khronos.org/registry/OpenCL/specs/opencl-2.1-extensions.pdf](https://www.khronos.org/registry/OpenCL/specs/opencl-2.1-extensions.pdf). This option should be used with[ov::hint::Priority](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__cpp__prop__api_1ga3e74923a1ee02f6f5067a368418f0442):LOW is used for CL_QUEUE_PRIORITY_LOW_KHR OpenCL priority hint

MEDIUM (DEFAULT) is used for CL_QUEUE_PRIORITY_MED_KHR OpenCL priority hint

HIGH is used for CL_QUEUE_PRIORITY_HIGH_KHR OpenCL priority hint



-
static constexpr Property<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[hint](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hintE)::[Priority](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint8PriorityE)> host_task_priority = {"GPU_HOST_TASK_PRIORITY"}[#](https://docs.openvino.ai#_CPPv418host_task_priority) This key instructs the GPU plugin which cpu core type of TBB affinity used in load network. This option has 3 types of levels: HIGH, LOW, and ANY. It is only affected on Hybrid CPUs.

LOW - instructs the GPU Plugin to use LITTLE cores if they are available

MEDIUM (DEFAULT) - instructs the GPU Plugin to use any available cores (BIG or LITTLE cores)

HIGH - instructs the GPU Plugin to use BIG cores if they are available



-
static constexpr Property<int64_t> available_device_mem = {"AVAILABLE_DEVICE_MEM_SIZE"}
[#](https://docs.openvino.ai#_CPPv420available_device_mem) This key identifies available device memory size in bytes.


-
static constexpr Property<bool> enable_sdpa_optimization = {"GPU_ENABLE_SDPA_OPTIMIZATION"}
[#](https://docs.openvino.ai#_CPPv424enable_sdpa_optimization) Turning on this key disables SDPA operation decomposition and keeps SDPA operation in the graph. Enabling SDPA optimization may provide performance improvements and memory usage reduction. This key serves as a recommendation and may be ignored in known sub-optimal cases.


-
static constexpr Property<bool> enable_lora_operation = {"GPU_ENABLE_LORA_OPERATION"}
[#](https://docs.openvino.ai#_CPPv421enable_lora_operation) Turning on this key enables LoRA operation, otherwise the graph will remain in its original form with the decomposed LoRA subgraph. Enabling LoRA operation may provide performance improvements, but has stricter restrictions: LoRA rank must be less than or equal to 256 and divisible by 16.


-
static constexpr Property<bool> enable_kernels_reuse = {"GPU_ENABLE_KERNELS_REUSE"}
[#](https://docs.openvino.ai#_CPPv420enable_kernels_reuse) Turning on this property enables kernels reuse between implementations, resulting in a lower memory footprint. However, as a drawback, OpenCL set_arguments() call will be made more often, resulting in higher host pressure and slower execution in some host-bottleneck cases. This property is available only for single-stream scenarios and will be ignored in other cases.


-
static constexpr Property<bool> enable_large_allocations = {"GPU_ENABLE_LARGE_ALLOCATIONS"}
[#](https://docs.openvino.ai#_CPPv424enable_large_allocations) Turning on this key switches addressing mode to allow allocations larger than 4GB as described here:

[intel/compute-runtime](https://github.com/intel/compute-runtime/blob/master/programmers-guide/ALLOCATIONS_GREATER_THAN_4GB.md#creating-allocations-greater-than-4GB)Note: Performance may be lower with this option enabled.

-
static constexpr auto surface = "GPU_SURFACE"
[#](https://docs.openvino.ai#_CPPv47surface) Native video decoder surface.


-
static constexpr const auto HW_MATMUL = "GPU_HW_MATMUL"
[#](https://docs.openvino.ai#_CPPv49HW_MATMUL) Device has hardware block for matrix multiplication.


-
static constexpr const auto USM_MEMORY = "GPU_USM_MEMORY"
[#](https://docs.openvino.ai#_CPPv410USM_MEMORY) Device supports unified shared memory.


-
using ThrottleLevel =