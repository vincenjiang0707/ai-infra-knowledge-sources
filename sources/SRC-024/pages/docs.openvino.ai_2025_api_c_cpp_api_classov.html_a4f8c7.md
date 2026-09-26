source: https://docs.openvino.ai/2025/api/c_cpp_api/classov.html
lastmod: 

# Class ov[#](https://docs.openvino.ai#class-ov)

- ov : private pass::low_precision::BaseMatcherPass public ov::pass::MatcherPass , private pass::low_precision::LowPrecision public ov::pass::ModelPass
Public Types

-
enum ColumnOfProcessorTypeTable
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTableE) This enum contains definition of each columns in processor type table which bases on cpu core types. Will extend to support other CPU core type like ARM.

The following are two example of processor type table.

Processor table of 4 numa nodes and 2 socket server


ALL_PROC | MAIN_CORE | EFFICIENT_CORE | LP_EFFICIENT_CORE | HYPER_THREADING | NUMA_NODE_ID | SOCKET_ID 96 48 0 0 48 -1 -1 24 12 0 0 12 0 0 24 12 0 0 12 1 0 24 12 0 0 12 2 1 24 12 0 0 12 3 1

Processor table of 1 numa node desktop

ALL_PROC | MAIN_CORE | EFFICIENT_CORE | LP_EFFICIENT_CORE | HYPER_THREADING | NUMA_NODE_ID | SOCKET_ID 16 4 8 4 0 0 0


*Values:*-
enumerator ALL_PROC
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTable8ALL_PROCE) All processors, regardless of backend cpu.


-
enumerator MAIN_CORE_PROC
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTable14MAIN_CORE_PROCE) Processor based on physical core of Intel Performance-cores.


-
enumerator EFFICIENT_CORE_PROC
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTable19EFFICIENT_CORE_PROCE) Processor based on Intel Efficient-cores.


-
enumerator LP_EFFICIENT_CORE_PROC
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTable22LP_EFFICIENT_CORE_PROCE) Processor based on Intel Low Power Efficient-cores.


-
enumerator HYPER_THREADING_PROC
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTable20HYPER_THREADING_PROCE) Processor based on logical core of Intel Performance-cores.


-
enumerator PROC_NUMA_NODE_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTable17PROC_NUMA_NODE_IDE) Numa node id of processors in this row.


-
enumerator PROC_SOCKET_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTable14PROC_SOCKET_IDE) Socket id of processors in this row.


-
enumerator PROC_TYPE_TABLE_SIZE
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26ColumnOfProcessorTypeTable20PROC_TYPE_TABLE_SIZEE) Size of processor type table.



-
enum ProcessorUseStatus
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18ProcessorUseStatusE) Definition of CPU_MAP_USED_FLAG column in CPU mapping table.

*Values:*-
enumerator CPU_BLOCKED
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18ProcessorUseStatus11CPU_BLOCKEDE) Processor is blocked to use.


-
enumerator NOT_USED
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18ProcessorUseStatus8NOT_USEDE) Processor is not bound to thread.


-
enumerator CPU_USED
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18ProcessorUseStatus8CPU_USEDE) CPU is in using.


-
enumerator CPU_BLOCKED

-
enum ColumnOfCPUMappingTable
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTableE) This enum contains definition of each columns in CPU mapping table which use processor id as index.

GROUP_ID is generated according to the following rules.

If one MAIN_CORE_PROC and one HYPER_THREADING_PROC are based on same Performance-cores, they are in one group.

If some EFFICIENT_CORE_PROC share one L2 cachle, they are in one group.

There are no duplicate group IDs in the system


The following is the example of CPU mapping table.

Four processors of two Pcore

Four processors of four Ecores shared L2 cache


PROCESSOR_ID | NUMA_NODE_ID | SOCKET_ID | CORE_ID | CORE_TYPE | GROUP_ID | Used 0 0 0 0 3 0 0 1 0 0 0 1 0 0 2 0 0 1 3 1 0 3 0 0 1 1 1 0 4 0 0 2 2 2 0 5 0 0 3 2 2 0 6 0 0 4 2 2 0 7 0 0 5 2 2 0

*Values:*-
enumerator CPU_MAP_PROCESSOR_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTable20CPU_MAP_PROCESSOR_IDE) column for processor id of the processor


-
enumerator CPU_MAP_NUMA_NODE_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTable20CPU_MAP_NUMA_NODE_IDE) column for node id of the processor


-
enumerator CPU_MAP_SOCKET_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTable17CPU_MAP_SOCKET_IDE) column for socket id of the processor


-
enumerator CPU_MAP_CORE_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTable15CPU_MAP_CORE_IDE) column for hardware core id of the processor


-
enumerator CPU_MAP_CORE_TYPE
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTable17CPU_MAP_CORE_TYPEE) column for CPU core type corresponding to the processor


-
enumerator CPU_MAP_GROUP_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTable16CPU_MAP_GROUP_IDE) column for group id to the processor. Processors in one group have dependency.


-
enumerator CPU_MAP_USED_FLAG
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTable17CPU_MAP_USED_FLAGE) column for resource management of the processor


-
enumerator CPU_MAP_TABLE_SIZE
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23ColumnOfCPUMappingTable18CPU_MAP_TABLE_SIZEE) Size of CPU mapping table.



-
enum ColumnOfCpuStreamsInfoTable
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError27ColumnOfCpuStreamsInfoTableE) This enum contains definition of each columns in cpu streams information table.

The following are two example of processor type table.

8 streams on hybrid platform which has 4 threads per stream (TPS). 1.1 2 streams (4 TPS) on physical core of Intel Performance-cores 1.2 4 streams (4 TPS) on Intel Efficient-cores 1.3 2 streams (4 TPS) on logic core of Intel Performance-cores


NUMBER_OF_STREAMS | PROC_TYPE | THREADS_PER_STREAM | STREAM_NUMA_NODE_ID | STREAM_SOCKET_ID 2 1 4 0 0 4 2 4 0 0 2 3 4 0 0

1 stream (10 TPS) on hybrid platform which has 2 threads on physical core and 8 threads on Ecore. 2.1 1 streams (10 TPS) on multiple types of processors 2.2 2 threads on physical core of Intel Performance-cores 2.3 8 threads on Intel Efficient-cores

NUMBER_OF_STREAMS | PROC_TYPE | THREADS_PER_STREAM | STREAM_NUMA_NODE_ID | STREAM_SOCKET_ID 1 0 10 0 0 0 1 2 0 0 0 2 8 0 0


*Values:*-
enumerator NUMBER_OF_STREAMS
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError27ColumnOfCpuStreamsInfoTable17NUMBER_OF_STREAMSE) Number of streams on specific CPU core tpye.


-
enumerator THREADS_PER_STREAM
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError27ColumnOfCpuStreamsInfoTable18THREADS_PER_STREAME) Number of threads per stream of current streams.


-
enumerator STREAM_NUMA_NODE_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError27ColumnOfCpuStreamsInfoTable19STREAM_NUMA_NODE_IDE) Numa node id of processors in this row.


-
enumerator STREAM_SOCKET_ID
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError27ColumnOfCpuStreamsInfoTable16STREAM_SOCKET_IDE) Socket id of processors in this row.


-
enumerator CPU_STREAMS_TABLE_SIZE
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError27ColumnOfCpuStreamsInfoTable22CPU_STREAMS_TABLE_SIZEE) Size of streams info table.



-
enum class PropertyMutability
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE) Enum to define property value mutability.

*Values:*-
enumerator RO
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE) Read-only property values can not be passed as input parameter.


-
enumerator RW
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE) Read/Write property key may change readability in runtime.


-
enumerator WO
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2WOE) Write-only property can not be read.


-
enumerator RO

-
enum class WorkloadType
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError12WorkloadTypeE) Enum to define possible workload types.

Workload type represents the execution priority for an inference.

*Values:*-
enumerator DEFAULT
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError12WorkloadType7DEFAULTE)

-
enumerator EFFICIENT
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError12WorkloadType9EFFICIENTE)

-
enumerator DEFAULT

-
enum class CacheMode
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError9CacheModeE) Enum to define possible cache mode.

*Values:*-
enumerator OPTIMIZE_SIZE
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError9CacheMode13OPTIMIZE_SIZEE) smaller cache size


-
enumerator OPTIMIZE_SPEED
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError9CacheMode14OPTIMIZE_SPEEDE) faster loading time


-
enumerator OPTIMIZE_SIZE

-
using TensorSymbol = std::vector<std::shared_ptr<Symbol>>
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError12TensorSymbolE) Alias for symbol tensor.


-
using TensorSymbolVector = std::vector<
[TensorSymbol](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError12TensorSymbolE)>[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18TensorSymbolVectorE) Alias for vector of symbol tensors.


-
using TensorNames = std::unordered_set<std::string>
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError11TensorNamesE) Alias for set of tensor names.


-
using EvaluationContext =
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::RTMap[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError17EvaluationContextE) EvaluationContext stores and manages a context (additional parameters, values and environment) for evaluating

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).

-
using Rank = Dimension
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError4RankE) Alias for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension), used when the value represents the number of axes in a shape, rather than the size of one dimension in a shape.

-
using SupportedOpsMap = std::map<std::string, std::string>
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError15SupportedOpsMapE) This type of map is used for result of

[Core::query_model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_core_1acdf8e64824fe4cf147c3b52ab32c1aab).`key`

means operation name`value`

means device name supporting this operation


Public Static Attributes

-
static constexpr Property<std::vector<PropertyName>,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> supported_properties{"SUPPORTED_PROPERTIES"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError20supported_propertiesE) Read-only property to get a std::vector<PropertyName> of supported read-only properties. This can be used as a compiled model property as well.


-
static constexpr Property<std::vector<std::string>,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> available_devices = {"AVAILABLE_DEVICES"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError17available_devicesE) Read-only property to get a std::vector<std::string> of available device IDs.


-
static constexpr Property<std::string,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> model_name = {"NETWORK_NAME"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError10model_nameE) Read-only property to get a name of name of a model.


-
static constexpr Property<uint32_t,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> optimal_number_of_infer_requests{"OPTIMAL_NUMBER_OF_INFER_REQUESTS"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError32optimal_number_of_infer_requestsE) Read-only property to get an unsigned integer value of optimal number of compiled model infer requests.


-
static constexpr Property<bool> enable_profiling = {"PERF_COUNT"}
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError16enable_profilingE) The name for setting performance counters option.


-
static constexpr Property<std::string> cache_dir = {"CACHE_DIR"}
[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError9cache_dirE) This property defines the directory which will be used to store any data cached by plugins.

The underlying cache structure is not defined and might differ between OpenVINO releases Cached data might be platform / device specific and might be invalid after OpenVINO version change If this property is not specified or value is empty string, then caching is disabled. The property might enable caching for the plugin using the following code:

ie.set_property("GPU", ov::cache_dir("cache/")); // enables cache for GPU plugin

The following code enables caching of compiled network blobs for devices where import/export is supported

ie.set_property(ov::cache_dir("cache/")); // enables models cache


-
static constexpr Property<bool,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> loaded_from_cache = {"LOADED_FROM_CACHE"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError17loaded_from_cacheE) Read-only property to notify user that compiled model was loaded from the cache.


-
static constexpr Property<std::filesystem::path,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[WO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2WOE)> cache_model_path = {"CACHE_MODEL_PATH"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError16cache_model_pathE) Write property to specify the origin path of compiled model to speed cache model ID calculation.

The property has meaning when used in

`core::compile_model(const std::shared_ptr<const`

and cache feature is enabled.[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)>& model, ...)

-
static constexpr Property<
[WorkloadType](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError12WorkloadTypeE),[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> workload_type = {"WORKLOAD_TYPE"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError13workload_typeE) Read-write property to select in which mode the workload will be executed This is only supported by NPU.


-
static constexpr Property<
[CacheMode](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError9CacheModeE),[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> cache_mode = {"CACHE_MODE"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError10cache_modeE) Read-write property to select the cache mode between OPTIMIZE_SIZE and OPTIMIZE_SPEED. If OPTIMIZE_SPEED is selected (default), loading time will decrease but the cache file size will increase. If OPTIMIZE_SIZE is selected, smaller cache files will be created. The cache model default behaviour can be overridden by ENABLE_WEIGHTLESS property.


-
static constexpr Property<bool,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> enable_weightless = {"ENABLE_WEIGHTLESS"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError17enable_weightlessE) Read-write property to enable/disable weightless cache.


-
static constexpr Property<EncryptionCallbacks,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[WO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2WOE)> cache_encryption_callbacks{"CACHE_ENCRYPTION_CALLBACKS"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError26cache_encryption_callbacksE) Write-only property to set encryption/decryption function for saving/loading model cache. If cache_encryption_callbacks is set, the model topology will be encrypted when saving to the cache and decrypted when loading from the cache. This property is set in core.compile_model only.

First value of the struct is encryption function.

Second value of the struct is decryption function.



-
static constexpr Property<std::tuple<unsigned int, unsigned int>,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> range_for_streams{"RANGE_FOR_STREAMS"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError17range_for_streamsE) Read-only property to provide information about a range for streams on platforms where streams are supported.

[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)returns a value of std::tuple<unsigned int, unsigned int> type, where:First value is bottom bound.

Second value is upper bound.



-
static constexpr Property<unsigned int,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> optimal_batch_size = {"OPTIMAL_BATCH_SIZE"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18optimal_batch_sizeE) Read-only property to query information optimal batch size for the given device and the network.

[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)returns a value of unsigned int type, Returns optimal batch size for a given network on the given device. The returned value is aligned to power of 2. Also,[ov::hint::model](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__cpp__prop__api_1ga214004bd94dd23a943194b10fd273d81)is the required option for this metric since the optimal batch size depends on the model, so if the[ov::hint::model](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__runtime__cpp__prop__api_1ga214004bd94dd23a943194b10fd273d81)is not given, the result of the metric is always 1. For the GPU the metric is queried automatically whenever the OpenVINO performance hint for the throughput is used, so that the result (>1) governs the automatic batching (transparently to the application). The automatic batching can be disabled with ALLOW_AUTO_BATCHING set to NO

-
static constexpr Property<uint32_t,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> max_batch_size = {"MAX_BATCH_SIZE"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError14max_batch_sizeE) Read-only property to get maximum batch size which does not cause performance degradation due to memory swap impact.


-
static constexpr Property<uint32_t,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> auto_batch_timeout = {"AUTO_BATCH_TIMEOUT"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18auto_batch_timeoutE) Read-write property to set the timeout used to collect the inputs for the auto-batching impact.


-
static constexpr Property<std::tuple<unsigned int, unsigned int, unsigned int>,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> range_for_async_infer_requests = {"RANGE_FOR_ASYNC_INFER_REQUESTS"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError30range_for_async_infer_requestsE) Read-only property to provide a hint for a range for number of async infer requests. If device supports streams, the metric provides range for number of IRs per stream.

[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)returns a value of std::tuple<unsigned int, unsigned int, unsigned int> type, where:First value is bottom bound.

Second value is upper bound.

Third value is step inside this range.



-
static constexpr Property<bool,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> force_tbb_terminate = {"FORCE_TBB_TERMINATE"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError19force_tbb_terminateE) Read-write property to set whether force terminate tbb when ov core destruction value type: boolean.

True explicitly terminate tbb when ov core destruction

False will not involve additional tbb operations when core destruction



-
static constexpr Property<bool,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> enable_mmap = {"ENABLE_MMAP"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError11enable_mmapE) Read-write property to configure

`mmap()`

use for model read. Enabled by default. For the moment only IR Frontend supports the property.value type: boolean

True enable

`mmap()`

use and map modelFalse disable

`mmap()`

use and read model


-
static constexpr Property<streams::Num,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> num_streams = {"NUM_STREAMS"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError11num_streamsE) The number of executor logical partitions.


-
static constexpr Property<int32_t,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> inference_num_threads = {"INFERENCE_NUM_THREADS"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError21inference_num_threadsE) Maximum number of threads that can be used for inference tasks.


-
static constexpr Property<int32_t,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> compilation_num_threads = {"COMPILATION_NUM_THREADS"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError23compilation_num_threadsE) Maximum number of threads that can be used for compilation tasks.


-
static constexpr Property<std::vector<std::string>,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RO](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2ROE)> execution_devices = {"EXECUTION_DEVICES"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError17execution_devicesE) The devices that the inference task been executed.


-
static constexpr Property<std::string,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> weights_path = {"WEIGHTS_PATH"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError12weights_pathE) Path to the file with model’s weights.

Note

This property is used for weightless caching. Only used when

[ov::CacheMode](https://docs.openvino.ai/group__ov__runtime__cpp__prop__api.html#group__ov__runtime__cpp__prop__api_1gadcca1aebf14e3d3cf2aed26b161214d7)[Property](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_property)is set to “OPTIMIZE_SIZE”.

-
static constexpr Property<element::Type,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> key_cache_precision = {"KEY_CACHE_PRECISION"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError19key_cache_precisionE) The precision of key cache compression.


-
static constexpr Property<element::Type,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> value_cache_precision = {"VALUE_CACHE_PRECISION"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError21value_cache_precisionE) The precision of value cache compression.


-
static constexpr Property<uint64_t,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> key_cache_group_size = {"KEY_CACHE_GROUP_SIZE"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError20key_cache_group_sizeE) The group_size of key cache compression.


-
static constexpr Property<uint64_t,
[PropertyMutability](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutabilityE)::[RW](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError18PropertyMutability2RWE)> value_cache_group_size = {"VALUE_CACHE_GROUP_SIZE"}[#](https://docs.openvino.ai#_CPPv4N19PhonyNameDueToError22value_cache_group_sizeE) The group_size of value cache compression.


-
enum ColumnOfProcessorTypeTable