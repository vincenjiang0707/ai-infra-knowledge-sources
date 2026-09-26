source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_memory_solver.html
lastmod: 

# Class ov::MemorySolver[#](https://docs.openvino.ai#class-ov-memorysolver)

-
class MemorySolver
[#](https://docs.openvino.ai#_CPPv4N2ov12MemorySolverE) Helps to solve issue of optimal memory allocation only for particular execution order.

It works with abstract data description where

Example:

Mem(offset) | |____|

[Box](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1_memory_solver_1_1_box){4, 5} | |_____________|[Box](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1_memory_solver_1_1_box){2, 6} | |____|[Box](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1_memory_solver_1_1_box){3, 4} | |____|[Box](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1_memory_solver_1_1_box){2, 3} | |____|[Box](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1_memory_solver_1_1_box){6, 7} |_____________________________________ 1 2 3 4 5 6 7 8 9 ExecOrderBoxes which has an ExecOrder-axis intersection should have no Mem-axis intersections. The goal is to define a minimal required memory blob to store all boxes with such constraints and specify all corresponding position on Mem axis(through offset field).

NOTE! Exec order is predefined.

Public Functions

-
inline int64_t solve()
[#](https://docs.openvino.ai#_CPPv4N2ov12MemorySolver5solveEv) Solve memory location with maximal reuse.

- Returns:
Size of common memory blob required for storing all



-
inline int64_t get_offset(int id) const
[#](https://docs.openvino.ai#_CPPv4NK2ov12MemorySolver10get_offsetEi) Provides calculated offset for specified box id


-
inline int64_t max_depth()
[#](https://docs.openvino.ai#_CPPv4N2ov12MemorySolver9max_depthEv) Additional info. Max sum of box sizes required for any time stamp.


-
inline int64_t max_top_depth()
[#](https://docs.openvino.ai#_CPPv4N2ov12MemorySolver13max_top_depthEv) Additional info. Max num of boxes required for any time stamp.


Public Static Functions

-
struct Box
[#](https://docs.openvino.ai#_CPPv4N2ov12MemorySolver3BoxE) Representation of edge (size and live time)

Public Members

-
int start
[#](https://docs.openvino.ai#_CPPv4N2ov12MemorySolver3Box5startE) Execution order index of first use. The data will be produced here.


-
int finish
[#](https://docs.openvino.ai#_CPPv4N2ov12MemorySolver3Box6finishE) The execution order index of last use. After that data will be released. -1 is a reserved value for “till to end”. The data will be alive to very end of execution.


-
int64_t size
[#](https://docs.openvino.ai#_CPPv4N2ov12MemorySolver3Box4sizeE) Size of data. In abstract unit of measure (byte, simd, cache line, …)


-
int start

-
inline int64_t solve()