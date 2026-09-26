source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v13_1_1_multinomial.html
lastmod: 

# Class ov::op::v13::Multinomial[#](https://docs.openvino.ai#class-ov-op-v13-multinomial)

-
class Multinomial : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311MultinomialE) [Multinomial](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_multinomial)operation creates a sequence of indices of classes sampled from the multinomial distribution.Public Functions

-
Multinomial(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_samples, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type_t](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element6Type_tE)convert_type, const bool with_replacement, const bool log_probs, const uint64_t global_seed = 0, const uint64_t op_seed = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311Multinomial11MultinomialERK6OutputI4NodeERK6OutputI4NodeEKN2ov7element6Type_tEKbKbK8uint64_tK8uint64_t) [Multinomial](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_multinomial)operation creates a sequence of indices of classes sampled from the multinomial distribution.- Parameters:
**probs**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor containing at each index poisition probability/log probability of sampling a given class.[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)floating-point precision values are allowed.**num_samples**– Scalar or 1D tensor with a single value that determines the number of samples to generate per batch. Values should be of an integer type.**convert_type**– Data type to which to convert the output class indices. Allowed values: i32/i64**with_replacement**– Boolean that determines whether a sampled class can appear more than once in the output.**log_probs**– Boolean that determines whether to treat input probabilities as log probabilities.**global_seed**– First seed value (key) of Philox random number generation algorithm. (See RandomUniform for details)**op_seed**– Second seed value (counter) of Philox random number generation algorithm. (See RandomUniform for details)



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311Multinomial24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Multinomial(const