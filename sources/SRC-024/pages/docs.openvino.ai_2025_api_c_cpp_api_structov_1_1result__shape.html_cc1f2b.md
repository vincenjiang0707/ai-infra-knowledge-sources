source: https://docs.openvino.ai/2025/api/c_cpp_api/structov_1_1result__shape.html
lastmod: 

# Struct ov::result_shape[#](https://docs.openvino.ai#struct-ov-result-shape)

-
template<class TShape>

struct result_shape[#](https://docs.openvino.ai#_CPPv4I0EN2ov12result_shapeE) Get correct return type of input shape when call

`shape_infer`

.The input shapes are vector like std::vector<TShape>, where

`TShape`

can be`std::vector<const size_t>`

This will provide correct return especially for static shape which can work as reference to dimension or hold them.- Template Parameters:
**TShape**– Type of input shape.