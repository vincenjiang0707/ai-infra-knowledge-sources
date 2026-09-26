source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1_get_original_coordinate.html
lastmod: 

# Class ov::reference::GetOriginalCoordinate[#](https://docs.openvino.ai#class-ov-reference-getoriginalcoordinate)

-
class GetOriginalCoordinate
[#](https://docs.openvino.ai#_CPPv4N2ov9reference21GetOriginalCoordinateE) Calculation of the source coordinate using the resized coordinate.

Public Functions

-
inline GetOriginalCoordinate()
[#](https://docs.openvino.ai#_CPPv4N2ov9reference21GetOriginalCoordinate21GetOriginalCoordinateEv) Constructs calculation of a nearest pixel in the default mode.


-
inline GetOriginalCoordinate(
[Transform_mode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference14Transform_modeE)mode)[#](https://docs.openvino.ai#_CPPv4N2ov9reference21GetOriginalCoordinate21GetOriginalCoordinateE14Transform_mode) Constructs calculation of the source coordinate.

- Parameters:
**mode**– the mode of the calculation of the source coordinate.


-
inline float operator()(float x_resized, float x_scale, float length_resized, float length_original) const
[#](https://docs.openvino.ai#_CPPv4NK2ov9reference21GetOriginalCoordinateclEffff) Performing the source coordinate calculation.

- Parameters:
**x_resized**– resized coordinate**x_scale**– scale for the considered axis**length_resized**– length of the resized axis**length_original**– original length of the axis

- Returns:
the source coordinate



-
inline GetOriginalCoordinate()