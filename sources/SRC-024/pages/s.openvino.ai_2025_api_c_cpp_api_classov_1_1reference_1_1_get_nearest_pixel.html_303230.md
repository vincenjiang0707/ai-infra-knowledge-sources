source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1_get_nearest_pixel.html
lastmod: 

# Class ov::reference::GetNearestPixel[#](https://docs.openvino.ai#class-ov-reference-getnearestpixel)

-
class GetNearestPixel
[#](https://docs.openvino.ai#_CPPv4N2ov9reference15GetNearestPixelE) Calculation of nearest pixel.

Public Functions

-
inline GetNearestPixel()
[#](https://docs.openvino.ai#_CPPv4N2ov9reference15GetNearestPixel15GetNearestPixelEv) Constructs calculation of a nearest pixel in the default mode.


-
inline GetNearestPixel(
[Nearest_mode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference12Nearest_modeE)mode)[#](https://docs.openvino.ai#_CPPv4N2ov9reference15GetNearestPixel15GetNearestPixelE12Nearest_mode) Constructs calculation of nearest pixel for the specified mode.

- Parameters:
**mode**– the mode of the calculation of the nearest pixel


-
inline int64_t operator()(float original, bool is_downsample) const
[#](https://docs.openvino.ai#_CPPv4NK2ov9reference15GetNearestPixelclEfb) Performing the nearest pixel calculation.

- Parameters:
**original**– original coordinate**is_downsample**– true if it has downsample and false otherwise

- Returns:
the nearest pixel



-
inline GetNearestPixel()