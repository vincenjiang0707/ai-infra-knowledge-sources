source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v3_1_1_atanh.html
lastmod: 

Class ov::op::v3::Atanh# class Atanh : public ov::op::util::UnaryElementwiseArithmetic# Elementwise inverse hyperbolic tangent operation. Public Functions Atanh() = default# Constructs an Atanh operation. Atanh(const Output<Node> &arg)# Constructs an Atanh operation. Output [d1, ...] Parameters: arg – Output that produces the input tensor.[d1, ...] virtual bool has_evaluate() const override# Allows to get information about availability of evaluate method for the current operation.