source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_hash.html
lastmod: 

# Class ov::pass::Hash[#](https://docs.openvino.ai#class-ov-pass-hash)

-
class Hash : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[pass](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov4passE)::[ModelPass](https://docs.openvino.ai/classov_1_1pass_1_1_model_pass.html#_CPPv4N2ov4pass9ModelPassE)[#](https://docs.openvino.ai#_CPPv4N2ov4pass4HashE) [Hash](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_hash)transformation calculates hash value for[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).Public Functions

-
Hash(uint64_t &output_hash_value, bool skip_weights = false)
[#](https://docs.openvino.ai#_CPPv4N2ov4pass4Hash4HashER8uint64_tb) [Hash](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1_hash)pass constructor.- Parameters:
**output_hash_value**– Reference to output value. By applying hash pass on function, resulting hash value will be set to this variable**skip_weights**– If set to true, simplifies the hashing process by excluding weights values.



-
Hash(uint64_t &output_hash_value, bool skip_weights = false)