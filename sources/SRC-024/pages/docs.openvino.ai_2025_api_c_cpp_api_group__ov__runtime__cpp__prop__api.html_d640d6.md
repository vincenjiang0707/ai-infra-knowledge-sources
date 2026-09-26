source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__runtime__cpp__prop__api.html
lastmod: 

# Group Device properties[#](https://docs.openvino.ai#group-device-properties)

-
*group*Device properties Enums

-
enum class SchedulePolicy
[#](https://docs.openvino.ai#_CPPv414SchedulePolicy) Enum to define the policy of scheduling inference request to target device in cumulative throughput mode on AUTO.

*Values:*-
enumerator ROUND_ROBIN
[#](https://docs.openvino.ai#_CPPv4N14SchedulePolicy11ROUND_ROBINE)

-
enumerator DEVICE_PRIORITY
[#](https://docs.openvino.ai#_CPPv4N14SchedulePolicy15DEVICE_PRIORITYE)

-
enumerator DEFAULT
[#](https://docs.openvino.ai#_CPPv4N14SchedulePolicy7DEFAULTE) Default schedule policy is DEVICE_PRIORITY.


-
enumerator ROUND_ROBIN

-
enum class Priority
[#](https://docs.openvino.ai#_CPPv48Priority) Enum to define possible priorities hints.

*Values:*-
enumerator LOW
[#](https://docs.openvino.ai#_CPPv4N8Priority3LOWE) Low priority.


-
enumerator MEDIUM
[#](https://docs.openvino.ai#_CPPv4N8Priority6MEDIUME) Medium priority.


-
enumerator HIGH
[#](https://docs.openvino.ai#_CPPv4N8Priority4HIGHE) High priority.


-
enumerator DEFAULT
[#](https://docs.openvino.ai#_CPPv4N8Priority7DEFAULTE) Default priority is MEDIUM.


-
enumerator LOW

-
enum class PerformanceMode
[#](https://docs.openvino.ai#_CPPv415PerformanceMode) Enum to define possible performance mode hints.

*Values:*-
enumerator LATENCY
[#](https://docs.openvino.ai#_CPPv4N15PerformanceMode7LATENCYE) Optimize for latency.


-
enumerator THROUGHPUT
[#](https://docs.openvino.ai#_CPPv4N15PerformanceMode10THROUGHPUTE) Optimize for throughput.


-
enumerator CUMULATIVE_THROUGHPUT
[#](https://docs.openvino.ai#_CPPv4N15PerformanceMode21CUMULATIVE_THROUGHPUTE) Optimize for cumulative throughput.


-
enumerator LATENCY

-
enum class ExecutionMode
[#](https://docs.openvino.ai#_CPPv413ExecutionMode) Enum to define possible execution mode hints.

*Values:*-
enumerator PERFORMANCE
[#](https://docs.openvino.ai#_CPPv4N13ExecutionMode11PERFORMANCEE) Optimize for max performance, may apply properties which slightly affect accuracy.


-
enumerator ACCURACY
[#](https://docs.openvino.ai#_CPPv4N13ExecutionMode8ACCURACYE) Optimize for max accuracy.


-
enumerator PERFORMANCE

-
enum class Level
[#](https://docs.openvino.ai#_CPPv45Level) Enum to define possible log levels.

*Values:*-
enumerator NO
[#](https://docs.openvino.ai#_CPPv4N5Level2NOE) disable any logging


-
enumerator ERR
[#](https://docs.openvino.ai#_CPPv4N5Level3ERRE) error events that might still allow the application to continue running


-
enumerator WARNING
[#](https://docs.openvino.ai#_CPPv4N5Level7WARNINGE) potentially harmful situations which may further lead to ERROR


-
enumerator INFO
[#](https://docs.openvino.ai#_CPPv4N5Level4INFOE) informational messages that display the progress of the application at coarse-grained level


-
enumerator DEBUG
[#](https://docs.openvino.ai#_CPPv4N5Level5DEBUGE) fine-grained events that are most useful to debug an application.


-
enumerator TRACE
[#](https://docs.openvino.ai#_CPPv4N5Level5TRACEE) finer-grained informational events than the DEBUG


-
enumerator NO

-
enum class WorkloadType
[#](https://docs.openvino.ai#_CPPv412WorkloadType) Enum to define possible workload types.

Workload type represents the execution priority for an inference.

*Values:*-
enumerator DEFAULT
[#](https://docs.openvino.ai#_CPPv4N12WorkloadType7DEFAULTE)

-
enumerator EFFICIENT
[#](https://docs.openvino.ai#_CPPv4N12WorkloadType9EFFICIENTE)

-
enumerator DEFAULT

Variables

-
static constexpr Property<std::vector<PropertyName>, PropertyMutability::RO> supported_properties{"INTERNAL_SUPPORTED_PROPERTIES"}
[#](https://docs.openvino.ai#_CPPv420supported_properties) Read-only property to get a std::vector<PropertyName> of supported internal properties.


-
static constexpr Property<uint32_t, PropertyMutability::RO> cache_header_alignment = {"CACHE_HEADER_ALIGNMENT"}
[#](https://docs.openvino.ai#_CPPv422cache_header_alignment) Read-only property to get plugin specific needed alignment for cache header.


-
static constexpr Property<
[SchedulePolicy](https://docs.openvino.ai#_CPPv414SchedulePolicy)> schedule_policy = {"SCHEDULE_POLICY"}[#](https://docs.openvino.ai#_CPPv415schedule_policy) High-level OpenVINO model policy hint Defines what scheduling policy should be used in AUTO CUMULATIVE_THROUGHPUT or MULTI case.


-
static constexpr Property<uint64_t, PropertyMutability::RW> dynamic_quantization_group_size_max{"GPU_DYNAMIC_QUANTIZATION_GROUP_SIZE_MAX"}
[#](https://docs.openvino.ai#_CPPv435dynamic_quantization_group_size_max) This property defines maximum group size for dynamic quantization optimization.

If dynamic_quantization_group_size is larger than this max value, dynamic quantization will be disabled. This property is intended to be set from model rt-info to limit dynamic quantization group size for certain models.


-
static constexpr Property<std::vector<PropertyName>, PropertyMutability::RO> supported_properties{"SUPPORTED_PROPERTIES"}
Read-only property to get a std::vector<PropertyName> of supported read-only properties. This can be used as a compiled model property as well.


-
static constexpr Property<std::vector<std::string>, PropertyMutability::RO> available_devices = {"AVAILABLE_DEVICES"}
[#](https://docs.openvino.ai#_CPPv417available_devices) Read-only property to get a std::vector<std::string> of available device IDs.


-
static constexpr Property<std::string, PropertyMutability::RO> model_name = {"NETWORK_NAME"}
[#](https://docs.openvino.ai#_CPPv410model_name) Read-only property to get a name of name of a model.


-
static constexpr Property<uint32_t, PropertyMutability::RO> optimal_number_of_infer_requests{"OPTIMAL_NUMBER_OF_INFER_REQUESTS"}
[#](https://docs.openvino.ai#_CPPv432optimal_number_of_infer_requests) Read-only property to get an unsigned integer value of optimal number of compiled model infer requests.


-
static constexpr Property<element::Type, PropertyMutability::RW> inference_precision = {"INFERENCE_PRECISION_HINT"}
[#](https://docs.openvino.ai#_CPPv419inference_precision) Hint for device to use specified precision for inference.


-
static constexpr Property<
[Priority](https://docs.openvino.ai#_CPPv48Priority)> model_priority = {"MODEL_PRIORITY"}[#](https://docs.openvino.ai#_CPPv414model_priority) High-level OpenVINO model priority hint Defines what model should be provided with more performant bounded resource first.


-
static constexpr Property<
[PerformanceMode](https://docs.openvino.ai#_CPPv415PerformanceMode)> performance_mode = {"PERFORMANCE_HINT"}[#](https://docs.openvino.ai#_CPPv416performance_mode) High-level OpenVINO Performance Hints unlike low-level properties that are individual (per-device), the hints are something that every device accepts and turns into device-specific settings.


-
static constexpr Property<SchedulingCoreType> scheduling_core_type = {"SCHEDULING_CORE_TYPE"}
[#](https://docs.openvino.ai#_CPPv420scheduling_core_type) This property defines CPU core type which can be used during inference.

Developer can use this property to select specific CPU cores for inference. Please refer SchedulingCoreType for all definition of core type.

The following code is an example to only use efficient-cores for inference on hybrid CPU. If user sets this configuration on a platform with only performance-cores, CPU inference will still run on the performance-cores.

ie.set_property(ov::hint::scheduling_core_type(ov::hint::SchedulingCoreType::ECORE_ONLY));


-
static constexpr Property<std::set<ModelDistributionPolicy>> model_distribution_policy = {"MODEL_DISTRIBUTION_POLICY"}
[#](https://docs.openvino.ai#_CPPv425model_distribution_policy) This property defines model distribution policy for inference with multiple sockets/devices.

This property can be used to select model distribution policy between execution units (e.g. between CPU sockets/NUMA nodes or between different GPUs). — TENSOR_PARALLEL : Distribute tensor to multiple sockets/devices during model compilation. At inference time, sockets/devices process individual tensor in parallel. — PIPELINE_PARALLEL : Distribute tensor to multiple sockets/devices during model compilation. At inference time, sockets/devices process individual tensor one by one. And each socket/device processes a portion of a different tensor in parallel.

The following code is an example how TENSOR_PARALLEL or PIPELINE_PARALLEL model distribution policy might be enabled.

ie.set_property(ov::hint::model_distribution_policy({ov::hint::ModelDistributionPolicy::TENSOR_PARALLEL})); ie.set_property(ov::hint::model_distribution_policy({ov::hint::ModelDistributionPolicy::PIPELINE_PARALLEL}));


-
static constexpr Property<bool> enable_cpu_pinning = {"ENABLE_CPU_PINNING"}
[#](https://docs.openvino.ai#_CPPv418enable_cpu_pinning) This property allows CPU pinning during inference.

Developer can use this property to enable or disable CPU pinning during inference on Windows and Linux. MacOS does not support CPU pinning, and this property is always disabled. If user does not explicitly set value for this property, OpenVINO may choose any desired value based on internal logic.

The following is an example of CPU fixed behavior on a hybrid CPU (8 performance cores and 16 efficiency cores). For stream with 4 threads on performance cores, if CPU pinning is enabled, each thread is bound to a specific performance core. If CPU pinning is disabled, OS will schedule 4 threads on performance cores only. For stream with 24 threads on all cores, if CPU pinning is enabled, each thread is bound to a specific performance core. If CPU pinning is disabled, OS will schedule 24 threads on both performance cores and efficiency cores.

The following code is example to use this property.

ie.set_property(ov::hint::enable_cpu_pinning(true)); ie.set_property(ov::hint::enable_cpu_pinning(false));


-
static constexpr Property<bool> enable_cpu_reservation = {"ENABLE_CPU_RESERVATION"}
[#](https://docs.openvino.ai#_CPPv422enable_cpu_reservation) This property allows CPU reservation during inference.

Cpu Reservation means reserve cpus which will not be used by other plugin or compiled model. Developer can use this property to enable or disable CPU reservation during inference on Windows and Linux. MacOS does not support CPU reservation, and this property is always disabled. This property defaults to false.

The following code is example to use this property.

ie.set_property(ov::hint::enable_cpu_reservation(true)); ie.set_property(ov::hint::enable_cpu_reservation(false));


-
static constexpr Property<bool> enable_hyper_threading = {"ENABLE_HYPER_THREADING"}
[#](https://docs.openvino.ai#_CPPv422enable_hyper_threading) This property define if using hyper threading during inference.

Developer can use this property to use or not use CPU pinning during inference. If user does not explicitly set value for this property, OpenVINO may choose any desired value based on internal logic.

The following code is example to use this property.

ie.set_property(ov::hint::enable_hyper_threading(true)); ie.set_property(ov::hint::enable_hyper_threading(false));


-
static constexpr Property<uint32_t> num_requests = {"PERFORMANCE_HINT_NUM_REQUESTS"}
[#](https://docs.openvino.ai#_CPPv412num_requests) (Optional) property that backs the (above) Performance Hints by giving additional information on how many inference requests the application will be keeping in flight usually this value comes from the actual use-case (e.g. number of video-cameras, or other sources of inputs)


-
static constexpr Property<std::shared_ptr<const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)>> model = {"MODEL_PTR"}[#](https://docs.openvino.ai#_CPPv45model) This key identifies shared pointer to the

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model), required for some properties ([ov::max_batch_size](https://docs.openvino.ai#group__ov__runtime__cpp__prop__api_1ga5dbd8ab0c8a177234cade9a54c96249c)and[ov::optimal_batch_size](https://docs.openvino.ai#group__ov__runtime__cpp__prop__api_1ga129bad2da2fc2a40a7d746d86fc9c68d))

-
static constexpr Property<bool, PropertyMutability::RW> allow_auto_batching = {"ALLOW_AUTO_BATCHING"}
[#](https://docs.openvino.ai#_CPPv419allow_auto_batching) Special key for auto batching feature configuration. Enabled by default.


-
static constexpr Property<
[ExecutionMode](https://docs.openvino.ai#_CPPv413ExecutionMode)> execution_mode = {"EXECUTION_MODE_HINT"}[#](https://docs.openvino.ai#_CPPv414execution_mode) High-level OpenVINO Execution hint unlike low-level properties that are individual (per-device), the hints are something that every device accepts and turns into device-specific settings Execution mode hint controls preferred optimization targets (performance or accuracy) for given model.


-
static constexpr Property<uint64_t, PropertyMutability::RW> dynamic_quantization_group_size{"DYNAMIC_QUANTIZATION_GROUP_SIZE"}
[#](https://docs.openvino.ai#_CPPv431dynamic_quantization_group_size) This property defines group size for dynamic quantization optimization.

Dynamic quantization optimization provides an ability to get performance benefit from int8 compute. In contrast with static quantization dynamic approach assumes activations are quantized during inference. Despite the fact dynamic quantization has some runtime overheads, it might provide better accuracy metrics. This property defines granularity (aka block size) for dynamic quantization algorithms. Lower group size values might result in better accuracy, but the drawback is worse performance. Group size equal 0 means dynamic quantization optimization is disabled.


-
static constexpr Property<element::Type, PropertyMutability::RW> kv_cache_precision = {"KV_CACHE_PRECISION"}
[#](https://docs.openvino.ai#_CPPv418kv_cache_precision) Hint for device to use specified precision for kv cache compression.


-
static constexpr Property<float, PropertyMutability::RW> activations_scale_factor = {"ACTIVATIONS_SCALE_FACTOR"}
[#](https://docs.openvino.ai#_CPPv424activations_scale_factor) This property scales down activations to prevent overflows when inference precision is f16.


-
constexpr Property<Tensor, PropertyMutability::RW> compiled_blob = {"COMPILED_BLOB"}
[#](https://docs.openvino.ai#_CPPv413compiled_blob) Hint for device to use model compiled blob.

The property is used pass compiled blob as

[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor). The blob can be regular or weightless model. The`weights_path`

property is hint where to look for weights.

-
static constexpr Property<bool> enable_profiling = {"PERF_COUNT"}
[#](https://docs.openvino.ai#_CPPv416enable_profiling) The name for setting performance counters option.


-
static constexpr Property<
[Level](https://docs.openvino.ai#_CPPv45Level)> level = {"LOG_LEVEL"}[#](https://docs.openvino.ai#_CPPv45level) the property for setting desirable log level.


-
static constexpr Property<std::string> cache_dir = {"CACHE_DIR"}
[#](https://docs.openvino.ai#_CPPv49cache_dir) This property defines the directory which will be used to store any data cached by plugins.

The underlying cache structure is not defined and might differ between OpenVINO releases Cached data might be platform / device specific and might be invalid after OpenVINO version change If this property is not specified or value is empty string, then caching is disabled. The property might enable caching for the plugin using the following code:

ie.set_property("GPU", ov::cache_dir("cache/")); // enables cache for GPU plugin

The following code enables caching of compiled network blobs for devices where import/export is supported

ie.set_property(ov::cache_dir("cache/")); // enables models cache


-
static constexpr Property<bool, PropertyMutability::RO> loaded_from_cache = {"LOADED_FROM_CACHE"}
[#](https://docs.openvino.ai#_CPPv417loaded_from_cache) Read-only property to notify user that compiled model was loaded from the cache.


-
static constexpr Property<std::filesystem::path, PropertyMutability::WO> cache_model_path = {"CACHE_MODEL_PATH"}
[#](https://docs.openvino.ai#_CPPv416cache_model_path) Write property to specify the origin path of compiled model to speed cache model ID calculation.

The property has meaning when used in

`core::compile_model(const std::shared_ptr<const`

and cache feature is enabled.[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)>& model, ...)

-
static constexpr Property<
[WorkloadType](https://docs.openvino.ai#_CPPv412WorkloadType), PropertyMutability::RW> workload_type = {"WORKLOAD_TYPE"}[#](https://docs.openvino.ai#_CPPv413workload_type) Read-write property to select in which mode the workload will be executed This is only supported by NPU.


-
static constexpr Property<
[CacheMode](https://docs.openvino.ai#_CPPv49CacheMode), PropertyMutability::RW> cache_mode = {"CACHE_MODE"}[#](https://docs.openvino.ai#_CPPv410cache_mode) Read-write property to select the cache mode between OPTIMIZE_SIZE and OPTIMIZE_SPEED. If OPTIMIZE_SPEED is selected (default), loading time will decrease but the cache file size will increase. If OPTIMIZE_SIZE is selected, smaller cache files will be created. The cache model default behaviour can be overridden by ENABLE_WEIGHTLESS property.


-
static constexpr Property<bool, PropertyMutability::RW> enable_weightless = {"ENABLE_WEIGHTLESS"}
[#](https://docs.openvino.ai#_CPPv417enable_weightless) Read-write property to enable/disable weightless cache.


-
static constexpr Property<EncryptionCallbacks, PropertyMutability::WO> cache_encryption_callbacks{"CACHE_ENCRYPTION_CALLBACKS"}
[#](https://docs.openvino.ai#_CPPv426cache_encryption_callbacks) Write-only property to set encryption/decryption function for saving/loading model cache. If cache_encryption_callbacks is set, the model topology will be encrypted when saving to the cache and decrypted when loading from the cache. This property is set in core.compile_model only.

First value of the struct is encryption function.

Second value of the struct is decryption function.



-
static constexpr Property<std::tuple<unsigned int, unsigned int>, PropertyMutability::RO> range_for_streams{"RANGE_FOR_STREAMS"}
[#](https://docs.openvino.ai#_CPPv417range_for_streams) Read-only property to provide information about a range for streams on platforms where streams are supported.

[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)returns a value of std::tuple<unsigned int, unsigned int> type, where:First value is bottom bound.

Second value is upper bound.



-
static constexpr Property<unsigned int, PropertyMutability::RO> optimal_batch_size = {"OPTIMAL_BATCH_SIZE"}
[#](https://docs.openvino.ai#_CPPv418optimal_batch_size) Read-only property to query information optimal batch size for the given device and the network.

[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)returns a value of unsigned int type, Returns optimal batch size for a given network on the given device. The returned value is aligned to power of 2. Also,[ov::hint::model](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__cpp__prop__api_1ga214004bd94dd23a943194b10fd273d81)is the required option for this metric since the optimal batch size depends on the model, so if the[ov::hint::model](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__cpp__prop__api_1ga214004bd94dd23a943194b10fd273d81)is not given, the result of the metric is always 1. For the GPU the metric is queried automatically whenever the OpenVINO performance hint for the throughput is used, so that the result (>1) governs the automatic batching (transparently to the application). The automatic batching can be disabled with ALLOW_AUTO_BATCHING set to NO

-
static constexpr Property<uint32_t, PropertyMutability::RO> max_batch_size = {"MAX_BATCH_SIZE"}
[#](https://docs.openvino.ai#_CPPv414max_batch_size) Read-only property to get maximum batch size which does not cause performance degradation due to memory swap impact.


-
static constexpr Property<uint32_t, PropertyMutability::RW> auto_batch_timeout = {"AUTO_BATCH_TIMEOUT"}
[#](https://docs.openvino.ai#_CPPv418auto_batch_timeout) Read-write property to set the timeout used to collect the inputs for the auto-batching impact.


-
static constexpr Property<std::tuple<unsigned int, unsigned int, unsigned int>, PropertyMutability::RO> range_for_async_infer_requests = {"RANGE_FOR_ASYNC_INFER_REQUESTS"}
[#](https://docs.openvino.ai#_CPPv430range_for_async_infer_requests) Read-only property to provide a hint for a range for number of async infer requests. If device supports streams, the metric provides range for number of IRs per stream.

[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)returns a value of std::tuple<unsigned int, unsigned int, unsigned int> type, where:First value is bottom bound.

Second value is upper bound.

Third value is step inside this range.



-
static constexpr Property<bool, PropertyMutability::RW> force_tbb_terminate = {"FORCE_TBB_TERMINATE"}
[#](https://docs.openvino.ai#_CPPv419force_tbb_terminate) Read-write property to set whether force terminate tbb when ov core destruction value type: boolean.

True explicitly terminate tbb when ov core destruction

False will not involve additional tbb operations when core destruction



-
static constexpr Property<bool, PropertyMutability::RW> enable_mmap = {"ENABLE_MMAP"}
[#](https://docs.openvino.ai#_CPPv411enable_mmap) Read-write property to configure

`mmap()`

use for model read. Enabled by default. For the moment only IR Frontend supports the property.value type: boolean

True enable

`mmap()`

use and map modelFalse disable

`mmap()`

use and read model


-
static constexpr Property<std::string> id = {"DEVICE_ID"}
[#](https://docs.openvino.ai#_CPPv42id) the property for setting of required device to execute on values: device id starts from “0” - first device, “1” - second device, etc


-
static constexpr Priorities priorities = {"MULTI_DEVICE_PRIORITIES"}
[#](https://docs.openvino.ai#_CPPv410priorities) Device

[Priorities](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_priorities)config option, with comma-separated devices listed in the desired priority.

-
static constexpr Properties properties = {"DEVICE_PROPERTIES"}
[#](https://docs.openvino.ai#_CPPv410properties) [Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)to pass set of property values to specified deviceUsage Example:

core.compile_model("HETERO" ov::device::priorities("GPU", "CPU"), ov::device::properties("CPU", ov::enable_profiling(true)), ov::device::properties("GPU", ov::enable_profiling(false)));


-
static constexpr Property<std::string, PropertyMutability::RO> full_name = {"FULL_DEVICE_NAME"}
[#](https://docs.openvino.ai#_CPPv49full_name) Read-only property to get a std::string value representing a full device name.


-
static constexpr Property<std::string, PropertyMutability::RO> architecture = {"DEVICE_ARCHITECTURE"}
[#](https://docs.openvino.ai#_CPPv412architecture) Read-only property which defines the device architecture.


-
static constexpr Property<UUID, PropertyMutability::RO> uuid = {"DEVICE_UUID"}
[#](https://docs.openvino.ai#_CPPv44uuid) Read-only property which defines the

[UUID](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_u_u_i_d)of the device.

-
static constexpr Property<LUID, PropertyMutability::RO> luid = {"DEVICE_LUID"}
[#](https://docs.openvino.ai#_CPPv44luid) Read-only property which defines the

[LUID](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_l_u_i_d)of the device.

-
static constexpr Property<
[Type](https://docs.openvino.ai#_CPPv44Type), PropertyMutability::RO> type = {"DEVICE_TYPE"}[#](https://docs.openvino.ai#_CPPv44type) Read-only property to get a type of device. See Type enum definition for possible return values.


-
static constexpr Property<std::map<element::Type, float>, PropertyMutability::RO> gops = {"DEVICE_GOPS"}
[#](https://docs.openvino.ai#_CPPv44gops) Read-only property which defines Giga OPS per second count (GFLOPS or GIOPS) for a set of precisions supported by specified device.


-
static constexpr Property<PCIInfo, PropertyMutability::RO> pci_info = {"DEVICE_PCI_INFO"}
[#](https://docs.openvino.ai#_CPPv48pci_info) Read-only property to get PCI bus information of device. See

[PCIInfo](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_p_c_i_info)struct definition for details.

-
static constexpr Property<float, PropertyMutability::RO> thermal = {"DEVICE_THERMAL"}
[#](https://docs.openvino.ai#_CPPv47thermal) Read-only property to get a float of device thermal.


-
static constexpr Property<std::vector<std::string>, PropertyMutability::RO> capabilities = {"OPTIMIZATION_CAPABILITIES"}
[#](https://docs.openvino.ai#_CPPv412capabilities) Read-only property to get a std::vector<std::string> of capabilities options per device.


-
static constexpr const auto FP32 = "FP32"
[#](https://docs.openvino.ai#_CPPv44FP32) Device supports fp32 inference.


-
static constexpr const auto BF16 = "BF16"
[#](https://docs.openvino.ai#_CPPv44BF16) Device supports bf16 inference.


-
static constexpr const auto FP16 = "FP16"
[#](https://docs.openvino.ai#_CPPv44FP16) Device supports fp16 inference.


-
static constexpr const auto INT8 = "INT8"
[#](https://docs.openvino.ai#_CPPv44INT8) Device supports int8 inference.


-
static constexpr const auto INT16 = "INT16"
[#](https://docs.openvino.ai#_CPPv45INT16) Device supports int16 inference.


-
static constexpr const auto BIN = "BIN"
[#](https://docs.openvino.ai#_CPPv43BIN) Device supports binary inference.


-
static constexpr const auto WINOGRAD = "WINOGRAD"
[#](https://docs.openvino.ai#_CPPv48WINOGRAD) Device supports winograd optimization.


-
static constexpr const auto EXPORT_IMPORT = "EXPORT_IMPORT"
[#](https://docs.openvino.ai#_CPPv413EXPORT_IMPORT) Device supports compiled model export and import.


-
static constexpr Property<Num, PropertyMutability::RW> num = {"NUM_STREAMS"}
[#](https://docs.openvino.ai#_CPPv43num) The number of executor logical partitions.


-
static constexpr Num AUTO = {-1}
[#](https://docs.openvino.ai#_CPPv44AUTO) Creates bare minimum of streams to improve the performance.


-
static constexpr Num NUMA = {-2}
[#](https://docs.openvino.ai#_CPPv44NUMA) Creates as many streams as needed to accommodate NUMA and avoid associated penalties.


-
static constexpr Property<streams::Num, PropertyMutability::RW> num_streams = {"NUM_STREAMS"}
[#](https://docs.openvino.ai#_CPPv411num_streams) The number of executor logical partitions.


-
static constexpr Property<int32_t, PropertyMutability::RW> inference_num_threads = {"INFERENCE_NUM_THREADS"}
[#](https://docs.openvino.ai#_CPPv421inference_num_threads) Maximum number of threads that can be used for inference tasks.


-
static constexpr Property<int32_t, PropertyMutability::RW> compilation_num_threads = {"COMPILATION_NUM_THREADS"}
[#](https://docs.openvino.ai#_CPPv423compilation_num_threads) Maximum number of threads that can be used for compilation tasks.


-
static constexpr Property<std::vector<std::string>, PropertyMutability::RO> execution_devices = {"EXECUTION_DEVICES"}
[#](https://docs.openvino.ai#_CPPv417execution_devices) The devices that the inference task been executed.


-
static constexpr Property<element::Type, PropertyMutability::RW> key_cache_precision = {"KEY_CACHE_PRECISION"}
[#](https://docs.openvino.ai#_CPPv419key_cache_precision) The precision of key cache compression.


-
static constexpr Property<element::Type, PropertyMutability::RW> value_cache_precision = {"VALUE_CACHE_PRECISION"}
[#](https://docs.openvino.ai#_CPPv421value_cache_precision) The precision of value cache compression.


-
static constexpr Property<uint64_t, PropertyMutability::RW> key_cache_group_size = {"KEY_CACHE_GROUP_SIZE"}
[#](https://docs.openvino.ai#_CPPv420key_cache_group_size) The group_size of key cache compression.


-
static constexpr Property<uint64_t, PropertyMutability::RW> value_cache_group_size = {"VALUE_CACHE_GROUP_SIZE"}
[#](https://docs.openvino.ai#_CPPv422value_cache_group_size) The group_size of value cache compression.


-
struct Priorities : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<std::string>[#](https://docs.openvino.ai#_CPPv4N2ov6device10PrioritiesE) *#include <properties.hpp>*Type for device

[Priorities](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_priorities)config option, with comma-separated devices listed in the desired priority.Public Functions


-
struct Properties : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Property](https://docs.openvino.ai/classov_1_1_property.html#_CPPv4I0_18PropertyMutabilityEN2ov8PropertyE)<std::map<std::string, std::map<std::string,[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)>>>[#](https://docs.openvino.ai#_CPPv4N2ov6device10PropertiesE) *#include <properties.hpp>*Type for property to pass set of properties to specified device.

Public Functions

-
inline std::pair<std::string,
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)> operator()(const AnyMap &config) const[#](https://docs.openvino.ai#_CPPv4NK2ov6device10PropertiesclERK6AnyMap) Constructs property.

- Parameters:
**configs**– set of property values with names- Returns:
Pair of string key representation and type erased property value.



-
inline std::pair<std::string,
[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)> operator()(const std::string &device_name, const AnyMap &config) const[#](https://docs.openvino.ai#_CPPv4NK2ov6device10PropertiesclERKNSt6stringERK6AnyMap) Constructs property.

- Parameters:
**device_name**– device plugin alias**config**– set of property values with names

- Returns:
Pair of string key representation and type erased property value.



-
template<typename ...Properties>

inline[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4utilE)::EnableIfAllStringAny<std::pair<std::string,[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)>,[Properties](https://docs.openvino.ai/structov_1_1device_1_1_properties.html#_CPPv4IDpENK2ov6device10PropertiesclEN4util20EnableIfAllStringAnyINSt4pairINSt6stringE3AnyEEDp10PropertiesEERKNSt6stringEDpRR10Properties)...> operator()(const std::string &device_name,[Properties](https://docs.openvino.ai/structov_1_1device_1_1_properties.html#_CPPv4IDpENK2ov6device10PropertiesclEN4util20EnableIfAllStringAnyINSt4pairINSt6stringE3AnyEEDp10PropertiesEERKNSt6stringEDpRR10Properties)&&... configs) const[#](https://docs.openvino.ai#_CPPv4IDpENK2ov6device10PropertiesclEN4util20EnableIfAllStringAnyINSt4pairINSt6stringE3AnyEEDp10PropertiesEERKNSt6stringEDpRR10Properties) Constructs property.

- Template Parameters:
**Properties**– Should be the pack of`std::pair<std::string,`

types[ov::Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)>- Parameters:
**device_name**– device plugin alias**configs**– Optional pack of pairs: (config parameter name, config parameter value)

- Returns:
Pair of string key representation and type erased property value.



-
inline std::pair<std::string,

-
struct UUID
[#](https://docs.openvino.ai#_CPPv4N2ov6device4UUIDE) *#include <properties.hpp>*Structure which defines format of

[UUID](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_u_u_i_d).Public Members

-
std::array<uint8_t,
[MAX_UUID_SIZE](https://docs.openvino.ai/structov_1_1device_1_1_u_u_i_d.html#_CPPv4N2ov6device4UUID13MAX_UUID_SIZEE)> uuid[#](https://docs.openvino.ai#_CPPv4N2ov6device4UUID4uuidE) Array with uuid for a device.


Public Static Attributes

-
static const uint64_t MAX_UUID_SIZE = 16
[#](https://docs.openvino.ai#_CPPv4N2ov6device4UUID13MAX_UUID_SIZEE) Max size of uuid array (128 bits)


-
std::array<uint8_t,

-
struct LUID
[#](https://docs.openvino.ai#_CPPv4N2ov6device4LUIDE) *#include <properties.hpp>*Structure which defines format of

[LUID](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1device_1_1_l_u_i_d).Public Members

-
std::array<uint8_t,
[MAX_LUID_SIZE](https://docs.openvino.ai/structov_1_1device_1_1_l_u_i_d.html#_CPPv4N2ov6device4LUID13MAX_LUID_SIZEE)> luid[#](https://docs.openvino.ai#_CPPv4N2ov6device4LUID4luidE) Array with luid for a device.


Public Static Attributes

-
static const uint64_t MAX_LUID_SIZE = 8
[#](https://docs.openvino.ai#_CPPv4N2ov6device4LUID13MAX_LUID_SIZEE) Max size of luid array (64 bits)


-
std::array<uint8_t,

-
struct PCIInfo
[#](https://docs.openvino.ai#_CPPv4N2ov6device7PCIInfoE) *#include <properties.hpp>*Structure to store PCI bus information of device (Domain/Bus/Device/Function)


-
enum class SchedulePolicy