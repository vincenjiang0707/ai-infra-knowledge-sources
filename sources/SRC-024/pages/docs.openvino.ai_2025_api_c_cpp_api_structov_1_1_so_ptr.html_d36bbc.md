source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1_so_ptr.html
lastmod: 

# Struct ov::SoPtr[#](https://docs.openvino.ai#struct-ov-soptr)

-
template<class T>

struct SoPtr[#](https://docs.openvino.ai#_CPPv4I0EN2ov5SoPtrE) This class instantiate object using shared library.

- Template Parameters:
**T**– An type of object[SoPtr](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1_so_ptr)can hold

Public Functions

-
SoPtr() = default
[#](https://docs.openvino.ai#_CPPv4N2ov5SoPtr5SoPtrEv) Default constructor.


-
inline ~SoPtr()
[#](https://docs.openvino.ai#_CPPv4N2ov5SoPtrD0Ev) Destructor preserves unloading order of implementation object and reference to library.


Constructs an object with existing shared object reference and loaded pointer.

- Parameters:
**ptr**– pointer to the loaded object**so**– Existing reference to library



Constructs an object with existing shared object reference.

- Parameters:
**ptr**– pointer to the loaded object


Constructs an object with existing shared object reference.

- Parameters:
**ptr**– pointer to the loaded object