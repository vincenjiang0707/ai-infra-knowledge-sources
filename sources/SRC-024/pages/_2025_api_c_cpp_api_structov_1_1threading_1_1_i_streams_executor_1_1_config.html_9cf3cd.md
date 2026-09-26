source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1threading_1_1_i_streams_executor_1_1_config.html
lastmod: 

# Struct ov::threading::IStreamsExecutor::Config[#](https://docs.openvino.ai#struct-ov-threading-istreamsexecutor-config)

-
struct Config
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6ConfigE) Defines

[IStreamsExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_i_streams_executor)configuration.Public Types

-
enum class StreamsMode
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsModeE) This enum contains definition of each sub streams mode, indicating the main stream situation.

*Values:*-
enumerator SUB_STREAMS_NULL
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsMode16SUB_STREAMS_NULLE) Do not create sub streams.


-
enumerator SUB_STREAMS_FOR_SOCKET
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsMode22SUB_STREAMS_FOR_SOCKETE) Create sub streams for multiple sockets in main stream.


-
enumerator LATENCY
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsMode7LATENCYE) latency mode


-
enumerator THROUGHPUT
[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config11StreamsMode10THROUGHPUTE) throughput mode


-
enumerator SUB_STREAMS_NULL

Public Functions

-
inline Config(std::string name = "StreamsExecutor", int streams = 1, int threads_per_stream = 0,
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[hint](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hintE)::[SchedulingCoreType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint18SchedulingCoreTypeE)thread_preferred_core_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[hint](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hintE)::[SchedulingCoreType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint18SchedulingCoreTypeE)::[ANY_CORE](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4hint18SchedulingCoreType8ANY_COREE), bool cpu_reservation = false, bool cpu_pinning = false, bool cores_limit = true, std::vector<std::vector<int>> streams_info_table = {}, std::vector<int> rank = {}, bool add_lock = true)[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config6ConfigENSt6stringEiiN2ov4hint18SchedulingCoreTypeEbbbNSt6vectorINSt6vectorIiEEEENSt6vectorIiEEb) A constructor with arguments.

- Parameters:
**name**–**[in]**The executor name**streams**–**[in]****threads_per_stream**–**[in]****thread_preferred_core_type**–**[in]****cpu_reservation**–**[in]****cpu_pinning**–**[in]****streams_info_table**–**[in]****rank**–**[in]**



-
void set_property(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::AnyMap &properties)[#](https://docs.openvino.ai#_CPPv4N2ov9threading16IStreamsExecutor6Config12set_propertyERKN2ov6AnyMapE) Sets configuration.

- Parameters:
**properties**– map of properties


-
enum class StreamsMode