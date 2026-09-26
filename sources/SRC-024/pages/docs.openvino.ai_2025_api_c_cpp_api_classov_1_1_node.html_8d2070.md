source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_node.html
lastmod: 

# Class ov::Node[#](https://docs.openvino.ai#class-ov-node)

-
class Node : public std::enable_shared_from_this<
[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)>[#](https://docs.openvino.ai#_CPPv4N2ov4NodeE) Nodes are the backbone of the graph of Value dataflow. Every node has zero or more nodes as arguments and one value, which is either a tensor or a (possibly empty) tuple of values.

Subclassed by

[ov::op::Op](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_op),[ov::pass::pattern::op::Pattern](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1pass_1_1pattern_1_1op_1_1_pattern)Public Functions

-
virtual void validate_and_infer_types()
[#](https://docs.openvino.ai#_CPPv4N2ov4Node24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&get_autob() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node9get_autobEv) - Returns:
the autobroadcasr spec



-
virtual bool has_evaluate() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &output_values, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &input_values) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &output_values, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &input_values, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::EvaluationContext &evaluationContext) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorERKN2ov17EvaluationContextE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.**evaluation_context**– Storage of additional settings and attributes that can be used when evaluating the op.

- Returns:
true if successful



-
inline virtual OutputVector decompose_op() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node12decompose_opEv) Decomposes the FusedOp into a sub-graph consisting of core openvino ops.

- Returns:
A vector of nodes comprising the sub-graph. The order of output tensors must match the match output tensors of the FusedOp



-
virtual const type_info_t &get_type_info() const = 0
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node13get_type_infoEv) Returns the NodeTypeInfo for the node’s class. During transition to type_info, returns a dummy type_info for

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)if the class has not been updated yet.

-
void set_arguments(const NodeVector &arguments)
[#](https://docs.openvino.ai#_CPPv4N2ov4Node13set_argumentsERK10NodeVector) Sets/replaces the arguments with new arguments.


-
void set_arguments(const OutputVector &arguments)
[#](https://docs.openvino.ai#_CPPv4N2ov4Node13set_argumentsERK12OutputVector) Sets/replaces the arguments with new arguments.


-
void set_argument(size_t position, const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)> &argument)[#](https://docs.openvino.ai#_CPPv4N2ov4Node12set_argumentE6size_tRK6OutputI4NodeE) Sets/replaces the arguments with new arguments.


-
void set_output_size(size_t output_size)
[#](https://docs.openvino.ai#_CPPv4N2ov4Node15set_output_sizeE6size_t) Sets the number of outputs.


-
virtual std::string description() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node11descriptionEv) Get the string name for the type of the node, such as

`Add`

or`Multiply`

. The class name, must not contain spaces as it is used for codegen.- Returns:
A const reference to the node’s type name



-
const std::string &get_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node8get_nameEv) Get the unique name of the node.

- Returns:
A const reference to the node’s unique name.



-
void set_friendly_name(const std::string &name)
[#](https://docs.openvino.ai#_CPPv4N2ov4Node17set_friendly_nameERKNSt6stringE) Sets a friendly name for a node. This does not overwrite the unique name of the node and is retrieved via

[get_friendly_name()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node_1a8bef14ca0387b1f71c52339952182be0). Used mainly for debugging. The friendly name may be set exactly once.- Parameters:
**name**– is the friendly name to set


-
const std::string &get_friendly_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node17get_friendly_nameEv) Gets the friendly name for a node. If no friendly name has been set via set_friendly_name then the node’s unique name is returned.

- Returns:
A const reference to the node’s friendly name.



-
virtual std::ostream &write_description(std::ostream &os, uint32_t depth = 0) const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node17write_descriptionERNSt7ostreamE8uint32_t) Writes a description of a node to a stream.

- Parameters:
**os**– The stream; should be returned**depth**– How many levels of inputs to describe

- Returns:
The stream os



-
const std::vector<std::shared_ptr<
[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)>> &get_control_dependencies() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node24get_control_dependenciesEv) Get control dependencies registered on the node.


This node cannot execute until node executes.


Remove the dependency of this node on node.


-
void clear_control_dependencies()
[#](https://docs.openvino.ai#_CPPv4N2ov4Node26clear_control_dependenciesEv) Remove all dependencies from this node.


-
void clear_control_dependents()
[#](https://docs.openvino.ai#_CPPv4N2ov4Node24clear_control_dependentsEv) Remove this node as a dependency from all dependent nodes.


This node absorbs the control dependencies of source_node.


This node becomes a dependent of every node dependent on source_node.


This node’s control dependencies are replaced by replacement.


-
size_t get_output_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node15get_output_sizeEv) Returns the number of outputs from the node.


-
const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&get_output_element_type(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node23get_output_element_typeE6size_t) Returns the element type for output i.


-
const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&get_element_type() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node16get_element_typeEv) Checks that there is exactly one output and returns its element type.


-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&get_output_partial_shape(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node24get_output_partial_shapeE6size_t) Returns the partial shape for output i.


-
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputIK4NodeEE)<const[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)> get_default_output() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node18get_default_outputEv) Return the output to use when converting to an

[Output<Node>](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output_3_01_node_01_4)with no index specified. Throws when not supported.

-
virtual size_t get_default_output_index() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node24get_default_output_indexEv) Returns the output of the default output, or throws if there is none.


-
size_t no_default_index() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node16no_default_indexEv) Throws no default.


-
[descriptor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov10descriptorE)::[Tensor](https://docs.openvino.ai/classov_1_1descriptor_1_1_tensor.html#_CPPv4N2ov10descriptor6TensorE)&get_output_tensor(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node17get_output_tensorE6size_t) Returns the tensor for output or input i.


-
size_t get_input_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node14get_input_sizeEv) Returns the number of inputs for the op.


-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&get_input_partial_shape(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node23get_input_partial_shapeE6size_t) Returns the partial shape of input i.


True if this and node have one output with same element type and shape.


-
NodeVector get_users(bool check_is_used = false) const
[#](https://docs.openvino.ai#_CPPv4NK2ov4Node9get_usersEb) Get all the nodes that uses the current node.


-
inline bool operator<(const
[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)&other) const[#](https://docs.openvino.ai#_CPPv4NK2ov4NodeltERK4Node) Use instance ids for comparison instead of memory addresses to improve determinism.


-
std::vector<
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputI4NodeEE)<[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)>> inputs()[#](https://docs.openvino.ai#_CPPv4N2ov4Node6inputsEv) - Returns:
A vector containing a handle for each of this node’s inputs, in order.



-
std::vector<
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputIK4NodeEE)<const[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)>> inputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node6inputsEv) - Returns:
A vector containing a handle for each of this node’s inputs, in order.



-
std::vector<
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)>> input_values() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node12input_valuesEv) - Returns:
A vector containing the values for each input



-
std::vector<
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)>> outputs()[#](https://docs.openvino.ai#_CPPv4N2ov4Node7outputsEv) - Returns:
A vector containing a handle for each of this node’s outputs, in order.



-
std::vector<
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputIK4NodeEE)<const[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)>> outputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node7outputsEv) - Returns:
A vector containing a handle for each of this node’s outputs, in order.



-
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputI4NodeEE)<[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)> input(size_t input_index)[#](https://docs.openvino.ai#_CPPv4N2ov4Node5inputE6size_t) - Throws:
std::out_of_range – if the node does not have at least

`input_index+1`

inputs.- Returns:
A handle to the

`input_index`

th input of this node.


-
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputIK4NodeEE)<const[Node](https://docs.openvino.ai#_CPPv4N2ov4NodeE)> input(size_t input_index) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node5inputE6size_t) - Throws:
std::out_of_range – if the node does not have at least

`input_index+1`

inputs.- Returns:
A handle to the

`input_index`

th input of this node.


-
virtual void validate_and_infer_types()