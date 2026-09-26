source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1element_1_1_type.html
lastmod: 

# Class ov::element::Type[#](https://docs.openvino.ai#class-ov-element-type)

-
class Type
[#](https://docs.openvino.ai#_CPPv4N2ov7element4TypeE) Base class to define element type.

Public Functions

Public Static Functions

-
static bool merge(
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai#_CPPv4N2ov7element4TypeE)&dst, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai#_CPPv4N2ov7element4TypeE)&t1, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai#_CPPv4N2ov7element4TypeE)&t2)[#](https://docs.openvino.ai#_CPPv4N2ov7element4Type5mergeERN7element4TypeERKN7element4TypeERKN7element4TypeE) Merges two element types t1 and t2, writing the result into dst and returning true if successful, else returning false.

To “merge” two element types t1 and t2 is to find the least restrictive element type t that is no more restrictive than t1 and t2, if t exists. More simply:

merge(dst,element::Type::dynamic,t) writes t to dst and returns true

merge(dst,t,element::Type::dynamic) writes t to dst and returns true

merge(dst,t1,t2) where t1, t2 both static and equal writes t1 to dst and returns true

merge(dst,t1,t2) where t1, t2 both static and unequal does nothing to dst, and returns false


-
static bool merge(