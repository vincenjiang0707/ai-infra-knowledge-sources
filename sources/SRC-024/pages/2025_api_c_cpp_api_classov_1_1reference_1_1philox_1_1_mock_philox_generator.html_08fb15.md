source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1philox_1_1_mock_philox_generator.html
lastmod: 

# Class ov::reference::philox::MockPhiloxGenerator[#](https://docs.openvino.ai#class-ov-reference-philox-mockphiloxgenerator)

-
class MockPhiloxGenerator : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[reference](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9referenceE)::[philox](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philoxE)::[PhiloxGenerator](https://docs.openvino.ai/classov_1_1reference_1_1philox_1_1_philox_generator.html#_CPPv4N2ov9reference6philox15PhiloxGeneratorE)[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox19MockPhiloxGeneratorE) Mock specialization of the

[PhiloxGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_philox_generator)class (in case of unknown alignment).Public Functions

-
virtual
[PhiloxOutput](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philox12PhiloxOutputE)random() override[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox19MockPhiloxGenerator6randomEv) Get a set of 4 32-bit unsigned integers (zeros).

- Returns:
A structure with a set of 32-bit zeros.



-
virtual std::pair<uint64_t, uint64_t> get_next_state() override
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox19MockPhiloxGenerator14get_next_stateEv) Returns the modified state to feed to the next execution.

- Returns:
A pair of uint64s that represent the output state to be fed to the next generator execution.



-
virtual