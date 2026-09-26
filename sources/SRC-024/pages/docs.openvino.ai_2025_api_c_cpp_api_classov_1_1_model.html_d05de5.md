source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_model.html
lastmod: 

# Class ov::Model[#](https://docs.openvino.ai#class-ov-model)

-
class Model : public std::enable_shared_from_this<
[Model](https://docs.openvino.ai#_CPPv4N2ov5ModelE)>[#](https://docs.openvino.ai#_CPPv4N2ov5ModelE) A user-defined model.

Public Functions

-
explicit Model(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::OutputVector &results, const std::string &name = "")[#](https://docs.openvino.ai#_CPPv4N2ov5Model5ModelERKN2ov12OutputVectorERKNSt6stringE) Constructs a

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model). Lists of parameters and variables will be generated automatically based on traversing the graph from the results.

-
Model(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::OutputVector &results, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::SinkVector &sinks, const std::string &name = "")[#](https://docs.openvino.ai#_CPPv4N2ov5Model5ModelERKN2ov12OutputVectorERKN2ov10SinkVectorERKNSt6stringE) Constructs a

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model). Lists of parameters and variables will be generated automatically based on traversing the graph from the results and the sinks.

-
const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&get_output_element_type(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov5Model23get_output_element_typeE6size_t) Return the element type of output i.


-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&get_output_partial_shape(size_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov5Model24get_output_partial_shapeE6size_t) Return the partial shape of element i.


-
const std::string &get_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5Model8get_nameEv) Get the unique name of the model.

- Returns:
A const reference to the model’s unique name.



-
void set_friendly_name(const std::string &name)
[#](https://docs.openvino.ai#_CPPv4N2ov5Model17set_friendly_nameERKNSt6stringE) Sets a friendly name for a model. This does not overwrite the unique name of the model and is retrieved via

[get_friendly_name()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model_1a303a2a50536b41cd52c8eae017caf4a8). Used mainly for debugging.- Parameters:
**name**– is the friendly name to set


-
const std::string &get_friendly_name() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5Model17get_friendly_nameEv) Gets the friendly name for a model. If no friendly name has been set via set_friendly_name then the model’s unique name is returned.

- Returns:
A const reference to the model’s friendly name.



-
size_t get_graph_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5Model14get_graph_sizeEv) Returns the sum of the size of all nodes in the graph plus the size of all constant data. This has little value beyond comparing the relative size of graphs and should not be considered the actual memory consumption of a graph.


-
bool is_dynamic() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5Model10is_dynamicEv) Returns true if any of the op’s defined in the model contains partial shape.


Replace the

`parameter_index`

th parameter of the model with`parameter`

.All users of the

`parameter_index`

th parameter are redirected to`parameter`

, and the`parameter_index`

th entry in the model parameter list is replaced with`parameter`

.- Parameters:
**parameter_index**– The index of the parameter to replace.**parameter**– The parameter to substitute for the`parameter_index`

th parameter.



Index for parameter, or -1.


-
int64_t get_result_index(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &value) const[#](https://docs.openvino.ai#_CPPv4NK2ov5Model16get_result_indexERKN2ov6OutputIN2ov4NodeEEE) Return the index of this model’s Result represented by the “value”

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)object. This method returns -1 if an the passed output is not related to the Results of a model.

-
int64_t get_result_index(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &value) const[#](https://docs.openvino.ai#_CPPv4NK2ov5Model16get_result_indexERKN2ov6OutputIKN2ov4NodeEEE) Return the index of this model’s Result represented by the “value”

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)object. This method returns -1 if an the passed output is not related to the Results of a model.

-
bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &output_tensors, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &input_tensors,[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::EvaluationContext &evaluation_context) const[#](https://docs.openvino.ai#_CPPv4NK2ov5Model8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorERN2ov17EvaluationContextE) Evaluate the model on inputs, putting results in outputs.

- Parameters:
**output_tensors**– Tensors for the outputs to compute. One for each result**input_tensors**– Tensors for the inputs. One for each inputs.**evaluation_context**– Storage of additional settings and attributes that can be used when evaluating the model. This additional information can be shared across nodes.



-
bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &output_tensors, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &input_tensors) const[#](https://docs.openvino.ai#_CPPv4NK2ov5Model8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluate the model on inputs, putting results in outputs.

- Parameters:
**output_tensors**– Tensors for the outputs to compute. One for each result**input_tensors**– Tensors for the inputs. One for each inputs.



-
void add_sinks(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::SinkVector &sinks)[#](https://docs.openvino.ai#_CPPv4N2ov5Model9add_sinksERKN2ov10SinkVectorE) Add new sink nodes to the list. Method doesn’t validate graph, it should be done manually after all changes.

- Parameters:
**sinks**– new sink nodes


Delete sink node from the list of sinks. Method doesn’t delete node from graph.

- Parameters:
**sink**– Sink to delete


-
void add_results(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ResultVector &results)[#](https://docs.openvino.ai#_CPPv4N2ov5Model11add_resultsERKN2ov12ResultVectorE) Add new Result nodes to the list. Method doesn’t validate graph, it should be done manually after all changes.

- Parameters:
**results**– new Result nodes


Delete Result node from the list of results. Method will not delete node from graph.

- Parameters:
**result**– Result node to delete


-
void add_parameters(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::ParameterVector ¶ms)[#](https://docs.openvino.ai#_CPPv4N2ov5Model14add_parametersERKN2ov15ParameterVectorE) Add new Parameter nodes to the list.

Method doesn’t change or validate graph, it should be done manually. For example, if you want to replace

`ReadValue`

node by`Parameter`

, you should do the following steps:replace node

`ReadValue`

by`Parameter`

in graphcall add_parameter() to add new input to the list

call graph validation to check correctness of changes


- Parameters:
**params**– new Parameter nodes


Delete Parameter node from the list of parameters. Method will not delete node from graph. You need to replace Parameter with other operation manually. Attention: Indexing of parameters can be changed.

Possible use of method is to replace input by variable. For it the following steps should be done:

`Parameter`

node should be replaced by`ReadValue`

call remove_parameter(param) to remove input from the list

check if any parameter indexes are saved/used somewhere, update it for all inputs because indexes can be changed

call graph validation to check all changes


- Parameters:
**param**– Parameter node to delete


-
void add_variables(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[VariableVector](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4util14VariableVectorE)&variables)[#](https://docs.openvino.ai#_CPPv4N2ov5Model13add_variablesERKN2ov2op4util14VariableVectorE) Add new variables to the list. Method doesn’t validate graph, it should be done manually after all changes.

- Parameters:
**variables**– new variables to add


-
void remove_variable(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[Variable](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_variable.html#_CPPv4N2ov2op4util8VariableE)::Ptr &variable)[#](https://docs.openvino.ai#_CPPv4N2ov5Model15remove_variableERKN2ov2op4util8Variable3PtrE) Delete variable from the list of variables. Method doesn’t delete nodes that used this variable from the graph.

- Parameters:
**variable**– Variable to delete


-
inline const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[VariableVector](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4util14VariableVectorE)&get_variables() const[#](https://docs.openvino.ai#_CPPv4NK2ov5Model13get_variablesEv) Return a list of model’s variables.


-
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[Variable](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_variable.html#_CPPv4N2ov2op4util8VariableE)::Ptr get_variable_by_id(const std::string &variable_id) const[#](https://docs.openvino.ai#_CPPv4NK2ov5Model18get_variable_by_idERKNSt6stringE) Return a variable by specified variable_id.


-
inline RTMap &get_rt_info()
[#](https://docs.openvino.ai#_CPPv4N2ov5Model11get_rt_infoEv) Returns a runtime info.

- Returns:
reference to ov::AnyMap with runtime info



-
inline const RTMap &get_rt_info() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5Model11get_rt_infoEv) Returns a constant runtime info.

- Returns:
reference to const ov::AnyMap with runtime info



-
template<class T, class ...Args>

inline const[T](https://docs.openvino.ai#_CPPv4I0DpENK2ov5Model11get_rt_infoERK1TDp4Args)&get_rt_info([Args](https://docs.openvino.ai#_CPPv4I0DpENK2ov5Model11get_rt_infoERK1TDp4Args)... args) const[#](https://docs.openvino.ai#_CPPv4I0DpENK2ov5Model11get_rt_infoERK1TDp4Args) Returns a runtime attribute for the path, throws an

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if path doesn’t exist.- Template Parameters:
**T**– the type of returned value**Args**– types of variadic arguments

- Parameters:
**args**– path to the runtime attribute- Returns:
constant reference to value from runtime info



-
template<class T>

inline const[T](https://docs.openvino.ai#_CPPv4I0ENK2ov5Model11get_rt_infoERK1TRKNSt6vectorINSt6stringEEE)&get_rt_info(const std::vector<std::string> &args) const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov5Model11get_rt_infoERK1TRKNSt6vectorINSt6stringEEE) Returns a runtime attribute for the path, throws an

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if path doesn’t exist.- Template Parameters:
**T**– the type of returned value- Parameters:
**args**– vector with path to the runtime attribute- Returns:
constant reference to value from runtime info



-
template<class ...Args>

inline bool has_rt_info([Args](https://docs.openvino.ai#_CPPv4IDpENK2ov5Model11has_rt_infoEbDp4Args)... args) const[#](https://docs.openvino.ai#_CPPv4IDpENK2ov5Model11has_rt_infoEbDp4Args) Checks if given path exists in runtime info.

- Template Parameters:
**Args**– types of variadic arguments- Parameters:
**args**– path to the runtime attribute- Returns:
true if path exists, otherwise false



-
bool has_rt_info(const std::vector<std::string> &args) const
[#](https://docs.openvino.ai#_CPPv4NK2ov5Model11has_rt_infoERKNSt6vectorINSt6stringEEE) Checks if given path exists in runtime info.

- Parameters:
**args**– vector with path to the runtime attribute- Returns:
true if path exists, otherwise false



-
explicit Model(const