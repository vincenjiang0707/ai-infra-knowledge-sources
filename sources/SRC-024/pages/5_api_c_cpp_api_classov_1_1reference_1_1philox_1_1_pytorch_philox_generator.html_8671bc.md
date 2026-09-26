source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1reference_1_1philox_1_1_pytorch_philox_generator.html
lastmod: 

# Class ov::reference::philox::PytorchPhiloxGenerator[#](https://docs.openvino.ai#class-ov-reference-philox-pytorchphiloxgenerator)

-
class PytorchPhiloxGenerator : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[reference](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9referenceE)::[philox](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philoxE)::[PhiloxGenerator](https://docs.openvino.ai/classov_1_1reference_1_1philox_1_1_philox_generator.html#_CPPv4N2ov9reference6philox15PhiloxGeneratorE)[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox22PytorchPhiloxGeneratorE) PyTorch specialization of the

[PhiloxGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_philox_generator)class.Public Functions

-
PytorchPhiloxGenerator(const uint64_t global_seed)
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox22PytorchPhiloxGenerator22PytorchPhiloxGeneratorEK8uint64_t) Constructor for the

[PytorchPhiloxGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1reference_1_1philox_1_1_pytorch_philox_generator)class.Note

This version of the Philox algorithm does NOT use operator seed, and. does not support the use of the previous/next state.

- Parameters:
**global_seed**– The operator seed for the Philox algorithm


-
virtual
[PhiloxOutput](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov9reference6philox12PhiloxOutputE)random() override[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox22PytorchPhiloxGenerator6randomEv) Get a set of random 32-bit unsigned integers based on the seed(s).

- Returns:
A structure with a random set of 32-bit unsigned integers and their count.



-
virtual std::pair<uint64_t, uint64_t> get_next_state() override
[#](https://docs.openvino.ai#_CPPv4N2ov9reference6philox22PytorchPhiloxGenerator14get_next_stateEv) Returns the INPUT state to feed to the next execution, as the algorithm does not use this to compute results.


-
PytorchPhiloxGenerator(const uint64_t global_seed)