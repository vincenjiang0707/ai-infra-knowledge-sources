source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_shape.html
lastmod: 

# Class ov::Shape[#](https://docs.openvino.ai#class-ov-shape)

-
class Shape : public std::vector<size_t>
[#](https://docs.openvino.ai#_CPPv4N2ov5ShapeE) [Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)for a tensor.Public Functions

- OPENVINO_API Shape::reference operator[] (std::ptrdiff_t i)
Gets dimension at index.

- Parameters:
**i**– Index to shape dimension [-rank, rank).- Returns:
A reference to i-th dimension of this shape.



- OPENVINO_API Shape::const_reference operator[] (std::ptrdiff_t i) const
Gets dimension at index.

- Parameters:
**i**– Index to shape dimension [-rank, rank).- Returns:
A const reference to i-th dimension of this shape.



- OPENVINO_API Shape::reference at (std::ptrdiff_t i)
Gets dimension at index, with bounds checking.

- Parameters:
**i**– Index to shape dimension [-rank, rank).- Returns:
A reference to i-th dimension of this shape.



- OPENVINO_API Shape::const_reference at (std::ptrdiff_t i) const
Gets dimension at index, with bounds checking.

- Parameters:
**i**– Index to shape dimension [-rank, rank).- Returns:
A const reference to i-th dimension of this shape.