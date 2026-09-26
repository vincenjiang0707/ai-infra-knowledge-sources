source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1frontend_1_1_input_model.html
lastmod: 

# Class ov::frontend::InputModel[#](https://docs.openvino.ai#class-ov-frontend-inputmodel)

-
class InputModel
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModelE) [InputModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_input_model)class represents an original, not yet converted model graph in a framework format given services to find places of interest in a graph or specialize/edit the model before conversion.Editing requests may affect ability to convert the original model to OV

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model). Aim to provide these editing capabilities is to unlock conversion for models that are not natively supported “as-is” because of undefined shapes, types or operations.Specific front-end implementation is supposed to have a lazy implementation for all methods, not doing a complete load of a model without an explicit method call. For example, the list of all inputs are not pre-fetched by

[InputModel](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_input_model)derived class instance creation, but only when get_inputs method is called. But it is not an obligation, the most convenient way should be chosen depending on the framework model representation.All editing requests affect the model representation that is held behind the scene successive method calls observe a new graph structure.

Note

Class methods are divided into several groups: searching for places, naming and annotation, topology editing, setting tensor properties.

Public Functions

-
virtual std::vector<
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr> get_inputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend10InputModel10get_inputsEv) Returns all inputs for a model An input is a place in a graph where data is supposed to flow inside graph from outside. It can be a tensor, port, operation; which kind of place can be an output is FW dependent. Usually framework models have a dedicated artifact to code model input, it can be a tensor without producer, that writes to it in ONNX, or a special operation like Placeholder in TensorFlow.

- Returns:
A vector of input place references



-
virtual std::vector<
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr> get_outputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend10InputModel11get_outputsEv) Returns all output for a model An output is a terminal place in a graph where data escapes the flow. It can be a tensor, port, operation; which kind of place can be an output is FW dependent. In comparison to a graph input, the output is less formally defined thing and determination of initial list of outputs may include some conventions defined by a frontend itself, not a framework. For example, all output ports without consumers may be considered as outputs.

- Returns:
A vector of output place references



-
virtual
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr get_place_by_tensor_name(const std::string &tensor_name) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend10InputModel24get_place_by_tensor_nameERKNSt6stringE) Returns a tensor place by a tensor name following framework conventions, or nullptr if a tensor with this name doesn’t exist.

- Parameters:
**tensor_name**– Name of tensor- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)place corresponding to specified tensor name or nullptr if not exists


-
virtual
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr get_place_by_input_index(size_t input_idx) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend10InputModel24get_place_by_input_indexE6size_t) Returns a tensor place by an input index.

- Parameters:
**input_idx**– Index of model input- Returns:
[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)place corresponding to specified input index or nullptr


-
virtual
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr get_place_by_operation_name(const std::string &operation_name) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend10InputModel27get_place_by_operation_nameERKNSt6stringE) Returns an operation place by an operation name following framework conventions, or nullptr if an operation with this name doesn’t exist.

- Parameters:
**operation_name**– Name of operation- Returns:
[Place](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_place)representing operation or nullptr if not exists


-
virtual
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr get_place_by_operation_name_and_input_port(const std::string &operation_name, int input_port_index)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel42get_place_by_operation_name_and_input_portERKNSt6stringEi) Returns an input port place by operation name and appropriate port index.

- Parameters:
**operation_name**– Name of operation**input_port_index**– Index of input port for this operation

- Returns:
[Place](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_place)representing input port of operation or nullptr if not exists


-
virtual
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr get_place_by_operation_name_and_output_port(const std::string &operation_name, int output_port_index)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel43get_place_by_operation_name_and_output_portERKNSt6stringEi) Returns an output port place by operation name and appropriate port index.

- Parameters:
**operation_name**– Name of operation**output_port_index**– Index of output port for this operation

- Returns:
[Place](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_place)representing output port of operation or nullptr if not exists


-
virtual void set_name_for_tensor(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &tensor, const std::string &new_name)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel19set_name_for_tensorERKN5Place3PtrERKNSt6stringE) Sets name for tensor. Overwrites existing names of this place.

- Parameters:
**tensor**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)place**new_name**– New name for this tensor



-
virtual void add_name_for_tensor(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &tensor, const std::string &new_name)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel19add_name_for_tensorERKN5Place3PtrERKNSt6stringE) Adds new name for tensor.

- Parameters:
**tensor**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)place**new_name**– New name to be added to this place



-
virtual void set_name_for_operation(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &operation, const std::string &new_name)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel22set_name_for_operationERKN5Place3PtrERKNSt6stringE) Sets name for operation. Overwrites existing names of this place.

- Parameters:
**operation**– Operation place**new_name**– New name for this operation



-
virtual void free_name_for_tensor(const std::string &name)
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel20free_name_for_tensorERKNSt6stringE) Unassign specified name from tensor place(s)

- Parameters:
**name**– Name of tensor


-
virtual void free_name_for_operation(const std::string &name)
[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel23free_name_for_operationERKNSt6stringE) Unassign specified name from operation place(s)

- Parameters:
**name**– Name of operation


-
virtual void set_name_for_dimension(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place, size_t shape_dim_index, const std::string &dim_name)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel22set_name_for_dimensionERKN5Place3PtrE6size_tRKNSt6stringE) Set name for a particular dimension of a place (e.g. batch dimension)


-
virtual void cut_and_add_new_input(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place, const std::string &new_name_optional = "")[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel21cut_and_add_new_inputERKN5Place3PtrERKNSt6stringE) Cut immediately before this place and assign this place as new input; prune all nodes that don’t contribute to any output.

- Parameters:
**place**– New place to be assigned as input**new_name_optional**– Optional new name assigned to this input place



-
virtual void cut_and_add_new_output(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place, const std::string &new_name_optional = "")[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel22cut_and_add_new_outputERKN5Place3PtrERKNSt6stringE) Cut immediately after this place and assign this place as new output; prune all nodes that don’t contribute to any output.

- Parameters:
**place**– New place to be assigned as output**new_name_optional**– Optional new name assigned to this output place



-
virtual
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr add_output(const[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel10add_outputERKN5Place3PtrE) Assign this place as new output or add necessary nodes to represent a new output.

- Parameters:
**place**– Anchor point to add an output- Returns:
new output place, may be the same as a given place



-
virtual void remove_output(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel13remove_outputERKN5Place3PtrE) Removes any sinks directly attached to this place with all inbound data flow if it is not required by any other output.

- Parameters:
**place**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)place


-
virtual void override_all_outputs(const std::vector<
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr> &outputs)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel20override_all_outputsERKNSt6vectorIN5Place3PtrEEE) Replaces all existing outputs with new ones removing all data flow that is not required for new outputs.

- Parameters:
**outputs**– Vector with places that will become new outputs; may intersect existing outputs.**outputs**– Array of new output places



-
virtual void override_all_inputs(const std::vector<
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr> &inputs)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel19override_all_inputsERKNSt6vectorIN5Place3PtrEEE) Modifies the graph to use new inputs instead of existing ones. New inputs should completely satisfy all existing outputs.

- Parameters:
**inputs**– Array of new input places


-
virtual void extract_subgraph(const std::vector<
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr> &inputs, const std::vector<[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr> &outputs)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel16extract_subgraphERKNSt6vectorIN5Place3PtrEEERKNSt6vectorIN5Place3PtrEEE) Leaves only subgraph that are defined by new inputs and new outputs.

- Parameters:
**inputs**– Array of new input places**outputs**– Array of new output places



-
virtual void set_partial_shape(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&shape)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel17set_partial_shapeERKN5Place3PtrERKN2ov12PartialShapeE) Defines all possible shape that may be used for this place; place should be uniquely refer to some data. This partial shape will be converted to corresponding shape of results OV nodes and will define shape inference when the model is converted to OV.

- Parameters:
**place**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)place**shape**– Partial shape for this place



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)get_partial_shape(const[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend10InputModel17get_partial_shapeERKN5Place3PtrE) Returns current partial shape used for this place.

- Parameters:
**place**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)place- Returns:
Partial shape for this place



-
virtual void set_element_type(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel16set_element_typeERKN5Place3PtrERKN2ov7element4TypeE) Sets new element type for a place.

- Parameters:
**place**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)place**type**– New element type



-
virtual
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)get_element_type(const[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place) const[#](https://docs.openvino.ai#_CPPv4NK2ov8frontend10InputModel16get_element_typeERKN5Place3PtrE) Returns current element type used for this place.

- Parameters:
**place**–[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)place- Returns:
Element type for this place



-
virtual void set_tensor_value(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place, const void *value)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel16set_tensor_valueERKN5Place3PtrEPKv) Freezes a tensor with statically defined value or replace existing value for already constant node or tensor.

- Parameters:
**place**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)place**value**– Value for tensor place representing a memory buffer



-
virtual void set_tensor_partial_value(const
[Place](https://docs.openvino.ai/classov_1_1frontend_1_1_place.html#_CPPv4N2ov8frontend5PlaceE)::Ptr &place, const void *min_value, const void *max_value)[#](https://docs.openvino.ai#_CPPv4N2ov8frontend10InputModel24set_tensor_partial_valueERKN5Place3PtrEPKvPKv) Defines partial value (lower bound and upper bound) for a tensor place TODO: more details for min_value and max_value format; who defines shape?

- Parameters:
**place**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)place**min_value**– Lower bound of partial value for tensor place**max_value**– Upper bound of partial value for tensor place



-
virtual std::vector<