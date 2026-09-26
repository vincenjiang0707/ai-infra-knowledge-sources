source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1internal_1_1_dynamic_quantize.html
lastmod: 

# Class ov::op::internal::DynamicQuantize[#](https://docs.openvino.ai#class-ov-op-internal-dynamicquantize)

-
class DynamicQuantize : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantizeE) Operator performing Dynamic Quantize.

Public Types

-
enum class QuantizationType
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize16QuantizationTypeE) Configuration for the type of quantization applied to the data:

Symmetric: Quantization where the zero point is fixed at zero, and the range is symmetric around zero.

Asymmetric: Quantization where the zero point is not fixed at zero.


*Values:*-
enumerator Symmetric
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize16QuantizationType9SymmetricE)

-
enumerator Asymmetric
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize16QuantizationType10AsymmetricE)


-
enum class OutputStorageType
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize17OutputStorageTypeE) Configuration for how Activations, Scales and Zero Points will be stored in output buffers:

Planar: Activations, Scales, and Zero Points are stored in independent buffers.

InterleavedScalesZP: Activations are stored in an independent buffer, while Scales and Zero Points (if any) are combined in a separate buffer.


*Values:*-
enumerator Planar
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize17OutputStorageType6PlanarE)

-
enumerator InterleavedScalesZP
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize17OutputStorageType19InterleavedScalesZPE)


Public Functions

-
DynamicQuantize(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Attributes](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize15DynamicQuantizeERK6OutputI4NodeERK10Attributes) Constructs an

[DynamicQuantize](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_dynamic_quantize)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**config**– Dynamic quantization configuration



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal15DynamicQuantize10AttributesE) Structure that specifies attributes for interpolation.


-
enum class QuantizationType