source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1_memory_solver_1_1_box.html
lastmod: 

# Struct ov::MemorySolver::Box[#](https://docs.openvino.ai#struct-ov-memorysolver-box)

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