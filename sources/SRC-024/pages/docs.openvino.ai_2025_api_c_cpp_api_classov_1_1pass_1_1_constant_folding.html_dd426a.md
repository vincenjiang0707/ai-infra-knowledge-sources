source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_constant_folding.html
lastmod: 

Class ov::pass::ConstantFolding# class ConstantFolding : public ov::pass::ModelPass# Constant folding iterates over the function and tries to evaluate nodes with constant inputs. Such nodes are then replaced with new Constants containing the result of a folded operation.