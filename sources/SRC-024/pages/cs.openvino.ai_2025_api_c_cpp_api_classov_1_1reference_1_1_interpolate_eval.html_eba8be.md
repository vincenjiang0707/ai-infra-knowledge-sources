source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1_interpolate_eval.html
lastmod: 

# Class ov::reference::InterpolateEval[#](https://docs.openvino.ai#class-ov-reference-interpolateeval)

-
template<typename T>

class InterpolateEval[#](https://docs.openvino.ai#_CPPv4I0EN2ov9reference15InterpolateEvalE) Class to perform interpolation calculation.

Public Functions

-
inline InterpolateEval(const
[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[v4](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op2v4E)::[Interpolate](https://docs.openvino.ai/classov_1_1op_1_1v4_1_1_interpolate.html#_CPPv4N2ov2op2v411InterpolateE)::InterpolateAttrs &attrs)[#](https://docs.openvino.ai#_CPPv4N2ov9reference15InterpolateEval15InterpolateEvalERKN2op2v411Interpolate16InterpolateAttrsE) Constructs interpolation calculation using Interpolate attributes.

- Parameters:
**attrs**– Interpolate-4 attributes.


-
inline void operator()(const
[T](https://docs.openvino.ai#_CPPv4I0EN2ov9reference15InterpolateEvalE)*input_data, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&input_data_shape, const std::vector<float> &scales, const std::vector<int64_t> &axes,[T](https://docs.openvino.ai#_CPPv4I0EN2ov9reference15InterpolateEvalE)*out, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&out_shape)[#](https://docs.openvino.ai#_CPPv4N2ov9reference15InterpolateEvalclEPK1TRK5ShapeRKNSt6vectorIfEERKNSt6vectorI7int64_tEEP1TRK5Shape) Performing interpolation calculation.

- Parameters:
**input_data**– pointer to input data**input_data_shape**– shape of the input data**scales**– scale factors for each interpolated axis**axes**– axes to interpolate**out**– pointer to memory block for output data**out_shape**– shape of output data



-
inline InterpolateEval(const