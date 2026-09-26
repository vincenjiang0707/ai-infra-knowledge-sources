source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_decoder_base.html
lastmod: 

# Class ov::frontend::DecoderBase[#](https://docs.openvino.ai#class-ov-frontend-decoderbase)

-
class DecoderBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[frontend](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov8frontendE)::[IDecoder](https://docs.openvino.ai/classov_1_1frontend_1_1_i_decoder.html#_CPPv4N2ov8frontend8IDecoderE)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend11DecoderBaseE) Public Functions

-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Any](https://docs.openvino.ai/classov_1_1_any.html#_CPPv4N2ov3AnyE)get_attribute(const std::string &name) const = 0[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11DecoderBase13get_attributeERKNSt6stringE) Get attribute value by name.

- Parameters:
**name**– Attribute name- Returns:
Shared pointer to appropriate value converted to openvino data type if it exists, ‘nullptr’ otherwise



-
virtual size_t get_input_size() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11DecoderBase14get_input_sizeEv) Get a number of inputs.


-
virtual void get_input_node(size_t input_port_idx, std::string &producer_name, std::string &producer_output_port_name, size_t &producer_output_port_index) const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11DecoderBase14get_input_nodeE6size_tRNSt6stringERNSt6stringER6size_t) Get a producer name and its output port index.


-
virtual const std::string &get_op_type() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11DecoderBase11get_op_typeEv) Get operation type.


-
virtual const std::string &get_op_name() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend11DecoderBase11get_op_nameEv) Get node name.


-
virtual ~DecoderBase()
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend11DecoderBaseD0Ev) Destructor.


-
virtual