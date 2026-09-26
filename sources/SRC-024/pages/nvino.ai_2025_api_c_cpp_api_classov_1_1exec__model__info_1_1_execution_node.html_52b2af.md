source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1exec__model__info_1_1_execution_node.html
lastmod: 

# Class ov::exec_model_info::ExecutionNode[#](https://docs.openvino.ai#class-ov-exec-model-info-executionnode)

-
class ExecutionNode : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov15exec_model_info13ExecutionNodeE) The Execution node which is used to represent node in execution graph.

It contains the following type of information in node runtime information:

ExecGraphInfoSerialization::ORIGINAL_NAMES

ExecGraphInfoSerialization::IMPL_TYPE

ExecGraphInfoSerialization::OUTPUT_PRECISIONS

ExecGraphInfoSerialization::PERF_COUNTER

ExecGraphInfoSerialization::OUTPUT_LAYOUTS

ExecGraphInfoSerialization::EXECUTION_ORDER

ExecGraphInfoSerialization::LAYER_TYPE

ExecGraphInfoSerialization::RUNTIME_PRECISION


Public Functions

-
ExecutionNode()
[#](https://docs.openvino.ai#_CPPv4N2ov15exec_model_info13ExecutionNode13ExecutionNodeEv) A default constructor with no node inputs and 0 output ports.


-
ExecutionNode(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::OutputVector &arguments, size_t output_size = 1)[#](https://docs.openvino.ai#_CPPv4N2ov15exec_model_info13ExecutionNode13ExecutionNodeERKN2ov12OutputVectorE6size_t) Constructs a new execution node with a given parameters.

- Parameters:
**arguments**–**[in]**Inputs nodes**output_size**–**[in]**A number of output ports



-
std::shared_ptr<
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> clone_with_new_inputs(const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::OutputVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov15exec_model_info13ExecutionNode21clone_with_new_inputsERKN2ov12OutputVectorE) Creates a new execution node with the same state, but different input nodes.

- Parameters:
**inputs**–**[in]**The input nodes- Returns:
A newly created execution node



-
virtual bool visit_attributes(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[AttributeVisitor](https://docs.openvino.ai/classov_1_1_attribute_visitor.html#_CPPv4N2ov16AttributeVisitorE)&) override[#](https://docs.openvino.ai#_CPPv4N2ov15exec_model_info13ExecutionNode16visit_attributesERN2ov16AttributeVisitorE) Visits attributes of the node.

- Parameters:
**visitor**–**[in]**An attribute visitor- Returns:
Returns

`true`

if an operation has completed successfully