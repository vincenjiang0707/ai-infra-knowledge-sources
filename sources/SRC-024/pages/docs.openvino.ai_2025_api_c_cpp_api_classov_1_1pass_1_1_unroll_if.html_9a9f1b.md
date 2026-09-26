source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_unroll_if.html
lastmod: 

Class ov::pass::UnrollIf# class UnrollIf : public ov::pass::ModelPass# The transformation replaces ‘If’ operations with one of the internal functions (bodies) if the provided condition is constant. The condition is true: ‘If’ op is replaced with then_body The condition is false ‘If’ op is replaced with else_body.