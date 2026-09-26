source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1philox_1_1_tensorflow_philox_converter.html
lastmod: 

# Class ov::reference::philox::TensorflowPhiloxConverter[#](https://docs.openvino.ai#class-ov-reference-philox-tensorflowphiloxconverter)

-
class TensorflowPhiloxConverter : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[reference](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9referenceE)::[philox](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philoxE)::[PhiloxConverter](https://docs.openvino.ai/classov_1_1reference_1_1philox_1_1_philox_converter.html#_CPPv4N2ov9reference6philox15PhiloxConverterE)[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox25TensorflowPhiloxConverterE) Public Functions

-
virtual size_t get_converted_elements_count() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov9reference6philox25TensorflowPhiloxConverter28get_converted_elements_countEv) Returns the number of generated elements per execution based on the requested data type.


-
virtual void convert(const
[PhiloxOutput](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philox12PhiloxOutputE)result, size_t idx) override[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox25TensorflowPhiloxConverter7convertEK12PhiloxOutput6size_t) Converts the given array (PhiloxOutput) to the target dtype and assigns them at the k-th index of the output array.


-
virtual size_t get_converted_elements_count() const override