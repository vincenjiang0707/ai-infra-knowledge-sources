source: https://docs.openvino.ai/2025/api/c_cpp_api/group__ov__ops__cpp__api.html
lastmod: 

# Group Operations[#](https://docs.openvino.ai#group-operations)

-
*group*Operations OpenVINO C++ API to create operations from different opsets. Such API is used to creation models from code, write transformations and traverse the model graph

-
class AUGRUCell : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal9AUGRUCellE) *#include <augru_cell.hpp>*[AUGRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_a_u_g_r_u_cell)operation.Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal9AUGRUCell24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override

-
class AUGRUSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal13AUGRUSequenceE) *#include <augru_sequence.hpp>*[AUGRUSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_a_u_g_r_u_sequence)operation.Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op8internal13AUGRUSequence24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override

-
class Abs : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03AbsE) *#include <abs.hpp>*Elementwise absolute value operation.

Public Functions

-
Abs() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Abs3AbsEv) Constructs an absolute value operation.


-
Abs(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Abs3AbsERK6OutputI4NodeE) Constructs an absolute value operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d1, ...]`

- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)that produces the input tensor.`[d1, ...]`



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Abs12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Abs() = default

-
class Acos : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04AcosE) *#include <acos.hpp>*Elementwise inverse cosine (arccos) operation.

Public Functions

-
Acos() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Acos4AcosEv) Constructs an arccos operation.


-
Acos(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Acos4AcosERK6OutputI4NodeE) Constructs an arccos operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d1, ...]`

- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)that produces the input tensor.`[d1, ...]`



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Acos12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Acos() = default

-
class Acosh : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v35AcoshE) *#include <acosh.hpp>*Elementwise inverse hyperbolic cos operation.


-
class AdaptiveAvgPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveAvgPoolE) *#include <adaptive_avg_pool.hpp>*Adaptive average pooling operation.

Public Functions

-
AdaptiveAvgPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_shape)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveAvgPool15AdaptiveAvgPoolERK6OutputI4NodeERK6OutputI4NodeE) Constructs adaptive average pooling operation.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**output_shape**– 1D tensor describing output shape for spatial dimensions.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveAvgPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
AdaptiveAvgPool(const

-
class AdaptiveMaxPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveMaxPoolE) *#include <adaptive_max_pool.hpp>*Adaptive max pooling operation.

Public Functions

-
AdaptiveMaxPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_shape, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveMaxPool15AdaptiveMaxPoolERK6OutputI4NodeERK6OutputI4NodeERKN2ov7element4TypeE) Constructs adaptive max pooling operation.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**output_shape**– 1D tensor describing output shape for spatial dimensions.**index_element_type**– Specifies the output tensor type for indices output



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v815AdaptiveMaxPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
AdaptiveMaxPool(const

-
class Add : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13AddE) *#include <add.hpp>*Elementwise addition operation.

Public Functions

-
inline Add()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Add3AddEv) Constructs an uninitialized addition operation.


-
Add(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Add3AddERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs an addition operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Add12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Add()

-
class Asin : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04AsinE) *#include <asin.hpp>*Elementwise inverse sine (arcsin) operation.

Public Functions

-
Asin() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Asin4AsinEv) Constructs an arcsin operation.


-
Asin(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Asin4AsinERK6OutputI4NodeE) Constructs an arcsin operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d1, ...]`

- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)that produces the input tensor.`[d1, ...]`



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Asin12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Asin() = default

-
class Assign : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[AssignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_assign_base.html#_CPPv4N2ov2op4util10AssignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v36AssignE) *#include <assign.hpp>*[Assign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_assign)operation sets an input value to the variable with`variable_id`

Public Functions

-
Assign(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &new_value, const std::string &variable_id)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v36Assign6AssignERK6OutputI4NodeERKNSt6stringE) Constructs an

[Assign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_assign)operation.- Parameters:
**new_value**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**variable_id**– identifier of the variable to be updated.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v36Assign24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual std::string get_variable_id() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v36Assign15get_variable_idEv) Returns the identifier of corresponding variable.


-
Assign(const

-
class Assign : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[AssignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_assign_base.html#_CPPv4N2ov2op4util10AssignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v66AssignE) *#include <assign.hpp>*[Assign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_assign)operation sets an input value to the variable with`variable_id`

Public Functions

Constructs an

[Assign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_assign)operation.- Parameters:
**new_value**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**variable**– Class for storing and synchronizing element types, shapes and identifiers between pairs of Assign/ReadValue nodes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v66Assign24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual std::string get_variable_id() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v66Assign15get_variable_idEv) Returns the identifier of corresponding variable.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v66Assign12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.



-
class Atan : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04AtanE) *#include <atan.hpp>*Elementwise inverse tangent (arctan) operation.

Public Functions

-
Atan() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Atan4AtanEv) Constructs an arctan operation.


-
Atan(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Atan4AtanERK6OutputI4NodeE) Constructs an arctan operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d1, ...]`

- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)that produces the input tensor.`[d1, ...]`



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Atan12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Atan() = default

-
class Atanh : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v35AtanhE) *#include <atanh.hpp>*Elementwise inverse hyperbolic tangent operation.


-
class AvgPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[AvgPoolBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_avg_pool_base.html#_CPPv4N2ov2op4util11AvgPoolBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17AvgPoolE) *#include <avg_pool.hpp>*Batched average pooling operation.

Public Functions

-
AvgPool() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17AvgPool7AvgPoolEv) Constructs a batched average pooling operation.


-
AvgPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, bool exclude_pad,[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17AvgPool7AvgPoolERK6OutputI4NodeERK7StridesRK5ShapeRK5ShapeRK5Shapeb12RoundingTypeRK7PadType) Constructs a batched average pooling operation.

- Parameters:
**arg**– The output producing the input data batch tensor.`[d1, dn]`

**strides**– The strides.`[n]`

**pads_begin**– The beginning of padding shape.`[n]`

**pads_end**– The end of padding shape.`[n]`

**kernel**– The kernel shape.`[n]`

**exclude_pad**– If false then averages include padding elements, each treated as the number zero. If true, padding elements are entirely ignored when computing averages.**rounding_type**– Whether to use ceiling or floor rounding type while computing output shape.**auto_pad**– Padding type to use for additional padded dimensions



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17AvgPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
AvgPool() = default

-
class AvgPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[AvgPoolBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_avg_pool_base.html#_CPPv4N2ov2op4util11AvgPoolBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147AvgPoolE) *#include <avg_pool.hpp>*Batched average pooling operation.

Public Functions

-
AvgPool() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147AvgPool7AvgPoolEv) Constructs a batched average pooling operation.


-
AvgPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, bool exclude_pad,[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147AvgPool7AvgPoolERK6OutputI4NodeERK7StridesRK5ShapeRK5ShapeRK5Shapeb12RoundingTypeRK7PadType) Constructs a batched average pooling operation.

- Parameters:
**arg**– The output producing the input data batch tensor.`[d1, dn]`

**strides**– The strides.`[n]`

**pads_begin**– The beginning of padding shape.`[n]`

**pads_end**– The end of padding shape.`[n]`

**kernel**– The kernel shape.`[n]`

**exclude_pad**– If false then averages include padding elements, each treated as the number zero. If true, padding elements are entirely ignored when computing averages.**rounding_type**– Whether to use ceiling or floor rounding type while computing output shape.**auto_pad**– Padding type to use for additional padded dimensions



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147AvgPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
AvgPool() = default

-
class AvgPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[AvgPoolBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_avg_pool_base.html#_CPPv4N2ov2op4util11AvgPoolBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v167AvgPoolE) *#include <avg_pool.hpp>*Batched average pooling operation.

Public Functions

-
AvgPool() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v167AvgPool7AvgPoolEv) Constructs a batched average pooling operation.


-
AvgPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, bool exclude_pad,[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v167AvgPool7AvgPoolERK6OutputI4NodeERK7StridesRK7StridesRK5ShapeRK5ShapeRK5Shapeb12RoundingTypeRK7PadType) Constructs a batched average pooling operation.

- Parameters:
**arg**– The output producing the input data batch tensor.`[d1, dn]`

**strides**– The strides.`[n]`

**dilations**– The dilations.`[n]`

**pads_begin**– The beginning of padding shape.`[n]`

**pads_end**– The end of padding shape.`[n]`

**kernel**– The kernel shape.`[n]`

**exclude_pad**– If false then averages include padding elements, each treated as the number zero. If true, padding elements are entirely ignored when computing averages.**rounding_type**– Whether to use ceiling or floor rounding type while computing output shape.**auto_pad**– Padding type to use for additional padded dimensions



-
AvgPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, bool exclude_pad,[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v167AvgPool7AvgPoolERK6OutputI4NodeERK7StridesRK5ShapeRK5ShapeRK5Shapeb12RoundingTypeRK7PadType) Constructs a batched average pooling operation.

- Parameters:
**arg**– The output producing the input data batch tensor.`[d1, dn]`

**strides**– The strides.`[n]`

**pads_begin**– The beginning of padding shape.`[n]`

**pads_end**– The end of padding shape.`[n]`

**kernel**– The kernel shape.`[n]`

**exclude_pad**– If false then averages include padding elements, each treated as the number zero. If true, padding elements are entirely ignored when computing averages.**rounding_type**– Whether to use ceiling or floor rounding type while computing output shape.**auto_pad**– Padding type to use for additional padded dimensions



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v167AvgPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
AvgPool() = default

-
class BatchNormInference : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v018BatchNormInferenceE) *#include <batch_norm.hpp>*[BatchNormInference](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_batch_norm_inference)operation.Public Functions

-
BatchNormInference(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &gamma, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &beta, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &mean, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &variance, double epsilon)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v018BatchNormInference18BatchNormInferenceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEd) - Parameters:
**input**– [., C, …]**gamma**– gamma scaling for normalized value. [C]**beta**– bias added to the scaled normalized value [C]**mean**– value for mean normalization [C]**variance**– value for variance normalization [C]**epsilon**– Avoids divsion by 0 if input has 0 variance



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v018BatchNormInference24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
BatchNormInference(const

-
class BatchNormInference : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v518BatchNormInferenceE) *#include <batch_norm.hpp>*[BatchNormInference](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_batch_norm_inference)operation.Public Functions

-
BatchNormInference(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &gamma, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &beta, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &mean, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &variance, double epsilon)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v518BatchNormInference18BatchNormInferenceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEd) - Parameters:
**input**– [., C, …]**gamma**– gamma scaling for normalized value. [C]**beta**– bias added to the scaled normalized value [C]**mean**– value for mean normalization [C]**variance**– value for variance normalization [C]**epsilon**– Avoids divsion by 0 if input has 0 variance



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v518BatchNormInference24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
BatchNormInference(const

-
class BatchToSpace : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112BatchToSpaceE) *#include <batch_to_space.hpp>*[BatchToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_batch_to_space)permutes data from the batch dimension of the data tensor into spatial dimensions.Note

Values from the batch dimension are moved in spatial blocks dimensions.

Output node produces a tensor with shape: `[batch / (block_shape[0] * block_shape[1] * ... * block_shape[N - 1]), D_1 * block_shape[1] - crops_begin[1] - crops_end[1], D_2 * block_shape[2] - crops_begin[2] - crops_end[2], ..., D_{N - 1} * block_shape[N - 1] - crops_begin[N - 1] - crops_end[N - 1]` of the same type as `data` input.

Public Functions

-
BatchToSpace(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &block_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &crops_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &crops_end)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112BatchToSpace12BatchToSpaceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[BatchToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_batch_to_space)operation.- Parameters:
**data**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the data tensor**block_shape**– The sizes of the block of values to be moved**crops_begin**– Specifies the amount to crop from the beginning along each axis of`data`

input**crops_end**– Specifies the amount to crop from the ending along each axis of`data`

input.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v112BatchToSpace12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112BatchToSpace24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
BatchToSpace(const

-
class BinaryConvolution : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionFwdPropBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_fwd_prop_base.html#_CPPv4N2ov2op4util22ConvolutionFwdPropBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117BinaryConvolutionE) *#include <binary_convolution.hpp>*[BinaryConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_binary_convolution)operation.Public Functions

-
BinaryConvolution() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117BinaryConvolution17BinaryConvolutionEv) Constructs a binary convolution operation.


-
BinaryConvolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &kernel, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, BinaryConvolutionMode mode, float pad_value, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117BinaryConvolution17BinaryConvolutionERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7Strides21BinaryConvolutionModefRK7PadType) Constructs a binary convolution operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[N, C_OUT, R1, ... Rf]`

- Parameters:
**data**– The node producing the input data batch tensor.**kernel**– The node producing the filters tensor.**strides**– The strides.**pads_begin**– The beginning of padding shape.**pads_end**– The end of padding shape.**dilations**– The dilations.**mode**– Defines how input tensor 0/1 values and weights 0/1 are interpreted.**pad_value**– Floating-point value used to fill pad area.**auto_pad**– The pad type for automatically computing padding sizes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117BinaryConvolution24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const BinaryConvolutionMode &get_mode() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v117BinaryConvolution8get_modeEv) - Returns:
The mode of convolution.



-
inline float get_pad_value() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v117BinaryConvolution13get_pad_valueEv) - Returns:
The pad value.



-
BinaryConvolution() = default

-
class BitwiseAnd : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseBitwise](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_bitwise.html#_CPPv4N2ov2op4util24BinaryElementwiseBitwiseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseAndE) *#include <bitwise_and.hpp>*Elementwise bitwise AND operation.

Public Functions

-
BitwiseAnd() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseAnd10BitwiseAndEv) Constructs a bitwise AND operation.


-
BitwiseAnd(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseAnd10BitwiseAndERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a bitwise AND operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
BitwiseAnd() = default

-
class BitwiseLeftShift : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseBitwise](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_bitwise.html#_CPPv4N2ov2op4util24BinaryElementwiseBitwiseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1516BitwiseLeftShiftE) *#include <bitwise_left_shift.hpp>*Elementwise bitwise

[BitwiseLeftShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_left_shift)operation.Public Functions

-
BitwiseLeftShift() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1516BitwiseLeftShift16BitwiseLeftShiftEv) Constructs a bitwise

[BitwiseLeftShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_left_shift)operation.

-
BitwiseLeftShift(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1516BitwiseLeftShift16BitwiseLeftShiftERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a bitwise

[BitwiseLeftShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_left_shift)operation.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1516BitwiseLeftShift24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1516BitwiseLeftShift12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
BitwiseLeftShift() = default

-
class BitwiseNot : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseNotE) *#include <bitwise_not.hpp>*Elementwise bitwise negation operation.

Public Functions

-
BitwiseNot() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseNot10BitwiseNotEv) Constructs a bitwise negation operation.


-
BitwiseNot(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseNot10BitwiseNotERK6OutputI4NodeE) Constructs a bitwise negation operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseNot24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
BitwiseNot() = default

-
class BitwiseOr : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseBitwise](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_bitwise.html#_CPPv4N2ov2op4util24BinaryElementwiseBitwiseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v139BitwiseOrE) *#include <bitwise_or.hpp>*Elementwise bitwise OR operation.

Public Functions

-
BitwiseOr() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v139BitwiseOr9BitwiseOrEv) Constructs a bitwise OR operation.


-
BitwiseOr(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v139BitwiseOr9BitwiseOrERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a bitwise OR operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
BitwiseOr() = default

-
class BitwiseRightShift : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseBitwise](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_bitwise.html#_CPPv4N2ov2op4util24BinaryElementwiseBitwiseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1517BitwiseRightShiftE) *#include <bitwise_right_shift.hpp>*Elementwise bitwise

[BitwiseRightShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_right_shift)operation.Public Functions

-
BitwiseRightShift() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1517BitwiseRightShift17BitwiseRightShiftEv) Constructs a bitwise

[BitwiseRightShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_right_shift)operation.

-
BitwiseRightShift(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1517BitwiseRightShift17BitwiseRightShiftERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a bitwise

[BitwiseRightShift](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_bitwise_right_shift)operation.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1517BitwiseRightShift24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1517BitwiseRightShift12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
BitwiseRightShift() = default

-
class BitwiseXor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseBitwise](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_bitwise.html#_CPPv4N2ov2op4util24BinaryElementwiseBitwiseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseXorE) *#include <bitwise_xor.hpp>*Elementwise bitwise XOR operation.

Public Functions

-
BitwiseXor() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseXor10BitwiseXorEv) Constructs a bitwise XOR operation.


-
BitwiseXor(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1310BitwiseXor10BitwiseXorERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a bitwise XOR operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
BitwiseXor() = default

-
class Broadcast : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BroadcastBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_broadcast_base.html#_CPPv4N2ov2op4util13BroadcastBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39BroadcastE) *#include <broadcast.hpp>*Operation which “adds” axes to an input tensor, replicating elements from the input as needed along the new axes.

Public Functions

-
Broadcast() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Broadcast9BroadcastEv) Constructs a broadcast operation.


-
Broadcast(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &target_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes_mapping, const[BroadcastModeSpec](https://docs.openvino.ai/structov_1_1op_1_1_broadcast_mode_spec.html#_CPPv4N2ov2op17BroadcastModeSpecE)&broadcast_spec =[BroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op13BroadcastTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op13BroadcastType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Broadcast9BroadcastERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK17BroadcastModeSpec) Constructs a broadcast operation.

- Parameters:
**arg**– The input tensor to be broadcast.**target_shape**– The shape of the output tensor.**axes_mapping**– The axis positions (0-based) in the result that correspond to input axes. ‘Arg’ tensor is broadcast along the remaining axes. E.g.,[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)- [3, 4], Target[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)- [3, 5, 4, 4] axes_mapping - [0, 2] =>[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)along axes 1 and 3. axes_mapping - [0, 3] =>[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)along axes 1 and 2.**broadcast_spec**–[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)specification to use for determining broadcast axes. ‘axes_mapping’ should not be provided if mode other than explicit (none) is used.



-
Broadcast(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &target_shape, const[BroadcastModeSpec](https://docs.openvino.ai/structov_1_1op_1_1_broadcast_mode_spec.html#_CPPv4N2ov2op17BroadcastModeSpecE)&broadcast_spec =[BroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op13BroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op13BroadcastType5NUMPYE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Broadcast9BroadcastERK6OutputI4NodeERK6OutputI4NodeERK17BroadcastModeSpec) Constructs a broadcast operation.

- Parameters:
**arg**– The input tensor to be broadcast.**target_shape**– The shape of the output tensor.**broadcast_spec**–[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_broadcast)specification to use for determining broadcast axes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Broadcast24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual std::pair<bool,
[AxisSet](https://docs.openvino.ai/classov_1_1_axis_set.html#_CPPv4N2ov7AxisSetE)> get_broadcast_axes() const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v39Broadcast18get_broadcast_axesEv) - Returns:
true and the

[AxisSet](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_axis_set)if broadcast axes can be fully determined.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v39Broadcast8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v39Broadcast12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Broadcast() = default

-
class Broadcast : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BroadcastBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_broadcast_base.html#_CPPv4N2ov2op4util13BroadcastBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19BroadcastE) *#include <broadcast.hpp>*Operation which “adds” axes to an input tensor, replicating elements from the input as needed along the new axes.

Public Functions

-
Broadcast() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Broadcast9BroadcastEv) Constructs a broadcast operation.


-
Broadcast(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &target_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes_mapping, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&broadcast_spec =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)())[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Broadcast9BroadcastERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a broadcast operation.

- Parameters:
**arg**– The input tensor to be broadcast.**target_shape**– The shape of the output tensor.**axes_mapping**– The axis positions (0-based) in the result that correspond to input axes. ‘Arg’ tensor is broadcast along the remaining axes. E.g.,[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)- [3, 4], Target[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)- [3, 5, 4, 4] axes_mapping - [0, 2] =>[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)along axes 1 and 3. axes_mapping - [0, 3] =>[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)along axes 1 and 2.**broadcast_spec**–[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)specification to use for determining broadcast axes. ‘axes_mapping’ is ignored if broadcast_spec is not NONE



-
Broadcast(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &target_shape, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&broadcast_spec =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Broadcast9BroadcastERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a broadcast operation.

- Parameters:
**arg**– The input tensor to be broadcast.**target_shape**– The shape of the output tensor.**broadcast_spec**–[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)specification to use for determining broadcast axes



-
inline const
[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&get_broadcast_spec() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19Broadcast18get_broadcast_specEv) - Returns:
[Broadcast](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_broadcast)Specification.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Broadcast24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19Broadcast8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19Broadcast12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Broadcast() = default

-
class Bucketize : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39BucketizeE) *#include <bucketize.hpp>*Operation that bucketizes the input based on boundaries.

Public Functions

-
Bucketize(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &buckets, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)output_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E), const bool with_right_bound = true)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Bucketize9BucketizeERK6OutputI4NodeERK6OutputI4NodeEKN7element4TypeEKb) Constructs a

[Bucketize](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_bucketize)node.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39Bucketize24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Bucketize(const

-
class Ceiling : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07CeilingE) *#include <ceiling.hpp>*Elementwise ceiling operation.

Public Functions

-
Ceiling() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Ceiling7CeilingEv) Constructs a ceiling operation.


-
Ceiling(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Ceiling7CeilingERK6OutputI4NodeE) Constructs a ceiling operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v07Ceiling12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Ceiling() = default

-
class Clamp : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05ClampE) *#include <clamp.hpp>*Performs a clipping operation on all elements of the input node.

All input values that are outside of the <min;max> range are set to ‘min’ or ‘max’ depending on which side of the <min;max> range they are. The values that fall into this range remain unchanged.

Public Functions

-
Clamp(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const double min, const double max)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Clamp5ClampERK6OutputI4NodeEKdKd) Constructs a

[Clamp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_clamp)node.- Parameters:
**data**– -[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor**min**– - the lower bound of the <min;max> range**max**– - the upper bound of the <min;max> range



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Clamp24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v05Clamp12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Clamp(const

-
class Col2Im : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v156Col2ImE) *#include <col2im.hpp>*Operator combining sliding blocks into an image tensor.

Public Functions

-
Col2Im(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_size, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &kernel_size, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides =[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE){1, 1}, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations =[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE){1, 1}, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin =[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE){0, 0}, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end =[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE){0, 0})[#](https://docs.openvino.ai#_CPPv4N2ov2op3v156Col2Im6Col2ImERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK7StridesRK5ShapeRK5Shape) Constructs a

[Col2Im](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_col2_im)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**output_size**–[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)of the spatial dimensions of the output image**kernel_size**– Size of the sliding blocks**strides**– Stride in the sliding blocks in the input spatial dimensions**dilations**– Local stride of the elements**pads_begin**– Paddings at the beginning of each spatial axis, if undefined no padding is applied**pads_end**– Paddings at the end of each spatial axis, if undefined no padding is applied



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v156Col2Im24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Col2Im(const

-
class Concat : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06ConcatE) *#include <concat.hpp>*Concatenation operation.

Public Functions

-
Concat() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Concat6ConcatEv) Constructs a concatenation operation.


-
Concat(const OutputVector &args, int64_t axis)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Concat6ConcatERK12OutputVector7int64_t) Constructs a concatenation operation.

- Parameters:
**args**– The outputs producing the input tensors.**axis**– The axis along which to concatenate the input tensors.



-
Concat(const NodeVector &args, int64_t axis)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Concat6ConcatERK10NodeVector7int64_t) Constructs a concatenation operation.

- Parameters:
**args**– The nodes producing the input tensors.**axis**– The axis along which to concatenate the input tensors.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Concat24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline int64_t get_axis() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06Concat8get_axisEv) - Returns:
The concatenation axis.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06Concat12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Concat() = default

-
class Constant : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08ConstantE) *#include <constant.hpp>*Class for constants.

Public Functions

-
Constant(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Tensor](https://docs.openvino.ai/classov_1_1_tensor.html#_CPPv4N2ov6TensorE)&tensor)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Constant8ConstantERKN2ov6TensorE) Initialize a constant from

[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor).- Parameters:
**tensor**– The[ov::Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with data


-
template<typename T>

inline Constant(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const std::vector<[T](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_constant.html#_CPPv4I0EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5ShapeRKNSt6vectorI1TEE)> &values)[#](https://docs.openvino.ai#_CPPv4I0EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5ShapeRKNSt6vectorI1TEE) Constructs a tensor constant.

- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**values**– A vector of literals for initializing the tensor constant. The size of values must match the size of the shape.



-
template<class T, class = typename std::enable_if<std::is_fundamental<
[T](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_constant.html#_CPPv4I00EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5Shape1T)>::value>::type>

inline Constant(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape,[T](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_constant.html#_CPPv4I00EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5Shape1T)value)[#](https://docs.openvino.ai#_CPPv4I00EN2ov2op2v08Constant8ConstantERKN7element4TypeERK5Shape1T) Constructs a uniform tensor constant.

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
[T](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_constant.html#_CPPv4I0_PNSt9enable_ifIXntNSt7is_sameIb1TE5valueEEE4typeEENK2ov2op2v08Constant10get_vectorENSt6vectorI1TEEv)>::value>::type* = nullptr>

inline std::vector<[T](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_constant.html#_CPPv4I0_PNSt9enable_ifIXntNSt7is_sameIb1TE5valueEEE4typeEENK2ov2op2v08Constant10get_vectorENSt6vectorI1TEEv)> get_vector() const[#](https://docs.openvino.ai#_CPPv4I0_PNSt9enable_ifIXntNSt7is_sameIb1TE5valueEEE4typeEENK2ov2op2v08Constant10get_vectorENSt6vectorI1TEEv) Get constant buffer as vector of element type T.

For low precision the vector do not perform bit unpacks. The returned vector has N elements where:

N is (elements count * (precision byte size / T byte size)) for standard precisions.

N is (byte size) for low precisions.



-
template<typename T>

inline std::vector<[T](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_constant.html#_CPPv4I0ENK2ov2op2v08Constant11cast_vectorENSt6vectorI1TEE7int64_t)> cast_vector(int64_t num_elements = -1) const[#](https://docs.openvino.ai#_CPPv4I0ENK2ov2op2v08Constant11cast_vectorENSt6vectorI1TEE7int64_t) Return the

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
[Constant](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_constant.html#_CPPv4N2ov2op2v08ConstantE)> create(const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&type, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&shape, const void *memory)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Constant6createERKN7element4TypeERK5ShapePKv) Wrapper around constructing a shared_ptr of a

[Constant](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_constant).- Parameters:
**type**– The element type of the tensor constant.**shape**– The shape of the tensor constant.**memory**– An continues memory chunk which contains the constant data.



-
Constant(const

-
class Convert : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07ConvertE) *#include <convert.hpp>*Elementwise type conversion operation.

Public Functions

-
Convert() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Convert7ConvertEv) Constructs a conversion operation.


-
Convert(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&destination_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Convert7ConvertERK6OutputI4NodeERKN2ov7element4TypeE) Constructs a conversion operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**destination_type**– Element type for the output tensor.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Convert24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v07Convert12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Convert() = default

-
class ConvertLike : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111ConvertLikeE) *#include <convert_like.hpp>*Elementwise type conversion operation.

Public Functions

-
ConvertLike() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111ConvertLike11ConvertLikeEv) Constructs a conversion operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111ConvertLike24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ConvertLike() = default

-
class ConvertPromoteTypes : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypesE) *#include <convert_promote_types.hpp>*Elementwise operation that promote and convert input types to one common datatype.

Public Functions

-
ConvertPromoteTypes() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes19ConvertPromoteTypesEv) Constructs operation that promote and convert input types to one common datatype.


-
ConvertPromoteTypes(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_1, const bool promote_unsafe = false, const bool pytorch_scalar_promotion = false, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&u64_integer_promotion_target =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[f32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3f32EN6Type_t3f32E))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes19ConvertPromoteTypesERK6OutputI4NodeERK6OutputI4NodeEKbKbRKN7element4TypeE) Constructs operation that promote and convert input types to one common datatype.

- Parameters:
**input_0**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)with datatype to be promoted.**input_1**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)with datatype to be promoted.**promote_unsafe**– Bool attribute whether to allow promotions that might result in bit-widening, precision loss and undefined behaviors.**pytorch_scalar_promotion**– Bool attribute whether to promote scalar input to type provided by non-scalar input when number format is matching.**u64_integer_promotion_target**– Element type attribute to select promotion result for u64 and signed integers.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
bool get_pytorch_scalar_promotion() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1419ConvertPromoteTypes28get_pytorch_scalar_promotionEv) Get bool attribute whether to promote scalar input to type provided by non-scalar input when number format is matching.


-
void set_pytorch_scalar_promotion(bool pytorch_scalar_promotion)
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes28set_pytorch_scalar_promotionEb) Set bool attribute whether to promote scalar input to type provided by non-scalar input when number format is matching.


-
bool get_promote_unsafe() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1419ConvertPromoteTypes18get_promote_unsafeEv) Get bool attribute whether to allow promotions that might result in bit-widening, precision loss and undefined behaviors.


-
void set_promote_unsafe(bool promote_unsafe)
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1419ConvertPromoteTypes18set_promote_unsafeEb) Set bool attribute whether to allow promotions that might result in bit-widening, precision loss and undefined behaviors.


-
ConvertPromoteTypes() = default

-
class Convolution : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionFwdPropBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_fwd_prop_base.html#_CPPv4N2ov2op4util22ConvolutionFwdPropBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111ConvolutionE) *#include <convolution.hpp>*Batched convolution operation, with optional window dilation and stride.

Public Functions

-
Convolution() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111Convolution11ConvolutionEv) Constructs a batched convolution operation.


-
Convolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data_batch, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &filters, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111Convolution11ConvolutionERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadType) Constructs a batched convolution operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[N, C_OUT, R1, ... Rf]`

- Parameters:
**data_batch**– The node producing the input data batch tensor.`[N, C_IN, D1, ... Df]`

**filters**– The node producing the filters tensor.`[C_OUT, C_IN, F1, ... Ff]`

**strides**– The strides.`[f]`

**dilations**– The dilations.`[f]`

**pads_begin**– The beginning of padding shape.`[f]`

**pads_end**– The end of padding shape.`[f]`

**auto_pad**– The pad type for automatically computing padding sizes.`[f]`




-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v111Convolution24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Convolution() = default

-
class ConvolutionBackpropData : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvolutionBackPropBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convolution_back_prop_base.html#_CPPv4N2ov2op4util23ConvolutionBackPropBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v123ConvolutionBackpropDataE) *#include <convolution.hpp>*Data batch backprop for batched convolution operation.

Public Functions

-
ConvolutionBackpropData() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v123ConvolutionBackpropData23ConvolutionBackpropDataEv) Constructs a batched-convolution data batch-backprop operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v123ConvolutionBackpropData24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
const
[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)get_output_shape() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v123ConvolutionBackpropData16get_output_shapeEv) - Returns:
The output spatial dimensions shape.



-
ConvolutionBackpropData() = default

-
class Cos : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03CosE) *#include <cos.hpp>*Elementwise cosine operation.

Public Functions

-
Cos() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Cos3CosEv) Constructs a cosine operation.


-
Cos(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Cos3CosERK6OutputI4NodeE) Constructs a cosine operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Cos12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Cos() = default

-
class Cosh : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04CoshE) *#include <cosh.hpp>*Elementwise hyperbolic cosine (cosh) operation.

Public Functions

-
Cosh() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Cosh4CoshEv) Constructs a hyperbolic cosine operation.


-
Cosh(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Cosh4CoshERK6OutputI4NodeE) Constructs a hyperbolic cosine operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Cosh12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Cosh() = default

-
class CTCGreedyDecoder : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v016CTCGreedyDecoderE) *#include <ctc_greedy_decoder.hpp>*[CTCGreedyDecoder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_c_t_c_greedy_decoder)operation.Public Functions

-
CTCGreedyDecoder(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &seq_len, const bool ctc_merge_repeated)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v016CTCGreedyDecoder16CTCGreedyDecoderERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a

[CTCGreedyDecoder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_c_t_c_greedy_decoder)operation.- Parameters:
**input**– Logits on which greedy decoding is performed**seq_len**– Sequence lengths**ctc_merge_repeated**– Whether to merge repeated labels



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v016CTCGreedyDecoder24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
CTCGreedyDecoder(const

-
class CTCGreedyDecoderSeqLen : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v622CTCGreedyDecoderSeqLenE) *#include <ctc_greedy_decoder_seq_len.hpp>*Operator performing CTCGreedyDecoder.

Public Functions

-
CTCGreedyDecoderSeqLen(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &seq_len, const bool merge_repeated = true, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&classes_index_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E), const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&sequence_length_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v622CTCGreedyDecoderSeqLen22CTCGreedyDecoderSeqLenERK6OutputI4NodeERK6OutputI4NodeEKbRKN7element4TypeERKN7element4TypeE) Constructs a

[CTCGreedyDecoderSeqLen](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_c_t_c_greedy_decoder_seq_len)operation.- Parameters:
**input**– 3-D tensor of logits on which greedy decoding is performed**seq_len**– 1-D tensor of sequence lengths**merge_repeated**– Whether to merge repeated labels**classes_index_type**– Specifies the output classes_index tensor type**sequence_length_type**– Specifies the output sequence_length tensor type



-
CTCGreedyDecoderSeqLen(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &seq_len, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &blank_index, const bool merge_repeated = true, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&classes_index_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E), const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&sequence_length_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v622CTCGreedyDecoderSeqLen22CTCGreedyDecoderSeqLenERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKbRKN7element4TypeERKN7element4TypeE) Constructs a

[CTCGreedyDecoderSeqLen](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_c_t_c_greedy_decoder_seq_len)operation.- Parameters:
**input**– 3-D tensor of logits on which greedy decoding is performed**seq_len**– 1-D tensor of sequence lengths**blank_index**– Scalar or 1-D tensor with 1 element used to mark a blank index**merge_repeated**– Whether to merge repeated labels**classes_index_type**– Specifies the output classes_index tensor type**sequence_length_type**– Specifies the output sequence_length tensor type



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v622CTCGreedyDecoderSeqLen24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline bool get_merge_repeated() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v622CTCGreedyDecoderSeqLen18get_merge_repeatedEv) Get merge_repeated attribute.

- Returns:
Current value of merge_repeated attribute



-
inline void set_merge_repeated(bool merge_repeated)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v622CTCGreedyDecoderSeqLen18set_merge_repeatedEb) Set merge_repeated attribute.

- Parameters:
**merge_repeated**– A new value for the attribute


-
inline const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&get_classes_index_type() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v622CTCGreedyDecoderSeqLen22get_classes_index_typeEv) Get classes_index_type attribute.

- Returns:
Current value of classes_index_type attribute



-
inline void set_classes_index_type(const
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&classes_index_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v622CTCGreedyDecoderSeqLen22set_classes_index_typeERKN7element4TypeE) Set classes_index_type attribute.

- Parameters:
**classes_index_type**– Type of classes_index


-
CTCGreedyDecoderSeqLen(const

-
class CTCLoss : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v47CTCLossE) *#include <ctc_loss.hpp>*[CTCLoss](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_c_t_c_loss)operation.Public Functions

-
CTCLoss(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &logits, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &logit_length, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &labels, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &label_length, const bool preprocess_collapse_repeated = false, const bool ctc_merge_repeated = true, const bool unique = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v47CTCLoss7CTCLossERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKbKbKb) Constructs a

[CTCLoss](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_c_t_c_loss)operation.- Parameters:
**logits**– 3-D tensor of logits**logit_length**– 1-D tensor of length for each object from a batch**labels**– 2-D tensor of labels for which likelyhood is estimated using logist**label_length**– 1-D tensor of length for each label sequence**blank_index**– Scalar used to mark a blank index**preprocess_collapse_repeated**– Flag for preprocessing labels before loss calculation**ctc_merge_repeated**– Flag for merging repeated characters in a potential alignment**unique**– Flag to find unique elements in a target before matching with alignment



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v47CTCLoss24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
CTCLoss(const

-
class CumSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSumE) *#include <cum_sum.hpp>*[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)cumulative sum operation.Compute the cumulative sum of the input tensor along the axis specified.

Public Functions

-
CumSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSum6CumSumEv) Constructs a cumulative summation operation.


-
CumSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const bool exclusive = false, const bool reverse = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSum6CumSumERK6OutputI4NodeERK6OutputI4NodeEKbKb) Constructs a cumulative summation operation.

- Parameters:
**arg**– The tensor to be summed.**axis**– zero dimension tensor specifying axis position along which cumulative sum must be performed**exclusive**– if set to true, the top element is not included**reverse**– if set to true, will perform the sums in reverse direction



-
CumSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const bool exclusive = false, const bool reverse = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSum6CumSumERK6OutputI4NodeEKbKb) Constructs a cumulative summation operation with axis = 0.

- Parameters:
**arg**– The tensor to be summed


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06CumSum12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06CumSum24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
CumSum() = default

-
class DeformableConvolution : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[DeformableConvolutionBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_deformable_convolution_base.html#_CPPv4N2ov2op4util25DeformableConvolutionBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v121DeformableConvolutionE) *#include <deformable_convolution.hpp>*[DeformableConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_deformable_convolution)operation.Public Functions

-
DeformableConvolution() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v121DeformableConvolution21DeformableConvolutionEv) Constructs a conversion operation.


-
DeformableConvolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &filters, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), const int64_t group = 1, const int64_t deformable_group = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v121DeformableConvolution21DeformableConvolutionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadTypeK7int64_tK7int64_t) Constructs a conversion operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**offsets**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the deformable values tensor.**filters**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the filters(kernels) tensor with OIZYX layout.**strides**–[Convolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_convolution)strides.**pads_begin**– Amount of padding to be added to the beginning along each axis. For example in case of a 2D input the value of (1, 2) means that 1 element will be added to the top and 2 elements to the left.**pads_end**– Amount of padding to be added to the end along each axis.**dilations**– The distance in width and height between the weights in the filters tensor.**auto_pad**– Specifies how the automatic calculation of padding should be done.**group**– The number of groups which both output and input should be split into.**deformable_group**– The number of groups which deformable values and output should be split into along the channel axis.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v121DeformableConvolution24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
DeformableConvolution() = default

-
class DeformableConvolution : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[DeformableConvolutionBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_deformable_convolution_base.html#_CPPv4N2ov2op4util25DeformableConvolutionBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolutionE) *#include <deformable_convolution.hpp>*[DeformableConvolution](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_deformable_convolution)operation.Public Functions

-
DeformableConvolution() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolution21DeformableConvolutionEv) Constructs a conversion operation.


-
DeformableConvolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &filters, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), const int64_t group = 1, const int64_t deformable_group = 1, const bool bilinear_interpolation_pad = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolution21DeformableConvolutionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadTypeK7int64_tK7int64_tKb) Constructs a conversion operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**offsets**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the deformable values tensor.**filters**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the filters(kernels) tensor with OIZYX layout.**strides**– Convolution strides.**pads_begin**– Amount of padding to be added to the beginning along each axis. For example in case of a 2D input the value of (1, 2) means that 1 element will be added to the top and 2 elements to the left.**pads_end**– Amount of padding to be added to the end along each axis.**dilations**– The distance in width and height between the weights in the filters tensor.**auto_pad**– Specifies how the automatic calculation of padding should be done.**group**– The number of groups which both output and input should be split into.**deformable_group**– The number of groups which deformable values and output should be split into along the channel axis.**bilinear_interpolation_pad**– The flag that determines the mode of bilinear interpolation execution.[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)the flag is`true`

and the sampling location is within one pixel outside of the feature map boundary, then bilinear interpolation is performed on the zero padded feature map.[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)the flag is`false`

and the sampling location is within one pixel outside of the feature map boundary, then the sampling location shifts to the inner boundary of the feature map.`



-
DeformableConvolution(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &filters, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &mask, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_begin, const[CoordinateDiff](https://docs.openvino.ai/classov_1_1_coordinate_diff.html#_CPPv4N2ov14CoordinateDiffE)&pads_end, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad =[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), const int64_t group = 1, const int64_t deformable_group = 1, const bool bilinear_interpolation_pad = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolution21DeformableConvolutionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK7StridesRK14CoordinateDiffRK14CoordinateDiffRK7StridesRK7PadTypeK7int64_tK7int64_tKb) Constructs a conversion operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**offsets**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the deformable values tensor.**filters**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the filters(kernels) tensor with OIZYX layout.**mask**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the mask(mask) tensor.**strides**– Convolution strides.**pads_begin**– Amount of padding to be added to the beginning along each axis. For example in case of a 2D input the value of (1, 2) means that 1 element will be added to the top and 2 elements to the left.**pads_end**– Amount of padding to be added to the end along each axis.**dilations**– The distance in width and height between the weights in the filters tensor.**auto_pad**– Specifies how the automatic calculation of padding should be done.**group**– The number of groups which both output and input should be split into.**deformable_group**– The number of groups which deformable values and output should be split into along the channel axis.**bilinear_interpolation_pad**– The flag that determines the mode of bilinear interpolation execution.[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)the flag is`true`

and the sampling location is within one pixel outside of the feature map boundary, then bilinear interpolation is performed on the zero padded feature map.[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)the flag is`false`

and the sampling location is within one pixel outside of the feature map boundary, then the sampling location shifts to the inner boundary of the feature map.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v821DeformableConvolution24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
DeformableConvolution() = default

-
class DeformablePSROIPooling : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v122DeformablePSROIPoolingE) *#include <deformable_psroi_pooling.hpp>*[DeformablePSROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_deformable_p_s_r_o_i_pooling)operation.Public Functions

-
DeformablePSROIPooling(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &coords, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const int64_t output_dim, const float spatial_scale, const int64_t group_size = 1, const std::string mode = "bilinear_deformable", int64_t spatial_bins_x = 1, int64_t spatial_bins_y = 1, float trans_std = 1, int64_t part_size = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v122DeformablePSROIPooling22DeformablePSROIPoolingERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK7int64_tKfK7int64_tKNSt6stringE7int64_t7int64_tf7int64_t) Constructs a

[DeformablePSROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_deformable_p_s_r_o_i_pooling)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with position sensitive score maps**coords**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with list of five element tuples describing ROI coordinates**offsets**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with transformation values**output_dim**– Pooled output channel number**group_size**– Number of horizontal bins per row to divide ROI area, it defines output width and height**spatial_scale**– Multiplicative spatial scale factor to translate ROI coordinates from their input scale to the scale used when pooling**mode**– Specifies mode for pooling.**spatial_bins_x**– Specifies numbers of bins to divide ROI single bin over width**spatial_bins_y**– Specifies numbers of bins to divide ROI single bin over height**no_trans**– The flag that specifies whenever third input exists and contains transformation (offset) values**trans_std**– The value that all transformation (offset) values are multiplied with**part_size**– The number of parts the output tensor spatial dimensions are divided into. Basically it is the height and width of the third input



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v122DeformablePSROIPooling24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
DeformablePSROIPooling(const

-
class DepthToSpace : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012DepthToSpaceE) *#include <depth_to_space.hpp>*[DepthToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_depth_to_space)permutes data from the depth dimension of the input blob into spatial dimensions.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node produces a tensor with shape: [N, C/(blocksize * blocksize), H * blocksize, W * blocksize]Note

Values from the depth dimension (assuming NCHW layout) are moved in spatial blocks to the height and width dimensions.

Public Functions

-
DepthToSpace(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const DepthToSpaceMode &mode, std::size_t block_size = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012DepthToSpace12DepthToSpaceERK6OutputI4NodeERK16DepthToSpaceModeNSt6size_tE) Constructs a

[DepthToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_depth_to_space)operation.- Parameters:
**data**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor**mode**– Specifies how the input depth dimension is split to block coordinates**block_size**– The size of the block of values to be moved



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012DepthToSpace24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v012DepthToSpace12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
DepthToSpace(const

-
class DFT : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[FFTBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_f_f_t_base.html#_CPPv4N2ov2op4util7FFTBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v73DFTE) *#include <dft.hpp>*An operation

[DFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_d_f_t)that computes the discrete Fourier transformation.

-
class Divide : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16DivideE) *#include <divide.hpp>*Elementwise division operation.

Public Functions

-
inline Divide()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Divide6DivideEv) Constructs a division operation.


-
Divide(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, bool pythondiv, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Divide6DivideERK6OutputI4NodeERK6OutputI4NodeEbRK17AutoBroadcastSpec) Constructs a division operation.


-
Divide(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Divide6DivideERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a division operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v16Divide12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Divide()

-
class Einsum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76EinsumE) *#include <einsum.hpp>*[Einsum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_einsum)operation.Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Einsum24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


Public Static Functions

-
static void parse_equation(const std::string &equation, std::vector<std::string> &input_subscripts, std::string &output_subscript)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Einsum14parse_equationERKNSt6stringERNSt6vectorINSt6stringEEERNSt6stringE) Check correctness of equation format and extract input subscripts and output subscript.

- Parameters:
**equation**– Equation to be parsed and checked**input_subscripts**– A vector of extracted input subscripts**output_subscript**– An output subscript



-
static std::vector<std::string> extract_labels(const std::string &subscript)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Einsum14extract_labelsERKNSt6stringE) Extract labels (from subscript) that can be alphabetic letters or ellipsis.

- Parameters:
**subscript**– Subscript- Returns:
A vector of extracted labels from the input subscript in the order of appearence



-
virtual void validate_and_infer_types() override

-
class Elu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03EluE) *#include <elu.hpp>*Exponential Linear Unit x < 0 => f(x) = alpha * (exp(x) - 1.) x >= 0 => f(x) = x.

Public Functions

-
Elu(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const double alpha)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Elu3EluERK6OutputI4NodeEKd) Constructs an

[Elu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_elu)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor**alpha**– Multiplier for negative values



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Elu24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Elu(const

-
class EmbeddingSegmentsSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v320EmbeddingSegmentsSumE) *#include <embedding_segments_sum.hpp>*Returns embeddings for given indices.

Public Functions

-
EmbeddingSegmentsSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v320EmbeddingSegmentsSum20EmbeddingSegmentsSumEv) Constructs a

[EmbeddingSegmentsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_segments_sum)operation.

-
EmbeddingSegmentsSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &segment_ids, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_segments, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &default_index, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v320EmbeddingSegmentsSum20EmbeddingSegmentsSumERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[EmbeddingSegmentsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_segments_sum)operation.[EmbeddingSegmentsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_segments_sum)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**'emb_table'**– tensor containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**'indices'**– tensor of shape [num_indices] and of type T_IND. Required**<tt>segment_ids</tt>**– tensor of shape`[num_indices]`

and of type*T_IND*with indices into the output[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor). Values should be sorted and can be repeated. Required.**<tt>num_segments</tt>**– scalar of type*T_IND*indicating the number of segments. Required.**'default_index'**– scalar of type T_IND containing default index in embedding table to fill empty “bags”. If not provided empty “bags” are filled with zeros. Optional.**'per_sample_weights'**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v320EmbeddingSegmentsSum24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
EmbeddingSegmentsSum() = default

-
class EmbeddingBagOffsets : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[EmbeddingBagOffsetsBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_embedding_bag_offsets_base.html#_CPPv4N2ov2op4util23EmbeddingBagOffsetsBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1519EmbeddingBagOffsetsE) *#include <embeddingbag_offsets.hpp>*Returns embeddings for given indices.

Public Functions

-
EmbeddingBagOffsets() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1519EmbeddingBagOffsets19EmbeddingBagOffsetsEv) Constructs a

[EmbeddingBagOffsets](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_offsets)operation.

-
EmbeddingBagOffsets(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &default_index, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights, const Reduction &reduction = Reduction::SUM)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1519EmbeddingBagOffsets19EmbeddingBagOffsetsERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK9Reduction) Constructs a

[EmbeddingBagOffsets](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_offsets)operation.[EmbeddingBagOffsets](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_offsets)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**emb_table**– tensor containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**indices**– tensor of shape [num_indices] and of type T_IND. Required**offsets**– tensor of shape [batch] and of type T_IND containing the starting index positions of each “bag” in indices. Required.**default_index**– scalar of type T_IND containing default index in embedding table to fill empty “bags”. If set to value -1 or not provided, empty “bags” are filled with zeros. Reverse indexing using negative values is not supported. Optional.**per_sample_weights**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.**reduction**– enum to select algorithm used to perform reduction of elements in bag. Optional.



-
EmbeddingBagOffsets() = default

-
class EmbeddingBagOffsetsSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[EmbeddingBagOffsetsBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_embedding_bag_offsets_base.html#_CPPv4N2ov2op4util23EmbeddingBagOffsetsBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v322EmbeddingBagOffsetsSumE) *#include <embeddingbag_offsets_sum.hpp>*Returns embeddings for given indices.

Public Functions

-
EmbeddingBagOffsetsSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v322EmbeddingBagOffsetsSum22EmbeddingBagOffsetsSumEv) Constructs a

[EmbeddingBagOffsetsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_offsets_sum)operation.

-
EmbeddingBagOffsetsSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &offsets, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &default_index, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v322EmbeddingBagOffsetsSum22EmbeddingBagOffsetsSumERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[EmbeddingBagOffsetsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_offsets_sum)operation.[EmbeddingBagOffsetsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_offsets_sum)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**emb_table**– tensor containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**indices**– tensor of shape [num_indices] and of type T_IND. Required**offsets**– tensor of shape [batch] and of type T_IND containing the starting index positions of each “bag” in indices. Required.**default_index**– scalar of type T_IND containing default index in embedding table to fill empty “bags”. If set to value -1 or not provided, empty “bags” are filled with zeros. Reverse indexing using negative values is not supported. Optional.**per_sample_weights**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.



-
EmbeddingBagOffsetsSum() = default

-
class EmbeddingBagPacked : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[EmbeddingBagPackedBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_embedding_bag_packed_base.html#_CPPv4N2ov2op4util22EmbeddingBagPackedBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518EmbeddingBagPackedE) *#include <embeddingbag_packed.hpp>*Returns embeddings for given indices.

Public Functions

-
EmbeddingBagPacked() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518EmbeddingBagPacked18EmbeddingBagPackedEv) Constructs a

[EmbeddingBagPacked](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_packed)operation.

-
EmbeddingBagPacked(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights, const Reduction &reduction = Reduction::SUM)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518EmbeddingBagPacked18EmbeddingBagPackedERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK9Reduction) Constructs a

[EmbeddingBagPacked](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_packed)operation.[EmbeddingBagPacked](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_embedding_bag_packed)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**emb_table**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**indices**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape`[batch, indices_per_bag]`

and of type*T_IND*. Required.**per_sample_weights**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.**reduction**– enum to select algorithm used to perform reduction of elements in bag. Optional.



-
EmbeddingBagPacked() = default

-
class EmbeddingBagPackedSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[EmbeddingBagPackedBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_embedding_bag_packed_base.html#_CPPv4N2ov2op4util22EmbeddingBagPackedBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321EmbeddingBagPackedSumE) *#include <embeddingbag_packedsum.hpp>*Returns embeddings for given indices.

Public Functions

-
EmbeddingBagPackedSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321EmbeddingBagPackedSum21EmbeddingBagPackedSumEv) Constructs a

[EmbeddingBagPackedSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_packed_sum)operation.

-
EmbeddingBagPackedSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &emb_table, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &per_sample_weights)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321EmbeddingBagPackedSum21EmbeddingBagPackedSumERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[EmbeddingBagPackedSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_packed_sum)operation.[EmbeddingBagPackedSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_bag_packed_sum)constructs an output tensor by replacing every index in a given input tensor with a row (from the weights matrix) at that index- Parameters:
**emb_table**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)containing the embedding lookup table of the module of shape [num_emb, emb_dim1, emb_dim2, …] and of type T**indices**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape`[batch, indices_per_bag]`

and of type*T_IND*. Required.**per_sample_weigths**– tensor of the same shape as indices and of type T. Each value in this tensor are multiplied with each value pooled from embedding table for each index. Optional.



-
EmbeddingBagPackedSum() = default

-
class Equal : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseComparison](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_comparison.html#_CPPv4N2ov2op4util27BinaryElementwiseComparisonE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15EqualE) *#include <equal.hpp>*Elementwise is-equal operation.

*Inputs*Type

Description

`arg0`

\(E[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and element type.

`arg1`

\(E[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of the same shape and element type as

`arg0`

.`autob`

Auto broadcast specification.

Type

Description

\(\texttt{bool}[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = 1\text{ if }\texttt{arg0}[i_1,\dots,i_n] = \texttt{arg1}[i_1,\dots,i_n]\text{, else } 0\)

Public Functions

-
inline Equal()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Equal5EqualEv) Constructs an equal operation.


-
Equal(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Equal5EqualERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs an equal operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v15Equal12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Equal()

-
class Erf : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03ErfE) *#include <erf.hpp>*Elementwise erf operation.

Public Functions

-
Erf() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Erf3ErfEv) Constructs a floor operation.


-
Erf(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Erf3ErfERK6OutputI4NodeE) Constructs a floor operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Erf12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Erf() = default

-
class Exp : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03ExpE) *#include <exp.hpp>*Elementwise natural exponential (exp) operation.

Public Functions

-
Exp() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Exp3ExpEv) Constructs an exponential operation.


-
Exp(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Exp3ExpERK6OutputI4NodeE) Constructs an exponential operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Exp12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Exp() = default

-
class ExperimentalDetectronDetectionOutput : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutputE) *#include <experimental_detectron_detection_output.hpp>*An operation

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output)performs non-maximum suppression to generate the detection output using information on location and score predictions.Public Functions

-
ExperimentalDetectronDetectionOutput(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_deltas, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_im_info, const[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output.html#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput36ExperimentalDetectronDetectionOutputERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output)operation.- Parameters:
**input_rois**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)rois**input_deltas**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)deltas**input_scores**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)scores**input_im_info**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)image info**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v6_1_1_experimental_detectron_detection_output_1_1_attributes)attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const
[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output.html#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v636ExperimentalDetectronDetectionOutput9get_attrsEv) Returns attributes of the operation

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output).

-
void set_attrs(
[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output.html#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput10AttributesE)attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput9set_attrsE10Attributes) Set the attributes of the operation

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output).- Parameters:
**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v6_1_1_experimental_detectron_detection_output_1_1_attributes)to set.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v636ExperimentalDetectronDetectionOutput10AttributesE) *#include <experimental_detectron_detection_output.hpp>*Structure that specifies attributes of the operation.


-
ExperimentalDetectronDetectionOutput(const

-
class ExperimentalDetectronGenerateProposalsSingleImage : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImageE) *#include <experimental_detectron_generate_proposals.hpp>*An operation

[ExperimentalDetectronGenerateProposalsSingleImage](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_generate_proposals_single_image)computes ROIs and their scores based on input data.Public Functions

-
ExperimentalDetectronGenerateProposalsSingleImage(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &im_info, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &anchors, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &deltas, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_generate_proposals_single_image.html#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImage10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImage49ExperimentalDetectronGenerateProposalsSingleImageERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[ExperimentalDetectronGenerateProposalsSingleImage](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_generate_proposals_single_image)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImage24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v649ExperimentalDetectronGenerateProposalsSingleImage10AttributesE) *#include <experimental_detectron_generate_proposals.hpp>*Structure that specifies attributes of the operation.


-
ExperimentalDetectronGenerateProposalsSingleImage(const

-
class ExperimentalDetectronPriorGridGenerator : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGeneratorE) *#include <experimental_detectron_prior_grid_generator.hpp>*An operation

[ExperimentalDetectronPriorGridGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator)generates prior grids of specified sizes.Public Functions

-
ExperimentalDetectronPriorGridGenerator(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &priors, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &feature_map, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &im_data, const[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator.html#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator39ExperimentalDetectronPriorGridGeneratorERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const
[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator.html#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v639ExperimentalDetectronPriorGridGenerator9get_attrsEv) Returns attributes of this operation.


-
void set_attrs(
[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator.html#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator10AttributesE)attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator9set_attrsE10Attributes) Set the attributes of the operation

[ExperimentalDetectronPriorGridGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator).- Parameters:
**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator_1_1_attributes)to set.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v639ExperimentalDetectronPriorGridGenerator10AttributesE) *#include <experimental_detectron_prior_grid_generator.hpp>*Structure that specifies attributes of the operation.


-
ExperimentalDetectronPriorGridGenerator(const

-
class ExperimentalDetectronROIFeatureExtractor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractorE) *#include <experimental_detectron_roi_feature.hpp>*An operation

[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)is the ROIAlign operation applied over a feature pyramid.Public Functions

-
ExperimentalDetectronROIFeatureExtractor(const OutputVector &args, const
[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor.html#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor40ExperimentalDetectronROIFeatureExtractorERK12OutputVectorRK10Attributes) Constructs a

[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)operation.- Parameters:
**args**– Inputs of[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)**attrs**– Operation attributes



-
ExperimentalDetectronROIFeatureExtractor(const NodeVector &args, const
[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor.html#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor40ExperimentalDetectronROIFeatureExtractorERK10NodeVectorRK10Attributes) Constructs a

[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)operation.- Parameters:
**args**– Inputs of[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)**attrs**– Operation attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const
[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor.html#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v640ExperimentalDetectronROIFeatureExtractor9get_attrsEv) Returns attributes of the operation.


-
void set_attrs(
[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor.html#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE)attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor9set_attrsE10Attributes) Set the

[ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor)’s attributes.- Parameters:
**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor_1_1_attributes)to set.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v640ExperimentalDetectronROIFeatureExtractor10AttributesE) *#include <experimental_detectron_roi_feature.hpp>*Structure that specifies attributes of the operation.


-
ExperimentalDetectronROIFeatureExtractor(const OutputVector &args, const

-
class ExperimentalDetectronTopKROIs : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v629ExperimentalDetectronTopKROIsE) *#include <experimental_detectron_topkrois.hpp>*An operation

[ExperimentalDetectronTopKROIs](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_top_k_r_o_is), according to the repository is TopK operation applied to probabilities of input ROIs.Public Functions

-
ExperimentalDetectronTopKROIs(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &rois_probs, size_t max_rois = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v629ExperimentalDetectronTopKROIs29ExperimentalDetectronTopKROIsERK6OutputI4NodeERK6OutputI4NodeE6size_t) Constructs a

[ExperimentalDetectronTopKROIs](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_top_k_r_o_is)operation.- Parameters:
**input_rois**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)rois**rois_probs**– Probabilities for input rois**max_rois**– Maximal numbers of output rois



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v629ExperimentalDetectronTopKROIs24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ExperimentalDetectronTopKROIs(const

-
class ExtractImagePatches : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v319ExtractImagePatchesE) *#include <extractimagepatches.hpp>*[ExtractImagePatches](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_extract_image_patches)operation.Public Functions

-
ExtractImagePatches(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&sizes, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&rates, const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)&auto_pad)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v319ExtractImagePatches19ExtractImagePatchesERK6OutputI4NodeERK5ShapeRK7StridesRK5ShapeRK7PadType) Constructs a

[ExtractImagePatches](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_extract_image_patches)operation.- Parameters:
**data**– 4-D[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data to extract image patches**sizes**– Patch size in the format of [size_rows, size_cols]**strides**– Patch movement stride in the format of [stride_rows, stride_cols]**rates**– Element seleciton rate for creating a patch. in the format of [rate_rows, rate_cols]**auto_pad**– Padding type. it can be any value from valid, same_lower, same_upper



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v319ExtractImagePatches24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ExtractImagePatches(const

-
class Eye : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v93EyeE) *#include <eye.hpp>*Public Functions

-
Eye(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_rows, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_columns, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &diagonal_index, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &batch_shape, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&out_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v93Eye3EyeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKN2ov7element4TypeE) Constructs a

[Eye](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_eye)operation.- Parameters:


-
Eye(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_rows, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_columns, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &diagonal_index, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&out_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v93Eye3EyeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKN2ov7element4TypeE) Constructs a

[Eye](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_eye)operation without batch_shape.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v93Eye24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v93Eye12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Eye(const

-
class FakeConvert : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvertE) *#include <fake_convert.hpp>*[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)performs element-wise quantization of input values into a set of values corresponding to a target low-precision type.Note

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)is an experimental operation and subject to change.Public Functions

-
FakeConvert(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, std::string destination_type = "f8e4m3")[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert11FakeConvertERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEENSt6stringE) Constructs

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)operation (default shift).- Parameters:
**data**– The input data tensor.**scale**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with a scale factor for the data input.**destination_type**– The low precision type to be emulated.



-
FakeConvert(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &shift, std::string destination_type = "f8e4m3")[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert11FakeConvertERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEENSt6stringE) Constructs

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)operation.

-
FakeConvert(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&destination_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert11FakeConvertERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEERKN2ov7element4TypeE) Constructs

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)operation (default shift).- Parameters:
**data**– The input data tensor.**scale**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with a scale factor for the data input.**destination_type**– The low precision type to be emulated.



-
FakeConvert(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &shift, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&destination_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert11FakeConvertERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEERKN2ov6OutputIN2ov4NodeEEERKN2ov7element4TypeE) Constructs

[FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311FakeConvert24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1311FakeConvert12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
FakeConvert(const

-
class FakeQuantize : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012FakeQuantizeE) *#include <fake_quantize.hpp>*Class performing element-wise linear quantization.

Note

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)floating point values are quantized into a discrete set of floating point values.Public Functions

-
FakeQuantize(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_low, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_high, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_low, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_high, std::size_t levels, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012FakeQuantize12FakeQuantizeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERK17AutoBroadcastSpec) Constructs a

[FakeQuantize](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_fake_quantize)operation node.- Parameters:
**data**–**[in]**The input data tensor.**input_low**–**[in]**The minimum limit for input values.**input_high**–**[in]**The maximum limit for input values.**output_low**–**[in]**The minimum quantized value.**output_high**–**[in]**The maximum quantized value.**levels**–**[in]**The number of quantization levels.**auto_broadcast**–**[in]**AutoBroadcast mode to be used for broadcasting limit values



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012FakeQuantize24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v012FakeQuantize12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
FakeQuantize(const

-
class Floor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05FloorE) *#include <floor.hpp>*Elementwise floor operation.

Public Functions

-
Floor() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Floor5FloorEv) Constructs a floor operation.


-
Floor(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Floor5FloorERK6OutputI4NodeE) Constructs a floor operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v05Floor12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Floor() = default

-
class FloorMod : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18FloorModE) *#include <floor_mod.hpp>*Elementwise

[FloorMod](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_floor_mod)operation.Public Functions

-
inline FloorMod()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18FloorMod8FloorModEv) Constructs an uninitialized addition operation.


-
FloorMod(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18FloorMod8FloorModERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs an Floor

[Mod](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_mod)operation.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v18FloorMod12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline FloorMod()

-
class Gather : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[GatherBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_gather_base.html#_CPPv4N2ov2op4util10GatherBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16GatherE) *#include <gather.hpp>*[Gather](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_gather)slices from axis of data according to indices.

-
class Gather : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[GatherBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_gather_base.html#_CPPv4N2ov2op4util10GatherBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76GatherE) *#include <gather.hpp>*[Gather](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_gather)slices from axis of data according to indices.Public Functions

-
Gather(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const int64_t batch_dims = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Gather6GatherERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK7int64_t)

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v76Gather24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Gather(const

-
class Gather : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[GatherBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_gather_base.html#_CPPv4N2ov2op4util10GatherBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v86GatherE) *#include <gather.hpp>*[Gather](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_gather)slices from axis of data according to indices. Negative indices are supported and indicate reverse indexing from the end.Subclassed by

[ov::op::internal::GatherCompressed](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_gather_compressed)Public Functions

-
Gather(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const int64_t batch_dims = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v86Gather6GatherERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK7int64_t) - Parameters:
**data**– The tensor from which slices are gathered**indices**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)with indexes to gather**axis**– The tensor is a dimension index to gather data from**batch_dims**– The number of batch dimension in data and indices tensors.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v86Gather24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Gather(const

-
class GatherElements : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v614GatherElementsE) *#include <gather_elements.hpp>*[GatherElements](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_gather_elements)operation.Public Functions

-
GatherElements(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const int64_t axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v614GatherElements14GatherElementsERK6OutputI4NodeERK6OutputI4NodeEK7int64_t) Constructs a

[GatherElements](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_gather_elements)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v614GatherElements24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GatherElements(const

-
class GatherND : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[GatherNDBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_gather_n_d_base.html#_CPPv4N2ov2op4util12GatherNDBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v58GatherNDE) *#include <gather_nd.hpp>*[GatherND](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_gather_n_d)operation.Public Functions

-
GatherND(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const size_t batch_dims = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v58GatherND8GatherNDERK6OutputI4NodeERK6OutputI4NodeEK6size_t) Constructs a

[GatherND](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_gather_n_d)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v58GatherND24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GatherND(const

-
class GatherND : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[GatherNDBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_gather_n_d_base.html#_CPPv4N2ov2op4util12GatherNDBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88GatherNDE) *#include <gather_nd.hpp>*[GatherND](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_gather_n_d)operation.Public Functions

-
GatherND(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const size_t batch_dims = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88GatherND8GatherNDERK6OutputI4NodeERK6OutputI4NodeEK6size_t) Constructs a

[GatherND](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_gather_n_d)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88GatherND24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GatherND(const

-
class GatherTree : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110GatherTreeE) *#include <gather_tree.hpp>*Generates the complete beams from the ids per each step and the parent beam ids.

Public Functions

-
GatherTree(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step_ids, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &parent_idx, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_seq_len, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &end_token)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110GatherTree10GatherTreeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) - Parameters:
**step_ids**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape [MAX_TIME, BATCH_SIZE, BEAM_WIDTH] with indices from per each step**parent_idx**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape [MAX_TIME, BATCH_SIZE, BEAM_WIDTH] with parent beam indices**max_seq_len**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape [BATCH_SIZE] with maximum lengths for each sequence in the batch**end_token**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)of shape [MAX_TIME, BATCH_SIZE, BEAM_WIDTH]



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110GatherTree24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GatherTree(const

-
class Gelu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04GeluE) *#include <gelu.hpp>*Gaussian Error Linear Unit f(x) = 0.5 * x * (1 + erf( x / sqrt(2) )

Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Gelu24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override

-
class Gelu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74GeluE) *#include <gelu.hpp>*Gaussian Error Linear Unit f(x) = 0.5 * x * (1 + erf( x / sqrt(2) ) for “approximation” = “erf” f(x) = 0.5 * x * (1 + tanh([sqrt(2 / pi)] * [x + 0.044715^3]) for “approximation” = “tanh”.

Public Functions

-
Gelu(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data,[GeluApproximationMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op21GeluApproximationModeE)mode =[GeluApproximationMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op21GeluApproximationModeE)::[ERF](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op21GeluApproximationMode3ERFE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74Gelu4GeluERK6OutputI4NodeE21GeluApproximationMode) Constructs a

[Gelu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_gelu)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor**mode**– Approximation mode



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74Gelu24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v74Gelu12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Gelu(const

-
class Greater : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseComparison](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_comparison.html#_CPPv4N2ov2op4util27BinaryElementwiseComparisonE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17GreaterE) *#include <greater.hpp>*Elementwise greater-than operation.

Public Functions

-
inline Greater()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Greater7GreaterEv) Constructs a greater-than operation.


-
Greater(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Greater7GreaterERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a greater-than operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Greater12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Greater()

-
class GreaterEqual : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseComparison](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_comparison.html#_CPPv4N2ov2op4util27BinaryElementwiseComparisonE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112GreaterEqualE) *#include <greater_eq.hpp>*Elementwise greater-than-or-equal operation.

Public Functions

-
inline GreaterEqual()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112GreaterEqual12GreaterEqualEv) Constructs a greater-than-or-equal operation.


-
GreaterEqual(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112GreaterEqual12GreaterEqualERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a greater-than-or-equal operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v112GreaterEqual12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline GreaterEqual()

-
class GridSample : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v910GridSampleE) *#include <grid_sample.hpp>*Operator performing interpolated sampling of the input tensor.

Public Functions

-
GridSample(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &grid, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v9_1_1_grid_sample_1_1_attributes.html#_CPPv4N2ov2op2v910GridSample10AttributesE)&attributes)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v910GridSample10GridSampleERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[GridSample](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_grid_sample)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data tensor (input image)**grid**– Normalized interpolation coordinates**attrs**–[GridSample](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_grid_sample)attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v910GridSample24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v910GridSample12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v910GridSample10AttributesE) *#include <grid_sample.hpp>*A Structure which contains all

[GridSample](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_grid_sample)attributes.

-
GridSample(const

-
class GroupNormalization : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1218GroupNormalizationE) *#include <group_normalization.hpp>*[GroupNormalization](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v12_1_1_group_normalization)operation over the input tensor.Public Functions

-
GroupNormalization(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scale, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &bias, int64_t num_groups, double epsilon)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1218GroupNormalization18GroupNormalizationERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7int64_td) - Parameters:
**data**– The input tensor to be normalized**scale**– The tensor containing scale values for each channel**bias**– The tensor containing bias values for each channel**num_groups**– The number of groups that the channel dimension will be divided into**epsilon**– The value that prevents divisions by zero in[GroupNormalization](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v12_1_1_group_normalization)formula



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1218GroupNormalization24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GroupNormalization(const

-
class GRUCell : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCellE) *#include <gru_cell.hpp>*Class for GRU cell node.

Note

Note this class represents only single

*cell*and not whole GRU*layer*.Public Functions

-
GRUCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCell7GRUCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tE) Constructs

[GRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_g_r_u_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [gates_count * hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [gates_count * hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.



-
GRUCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size, const std::vector<std::string> &activations, const std::vector<float> &activations_alpha, const std::vector<float> &activations_beta, float clip, bool linear_before_reset)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCell7GRUCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[GRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_g_r_u_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [gates_count * hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [gates_count * hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.



-
GRUCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, std::size_t hidden_size, const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f, bool linear_before_reset = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCell7GRUCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[GRUCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_g_r_u_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [gates_count * hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [gates_count * hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**B**–**[in]**The sum of biases (weight and recurrence) for update, reset and hidden gates. If linear_before_reset := true then biases for hidden gates are placed separately (weight and recurrence).[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape): [gates_count * hidden_size] if linear_before_reset := false[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape): [(gates_count + 1) * hidden_size] if linear_before_reset := true**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**linear_before_reset**–**[in]**Whether or not to apply the linear transformation before multiplying by the output of the reset gate.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37GRUCell24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
GRUCell(const

-
class GRUSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v511GRUSequenceE) *#include <gru_sequence.hpp>*[GRUSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_g_r_u_sequence)operation.Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v511GRUSequence24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override

-
class HardSigmoid : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011HardSigmoidE) *#include <hard_sigmoid.hpp>*Parameterized, bounded sigmoid-like, piecewise linear function. min(max(alpha*x + beta, 0), 1)

Public Functions

-
HardSigmoid(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &alpha, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &beta)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011HardSigmoid11HardSigmoidERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[HardSigmoid](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_hard_sigmoid)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor.**alpha**–**[in]**A scalar value representing the alpha parameter.**beta**–**[in]**A scalar value representing the beta parameter.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011HardSigmoid24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
HardSigmoid(const

-
class HSigmoid : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v58HSigmoidE) *#include <hsigmoid.hpp>*A

[HSigmoid](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_h_sigmoid)Activation Function f(x) = min(max(x + 3, 0), 6) / 6 or f(x) = min(ReLU(x + 3), 6) / 6.

-
class HSwish : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v46HSwishE) *#include <hswish.hpp>*A

[HSwish](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_h_swish)Activation Function f(x) = x * min(max(x + 3, 0), 6) / 6 or f(x) = x * min(ReLU(x + 3), 6) / 6.

-
class I420toBGR : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvertColorI420Base](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convert_color_i420_base.html#_CPPv4N2ov2op4util20ConvertColorI420BaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89I420toBGRE) *#include <i420_to_bgr.hpp>*Color conversion operation from I420 to BGR format.

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input):[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)NV12 image can be represented in two ways: a) Single plane (as it is in the file): I420 height dimension is 1.5x bigger than image height. ‘C’ dimension shall be 1. b) Three separate planes (used this way in many physical video sources): Y, U and V. In this case b1) Y plane has height same as image height. ‘C’ dimension equals to 1 b2) U plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 1. b3) V plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 1.Supported element types: u8 or any supported floating-point type.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output):[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node will have NHWC layout and shape HxW same as image spatial dimensions.Number of output channels ‘C’ will be 3, as per interleaved BGR format, first channel is B, last is R

Conversion of each pixel from I420 (YUV) to RGB space is represented by following formulas: R = 1.164 * (Y - 16) + 1.596 * (V - 128) G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128) B = 1.164 * (Y - 16) + 2.018 * (U - 128) Then R, G, B values are clipped to range (0, 255)


Public Functions

-
explicit I420toBGR(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89I420toBGR9I420toBGRERK6OutputI4NodeE) Constructs a conversion operation from input image in I420 format As per I420 format definition, node height dimension shall be 1.5 times bigger than image height so that image (w=640, h=480) is represented by NHWC shape {N,720,640,1} (height*1.5 x width)


-
explicit I420toBGR(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_y, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_u, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_v)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89I420toBGR9I420toBGRERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a conversion operation from 2-plane input image in NV12 format In general case Y channel of image can be separated from UV channel which means that operation needs two nodes for Y and UV planes respectively. Y plane has one channel, and UV has 2 channels, both expect ‘NHWC’ layout.

- Parameters:
**arg_y**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for Y plane (NHWC layout). Shall have WxH dimensions equal to image dimensions. ‘C’ dimension equals to 1.**arg_u**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for U plane (NHWC layout). ‘H’ is half of image height, ‘W’ is half of image width, ‘C’ dimension equals to 1.**arg_v**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for V plane (NHWC layout). ‘H’ is half of image height, ‘W’ is half of image width, ‘C’ dimension equals to 1.




-
class I420toRGB : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvertColorI420Base](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convert_color_i420_base.html#_CPPv4N2ov2op4util20ConvertColorI420BaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89I420toRGBE) *#include <i420_to_rgb.hpp>*Color conversion operation from I420 to RGB format.

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input):[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)NV12 image can be represented in two ways: a) Single plane (as it is in the file): I420 height dimension is 1.5x bigger than image height. ‘C’ dimension shall be 1. b) Three separate planes (used this way in many physical video sources): Y, U and V. In this case b1) Y plane has height same as image height. ‘C’ dimension equals to 1 b2) U plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 1. b3) V plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 1.Supported element types: u8 or any supported floating-point type.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output):[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node will have NHWC layout and shape HxW same as image spatial dimensions.Number of output channels ‘C’ will be 3, as per interleaved RGB format, first channel is R, last is B

Conversion of each pixel from I420 (YUV) to RGB space is represented by following formulas: R = 1.164 * (Y - 16) + 1.596 * (V - 128) G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128) B = 1.164 * (Y - 16) + 2.018 * (U - 128) Then R, G, B values are clipped to range (0, 255)


Public Functions

-
explicit I420toRGB(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89I420toRGB9I420toRGBERK6OutputI4NodeE) Constructs a conversion operation from input image in I420 format As per I420 format definition, node height dimension shall be 1.5 times bigger than image height so that image (w=640, h=480) is represented by NHWC shape {N,720,640,1} (height*1.5 x width)


-
explicit I420toRGB(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_y, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_u, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_v)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89I420toRGB9I420toRGBERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a conversion operation from 2-plane input image in NV12 format In general case Y channel of image can be separated from UV channel which means that operation needs two nodes for Y and UV planes respectively. Y plane has one channel, and UV has 2 channels, both expect ‘NHWC’ layout.

- Parameters:
**arg_y**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for Y plane (NHWC layout). Shall have WxH dimensions equal to image dimensions. ‘C’ dimension equals to 1.**arg_u**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for U plane (NHWC layout). ‘H’ is half of image height, ‘W’ is half of image width, ‘C’ dimension equals to 1.**arg_v**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for V plane (NHWC layout). ‘H’ is half of image height, ‘W’ is half of image width, ‘C’ dimension equals to 1.




-
class Identity : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v168IdentityE) *#include <identity.hpp>*[Identity](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_identity)operation is used as a placeholder op.Public Functions

-
Identity(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v168Identity8IdentityERK6OutputI4NodeE) [Identity](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_identity)operation is used as a placeholder. It copies the tensor data to the output.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v168Identity24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Identity(const

-
class IDFT : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[FFTBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_f_f_t_base.html#_CPPv4N2ov2op4util7FFTBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74IDFTE) *#include <idft.hpp>*An operation

[IDFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_i_d_f_t)that computes the inverse discrete Fourier transformation.

-
class If : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MultiSubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_multi_sub_graph_op.html#_CPPv4N2ov2op4util15MultiSubGraphOpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v82IfE) *#include <if.hpp>*[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)operation.Public Functions

-
If(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &execution_condition)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v82If2IfERK6OutputI4NodeE) Constructs

[If](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_if)with condition.- Parameters:
**execution_condition**– condition node.


-
inline const std::shared_ptr<
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> &get_then_body() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v82If13get_then_bodyEv) gets then_body as

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).- Returns:
then_body as

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).


-
inline const std::shared_ptr<
[Model](https://docs.openvino.ai/classov_1_1_model.html#_CPPv4N2ov5ModelE)> &get_else_body() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v82If13get_else_bodyEv) gets else_body as

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).- Returns:
else_body as

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model).


sets new

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)as new then_body.- Parameters:
**body**– new body for ‘then’ branch.


sets new

[ov::Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)as new else_body.- Parameters:
**body**– new body for ‘else’ branch.


sets new input to the operation associated with parameters of each sub-graphs

- Parameters:
**value**– input to operation**then_parameter**– parameter for then_body or nullptr**else_parameter**– parameter for else_body or nullpt



sets new output from the operation associated with results of each sub-graphs

- Parameters:
**then_result**– result from then_body**else_parameter**– result from else_body

- Returns:
output from operation



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v82If24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
If(const

-
class Interpolate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011InterpolateE) *#include <interpolate.hpp>*Layer which performs bilinear interpolation.

Public Functions

-
Interpolate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_shape, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_interpolate_1_1_attributes.html#_CPPv4N2ov2op2v011Interpolate10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011Interpolate11InterpolateERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_interpolate)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011Interpolate24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011Interpolate10AttributesE) *#include <interpolate.hpp>*Structure that specifies attributes for interpolation.


-
Interpolate(const

-
class Interpolate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[InterpolateBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_interpolate_base.html#_CPPv4N2ov2op4util15InterpolateBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v411InterpolateE) *#include <interpolate.hpp>*[Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_interpolate)operation.Public Functions

-
Interpolate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scales, const InterpolateAttrs &attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v411Interpolate11InterpolateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK16InterpolateAttrs) Constructs a

[Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_interpolate)operation without ‘axes’ input.

-
Interpolate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &output_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scales, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes, const InterpolateAttrs &attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v411Interpolate11InterpolateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK16InterpolateAttrs) Constructs a

[Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_interpolate)operation with ‘axes’ input.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v411Interpolate24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v411Interpolate12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Interpolate(const

-
class Interpolate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[InterpolateBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_interpolate_base.html#_CPPv4N2ov2op4util15InterpolateBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1111InterpolateE) *#include <interpolate.hpp>*[Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_interpolate)operation.Public Functions

-
Interpolate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scales_or_sizes, const InterpolateAttrs &attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1111Interpolate11InterpolateERK6OutputI4NodeERK6OutputI4NodeERK16InterpolateAttrs) Constructs a

[Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_interpolate)operation without ‘axes’ input.- Parameters:
**image**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)image**scales_or_sizes**– Scales of spatial axes, i.e. output_shape / input_shape**attrs**– Interpolation attributes



-
Interpolate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scales_or_sizes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes, const InterpolateAttrs &attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1111Interpolate11InterpolateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK16InterpolateAttrs) Constructs a

[Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_interpolate)operation with ‘axes’ input.- Parameters:
**image**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)image**scales_or_sizes**– Scales of spatial axes, i.e. output_shape / input_shape**axes**– Interpolation axes**attrs**– Interpolation attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1111Interpolate24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1111Interpolate12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Interpolate(const

-
class Inverse : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147InverseE) *#include <inverse.hpp>*[Inverse](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_inverse)operation computes the inverse of the input tensor.Public Functions

-
Inverse(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const bool adjoint = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147Inverse7InverseERK6OutputI4NodeEKb) [Inverse](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_inverse)operation computes the inverse of the input matrices. The inverse is computed for each MxM matrix separetely, preserving all batch dimensions.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)matrices to compute the inverse for. Last two tensor dimensions must be of the same size.**adjoint**– Boolean that determines whether to return a normal inverse or adjoint (conjugate transpose) of the input matrices.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147Inverse24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Inverse(const

-
class IsFinite : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v108IsFiniteE) *#include <is_finite.hpp>*Boolean mask that maps NaN and Infinity values to false and other values to true.

Public Functions

-
IsFinite(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v108IsFinite8IsFiniteERK6OutputI4NodeE) Constructs a

[IsFinite](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_is_finite)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data tensor


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v108IsFinite24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
IsFinite(const

-
class IsInf : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsInfE) *#include <is_inf.hpp>*Boolean mask that maps infinite values to true.

Public Functions

-
IsInf(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Attributes](https://docs.openvino.ai/classov_1_1op_1_1v10_1_1_is_inf.html#_CPPv4N2ov2op3v105IsInf10AttributesE)&attributes)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsInf5IsInfERK6OutputI4NodeERK10Attributes) Constructs a

[IsInf](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_is_inf)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsInf24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
IsInf(const

-
class IsNaN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsNaNE) *#include <is_nan.hpp>*Boolean mask that maps NaN values to true and other values to false.

Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v105IsNaN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override

-
class ISTFT : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v165ISTFTE) *#include <istft.hpp>*An operation

[ISTFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_i_s_t_f_t)that computes the Inverse Short Time Fourier Transform.Public Functions

-
ISTFT(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &window, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &frame_size, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &frame_step, const bool center, const bool normalized)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v165ISTFT5ISTFTERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKbKb) Constructs an

[ISTFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_i_s_t_f_t)operation with signal length to be inferred.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**window**– Window values applied in[ISTFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_i_s_t_f_t)**frame_size**– Scalar value representing the size of Fourier Transform**frame_step**– The distance (number of samples) between successive window frames**center**– Flag signaling if the signal input has been padded before STFT**normalized**– Flag signaling if the STFT result has been normalized



-
ISTFT(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &window, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &frame_size, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &frame_step, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &signal_length, const bool center, const bool normalized)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v165ISTFT5ISTFTERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKbKb) Constructs an

[ISTFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_i_s_t_f_t)operation with signal length provided.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**window**– Window values applied in[ISTFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_i_s_t_f_t)**frame_size**– Scalar value representing the size of Fourier Transform**frame_step**– The distance (number of samples) between successive window frames**signal_length**– The signal length of the original signal**center**– Flag signaling if the signal input has been padded before STFT**normalized**– Flag signaling if the STFT result has been normalized



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v165ISTFT24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ISTFT(const

-
class Less : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseComparison](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_comparison.html#_CPPv4N2ov2op4util27BinaryElementwiseComparisonE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v14LessE) *#include <less.hpp>*Elementwise less-than operation.

Public Functions

-
inline Less()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v14Less4LessEv) Constructs a less-than operation.


-
Less(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v14Less4LessERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a less-than operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v14Less12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Less()

-
class LessEqual : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseComparison](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_comparison.html#_CPPv4N2ov2op4util27BinaryElementwiseComparisonE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19LessEqualE) *#include <less_eq.hpp>*Elementwise less-than-or-equal operation.

Public Functions

-
inline LessEqual()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19LessEqual9LessEqualEv) Constructs a less-than-or-equal operation.


-
LessEqual(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19LessEqual9LessEqualERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a less-than-or-equal operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19LessEqual12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline LessEqual()

-
class Log : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03LogE) *#include <log.hpp>*Elementwise natural log operation.

Public Functions

-
Log() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Log3LogEv) Constructs a natural log operation.


-
Log(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Log3LogERK6OutputI4NodeE) Constructs a natural log operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Log12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Log() = default

-
class LogSoftmax : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v510LogSoftmaxE) *#include <log_softmax.hpp>*[LogSoftmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_log_softmax)operation.Public Functions

-
LogSoftmax(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const int64_t axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v510LogSoftmax10LogSoftmaxERK6OutputI4NodeEK7int64_t) Constructs a

[LogSoftmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_log_softmax)operation.[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the first input tensor.`[d0, ...]`

**axis**– The axis position (0-based) on which to calculate the[LogSoftmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_log_softmax).



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v510LogSoftmax24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
LogSoftmax(const

-
class LogicalAnd : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseLogical](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_logical.html#_CPPv4N2ov2op4util24BinaryElementwiseLogicalE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalAndE) *#include <logical_and.hpp>*Elementwise logical-and operation.

Public Functions

-
LogicalAnd() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalAnd10LogicalAndEv) Constructs a logical-and operation.


-
LogicalAnd(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalAnd10LogicalAndERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a logical-and operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v110LogicalAnd12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
LogicalAnd() = default

-
class LogicalNot : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalNotE) *#include <logical_not.hpp>*Elementwise logical negation operation.

Public Functions

-
LogicalNot() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalNot10LogicalNotEv) Constructs a logical negation operation.


-
LogicalNot(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalNot10LogicalNotERK6OutputI4NodeE) Constructs a logical negation operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalNot24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v110LogicalNot12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
LogicalNot() = default

-
class LogicalOr : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseLogical](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_logical.html#_CPPv4N2ov2op4util24BinaryElementwiseLogicalE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19LogicalOrE) *#include <logical_or.hpp>*Elementwise logical-or operation.

Public Functions

-
LogicalOr(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19LogicalOr9LogicalOrERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a logical-or operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19LogicalOr12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
LogicalOr(const

-
class LogicalXor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseLogical](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_logical.html#_CPPv4N2ov2op4util24BinaryElementwiseLogicalE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalXorE) *#include <logical_xor.hpp>*Elementwise logical-xor operation.

Public Functions

-
LogicalXor(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110LogicalXor10LogicalXorERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a logical-xor operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v110LogicalXor12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
LogicalXor(const

-
class Loop : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[SubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_sub_graph_op.html#_CPPv4N2ov2op4util10SubGraphOpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54LoopE) *#include <loop.hpp>*Iterate a body over tensors, accumulating into tensors.

Public Functions

-
Loop(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &trip_count, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &execution_condition)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54Loop4LoopERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[Loop](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_loop)operation.

-
virtual
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> get_concatenated_slices(const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &value, int64_t start, int64_t stride, int64_t part_size, int64_t end, int64_t axis) override[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54Loop23get_concatenated_slicesERK6OutputI4NodeE7int64_t7int64_t7int64_t7int64_t7int64_t) Concatenates slices from all iterations.

- Parameters:
**value**– The value supplying slice values from each iteration.**start**– First index on axis of the slicing**stride**– Stepping of the slice**part_size**– Size of the slice on axis**end**– The last index on axis of the slicing**axis**– The axis to slice along

- Returns:
The concatenated slices.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54Loop24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v54Loop8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v54Loop12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
struct SpecialBodyPorts
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v54Loop16SpecialBodyPortsE) *#include <loop.hpp>*Allows to define the purpose of inputs/outputs in the body.


-
Loop(const

-
class LRN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03LRNE) *#include <lrn.hpp>*Elementwise Local Response Normalization (

[LRN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_r_n)) operation.*Inputs*Type

Description

`arg`

\(N[n, c, d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and numeric element type.

Type

Description

\(N[n, c, d_1,\dots,d_n]\)

The tensor \(T\), where \(T[n, c, d_1,\dots,d_n] = \frac{N[n,i,d_1,\dots,d_n]}{ (bias + alpha * (\sum_{i=max(0,(nsize-1)/2)}^{min(C, (nsize-1)/2)+1} N[n,i,d_1,\dots,d_n]^{2}) ^ {2})}\)

Public Functions

-
LRN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, double alpha, double beta, double bias, size_t size)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03LRN3LRNERK6OutputI4NodeEddd6size_t) Constructs a

[LRN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_r_n)operation.- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03LRN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
LRN(const

-
class LSTMCell : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCellE) *#include <lstm_cell.hpp>*Class for single lstm cell node.

See also

LSTMSequence,

[RNNCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_n_n_cell), GRUCellNote

Following implementation supports:

`peepholes`

Gers & Schmidhuber (2000)[https://ieeexplore.ieee.org/document/861302](https://ieeexplore.ieee.org/document/861302)Coupling input and forget gates.


Note

It calculates following equations:

it = f(Xt*(Wi^T) + Ht-1*(Ri^T) + Pi (.) Ct-1 + Wbi + Rbi) ft = f(Xt*(Wf^T) + Ht-1*(Rf^T) + Pf (.) Ct-1 + Wbf + Rbf) ct = g(Xt*(Wc^T) + Ht-1*(Rc^T) + Wbc + Rbc) Ct = ft (.) Ct-1 + it (.) ct ot = f(Xt*(Wo^T) + Ht-1*(Ro^T) + Po (.) Ct + Wbo + Rbo) Ht = ot (.) h(Ct) * - Is a dot product, (.) - is a Hadamard product (element-wise), f, g, h - are activation functions.

Note

This class represents only single

*cell*(for current time step) and not the whole LSTM Sequence layerPublic Functions

-
LSTMCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_cell_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size,[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)weights_format =[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)::[IFCO](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormat4IFCOE), const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f, bool input_forget = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCell8LSTMCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tE17LSTMWeightsFormatRKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**initial_cell_state**–**[in]**The cell state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The gate weights tensor with shape: [4*hidden_size, input_size].**R**–**[in]**The recurrence weights tensor with shape: [4*hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**weights_format**–**[in]**The order of gates in weights tensors. The default format is IFCO since it is used by DNNL.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**input_forget**–**[in]**Controls coupling input and forget gates.



-
LSTMCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_cell_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, std::size_t hidden_size,[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)weights_format =[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)::[IFCO](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormat4IFCOE), const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f, bool input_forget = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCell8LSTMCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tE17LSTMWeightsFormatRKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**initial_cell_state**–**[in]**The cell state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [4*hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [4*hidden_size, hidden_size].**B**–**[in]**The bias tensor for gates with shape: [4*hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**weights_format**–**[in]**The order of gates in weights tensors. The default format is IFCO since it is used by DNNL.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**input_forget**–**[in]**Controls coupling input and forget gates.



-
LSTMCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_cell_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &P, std::size_t hidden_size,[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)weights_format =[LSTMWeightsFormat](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormatE)::[IFCO](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17LSTMWeightsFormat4IFCOE), const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f, bool input_forget = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCell8LSTMCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tE17LSTMWeightsFormatRKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEfb) Constructs

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**initial_cell_state**–**[in]**The cell state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [4*hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [4*hidden_size, hidden_size].**B**–**[in]**The bias tensor for gates with shape: [4*hidden_size].**P**–**[in]**The weight tensor for peepholes with shape: [3*hidden_size] - 3 equals to only iof gates. The order is: input, output, forget gates.**hidden_size**–**[in]**The number of hidden units for recurrent cell.**weights_format**–**[in]**The order of gates in weights tensors. The default format is IFCO since it is used by DNNL.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.**input_forget**–**[in]**Controls coupling input and forget gates.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08LSTMCell24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.



-
class LSTMCell : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48LSTMCellE) *#include <lstm_cell.hpp>*Class for single lstm cell node.

See also

LSTMSequence, RNNCell, GRUCell

Note

Following implementation supports:

`peepholes`

Gers & Schmidhuber (2000)[https://ieeexplore.ieee.org/document/861302](https://ieeexplore.ieee.org/document/861302)Coupling input and forget gates.


Note

It calculates following equations:

it = f(Xt*(Wi^T) + Ht-1*(Ri^T) + Wbi + Rbi) ft = f(Xt*(Wf^T) + Ht-1*(Rf^T) + Wbf + Rbf) ct = g(Xt*(Wc^T) + Ht-1*(Rc^T) + Wbc + Rbc) Ct = ft (.) Ct-1 + it (.) ct ot = f(Xt*(Wo^T) + Ht-1*(Ro^T) + Wbo + Rbo) Ht = ot (.) h(Ct) * - Is a dot product, (.) - is a Hadamard product (element-wise), f, g, h - are activation functions.

Note

This class represents only single

*cell*(for current time step) and not the whole LSTM Sequence layerPublic Functions

-
LSTMCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_cell_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size, const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48LSTMCell8LSTMCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEf) Constructs

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_l_s_t_m_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**initial_cell_state**–**[in]**The cell state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The gate weights tensor with shape: [4*hidden_size, input_size].**R**–**[in]**The recurrence weights tensor with shape: [4*hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.



-
LSTMCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_cell_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, std::size_t hidden_size, const std::vector<std::string> &activations = std::vector<std::string>{"sigmoid", "tanh", "tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48LSTMCell8LSTMCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEf) Constructs

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_l_s_t_m_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**initial_cell_state**–**[in]**The cell state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [4*hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [4*hidden_size, hidden_size].**B**–**[in]**The bias tensor for gates with shape: [4*hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48LSTMCell24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.



-
class LSTMSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v512LSTMSequenceE) *#include <lstm_sequence.hpp>*Class for lstm sequence node.

See also

LSTMCell, RNNCell, GRUCell

Note

It follows notation and equations defined as in ONNX standard:

[onnx/onnx](https://github.com/onnx/onnx/blob/master/docs/Operators.md#LSTM)Public Functions

-
inline virtual size_t get_default_output_index() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v512LSTMSequence24get_default_output_indexEv) Returns the output of the default output, or throws if there is none.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v512LSTMSequence24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual size_t get_default_output_index() const override

-
class MatMul : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06MatMulE) *#include <matmul.hpp>*Operator performing Matrix Multiplication.

Public Functions

-
MatMul(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &A, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, const bool &transpose_a = false, const bool &transpose_b = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06MatMul6MatMulERK6OutputI4NodeERK6OutputI4NodeERKbRKb) Constructs an Matrix Multiplication operation.

- Parameters:
**A**– Matrix A**B**– Matrix B**transpose_a**– If matrix A should be transposed.**transpose_b**– If matrix B should be transposed.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06MatMul24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06MatMul12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
MatMul(const

-
class MatrixNms : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNmsE) *#include <matrix_nms.hpp>*[MatrixNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_matrix_nms)operation.Public Functions

-
MatrixNms() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNms9MatrixNmsEv) Constructs a conversion operation.


-
MatrixNms(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v8_1_1_matrix_nms_1_1_attributes.html#_CPPv4N2ov2op2v89MatrixNms10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNms9MatrixNmsERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[MatrixNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_matrix_nms)operation.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v8_1_1_matrix_nms_1_1_attributes)of the operation



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNms24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline const
[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v8_1_1_matrix_nms_1_1_attributes.html#_CPPv4N2ov2op2v89MatrixNms10AttributesE)&get_attrs() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v89MatrixNms9get_attrsEv) Returns attributes of the operation

[MatrixNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_matrix_nms).

-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89MatrixNms10AttributesE) *#include <matrix_nms.hpp>*Structure that specifies attributes of the operation.


-
MatrixNms() = default

-
class MaxPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MaxPoolBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_max_pool_base.html#_CPPv4N2ov2op4util11MaxPoolBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17MaxPoolE) *#include <max_pool.hpp>*Batched max pooling operation.

Public Functions

-
MaxPool() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17MaxPool7MaxPoolEv) Constructs a batched max pooling operation.


-
MaxPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, const[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)auto_pad =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17MaxPool7MaxPoolERK6OutputI4NodeERK7StridesRK5ShapeRK5ShapeRK5ShapeKN2op12RoundingTypeEK7PadType) Constructs a batched max pooling operation.

- Parameters:
**arg**– The node producing the input data batch tensor.**strides**– The strides.**pads_begin**– The beginning of padding shape.**pads_end**– The end of padding shape.**kernel**– The kernel shape.**rounding_type**– Whether to use ceiling or floor rounding type while computing output shape.**auto_pad**– The pad type for automatically computing padding sizes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17MaxPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17MaxPool12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
MaxPool() = default

-
class MaxPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MaxPoolBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_max_pool_base.html#_CPPv4N2ov2op4util11MaxPoolBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87MaxPoolE) *#include <max_pool.hpp>*MaxPooling operation with values and indices calculated as individual outputs.

Public Functions

-
MaxPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, const[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)auto_pad =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E), const int64_t axis = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87MaxPool7MaxPoolERK6OutputI4NodeERK7StridesRK7StridesRK5ShapeRK5ShapeRK5ShapeKN2op12RoundingTypeEK7PadTypeKN7element4TypeEK7int64_t) Constructs a parametrized

[MaxPool](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_max_pool)operation.- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)of a node producing the feature tensor to be pooled.**strides**– The strides of the pooling filter.**dilations**– The dilations of the pooling filter.**pads_begin**– Paddings at the beginning of each spatial axis.**pads_end**– Paddings at the end of each spatial axis.**kernel**– The kernel shape.**rounding_type**– Whether to use ceiling or floor rounding type while computing the output shape.**auto_pad**– The pad type for automatic calculation of the padding sizes.**index_element_type**– The data type used by the second output tensor containing the selected indices.**axis**– Indicates a dimension in the input data shape which should be used as a starting point for calculation of the upper bound of allowed values of the indices output.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87MaxPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)get_index_element_type() const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v87MaxPool22get_index_element_typeEv) - Returns:
The data type of the second output tensor (indices).



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v87MaxPool12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
MaxPool(const

-
class MaxPool : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[MaxPoolBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_max_pool_base.html#_CPPv4N2ov2op4util11MaxPoolBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147MaxPoolE) *#include <max_pool.hpp>*MaxPooling operation with values and indices calculated as individual outputs.

Public Functions

-
MaxPool(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&strides, const[Strides](https://docs.openvino.ai/classov_1_1_strides.html#_CPPv4N2ov7StridesE)&dilations, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_begin, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&pads_end, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&kernel, const[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)rounding_type =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[RoundingType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingTypeE)::[FLOOR](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12RoundingType5FLOORE), const[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)auto_pad =[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PadType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadTypeE)::[EXPLICIT](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadType8EXPLICITE), const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E), const int64_t axis = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147MaxPool7MaxPoolERK6OutputI4NodeERK7StridesRK7StridesRK5ShapeRK5ShapeRK5ShapeKN2op12RoundingTypeEK7PadTypeKN7element4TypeEK7int64_t) Constructs a parametrized

[MaxPool](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_max_pool)operation.- Parameters:
**arg**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)of a node producing the feature tensor to be pooled.**strides**– The strides of the pooling filter.**dilations**– The dilations of the pooling filter.**pads_begin**– Paddings at the beginning of each spatial axis.**pads_end**– Paddings at the end of each spatial axis.**kernel**– The kernel shape.**rounding_type**– Whether to use ceiling or floor rounding type while computing the output shape.**auto_pad**– The pad type for automatic calculation of the padding sizes.**index_element_type**– The data type used by the second output tensor containing the selected indices.**axis**– Indicates a dimension in the input data shape which should be used as a starting point for calculation of the upper bound of allowed values of the indices output.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v147MaxPool24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)get_index_element_type() const noexcept[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v147MaxPool22get_index_element_typeEv) - Returns:
The data type of the second output tensor (indices).



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v147MaxPool12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
MaxPool(const

-
class Maximum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17MaximumE) *#include <maximum.hpp>*Elementwise maximum operation.

Public Functions

-
inline Maximum()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Maximum7MaximumEv) Constructs a maximum operation.


-
Maximum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Maximum7MaximumERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a maximum operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Maximum12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Maximum()

-
class Minimum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17MinimumE) *#include <minimum.hpp>*Elementwise minimum operation.

Public Functions

-
inline Minimum()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Minimum7MinimumEv) Constructs a minimum operation.


-
Minimum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Minimum7MinimumERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a minimum operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Minimum12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Minimum()

-
class Mish : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v44MishE) *#include <mish.hpp>*A Self Regularized Non-Monotonic Neural Activation Function f(x) = x * tanh(log(exp(x) + 1.))

Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v44Mish24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v44Mish12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual void validate_and_infer_types() override

-
class Mod : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13ModE) *#include <mod.hpp>*[Mod](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_mod)returns an element-wise division reminder with two given tensors applying multi-directional broadcast rules.Public Functions

-
Mod(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &A, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Mod3ModERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) - Parameters:
**A**– - Dividend tensor**B**– - Divisor tensor**auto_broadcast**– Auto broadcast specification



-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Mod8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Mod12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Mod(const

-
class Multinomial : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311MultinomialE) *#include <multinomial.hpp>*[Multinomial](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_multinomial)operation creates a sequence of indices of classes sampled from the multinomial distribution.Public Functions

-
Multinomial(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_samples, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type_t](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element6Type_tE)convert_type, const bool with_replacement, const bool log_probs, const uint64_t global_seed = 0, const uint64_t op_seed = 0)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311Multinomial11MultinomialERK6OutputI4NodeERK6OutputI4NodeEKN2ov7element6Type_tEKbKbK8uint64_tK8uint64_t) [Multinomial](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_multinomial)operation creates a sequence of indices of classes sampled from the multinomial distribution.- Parameters:
**probs**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor containing at each index poisition probability/log probability of sampling a given class.[Any](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_any)floating-point precision values are allowed.**num_samples**– Scalar or 1D tensor with a single value that determines the number of samples to generate per batch. Values should be of an integer type.**convert_type**– Data type to which to convert the output class indices. Allowed values: i32/i64**with_replacement**– Boolean that determines whether a sampled class can appear more than once in the output.**log_probs**– Boolean that determines whether to treat input probabilities as log probabilities.**global_seed**– First seed value (key) of Philox random number generation algorithm. (See RandomUniform for details)**op_seed**– Second seed value (counter) of Philox random number generation algorithm. (See RandomUniform for details)



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1311Multinomial24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Multinomial(const

-
class Multiply : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18MultiplyE) *#include <multiply.hpp>*Elementwise multiplication operation.

Public Functions

-
inline Multiply()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18Multiply8MultiplyEv) Constructs a multiplication operation.


-
Multiply(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18Multiply8MultiplyERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a multiplication operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v18Multiply12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Multiply()

-
class MVN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03MVNE) *#include <mvn.hpp>*Operator performing Mean Variance Normalization.

Public Functions

-
MVN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, bool across_channels = true, bool normalize_variance = true, double eps = 1e-9)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03MVN3MVNERK6OutputI4NodeEbbd) Constructs an

[MVN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_m_v_n)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**normalize_variance**– flag that denotes whether to perform variance normalization.**across_channels**– flag that denotes if mean values are shared across channels.**eps**– the number to be added to the variance to avoid division by zero when normalizing the value



-
MVN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data,[AxisSet](https://docs.openvino.ai/classov_1_1_axis_set.html#_CPPv4N2ov7AxisSetE)reduction_axes, bool normalize_variance = true, double eps = 1e-9)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03MVN3MVNERK6OutputI4NodeE7AxisSetbd) Constructs an

[MVN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_m_v_n)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**reduction_axes**– A list of axes, along which to reduce.**normalize_variance**– flag that denotes whether to perform variance normalization.**eps**– the number to be added to the variance to avoid division by zero when normalizing the value



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03MVN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
MVN(const

-
class MVN : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v63MVNE) *#include <mvn.hpp>*Operator performing Mean Variance Normalization.

Public Functions

-
MVN(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool normalize_variance, float eps,[MVNEpsMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op10MVNEpsModeE)eps_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v63MVN3MVNERK6OutputI4NodeERK6OutputI4NodeEbf10MVNEpsMode) Constructs an

[MVN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_m_v_n)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**reduction_axes**– A list of axes, along which to reduce.**normalize_variance**– flag that denotes whether to perform variance normalization.**eps**– the number to be added to the variance to avoid division by zero when normalizing the value**eps_mode**– the mode of applying epsilon



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v63MVN24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &output_values, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &input_values) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v63MVN8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v63MVN12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
MVN(const

-
class Negative : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08NegativeE) *#include <negative.hpp>*Elementwise negative operation.

Public Functions

-
Negative() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Negative8NegativeEv) Constructs a negative operation.


-
Negative(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Negative8NegativeERK6OutputI4NodeE) Constructs a negative operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08Negative12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Negative() = default

-
class NonMaxSuppression : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117NonMaxSuppressionE) *#include <non_max_suppression.hpp>*Elementwise addition operation.

Public Functions

-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_output_boxes_per_class, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &iou_threshold, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &score_threshold, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKb) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_non_max_suppression)operation.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**max_output_boxes_per_class**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing maximum number of boxes to be selected per class**iou_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing intersection over union threshold**score_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing minimum score threshold**box_encoding**– Specifies the format of boxes data encoding



-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKb) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_non_max_suppression)operation with default values for the last 3 inputs.- Parameters:


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v117NonMaxSuppression24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
NonMaxSuppression(const

-
class NonMaxSuppression : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v317NonMaxSuppressionE) *#include <non_max_suppression.hpp>*[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_max_suppression)operation.Subclassed by

[ov::op::v4::NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_non_max_suppression)Public Functions

-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_output_boxes_per_class, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &iou_threshold, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &score_threshold, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v317NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_max_suppression)operation.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**max_output_boxes_per_class**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing maximum number of boxes to be selected per class**iou_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing intersection over union threshold**score_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing minimum score threshold**box_encoding**– Specifies the format of boxes data encoding**sort_result_descending**– Specifies whether it is necessary to sort selected boxes across batches**output_type**– Specifies the output tensor type



-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v317NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_max_suppression)operation with default values for the last 3 inputs.- Parameters:


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v317NonMaxSuppression24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
NonMaxSuppression(const

-
class NonMaxSuppression : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[v3](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op2v3E)::[NonMaxSuppression](https://docs.openvino.ai/classov_1_1op_1_1v3_1_1_non_max_suppression.html#_CPPv4N2ov2op2v317NonMaxSuppressionE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v417NonMaxSuppressionE) *#include <non_max_suppression.hpp>*[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_non_max_suppression)operation.Public Functions

-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_output_boxes_per_class, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &iou_threshold, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &score_threshold, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v417NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_non_max_suppression)operation.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**max_output_boxes_per_class**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing maximum number of boxes to be selected per class**iou_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing intersection over union threshold**score_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing minimum score threshold**box_encoding**– Specifies the format of boxes data encoding**sort_result_descending**– Specifies whether it is necessary to sort selected boxes across batches**output_type**– Specifies the output tensor type



-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v417NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_non_max_suppression)operation with default values for the last 3 inputs.- Parameters:


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v417NonMaxSuppression24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
NonMaxSuppression(const

-
class NonMaxSuppression : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v517NonMaxSuppressionE) *#include <non_max_suppression.hpp>*[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_non_max_suppression)operation.Public Functions

-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v517NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_non_max_suppression)operation with default values in the last 4 inputs.

-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_output_boxes_per_class, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v517NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_non_max_suppression)operation with default values in the last. 3 inputs.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**max_output_boxes_per_class**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing maximum number of boxes to be selected per class**box_encoding**– Specifies the format of boxes data encoding**sort_result_descending**– Specifies whether it is necessary to sort selected boxes across batches**output_type**– Specifies the output tensor type



-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_output_boxes_per_class, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &iou_threshold, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v517NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_non_max_suppression)operation with default values in the last. 2 inputs.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**max_output_boxes_per_class**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing maximum number of boxes to be selected per class**iou_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing intersection over union threshold**box_encoding**– Specifies the format of boxes data encoding**sort_result_descending**– Specifies whether it is necessary to sort selected boxes across batches**output_type**– Specifies the output tensor type



-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_output_boxes_per_class, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &iou_threshold, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &score_threshold, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v517NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_non_max_suppression)operation with default value in the last. input.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**max_output_boxes_per_class**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing maximum number of boxes to be selected per class**iou_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing intersection over union threshold**score_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing minimum score threshold**box_encoding**– Specifies the format of boxes data encoding**sort_result_descending**– Specifies whether it is necessary to sort selected boxes across batches**output_type**– Specifies the output tensor type



-
NonMaxSuppression(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &boxes, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &scores, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_output_boxes_per_class, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &iou_threshold, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &score_threshold, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &soft_nms_sigma, const BoxEncodingType box_encoding = BoxEncodingType::CORNER, const bool sort_result_descending = true, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v517NonMaxSuppression17NonMaxSuppressionERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK15BoxEncodingTypeKbRKN2ov7element4TypeE) Constructs a

[NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_non_max_suppression)operation.- Parameters:
**boxes**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box coordinates**scores**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the box scores**max_output_boxes_per_class**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing maximum number of boxes to be selected per class**iou_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing intersection over union threshold**score_threshold**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing minimum score threshold**soft_nms_sigma**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)specifying the sigma parameter for Soft-NMS**box_encoding**– Specifies the format of boxes data encoding**sort_result_descending**– Specifies whether it is necessary to sort selected boxes across batches**output_type**– Specifies the output tensor type



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v517NonMaxSuppression24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
NonMaxSuppression(const

-
class NonZero : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZeroE) *#include <non_zero.hpp>*[NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero)operation returning indices of non-zero elements in the input tensor.Note

The indices are returned by-dimension in row-major order. For example the following output contains 3 indices of a 3D input tensor elements: [[0, 0, 2], [0, 1, 1], [0, 1, 2]] The values point to input elements at [0,0,0], [0,1,1] and [2,1,2]

Public Functions

-
NonZero(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZero7NonZeroERK6OutputI4NodeE) Constructs a

[NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero)operation.Note

The output type is int64.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
NonZero(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const std::string &output_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZero7NonZeroERK6OutputI4NodeERKNSt6stringE) Constructs a

[NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero)operation.- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**output_type**– produce indices. Currently, only ‘int64’ or ‘int32’ are supported



-
NonZero(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZero7NonZeroERK6OutputI4NodeERKN7element4TypeE) Constructs a

[NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero)operation.- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**output_type**– produce indices. Currently, only int64 or int32 are supported



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37NonZero24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v37NonZero12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
NonZero(const

-
class NormalizeL2 : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011NormalizeL2E) *#include <normalize_l2.hpp>*Normalization with L2 norm.

Public Functions

-
NormalizeL2(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes, float eps,[EpsMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7EpsModeE)eps_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011NormalizeL211NormalizeL2ERK6OutputI4NodeERK6OutputI4NodeEf7EpsMode) Constructs a

[NormalizeL2](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_normalize_l2)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v011NormalizeL224validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
NormalizeL2(const

-
class NotEqual : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseComparison](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_comparison.html#_CPPv4N2ov2op4util27BinaryElementwiseComparisonE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18NotEqualE) *#include <not_equal.hpp>*Elementwise not-equal operation.

Public Functions

-
inline NotEqual()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18NotEqual8NotEqualEv) Constructs a not-equal operation.


-
NotEqual(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18NotEqual8NotEqualERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a not-equal operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v18NotEqual12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline NotEqual()

-
class NV12toBGR : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvertColorNV12Base](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convert_color_n_v12_base.html#_CPPv4N2ov2op4util20ConvertColorNV12BaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toBGRE) *#include <nv12_to_bgr.hpp>*Color conversion operation from NV12 to RGB format.

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input):[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)NV12 image can be represented in two ways: a) Single plane (as it is in the file): NV12 height dimension is 1.5x bigger than image height. ‘C’ dimension shall be 1. b) Two separate planes (used this way in many physical video sources): Y and UV. In this case b1) Y plane has height same as image height. ‘C’ dimension equals to 1 b2) UV plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 2.Supported element types: u8 or any supported floating-point type.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output):[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node will have NHWC layout and shape HxW same as image spatial dimensions.Number of output channels ‘C’ will be 3, as per interleaved RGB format, first channel is B, last is R

Conversion of each pixel from NV12 (YUV) to RGB space is represented by following formulas: R = 1.164 * (Y - 16) + 1.596 * (V - 128) G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128) B = 1.164 * (Y - 16) + 2.018 * (U - 128) Then R, G, B values are clipped to range (0, 255)


Public Functions

-
explicit NV12toBGR(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toBGR9NV12toBGRERK6OutputI4NodeE) Constructs a conversion operation from input image in NV12 format As per NV12 format definition, node height dimension shall be 1.5 times bigger than image height so that image (w=640, h=480) is represented by NHWC shape {N,720,640,1} (height*1.5 x width)


-
explicit NV12toBGR(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_y, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_uv)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toBGR9NV12toBGRERK6OutputI4NodeERK6OutputI4NodeE) Constructs a conversion operation from 2-plane input image in NV12 format In general case Y channel of image can be separated from UV channel which means that operation needs two nodes for Y and UV planes respectively. Y plane has one channel, and UV has 2 channels, both expect ‘NHWC’ layout.

- Parameters:
**arg_y**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for Y plane (NHWC layout). Shall have WxH dimensions equal to image dimensions. ‘C’ dimension equals to 1.**arg_uv**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for UV plane (NHWC layout). ‘H’ is half of image height, ‘W’ is half of image width, ‘C’ dimension equals to 2. Channel 0 represents ‘U’, channel 1 represents ‘V’ channel




-
class NV12toRGB : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ConvertColorNV12Base](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_convert_color_n_v12_base.html#_CPPv4N2ov2op4util20ConvertColorNV12BaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toRGBE) *#include <nv12_to_rgb.hpp>*Color conversion operation from NV12 to RGB format.

[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input):[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)NV12 image can be represented in two ways: a) Single plane (as it is in the file): NV12 height dimension is 1.5x bigger than image height. ‘C’ dimension shall be 1. b) Two separate planes (used this way in many physical video sources): Y and UV. In this case b1) Y plane has height same as image height. ‘C’ dimension equals to 1 b2) UV plane has dimensions: ‘H’ = image_h / 2; ‘W’ = image_w / 2; ‘C’ = 2.Supported element types: u8 or any supported floating-point type.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output):[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)node will have NHWC layout and shape HxW same as image spatial dimensions.Number of output channels ‘C’ will be 3, as per interleaved RGB format, first channel is R, last is B

Conversion of each pixel from NV12 (YUV) to RGB space is represented by following formulas: R = 1.164 * (Y - 16) + 1.596 * (V - 128) G = 1.164 * (Y - 16) - 0.813 * (V - 128) - 0.391 * (U - 128) B = 1.164 * (Y - 16) + 2.018 * (U - 128) Then R, G, B values are clipped to range (0, 255)


Public Functions

-
explicit NV12toRGB(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toRGB9NV12toRGBERK6OutputI4NodeE) Constructs a conversion operation from input image in NV12 format As per NV12 format definition, node height dimension shall be 1.5 times bigger than image height so that image (w=640, h=480) is represented by NHWC shape {N,720,640,1} (height*1.5 x width)


-
NV12toRGB(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_y, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_uv)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v89NV12toRGB9NV12toRGBERK6OutputI4NodeERK6OutputI4NodeE) Constructs a conversion operation from 2-plane input image in NV12 format In general case Y channel of image can be separated from UV channel which means that operation needs two nodes for Y and UV planes respectively. Y plane has one channel, and UV has 2 channels, both expect ‘NHWC’ layout.

- Parameters:
**arg_y**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for Y plane (NHWC layout). Shall have WxH dimensions equal to image dimensions. ‘C’ dimension equals to 1.**arg_uv**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor for UV plane (NHWC layout). ‘H’ is half of image height, ‘W’ is half of image width, ‘C’ dimension equals to 2. Channel 0 represents ‘U’, channel 1 represents ‘V’ channel




-
class OneHot : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[OneHotBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_one_hot_base.html#_CPPv4N2ov2op4util10OneHotBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16OneHotE) *#include <one_hot.hpp>*[OneHot](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_one_hot)operation.Public Functions

-
OneHot() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16OneHot6OneHotEv) Constructs a one-hot operation.


-
OneHot(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &depth, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &on_value, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &off_value, int64_t axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16OneHot6OneHotERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7int64_t) Constructs a one-hot operation.

- Parameters:
**indices**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor containing indices.**depth**– Specifies number of classes and the size of one-hot dimension.**on_value**– Specifies value that the locations in output tensor represented by indices in input take.**off_value**– Specifies value that the locations in output tensor not represented by indices in input take.**axis**– Axis along which one-hot representation in added.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16OneHot24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v16OneHot12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
OneHot() = default

-
class OneHot : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[OneHotBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_one_hot_base.html#_CPPv4N2ov2op4util10OneHotBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v166OneHotE) *#include <one_hot.hpp>*[OneHot](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_one_hot)operation.Public Types

Public Functions

-
OneHot() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v166OneHot6OneHotEv) Constructs a one-hot operation.


-
OneHot(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &depth, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &on_value, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &off_value, int64_t axis,[NegativeIndicesMode](https://docs.openvino.ai/classov_1_1op_1_1v16_1_1_one_hot.html#_CPPv4N2ov2op3v166OneHot19NegativeIndicesModeE)mode =[NegativeIndicesMode](https://docs.openvino.ai/classov_1_1op_1_1v16_1_1_one_hot.html#_CPPv4N2ov2op3v166OneHot19NegativeIndicesModeE)::[IGNORE_NEGATIVE](https://docs.openvino.ai/classov_1_1op_1_1v16_1_1_one_hot.html#_CPPv4N2ov2op3v166OneHot19NegativeIndicesMode15IGNORE_NEGATIVEE))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v166OneHot6OneHotERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7int64_t19NegativeIndicesMode) Constructs a one-hot operation.

- Parameters:
**indices**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor containing indices.**depth**– Specifies number of classes and the size of one-hot dimension.**on_value**– Specifies value that the locations in output tensor represented by indices in input take.**off_value**– Specifies value that the locations in output tensor not represented by indices in input take.**axis**– Axis along which one-hot representation in added.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v166OneHot24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v166OneHot12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline void set_negative_indices_mode(
[NegativeIndicesMode](https://docs.openvino.ai/classov_1_1op_1_1v16_1_1_one_hot.html#_CPPv4N2ov2op3v166OneHot19NegativeIndicesModeE)mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v166OneHot25set_negative_indices_modeE19NegativeIndicesMode) Sets the negative indices mode.


-
inline
[NegativeIndicesMode](https://docs.openvino.ai/classov_1_1op_1_1v16_1_1_one_hot.html#_CPPv4N2ov2op3v166OneHot19NegativeIndicesModeE)get_negative_indices_mode() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v166OneHot25get_negative_indices_modeEv) - Returns:
The negative indices mode.



-
OneHot() = default

-
class Op : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2OpE) *#include <op.hpp>*Root of all actual ops.

Subclassed by

[ov::exec_model_info::ExecutionNode](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1exec__model__info_1_1_execution_node),[ov::op::Sink](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1_sink),[ov::op::internal::DynamicQuantize](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_dynamic_quantize),[ov::op::internal::FullyConnected](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_fully_connected),[ov::op::internal::GLU](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_g_l_u),[ov::op::internal::NonMaxSuppressionIEInternal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_non_max_suppression_i_e_internal),[ov::op::internal::RMS](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_r_m_s),[ov::op::internal::RoPE](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_ro_p_e),[ov::op::internal::VLSDPA](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1internal_1_1_v_l_s_d_p_a),[ov::op::util::AvgPoolBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_avg_pool_base),[ov::op::util::BinaryElementwiseArithmetic](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic),[ov::op::util::BinaryElementwiseBitwise](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_binary_elementwise_bitwise),[ov::op::util::BinaryElementwiseComparison](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_binary_elementwise_comparison),[ov::op::util::BinaryElementwiseLogical](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_binary_elementwise_logical),[ov::op::util::BroadcastBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_broadcast_base),[ov::op::util::ConvertColorI420Base](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_convert_color_i420_base),[ov::op::util::ConvertColorNV12Base](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_convert_color_n_v12_base),[ov::op::util::ConvolutionBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_convolution_base),[ov::op::util::DetectionOutputBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_detection_output_base),[ov::op::util::EmbeddingBagOffsetsBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_embedding_bag_offsets_base),[ov::op::util::EmbeddingBagPackedBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_embedding_bag_packed_base),[ov::op::util::FFTBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_f_f_t_base),[ov::op::util::GatherBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_gather_base),[ov::op::util::GatherNDBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_gather_n_d_base),[ov::op::util::IndexReduction](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_index_reduction),[ov::op::util::InterpolateBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_interpolate_base),[ov::op::util::MaxPoolBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_max_pool_base),[ov::op::util::MulticlassNmsBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multiclass_nms_base),[ov::op::util::OneHotBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_one_hot_base),[ov::op::util::PadBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_pad_base),[ov::op::util::RNNCellBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_r_n_n_cell_base),[ov::op::util::ROIAlignBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_r_o_i_align_base),[ov::op::util::ReadValueBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_read_value_base),[ov::op::util::ReductionBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_reduction_base),[ov::op::util::ScatterBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_scatter_base),[ov::op::util::ScatterElementsUpdateBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_scatter_elements_update_base),[ov::op::util::ScatterNDBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_scatter_n_d_base),[ov::op::util::ShapeOfBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_shape_of_base),[ov::op::util::SqueezeBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_squeeze_base),[ov::op::util::TopKBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_top_k_base),[ov::op::util::UnaryElementwiseArithmetic](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic),[ov::op::v0::BatchNormInference](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_batch_norm_inference),[ov::op::v0::CTCGreedyDecoder](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_c_t_c_greedy_decoder),[ov::op::v0::Concat](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_concat),[ov::op::v0::Constant](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_constant),[ov::op::v0::Convert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_convert),[ov::op::v0::CumSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_cum_sum),[ov::op::v0::DepthToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_depth_to_space),[ov::op::v0::FakeQuantize](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_fake_quantize),[ov::op::v0::HardSigmoid](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_hard_sigmoid),[ov::op::v0::Interpolate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_interpolate),[ov::op::v0::LRN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_r_n),[ov::op::v0::MVN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_m_v_n),[ov::op::v0::MatMul](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_mat_mul),[ov::op::v0::NormalizeL2](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_normalize_l2),[ov::op::v0::PRelu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_p_relu),[ov::op::v0::PSROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_p_s_r_o_i_pooling),[ov::op::v0::Parameter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_parameter),[ov::op::v0::PriorBox](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_prior_box),[ov::op::v0::PriorBoxClustered](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_prior_box_clustered),[ov::op::v0::Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_proposal),[ov::op::v0::ROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_o_i_pooling),[ov::op::v0::Range](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_range),[ov::op::v0::RegionYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_region_yolo),[ov::op::v0::ReorgYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reorg_yolo),[ov::op::v0::Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result),[ov::op::v0::ReverseSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reverse_sequence),[ov::op::v0::Selu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_selu),[ov::op::v0::ShuffleChannels](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_shuffle_channels),[ov::op::v0::SpaceToDepth](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_space_to_depth),[ov::op::v0::Tile](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_tile),[ov::op::v0::Unsqueeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_unsqueeze),[ov::op::v10::IsFinite](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_is_finite),[ov::op::v10::IsInf](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_is_inf),[ov::op::v10::IsNaN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_is_na_n),[ov::op::v10::Unique](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_unique),[ov::op::v12::GroupNormalization](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v12_1_1_group_normalization),[ov::op::v13::BitwiseNot](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_bitwise_not),[ov::op::v13::FakeConvert](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_fake_convert),[ov::op::v13::Multinomial](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_multinomial),[ov::op::v13::NMSRotated](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_n_m_s_rotated),[ov::op::v13::ScaledDotProductAttention](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_scaled_dot_product_attention),[ov::op::v14::ConvertPromoteTypes](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_convert_promote_types),[ov::op::v14::Inverse](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v14_1_1_inverse),[ov::op::v15::Col2Im](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_col2_im),[ov::op::v15::STFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_s_t_f_t),[ov::op::v15::SearchSorted](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_search_sorted),[ov::op::v15::SliceScatter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_slice_scatter),[ov::op::v15::StringTensorPack](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_string_tensor_pack),[ov::op::v15::StringTensorUnpack](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_string_tensor_unpack),[ov::op::v16::ISTFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_i_s_t_f_t),[ov::op::v16::Identity](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_identity),[ov::op::v16::SegmentMax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_segment_max),[ov::op::v16::SparseFillEmptyRows](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_sparse_fill_empty_rows),[ov::op::v1::BatchToSpace](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_batch_to_space),[ov::op::v1::ConvertLike](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_convert_like),[ov::op::v1::DeformablePSROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_deformable_p_s_r_o_i_pooling),[ov::op::v1::GatherTree](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_gather_tree),[ov::op::v1::LogicalNot](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_logical_not),[ov::op::v1::NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_non_max_suppression),[ov::op::v1::Reshape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reshape),[ov::op::v1::Reverse](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reverse),[ov::op::v1::Select](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_select),[ov::op::v1::Softmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_softmax),[ov::op::v1::SpaceToBatch](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_space_to_batch),[ov::op::v1::Split](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_split),[ov::op::v1::StridedSlice](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_strided_slice),[ov::op::v1::Transpose](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_transpose),[ov::op::v1::VariadicSplit](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_variadic_split),[ov::op::v3::Bucketize](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_bucketize),[ov::op::v3::EmbeddingSegmentsSum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_embedding_segments_sum),[ov::op::v3::ExtractImagePatches](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_extract_image_patches),[ov::op::v3::NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_max_suppression),[ov::op::v3::NonZero](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_non_zero),[ov::op::v4::CTCLoss](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_c_t_c_loss),[ov::op::v4::Range](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_range),[ov::op::v4::Swish](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_swish),[ov::op::v5::BatchNormInference](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_batch_norm_inference),[ov::op::v5::LogSoftmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_log_softmax),[ov::op::v5::NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_non_max_suppression),[ov::op::v6::CTCGreedyDecoderSeqLen](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_c_t_c_greedy_decoder_seq_len),[ov::op::v6::ExperimentalDetectronDetectionOutput](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_detection_output),[ov::op::v6::ExperimentalDetectronGenerateProposalsSingleImage](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_generate_proposals_single_image),[ov::op::v6::ExperimentalDetectronPriorGridGenerator](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_prior_grid_generator),[ov::op::v6::ExperimentalDetectronROIFeatureExtractor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_r_o_i_feature_extractor),[ov::op::v6::ExperimentalDetectronTopKROIs](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_experimental_detectron_top_k_r_o_is),[ov::op::v6::GatherElements](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_gather_elements),[ov::op::v6::MVN](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_m_v_n),[ov::op::v7::Einsum](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_einsum),[ov::op::v7::Roll](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v7_1_1_roll),[ov::op::v8::AdaptiveAvgPool](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_adaptive_avg_pool),[ov::op::v8::AdaptiveMaxPool](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_adaptive_max_pool),[ov::op::v8::MatrixNms](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_matrix_nms),[ov::op::v8::PriorBox](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_prior_box),[ov::op::v8::RandomUniform](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_random_uniform),[ov::op::v8::Slice](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_slice),[ov::op::v8::Softmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_softmax),[ov::op::v9::Eye](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_eye),[ov::op::v9::GenerateProposals](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_generate_proposals),[ov::op::v9::GridSample](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_grid_sample),[ov::op::v9::NonMaxSuppression](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v9_1_1_non_max_suppression)

-
class Pad : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[PadBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_pad_base.html#_CPPv4N2ov2op4util7PadBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13PadE) *#include <pad.hpp>*Generic padding operation.

Public Functions

-
Pad() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Pad3PadEv) Constructs a Pad-1 operation.


-
Pad(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_pad_value,[PadMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadModeE)pad_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Pad3PadERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7PadMode) Constructs a Pad-1 operation.

- Parameters:
**arg**– The output producing input tensor to be padded.**pads_begin**– The output which specifies the number of padding elements added before position 0 on each axis of arg.**pads_end**– The output which specifies the number of padding elements after the last element on each axis.**arg_pad_value**– The scalar output with the value used for padding if pad_mode is CONSTANT**pad_mode**– The padding mode: CONSTANT, EDGE, REFLECT or SYMMETRIC. CONSTANT initializes new elements with arg_pad_value, EDGE uses the nearest value from arg. REFLECT and SYMMETRIC tile the background by flipping arg at the edge (SYMMETRIC) or on the last row/column/etc. (REFLECT).



-
Pad(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end,[PadMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadModeE)pad_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v13Pad3PadERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7PadMode) Constructs a Pad-1 operation.

- Parameters:
**arg**– The output producing input tensor to be padded.**pads_begin**– The output which specifies the number of padding elements added**pads_end**– The output which specifies the number of padding elements after the last element on each axis.**pad_mode**– The padding mode: CONSTANT, EDGE, REFLECT or SYMMETRIC.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Pad12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v13Pad8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
Pad() = default

-
class Pad : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[PadBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_pad_base.html#_CPPv4N2ov2op4util7PadBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v123PadE) *#include <pad.hpp>*Generic padding operation.

Public Functions

-
Pad() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v123Pad3PadEv) Constructs a Pad-12 operation.


-
Pad(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end,[PadMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadModeE)pad_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v123Pad3PadERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7PadMode) Constructs a Pad-12 operation.

- Parameters:
**arg**– The output producing input tensor to be padded.**pads_begin**– The output which specifies the number of padding elements to add (or remove) before position 0 on each axis of arg.**pads_end**– The output which specifies the number of padding elements to add (or remove) after the last element on each axis.**pad_mode**– The padding mode: CONSTANT, EDGE, REFLECT or SYMMETRIC.



-
Pad(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg_pad_value,[PadMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op7PadModeE)pad_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v123Pad3PadERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE7PadMode) Constructs a Pad-12 operation.

- Parameters:
**arg**– The output producing input tensor to be padded.**pads_begin**– The output which specifies the number of padding elements to add (or remove) before position 0 on each axis of arg.**pads_end**– The output which specifies the number of padding elements to add (or remove) after the last element on each axis.**arg_pad_value**– The scalar output with the value used for padding if pad_mode is CONSTANT**pad_mode**– The padding mode: CONSTANT, EDGE, REFLECT or SYMMETRIC.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v123Pad12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v123Pad8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
Pad() = default

-
class Parameter : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09ParameterE) *#include <parameter.hpp>*A model parameter.

Parameters are nodes that represent the arguments that will be passed to user-defined models.

[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)creation requires a sequence of parameters. Basic graph operations do not need parameters attached to a model.Public Functions

-
Parameter() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09Parameter9ParameterEv) Constructions a tensor-typed parameter node.


-
Parameter(const
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&element_type, const[PartialShape](https://docs.openvino.ai/classov_1_1_partial_shape.html#_CPPv4N2ov12PartialShapeE)&pshape)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09Parameter9ParameterERKN2ov7element4TypeERK12PartialShape) Constructions a tensor-typed parameter node.

- Parameters:
**element_type**– The element type of the parameter.**pshape**– The partial shape of the parameter.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09Parameter24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Parameter() = default

-
class Power : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15PowerE) *#include <power.hpp>*Elementwise exponentiation operation.

*Inputs*Type

Description

`arg0`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and numeric element type.

`arg1`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of the same shape and element type as

`arg0`

.Type

Description

\(N[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \texttt{arg0}[i_1,\dots,i_n]^{\texttt{arg1}[i_1,\dots,i_n]}\)

Public Functions

-
Power(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Power5PowerERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs an exponentiation operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v15Power12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Power(const

-
class PRelu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05PReluE) *#include <prelu.hpp>*Parametrized

[Relu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_relu)x < 0 => f(x) = x * slope x >= 0 => f(x) = x.Public Functions

-
PRelu(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &slope)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05PRelu5PReluERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[PRelu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_p_relu)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor**slope**– Multipliers for negative values



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05PRelu24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v05PRelu12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
PRelu(const

-
class PriorBox : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08PriorBoxE) *#include <prior_box.hpp>*Layer which generates prior boxes of specified sizes normalized to input image size.

Public Functions

-
PriorBox(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &layer_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image_shape, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_prior_box_1_1_attributes.html#_CPPv4N2ov2op2v08PriorBox10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08PriorBox8PriorBoxERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[PriorBox](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_prior_box)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08PriorBox24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v08PriorBox12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08PriorBox10AttributesE) *#include <prior_box.hpp>*

-
PriorBox(const

-
class PriorBox : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88PriorBoxE) *#include <prior_box.hpp>*Layer which generates prior boxes of specified sizes normalized to input image size.

Public Functions

-
PriorBox(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &layer_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image_shape, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v8_1_1_prior_box_1_1_attributes.html#_CPPv4N2ov2op2v88PriorBox10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88PriorBox8PriorBoxERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[PriorBox](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_prior_box)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88PriorBox24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v88PriorBox12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v88PriorBox10AttributesE) *#include <prior_box.hpp>*

-
PriorBox(const

-
class PriorBoxClustered : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v017PriorBoxClusteredE) *#include <prior_box_clustered.hpp>*Layer which generates prior boxes of specified sizes normalized to input image size.

Public Functions

-
PriorBoxClustered(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &layer_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image_shape, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_prior_box_clustered_1_1_attributes.html#_CPPv4N2ov2op2v017PriorBoxClustered10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v017PriorBoxClustered17PriorBoxClusteredERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[PriorBoxClustered](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_prior_box_clustered)operation.- Parameters:
**layer_shape**–[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)of layer for which prior boxes are computed**image_shape**–[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)of image to which prior boxes are scaled**attrs**–[PriorBoxClustered](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_prior_box_clustered)attributes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v017PriorBoxClustered24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v017PriorBoxClustered12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v017PriorBoxClustered10AttributesE) *#include <prior_box_clustered.hpp>*

-
PriorBoxClustered(const

-
class Proposal : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08ProposalE) *#include <proposal.hpp>*[Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_proposal)operation.Subclassed by

[ov::op::v4::Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_proposal)Unnamed Group

-
void set_attrs(
[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_proposal_1_1_attributes.html#_CPPv4N2ov2op2v08Proposal10AttributesE)&&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Proposal9set_attrsERR10Attributes) Set the

[Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_proposal)operator attributes.- Parameters:
**attrs**–[Attributes](https://docs.openvino.ai/group__ov__transformation__common__api.html#structov_1_1op_1_1v0_1_1_proposal_1_1_attributes)to be set.


Public Functions

-
Proposal(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &class_probs, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &bbox_deltas, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image_shape, const[Attributes](https://docs.openvino.ai/structov_1_1op_1_1v0_1_1_proposal_1_1_attributes.html#_CPPv4N2ov2op2v08Proposal10AttributesE)&attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Proposal8ProposalERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_proposal)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Proposal24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
struct Attributes
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v08Proposal10AttributesE) *#include <proposal.hpp>*

-
void set_attrs(

-
class Proposal : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[v0](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op2v0E)::[Proposal](https://docs.openvino.ai/classov_1_1op_1_1v0_1_1_proposal.html#_CPPv4N2ov2op2v08ProposalE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ProposalE) *#include <proposal.hpp>*[Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_proposal)operation.Public Functions

-
Proposal(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &class_probs, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &bbox_deltas, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &image_shape, const Attributes &attrs)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48Proposal8ProposalERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK10Attributes) Constructs a

[Proposal](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_proposal)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48Proposal24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Proposal(const

-
class PSROIPooling : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPoolingE) *#include <psroi_pooling.hpp>*[PSROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_p_s_r_o_i_pooling)operation.Public Functions

-
PSROIPooling(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &coords, const size_t output_dim, const size_t group_size, const float spatial_scale, int spatial_bins_x, int spatial_bins_y, const std::string &mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling12PSROIPoolingERK6OutputI4NodeERK6OutputI4NodeEK6size_tK6size_tKfiiRKNSt6stringE) Constructs a

[PSROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_p_s_r_o_i_pooling)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)feature map {N, C, …}**coords**– Coordinates of bounding boxes**output_dim**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)channel number**group_size**– Number of groups to encode position-sensitive scores**spatial_scale**– Ratio of input feature map over input image size**spatial_bins_x**– Numbers of bins to divide the input feature maps over width**spatial_bins_y**– Numbers of bins to divide the input feature maps over height**mode**– Mode of pooling - Avg or Bilinear



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
void set_output_dim(size_t output_dim)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling14set_output_dimE6size_t) Set the output channel dimension size.

- Parameters:
**output_dim**– Channel dimension size.


-
void set_group_size(size_t group_size)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling14set_group_sizeE6size_t) Set the output groups number.

- Parameters:
**group_size**– Number of groups.


-
void set_spatial_scale(float scale)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling17set_spatial_scaleEf) Set the spatial scale.

- Parameters:
**scale**– Spatial scale value.


-
void set_spatial_bins_x(int x)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling18set_spatial_bins_xEi) Set the number of bins over image width.

- Parameters:
**x**– Number of bins over width (x) axis.


-
void set_spatial_bins_y(int y)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling18set_spatial_bins_yEi) Set the number of bins over image height.

- Parameters:
**y**– Number of bins over height (y) axis.


-
void set_mode(std::string mode)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012PSROIPooling8set_modeENSt6stringE) Set the pooling mode.

- Parameters:
**mode**– Pooling mode name.


-
PSROIPooling(const

-
class RandomUniform : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v813RandomUniformE) *#include <random_uniform.hpp>*[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)[RandomUniform](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_random_uniform)operation.Public Functions

-
RandomUniform(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &out_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &min_val, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &max_val, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&out_type, uint64_t global_seed = 0, uint64_t op_seed = 0,[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PhiloxAlignment](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op15PhiloxAlignmentE)alignment =[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PhiloxAlignment](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op15PhiloxAlignmentE)::[TENSORFLOW](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op15PhiloxAlignment10TENSORFLOWE))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v813RandomUniform13RandomUniformERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKN2ov7element4TypeE8uint64_t8uint64_tN2ov2op15PhiloxAlignmentE) Constructs a

[RandomUniform](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_random_uniform)operation.- Parameters:
**out_shape**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the tensor with output shape.**min_val**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the tensor with minimum value.**max_val**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the tensor with maximum value.**out_type**–[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)type of the tensor.**global_seed**– Global seed value.**op_seed**– Operational seed value.**alignment**– Alignment of numbers generated by Philox algorithm based on provided seed.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v813RandomUniform24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool can_constant_fold(const OutputVector &inputs_values) const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v813RandomUniform17can_constant_foldERK12OutputVector) - Returns:
Turns off constant folding for

[RandomUniform](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_random_uniform)operation.


-
uint64_t get_global_seed() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v813RandomUniform15get_global_seedEv) - Returns:
The global seed value.



-
uint64_t get_op_seed() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v813RandomUniform11get_op_seedEv) - Returns:
The operational seed value.



-
std::pair<uint64_t, uint64_t> get_state() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v813RandomUniform9get_stateEv) - Returns:
The state value.



-
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[PhiloxAlignment](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op15PhiloxAlignmentE)get_alignment() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v813RandomUniform13get_alignmentEv) - Returns:
The alignment mode.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v813RandomUniform12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
RandomUniform(const

-
class Range : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45RangeE) *#include <range.hpp>*[Range](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_range)operation, analogous to`arange()`

in Numpy.Public Functions

-
Range() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45Range5RangeEv) Constructs an unitialized range operation.


-
Range(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step,[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)output_type)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45Range5RangeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEN7element4TypeE) Constructs a range operation.

- Parameters:
**start**– The tensor producing the start value. Must be a scalar of numeric element type.**stop**– The tensor producing the stop value. Must be a scalar of numeric element type.**step**– The tensor producing the step value. Must be a scalar of numeric element type.**output_type**– The type of the output.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45Range24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v45Range12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Range() = default

-
class Range : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05RangeE) *#include <range.hpp>*[Range](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_range)operation, analogous to

in Python.[range()](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1reference_1af0fac75e70945db6b045007fe2f23e05)Public Functions

-
Range() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Range5RangeEv) Constructs an unitialized range operation.


-
Range(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Range5RangeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a range operation.

- Parameters:
**start**– The tensor producing the start value. Must be a scalar of integer element type, and same element type as`stop`

and`step`

.**stop**– The tensor producing the stop value. Must be a scalar of integer element type, and same element type as`start`

and`step`

.**step**– The tensor producing the step value. Must be a scalar of integer element type, and same element type as`start`

and`stop`

.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v05Range24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v05Range12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Range() = default

-
class ReadValue : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ReadValueBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_read_value_base.html#_CPPv4N2ov2op4util13ReadValueBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39ReadValueE) *#include <read_value.hpp>*[ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_read_value)operation creates the variable with`variable_id`

and returns value of this variable.Public Functions

-
ReadValue(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &init_value, const std::string &variable_id)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39ReadValue9ReadValueERK6OutputI4NodeERKNSt6stringE) Constructs a

[ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_read_value)operation.- Parameters:
**init_value**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**variable_id**– identificator of the variable to create.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v39ReadValue24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual std::string get_variable_id() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v39ReadValue15get_variable_idEv) Returns the identifier of corresponding variable.


-
ReadValue(const

-
class ReadValue : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ReadValueBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_read_value_base.html#_CPPv4N2ov2op4util13ReadValueBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v69ReadValueE) *#include <read_value.hpp>*[ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_read_value)operation gets an input value from the variable with`variable_id`

and returns it as an output.Public Functions

Constructs a

[ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_read_value)operation.- Parameters:
**variable**– Class for storing and synchronizing element types, shapes and identifiers between pairs of Assign/ReadValue nodes.


Constructs a

[ReadValue](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v6_1_1_read_value)operation.- Parameters:
**init_value**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**variable**– Class for storing and synchronizing element types, shapes and identifiers between pairs of Assign/ReadValue nodes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v69ReadValue24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual std::string get_variable_id() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v69ReadValue15get_variable_idEv) Returns the identifier of corresponding variable.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v69ReadValue12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.



-
class ReduceL1 : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL1E) *#include <reduce_l1.hpp>*Reduction operation using L1 norm: L1(x) = sum(abs(x)) if all dimensions are specified for the normalisation.

Reduces the tensor, eliminating the specified reduction axes by taking the L1-norm.

Public Functions

-
ReduceL1() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL18ReduceL1Ev) Constructs a reducet L1-norm operation.


-
ReduceL1(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL18ReduceL1ERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a reduce L1-norm operation.

- Parameters:
**arg**– The tensor to be reduced.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to true it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v48ReduceL112has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceL1() = default

-
class ReduceL2 : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL2E) *#include <reduce_l2.hpp>*Reduction operation using L2 norm:

Reduces the tensor, eliminating the specified reduction axes by taking the L2-norm.

Public Functions

-
ReduceL2() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL28ReduceL2Ev) Constructs a reducet L2-norm operation.


-
ReduceL2(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48ReduceL28ReduceL2ERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a reduce L2-norm operation.

- Parameters:
**arg**– The tensor to be reduced.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to true it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v48ReduceL212has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceL2() = default

-
class ReduceLogicalAnd : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[LogicalReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_logical_reduction_keep_dims.html#_CPPv4N2ov2op4util24LogicalReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v116ReduceLogicalAndE) *#include <reduce_logical_and.hpp>*Performs a reduction using “logical and”.

The reduction is performed over slices of the first input. The slices shape depends on the values passed to the second input - the axes.

Public Functions

-
ReduceLogicalAnd(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, const bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v116ReduceLogicalAnd16ReduceLogicalAndERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a

[ReduceLogicalAnd](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_logical_and)node.- Parameters:
**data**– - The input tensor with data to be reduced**reduction_axes**– - The input tensor with information about axes over which the first tensor should be sliced prior to the reduction operation**keep_dims**– - Indicates if the axes used for reduction should be held/kept



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v116ReduceLogicalAnd12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceLogicalAnd(const

-
class ReduceLogicalOr : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[LogicalReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_logical_reduction_keep_dims.html#_CPPv4N2ov2op4util24LogicalReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v115ReduceLogicalOrE) *#include <reduce_logical_or.hpp>*Performs a reduction using “logical or”.

The reduction is performed over slices of the first input. The slices shape depends on the values passed to the second input - the axes.

Public Functions

-
ReduceLogicalOr(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, const bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v115ReduceLogicalOr15ReduceLogicalOrERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a

[ReduceLogicalOr](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_logical_or)node.- Parameters:
**data**– - The input tensor with data to be reduced**reduction_axes**– - The input tensor with information about axes over which the first tensor should be sliced prior to the reduction operation**keep_dims**– - Indicates if the axes used for reduction should be held/kept



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v115ReduceLogicalOr12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceLogicalOr(const

-
class ReduceMax : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMaxE) *#include <reduce_max.hpp>*[ReduceMax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_max)operation.Public Functions

-
ReduceMax() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMax9ReduceMaxEv) Constructs a summation operation.


-
ReduceMax(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMax9ReduceMaxERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a summation operation.

- Parameters:
**arg**– The tensor to be summed.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to 1 it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19ReduceMax12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceMax() = default

-
class ReduceMean : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110ReduceMeanE) *#include <reduce_mean.hpp>*[ReduceMean](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_mean)operation.Public Functions

-
ReduceMean(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110ReduceMean10ReduceMeanERK6OutputI4NodeERK6OutputI4NodeEb) - Parameters:
**arg**– The tensor to be summed.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to 1 it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v110ReduceMean12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceMean(const

-
class ReduceMin : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMinE) *#include <reduce_min.hpp>*[ReduceMin](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reduce_min)operation.Public Functions

-
ReduceMin() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMin9ReduceMinEv) Constructs a summation operation.


-
ReduceMin(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceMin9ReduceMinERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a summation operation.

- Parameters:
**arg**– The tensor to be summed.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to 1 it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19ReduceMin12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceMin() = default

-
class ReduceProd : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110ReduceProdE) *#include <reduce_prod.hpp>*Product reduction operation.

Reduces the tensor, eliminating the specified reduction axes by taking the product.

Public Functions

-
ReduceProd() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110ReduceProd10ReduceProdEv) Constructs a product reduction operation.


-
ReduceProd(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v110ReduceProd10ReduceProdERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a product reduction operation.

- Parameters:
**arg**– The tensor to be reduced.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to true it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v110ReduceProd12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceProd() = default

-
class ReduceSum : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ArithmeticReductionKeepDims](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_arithmetic_reduction_keep_dims.html#_CPPv4N2ov2op4util27ArithmeticReductionKeepDimsE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceSumE) *#include <reduce_sum.hpp>*[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)sum operation.Element-wise sums the input tensor, eliminating the specified reduction axes. For example:

\[\begin{split} \mathit{sum}\left(\{0\}, \left[ \begin{array}{ccc} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{array} \right]\right) = \left[ (1 + 3 + 5), (2 + 4 + 6) \right] = \left[ 9, 12 \right]~~~\text{(dimension 0 (rows) is eliminated)} \end{split}\]\[\begin{split} \mathit{sum}\left(\{1\}, \left[ \begin{array}{ccc} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{array} \right]\right) = \left[ (1 + 2), (3 + 4), (5 + 6) \right] = \left[ 3, 7, 11 \right]~~~\text{(dimension 1 (columns) is eliminated)} \end{split}\]\[\begin{split} \mathit{sum}\left(\{0,1\}, \left[ \begin{array}{ccc} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{array} \right]\right) = (1 + 2) + (3 + 4) + (5 + 6) = 21~~~\text{(both dimensions (rows and columns) are eliminated)} \end{split}\]*Parameters*Description

`reduction_axes`

The axes to eliminate through summation.

`keep_dims`

If set to 1 it holds axes that are used for reduction.

*Inputs*Type

Description

`arg`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

An input tensor of any shape and numeric element type.

Type

Description

\(N[\textit{delete}(A,d_1,\dots,d_n)]\)

The tensor \(T\), where \(T\) is the input tensor with the

`reduction_axes`

\(A\) eliminated by summation.Public Functions

-
ReduceSum() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceSum9ReduceSumEv) Constructs a summation operation.


-
ReduceSum(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reduction_axes, bool keep_dims = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19ReduceSum9ReduceSumERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a summation operation.

- Parameters:
**arg**– The tensor to be summed.**reduction_axes**– The axis positions (0-based) to be eliminated.**keep_dims**– If set to 1 it holds axes that are used for reduction.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19ReduceSum12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ReduceSum() = default

-
class RegionYolo : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010RegionYoloE) *#include <region_yolo.hpp>*[RegionYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_region_yolo)operation.Public Functions

-
RegionYolo(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const size_t coords, const size_t classes, const size_t regions, const bool do_softmax, const std::vector<int64_t> &mask, const int axis, const int end_axis, const std::vector<float> &anchors = std::vector<float>{})[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010RegionYolo10RegionYoloERK6OutputI4NodeEK6size_tK6size_tK6size_tKbRKNSt6vectorI7int64_tEEKiKiRKNSt6vectorIfEE) Constructs a

[RegionYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_region_yolo)operation.- Parameters:
**input**–**[in]**[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)**coords**–**[in]**Number of coordinates for each region**classes**–**[in]**Number of classes for each region**regions**–**[in]**Number of regions**do_softmax**–**[in]**Compute softmax**mask**–**[in]**[Mask](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_mask)**axis**–**[in]**Axis to begin softmax on**end_axis**–**[in]**Axis to end softmax on**anchors**–**[in]**A flattened list of pairs`[width, height]`

that describes prior box sizes.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010RegionYolo24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
RegionYolo(const

-
class Relu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04ReluE) *#include <relu.hpp>*Elementwise

[Relu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_relu)operation.

-
class ReorgYolo : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09ReorgYoloE) *#include <reorg_yolo.hpp>*[ReorgYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reorg_yolo)operation.Public Functions

-
ReorgYolo(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const size_t stride)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09ReorgYolo9ReorgYoloERK6OutputI4NodeEK6size_t) Constructs a

[ReorgYolo](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reorg_yolo)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)**stride**– Stride to reorganize input by



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09ReorgYolo24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ReorgYolo(const

-
class Reshape : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17ReshapeE) *#include <reshape.hpp>*[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)dynamic reshape operation.“Converts” an input tensor into a new shape with the same number of elements. This op does not touch the actual data. If needed, use

[Transpose](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_transpose)for that purpose.Public Functions

-
Reshape(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &shape_pattern, bool special_zero)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Reshape7ReshapeERK6OutputI4NodeERK6OutputI4NodeEb) Constructs a dynamic reshape operation. This operation does not perform transpose.

- Parameters:
**arg**– The tensor to be reshaped.**shape_pattern**– The node that defines output shape shape_pattern. If the input shape is \((a_0,\dots,a_{k-1})\) then the output shape must be of the form \((b_0,\dots,b_{j-1})\) where \(\Pi(a_i) = \Pi(b_i)\). A value of -1 is allowed for at most one dimension, in which case the dimension size is inferred based on element count of input tensor.**special_zero**– Treats zeros in`shape_pattern`

as wildcard flags indicating a copy from input shape at the same index.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Reshape24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Reshape8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Reshape12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Reshape(const

-
class Result : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06ResultE) *#include <result.hpp>*[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)operation.The

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)output tensor is special, it shares tensor with[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s input but requires to have dedicated properties like:tensor names.


Setting/adding

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s output names modify this specific tensor names.[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s specific tensor names are added to input descriptor and transferred to new descriptor if[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s input has been replaced.Examples 1: No specific names on

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s outputset output names: [N1] ↓ |————-—| [names: N1] |————–—| |

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)|—————————>|[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)| ->[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)output names: N1 |————-—| |————–—|Examples 2:

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)’s has got specific namesset output names: set output names: [N1] [R1, R2] ↓ ↓ |————-—| [names: N1, R1, R2] |————–—| |

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)|—————————>|[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)| ->[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)output names: R1, R2 |————-—| |————–—|Examples 3:

[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)from example 2 connected to new nodeset output names: set output names: [N2] [R1, R2] ↓ ↓ |————-—| [names: N2, R1, R2] |————–—| |

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)|—————————>|[Result](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_result)| ->[Model](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_model)output names: R1, R2 |————-—| |————–—|set output names: [N1] ↓ |————-—| [names: N1] |

[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)|————–—> |————-—|Public Functions

-
Result() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Result6ResultEv) Allows a value to be used as a function result.


-
Result(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Result6ResultERK6OutputI4NodeE) Allows a value to be used as a function result.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.


-
Result(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, bool use_input_names)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Result6ResultERK6OutputI4NodeEb) Allows a value to be used as a function result.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v06Result24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06Result8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v06Result12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.



-
class Reverse : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17ReverseE) *#include <reverse.hpp>*[Reverse](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_reverse)operation.Public Functions

-
Reverse(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &reversed_axes, const std::string &mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Reverse7ReverseERK6OutputI4NodeERK6OutputI4NodeERKNSt6stringE) Constructs a reverse operation.

- Parameters:
**data**– The input tensor, some of whose axes are to be reversed.**reversed_axes**– The axes to reverse in a form of a set of indices or boolean mask.**mode**– The way reversed_axes should be interpreted - a set or a mask.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Reverse24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline Mode get_mode() const
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Reverse8get_modeEv) - Returns:
The second input data interpretation mode.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Reverse12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Reverse(const

-
class ReverseSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ReverseSequenceE) *#include <reverse_sequence.hpp>*[ReverseSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reverse_sequence)operation.Public Functions

-
ReverseSequence(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &seq_lengths, int64_t batch_axis = 0, int64_t seq_axis = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ReverseSequence15ReverseSequenceERK6OutputI4NodeERK6OutputI4NodeE7int64_t7int64_t) Constructs a

[ReverseSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_reverse_sequence)operation.- Parameters:
**arg**– tensor with input data to reverse**seq_lengths**– 1D tensor of integers with sequence lengths in the input tensor.**batch_axis**– index of the batch dimension.**seq_axis**– index of the sequence dimension.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ReverseSequence24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ReverseSequence(const

-
class RNNCell : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07RNNCellE) *#include <rnn_cell.hpp>*Class for single RNN cell node.

See also

LSTMSequence,

[LSTMCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_l_s_t_m_cell), GRUCellNote

It follows notation and equations defined as in ONNX standard:

[onnx/onnx](https://github.com/onnx/onnx/blob/master/docs/Operators.md#RNN)Note

It calculates following equations:

Ht = f(Xt*(Wi^T) + Ht-1*(Ri^T) + Wbi + Rbi) * - Is a dot product, f - is activation functions.

Note

This class represents only single

*cell*(for current time step) and not the whole RNN Sequence layerPublic Functions

-
RNNCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, std::size_t hidden_size, const std::vector<std::string> &activations = std::vector<std::string>{"tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07RNNCell7RNNCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEf) Constructs

[RNNCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_n_n_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [hidden_size, hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.



-
RNNCell(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &X, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &initial_hidden_state, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &W, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &R, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &B, std::size_t hidden_size, const std::vector<std::string> &activations = std::vector<std::string>{"tanh"}, const std::vector<float> &activations_alpha = {}, const std::vector<float> &activations_beta = {}, float clip = 0.f)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07RNNCell7RNNCellERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeENSt6size_tERKNSt6vectorINSt6stringEEERKNSt6vectorIfEERKNSt6vectorIfEEf) Constructs

[RNNCell](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_n_n_cell)node.- Parameters:
**X**–**[in]**The input tensor with shape: [batch_size, input_size].**initial_hidden_state**–**[in]**The hidden state tensor at current time step with shape: [batch_size, hidden_size].**W**–**[in]**The weight tensor with shape: [hidden_size, input_size].**R**–**[in]**The recurrence weight tensor with shape: [hidden_size, hidden_size].**B**–**[in]**The bias tensor for input gate with shape: [hidden_size].**hidden_size**–**[in]**The number of hidden units for recurrent cell.**activations**–**[in]**The vector of activation functions used inside recurrent cell.**activations_alpha**–**[in]**The vector of alpha parameters for activation functions in order respective to activation list.**activations_beta**–**[in]**The vector of beta parameters for activation functions in order respective to activation list.**clip**–**[in]**The value defining clipping range [-clip, clip] on input of activation functions.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07RNNCell24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
RNNCell(const

-
class RNNSequence : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[RNNCellBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_n_n_cell_base.html#_CPPv4N2ov2op4util11RNNCellBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v511RNNSequenceE) *#include <rnn_sequence.hpp>*[RNNSequence](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v5_1_1_r_n_n_sequence)operation.Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v511RNNSequence24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual void validate_and_infer_types() override

-
class ROIAlign : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ROIAlignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_o_i_align_base.html#_CPPv4N2ov2op4util12ROIAlignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v38ROIAlignE) *#include <roi_align.hpp>*[ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_r_o_i_align)operation.Public Functions

-
ROIAlign(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &batch_indices, const int pooled_h, const int pooled_w, const int sampling_ratio, const float spatial_scale, const std::string &mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v38ROIAlign8ROIAlignERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKiKiKiKfRKNSt6stringE) Constructs a

[ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_r_o_i_align)node matching the ONNX[ROIAlign](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_r_o_i_align)specification Check[util::ROIAlignBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_r_o_i_align_base)for description of common params.- Parameters:
**mode**– Method of pooling - ‘avg’ or ‘max’


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v38ROIAlign24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v38ROIAlign12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ROIAlign(const

-
class ROIAlignRotated : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ROIAlignBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_r_o_i_align_base.html#_CPPv4N2ov2op4util12ROIAlignBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1515ROIAlignRotatedE) *#include <roi_align_rotated.hpp>*[ROIAlignRotated](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_r_o_i_align_rotated)operation.Public Functions

-
ROIAlignRotated(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &rois, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &batch_indices, const int pooled_h, const int pooled_w, const int sampling_ratio, const float spatial_scale, const bool clockwise_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1515ROIAlignRotated15ROIAlignRotatedERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKiKiKiKfKb) Constructs a

[ROIAlignRotated](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_r_o_i_align_rotated)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)feature map {N, C, H, W}**rois**– Regions of interest to pool over**batch_indices**– Indices of images in the batch matching the number or ROIs**pooled_h**– Height of the ROI output features**pooled_w**– Width of the ROI output features**sampling_ratio**– Number of sampling points used to compute an output element**spatial_scale**– Spatial scale factor used to translate ROI coordinates**clockwise_mode**– If true, rotation angle is interpreted as clockwise, otherwise as counterclockwise



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1515ROIAlignRotated24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ROIAlignRotated(const

-
class ROIPooling : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPoolingE) *#include <roi_pooling.hpp>*[ROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_o_i_pooling)operation.Public Functions

-
ROIPooling(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &coords, const[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&output_size, const float spatial_scale, const std::string &method = "max")[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling10ROIPoolingERK6OutputI4NodeERK6OutputI4NodeERK5ShapeKfRKNSt6stringE) Constructs a

[ROIPooling](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_r_o_i_pooling)operation.- Parameters:
**input**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)feature map {N, C, H, W}**coords**– Coordinates of bounding boxes**output_size**– Height/Width of ROI output features**spatial_scale**– Ratio of input feature map over input image size**method**– Method of pooling - Max or Bilinear



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
void set_output_roi(
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)output_size)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling14set_output_roiE5Shape) Set the output ROI feature map (pooled_h, pooled_w).

- Parameters:
**output_size**–[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)with pooling attributes pooled_h and pooled_w sizes.


-
const
[Shape](https://docs.openvino.ai/classov_1_1_shape.html#_CPPv4N2ov5ShapeE)&get_output_roi() const[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v010ROIPooling14get_output_roiEv) Get the output ROI feature map shape (H x W)

- Returns:
[Shape](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_shape)with pooled_h and pooled_w attributes.


-
void set_spatial_scale(float scale)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling17set_spatial_scaleEf) Set the spatial scale value.

- Parameters:
**scale**– Scale value to set.


-
void set_method(std::string method_name)
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v010ROIPooling10set_methodENSt6stringE) Set the method of pooling.

- Parameters:
**method_name**– Pooling method name.


-
ROIPooling(const

-
class Roll : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74RollE) *#include <roll.hpp>*[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)roll operation.Public Functions

-
Roll(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &shift, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74Roll4RollERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a roll operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v74Roll24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Roll(const

-
class Round : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v55RoundE) *#include <round.hpp>*Elementwise round operation. The output is round to the nearest integer for each value. In case of halfs, the rule is defined in attribute ‘mode’: ‘HALF_TO_EVEN’ - round halfs to the nearest even integer. ‘HALF_AWAY_FROM_ZERO’: - round in such a way that the result heads away from zero.

Public Functions

-
Round() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v55Round5RoundEv) Constructs a round operation.


-
Round(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const RoundMode mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v55Round5RoundERK6OutputI4NodeEK9RoundMode) Constructs a round operation.

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the input tensor.**mode**– Rule to resolve halfs



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v55Round24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v55Round12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Round() = default

-
class ScaledDotProductAttention : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1325ScaledDotProductAttentionE) *#include <scaled_dot_product_attention.hpp>*Scaled dot product attention operation from PyTorch.

Public Functions

-
ScaledDotProductAttention() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1325ScaledDotProductAttention25ScaledDotProductAttentionEv) Constructs a

[ScaledDotProductAttention](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v13_1_1_scaled_dot_product_attention)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1325ScaledDotProductAttention24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
ScaledDotProductAttention() = default

-
class ScatterElementsUpdate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ScatterElementsUpdateBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_scatter_elements_update_base.html#_CPPv4N2ov2op4util25ScatterElementsUpdateBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321ScatterElementsUpdateE) *#include <scatter_elements_update.hpp>*[ScatterElementsUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_scatter_elements_update)operation.Public Functions

-
ScatterElementsUpdate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v321ScatterElementsUpdate21ScatterElementsUpdateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[ScatterElementsUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_scatter_elements_update)node.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**indices**– Data entry index that will be updated**updates**– Update values**axis**– Axis to scatter on



-
ScatterElementsUpdate(const

-
class ScatterNDUpdate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ScatterNDBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_scatter_n_d_base.html#_CPPv4N2ov2op4util13ScatterNDBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v315ScatterNDUpdateE) *#include <scatter_nd_update.hpp>*Add updates to slices from inputs addressed by indices.

Public Functions

-
inline ScatterNDUpdate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &inputs, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v315ScatterNDUpdate15ScatterNDUpdateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) - Parameters:
**inputs**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)**indices**– Index tensor: Data type must be

or[element::i32](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga53dd97bfbd724cee3266cc80d758f323)[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)**updates**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor): Must have same type as inputs



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v315ScatterNDUpdate12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline ScatterNDUpdate(const

-
class ScatterNDUpdate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ScatterNDBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_scatter_n_d_base.html#_CPPv4N2ov2op4util13ScatterNDBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1515ScatterNDUpdateE) *#include <scatter_nd_update.hpp>*Add updates to slices from inputs addressed by indices.

Public Types

Public Functions

-
ScatterNDUpdate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &inputs, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Reduction](https://docs.openvino.ai/classov_1_1op_1_1v15_1_1_scatter_n_d_update.html#_CPPv4N2ov2op3v1515ScatterNDUpdate9ReductionE)reduction =[Reduction](https://docs.openvino.ai/classov_1_1op_1_1v15_1_1_scatter_n_d_update.html#_CPPv4N2ov2op3v1515ScatterNDUpdate9ReductionE)::[NONE](https://docs.openvino.ai/classov_1_1op_1_1v15_1_1_scatter_n_d_update.html#_CPPv4N2ov2op3v1515ScatterNDUpdate9Reduction4NONEE))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1515ScatterNDUpdate15ScatterNDUpdateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEK9Reduction) - Parameters:
**inputs**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)**indices**– Index tensor: Data type must be

or[element::i32](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga53dd97bfbd724cee3266cc80d758f323)[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)**updates**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor): Must have same type as inputs**reduction**– Reduction: Type of operation to perform on inputs



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v1515ScatterNDUpdate12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ScatterNDUpdate(const

-
class ScatterUpdate : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ScatterBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_scatter_base.html#_CPPv4N2ov2op4util11ScatterBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v313ScatterUpdateE) *#include <scatter_update.hpp>*Set new values to slices from data addressed by indices.

Public Functions

-
ScatterUpdate(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v313ScatterUpdate13ScatterUpdateERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs

[ScatterUpdate](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_scatter_update)operator object.- Parameters:
**data**– The input tensor to be updated.**indices**– The tensor with indexes which will be updated.**updates**– The tensor with update values.**axis**–**[in]**The axis at which elements will be updated.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v313ScatterUpdate12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ScatterUpdate(const

-
class SearchSorted : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SearchSortedE) *#include <search_sorted.hpp>*[SearchSorted](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_search_sorted)operation.Public Functions

-
SearchSorted(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &sorted_sequence, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &values, bool right_mode = false, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&output_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SearchSorted12SearchSortedERK6OutputI4NodeERK6OutputI4NodeEbRKN7element4TypeE) Constructs a

[SearchSorted](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_search_sorted)operation.- Parameters:
**sorted_sequence**– Sorted sequence to search in.**values**– Values to search indexs for.**right_mode**– If False, return the first suitable index that is found for given value. If True, return the last such index.**output_type**– The element type of the output tensor. This is purely an implementation flag, which is used to convert the output type for CPU plugin in ConvertPrecision transformation (and potentially other plugins as well). Setting this flag to[element::i32](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga53dd97bfbd724cee3266cc80d758f323)will result in the output tensor of i32 element type. Setting this flag to[element::i64](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga6c86a9a54d44fc205ad9cbf28ca556a6)will generally not give any effect, since it will be converted to i32 anyway, at least for CPU plugin.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SearchSorted24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
SearchSorted(const

-
class SegmentMax : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1610SegmentMaxE) *#include <segment_max.hpp>*An operation which computes the maximum values along segments of a tensor.

Public Functions

-
SegmentMax(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &segment_ids, const[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[FillMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op8FillModeE)fill_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1610SegmentMax10SegmentMaxERK6OutputI4NodeERK6OutputI4NodeEKN2op8FillModeE) Constructs a

[SegmentMax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_segment_max)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**segment_ids**– Indices of segments in the data input tensor**fill_mode**– The value assigned to segments which are empty



-
SegmentMax(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &segment_ids, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &num_segments, const[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[FillMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op8FillModeE)fill_mode)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1610SegmentMax10SegmentMaxERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKN2op8FillModeE) Constructs a

[SegmentMax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_segment_max)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**segment_ids**– Indices of segments in the data input tensor**num_segments**– The segments count**fill_mode**– The value assigned to segments which are empty



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1610SegmentMax24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
SegmentMax(const

-
class Select : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16SelectE) *#include <select.hpp>*Elementwise selection operation.

*Inputs*Type

Description

`arg0`

\(\texttt{bool}[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape, with element

`bool`

.`arg1`

\(E[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of a shape that is broadcast-compatible with

`arg0`

, with any element type.`arg2`

\(E[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of a shape that is broadcast-compatible with

`arg0`

, and same element type as`arg1`

.`auto_broadcast`

Auto broadcast specification.

Type

Description

\(E[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \texttt{arg1}[i_1,\dots,i_n]\text{ if }\texttt{arg0}[i_1,\dots,i_n] \neq 0\text{, else }\texttt{arg2}[i_1,\dots,i_n]\)

Public Functions

-
inline Select()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Select6SelectEv) Constructs a selection operation.


-
Select(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg2, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Select6SelectERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a selection operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v16Select24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual const
[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&get_autob() const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v16Select9get_autobEv) - Returns:
the autobroadcasr spec



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v16Select12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline Select()

-
class Selu : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04SeluE) *#include <selu.hpp>*Performs a SELU activation function on all elements of the input node.

Public Functions

-
Selu(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &alpha, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &lambda)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Selu4SeluERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[Selu](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_selu)node.- Parameters:
**data**– -[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor**alpha**– - Alpha coefficient of SELU operation**lambda**– - Lambda coefficient of SELU operation



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Selu24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Selu(const

-
class ShapeOf : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ShapeOfBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_shape_of_base.html#_CPPv4N2ov2op4util11ShapeOfBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37ShapeOfE) *#include <shape_of.hpp>*Operation that returns the shape of its input argument as a tensor.

Public Functions

-
ShapeOf(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)output_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37ShapeOf7ShapeOfERK6OutputI4NodeEKN7element4TypeE) Constructs a shape-of operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v37ShapeOf24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v37ShapeOf12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ShapeOf(const

-
class ShapeOf : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[ShapeOfBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_shape_of_base.html#_CPPv4N2ov2op4util11ShapeOfBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07ShapeOfE) *#include <shape_of.hpp>*Operation that returns the shape of its input argument as a tensor.

Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07ShapeOf24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v07ShapeOf12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual void validate_and_infer_types() override

-
class ShuffleChannels : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ShuffleChannelsE) *#include <shuffle_channels.hpp>*Permutes data in the channel dimension of the input.

Public Functions

-
ShuffleChannels(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const int64_t axis = 1, const int64_t group = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ShuffleChannels15ShuffleChannelsERK6OutputI4NodeEK7int64_tK7int64_t) Constructs a

[ShuffleChannels](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_shuffle_channels)node.- Parameters:
**data**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor.**axis**– Channel dimension index in the data tensor. A negative value means that the index should be calculated from the back of the input data shape.**group**– Number of group the channel dimension should be split into.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v015ShuffleChannels24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v015ShuffleChannels12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
ShuffleChannels(const

-
class Sigmoid : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07SigmoidE) *#include <sigmoid.hpp>*[Sigmoid](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_sigmoid)operation.Public Functions

-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v07Sigmoid12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual bool has_evaluate() const override

-
class Sign : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04SignE) *#include <sign.hpp>*Elementwise sign operation.


-
class Sin : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03SinE) *#include <sin.hpp>*Elementwise sine operation.

*Inputs*Type

Description

`arg`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and numeric element type.

Type

Description

\(N[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \sin(\texttt{arg}[i_1,\dots,i_n])\)


-
class Sinh : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04SinhE) *#include <sinh.hpp>*Elementwise hyperbolic sine (sinh) operation.


-
class Sink : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4SinkE) *#include <sink.hpp>*Root of nodes that can be sink nodes.

Subclassed by

[ov::op::util::AssignBase](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_assign_base),[ov::op::util::MultiSubGraphOp](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1util_1_1_multi_sub_graph_op)

-
class Slice : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v85SliceE) *#include <slice.hpp>*[Slice](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_slice)operation.Public Functions

-
Slice(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v85Slice5SliceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs

[Slice](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_slice)operation (default axes).- Parameters:
**data**– The tensor to be sliced.**start**– 1D tensor with start indices of the slice.**stop**– 1D tensor with end indices of the slice.**step**– 1D tensor specifies the increment to use in slicing along corresponding axes.



-
Slice(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v85Slice5SliceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs

[Slice](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_slice)operation.- Parameters:
**data**– The tensor to be sliced.**start**– 1D tensor with start indices of the slice.**stop**– 1D tensor with end indices of the slice.**step**– 1D tensor specifies the increment to use in slicing along corresponding axes.**axes**– 1D tensor indicating which dimensions the values in the`start`

and`stop`

apply to.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v85Slice24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v85Slice12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Slice(const

-
class SliceScatter : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SliceScatterE) *#include <slice_scatter.hpp>*[SliceScatter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_slice_scatter)operation.Public Functions

-
SliceScatter(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SliceScatter12SliceScatterERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs

[SliceScatter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_slice_scatter)operation (default axes).- Parameters:
**data**– The tensor to be updated.**updates**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)containing update values.**start**– 1D tensor with start indices of the update slice.**stop**– 1D tensor with end indices of the update slice.**step**– 1D tensor specifies the increment to use in slicing along corresponding axes.



-
SliceScatter(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &updates, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &start, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &stop, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &step, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SliceScatter12SliceScatterERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs

[SliceScatter](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_slice_scatter)operation.- Parameters:
**data**– The tensor to be updated.**updates**–[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)containing update values.**start**– 1D tensor with start indices of the update slice.**stop**– 1D tensor with end indices of the update slice.**step**– 1D tensor specifies the increment to use in slicing along corresponding axes.**axes**– 1D tensor indicating which dimensions the values in the`start`

and`stop`

apply to.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1512SliceScatter24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
SliceScatter(const

-
class Softmax : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17SoftmaxE) *#include <softmax.hpp>*[Softmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_softmax)operation.Public Functions

-
Softmax(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const size_t axis = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Softmax7SoftmaxERK6OutputI4NodeEK6size_t) Constructs a softmax operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the first input tensor.`[d0, ...]`

**axis**– The axis position (0-based) on which to calculate the softmax.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v17Softmax24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v17Softmax12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Softmax(const

-
class Softmax : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87SoftmaxE) *#include <softmax.hpp>*[Softmax](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v8_1_1_softmax)operation with negative axis values.Public Functions

-
Softmax(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const int64_t axis = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87Softmax7SoftmaxERK6OutputI4NodeEK7int64_t) Constructs a softmax operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`

- Parameters:
**arg**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)that produces the first input tensor.`[d0, ...]`

**axis**– The axis position (0-based) in range [-rank(arg), rank(arg) - 1] on which to calculate the softmax.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v87Softmax24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v87Softmax12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Softmax(const

-
class SoftPlus : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48SoftPlusE) *#include <softplus.hpp>*A Self Regularized Non-Monotonic Neural Activation Function f(x) = ln(exp(x) + 1.)

Public Functions

-
SoftPlus(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48SoftPlus8SoftPlusERK6OutputI4NodeE) Constructs an

[SoftPlus](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_soft_plus)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v48SoftPlus24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v48SoftPlus12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
SoftPlus(const

-
class SpaceToBatch : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112SpaceToBatchE) *#include <space_to_batch.hpp>*[SpaceToBatch](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_space_to_batch)permutes data tensor blocks of spatial data into batch dimension.Note

Values from spatial blocks dimensions are moved in the batch dimension.

Output node produces a tensor with shape: tensor with shape `[batch * block_shape[0] * block_shape[1] * ... * block_shape[N - 1], (pads_begin[1] + D_1 + pads_end[1]) / block_shape[1], (pads_begin[2] + D_2 + pads_end[2]) / block_shape[2], ..., (pads_begin[N - 1] + D_{N - 1} + pads_end[N - 1]) / block_shape[N - 1]` of the same type as `data` input.

Public Functions

-
SpaceToBatch(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &block_shape, const[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_begin, const[Output](https://docs.openvino.ai/classov_1_1_output.html#_CPPv4I0EN2ov6OutputE)<[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &pads_end)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112SpaceToBatch12SpaceToBatchERK6OutputI4NodeERK6OutputI4NodeERK6OutputIN2ov4NodeEERK6OutputIN2ov4NodeEE) Constructs a

[SpaceToBatch](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_space_to_batch)operation.- Parameters:
**data**–[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the data tensor**block_shape**– The sizes of the block of values to be moved**pads_begin**– Specifies the padding for the beginning along each axis of`data`

input**pads_end**– Specifies the padding for the ending along each axis of`data`

input.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112SpaceToBatch24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v112SpaceToBatch12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
SpaceToBatch(const

-
class SpaceToDepth : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012SpaceToDepthE) *#include <space_to_depth.hpp>*[SpaceToDepth](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_space_to_depth)permutes input tensor blocks of spatial data into depth dimension.Note

Values from the height and width dimensions are moved to the depth dimension.

Output node produces a tensor with shape: [N, C * blocksize * blocksize, H / blocksize, W / blocksize]

Public Functions

-
SpaceToDepth(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const SpaceToDepthMode &mode, std::size_t block_size = 1)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012SpaceToDepth12SpaceToDepthERK6OutputI4NodeERK16SpaceToDepthModeNSt6size_tE) Constructs a

[SpaceToDepth](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_space_to_depth)operation.- Parameters:
**data**– -[Node](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_node)producing the input tensor**mode**– Specifies how the output depth dimension is gathered from block coordinates and the old depth dimension.**block_size**– - the size of the block of values to be moved



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v012SpaceToDepth24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v012SpaceToDepth12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
SpaceToDepth(const

-
class SparseFillEmptyRows : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1619SparseFillEmptyRowsE) *#include <sparse_fill_empty_rows.hpp>*An operation which fills empty rows of a sparse tensor with a default value.

Public Functions

-
SparseFillEmptyRows(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &indices, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &values, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &dense_shape, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &default_value)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1619SparseFillEmptyRows19SparseFillEmptyRowsERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[SparseFillEmptyRows](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v16_1_1_sparse_fill_empty_rows)operation.- Parameters:
**indices**– 2D tensor indicating the positions of values in the sparse tensor.**values**– 1D tensor containing the values to be inserted at the specified indices.**dense_shape**– 1D tensor indicating the shape of the 2D dense tensor.**default_value**– Scalar value to be inserted into the empty rows.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1619SparseFillEmptyRows24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
SparseFillEmptyRows(const

-
class Split : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15SplitE) *#include <split.hpp>*Splits the input tensor into a list of equal sized tensors.

Public Functions

-
Split() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Split5SplitEv) Constructs a split operation.


-
Split(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const size_t num_splits)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Split5SplitERK6OutputI4NodeERK6OutputI4NodeEK6size_t) Constructs a split operation.

- Parameters:
**data**– The tensor to be split.**axis**– The index of an axis in “data” along which to perform the split.**num_splits**– The number of pieces that the data tensor should be split into.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v15Split24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v15Split12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Split() = default

-
class Sqrt : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04SqrtE) *#include <sqrt.hpp>*Elementwise square root operation.

*Inputs*Type

Description

`arg`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and numeric element type.

Type

Description

\(N[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \sqrt{\texttt{arg}[i_1,\dots,i_n]}\)


-
class SquaredDifference : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v017SquaredDifferenceE) *#include <squared_difference.hpp>*Calculates an element-wise squared difference between two tensors.

y[i] = (x1[i] - x2[i])^2

Public Functions

-
inline SquaredDifference()
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v017SquaredDifference17SquaredDifferenceEv) Constrcuts an uninitialized squared difference operation.


-
SquaredDifference(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &x1, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &x2, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v017SquaredDifference17SquaredDifferenceERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs the squared difference operation.

- Parameters:
**x1**– First input tensor**x2**– Second input tensor**auto_broadcast**– Auto broadcast specification



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v017SquaredDifference12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
inline SquaredDifference()

-
class Squeeze : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[SqueezeBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_squeeze_base.html#_CPPv4N2ov2op4util11SqueezeBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07SqueezeE) *#include <squeeze.hpp>*[Squeeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_squeeze)operation.Public Functions

-
Squeeze(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Squeeze7SqueezeERK6OutputI4NodeE) Constructs a squeeze

[v0](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v0)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data


-
Squeeze(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Squeeze7SqueezeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a squeeze

[v0](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v0)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**axis**– The axis along which to squeeze the input tensor.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v07Squeeze24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Squeeze(const

-
class Squeeze : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[SqueezeBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_squeeze_base.html#_CPPv4N2ov2op4util11SqueezeBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v157SqueezeE) *#include <squeeze.hpp>*[Squeeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_squeeze)operation.Public Functions

-
Squeeze(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const bool allow_axis_skip = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v157Squeeze7SqueezeERK6OutputI4NodeEKb) Constructs a squeeze

[v15](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v15)operation.

-
Squeeze(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes, const bool allow_axis_skip = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v157Squeeze7SqueezeERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a squeeze

[v15](https://docs.openvino.ai/group__ov__transformation__common__api.html#namespaceov_1_1op_1_1v15)operation.

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v157Squeeze24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Squeeze(const

-
class STFT : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v154STFTE) *#include <stft.hpp>*An operation

[STFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_s_t_f_t)that computes the Short Time Fourier Transform.Public Functions

-
STFT(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &window, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &frame_size, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &frame_step, const bool transpose_frames)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v154STFT4STFTERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeEKb) Constructs a

[STFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_s_t_f_t)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data**window**– Window to perform[STFT](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_s_t_f_t)**frame_size**– Scalar value representing the size of Fourier Transform**frame_step**– The distance (number of samples) between successive window frames**transpose_frames**– Flag to set output shape layout. If true the`frames`

dimension is at out_shape[2], otherwise it is at out_shape[1].



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v154STFT24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
STFT(const

-
class StridedSlice : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112StridedSliceE) *#include <strided_slice.hpp>*Takes a slice of an input tensor, i.e., the sub-tensor that resides within a bounding box, optionally with stride.

Public Functions

-
StridedSlice(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &end, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &strides, const std::vector<int64_t> &begin_mask, const std::vector<int64_t> &end_mask, const std::vector<int64_t> &new_axis_mask = std::vector<int64_t>{}, const std::vector<int64_t> &shrink_axis_mask = std::vector<int64_t>{}, const std::vector<int64_t> &ellipsis_mask = std::vector<int64_t>{})[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112StridedSlice12StridedSliceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEE) Constructs a dynamic tensor strided slice operation.

- Parameters:
**data**– The tensor to be sliced.**begin**– 1D tensor with begin indexes for input blob slicing.**end**– 1D tensor with end indexes for input blob slicing.**strides**– The slicing strides; for example, strides of`{n,m}`

means to take every nth row and every mth column of the input matrix.**begin_mask**– When begin_mask[i] equal to 1 means that the corresponding dimension of the begin input is ignored.**end_mask**– When end_mask[i] is 1, the corresponding dimension of the end input is ignored.**new_axis_mask**– If new_axis_mask[i] is 1, a length 1 dimension is inserted on the i-th position.**shrink_axis_mask**– If shrink_axis_mask[i] is 1, the dimension on the i-th position is deleted.**ellipsis_mask**– It inserts missing dimensions on a position of a non-zero bit.



-
StridedSlice(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &begin, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &end, const std::vector<int64_t> &begin_mask, const std::vector<int64_t> &end_mask, const std::vector<int64_t> &new_axis_mask = std::vector<int64_t>{}, const std::vector<int64_t> &shrink_axis_mask = std::vector<int64_t>{}, const std::vector<int64_t> &ellipsis_mask = std::vector<int64_t>{})[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112StridedSlice12StridedSliceERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEERKNSt6vectorI7int64_tEE) Constructs a dynamic tensor strided slice operation.

- Parameters:
**data**– The tensor to be sliced.**begin**– 1D tensor with begin indexes for input blob slicing.**end**– 1D tensor with end indexes for input blob slicing.**begin_mask**– When begin_mask[i] equal to 1 means that the corresponding dimension of the begin input is ignored.**end_mask**– When end_mask[i] is 1, the corresponding dimension of the end input is ignored.**new_axis_mask**– If new_axis_mask[i] is 1, a length 1 dimension is inserted on the i-th position.**shrink_axis_mask**– If shrink_axis_mask[i] is 1, the dimension on the i-th position is deleted.**ellipsis_mask**– It inserts missing dimensions on a position of a non-zero bit.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v112StridedSlice24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v112StridedSlice12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
StridedSlice(const

-
class StringTensorPack : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1516StringTensorPackE) *#include <string_tensor_pack.hpp>*Operator packing a concatenated batch of strings into a batched string tensor.

Public Functions

-
StringTensorPack(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &begins, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &ends, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &symbols)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1516StringTensorPack16StringTensorPackERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a

[StringTensorPack](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_string_tensor_pack)operation.- Parameters:
**begins**– Indices of each string’s beginnings**ends**– Indices of each string’s endings**symbols**– Concatenated input strings encoded in utf-8 bytes



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1516StringTensorPack24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
StringTensorPack(const

-
class StringTensorUnpack : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518StringTensorUnpackE) *#include <string_tensor_unpack.hpp>*Operator unpacking a batch of strings into three tensors.

Public Functions

-
StringTensorUnpack(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518StringTensorUnpack18StringTensorUnpackERK6OutputI4NodeE) Constructs a

[StringTensorUnpack](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_string_tensor_unpack)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)of type[element::string](https://docs.openvino.ai/group__ov__transformation__common__api.html#group__ov__element__cpp__api_1ga4460befbdeb69377360bdc52b2e61a25)


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v1518StringTensorUnpack24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
StringTensorUnpack(const

-
class Subtract : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_arithmetic.html#_CPPv4N2ov2op4util27BinaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18SubtractE) *#include <subtract.hpp>*Elementwise subtraction operation.

Public Functions

-
Subtract(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)([AutoBroadcastType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastTypeE)::[NUMPY](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op17AutoBroadcastType5NUMPYE)))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v18Subtract8SubtractERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a subtraction operation.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v18Subtract12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Subtract(const

-
class Swish : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45SwishE) *#include <swish.hpp>*A

[Swish](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_swish)Activation Function f(x) = x / (1.0 + exp(-beta * x)) or f(x) = x * sigmoid(beta * x)Public Functions

-
Swish(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &beta)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45Swish5SwishERK6OutputI4NodeERK6OutputI4NodeE) Constructs an

[Swish](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v4_1_1_swish)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor**beta**– Scalar with beta value. If the argument is not specified then use the default value 1.0



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v45Swish24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v45Swish12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Swish(const

-
class Tan : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03TanE) *#include <tan.hpp>*Elementwise tangent operation.

*Inputs*Type

Description

`arg`

\(N[d_1,\dots,d_n]~(n \geq 0)\)

A tensor of any shape and numeric element type.

Type

Description

\(N[d_1,\dots,d_n]\)

The tensor \(T\), where \(T[i_1,\dots,i_n] = \tan(\texttt{arg}[i_1,\dots,i_n])\)


-
class Tanh : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[UnaryElementwiseArithmetic](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_unary_elementwise_arithmetic.html#_CPPv4N2ov2op4util26UnaryElementwiseArithmeticE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04TanhE) *#include <tanh.hpp>*Elementwise hyperbolic tangent operation.


-
class TensorIterator : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[SubGraphOp](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_sub_graph_op.html#_CPPv4N2ov2op4util10SubGraphOpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v014TensorIteratorE) *#include <tensor_iterator.hpp>*Iterate a body over tensors, accumulating into tensors.

Public Functions

- Parameters:
**body**– set the body of the iteration


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v014TensorIterator24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.



-
class Tile : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04TileE) *#include <tile.hpp>*Dynamic Tiling operation which repeats a tensor multiple times along each dimension.

Public Functions

-
Tile(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &repeats)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Tile4TileERK6OutputI4NodeERK6OutputI4NodeE) Perform dynamic padding of a tensor.

- Parameters:
**data**– The node producing input tensor to be padded.**repeats**– The node producing the per-dimension replication factor



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v04Tile24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Tile12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v04Tile8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
Tile(const

-
class TopK : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[TopKBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_top_k_base.html#_CPPv4N2ov2op4util8TopKBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v14TopKE) *#include <topk.hpp>*Computes indices and values of the k maximum/minimum values for each slice along specified axis.

Public Functions

-
TopK(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &k, const int64_t axis, const std::string &mode, const std::string &sort, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v14TopK4TopKERK6OutputI4NodeERK6OutputI4NodeEK7int64_tRKNSt6stringERKNSt6stringERKN7element4TypeE) Constructs a

[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_top_k)operation with two outputs: values and indices. By default the indices output is described by i32 data type.- Parameters:
**data**– The input tensor**k**– Specifies how many maximum/minimum elements should be computed (note: scalar input tensor)**axis**– The axis along which to compute top k indices**mode**– Specifies which operation (min or max) is used to select the biggest element of two.**sort**– Specifies order of output elements and/or indices Accepted values: none, index, value**index_element_type**– Specifies type of produced indices



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v14TopK12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
TopK(const

-
class TopK : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[TopKBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_top_k_base.html#_CPPv4N2ov2op4util8TopKBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v34TopKE) *#include <topk.hpp>*Computes indices and values of the k maximum/minimum values for each slice along specified axis.

Public Functions

-
TopK(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &k, const int64_t axis, const std::string &mode, const std::string &sort, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E))[#](https://docs.openvino.ai#_CPPv4N2ov2op2v34TopK4TopKERK6OutputI4NodeERK6OutputI4NodeEK7int64_tRKNSt6stringERKNSt6stringERKN7element4TypeE) Constructs a

[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v3_1_1_top_k)operation with two outputs: values and indices. By default the indices output is described by i32 data type.- Parameters:
**data**– The input tensor**k**– Specifies how many maximum/minimum elements should be computed (note: scalar input tensor)**axis**– The axis along which to compute top k indices**mode**– Specifies which operation (min or max) is used to select the biggest element of two.**sort**– Specifies order of output elements and/or indices Accepted values: none, index, value**index_element_type**– Specifies type of produced indices



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v34TopK12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
TopK(const

-
class TopK : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[TopKBase](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_top_k_base.html#_CPPv4N2ov2op4util8TopKBaseE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v114TopKE) *#include <topk.hpp>*Computes the top K elements of a given tensor along the specified axis.

Public Functions

-
TopK(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &k, const int64_t axis, const std::string &mode, const std::string &sort, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E), const bool stable = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v114TopK4TopKERK6OutputI4NodeERK6OutputI4NodeEK7int64_tRKNSt6stringERKNSt6stringERKN7element4TypeEKb) Constructs a

[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)operation with two outputs: values and indices.- Parameters:
**data**– The input tensor**k**– Specifies how many maximum/minimum elements should be computed**axis**– The axis along which the[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)operation should be executed**mode**– Specifies whether[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)selects the largest or the smallest elements from each slice**sort**– Specifies the order of corresponding elements of the output tensor**index_element_type**– Specifies the data type of the elements in the ‘indices’ output tensor.**stable**– Specifies whether the equivalent elements should maintain their relative order from the input tensor during sorting.



-
TopK(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &k, const int64_t axis, const[TopKMode](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op8TopKModeE)mode, const[TopKSortType](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op12TopKSortTypeE)sort, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i32](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i32EN6Type_t3i32E), const bool stable = false)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v114TopK4TopKERK6OutputI4NodeERK6OutputI4NodeEK7int64_tK8TopKModeK12TopKSortTypeRKN7element4TypeEKb) Constructs a

[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)operation with two outputs: values and indices.- Parameters:
**data**– The input tensor**k**– Specifies how many maximum/minimum elements should be computed**axis**– The axis along which the[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)operation should be executed**mode**– Specifies whether[TopK](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v11_1_1_top_k)selects the largest or the smallest elements from each slice**sort**– Specifies the order of corresponding elements of the output tensor**index_element_type**– Specifies the data type of the elements in the ‘indices’ output tensor.**stable**– Specifies whether the equivalent elements should maintain their relative order from the input tensor during sorting.



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v114TopK24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op3v114TopK12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
TopK(const

-
class Transpose : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19TransposeE) *#include <transpose.hpp>*[Tensor](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_tensor)transpose operation.Public Types

Public Functions

-
Transpose(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &input_order)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Transpose9TransposeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a transpose operation.


-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v19Transpose24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v19Transpose12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Transpose(const

-
class Unique : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op3v106UniqueE) *#include <unique.hpp>*Operator which selects and returns unique elements or unique slices of the input tensor.

Public Functions

-
Unique(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const bool sorted = true, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E), const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&count_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v106Unique6UniqueERK6OutputI4NodeEKbRKN7element4TypeERKN7element4TypeE) Constructs a

[Unique](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_unique)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data tensor**sorted**– Controls the order of the returned unique values (sorts ascendingly when true)**index_element_type**– The data type for outputs containing indices**count_element_type**– The data type for output containing repetition count



-
Unique(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const bool sorted = true, const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&index_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E), const[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[Type](https://docs.openvino.ai/classov_1_1element_1_1_type.html#_CPPv4N2ov7element4TypeE)&count_element_type =[element](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7elementE)::[i64](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov7element3i64EN6Type_t3i64E))[#](https://docs.openvino.ai#_CPPv4N2ov2op3v106Unique6UniqueERK6OutputI4NodeERK6OutputI4NodeEKbRKN7element4TypeERKN7element4TypeE) Constructs a

[Unique](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v10_1_1_unique)operation.- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)data tensor**axis**– An input tensor containing the axis value**sorted**– Controls the order of the returned unique values (sorts ascendingly when true)**index_element_type**– The data type for outputs containing indices**count_element_type**– The data type for output containing repetition count



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op3v106Unique24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
Unique(const

-
class Unsqueeze : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09UnsqueezeE) *#include <unsqueeze.hpp>*[Unsqueeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_unsqueeze)operation.Public Functions

-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v09Unsqueeze24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
virtual bool evaluate(
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &outputs, const[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::TensorVector &inputs) const override[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v09Unsqueeze8evaluateERN2ov12TensorVectorERKN2ov12TensorVectorE) Evaluates the op on input_values putting results in output_values.

- Parameters:
**output_values**– Tensors for the outputs to compute. One for each result**input_values**– Tensors for the inputs. One for each inputs.

- Returns:
true if successful



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v09Unsqueeze12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
virtual void validate_and_infer_types() override

-
class SqueezeBase : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11SqueezeBaseE) *#include <squeeze_base.hpp>*Squeeze operation.

Subclassed by

[ov::op::v0::Squeeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v0_1_1_squeeze),[ov::op::v15::Squeeze](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v15_1_1_squeeze)Public Functions

-
SqueezeBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11SqueezeBase11SqueezeBaseERK6OutputI4NodeE) Constructs a squeeze operation.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data


-
SqueezeBase(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axes)[#](https://docs.openvino.ai#_CPPv4N2ov2op4util11SqueezeBase11SqueezeBaseERK6OutputI4NodeERK6OutputI4NodeE) Constructs a squeeze operation.

- Parameters:
**data**–[Input](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_input)tensor with data**axis**– The axis along which to squeeze the input tensor.



-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op4util11SqueezeBase12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
SqueezeBase(const

-
class VariadicSplit : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[Op](https://docs.openvino.ai/classov_1_1op_1_1_op.html#_CPPv4N2ov2op2OpE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v113VariadicSplitE) *#include <variadic_split.hpp>*[VariadicSplit](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1op_1_1v1_1_1_variadic_split)operation splits an input tensor into pieces along some axis. The pieces may have variadic lengths depending on “split_lengths” attribute.Public Functions

-
VariadicSplit() = default
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v113VariadicSplit13VariadicSplitEv) Constructs a variadic split operation.


-
VariadicSplit(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &data, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &axis, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &split_lengths)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v113VariadicSplit13VariadicSplitERK6OutputI4NodeERK6OutputI4NodeERK6OutputI4NodeE) Constructs a variadic split operation.

outputs. The sum of split_lengths must match data.shape[axis]

- Parameters:
**data**– The tensor to be split.**axis**– The index of an axis in “data” along which to perform the split.**split_lengths**– A list containing the sizes of each output tensor along the split “axis”. Size of “split_lengths” should be equal to the number of



-
virtual void validate_and_infer_types() override
[#](https://docs.openvino.ai#_CPPv4N2ov2op2v113VariadicSplit24validate_and_infer_typesEv) Verifies that attributes and inputs are consistent and computes output shapes and element types. Must be implemented by concrete child classes so that it can be run any number of times.

Throws if the node is invalid.


-
inline virtual size_t get_default_output_index() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v113VariadicSplit24get_default_output_indexEv) Returns the output of the default output, or throws if there is none.


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v113VariadicSplit12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
VariadicSplit() = default

-
class Xor : public
[ov](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv42ov)::[op](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2opE)::[util](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4N2ov2op4utilE)::[BinaryElementwiseLogical](https://docs.openvino.ai/classov_1_1op_1_1util_1_1_binary_elementwise_logical.html#_CPPv4N2ov2op4util24BinaryElementwiseLogicalE)[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03XorE) *#include <xor.hpp>*Elementwise logical-xor operation.

Public Functions

-
Xor(const
[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg0, const[Output](https://docs.openvino.ai/group__ov__dev__exec__model.html#_CPPv4IEN2ov6OutputI4NodeEE)<[Node](https://docs.openvino.ai/classov_1_1_node.html#_CPPv4N2ov4NodeE)> &arg1, const[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)&auto_broadcast =[AutoBroadcastSpec](https://docs.openvino.ai/structov_1_1op_1_1_auto_broadcast_spec.html#_CPPv4N2ov2op17AutoBroadcastSpecE)())[#](https://docs.openvino.ai#_CPPv4N2ov2op2v03Xor3XorERK6OutputI4NodeERK6OutputI4NodeERK17AutoBroadcastSpec) Constructs a logical-xor operation.

[Output](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_output)`[d0, ...]`


-
virtual bool has_evaluate() const override
[#](https://docs.openvino.ai#_CPPv4NK2ov2op2v03Xor12has_evaluateEv) Allows to get information about availability of evaluate method for the current operation.


-
Xor(const

-
class AUGRUCell : public