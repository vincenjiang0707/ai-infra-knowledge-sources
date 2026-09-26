source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1util_1_1_interpolate_base.html
lastmod: 

# Class ov::op::util::InterpolateBase[#](https://docs.openvino.ai#class-ov-op-util-interpolatebase)

-
class InterpolateBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBaseE) Subclassed by

[ov::op::v11::Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_interpolate),[ov::op::v4::Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_interpolate)Public Types

-
enum class ShapeCalcMode
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase13ShapeCalcModeE) [PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)calculation mode.SIZES - output shape for interpolated axes is calculated using input

`sizes`

SCALES - output shape for interpolated axes is calculated using input`scales`

*Values:*-
enumerator SIZES
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase13ShapeCalcMode5SIZESE)

-
enumerator SCALES
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase13ShapeCalcMode6SCALESE)

-
enumerator SIZES

-
enum class InterpolateMode
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase15InterpolateModeE) Interpolation mode.

NEAREST - nearest interpolation LINEAR - linear interpolation as in TensorFlow LINEAR_ONNX - linear interpolation as in ONNX CUBIC - cubic interpolation BILINEAR_PILLOW - bilinear interpolation as in Pillow BICUBIC_PILLOW - bicubic interpolation as in Pillow

*Values:*-
enumerator NEAREST
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase15InterpolateMode7NEARESTE)

-
enumerator LINEAR
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase15InterpolateMode6LINEARE)

-
enumerator LINEAR_ONNX
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase15InterpolateMode11LINEAR_ONNXE)

-
enumerator CUBIC
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase15InterpolateMode5CUBICE)

-
enumerator BILINEAR_PILLOW
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase15InterpolateMode15BILINEAR_PILLOWE)

-
enumerator BICUBIC_PILLOW
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase15InterpolateMode14BICUBIC_PILLOWE)

-
enumerator NEAREST

Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct InterpolateAttrs
[#](https://docs.openvino.ai#_CPPv4N2ov2op4util15InterpolateBase16InterpolateAttrsE)

-
enum class ShapeCalcMode