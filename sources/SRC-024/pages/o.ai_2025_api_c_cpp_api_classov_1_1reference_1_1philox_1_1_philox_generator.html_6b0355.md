source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1philox_1_1_philox_generator.html
lastmod: 

# Class ov::reference::philox::PhiloxGenerator[#](https://docs.openvino.ai#class-ov-reference-philox-philoxgenerator)

-
class PhiloxGenerator
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox15PhiloxGeneratorE) Generator of random numbers based on the Philox algorithm. Abstract base class for various specializations used to match outputs based on input seed(s) for supported frameworks.

Subclassed by

[ov::reference::philox::MockPhiloxGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_mock_philox_generator),[ov::reference::philox::PytorchPhiloxGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_pytorch_philox_generator),[ov::reference::philox::TensorflowPhiloxGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_tensorflow_philox_generator)Public Functions

-
virtual
[PhiloxOutput](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philox12PhiloxOutputE)random() = 0[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox15PhiloxGenerator6randomEv) Get a set of 4 random 32-bit unsigned integers based on the seed(s).

- Returns:
A vector with a random set of 4 32-bit unsigned integers.



-
virtual std::pair<uint64_t, uint64_t> get_next_state() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox15PhiloxGenerator14get_next_stateEv) Returns the modified state to feed to the next execution.

- Returns:
A pair of uint64s that represent the output state to be fed to the next generator execution.



-
uint64_t get_global_seed() const
[#](https://docs.openvino.ai#_CPPv4NK2ov9reference6philox15PhiloxGenerator15get_global_seedEv) Returns the global seed of the generator.


-
uint64_t get_operator_seed() const
[#](https://docs.openvino.ai#_CPPv4NK2ov9reference6philox15PhiloxGenerator17get_operator_seedEv) Returns the operator seed of the generator.


-
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PhiloxAlignment](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op15PhiloxAlignmentE)get_alignment() const[#](https://docs.openvino.ai#_CPPv4NK2ov9reference6philox15PhiloxGenerator13get_alignmentEv) Returns the alignment mode of the generator.


-
std::pair<uint64_t, uint64_t> get_previous_state() const
[#](https://docs.openvino.ai#_CPPv4NK2ov9reference6philox15PhiloxGenerator18get_previous_stateEv) Returns the input (previous execution) state of the generator.


-
void set_global_seed(const uint64_t global_seed)
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox15PhiloxGenerator15set_global_seedEK8uint64_t) Setter for the global seed.

- Parameters:
**global_seed**– The new global seed for the Philox algorithm


-
void set_operator_seed(const uint64_t op_seed)
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox15PhiloxGenerator17set_operator_seedEK8uint64_t) Setter for the operator seed.

- Parameters:
**op_seed**– The new operator seed for the Philox algorithm


-
virtual