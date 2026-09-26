source: https://docs.openvino.ai/2025/api/c_cpp_api/classov_1_1_dimension.html
lastmod: 

# Class ov::Dimension[#](https://docs.openvino.ai#class-ov-dimension)

-
class Dimension
[#](https://docs.openvino.ai#_CPPv4N2ov9DimensionE) Class representing a dimension, which may be dynamic (undetermined until runtime), in a shape or shape-like object.

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
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&dim) const[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension11same_schemeERK9Dimension) Check whether this dimension represents the same scheme as the argument (both dynamic, or equal).

- Parameters:
**dim**– The other dimension to compare this dimension to.- Returns:
`true`

if this dimension and`dim`

are both dynamic, or if they are both static and equal; otherwise,`false`

.


-
bool compatible(const
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&d) const[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension10compatibleERK9Dimension) Check whether this dimension is capable of being merged with the argument dimension.

Two dimensions are considered compatible if it is possible to merge them. (See

[Dimension::merge](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension_1aef570cc1ebefa3e2b63fe91e4a600e5d).)- Parameters:
**d**– The dimension to compare this dimension with.- Returns:
`true`

if this dimension is compatible with`d`

, else`false`

.


-
bool relaxes(const
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&d) const[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension7relaxesERK9Dimension) Check whether this dimension is a relaxation of the argument.

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
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&d) const[#](https://docs.openvino.ai#_CPPv4NK2ov9Dimension7refinesERK9Dimension) Check whether this dimension is a refinement of the argument.

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
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)operator+(const[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&dim) const[#](https://docs.openvino.ai#_CPPv4NK2ov9DimensionplERK9Dimension) Addition operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for addition.- Returns:
Smallest interval dimension enclosing inputs



-
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)operator-(const[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&dim) const[#](https://docs.openvino.ai#_CPPv4NK2ov9DimensionmiERK9Dimension) Subtraction operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for subtraction.- Returns:
Smallest interval dimension enclosing inputs



-
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)operator/(const value_type divisor) const[#](https://docs.openvino.ai#_CPPv4NK2ov9DimensiondvEK10value_type) Division operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension)divided by a value_type parameter.- Parameters:
**divisor**– Right operand for division.- Returns:
Smallest interval dimension enclosing inputs



-
inline
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&operator/=(const value_type divisor)[#](https://docs.openvino.ai#_CPPv4N2ov9DimensiondVEK10value_type) Divided-into operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**divisor**– Right operand for multiplication.- Returns:
A reference to

`*this`

, after updating`*this`

to the value`*this * dim`

.


-
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)operator*(const[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&dim) const[#](https://docs.openvino.ai#_CPPv4NK2ov9DimensionmlERK9Dimension) Multiplication operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for multiplicaiton.- Returns:
Smallest interval containing all “produces” which are 0 if either of

`this`

or`dim`

has length`0`

, else unbounded if either is unbounded, else product of lengths.


-
inline
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&operator+=(const[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&dim)[#](https://docs.openvino.ai#_CPPv4N2ov9DimensionpLERK9Dimension) Add-into operator for

[Dimension](https://docs.openvino.ai/group__ov__transformation__common__api.html#classov_1_1_dimension).- Parameters:
**dim**– Right operand for addition.- Returns:
A reference to

`*this`

, after updating`*this`

to the value`*this + dim`

.


-
inline
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&operator*=(const[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&dim)[#](https://docs.openvino.ai#_CPPv4N2ov9DimensionmLERK9Dimension) Multiply-into operator for

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
[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&dst, const[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&d1, const[Dimension](https://docs.openvino.ai#_CPPv4N2ov9DimensionE)&d2)[#](https://docs.openvino.ai#_CPPv4N2ov9Dimension5mergeER9DimensionRK9DimensionRK9Dimension) Try to merge two

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