source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_graph_iterator.html
lastmod: 

# Class ov::frontend::GraphIterator[#](https://docs.openvino.ai#class-ov-frontend-graphiterator)

-
class GraphIterator : private
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[RuntimeAttribute](https://docs.openvino.ai/classov_1_1_runtime_attribute.html#_CPPv4N2ov16RuntimeAttributeE)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend13GraphIteratorE) Abstract representation for an input model graph that gives nodes in topologically sorted order.

Public Functions

-
virtual size_t size() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend13GraphIterator4sizeEv) Get a number of operation nodes in the graph.


-
virtual void reset() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend13GraphIterator5resetEv) Set iterator to the start position.


-
virtual void next() = 0
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend13GraphIterator4nextEv) Move to the next node in the graph.


-
virtual bool is_end() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend13GraphIterator6is_endEv) Returns true if iterator goes out of the range of available nodes.


-
virtual std::shared_ptr<
[DecoderBase](https://docs.openvino.ai/classov_1_1frontend_1_1_decoder_base.html#_CPPv4N2ov8frontend11DecoderBaseE)> get_decoder() const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend13GraphIterator11get_decoderEv) Return a pointer to a decoder of the current node.


-
virtual std::shared_ptr<
[GraphIterator](https://docs.openvino.ai#_CPPv4N2ov8frontend13GraphIteratorE)> get_body_graph_iterator(const std::string &func_name) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend13GraphIterator23get_body_graph_iteratorERKNSt6stringE) Checks if the main model graph contains a function of the requested name in the library Returns

[GraphIterator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_graph_iterator)to this function and nullptr, if it does not exist.

-
virtual std::vector<std::string> get_input_names() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend13GraphIterator15get_input_namesEv) Returns a vector of input names in the original order.


-
virtual std::vector<std::string> get_output_names() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend13GraphIterator16get_output_namesEv) Returns a vector of output names in the original order.


-
virtual std::map<std::string, std::string> get_input_names_map() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend13GraphIterator19get_input_names_mapEv) Returns a map from internal tensor name to (user-defined) external name for inputs.


-
virtual std::map<std::string, std::string> get_output_names_map() const
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend13GraphIterator20get_output_names_mapEv) Returns a map from internal tensor name to (user-defined) external name for outputs.


-
virtual size_t size() const = 0