source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1_profiling_info.html
lastmod: 

Represents basic inference profiling information per operation.

If the operation is executed using tiling, the sum time per each tile is indicated as the total execution time. Due to parallel execution, the total execution time for all nodes might be greater than the total inference time.

Public Types

-
enum class Status

Defines the general status of a node.

*Values:*

-
enumerator NOT_RUN

A node is not executed.


-
enumerator OPTIMIZED_OUT

A node is optimized out during graph optimization phase.


-
enumerator EXECUTED

A node is executed.



Public Members

-
[Status](#_CPPv4N2ov13ProfilingInfo6StatusE) status

Defines the node status.


-
std::chrono::microseconds real_time

The absolute time, in microseconds, that the node ran (in total).


-
std::chrono::microseconds cpu_time

The net host CPU time that the node ran.


-
std::string node_name

Name of a node.


-
std::string exec_type

Execution type of a unit.


-
std::string node_type

[Node](group__ov__transformation__common__api.html#classov_1_1_node) type.