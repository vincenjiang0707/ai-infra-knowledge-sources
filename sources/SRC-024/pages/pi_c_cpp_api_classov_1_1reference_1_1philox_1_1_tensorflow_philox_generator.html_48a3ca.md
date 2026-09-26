source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1philox_1_1_tensorflow_philox_generator.html
lastmod: 

# Class ov::reference::philox::TensorflowPhiloxGenerator[#](https://docs.openvino.ai#class-ov-reference-philox-tensorflowphiloxgenerator)

-
class TensorflowPhiloxGenerator : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[reference](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9referenceE)::[philox](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philoxE)::[PhiloxGenerator](https://docs.openvino.ai/classov_1_1reference_1_1philox_1_1_philox_generator.html#_CPPv4N2ov9reference6philox15PhiloxGeneratorE)[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox25TensorflowPhiloxGeneratorE) OpenVINO specialization of the

[PhiloxGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_philox_generator)class.Public Functions

-
TensorflowPhiloxGenerator(const uint64_t global_seed, const uint64_t operator_seed, const std::pair<uint64_t, uint64_t> previous_state)
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox25TensorflowPhiloxGenerator25TensorflowPhiloxGeneratorEK8uint64_tK8uint64_tKNSt4pairI8uint64_t8uint64_tEE) Constructor for the

[TensorflowPhiloxGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_tensorflow_philox_generator)class.- Parameters:
**global_seed**– The global seed for the Philox algorithm**operator_seed**– The operator seed for the Philox algorithm**previous_state**– The state returned from the previous execution of the generator



-
virtual
[PhiloxOutput](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philox12PhiloxOutputE)random() override[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox25TensorflowPhiloxGenerator6randomEv) Get a set of 4 random 32-bit unsigned integers based on the seeds.

- Returns:
A structure with a random set of 32-bit unsigned integers.



-
virtual std::pair<uint64_t, uint64_t> get_next_state() override
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox25TensorflowPhiloxGenerator14get_next_stateEv) Returns the modified state to feed to the next execution.

- Returns:
A pair of uint64s that represent the output state to be fed to the next generator execution.



-
TensorflowPhiloxGenerator(const uint64_t global_seed, const uint64_t operator_seed, const std::pair<uint64_t, uint64_t> previous_state)