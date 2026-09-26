source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_node_validation_failure.html
lastmod: 

# Class ov::NodeValidationFailure[#](https://docs.openvino.ai#class-ov-nodevalidationfailure)

-
class NodeValidationFailure : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AssertFailure](https://docs.openvino.ai/classov_1_1_assert_failure.html#_CPPv4N2ov13AssertFailureE)[#](https://docs.openvino.ai#_CPPv4N2ov21NodeValidationFailureE) Public Functions

- template<> OPENVINO_API void create (const char *file, int line, const char *check_string, std::pair< const Node *, const std::vector< PartialShape > * > &&ctx, const std::string &explanation)
Specialization to throw the


for shape inference using[NodeValidationFailure](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node_validation_failure)[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)- Parameters:
**check_loc_info**–[Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)location details to print.**ctx**–[NodeValidationFailure](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node_validation_failure)context which got pointer to node and input shapes used for shape inference.**explanation**–[Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)explanation string.