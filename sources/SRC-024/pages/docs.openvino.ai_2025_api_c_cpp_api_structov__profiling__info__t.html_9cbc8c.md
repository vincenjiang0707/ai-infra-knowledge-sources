source: https://docs.openvino.ai/2025/api/c_cpp_api/structov__profiling__info__t.html
lastmod: 

# Struct ov_profiling_info_t[#](https://docs.openvino.ai#struct-ov-profiling-info-t)

-
struct ov_profiling_info_t
[#](https://docs.openvino.ai#_CPPv419ov_profiling_info_t) Public Members

-
enum
[ov_profiling_info_t](https://docs.openvino.ai#_CPPv419ov_profiling_info_t)::Status status[#](https://docs.openvino.ai#_CPPv4N19ov_profiling_info_t6statusE) status


-
int64_t real_time
[#](https://docs.openvino.ai#_CPPv4N19ov_profiling_info_t9real_timeE) The absolute time, in microseconds, that the node ran (in total).


-
int64_t cpu_time
[#](https://docs.openvino.ai#_CPPv4N19ov_profiling_info_t8cpu_timeE) The net host CPU time that the node ran.


-
const char *node_name
[#](https://docs.openvino.ai#_CPPv4N19ov_profiling_info_t9node_nameE) Name of a node.


-
const char *exec_type
[#](https://docs.openvino.ai#_CPPv4N19ov_profiling_info_t9exec_typeE) Execution type of a unit.


-
const char *node_type
[#](https://docs.openvino.ai#_CPPv4N19ov_profiling_info_t9node_typeE) Node type.


-
enum