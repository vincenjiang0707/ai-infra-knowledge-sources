source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_coordinate_transform_basic.html
lastmod: 

# Class ov::CoordinateTransformBasic[#](https://docs.openvino.ai#class-ov-coordinatetransformbasic)

-
class CoordinateTransformBasic
[#](https://docs.openvino.ai#_CPPv4N2ov24CoordinateTransformBasicE) Class which allows to calculate item index with given coordinates in tensor and helps to iterate over all coordinates.

[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)items should be placed in memory in row-major order.Public Functions

-
[CoordinateIterator](https://docs.openvino.ai/classov_1_1_coordinate_iterator.html#_CPPv4N2ov18CoordinateIteratorE)begin() const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov24CoordinateTransformBasic5beginEv) Returns an iterator to the first coordinate of the tensor.


-
const
[CoordinateIterator](https://docs.openvino.ai/classov_1_1_coordinate_iterator.html#_CPPv4N2ov18CoordinateIteratorE)&end() const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov24CoordinateTransformBasic3endEv) Returns an iterator to the coordinate following the last element of the tensor.


-