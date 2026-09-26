source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_mapped_memory.html
lastmod: 

# Class ov::MappedMemory[#](https://docs.openvino.ai#class-ov-mappedmemory)

-
class MappedMemory
[#](https://docs.openvino.ai#_CPPv4N2ov12MappedMemoryE) This class represents a mapped memory. Instead of reading files, we can map the memory via mmap for Linux or MapViewOfFile for Windows. The

[MappedMemory](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_mapped_memory)class is a abstraction to handle such memory with os-dependent details.