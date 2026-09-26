source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_bucketize.html
lastmod: 

# Class ov::op::v3::Bucketize[#](https://docs.openvino.ai#class-ov-op-v3-bucketize)

-
class Bucketize : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39BucketizeE) Operation that bucketizes the input based on boundaries.

Public Functions

-
Bucketize(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &buckets, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)output_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E), const bool with_right_bound = true)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Bucketize9BucketizeERK6OutputI4NodeERK6OutputI4NodeEKN7element4TypeEKb) Constructs a

[Bucketize](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_bucketize)node.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Bucketize24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Bucketize(const