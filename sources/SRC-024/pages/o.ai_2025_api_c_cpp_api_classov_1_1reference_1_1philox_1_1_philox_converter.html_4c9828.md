source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1philox_1_1_philox_converter.html
lastmod: 

# Class ov::reference::philox::PhiloxConverter[#](https://docs.openvino.ai#class-ov-reference-philox-philoxconverter)

-
class PhiloxConverter
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox15PhiloxConverterE) Subclassed by

[ov::reference::philox::MockPhiloxConverter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_mock_philox_converter),[ov::reference::philox::PyTorchPhiloxConverter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_py_torch_philox_converter),[ov::reference::philox::TensorflowPhiloxConverter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_tensorflow_philox_converter)Public Functions

-
virtual size_t get_converted_elements_count() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov9reference6philox15PhiloxConverter28get_converted_elements_countEv) Returns the number of generated elements per execution based on the requested data type.


-
virtual void convert(const
[PhiloxOutput](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philox12PhiloxOutputE)result, size_t k) = 0[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox15PhiloxConverter7convertEK12PhiloxOutput6size_t) Converts the given array (PhiloxOutput) to the target dtype and assigns them at the k-th index of the output array.


-
virtual size_t get_converted_elements_count() const = 0