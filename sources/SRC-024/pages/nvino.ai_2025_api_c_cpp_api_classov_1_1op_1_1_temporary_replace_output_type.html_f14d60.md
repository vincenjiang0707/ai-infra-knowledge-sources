source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1_temporary_replace_output_type.html
lastmod: 

# Class ov::op::TemporaryReplaceOutputType[#](https://docs.openvino.ai#class-ov-op-temporaryreplaceoutputtype)

-
class TemporaryReplaceOutputType
[#](https://docs.openvino.ai#_CPPv4N2ov2op26TemporaryReplaceOutputTypeE) Set another type for a specified output for the period of time when an instance of the class exists. When the execution leaves the scope where an onject of

[TemporaryReplaceOutputType](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_temporary_replace_output_type)is defined, the type of the output is set to its original value. Used when initialized TypeRelaxed<BaseOp> operation in case when inputs have types that are not compatible with BaseOp infer function. In this case before[TypeRelaxed](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_type_relaxed)is constructed the BaseOp contructor requires modified data types. So it should be