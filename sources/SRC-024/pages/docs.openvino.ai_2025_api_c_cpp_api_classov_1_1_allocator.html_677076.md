source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_allocator.html
lastmod: 

# Class ov::Allocator[#](https://docs.openvino.ai#class-ov-allocator)

-
class Allocator
[#](https://docs.openvino.ai#_CPPv4N2ov9AllocatorE) Wraps allocator implementation to provide safe way to store allocater loaded from shared library And constructs default based on

`new`

`delete`

c++ calls allocator if created without parameters Accepts any[std::pmr::memory_resource](https://en.cppreference.com/w/cpp/memory/memory_resource)like allocator.Public Functions

-
~Allocator()
[#](https://docs.openvino.ai#_CPPv4N2ov9AllocatorD0Ev) Destructor preserves unloading order of implementation object and reference to library.


-
Allocator()
[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator9AllocatorEv) Default constructor.


-
Allocator(const
[Allocator](https://docs.openvino.ai#_CPPv4N2ov9Allocator9AllocatorERK9Allocator)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator9AllocatorERK9Allocator) Default copy constructor.

- Parameters:
**other**– other[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)object


-
[Allocator](https://docs.openvino.ai#_CPPv4N2ov9AllocatorE)&operator=(const[Allocator](https://docs.openvino.ai#_CPPv4N2ov9AllocatorE)&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov9AllocatoraSERK9Allocator) Default copy assignment operator.

- Parameters:
**other**– other[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)object- Returns:
reference to the current object



-
Allocator(
[Allocator](https://docs.openvino.ai#_CPPv4N2ov9Allocator9AllocatorERR9Allocator)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator9AllocatorERR9Allocator) Default move constructor.

- Parameters:
**other**– other[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)object


-
[Allocator](https://docs.openvino.ai#_CPPv4N2ov9AllocatorE)&operator=([Allocator](https://docs.openvino.ai#_CPPv4N2ov9AllocatorE)&&other) = default[#](https://docs.openvino.ai#_CPPv4N2ov9AllocatoraSERR9Allocator) Default move assignment operator.

- Parameters:
**other**– other[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)object- Returns:
reference to the current object



Initialize allocator using any allocator like object.

- Template Parameters:
**A**– Type of allocator- Parameters:
**a**– allocator object


-
void *allocate(const size_t bytes, const size_t alignment = alignof(max_align_t))
[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator8allocateEK6size_tK6size_t) Allocates memory.

- Parameters:
**bytes**– The size in bytes at least to allocate**alignment**– The alignment of storage

- Throws:
[Exception](https://docs.openvino.ai/classov_1_1_exception.html#_CPPv4N2ov9ExceptionE)– if specified size and alignment is not supported- Returns:
Handle to the allocated resource



-
void deallocate(void *ptr, const size_t bytes = 0, const size_t alignment = alignof(max_align_t)) noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov9Allocator10deallocateEPvK6size_tK6size_t) Releases the handle and all associated memory resources which invalidates the handle.

- Parameters:
**ptr**– The handle to free**bytes**– The size in bytes that was passed into[allocate()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator_1aebd41905b0026a61af51360fabaaf947)method**alignment**– The alignment of storage that was passed into[allocate()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator_1aebd41905b0026a61af51360fabaaf947)method



-
bool operator==(const
[Allocator](https://docs.openvino.ai#_CPPv4N2ov9AllocatorE)&other) const[#](https://docs.openvino.ai#_CPPv4NK2ov9AllocatoreqERK9Allocator) Compares with other

[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator).- Parameters:
**other**– Other instance of allocator- Returns:
`true`

if and only if memory allocated from one[Allocator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_allocator)can be deallocated from the other and vice versa


-
~Allocator()