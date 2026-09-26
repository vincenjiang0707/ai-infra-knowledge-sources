source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_pass_base.html
lastmod: 

# Class ov::pass::PassBase[#](https://docs.openvino.ai#class-ov-pass-passbase)

-
class PassBase
[#](https://docs.openvino.ai#_CPPv4N2ov4pass8PassBaseE) Base class for transformation passes.

Subclassed by

[ov::pass::MatcherPass](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_matcher_pass),[ov::pass::ModelPass](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_model_pass)Public Functions

-
bool get_property(const
[PassPropertyMask](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass16PassPropertyMaskE)&prop_mask) const[#](https://docs.openvino.ai#_CPPv4NK2ov4pass8PassBase12get_propertyERK16PassPropertyMask) Check if this pass has all the pass properties.


-
void set_callback(const
[param_callback](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4pass14param_callbackE)&callback)[#](https://docs.openvino.ai#_CPPv4N2ov4pass8PassBase12set_callbackERK14param_callback) Set callback for particular transformation type. This method set global callback. For more details see

[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)class documentation.- Parameters:
**callback**– lambda function that takes node and returns bool


Set

[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)for particular transformation instance.- Parameters:
**pass_config**– is a[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)shared_ptr


-
inline std::shared_ptr<
[PassConfig](https://docs.openvino.ai/classov_1_1pass_1_1_pass_config.html#_CPPv4N2ov4pass10PassConfigE)> get_pass_config()[#](https://docs.openvino.ai#_CPPv4N2ov4pass8PassBase15get_pass_configEv) Allows to access

[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)shared instance.- Returns:
Shared instance of

[PassConfig](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_pass_config)class


Applies callback for given node. By default callback returns false.

- Parameters:
**node**– which will be used inside callback- Returns:
result of callback execution for given node



-
bool get_property(const