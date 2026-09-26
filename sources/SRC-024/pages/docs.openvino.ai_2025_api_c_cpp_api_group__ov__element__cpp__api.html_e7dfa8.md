source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__element__cpp__api.html
lastmod: 

# Group Element types[#](https://docs.openvino.ai#group-element-types)

-
*group*Element types OpenVINO Element API to work with OpenVINO element types

Enums

-
enum class Type_t
[#](https://docs.openvino.ai#_CPPv46Type_t) Enum to define possible element types.

*Values:*-
enumerator dynamic
[#](https://docs.openvino.ai#_CPPv4N6Type_t7dynamicE) Dynamic element type.


-
enumerator OPENVINO_ENUM_DEPRECATED
[#](https://docs.openvino.ai#_CPPv4N6Type_t24OPENVINO_ENUM_DEPRECATEDE) Undefined element type.


-
enumerator boolean
[#](https://docs.openvino.ai#_CPPv4N6Type_t7booleanE) boolean element type


-
enumerator bf16
[#](https://docs.openvino.ai#_CPPv4N6Type_t4bf16E) bf16 element type


-
enumerator f16
[#](https://docs.openvino.ai#_CPPv4N6Type_t3f16E) f16 element type


-
enumerator f32
[#](https://docs.openvino.ai#_CPPv4N6Type_t3f32E) f32 element type


-
enumerator f64
[#](https://docs.openvino.ai#_CPPv4N6Type_t3f64E) f64 element type


-
enumerator i4
[#](https://docs.openvino.ai#_CPPv4N6Type_t2i4E) i4 element type


-
enumerator i8
[#](https://docs.openvino.ai#_CPPv4N6Type_t2i8E) i8 element type


-
enumerator i16
[#](https://docs.openvino.ai#_CPPv4N6Type_t3i16E) i16 element type


-
enumerator i32
[#](https://docs.openvino.ai#_CPPv4N6Type_t3i32E) i32 element type


-
enumerator i64
[#](https://docs.openvino.ai#_CPPv4N6Type_t3i64E) i64 element type


-
enumerator u1
[#](https://docs.openvino.ai#_CPPv4N6Type_t2u1E) binary element type


-
enumerator u2
[#](https://docs.openvino.ai#_CPPv4N6Type_t2u2E) u2 element type


-
enumerator u3
[#](https://docs.openvino.ai#_CPPv4N6Type_t2u3E) u3 element type


-
enumerator u4
[#](https://docs.openvino.ai#_CPPv4N6Type_t2u4E) u4 element type


-
enumerator u6
[#](https://docs.openvino.ai#_CPPv4N6Type_t2u6E) u6 element type


-
enumerator u8
[#](https://docs.openvino.ai#_CPPv4N6Type_t2u8E) u8 element type


-
enumerator u16
[#](https://docs.openvino.ai#_CPPv4N6Type_t3u16E) u16 element type


-
enumerator u32
[#](https://docs.openvino.ai#_CPPv4N6Type_t3u32E) u32 element type


-
enumerator u64
[#](https://docs.openvino.ai#_CPPv4N6Type_t3u64E) u64 element type


-
enumerator nf4
[#](https://docs.openvino.ai#_CPPv4N6Type_t3nf4E) nf4 element type


-
enumerator f8e4m3
[#](https://docs.openvino.ai#_CPPv4N6Type_t6f8e4m3E) f8e4m3 element type


-
enumerator f8e5m2
[#](https://docs.openvino.ai#_CPPv4N6Type_t6f8e5m2E) f8e5m2 element type


-
enumerator string
[#](https://docs.openvino.ai#_CPPv4N6Type_t6stringE) string element type


-
enumerator f4e2m1
[#](https://docs.openvino.ai#_CPPv4N6Type_t6f4e2m1E) f4e2m1 element type


-
enumerator f8e8m0
[#](https://docs.openvino.ai#_CPPv4N6Type_t6f8e8m0E) f8e8m0 element type


-
enumerator dynamic

Functions

- inline constexpr OPENVINO_SUPPRESS_DEPRECATED_START Type undefined (Type_t::undefined)
undefined element type


- inline constexpr OPENVINO_SUPPRESS_DEPRECATED_END Type dynamic (Type_t::dynamic)
dynamic element type


-
class Type
*#include <element_type.hpp>*Base class to define element type.

Public Functions

Public Static Functions

-
static bool merge(
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&dst, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&t1, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&t2) Merges two element types t1 and t2, writing the result into dst and returning true if successful, else returning false.

To “merge” two element types t1 and t2 is to find the least restrictive element type t that is no more restrictive than t1 and t2, if t exists. More simply:

merge(dst,element::Type::dynamic,t) writes t to dst and returns true

merge(dst,t,element::Type::dynamic) writes t to dst and returns true

merge(dst,t1,t2) where t1, t2 both static and equal writes t1 to dst and returns true

merge(dst,t1,t2) where t1, t2 both static and unequal does nothing to dst, and returns false


-
static bool merge(

-
enum class Type_t