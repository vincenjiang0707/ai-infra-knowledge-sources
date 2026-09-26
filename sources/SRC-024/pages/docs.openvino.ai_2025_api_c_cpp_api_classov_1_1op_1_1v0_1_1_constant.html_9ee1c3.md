source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1op_1_1v0_1_1_constant.html
lastmod: 

# Class ov::op::v0::Constant[#](https://docs.openvino.ai#class-ov-op-v0-constant)

-
class Constant : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08ConstantE) Class for constants.

Public Functions

-
Constant(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Constant8ConstantERKN2ov6TensorE) Initialize a constant from

[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor).- Parameters:
**tensor**– The[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with data


-
template<typename T>

inline Constant(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const std::vector<[T](https://docs.openvino.ai#_CPPv4I0EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5ShapeRKNSt6vectorI1TEE)> &values)[#](https://docs.openvino.ai#_CPPv4I0EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5ShapeRKNSt6vectorI1TEE) Constructs a tensor constant.

- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**values**– A vector of literals for initializing the tensor constant. The size of values must match the size of the shape.



-
template<class T, class = typename std::enable_if<std::is_fundamental<
[T](https://docs.openvino.ai#_CPPv4I00EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5Shape1T)>::value>::type>

inline Constant(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape,[T](https://docs.openvino.ai#_CPPv4I00EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5Shape1T)value)[#](https://docs.openvino.ai#_CPPv4I00EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5Shape1T) Constructs a uniform tensor constant.

- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**value**– A scalar for initializing the uniform tensor constant. The value is broadcast to the specified shape.



-
Constant(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const std::vector<std::string> &values)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Constant8ConstantERKN7element4TypeERK5ShapeRKNSt6vectorINSt6stringEEE) Constructs a tensor constant This constructor is mainly to support deserialization of constants.

- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**values**– A list of string values to use as the constant data.



-
Constant(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const void *data)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Constant8ConstantERKN7element4TypeERK5ShapePKv) Constructs a tensor constant with the supplied data.

- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**data**– A void* to constant data.



Construct a tensor constant from shared memory.

The

[Constant](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_constant)can take ownership of shared memory if provided shared object is not null and manges memory lifetime.- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**data**– The pointer to shared memory.**so**– The shared object to take it ownership.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Constant24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)get_shape_val() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant13get_shape_valEv) Returns the value of the constant node as a

[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)object Can only be used on[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)nodes and interprets negative values as zeros.

-
[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)get_strides_val() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant15get_strides_valEv) Returns the value of the constant node as a

[Strides](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_strides)object Can only be used on[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)nodes and interprets negative values as zeros.

-
[Coordinate](https://docs.openvino.ai/classov_1_1_coordinate.html#_CPPv4N2ov10CoordinateE)get_coordinate_val() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant18get_coordinate_valEv) Returns the value of the constant node as a

[Coordinate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_coordinate)object Can only be used on[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)nodes and interprets negative values as zeros.

-
[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)get_coordinate_diff_val() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant23get_coordinate_diff_valEv) Returns the value of the constant node as a

[CoordinateDiff](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_coordinate_diff)object Can only be used on[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)nodes.

-
[AxisVector](https://docs.openvino.ai/classov_1_1_axis_vector.html#_CPPv4N2ov10AxisVectorE)get_axis_vector_val() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant19get_axis_vector_valEv) Returns the value of the constant node as an

[AxisVector](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_axis_vector)object Can only be used on[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)nodes and interprets negative values as zeros.

-
[AxisSet](https://docs.openvino.ai/classov_1_1_axis_set.html#_CPPv4N2ov7AxisSetE)get_axis_set_val() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant16get_axis_set_valEv) Returns the value of the constant node as an

[AxisSet](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_axis_set)object Can only be used on[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)nodes and interprets negative values as zeros. Repeated values are allowed.

-
size_t get_byte_size() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant13get_byte_sizeEv) Return data size in bytes.


-
std::vector<std::string> get_value_strings() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant17get_value_stringsEv) - Returns:
The initialization literals for the tensor constant.



-
template<typename T, typename std::enable_if<!std::is_same<bool,
[T](https://docs.openvino.ai#_CPPv4I0_PNSt9enable_ifIXntNSt7is_sameIb1TE5valueEEE4typeEENK2ov2op2v08Constant10get_vectorENSt6vectorI1TEEv)>::value>::type* = nullptr>

inline std::vector<[T](https://docs.openvino.ai#_CPPv4I0_PNSt9enable_ifIXntNSt7is_sameIb1TE5valueEEE4typeEENK2ov2op2v08Constant10get_vectorENSt6vectorI1TEEv)> get_vector() const[#](https://docs.openvino.ai#_CPPv4I0_PNSt9enable_ifIXntNSt7is_sameIb1TE5valueEEE4typeEENK2ov2op2v08Constant10get_vectorENSt6vectorI1TEEv) Get constant buffer as vector of element type T.

For low precision the vector do not perform bit unpacks. The returned vector has N elements where:

N is (elements count * (precision byte size / T byte size)) for standard precisions.

N is (byte size) for low precisions.



-
template<typename T>

inline std::vector<[T](https://docs.openvino.ai#_CPPv4I0ENK2ov2op2v08Constant11cast_vectorENSt6vectorI1TEE7int64_t)> cast_vector(int64_t num_elements = -1) const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov2op2v08Constant11cast_vectorENSt6vectorI1TEE7int64_t) Return the

[Constant](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_constant)’s value as a vector cast to type T.- Template Parameters:
**T**– Type to which data vector’s entries will be cast.- Parameters:
**num_elements**– (Optional) Number of elements to cast. In default case returns all elements- Returns:
[Constant](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_constant)’s data vector.


-
const
[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)get_tensor_view() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Constant15get_tensor_viewEv) Get view on constant data as tensor.

- Returns:
[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with constant data.


Public Static Functions

Wrapper around constructing a shared_ptr of a

[Constant](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_constant).- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**values**– A vector of values to use as the constant data.



Wrapper around constructing a shared_ptr of a

[Constant](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_constant).- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**values**– An initializer_list of values to use as the constant data.



-
static inline std::shared_ptr<
[Constant](https://docs.openvino.ai#_CPPv4N2ov2op2v08ConstantE)> create(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const void *memory)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Constant6createERKN7element4TypeERK5ShapePKv) Wrapper around constructing a shared_ptr of a

[Constant](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_constant).- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**memory**– An continues memory chunk which contains the constant data.



-
Constant(const