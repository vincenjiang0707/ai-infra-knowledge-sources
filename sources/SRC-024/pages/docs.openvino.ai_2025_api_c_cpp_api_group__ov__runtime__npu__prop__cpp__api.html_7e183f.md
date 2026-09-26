source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__runtime__npu__prop__cpp__api.html
lastmod: 

# Group Intel NPU specific properties[#](https://docs.openvino.ai#group-intel-npu-specific-properties)

-
*group*Intel NPU specific properties Set of Intel NPU specific properties.

Variables

-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<uint64_t,[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::PropertyMutability::RO> device_alloc_mem_size = {"NPU_DEVICE_ALLOC_MEM_SIZE"}[#](https://docs.openvino.ai#_CPPv421device_alloc_mem_size) [Only for NPU plugin] Type: uint64_t Read-only property to get size of already allocated NPU DDR memory (both for discrete/integrated NPU devices)

Note: Queries driver both for discrete/integrated NPU devices


-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<uint64_t,[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::PropertyMutability::RO> device_total_mem_size = {"NPU_DEVICE_TOTAL_MEM_SIZE"}[#](https://docs.openvino.ai#_CPPv421device_total_mem_size) [Only for NPU plugin] Type: uint64_t Read-only property to get size of available NPU DDR memory (both for discrete/integrated NPU devices)

Note: Queries driver both for discrete/integrated NPU devices


-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<uint32_t,[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::PropertyMutability::RO> driver_version = {"NPU_DRIVER_VERSION"}[#](https://docs.openvino.ai#_CPPv414driver_version) [Only for NPU plugin] Type: uint32_t Read-only property to get NPU driver version (for both discrete/integrated NPU devices)


-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<uint32_t,[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::PropertyMutability::RO> compiler_version = {"NPU_COMPILER_VERSION"}[#](https://docs.openvino.ai#_CPPv416compiler_version) [Only for NPU plugin] Type: uint32_t Read-only property to get NPU compiler version. Composite of Major (16bit MSB) and Minor (16bit LSB)


-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<std::string> compilation_mode_params = {"NPU_COMPILATION_MODE_PARAMS"}[#](https://docs.openvino.ai#_CPPv423compilation_mode_params) [Only for NPU compiler] Type: std::string Set various parameters supported by the NPU compiler.


-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<bool> compiler_dynamic_quantization = {"NPU_COMPILER_DYNAMIC_QUANTIZATION"}[#](https://docs.openvino.ai#_CPPv429compiler_dynamic_quantization) [Only for NPU compiler] Type: boolean Set or verify state of dynamic quantization in the NPU compiler


-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<bool> qdq_optimization = {"NPU_QDQ_OPTIMIZATION"}[#](https://docs.openvino.ai#_CPPv416qdq_optimization) [Only for NPU compiler] Type: boolean This option enables additional optimizations and balances performance and accuracy for QDQ format models, quantized using ONNX Runtime


-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<bool> qdq_optimization_aggressive = {"NPU_QDQ_OPTIMIZATION_AGGRESSIVE"}[#](https://docs.openvino.ai#_CPPv427qdq_optimization_aggressive) [Only for NPU compiler] Type: boolean This option enables additional optimizations to improve performance for QDQ format models, quantized using ONNX Runtime


-
static constexpr
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<bool> turbo = {"NPU_TURBO"}[#](https://docs.openvino.ai#_CPPv45turbo) [Only for NPU plugin] Type: std::bool Set turbo on or off. The turbo mode, where available, provides a hint to the system to maintain the maximum NPU frequency and memory throughput within the platform TDP limits. Turbo mode is not recommended for sustainable workloads due to higher power consumption and potential impact on other compute resources.


-
static constexpr