source: https://docs.openvino.ai/2025/api/c_cpp_api/structov__partial__shape.html
lastmod: 

# Struct ov_partial_shape[#](https://docs.openvino.ai#struct-ov-partial-shape)

-
struct ov_partial_shape
[#](https://docs.openvino.ai#_CPPv416ov_partial_shape) It represents a shape that may be partially or totally dynamic. A PartialShape may have: Dynamic rank. (Informal notation:

`?`

) Static rank, but dynamic dimensions on some or all axes. (Informal notation examples:`{1,2,?,4}`

,`{?,?,?}`

,`{-1,-1,-1}`

) Static rank, and static dimensions on all axes. (Informal notation examples:`{1,2,3,4}`

,`{6}`

,`{}`

)An interface to make user can initialize ov_partial_shape_t