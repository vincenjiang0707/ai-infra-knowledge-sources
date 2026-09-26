source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1threading_1_1_c_p_u_streams_executor.html
lastmod: 

# Class ov::threading::CPUStreamsExecutor[#](https://docs.openvino.ai#class-ov-threading-cpustreamsexecutor)

-
class CPUStreamsExecutor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[threading](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threadingE)::[IStreamsExecutor](https://docs.openvino.ai/group__ov__dev__api__threading.html#_CPPv4N2ov9threading16IStreamsExecutorE)[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutorE) CPU Streams executor implementation. The executor splits the CPU into groups of threads, that can be pinned to cores or NUMA nodes. It uses custom threads to pull tasks from single queue.

Public Types

-
using Ptr = std::shared_ptr<
[CPUStreamsExecutor](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutorE)>[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor3PtrE) A shared pointer to a

[CPUStreamsExecutor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1threading_1_1_c_p_u_streams_executor)object.

Public Functions

-
explicit CPUStreamsExecutor(const Config &config)
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor18CPUStreamsExecutorERK6Config) Constructor.

- Parameters:
**config**– Stream executor parameters


-
~CPUStreamsExecutor() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutorD0Ev) A class destructor.


-
virtual void run(
[Task](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threading4TaskE)task) override[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor3runE4Task) Execute ov::Task inside task executor context.

- Parameters:
**task**– A task to start


-
virtual void execute(
[Task](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9threading4TaskE)task) override[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor7executeE4Task) Execute the task in the current thread using streams executor configuration and constraints.

- Parameters:
**task**– A task to start


-
virtual int get_stream_id() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor13get_stream_idEv) Return the index of current stream.

- Returns:
An index of current stream. Or throw exceptions if called not from stream thread



-
virtual int get_streams_num() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor15get_streams_numEv) Return the total number of streams.

- Returns:
The total number of streams.



-
virtual int get_numa_node_id() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor16get_numa_node_idEv) Return the id of current NUMA

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)Return 0 when current stream cross some NUMA Nodes.- Returns:
`ID`

of current NUMA[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node), or throws exceptions if called not from stream thread


-
virtual int get_socket_id() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor13get_socket_idEv) Return the id of current socket Return 0 when current stream cross some sockets.

- Returns:
`ID`

of current socket, or throws exceptions if called not from stream thread


-
virtual std::vector<int> get_rank() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor8get_rankEv) Return the rank of current stream Return {} when current stream has no rank.

- Returns:
Rank array, or throws exceptions if called not from stream thread



-
virtual void cpu_reset() override
[#](https://docs.openvino.ai#_CPPv4N2ov9threading18CPUStreamsExecutor9cpu_resetEv) Reset cpu map table when user set enable_cpu_reservation = true.


-
using Ptr = std::shared_ptr<