source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__model__cpp__api.html
lastmod: 

# Group Basics[#](https://docs.openvino.ai#group-basics)

-
*group*Basics OpenVINO Core C++ API to work with

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model), dynamic and static shapes, typesFunctions

-
template<typename ForwardIt>

size_t shape_size([ForwardIt](https://docs.openvino.ai#_CPPv4I0E10shape_size6size_t9ForwardItK9ForwardIt)start_dim, const[ForwardIt](https://docs.openvino.ai#_CPPv4I0E10shape_size6size_t9ForwardItK9ForwardIt)end_dim)[#](https://docs.openvino.ai#_CPPv4I0E10shape_size6size_t9ForwardItK9ForwardIt) Number of elements in a subset of dimensions of a shape. Returns a product of dimensions in a range [start_dim;end_dim)


-
template<typename SHAPE_TYPE>

size_t shape_size(const[SHAPE_TYPE](https://docs.openvino.ai#_CPPv4I0E10shape_size6size_tRK10SHAPE_TYPE)&shape)[#](https://docs.openvino.ai#_CPPv4I0E10shape_size6size_tRK10SHAPE_TYPE) Number of elements in spanned by a shape.


-
class Dimension
[#](https://docs.openvino.ai#_CPPv4N2ov9DimensionE) *#include <dimension.hpp>*Class representing a dimension, which may be dynamic (undetermined until runtime), in a shape or shape-like object.

Static dimensions may be implicitly converted from value_type. A dynamic dimension is constructed with

[Dimension()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension_1ac302bc8b5a833366709b842a1d992c88)or[Dimension::dynamic()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension_1ae20d6e04468016921fc572308c712a20).Public Functions

-
Dimension(value_type dimension)
[#](https://docs.openvino.ai#_CPPv4N2ov9Dimension9DimensionE10value_type) Construct a static dimension.

- Parameters:
**dimension**– Value of the dimension.


-
Dimension(value_type min_dimension, value_type max_dimension)
[#](https://docs.openvino.ai#_CPPv4N2ov9Dimension9DimensionE10value_type10value_type) Construct a dynamic dimension with bounded range.

- Parameters:
**min_dimension**– The lower inclusive limit for the dimension**max_dimension**– The upper inclusive limit for the dimension



-
Dimension(const std::string &str)
[#](https://docs.openvino.ai#_CPPv4N2ov9Dimension9DimensionERKNSt6stringE) Construct a dimension from string.

- Parameters:
**str**– String to parse to dimension.


-
Dimension() = default
[#](https://docs.openvino.ai#_CPPv4N2ov9Dimension9DimensionEv) Construct a dynamic dimension with range [0, …].


-
inline bool is_static() const
[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension9is_staticEv) Check whether this dimension is static.

- Returns:
`true`

if the dimension is static, else`false`

.


-
inline bool is_dynamic() const
[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension10is_dynamicEv) Check whether this dimension is dynamic.

- Returns:
`false`

if the dimension is static, else`true`

.


-
value_type get_length() const
[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension10get_lengthEv) Convert this dimension to

`value_type`

. This dimension must be static and non-negative.- Throws:
std::invalid_argument – If this dimension is dynamic or negative.



-
bool same_scheme(const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&dim) const[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension11same_schemeERK9Dimension) Check whether this dimension represents the same scheme as the argument (both dynamic, or equal).

- Parameters:
**dim**– The other dimension to compare this dimension to.- Returns:
`true`

if this dimension and`dim`

are both dynamic, or if they are both static and equal; otherwise,`false`

.


-
bool compatible(const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&d) const[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension10compatibleERK9Dimension) Check whether this dimension is capable of being merged with the argument dimension.

Two dimensions are considered compatible if it is possible to merge them. (See

[Dimension::merge](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension_1aef570cc1ebefa3e2b63fe91e4a600e5d).)- Parameters:
**d**– The dimension to compare this dimension with.- Returns:
`true`

if this dimension is compatible with`d`

, else`false`

.


-
bool relaxes(const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&d) const[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension7relaxesERK9Dimension) Check whether this dimension is a relaxation of the argument.

A dimension

`d1`

*relaxes*(or*is a relaxation of*)`d2`

if`d1`

and`d2`

are static and equal, or`d1`

is dynamic.`d1.relaxes(d2)`

is equivalent to`d2.refines(d1)`

.- Parameters:
**d**– The dimension to compare this dimension with.- Returns:
`true`

if this dimension relaxes`d`

, else`false`

.


-
bool refines(const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&d) const[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension7refinesERK9Dimension) Check whether this dimension is a refinement of the argument.

A dimension

`d2`

*refines*(or*is a refinement of*)`d1`

if`d1`

and`d2`

are static and equal, or`d2`

is dynamic.`d1.refines(d2)`

is equivalent to`d2.relaxes(d1)`

.- Parameters:
**d**– The dimension to compare this dimension with.- Returns:
`true`

if this dimension relaxes`d`

, else`false`

.


-
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)operator+(const[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&dim) const[#](https://docs.openvino.ai#_CPPv4NK2ov9DimensionplERK9Dimension) Addition operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for addition.- Returns:
Smallest interval dimension enclosing inputs



-
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)operator-(const[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&dim) const[#](https://docs.openvino.ai#_CPPv4NK2ov9DimensionmiERK9Dimension) Subtraction operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for subtraction.- Returns:
Smallest interval dimension enclosing inputs



-
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)operator/(const value_type divisor) const[#](https://docs.openvino.ai#_CPPv4NK2ov9DimensiondvEK10value_type) Division operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)divided by a value_type parameter.- Parameters:
**divisor**– Right operand for division.- Returns:
Smallest interval dimension enclosing inputs



-
inline
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&operator/=(const value_type divisor)[#](https://docs.openvino.ai#_CPPv4N2ov9DimensiondVEK10value_type) Divided-into operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**divisor**– Right operand for multiplication.- Returns:
A reference to

`*this`

, after updating`*this`

to the value`*this * dim`

.


-
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)operator*(const[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&dim) const[#](https://docs.openvino.ai#_CPPv4NK2ov9DimensionmlERK9Dimension) Multiplication operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for multiplicaiton.- Returns:
Smallest interval containing all “produces” which are 0 if either of

`this`

or`dim`

has length`0`

, else unbounded if either is unbounded, else product of lengths.


-
inline
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&operator+=(const[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&dim)[#](https://docs.openvino.ai#_CPPv4N2ov9DimensionpLERK9Dimension) Add-into operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for addition.- Returns:
A reference to

`*this`

, after updating`*this`

to the value`*this + dim`

.


-
inline
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&operator*=(const[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&dim)[#](https://docs.openvino.ai#_CPPv4N2ov9DimensionmLERK9Dimension) Multiply-into operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for multiplication.- Returns:
A reference to

`*this`

, after updating`*this`

to the value`*this * dim`

.


Sets symbol of the

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).

Public Static Functions

-
static bool merge(
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&dst, const[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&d1, const[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&d2)[#](https://docs.openvino.ai#_CPPv4N2ov9Dimension5mergeER9DimensionRK9DimensionRK9Dimension) Try to merge two

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)objects together.If

`d1`

is dynamic, writes`d2`

to`dst`

and returns`true`

.If

`d2`

is dynamic, writes`d1`

to`dst`

and returns`true`

.If

`d1`

and`d2`

are static and equal, writes`d1`

to`dst`

and returns`true`

.If

`d1`

and`d2`

are both static and unequal, leaves`dst`

unchanged and returns`false`

.

- Parameters:
**dst**–**[out]**Reference to write the merged[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)into.**d1**– First dimension to merge.**d2**– Second dimension to merge.

- Returns:
`true`

if merging succeeds, else`false`

.


-
Dimension(value_type dimension)

-
class Extension
[#](https://docs.openvino.ai#_CPPv4N2ov9ExtensionE) *#include <extension.hpp>*The class provides the base interface for OpenVINO extensions.

Subclassed by

[ov::BaseOpExtension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_base_op_extension),[ov::frontend::ConversionExtensionBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_conversion_extension_base),[ov::frontend::DecoderTransformationExtension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_decoder_transformation_extension),[ov::frontend::ProgressReporterExtension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_progress_reporter_extension),[ov::frontend::TelemetryExtension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1frontend_1_1_telemetry_extension)

-
class Model : public std::enable_shared_from_this<
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)>[#](https://docs.openvino.ai#_CPPv4N2ov5ModelE) *#include <model.hpp>*A user-defined model.

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

inline const[T](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4I0DpENK2ov5Model11get_rt_infoERK1TDp4Args)&get_rt_info([Args](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4I0DpENK2ov5Model11get_rt_infoERK1TDp4Args)... args) const[#](https://docs.openvino.ai#_CPPv4I0DpENK2ov5Model11get_rt_infoERK1TDp4Args) Returns a runtime attribute for the path, throws an

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if path doesn’t exist.- Template Parameters:
**T**– the type of returned value**Args**– types of variadic arguments

- Parameters:
**args**– path to the runtime attribute- Returns:
constant reference to value from runtime info



-
template<class T>

inline const[T](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4I0ENK2ov5Model11get_rt_infoERK1TRKNSt6vectorINSt6stringEEE)&get_rt_info(const std::vector<std::string> &args) const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov5Model11get_rt_infoERK1TRKNSt6vectorINSt6stringEEE) Returns a runtime attribute for the path, throws an

[ov::Exception](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_exception)if path doesn’t exist.- Template Parameters:
**T**– the type of returned value- Parameters:
**args**– vector with path to the runtime attribute- Returns:
constant reference to value from runtime info



-
template<class ...Args>

inline bool has_rt_info([Args](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4IDpENK2ov5Model11has_rt_infoEbDp4Args)... args) const[#](https://docs.openvino.ai#_CPPv4IDpENK2ov5Model11has_rt_infoEbDp4Args) Checks if given path exists in runtime info.

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

-
class Node : public std::enable_shared_from_this<
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>[#](https://docs.openvino.ai#_CPPv4N2ov4NodeE) *#include <node.hpp>*Nodes are the backbone of the graph of Value dataflow. Every node has zero or more nodes as arguments and one value, which is either a tensor or a (possibly empty) tuple of values.

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
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &argument)[#](https://docs.openvino.ai#_CPPv4N2ov4Node12set_argumentE6size_tRK6OutputI4NodeE) Sets/replaces the arguments with new arguments.


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
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> &get_control_dependencies() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node24get_control_dependenciesEv) Get control dependencies registered on the node.


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
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputIK4NodeEE)<const[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_default_output() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node18get_default_outputEv) Return the output to use when converting to an

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
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)&other) const[#](https://docs.openvino.ai#_CPPv4NK2ov4NodeltERK4Node) Use instance ids for comparison instead of memory addresses to improve determinism.


-
std::vector<
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> inputs()[#](https://docs.openvino.ai#_CPPv4N2ov4Node6inputsEv) - Returns:
A vector containing a handle for each of this node’s inputs, in order.



-
std::vector<
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputIK4NodeEE)<const[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> inputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node6inputsEv) - Returns:
A vector containing a handle for each of this node’s inputs, in order.



-
std::vector<
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> input_values() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node12input_valuesEv) - Returns:
A vector containing the values for each input



-
std::vector<
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> outputs()[#](https://docs.openvino.ai#_CPPv4N2ov4Node7outputsEv) - Returns:
A vector containing a handle for each of this node’s outputs, in order.



-
std::vector<
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputIK4NodeEE)<const[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> outputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node7outputsEv) - Returns:
A vector containing a handle for each of this node’s outputs, in order.



-
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> input(size_t input_index)[#](https://docs.openvino.ai#_CPPv4N2ov4Node5inputE6size_t) - Throws:
std::out_of_range – if the node does not have at least

`input_index+1`

inputs.- Returns:
A handle to the

`input_index`

th input of this node.


-
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputIK4NodeEE)<const[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> input(size_t input_index) const[#](https://docs.openvino.ai#_CPPv4NK2ov4Node5inputE6size_t) - Throws:
std::out_of_range – if the node does not have at least

`input_index+1`

inputs.- Returns:
A handle to the

`input_index`

th input of this node.


-
virtual void validate_and_infer_types()

-
template<>

class Input<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>[#](https://docs.openvino.ai#_CPPv4IEN2ov5InputI4NodeEE) *#include <node_input.hpp>*A handle for one of a node’s inputs.

Public Functions

-
Input(
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*node, size_t index)[#](https://docs.openvino.ai#_CPPv4N2ov5InputI4NodeE5InputEP4Node6size_t) Constructs a

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input).- Parameters:
**node**– Pointer to the node for the input handle.**index**– The index of the input.



-
size_t get_index() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5InputI4NodeE9get_indexEv) - Returns:
The index of the input referred to by this input handle.



- OV_NO_DANGLING const element::Type & get_element_type () const
- Returns:
The element type of the input referred to by this input handle.



- OV_NO_DANGLING const Shape & get_shape () const
- Returns:
The shape of the input referred to by this input handle.



- OV_NO_DANGLING const PartialShape & get_partial_shape () const
- Returns:
The partial shape of the input referred to by this input handle.



-
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_source_output() const[#](https://docs.openvino.ai#_CPPv4NK2ov5InputI4NodeE17get_source_outputEv) - Returns:
A handle to the output that is connected to this input.



- OV_NO_DANGLING descriptor::Tensor & get_tensor () const
- Returns:
A reference to the tensor descriptor for this input.



-
std::shared_ptr<
[descriptor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov10descriptorE)::[Tensor](https://docs.openvino.ai/classov_1_1descriptor_1_1_tensor.html#_CPPv4N2ov10descriptor6TensorE)> get_tensor_ptr() const[#](https://docs.openvino.ai#_CPPv4NK2ov5InputI4NodeE14get_tensor_ptrEv) - Returns:
A shared pointer to the tensor descriptor for this input.



-
bool get_is_relevant_to_shapes() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5InputI4NodeE25get_is_relevant_to_shapesEv) - Returns:
true if this input is relevant to its node’s output shapes; else false.



-
bool get_is_relevant_to_values() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5InputI4NodeE25get_is_relevant_to_valuesEv) - Returns:
true if this input is relevant to its node’s output values; else false.



-
void replace_source_output(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &new_source_output) const[#](https://docs.openvino.ai#_CPPv4NK2ov5InputI4NodeE21replace_source_outputERK6OutputI4NodeE) Replaces the source output of this input.

- Parameters:
**new_source_output**– A handle for the output that will replace this input’s source.


-
RTMap &get_rt_info()
[#](https://docs.openvino.ai#_CPPv4N2ov5InputI4NodeE11get_rt_infoEv) - Returns:
The reference to runtime info map



- OV_NO_DANGLING const RTMap & get_rt_info () const
- Returns:
The constant reference to runtime info map



-
Input(

-
template<>

class Input<const[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>[#](https://docs.openvino.ai#_CPPv4IEN2ov5InputIK4NodeEE) *#include <node_input.hpp>*A handle for one of a node’s inputs.

Public Functions

-
Input(const
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*node, size_t index)[#](https://docs.openvino.ai#_CPPv4N2ov5InputIK4NodeE5InputEPK4Node6size_t) Constructs a

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input).- Parameters:
**node**– Pointer to the node for the input handle.**index**– The index of the input.



-
size_t get_index() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5InputIK4NodeE9get_indexEv) - Returns:
The index of the input referred to by this input handle.



- OV_NO_DANGLING const element::Type & get_element_type () const
- Returns:
The element type of the input referred to by this input handle.



- OV_NO_DANGLING const Shape & get_shape () const
- Returns:
The shape of the input referred to by this input handle.



- OV_NO_DANGLING const PartialShape & get_partial_shape () const
- Returns:
The partial shape of the input referred to by this input handle.



-
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_source_output() const[#](https://docs.openvino.ai#_CPPv4NK2ov5InputIK4NodeE17get_source_outputEv) - Returns:
A handle to the output that is connected to this input.



- OV_NO_DANGLING descriptor::Tensor & get_tensor () const
- Returns:
A reference to the tensor descriptor for this input.



-
std::shared_ptr<
[descriptor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov10descriptorE)::[Tensor](https://docs.openvino.ai/classov_1_1descriptor_1_1_tensor.html#_CPPv4N2ov10descriptor6TensorE)> get_tensor_ptr() const[#](https://docs.openvino.ai#_CPPv4NK2ov5InputIK4NodeE14get_tensor_ptrEv) - Returns:
A shared pointer to the tensor descriptor for this input.



-
bool get_is_relevant_to_shapes() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5InputIK4NodeE25get_is_relevant_to_shapesEv) - Returns:
true if this input is relevant to its node’s output shapes; else false.



-
bool get_is_relevant_to_values() const
[#](https://docs.openvino.ai#_CPPv4NK2ov5InputIK4NodeE25get_is_relevant_to_valuesEv) - Returns:
true if this input is relevant to its node’s output values; else false.



- OV_NO_DANGLING const RTMap & get_rt_info () const
- Returns:
The constant reference to runtime info map



-
Input(const

-
template<>

class Output<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>[#](https://docs.openvino.ai#_CPPv4IEN2ov6OutputI4NodeEE) *#include <node_output.hpp>*A handle for one of a node’s outputs.

Public Functions

-
Output(
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*node, size_t index)[#](https://docs.openvino.ai#_CPPv4N2ov6OutputI4NodeE6OutputEP4Node6size_t) Constructs a

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output).- Parameters:
**node**– A pointer to the node for the output handle.**index**– The index of the output.



Constructs a

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output).- Parameters:
**node**– A`shared_ptr`

to the node for the output handle.**index**– The index of the output.



Constructs a

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output), referencing the default output of the node. If the node doesn’t have a default output, an exception will be thrown.- Parameters:
**node**– A`shared_ptr`

to the node for the output handle.


-
Output() = default
[#](https://docs.openvino.ai#_CPPv4N2ov6OutputI4NodeE6OutputEv) A null output.


- Returns:
A

`shared_ptr`

to the node referred to by this output handle.


-
size_t get_index() const
[#](https://docs.openvino.ai#_CPPv4NK2ov6OutputI4NodeE9get_indexEv) - Returns:
The index of the output referred to by this output handle.



- OV_NO_DANGLING descriptor::Tensor & get_tensor () const
- Returns:
A reference to the tensor descriptor for this output.



-
std::shared_ptr<
[descriptor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov10descriptorE)::[Tensor](https://docs.openvino.ai/classov_1_1descriptor_1_1_tensor.html#_CPPv4N2ov10descriptor6TensorE)> get_tensor_ptr() const[#](https://docs.openvino.ai#_CPPv4NK2ov6OutputI4NodeE14get_tensor_ptrEv) - Returns:
A shared point to the tensor ptr for this output.



- Returns:
Set new tensor desc shared pointer to this output



- OV_NO_DANGLING const element::Type & get_element_type () const
- Returns:
The element type of the output referred to by this output handle.



- OV_NO_DANGLING const Shape & get_shape () const
- Returns:
The shape of the output referred to by this output handle.



- OV_NO_DANGLING const PartialShape & get_partial_shape () const
- Returns:
The partial shape of the output referred to by this output handle.



-
RTMap &get_rt_info()
[#](https://docs.openvino.ai#_CPPv4N2ov6OutputI4NodeE11get_rt_infoEv) - Returns:
The reference to runtime info map



- OV_NO_DANGLING const RTMap & get_rt_info () const
- Returns:
The constant reference to runtime info map



- OV_NO_DANGLING const std::unordered_set< std::string > & get_names () const
- Returns:
The tensor names associated with this output



-
void set_names(const std::unordered_set<std::string> &names)
[#](https://docs.openvino.ai#_CPPv4N2ov6OutputI4NodeE9set_namesERKNSt13unordered_setINSt6stringEEE) - Returns:
Set tensor names associated with this output



-
void add_names(const std::unordered_set<std::string> &names)
[#](https://docs.openvino.ai#_CPPv4N2ov6OutputI4NodeE9add_namesERKNSt13unordered_setINSt6stringEEE) - Returns:
Add tensor names associated with this output



-
std::set<
[Input](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov5InputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>> get_target_inputs() const[#](https://docs.openvino.ai#_CPPv4NK2ov6OutputI4NodeE17get_target_inputsEv) - Returns:
A set containing handles for all inputs targeted by the output referenced by this output handle.



-
Output(

-
template<>

class Output<const[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)>[#](https://docs.openvino.ai#_CPPv4IEN2ov6OutputIK4NodeEE) *#include <node_output.hpp>*A handle for one of a node’s outputs.

Public Functions

-
Output(const
[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)*node, size_t index)[#](https://docs.openvino.ai#_CPPv4N2ov6OutputIK4NodeE6OutputEPK4Node6size_t) Constructs a

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output).- Parameters:
**node**– A pointer to the node for the output handle.**index**– The index of the output.



Constructs a

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output).- Parameters:
**node**– A`shared_ptr`

to the node for the output handle.**index**– The index of the output.



Constructs a

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output), referencing the zeroth output of the node.- Parameters:
**node**– A`shared_ptr`

to the node for the output handle.


-
Output() = default
[#](https://docs.openvino.ai#_CPPv4N2ov6OutputIK4NodeE6OutputEv) A null output.


- Returns:
A

`shared_ptr`

to the node referred to by this output handle.


-
size_t get_index() const
[#](https://docs.openvino.ai#_CPPv4NK2ov6OutputIK4NodeE9get_indexEv) - Returns:
The index of the output referred to by this output handle.



- OV_NO_DANGLING descriptor::Tensor & get_tensor () const
- Returns:
A reference to the tensor descriptor for this output.



-
std::shared_ptr<
[descriptor](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov10descriptorE)::[Tensor](https://docs.openvino.ai/classov_1_1descriptor_1_1_tensor.html#_CPPv4N2ov10descriptor6TensorE)> get_tensor_ptr() const[#](https://docs.openvino.ai#_CPPv4NK2ov6OutputIK4NodeE14get_tensor_ptrEv) - Returns:
A shared point to the tensor ptr for this output.



- OV_NO_DANGLING const element::Type & get_element_type () const
- Returns:
The element type of the output referred to by this output handle.



- OV_NO_DANGLING const Shape & get_shape () const
- Returns:
The shape of the output referred to by this output handle.



- OV_NO_DANGLING const PartialShape & get_partial_shape () const
- Returns:
The partial shape of the output referred to by this output handle.



- OV_NO_DANGLING const RTMap & get_rt_info () const
- Returns:
The constant reference to runtime info map



- OV_NO_DANGLING const std::unordered_set< std::string > & get_names () const
- Returns:
The tensor names associated with this output



-
Output(const

-
class PartialShape
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeE) *#include <partial_shape.hpp>*Class representing a shape that may be partially or totally dynamic.

A

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)may have:Dynamic rank. (Informal notation:

`?`

)Static rank, but dynamic dimensions on some or all axes. (Informal notation examples:

`{1,2,?,4}`

,`{?,?,?}`

)Static rank, and static dimensions on all axes. (Informal notation examples:

`{1,2,3,4}`

,`{6}`

,`{}`

)

Public Functions

-
PartialShape(std::initializer_list<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)> init)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeENSt16initializer_listI9DimensionEE) Constructs a shape with static rank from an initializer list of

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).Examples:

PartialShape s{2,3,4}; // rank=3, all dimensions static PartialShape s{}; // rank=0 PartialShape s{2,Dimension::dynamic(),3}; // rank=3, dimension 1 dynamic

- Parameters:
**init**– The[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)values for the constructed shape.


-
PartialShape(std::vector<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)> dimensions)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeENSt6vectorI9DimensionEE) Constructs a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with static rank from a vector of[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dimensions**– The[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)values for the constructed shape.


-
PartialShape(const std::vector<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)::value_type> &dimensions)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeERKNSt6vectorIN9Dimension10value_typeEEE) Constructs a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with static rank from a vector of dimensions values.- Parameters:
**dimensions**– The[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)values for the constructed shape.


-
PartialShape()
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeEv) Constructs a static

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with zero rank (the shape of a scalar).

-
PartialShape(const
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeERK5Shape) Constructs a static

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)from a[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).- Parameters:
**shape**– The[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)to convert into[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).


-
PartialShape(const std::string &shape)
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape12PartialShapeERKNSt6stringE) Constructs a static

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)from a string.- Parameters:
**shape**– The string to parse into[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).


-
bool is_static() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape9is_staticEv) Check if this shape is static.

A shape is considered static if it has static rank, and all dimensions of the shape are static.

- Returns:
`true`

if this shape is static, else`false`

.


-
inline bool is_dynamic() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape10is_dynamicEv) Check if this shape is dynamic.

A shape is considered static if it has static rank, and all dimensions of the shape are static.

- Returns:
`false`

if this shape is static, else`true`

.


-
inline Rank rank() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape4rankEv) Get the rank of the shape.

- Returns:
The rank of the shape. This will be

[Rank::dynamic()](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga65a44781c293f3559c2e037eb29c0f14)if the rank of the shape is dynamic.


-
bool compatible(const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&s) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape10compatibleERK12PartialShape) Check whether this shape is compatible with the argument, i.e., whether it is possible to merge them.

Two shapes are compatible if

one or both of them has dynamic rank, or

both shapes have dynamic and equal rank, and their dimensions are elementwise compatible (see

[Dimension::compatible()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension_1a930fe268cb5c954ac8696c97a974ca5b)).

- Parameters:
**s**– The shape to be checked for compatibility with this shape.- Returns:
`true`

if this shape is compatible with`s`

, else`false`

.


-
bool same_scheme(const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&s) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape11same_schemeERK12PartialShape) Check whether this shape represents the same scheme as the argument.

Two shapes

`s1`

and`s2`

represent the same scheme ifthey both have dynamic rank, or

they both have static and equal rank

`r`

, and for every`i`

from`0`

to`r-1`

,`s1[i]`

represents the same scheme as`s2[i]`

(see[Dimension::same_scheme()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension_1a8a463f7fdc62f36e22317d11b43d9f4c)).

- Parameters:
**s**– The shape whose scheme is being compared with this shape.- Returns:
`true`

if this shape represents the same scheme as`s`

, else`false`

.


-
bool relaxes(const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&s) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape7relaxesERK12PartialShape) Check whether this shape is a relaxation of the argument.

Intuitively, a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s1`

is said to*relax*`s2`

(or*is a relaxation*of`s2`

) if it is “more permissive” than`s2`

. In other words,`s1`

is a relaxation of`s2`

if anything you can form by plugging things into the dynamic dimensions of`s2`

is also something you can form by plugging things into the dynamic dimensions of`s1`

, but not necessarily the other way around.`s1.relaxes(s2)`

is equivalent to`s2.refines(s1)`

.Formally,

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s1`

is said to*relax*[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s2`

if:For every

`i`

from`0`

to`r-1`

, either`s1[i]`

contains s2[i].

- Parameters:
**s**– The shape which is being compared against this shape.- Returns:
`true`

if this shape relaxes`s`

, else`false`

.


-
bool refines(const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&s) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape7refinesERK12PartialShape) Check whether this shape is a refinement of the argument.

Intuitively, a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s1`

is said to*relax*`s2`

(or*is a relaxation*of`s2`

) if it is “less permissive” than`s2`

. In other words,`s1`

is a relaxation of`s2`

if anything you can form by plugging things into the dynamic dimensions of`s1`

is also something you can form by plugging things into the dynamic dimensions of`s2`

, but not necessarily the other way around.`s1.refines(s2)`

is equivalent to`s2.relaxes(s1)`

.Formally,

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s1`

is said to*refine*[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s2`

if:`s2`

has dynamic rank, or`s1`

and`s2`

both have static rank`r`

, and for every`i`

from`0`

to`r-1`

, either`s2[i]`

is dynamic, or`s1[i]`

==`s2[i]`

.

- Parameters:
**s**– The shape which is being compared against this shape.- Returns:
`true`

if this shape refines`s`

, else`false`

.


-
bool merge_rank(const Rank &r)
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape10merge_rankERK4Rank) Checks that this shape’s rank is compatible with

`r`

, and, if this shape’s rank is dynamic and`r`

is static, updates this shape to have a rank of`r`

with dimensions all dynamic.- Returns:
`true`

if this shape’s rank is compatible with`r`

, else`false`

.


-
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)to_shape() const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape8to_shapeEv) Convert a static

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)to a[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).- Throws:
std::invalid_argument – If this

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)is dynamic.- Returns:
A new

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)`s`

where`s[i] = size_t((*this)[i])`

.


-
bool all_non_negative() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape16all_non_negativeEv) Returns

`true`

if all static dimensions of the tensor are non-negative, else`false`

.

-
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&operator[](std::ptrdiff_t i)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShapeixENSt9ptrdiff_tE) Index operator for

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape), with bound checking.- Parameters:
**i**– The index of the dimension being selected in range [-rank, rank).- Returns:
A reference to the

`i`

th[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)of this shape.


-
const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&operator[](std::ptrdiff_t i) const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShapeixENSt9ptrdiff_tE) Index operator for

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape), with bound checking.- Parameters:
**i**– The index of the dimension being selected in range [-rank, rank).- Returns:
A reference to the

`i`

th[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)of this shape.


-
inline explicit operator std::vector<
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)>() const[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShapecvNSt6vectorI9DimensionEEEv) Returns a vector of the dimensions. This has no meaning if dynamic.


-
inline iterator begin() noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape5beginEv) Returns a read/write iterator that points to the first element in the shape. Iteration is done in ordinary element order.


-
inline const_iterator begin() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape5beginEv) Returns a read-only (constant) iterator that points to the first element in the shape. Iteration is done in ordinary element order.


-
inline iterator end() noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape3endEv) Returns a read/write iterator that points one past the last element in the shape. Iteration is done in ordinary element order.


-
inline const_iterator end() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape3endEv) Returns a read-only (constant) iterator that points one past the last element in the shape. Iteration is done in ordinary element order.


-
inline reverse_iterator rbegin() noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape6rbeginEv) Returns a read/write reverse iterator that points to the last element in the shape. Iteration is done in reverse element order.


-
inline const_reverse_iterator rbegin() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape6rbeginEv) Returns a read-only (constant) reverse iterator that points to the last element in the shape. Iteration is done in reverse element order.


-
inline reverse_iterator rend() noexcept
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape4rendEv) Returns a read/write reverse iterator that points to one before the first element in the shape. Iteration is done in reverse element order.


-
inline const_reverse_iterator rend() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape4rendEv) Returns a read-only (constant) reverse iterator that points to one before the first element in the shape. Iteration is done in reverse element order.


-
inline const_iterator cbegin() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape6cbeginEv) Returns a read-only (constant) iterator that points to the first element in the shape. Iteration is done in ordinary element order.


-
inline const_iterator cend() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape4cendEv) Returns a read-only (constant) iterator that points one past the last element in the shape. Iteration is done in ordinary element order.


-
inline const_reverse_iterator crbegin() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape7crbeginEv) Returns a read-only (constant) reverse iterator that points to the last element in the shape. Iteration is done in reverse element order.


-
inline const_reverse_iterator crend() const noexcept
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape5crendEv) Returns a read-only (constant) reverse iterator that points to one before the first element in the shape. Iteration is done in reverse element order.


-
inline void resize(size_t count)
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape6resizeE6size_t) Resizes dimensions container to contain count elements.


-
inline size_t size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape4sizeEv) Returns size of dimension vector. Requires rank to be static.


-
inline iterator insert(iterator position, const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&val)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape6insertE8iteratorRK9Dimension) Returns a read/write iterator that points to the inserted element in the shape.


-
inline void insert(iterator position, size_t n, const
[Dimension](https://docs.openvino.ai/classov_1_1_dimension.html#_CPPv4N2ov9DimensionE)&val)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape6insertE8iterator6size_tRK9Dimension) Inserts count copies of the value before position.


-
template<class InputIterator>

inline void insert(iterator position,[InputIterator](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4I0EN2ov12PartialShape6insertEv8iterator13InputIterator13InputIterator)first,[InputIterator](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4I0EN2ov12PartialShape6insertEv8iterator13InputIterator13InputIterator)last)[#](https://docs.openvino.ai#_CPPv4I0EN2ov12PartialShape6insertEv8iterator13InputIterator13InputIterator) Inserts elements from range [first, last) before position.


-
inline void reserve(size_t n)
[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape7reserveE6size_t) Requests that the dimensions vector capacity be enough to contain n elements.


-
template<class ...Args>

inline void emplace_back([Args](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4IDpEN2ov12PartialShape12emplace_backEvDpRR4Args)&&... args)[#](https://docs.openvino.ai#_CPPv4IDpEN2ov12PartialShape12emplace_backEvDpRR4Args) emplace element to the end of partial shape


-
std::string to_string() const
[#](https://docs.openvino.ai#_CPPv4NK2ov12PartialShape9to_stringEv) String representation of

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape).

Public Static Functions

-
static
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)dynamic(Rank r = Rank::dynamic())[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape7dynamicE4Rank) Construct a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with the given rank and all dimensions (if any) dynamic.- Returns:
A

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)with the given rank, and all dimensions (if any) dynamic.


-
static bool merge_into(
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&dst, const[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&src)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape10merge_intoER12PartialShapeRK12PartialShape) Try to merge one shape into another.

Merges

`src`

into`dst`

, returning`true`

on success and`false`

on failure. If`false`

is returned, the effect on`dst`

is unspecified.To merge two partial shapes

`s1`

and`s2`

is to find the most permissive partial shape`s`

that is no more permissive than`s1`

or`s2`

, if`s`

exists. For example:merge(?,?) -> ? merge(?,{?,?}) -> {?,?} merge({?,?},{?,?}) -> {?,?} merge({1,2,3,4},?) -> {1,2,3,4} merge({1,2},{1,?}) -> {1,2} merge({1,2,?,?},{1,?,3,?}) -> {1,2,3,?} merge({1,2,3},{1,2,3}) -> {1,2,3} merge({1,?},{2,?}) fails [dimension 0 constraints are inconsistent] merge({?,?},{?,?,?}) fails [ranks are inconsistent]

This function (merge_into) performs the “merge” operation described above on

`dst`

and`src`

, but overwrites`dst`

with the result and returns`true`

if merging is successful; if merging is unsuccessful, the function returns`false`

and may make unspecified changes to`dst`

.- Parameters:
**dst**–**[inout]**The shape that`src`

will be merged into.**src**– The shape that will be merged into`dst`

.

- Returns:
`true`

if merging succeeds, else`false`

.


-
static bool broadcast_merge_into(
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&dst, const[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&src, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&autob)[#](https://docs.openvino.ai#_CPPv4N2ov12PartialShape20broadcast_merge_intoER12PartialShapeRK12PartialShapeRKN2ov2op17AutoBroadcastSpecE) Try to merge one shape into another along with implicit broadcasting.


Friends

- friend OPENVINO_API std::ostream & operator<< (std::ostream &str, const PartialShape &shape)
Inserts a human-readable representation of a

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)into an output stream.The output to the stream is in “informal” notation. In other words:

If

`shape`

has dynamic rank, inserts the string`?`

.If

`shape`

has static rank, inserts the string`{`

, then inserts each dimension of`shape`

into the output stream separated by commas, then inserts`}`

.

PartialShape s1{PartialShape::dynamic())}; PartialShape s2{}; PartialShape s3{1,Dimension::dynamic(),2,3}; PartialShape s4{2,3,4}; std::cout << s1 << std::endl << s2 << std::endl << s3 << std::endl << s4 << std::endl;

? {} {1,?,2,3} {2,3,4}

- Parameters:
**str**– The output stream targeted for insertion.**shape**– The shape to be inserted into`str`

.

- Returns:
A reference to

`str`

after insertion.


- friend OPENVINO_API PartialShape operator+ (const PartialShape &s1, const PartialShape &s2)
Elementwise addition of two

[PartialShape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape)objects.If

`s1`

or`s2`

has dynamic rank, returns[PartialShape::dynamic()](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_partial_shape_1a5f8ce4b26f65232d9de8ab4e5e3b375d).If

`s1 and`

s2` both have static rank, and their ranks are unequal, throws std::invalid_argument.If

`s1`

and`s2`

both have static rank, and their ranks are equal, returns a new shape whose`i`

th dimension is`s1[i] + s2[i]`

.

- Parameters:
**s1**– Left operand for addition.**s2**– Right operand for addition.

- Throws:
std::invalid_argument – If

`s1`

and`s2`

have inconsistent ranks.- Returns:
The result of elementwise adding

`s1`

to`s2`

(see description).



-
class PrePostProcessor
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessorE) *#include <pre_post_process.hpp>*Main class for adding pre- and post- processing steps to existing

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).This is a helper class for writing easy pre- and post- processing operations on

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)object assuming that any preprocess operation takes one input and produces one output.For advanced preprocessing scenarios, like combining several functions with multiple inputs/outputs into one, client’s code can use transformation passes over

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)Public Functions

Default constructor.

- Parameters:
**function**– Existing function representing loaded model


-
PrePostProcessor(
[PrePostProcessor](https://docs.openvino.ai/classov_1_1preprocess_1_1_pre_post_processor.html#_CPPv4N2ov10preprocess16PrePostProcessor16PrePostProcessorERR16PrePostProcessor)&&) noexcept[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor16PrePostProcessorERR16PrePostProcessor) Default move constructor.


-
[PrePostProcessor](https://docs.openvino.ai/classov_1_1preprocess_1_1_pre_post_processor.html#_CPPv4N2ov10preprocess16PrePostProcessorE)&operator=([PrePostProcessor](https://docs.openvino.ai/classov_1_1preprocess_1_1_pre_post_processor.html#_CPPv4N2ov10preprocess16PrePostProcessorE)&&) noexcept[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessoraSERR16PrePostProcessor) Default move assignment operator.


-
~PrePostProcessor()
[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessorD0Ev) Default destructor.


-
[InputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_input_info.html#_CPPv4N2ov10preprocess9InputInfoE)&input()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor5inputEv) Gets input pre-processing data structure. Should be used only if model/function has only one input Using returned structure application’s code is able to set user’s tensor data (e.g layout), preprocess steps, target model’s data.

- Returns:
Reference to model’s input information structure



-
[InputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_input_info.html#_CPPv4N2ov10preprocess9InputInfoE)&input(const std::string &tensor_name)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor5inputERKNSt6stringE) Gets input pre-processing data structure for input identified by it’s tensor name.

- Parameters:
**tensor_name**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)name of specific input. Throws if tensor name is not associated with any input in a model- Returns:
Reference to model’s input information structure



-
[InputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_input_info.html#_CPPv4N2ov10preprocess9InputInfoE)&input(size_t input_index)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor5inputE6size_t) Gets input pre-processing data structure for input identified by it’s order in a model.

- Parameters:
**input_index**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)index of specific input. Throws if input index is out of range for associated function- Returns:
Reference to model’s input information structure



-
[OutputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_output_info.html#_CPPv4N2ov10preprocess10OutputInfoE)&output()[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor6outputEv) Gets output post-processing data structure. Should be used only if model/function has only one output Using returned structure application’s code is able to set model’s output data, post-process steps, user’s tensor data (e.g layout)

- Returns:
Reference to model’s output information structure



-
[OutputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_output_info.html#_CPPv4N2ov10preprocess10OutputInfoE)&output(const std::string &tensor_name)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor6outputERKNSt6stringE) Gets output post-processing data structure for output identified by it’s tensor name.

- Parameters:
**tensor_name**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)name of specific output. Throws if tensor name is not associated with any input in a model- Returns:
Reference to model’s output information structure



-
[OutputInfo](https://docs.openvino.ai/classov_1_1preprocess_1_1_output_info.html#_CPPv4N2ov10preprocess10OutputInfoE)&output(size_t output_index)[#](https://docs.openvino.ai#_CPPv4N2ov10preprocess16PrePostProcessor6outputE6size_t) Gets output post-processing data structure for output identified by it’s order in a model.

- Parameters:
**output_index**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)index of specific output. Throws if output index is out of range for associated function- Returns:
Reference to model’s output information structure




-
class Shape : public std::vector<size_t>
[#](https://docs.openvino.ai#_CPPv4N2ov5ShapeE) *#include <shape.hpp>*[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)for a tensor.Public Functions

- OPENVINO_API Shape::reference operator[] (std::ptrdiff_t i)
Gets dimension at index.

- Parameters:
**i**– Index to shape dimension [-rank, rank).- Returns:
A reference to i-th dimension of this shape.



- OPENVINO_API Shape::const_reference operator[] (std::ptrdiff_t i) const
Gets dimension at index.

- Parameters:
**i**– Index to shape dimension [-rank, rank).- Returns:
A const reference to i-th dimension of this shape.



- OPENVINO_API Shape::reference at (std::ptrdiff_t i)
Gets dimension at index, with bounds checking.

- Parameters:
**i**– Index to shape dimension [-rank, rank).- Returns:
A reference to i-th dimension of this shape.



- OPENVINO_API Shape::const_reference at (std::ptrdiff_t i) const
Gets dimension at index, with bounds checking.

- Parameters:
**i**– Index to shape dimension [-rank, rank).- Returns:
A const reference to i-th dimension of this shape.




-
class Symbol
[#](https://docs.openvino.ai#_CPPv4N2ov6SymbolE) *#include <symbol.hpp>*Class representing unique symbol for the purpose of symbolic shape inference. Equality of symbols is being tracked by Disjoint-set data structure.

Public Functions

-
Symbol() = default
[#](https://docs.openvino.ai#_CPPv4N2ov6Symbol6SymbolEv) Default constructs a unique symbol.


-
Symbol() = default

-
struct DiscreteTypeInfo
[#](https://docs.openvino.ai#_CPPv4N2ov16DiscreteTypeInfoE) *#include <type.hpp>*Type information for a type system without inheritance; instances have exactly one type not related to any other type.

Supports three functions,

[ov::is_type<Type>](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1ad291be1aadbe791ff028cabafbb8c121),[ov::as_type<Type>](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1a256640280744d370491c0ee03009fb28), and[ov::as_type_ptr<Type>](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1a349526e15197857749ee1a488814e7ec)for type-safe dynamic conversions via static_cast/static_ptr_cast without using C++ RTTI. Type must have a static type_info member and a virtual get_type_info() member that returns a reference to its type_info member.

-
template<typename ForwardIt>