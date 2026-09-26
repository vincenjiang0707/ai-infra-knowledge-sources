source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1pass_1_1_optimize_symbols_used_as_values.html
lastmod: 

Class ov::pass::OptimizeSymbolsUsedAsValues# class OptimizeSymbolsUsedAsValues : public ov::pass::ModelPass# Collects sources where each symbol initially appeared (on shape or shape sub-graph) and attaches all value usages of this label to this initial source.