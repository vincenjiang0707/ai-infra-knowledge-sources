source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v13_1_1_fake_convert.html
lastmod: 

# Class ov::op::v13::FakeConvert[#](https://docs.openvino.ai#class-ov-op-v13-fakeconvert)

-
class FakeConvert : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvertE) [FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)performs element-wise quantization of input values into a set of values corresponding to a target low-precision type.Note

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)is an experimental operation and subject to change.Public Functions

-
FakeConvert(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, std::string destination_type = "f8e4m3")[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert11FakeConvertERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEENSt6stringE) Constructs

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)operation (default shift).- Parameters:
**data**– The input data tensor.**scale**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with a scale factor for the data input.**destination_type**– The low precision type to be emulated.



-
FakeConvert(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &shift, std::string destination_type = "f8e4m3")[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert11FakeConvertERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEENSt6stringE) Constructs

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)operation.

-
FakeConvert(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&destination_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert11FakeConvertERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEERKN2ov7element4TypeE) Constructs

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)operation (default shift).- Parameters:
**data**– The input data tensor.**scale**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with a scale factor for the data input.**destination_type**– The low precision type to be emulated.



-
FakeConvert(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &shift, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&destination_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert11FakeConvertERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEERKN2ov7element4TypeE) Constructs

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1311FakeConvert12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
FakeConvert(const